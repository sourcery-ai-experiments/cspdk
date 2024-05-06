sample_pads = """
name: pads
pdk: cspdk.si500

instances:
    bl:
      component: pad
    tl:
      component: pad
    br:
      component: pad
    tr:
      component: pad

placements:
    tl:
        x: -200
        y: 500

    br:
        x: 400
        y: 400

    tr:
        x: 400
        y: 600


routes:
    electrical:
        settings:
            cross_section: xs_metal_routing
            separation: 20
            width: 10
            path_length_match_loops: 2
            end_straight_length: 100
        links:
            tl,e3: tr,e1
            bl,e3: br,e1
    optical:
        settings:
            cross_section: xs_rc
            radius: 100
        links:
            bl,e4: br,e3

"""


if __name__ == "__main__":
    import gdsfactory as gf

    c = gf.read.from_yaml(sample_pads)
    c.show()
