
from beet import Context
from simple_item_plugin.types import NAMESPACE, AUTHOR
from simple_item_plugin.utils import export_translated_string, Lang
from simple_item_plugin.guide import guide
from simple_item_plugin.versioning import beet_default as versioning
from mecha import beet_default as mecha
from weld_deps.main import DepsConfig as WeldDepsConfig
import json


def beet_default(ctx: Context):
    NAMESPACE.set(ctx.project_id)
    AUTHOR.set(ctx.project_author)
    ctx.meta.setdefault("simple_item_plugin", {}).setdefault("stable_cache", {})
    stable_cache = ctx.directory / "stable_cache.json"
    if stable_cache.exists():
        with open(stable_cache, "r") as f:
            ctx.meta["simple_item_plugin"]["stable_cache"] = json.load(f)
    project_name = ctx.project_name.split("_")
    project_name = "".join([word.capitalize() for word in project_name])
    export_translated_string(ctx, (f"{NAMESPACE}.name", {Lang.en_us: project_name, Lang.fr_fr: project_name}))
    ctx.meta.setdefault("required_deps", set())
    yield
    ctx.require(guide)
    ctx.require(versioning)
    ctx.require(mecha)

    opts = ctx.validate("weld_deps", WeldDepsConfig)
    for dep in ctx.meta["required_deps"]:
        assert dep in [d.id for d in opts.deps], f"Required dep {dep} not found in weld_deps"

    with open(stable_cache, "w") as f:
        json.dump(ctx.meta["simple_item_plugin"]["stable_cache"], f, indent=4)