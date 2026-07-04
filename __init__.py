from .nodes import ConditioningKrea2Rebalance

NODE_CLASS_MAPPINGS = {
    "ConditioningKrea2RebalanceGen1": ConditioningKrea2Rebalance,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ConditioningKrea2RebalanceGen1": "Conditioning Krea2 Rebalance [GEN-1]",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
