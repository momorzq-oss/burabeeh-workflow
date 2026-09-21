import sys,pathlib,json,hashlib
import torch
from safetensors import safe_open
from safetensors.torch import load_file,save_file
torch.set_num_threads(4)
import argparse
p=argparse.ArgumentParser();p.add_argument('--models',required=True);p.add_argument('--helper',required=True);args=p.parse_args()
tool=pathlib.Path(args.helper);sys.path.insert(0,str(tool))
from pdd_acc_core import rebase_adaln_to_curve,table_sha
from bake_pdd_trunk import _find_basis as match_adaln_basis
root=pathlib.Path(args.models);base=root/'diffusion_models/minimax_h3_hybrid_fl2va_ref2va_b25-49-int8.safetensors';src=root/'loras/lightx2v_hybrid-4to8step-Turbo_r48.safetensors';dst=root/'loras/lightx2v_hybrid-4to8step-Turbo_r48_b25_curve_compatible.safetensors'
with safe_open(str(base),framework='pt',device='cpu') as f:table=f.get_tensor('adaln_t_table')
c,V,note=match_adaln_basis(table);print(note,flush=True)
data=load_file(str(src));renamed={}
for k,v in data.items():
 if '.adaln_proj.linear.' in k:k=k.replace('.lora_down.weight','.lora_A.weight').replace('.lora_up.weight','.lora_B.weight')
 renamed[k]=v
converted,count=rebase_adaln_to_curve(renamed,c,V)
assert count==51,count
checks=[]
for k in renamed:
 if not k.endswith('.adaln_proj.linear.lora_A.weight'):continue
 mod=k[:-len('.lora_A.weight')];A=renamed[k].double();B=renamed[mod+'.lora_B.weight'].double();scale=float(renamed.get(mod+'.alpha',A.shape[0]))/A.shape[0]
 coords=table[[0,512,1024]].double();emb=c.double()[None,:]+coords@V.double().T
 original=(emb@A.T)@B.T*scale
 after=coords@converted[mod+'.diff'].double().T+converted[mod+'.diff_b'].double()[None,:]
 residual=float((after-original).norm()/original.norm().clamp_min(1e-12));assert residual<2e-5,(mod,residual);checks.append(residual)
save_file(converted,str(dst),metadata={'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'adaptation':'51 AdaLN modules projected into matching H3 curve coordinates including mandatory affine bias term; other adapter tensors unchanged. No PDD head or schedule patches.','target_table_sha':table_sha(table),'basis':note})
h=hashlib.sha256(dst.read_bytes()).hexdigest()
report={'source_file':str(src),'output_file':str(dst),'sha256':h,'base_table_sha':table_sha(table),'basis':note,'modules_converted':count,'modules_dropped':0,'affine_bias_preserved':True,'sampled_numerical_checks':len(checks),'maximum_relative_error_on_reconstructed_basis':max(checks),'quality_status':'Local numerical compatibility adaptation; visual equivalence to tutorial not established.'}
dst.with_suffix('.adaptation.json').write_text(json.dumps(report,indent=2));print(json.dumps(report),flush=True)
