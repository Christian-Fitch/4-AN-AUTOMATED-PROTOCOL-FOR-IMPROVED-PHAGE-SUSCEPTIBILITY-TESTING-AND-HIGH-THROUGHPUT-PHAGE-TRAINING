import json
from opentrons import protocol_api, types

metadata = {
    "protocolName": "CPL15_Better_Host_Range_Setup_MultiChannel",
    "author": "CPL, Christian Fitch",
    "created": "2026-03-09T14:50:25.266Z",
    "internalAppBuildDate": "Wed, 04 Mar 2026 17:13:57 GMT",
    "lastModified": "2026-03-09T15:32:11.652Z",
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
    reservoir_1 = protocol.load_labware_from_definition(
        CUSTOM_LABWARE["custom_beta/analyticalsales_4_reservoir_73000ul/1"],
        location="4",
    )
    well_plate_1 = protocol.load_labware(
        "greiner_96_wellplate_382ul",
        location="5",
        namespace="opentrons",
        version=1,
    )
    well_plate_2 = protocol.load_labware(
        "greiner_96_wellplate_382ul",
        location="2",
        namespace="opentrons",
        version=1,
    )

    # Load Pipettes:
    pipette_left = protocol.load_instrument("p300_multi_gen2", "left")
    pipette_right = protocol.load_instrument("p20_multi_gen2", "right")

    # Define Liquids:
    liquid_1 = protocol.define_liquid(
        "sLB",
        display_color="#ffbb00ff",
    )
    liquid_2 = protocol.define_liquid(
        "Phage-sLB",
        display_color="#ff9900ff",
    )
    liquid_3 = protocol.define_liquid(
        "Bacteria-sLB",
        display_color="#50d5ffff",
    )

    # Load Liquids:
    reservoir_1.load_liquid(
        wells=["A1"],
        liquid=liquid_1,
        volume=50000,
    )
    reservoir_1.load_liquid(
        wells=["A2"],
        liquid=liquid_2,
        volume=50000,
    )
    well_plate_1.load_liquid(
        wells=[
            "A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1",
            "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4",
            "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7",
            "A10", "B10", "C10", "D10", "E10", "F10", "G10", "H10"
        ],
        liquid=liquid_3,
        volume=200,
    )

    # PROTOCOL STEPS

    # Step 1: transfer
    pipette_left.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_left.transfer_with_liquid_class(
        volume=90,
        source=[reservoir_1["A1"], reservoir_1["A1"], reservoir_1["A1"], reservoir_1["A1"], reservoir_1["A1"], reservoir_1["A1"], reservoir_1["A1"], reservoir_1["A1"]],
        dest=[well_plate_2["A2"], well_plate_2["A3"], well_plate_2["A5"], well_plate_2["A6"], well_plate_2["A8"], well_plate_2["A9"], well_plate_2["A11"], well_plate_2["A12"]],
        new_tip="once",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_1",
            properties={"p300_multi_gen2": {"opentrons/opentrons_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 5},
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
                    "flow_rate_by_volume": [(0, 45)],
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
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_left.drop_tip()

    # Step 2: transfer
    pipette_left.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_left.transfer_with_liquid_class(
        volume=99,
        source=[reservoir_1["A2"], reservoir_1["A2"], reservoir_1["A2"], reservoir_1["A2"]],
        dest=[well_plate_2["A1"], well_plate_2["A4"], well_plate_2["A7"], well_plate_2["A10"]],
        new_tip="once",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_2",
            properties={"p300_multi_gen2": {"opentrons/opentrons_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 5},
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
                        "offset": {"x": 0, "y": 0, "z": 1},
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
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_left.drop_tip()

    # Step 3: transfer
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=1,
        source=[well_plate_1["A1"], well_plate_1["A4"], well_plate_1["A7"], well_plate_1["A10"]],
        dest=[well_plate_2["A1"], well_plate_2["A4"], well_plate_2["A7"], well_plate_2["A10"]],
        new_tip="per source",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_3",
            properties={"p20_multi_gen2": {"opentrons/opentrons_96_filtertiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 3},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": True, "repetitions": 3, "volume": 10},
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
                        "offset": {"x": 0, "y": 0, "z": 1},
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
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip()

CUSTOM_LABWARE = json.loads("""{"custom_beta/analyticalsales_4_reservoir_73000ul/1":{"ordering":[["A1"],["A2"],["A3"],["A4"]],"brand":{"brand":"analytical sales","brandId":["Deep Well Reservoir","Four Columns","96733"]},"metadata":{"displayName":"Analytical Sales 4 Reservoir 73000 µL","displayCategory":"reservoir","displayVolumeUnits":"µL","tags":[]},"dimensions":{"xDimension":127.76,"yDimension":85.47,"zDimension":44.04},"wells":{"A1":{"depth":42.08,"totalLiquidVolume":73000,"shape":"rectangular","xDimension":26.11,"yDimension":71,"x":23.06,"y":42.97,"z":1.96},"A2":{"depth":42.08,"totalLiquidVolume":73000,"shape":"rectangular","xDimension":26.11,"yDimension":71,"x":50.06,"y":42.97,"z":1.96},"A3":{"depth":42.08,"totalLiquidVolume":73000,"shape":"rectangular","xDimension":26.11,"yDimension":71,"x":77.06,"y":42.97,"z":1.96},"A4":{"depth":42.08,"totalLiquidVolume":73000,"shape":"rectangular","xDimension":26.11,"yDimension":71,"x":104.06,"y":42.97,"z":1.96}},"groups":[{"metadata":{"wellBottomShape":"v"},"wells":["A1","A2","A3","A4"]}],"parameters":{"format":"irregular","quirks":["centerMultichannelOnWells","touchTipDisabled"],"isTiprack":false,"isMagneticModuleCompatible":false,"loadName":"analyticalsales_4_reservoir_73000ul"},"namespace":"custom_beta","version":1,"schemaVersion":2,"cornerOffsetFromSlot":{"x":0,"y":0,"z":0}}}""")

DESIGNER_APPLICATION = """{"robot":{"model":"OT-2 Standard"},"designerApplication":{"name":"opentrons/protocol-designer","version":"8.8.0","data":{"pipetteTiprackAssignments":{"f477aa32-3a7e-4dd9-98ff-1b5f2dc97347":["opentrons/opentrons_96_filtertiprack_200ul/1"],"dc14a4c1-9431-42e2-87ba-9e8064d32a59":["opentrons/opentrons_96_filtertiprack_20ul/1"]},"dismissedWarnings":{"form":[],"timeline":[]},"ingredients":{"0":{"displayName":"sLB","displayColor":"#ffbb00ff","description":null,"liquidGroupId":"0"},"1":{"displayName":"Phage-sLB","displayColor":"#ff9900ff","description":null,"liquidGroupId":"1"},"2":{"displayName":"Bacteria-sLB","displayColor":"#50d5ffff","description":null,"liquidGroupId":"2"}},"ingredLocations":{"52455526-3113-4410-8154-ccb8f75f08d5:custom_beta/analyticalsales_4_reservoir_73000ul/1":{"A1":{"0":{"volume":50000}},"A2":{"1":{"volume":50000}}},"0f24ce6e-f4ad-4abe-9674-2e32e461c844:opentrons/greiner_96_wellplate_382ul/1":{"A1":{"2":{"volume":200}},"B1":{"2":{"volume":200}},"C1":{"2":{"volume":200}},"D1":{"2":{"volume":200}},"E1":{"2":{"volume":200}},"F1":{"2":{"volume":200}},"G1":{"2":{"volume":200}},"H1":{"2":{"volume":200}},"A4":{"2":{"volume":200}},"B4":{"2":{"volume":200}},"C4":{"2":{"volume":200}},"D4":{"2":{"volume":200}},"E4":{"2":{"volume":200}},"F4":{"2":{"volume":200}},"G4":{"2":{"volume":200}},"H4":{"2":{"volume":200}},"A7":{"2":{"volume":200}},"B7":{"2":{"volume":200}},"C7":{"2":{"volume":200}},"D7":{"2":{"volume":200}},"E7":{"2":{"volume":200}},"F7":{"2":{"volume":200}},"G7":{"2":{"volume":200}},"H7":{"2":{"volume":200}},"A10":{"2":{"volume":200}},"B10":{"2":{"volume":200}},"C10":{"2":{"volume":200}},"D10":{"2":{"volume":200}},"E10":{"2":{"volume":200}},"F10":{"2":{"volume":200}},"G10":{"2":{"volume":200}},"H10":{"2":{"volume":200}}}},"savedStepForms":{"__INITIAL_DECK_SETUP_STEP__":{"stepType":"manualIntervention","id":"__INITIAL_DECK_SETUP_STEP__","labwareLocationUpdate":{"f0a0340f-4371-4176-a0de-2526f6adbff0:opentrons/opentrons_96_filtertiprack_200ul/1":"10","95e49d40-4aef-4851-b157-1a252771d9ab:opentrons/opentrons_96_filtertiprack_20ul/1":"11","52455526-3113-4410-8154-ccb8f75f08d5:custom_beta/analyticalsales_4_reservoir_73000ul/1":"4","0f24ce6e-f4ad-4abe-9674-2e32e461c844:opentrons/greiner_96_wellplate_382ul/1":"5","86aa2c9b-53cb-4823-b289-2867dce00b6f:opentrons/greiner_96_wellplate_382ul/1":"2"},"pipetteLocationUpdate":{"f477aa32-3a7e-4dd9-98ff-1b5f2dc97347":"left","dc14a4c1-9431-42e2-87ba-9e8064d32a59":"right"},"moduleLocationUpdate":{},"moduleStateUpdate":{},"trashBinLocationUpdate":{"e948d926-0aa9-496a-9f5f-098e314c8acd:trashBin":"cutout12"},"wasteChuteLocationUpdate":{},"stagingAreaLocationUpdate":{},"gripperLocationUpdate":{}},"56db80c7-d70b-47ae-ba43-deb20c8eed89":{"id":"56db80c7-d70b-47ae-ba43-deb20c8eed89","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","stepNumber":0,"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"94","aspirate_labware":"52455526-3113-4410-8154-ccb8f75f08d5:custom_beta/analyticalsales_4_reservoir_73000ul/1","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":null,"aspirate_mmFromBottom":5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"125","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"125","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":60,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"94","blowout_location":null,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"45","dispense_labware":"86aa2c9b-53cb-4823-b289-2867dce00b6f:opentrons/greiner_96_wellplate_382ul/1","dispense_mix_checkbox":false,"dispense_mix_times":"","dispense_mix_volume":null,"dispense_mmFromBottom":3,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"125","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"125","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":60,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A2","A3","A5","A6","A8","A9","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"e948d926-0aa9-496a-9f5f-098e314c8acd:trashBin","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"f477aa32-3a7e-4dd9-98ff-1b5f2dc97347","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"99"},"cd2e45e2-53d3-48f7-becb-e63585e2e6c2":{"id":"cd2e45e2-53d3-48f7-becb-e63585e2e6c2","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","stepNumber":0,"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"94","aspirate_labware":"52455526-3113-4410-8154-ccb8f75f08d5:custom_beta/analyticalsales_4_reservoir_73000ul/1","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":null,"aspirate_mmFromBottom":5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"125","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"125","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":60,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"94","blowout_location":null,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"94","dispense_labware":"86aa2c9b-53cb-4823-b289-2867dce00b6f:opentrons/greiner_96_wellplate_382ul/1","dispense_mix_checkbox":false,"dispense_mix_times":"","dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"125","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"125","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":60,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1","A4","A7","A10"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"e948d926-0aa9-496a-9f5f-098e314c8acd:trashBin","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"f477aa32-3a7e-4dd9-98ff-1b5f2dc97347","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"99"},"0a4b08cf-2151-44e0-823c-5eebfb5c6f7d":{"id":"0a4b08cf-2151-44e0-823c-5eebfb5c6f7d","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","stepNumber":0,"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","aspirate_labware":"0f24ce6e-f4ad-4abe-9674-2e32e461c844:opentrons/greiner_96_wellplate_382ul/1","aspirate_mix_checkbox":true,"aspirate_mix_times":"3","aspirate_mix_volume":"10","aspirate_mmFromBottom":3,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"125","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"125","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":60,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1","A4","A7","A10"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"7.6","blowout_location":null,"changeTip":"perSource","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"7.6","dispense_labware":"86aa2c9b-53cb-4823-b289-2867dce00b6f:opentrons/greiner_96_wellplate_382ul/1","dispense_mix_checkbox":false,"dispense_mix_times":"","dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"125","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"125","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":60,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1","A4","A7","A10"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"e948d926-0aa9-496a-9f5f-098e314c8acd:trashBin","liquidClassesSupported":true,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"dc14a4c1-9431-42e2-87ba-9e8064d32a59","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_filtertiprack_20ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"1"}},"orderedStepIds":["56db80c7-d70b-47ae-ba43-deb20c8eed89","cd2e45e2-53d3-48f7-becb-e63585e2e6c2","0a4b08cf-2151-44e0-823c-5eebfb5c6f7d"],"pipettes":{"f477aa32-3a7e-4dd9-98ff-1b5f2dc97347":{"pipetteName":"p300_multi_gen2"},"dc14a4c1-9431-42e2-87ba-9e8064d32a59":{"pipetteName":"p20_multi_gen2"}},"modules":{},"labware":{"f0a0340f-4371-4176-a0de-2526f6adbff0:opentrons/opentrons_96_filtertiprack_200ul/1":{"displayName":"Opentrons OT-2 96 Filter Tip Rack 200 µL","labwareDefURI":"opentrons/opentrons_96_filtertiprack_200ul/1"},"95e49d40-4aef-4851-b157-1a252771d9ab:opentrons/opentrons_96_filtertiprack_20ul/1":{"displayName":"Opentrons OT-2 96 Filter Tip Rack 20 µL","labwareDefURI":"opentrons/opentrons_96_filtertiprack_20ul/1"},"52455526-3113-4410-8154-ccb8f75f08d5:custom_beta/analyticalsales_4_reservoir_73000ul/1":{"displayName":"Analytical Sales 4 Reservoir 73000 µL","labwareDefURI":"custom_beta/analyticalsales_4_reservoir_73000ul/1"},"0f24ce6e-f4ad-4abe-9674-2e32e461c844:opentrons/greiner_96_wellplate_382ul/1":{"displayName":"Greiner 96 Well Plate 382 µL","labwareDefURI":"opentrons/greiner_96_wellplate_382ul/1"},"86aa2c9b-53cb-4823-b289-2867dce00b6f:opentrons/greiner_96_wellplate_382ul/1":{"displayName":"Greiner 96 Well Plate 382 µL","labwareDefURI":"opentrons/greiner_96_wellplate_382ul/1"}}}},"metadata":{"protocolName":"CPL15_Better_Host_Range_Setup_MultiChannel","author":"CPL, Christian Fitch","description":"","source":"Protocol Designer","created":1773067825266,"lastModified":1773070331652}}"""
