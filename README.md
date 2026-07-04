## ComfyUI-ConditioningKrea2Rebalance

Originally made by @nova452<br>The first version of a conditioning optimizer with per layer weighting that offers IP-Adapter-like features for Krea 2 along with bypassing the built in quality diluation from the trained safety filter and also works as a means to unfilter the model.

Just clone this repo into `ComfyUI\custom_nodes`, restart ComfyUI and add `ConditioningKrea2RebalanceGen1` before Sampler:


    git clone https://github.com/Gourieff/ComfyUI-ConditioningKrea2Rebalance

---
If you want to generate smth with text, you'd better bypass this node or reduce multiplier to 0.5-1.
<br>Also you should bypass it if you need 100% quality of Krea-2.
