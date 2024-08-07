from typing import TYPE_CHECKING
import warnings


from bgpy.simulation_engine.policies.rov import ROV

if TYPE_CHECKING:
    from bgpy.simulation_engine import Announcement as Ann


class Pathend(ROV):
    """An Policy that deploys Pathend"""

    name: str = "Pathend"

    def __init__(self, *args, **kwargs) -> None:  # type: ignore
        warnings.warn(
            "Pathend is deprecated and will be removed in a future version. "
            "Use PathEnd instead. (The author of Path-End informed me that the"
            "Path-End name was spelled incorrectly, and changing the name "
            "breaks tests so for now it's just deprecated)",
            DeprecationWarning,
            stacklevel=2,
        )
        super().__init__(*args, **kwargs)  # type: ignore

    def _valid_ann(self, ann: "Ann", *args, **kwargs) -> bool:  # type: ignore
        """Returns announcement validity by checking pathend records"""

        origin_asn = ann.origin
        origin_as_obj = self.as_.as_graph.as_dict[origin_asn]
        # If the origin is deploying pathend and the path is longer than 1
        if isinstance(origin_as_obj.policy, Pathend) and len(ann.as_path) > 1:
            # If the provider is real, do the loop check
            # Mypy thinks this is unreachable for some reason, even tho tests pass
            for neighbor in origin_as_obj.neighbors:  # type: ignore
                if neighbor.asn == ann.as_path[-2]:
                    return super()._valid_ann(ann, *args, **kwargs)
            # Provider is fake, return False
            return False
        else:
            return super()._valid_ann(ann, *args, **kwargs)
