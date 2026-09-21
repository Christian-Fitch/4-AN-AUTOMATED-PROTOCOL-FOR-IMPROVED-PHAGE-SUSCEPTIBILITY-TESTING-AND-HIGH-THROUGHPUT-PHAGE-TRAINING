import json
from opentrons import protocol_api, types

metadata = {
    "protocolName": "CPL16_Better_Host_Range_SD_and_filter",
    "author": "CPL, Christian Fitch",
    "created": "2026-03-10T11:20:22.530Z",
    "internalAppBuildDate": "Wed, 04 Mar 2026 17:13:57 GMT",
    "lastModified": "2026-03-17T15:00:24.307Z",
    "protocolDesigner": "8.9.0",
    "source": "Protocol Designer",
}

requirements = {"robotType": "OT-2", "apiLevel": "2.27"}

def run(protocol: protocol_api.ProtocolContext) -> None:
    # Load Labware:
    tip_rack_1 = protocol.load_labware(
        "opentrons_96_filtertiprack_200ul",
        location="10",
        namespace="opentrons",
        version=1,
    )
    tip_rack_2 = protocol.load_labware(
        "opentrons_96_filtertiprack_20ul",
        location="11",
        namespace="opentrons",
        version=1,
    )
    well_plate_1 = protocol.load_labware_from_definition(
        CUSTOM_LABWARE["custom_beta/filterplate_96_wellplate_200ul/1"],
        location="2",
    )
    well_plate_2 = protocol.load_labware(
        "greiner_96_wellplate_382ul",
        location="1",
        namespace="opentrons",
        version=1,
    )

    # Load Pipettes:
    pipette_left = protocol.load_instrument("p300_multi_gen2", "left")
    pipette_right = protocol.load_instrument("p20_multi_gen2", "right")

    # Define Liquids:
    liquid_1 = protocol.define_liquid(
        "sLB",
        display_color="#ffd600ff",
    )
    liquid_2 = protocol.define_liquid(
        "test-sLB",
        display_color="#ff9900ff",
    )

    # Load Liquids:
    well_plate_2.load_liquid(
        wells=[
            "A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1",
            "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4",
            "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7",
            "A10", "B10", "C10", "D10", "E10", "F10", "G10", "H10"
        ],
        liquid=liquid_2,
        volume=100,
    )
    well_plate_2.load_liquid(
        wells=[
            "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2",
            "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3",
            "A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5",
            "A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6",
            "A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8",
            "A9", "B9", "C9", "D9", "E9", "F9", "G9", "H9",
            "A11", "B11", "C11", "D11", "E11", "F11", "G11", "H11",
            "A12", "B12", "C12", "D12", "E12", "F12", "G12", "H12"
        ],
        liquid=liquid_1,
        volume=90,
    )

    # PROTOCOL STEPS

    # Step 1: transfer
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=10,
        source=[well_plate_2["A1"]],
        dest=[well_plate_2["A2"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_1",
            properties={"p20_multi_gen2": {"opentrons/opentrons_96_filtertiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 7.6)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 7.6)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": True, "repetitions": 3, "volume": 20},
                },
            }}},
        ),
    )
    pipette_right.drop_tip()

    # Step 2: transfer
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=10,
        source=[well_plate_2["A2"]],
        dest=[well_plate_2["A3"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_2",
            properties={"p20_multi_gen2": {"opentrons/opentrons_96_filtertiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 7.6)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 7.6)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": True, "repetitions": 3, "volume": 20},
                },
            }}},
        ),
    )
    pipette_right.drop_tip()

    # Step 3: transfer
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=10,
        source=[well_plate_2["A4"]],
        dest=[well_plate_2["A5"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_3",
            properties={"p20_multi_gen2": {"opentrons/opentrons_96_filtertiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 7.6)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 7.6)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": True, "repetitions": 3, "volume": 20},
                },
            }}},
        ),
    )
    pipette_right.drop_tip()

    # Step 4: transfer
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=10,
        source=[well_plate_2["A5"]],
        dest=[well_plate_2["A6"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_4",
            properties={"p20_multi_gen2": {"opentrons/opentrons_96_filtertiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 7.6)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 7.6)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": True, "repetitions": 3, "volume": 20},
                },
            }}},
        ),
    )
    pipette_right.drop_tip()

    # Step 5: transfer
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=10,
        source=[well_plate_2["A7"]],
        dest=[well_plate_2["A8"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_5",
            properties={"p20_multi_gen2": {"opentrons/opentrons_96_filtertiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 7.6)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 7.6)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": True, "repetitions": 3, "volume": 20},
                },
            }}},
        ),
    )
    pipette_right.drop_tip()

    # Step 6: transfer
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=10,
        source=[well_plate_2["A8"]],
        dest=[well_plate_2["A9"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_6",
            properties={"p20_multi_gen2": {"opentrons/opentrons_96_filtertiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 7.6)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 7.6)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": True, "repetitions": 3, "volume": 20},
                },
            }}},
        ),
    )
    pipette_right.drop_tip()

    # Step 7: transfer
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=10,
        source=[well_plate_2["A10"]],
        dest=[well_plate_2["A11"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_7",
            properties={"p20_multi_gen2": {"opentrons/opentrons_96_filtertiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 7.6)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 7.6)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": True, "repetitions": 3, "volume": 20},
                },
            }}},
        ),
    )
    pipette_right.drop_tip()

    # Step 8: transfer
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=10,
        source=[well_plate_2["A11"]],
        dest=[well_plate_2["A12"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_8",
            properties={"p20_multi_gen2": {"opentrons/opentrons_96_filtertiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 7.6)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 7.6)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": True, "repetitions": 3, "volume": 20},
                },
            }}},
        ),
    )
    pipette_right.drop_tip()

    # Step 9: transfer
    pipette_left.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_left.transfer_with_liquid_class(
        volume=90,
        source=[well_plate_2["A1"], well_plate_2["A2"], well_plate_2["A3"], well_plate_2["A4"], well_plate_2["A5"], well_plate_2["A6"], well_plate_2["A7"], well_plate_2["A8"], well_plate_2["A9"], well_plate_2["A10"], well_plate_2["A11"], well_plate_2["A12"]],
        dest=[well_plate_1["A1"], well_plate_1["A2"], well_plate_1["A3"], well_plate_1["A4"], well_plate_1["A5"], well_plate_1["A6"], well_plate_1["A7"], well_plate_1["A8"], well_plate_1["A9"], well_plate_1["A10"], well_plate_1["A11"], well_plate_1["A12"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_9",
            properties={"p300_multi_gen2": {"opentrons/opentrons_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 94)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 3},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 94)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "destination", "flow_rate": 10},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_left.drop_tip()

CUSTOM_LABWARE = json.loads("""{"custom_beta/filterplate_96_wellplate_200ul/1":{"ordering":[["A1","B1","C1","D1","E1","F1","G1","H1"],["A2","B2","C2","D2","E2","F2","G2","H2"],["A3","B3","C3","D3","E3","F3","G3","H3"],["A4","B4","C4","D4","E4","F4","G4","H4"],["A5","B5","C5","D5","E5","F5","G5","H5"],["A6","B6","C6","D6","E6","F6","G6","H6"],["A7","B7","C7","D7","E7","F7","G7","H7"],["A8","B8","C8","D8","E8","F8","G8","H8"],["A9","B9","C9","D9","E9","F9","G9","H9"],["A10","B10","C10","D10","E10","F10","G10","H10"],["A11","B11","C11","D11","E11","F11","G11","H11"],["A12","B12","C12","D12","E12","F12","G12","H12"]],"brand":{"brand":"Filter Plate","brandId":[]},"metadata":{"displayName":"Filter Plate 96 Well Plate 200 µL","displayCategory":"wellPlate","displayVolumeUnits":"µL","tags":[]},"dimensions":{"xDimension":127,"yDimension":85,"zDimension":28},"wells":{"A1":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":14.38,"y":73.76,"z":16},"B1":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":14.38,"y":64.76,"z":16},"C1":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":14.38,"y":55.76,"z":16},"D1":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":14.38,"y":46.76,"z":16},"E1":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":14.38,"y":37.76,"z":16},"F1":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":14.38,"y":28.76,"z":16},"G1":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":14.38,"y":19.76,"z":16},"H1":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":14.38,"y":10.76,"z":16},"A2":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":23.38,"y":73.76,"z":16},"B2":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":23.38,"y":64.76,"z":16},"C2":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":23.38,"y":55.76,"z":16},"D2":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":23.38,"y":46.76,"z":16},"E2":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":23.38,"y":37.76,"z":16},"F2":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":23.38,"y":28.76,"z":16},"G2":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":23.38,"y":19.76,"z":16},"H2":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":23.38,"y":10.76,"z":16},"A3":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":32.38,"y":73.76,"z":16},"B3":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":32.38,"y":64.76,"z":16},"C3":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":32.38,"y":55.76,"z":16},"D3":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":32.38,"y":46.76,"z":16},"E3":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":32.38,"y":37.76,"z":16},"F3":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":32.38,"y":28.76,"z":16},"G3":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":32.38,"y":19.76,"z":16},"H3":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":32.38,"y":10.76,"z":16},"A4":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":41.38,"y":73.76,"z":16},"B4":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":41.38,"y":64.76,"z":16},"C4":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":41.38,"y":55.76,"z":16},"D4":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":41.38,"y":46.76,"z":16},"E4":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":41.38,"y":37.76,"z":16},"F4":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":41.38,"y":28.76,"z":16},"G4":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":41.38,"y":19.76,"z":16},"H4":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":41.38,"y":10.76,"z":16},"A5":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":50.38,"y":73.76,"z":16},"B5":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":50.38,"y":64.76,"z":16},"C5":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":50.38,"y":55.76,"z":16},"D5":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":50.38,"y":46.76,"z":16},"E5":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":50.38,"y":37.76,"z":16},"F5":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":50.38,"y":28.76,"z":16},"G5":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":50.38,"y":19.76,"z":16},"H5":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":50.38,"y":10.76,"z":16},"A6":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":59.38,"y":73.76,"z":16},"B6":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":59.38,"y":64.76,"z":16},"C6":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":59.38,"y":55.76,"z":16},"D6":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":59.38,"y":46.76,"z":16},"E6":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":59.38,"y":37.76,"z":16},"F6":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":59.38,"y":28.76,"z":16},"G6":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":59.38,"y":19.76,"z":16},"H6":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":59.38,"y":10.76,"z":16},"A7":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":68.38,"y":73.76,"z":16},"B7":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":68.38,"y":64.76,"z":16},"C7":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":68.38,"y":55.76,"z":16},"D7":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":68.38,"y":46.76,"z":16},"E7":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":68.38,"y":37.76,"z":16},"F7":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":68.38,"y":28.76,"z":16},"G7":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":68.38,"y":19.76,"z":16},"H7":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":68.38,"y":10.76,"z":16},"A8":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":77.38,"y":73.76,"z":16},"B8":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":77.38,"y":64.76,"z":16},"C8":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":77.38,"y":55.76,"z":16},"D8":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":77.38,"y":46.76,"z":16},"E8":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":77.38,"y":37.76,"z":16},"F8":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":77.38,"y":28.76,"z":16},"G8":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":77.38,"y":19.76,"z":16},"H8":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":77.38,"y":10.76,"z":16},"A9":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":86.38,"y":73.76,"z":16},"B9":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":86.38,"y":64.76,"z":16},"C9":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":86.38,"y":55.76,"z":16},"D9":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":86.38,"y":46.76,"z":16},"E9":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":86.38,"y":37.76,"z":16},"F9":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":86.38,"y":28.76,"z":16},"G9":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":86.38,"y":19.76,"z":16},"H9":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":86.38,"y":10.76,"z":16},"A10":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":95.38,"y":73.76,"z":16},"B10":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":95.38,"y":64.76,"z":16},"C10":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":95.38,"y":55.76,"z":16},"D10":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":95.38,"y":46.76,"z":16},"E10":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":95.38,"y":37.76,"z":16},"F10":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":95.38,"y":28.76,"z":16},"G10":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":95.38,"y":19.76,"z":16},"H10":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":95.38,"y":10.76,"z":16},"A11":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":104.38,"y":73.76,"z":16},"B11":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":104.38,"y":64.76,"z":16},"C11":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":104.38,"y":55.76,"z":16},"D11":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":104.38,"y":46.76,"z":16},"E11":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":104.38,"y":37.76,"z":16},"F11":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":104.38,"y":28.76,"z":16},"G11":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":104.38,"y":19.76,"z":16},"H11":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":104.38,"y":10.76,"z":16},"A12":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":113.38,"y":73.76,"z":16},"B12":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":113.38,"y":64.76,"z":16},"C12":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":113.38,"y":55.76,"z":16},"D12":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":113.38,"y":46.76,"z":16},"E12":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":113.38,"y":37.76,"z":16},"F12":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":113.38,"y":28.76,"z":16},"G12":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":113.38,"y":19.76,"z":16},"H12":{"depth":12,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":113.38,"y":10.76,"z":16}},"groups":[{"metadata":{"wellBottomShape":"u"},"wells":["A1","B1","C1","D1","E1","F1","G1","H1","A2","B2","C2","D2","E2","F2","G2","H2","A3","B3","C3","D3","E3","F3","G3","H3","A4","B4","C4","D4","E4","F4","G4","H4","A5","B5","C5","D5","E5","F5","G5","H5","A6","B6","C6","D6","E6","F6","G6","H6","A7","B7","C7","D7","E7","F7","G7","H7","A8","B8","C8","D8","E8","F8","G8","H8","A9","B9","C9","D9","E9","F9","G9","H9","A10","B10","C10","D10","E10","F10","G10","H10","A11","B11","C11","D11","E11","F11","G11","H11","A12","B12","C12","D12","E12","F12","G12","H12"]}],"parameters":{"format":"irregular","quirks":[],"isTiprack":false,"isMagneticModuleCompatible":false,"loadName":"filterplate_96_wellplate_200ul"},"namespace":"custom_beta","version":1,"schemaVersion":2,"cornerOffsetFromSlot":{"x":0,"y":0,"z":0}}}""")

DESIGNER_APPLICATION = """{"robot":{"model":"OT-2 Standard"},"designerApplication":{"name":"opentrons/protocol-designer","version":"8.8.0","data":{"pipetteTiprackAssignments":{"b8a668b7-16ae-455a-aef0-f6823d4dbffe":["opentrons/opentrons_96_filtertiprack_200ul/1"],"0d519eee-4c5e-445b-bebd-3c6e135657da":["opentrons/opentrons_96_filtertiprack_20ul/1"]},"dismissedWarnings":{"form":[],"timeline":[]},"ingredients":{"0":{"displayName":"sLB","displayColor":"#ffd600ff","description":null,"liquidGroupId":"0"},"1":{"displayName":"test-sLB","displayColor":"#ff9900ff","description":null,"liquidGroupId":"1"}},"ingredLocations":{"257f021c-6993-4b8b-ab99-f0d4e9fe6eec:opentrons/greiner_96_wellplate_382ul/1":{"A1":{"1":{"volume":100}},"B1":{"1":{"volume":100}},"C1":{"1":{"volume":100}},"D1":{"1":{"volume":100}},"E1":{"1":{"volume":100}},"F1":{"1":{"volume":100}},"G1":{"1":{"volume":100}},"H1":{"1":{"volume":100}},"A4":{"1":{"volume":100}},"B4":{"1":{"volume":100}},"C4":{"1":{"volume":100}},"D4":{"1":{"volume":100}},"E4":{"1":{"volume":100}},"F4":{"1":{"volume":100}},"G4":{"1":{"volume":100}},"H4":{"1":{"volume":100}},"A7":{"1":{"volume":100}},"B7":{"1":{"volume":100}},"C7":{"1":{"volume":100}},"D7":{"1":{"volume":100}},"E7":{"1":{"volume":100}},"F7":{"1":{"volume":100}},"G7":{"1":{"volume":100}},"H7":{"1":{"volume":100}},"A10":{"1":{"volume":100}},"B10":{"1":{"volume":100}},"C10":{"1":{"volume":100}},"D10":{"1":{"volume":100}},"E10":{"1":{"volume":100}},"F10":{"1":{"volume":100}},"G10":{"1":{"volume":100}},"H10":{"1":{"volume":100}},"A2":{"0":{"volume":90}},"B2":{"0":{"volume":90}},"C2":{"0":{"volume":90}},"D2":{"0":{"volume":90}},"E2":{"0":{"volume":90}},"F2":{"0":{"volume":90}},"G2":{"0":{"volume":90}},"H2":{"0":{"volume":90}},"A3":{"0":{"volume":90}},"B3":{"0":{"volume":90}},"C3":{"0":{"volume":90}},"D3":{"0":{"volume":90}},"E3":{"0":{"volume":90}},"F3":{"0":{"volume":90}},"G3":{"0":{"volume":90}},"H3":{"0":{"volume":90}},"A5":{"0":{"volume":90}},"B5":{"0":{"volume":90}},"C5":{"0":{"volume":90}},"D5":{"0":{"volume":90}},"E5":{"0":{"volume":90}},"F5":{"0":{"volume":90}},"G5":{"0":{"volume":90}},"H5":{"0":{"volume":90}},"A6":{"0":{"volume":90}},"B6":{"0":{"volume":90}},"C6":{"0":{"volume":90}},"D6":{"0":{"volume":90}},"E6":{"0":{"volume":90}},"F6":{"0":{"volume":90}},"G6":{"0":{"volume":90}},"H6":{"0":{"volume":90}},"A8":{"0":{"volume":90}},"B8":{"0":{"volume":90}},"C8":{"0":{"volume":90}},"D8":{"0":{"volume":90}},"E8":{"0":{"volume":90}},"F8":{"0":{"volume":90}},"G8":{"0":{"volume":90}},"H8":{"0":{"volume":90}},"A9":{"0":{"volume":90}},"B9":{"0":{"volume":90}},"C9":{"0":{"volume":90}},"D9":{"0":{"volume":90}},"E9":{"0":{"volume":90}},"F9":{"0":{"volume":90}},"G9":{"0":{"volume":90}},"H9":{"0":{"volume":90}},"A11":{"0":{"volume":90}},"B11":{"0":{"volume":90}},"C11":{"0":{"volume":90}},"D11":{"0":{"volume":90}},"E11":{"0":{"volume":90}},"F11":{"0":{"volume":90}},"G11":{"0":{"volume":90}},"H11":{"0":{"volume":90}},"A12":{"0":{"volume":90}},"B12":{"0":{"volume":90}},"C12":{"0":{"volume":90}},"D12":{"0":{"volume":90}},"E12":{"0":{"volume":90}},"F12":{"0":{"volume":90}},"G12":{"0":{"volume":90}},"H12":{"0":{"volume":90}}}},"savedStepForms":{"__INITIAL_DECK_SETUP_STEP__":{"stepType":"manualIntervention","id":"__INITIAL_DECK_SETUP_STEP__","labwareLocationUpdate":{"f6b244f9-c8be-46e6-982b-5f418dcde4ef:opentrons/opentrons_96_filtertiprack_200ul/1":"10","5c44abc2-b91e-4a9c-aaf0-4d618a6b3df8:opentrons/opentrons_96_filtertiprack_20ul/1":"11","a683bb9d-d6c3-4b26-8c10-78bbcde540d0:custom_beta/filterplate_96_wellplate_200ul/1":"2","257f021c-6993-4b8b-ab99-f0d4e9fe6eec:opentrons/greiner_96_wellplate_382ul/1":"1"},"pipetteLocationUpdate":{"b8a668b7-16ae-455a-aef0-f6823d4dbffe":"left","0d519eee-4c5e-445b-bebd-3c6e135657da":"right"},"moduleLocationUpdate":{},"moduleStateUpdate":{},"trashBinLocationUpdate":{"8098ed18-2e99-4807-984c-f33662579f43:trashBin":"cutout12"},"wasteChuteLocationUpdate":{},"stagingAreaLocationUpdate":{},"gripperLocationUpdate":{}},"548bd1bd-4325-46a3-900b-d5c416fea977":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"7.6","aspirate_labware":"257f021c-6993-4b8b-ab99-f0d4e9fe6eec:opentrons/greiner_96_wellplate_382ul/1","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"125","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"125","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":60,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"7.6","blowout_location":null,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"7.6","dispense_labware":"257f021c-6993-4b8b-ab99-f0d4e9fe6eec:opentrons/greiner_96_wellplate_382ul/1","dispense_mix_checkbox":true,"dispense_mix_times":"3","dispense_mix_volume":"20","dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"125","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"125","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":60,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A2"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"8098ed18-2e99-4807-984c-f33662579f43:trashBin","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"0d519eee-4c5e-445b-bebd-3c6e135657da","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_filtertiprack_20ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"10","id":"548bd1bd-4325-46a3-900b-d5c416fea977","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","stepNumber":0},"40c9d78b-0c01-4173-9228-7a64492d1605":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"7.6","aspirate_labware":"257f021c-6993-4b8b-ab99-f0d4e9fe6eec:opentrons/greiner_96_wellplate_382ul/1","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"125","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"125","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":60,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"7.6","blowout_location":null,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"7.6","dispense_labware":"257f021c-6993-4b8b-ab99-f0d4e9fe6eec:opentrons/greiner_96_wellplate_382ul/1","dispense_mix_checkbox":true,"dispense_mix_times":"3","dispense_mix_volume":"20","dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"125","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"125","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":60,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A3"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"8098ed18-2e99-4807-984c-f33662579f43:trashBin","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"0d519eee-4c5e-445b-bebd-3c6e135657da","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_filtertiprack_20ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"10","id":"40c9d78b-0c01-4173-9228-7a64492d1605","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","stepNumber":0},"d5474a31-a95c-4f41-94c1-147c3df466b4":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"7.6","aspirate_labware":"257f021c-6993-4b8b-ab99-f0d4e9fe6eec:opentrons/greiner_96_wellplate_382ul/1","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"125","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"125","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":60,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A4"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"7.6","blowout_location":null,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"7.6","dispense_labware":"257f021c-6993-4b8b-ab99-f0d4e9fe6eec:opentrons/greiner_96_wellplate_382ul/1","dispense_mix_checkbox":true,"dispense_mix_times":"3","dispense_mix_volume":"20","dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"125","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"125","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":60,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A5"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"8098ed18-2e99-4807-984c-f33662579f43:trashBin","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"0d519eee-4c5e-445b-bebd-3c6e135657da","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_filtertiprack_20ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"10","id":"d5474a31-a95c-4f41-94c1-147c3df466b4","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","stepNumber":0},"46301f6b-a5d5-4e73-90e2-54eb3890fe23":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"7.6","aspirate_labware":"257f021c-6993-4b8b-ab99-f0d4e9fe6eec:opentrons/greiner_96_wellplate_382ul/1","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"125","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"125","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":60,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A5"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"7.6","blowout_location":null,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"7.6","dispense_labware":"257f021c-6993-4b8b-ab99-f0d4e9fe6eec:opentrons/greiner_96_wellplate_382ul/1","dispense_mix_checkbox":true,"dispense_mix_times":"3","dispense_mix_volume":"20","dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"125","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"125","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":60,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"8098ed18-2e99-4807-984c-f33662579f43:trashBin","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"0d519eee-4c5e-445b-bebd-3c6e135657da","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_filtertiprack_20ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"10","id":"46301f6b-a5d5-4e73-90e2-54eb3890fe23","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","stepNumber":0},"b4a01bab-0462-4f19-a8f7-fc2b4c39de6e":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"7.6","aspirate_labware":"257f021c-6993-4b8b-ab99-f0d4e9fe6eec:opentrons/greiner_96_wellplate_382ul/1","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"125","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"125","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":60,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A7"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"7.6","blowout_location":null,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"7.6","dispense_labware":"257f021c-6993-4b8b-ab99-f0d4e9fe6eec:opentrons/greiner_96_wellplate_382ul/1","dispense_mix_checkbox":true,"dispense_mix_times":"3","dispense_mix_volume":"20","dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"125","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"125","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":60,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A8"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"8098ed18-2e99-4807-984c-f33662579f43:trashBin","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"0d519eee-4c5e-445b-bebd-3c6e135657da","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_filtertiprack_20ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"10","id":"b4a01bab-0462-4f19-a8f7-fc2b4c39de6e","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","stepNumber":0},"f41488af-f65e-420f-bdec-c235ebac9f87":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"7.6","aspirate_labware":"257f021c-6993-4b8b-ab99-f0d4e9fe6eec:opentrons/greiner_96_wellplate_382ul/1","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"125","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"125","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":60,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A8"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"7.6","blowout_location":null,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"7.6","dispense_labware":"257f021c-6993-4b8b-ab99-f0d4e9fe6eec:opentrons/greiner_96_wellplate_382ul/1","dispense_mix_checkbox":true,"dispense_mix_times":"3","dispense_mix_volume":"20","dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"125","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"125","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":60,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A9"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"8098ed18-2e99-4807-984c-f33662579f43:trashBin","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"0d519eee-4c5e-445b-bebd-3c6e135657da","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_filtertiprack_20ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"10","id":"f41488af-f65e-420f-bdec-c235ebac9f87","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","stepNumber":0},"5fbf0067-3c4b-4eac-9d1d-a719aee0d253":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"7.6","aspirate_labware":"257f021c-6993-4b8b-ab99-f0d4e9fe6eec:opentrons/greiner_96_wellplate_382ul/1","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"125","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"125","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":60,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A10"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"7.6","blowout_location":null,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"7.6","dispense_labware":"257f021c-6993-4b8b-ab99-f0d4e9fe6eec:opentrons/greiner_96_wellplate_382ul/1","dispense_mix_checkbox":true,"dispense_mix_times":"3","dispense_mix_volume":"20","dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"125","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"125","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":60,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A11"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"8098ed18-2e99-4807-984c-f33662579f43:trashBin","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"0d519eee-4c5e-445b-bebd-3c6e135657da","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_filtertiprack_20ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"10","id":"5fbf0067-3c4b-4eac-9d1d-a719aee0d253","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","stepNumber":0},"8123a3f5-eea5-4462-9e29-2e7130000b07":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"7.6","aspirate_labware":"257f021c-6993-4b8b-ab99-f0d4e9fe6eec:opentrons/greiner_96_wellplate_382ul/1","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"125","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"125","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":60,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A11"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"7.6","blowout_location":null,"changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"7.6","dispense_labware":"257f021c-6993-4b8b-ab99-f0d4e9fe6eec:opentrons/greiner_96_wellplate_382ul/1","dispense_mix_checkbox":true,"dispense_mix_times":"3","dispense_mix_volume":"20","dispense_mmFromBottom":2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"125","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"125","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":60,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"8098ed18-2e99-4807-984c-f33662579f43:trashBin","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"0d519eee-4c5e-445b-bebd-3c6e135657da","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_filtertiprack_20ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"10","id":"8123a3f5-eea5-4462-9e29-2e7130000b07","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","stepNumber":0},"ba44ef52-cd13-43d1-97a1-ac9f5bbbd1fd":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"94","aspirate_labware":"257f021c-6993-4b8b-ab99-f0d4e9fe6eec:opentrons/greiner_96_wellplate_382ul/1","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":null,"aspirate_mmFromBottom":2,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"125","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"125","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":60,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":true,"blowout_flowRate":"10","blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"94","dispense_labware":"a683bb9d-d6c3-4b26-8c10-78bbcde540d0:custom_beta/filterplate_96_wellplate_200ul/1","dispense_mix_checkbox":false,"dispense_mix_times":"","dispense_mix_volume":null,"dispense_mmFromBottom":3,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"125","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"125","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":60,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"8098ed18-2e99-4807-984c-f33662579f43:trashBin","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"b8a668b7-16ae-455a-aef0-f6823d4dbffe","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"90","id":"ba44ef52-cd13-43d1-97a1-ac9f5bbbd1fd","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","stepNumber":0}},"orderedStepIds":["548bd1bd-4325-46a3-900b-d5c416fea977","40c9d78b-0c01-4173-9228-7a64492d1605","d5474a31-a95c-4f41-94c1-147c3df466b4","46301f6b-a5d5-4e73-90e2-54eb3890fe23","b4a01bab-0462-4f19-a8f7-fc2b4c39de6e","f41488af-f65e-420f-bdec-c235ebac9f87","5fbf0067-3c4b-4eac-9d1d-a719aee0d253","8123a3f5-eea5-4462-9e29-2e7130000b07","ba44ef52-cd13-43d1-97a1-ac9f5bbbd1fd"],"pipettes":{"b8a668b7-16ae-455a-aef0-f6823d4dbffe":{"pipetteName":"p300_multi_gen2"},"0d519eee-4c5e-445b-bebd-3c6e135657da":{"pipetteName":"p20_multi_gen2"}},"modules":{},"labware":{"f6b244f9-c8be-46e6-982b-5f418dcde4ef:opentrons/opentrons_96_filtertiprack_200ul/1":{"displayName":"Opentrons OT-2 96 Filter Tip Rack 200 µL","labwareDefURI":"opentrons/opentrons_96_filtertiprack_200ul/1"},"5c44abc2-b91e-4a9c-aaf0-4d618a6b3df8:opentrons/opentrons_96_filtertiprack_20ul/1":{"displayName":"Opentrons OT-2 96 Filter Tip Rack 20 µL","labwareDefURI":"opentrons/opentrons_96_filtertiprack_20ul/1"},"a683bb9d-d6c3-4b26-8c10-78bbcde540d0:custom_beta/filterplate_96_wellplate_200ul/1":{"displayName":"Filter Plate 96 Well Plate 200 µL","labwareDefURI":"custom_beta/filterplate_96_wellplate_200ul/1"},"257f021c-6993-4b8b-ab99-f0d4e9fe6eec:opentrons/greiner_96_wellplate_382ul/1":{"displayName":"Greiner 96 Well Plate 382 µL","labwareDefURI":"opentrons/greiner_96_wellplate_382ul/1"}}}},"metadata":{"protocolName":"CPL16_Better_Host_Range_SD_and_filter","author":"CPL, Christian Fitch","description":"","source":"Protocol Designer","created":1773141622530,"lastModified":1773759624307}}"""
