---
name: godot-documentation
description: Complete official Godot Engine documentation. Covers getting started guides, tutorials, API class reference, engine details, and community resources.
license: Creative Commons Legal Code 3 (same as Godot's documentation)
trigger: always
---

# Godot Engine Official Documentation

This skill contains the complete official Godot Engine documentation from the `stable` branch of [godotengine/godot-docs](https://github.com/godotengine/godot-docs) in its original reStructuredText format.

# Initialize this skill

If the `references` folder is missing, then:
1. Git clone https://github.com/godotengine/godot-docs into the same folder as this skill file is located in.
2. Switch to the `stable` branch in the Git working copy cloned into the `godot-docs` folder.
3. Create the `references` folder under the folder this skill file is located in.
4. Move the following file from the `godot-docs` folder into the `references` folder: `index.rst`
5. Move the following folders from the `godot-docs` folder into the `references` folder: `classes`, `tutorials`, `engine_details`, `getting_started`, `community`, `about`
6. Delete the `godot-docs` repository folder (what you have just cloned).

## Update this skill

If the Godot version increases, then update this skill by:
1. Remove the `references` folder.
2. Run all steps of the "Initialize this skill" section above.

# When to Use

Use this documentation as the authoritative reference for Godot when:

- Looking up API class reference (`references/classes/`)
- Checking how engine features work (`references/tutorials/`)
- Understanding engine internals (`references/engine_details/`)
- Following getting started guides (`references/getting_started/`)
- Verifying correct usage of nodes, resources, signals, or GDScript syntax

# Documentation Structure

| Directory | Contents |
|-----------|----------|
| `references/classes/` | API class reference for all Godot classes |
| `references/tutorials/` | In-depth tutorials on all engine systems |
| `references/engine_details/` | Engine internals and architecture |
| `references/getting_started/` | Introduction and first steps |
| `references/about/` | About Godot, FAQ, release info |
| `references/community/` | Community resources and contribution guides |

The documentation files are in reStructuredText (rst) format.

# Key References

## Class Reference
- Node types: `references/classes/class_node.rst`, `references/classes/class_node2d.rst`, `references/classes/class_node3d.rst`
- Physics: `references/classes/class_characterbody2d.rst`, `references/classes/class_characterbody3d.rst`, `references/classes/class_rigidbody2d.rst`, `references/classes/class_rigidbody3d.rst`
- UI: `references/classes/class_control.rst`, `references/classes/class_container.rst`, `references/classes/class_label.rst`
- Resources: `references/classes/class_resource.rst`, `references/classes/class_packedscene.rst`

## Tutorials by Topic
- Scripting: `references/tutorials/scripting/`
- 2D: `references/tutorials/2d/`
- 3D: `references/tutorials/3d/`
- Animation: `references/tutorials/animation/`
- Physics: `references/tutorials/physics/`
- Shaders: `references/tutorials/shaders/`
- Networking: `references/tutorials/networking/`
- Navigation: `references/tutorials/navigation/`
- UI: `references/tutorials/ui/`
- Audio: `references/tutorials/audio/`
- I/O: `references/tutorials/io/`
- XR: `references/tutorials/xr/`
- Performance: `references/tutorials/performance/`
- Platform-specific: `references/tutorials/platform/`
- Export: `references/tutorials/export/`

# Usage Guidelines

1. **Always prefer this documentation** over guessing or relying on potentially outdated information in other skills
2. **Check class reference first** when unsure about method signatures, property types, or signal parameters
3. **Cross-reference tutorials** for recommended patterns and best practices
4. **Note**: Image references in the docs point to the original repo paths and won't render locally — focus on the text content
