# SNMP MIB module (STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/stratacom_351/STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:11:01 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(stratacom,
 svConnAbitStatus,
 svConnAlarmLocalEndNNI,
 svConnAlarmRemoteEndNNI,
 svConnLocalEndPt,
 svConnLocalStr,
 svConnOpStatus,
 svConnRemoteEndPt,
 svConnRemoteStr,
 svConnType,
 svPortLine,
 svPortPhysicalPort,
 svPortPort,
 svPortSlot,
 svPortState,
 svplus) = mibBuilder.importSymbols(
    "STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1",
    "stratacom",
    "svConnAbitStatus",
    "svConnAlarmLocalEndNNI",
    "svConnAlarmRemoteEndNNI",
    "svConnLocalEndPt",
    "svConnLocalStr",
    "svConnOpStatus",
    "svConnRemoteEndPt",
    "svConnRemoteStr",
    "svConnType",
    "svPortLine",
    "svPortPhysicalPort",
    "svPortPort",
    "svPortSlot",
    "svPortState",
    "svplus")


# MODULE-IDENTITY


# Types definitions



class Active(Integer32):
    """Custom type Active based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TopologyGroup_ObjectIdentity = ObjectIdentity
topologyGroup = _TopologyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 1, 100)
)
_SvNodeGroup_ObjectIdentity = ObjectIdentity
svNodeGroup = _SvNodeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1)
)
_TrunkGroup_ObjectIdentity = ObjectIdentity
trunkGroup = _TrunkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 3)
)
_SvTrunkTable_Object = MibTable
svTrunkTable = _SvTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 3, 2)
)
if mibBuilder.loadTexts:
    svTrunkTable.setStatus("mandatory")
_SvTrunkEntry_Object = MibTableRow
svTrunkEntry = _SvTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 3, 2, 1)
)
svTrunkEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svTrunkLocalSlot"),
    (0, "STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svTrunkLocalPort"),
    (0, "STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svTrunkLocalVtrkId"),
)
if mibBuilder.loadTexts:
    svTrunkEntry.setStatus("mandatory")
_SvTrunkLocalSlot_Type = Integer32
_SvTrunkLocalSlot_Object = MibTableColumn
svTrunkLocalSlot = _SvTrunkLocalSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 3, 2, 1, 1),
    _SvTrunkLocalSlot_Type()
)
svTrunkLocalSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svTrunkLocalSlot.setStatus("mandatory")
_SvTrunkLocalPort_Type = Integer32
_SvTrunkLocalPort_Object = MibTableColumn
svTrunkLocalPort = _SvTrunkLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 3, 2, 1, 2),
    _SvTrunkLocalPort_Type()
)
svTrunkLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svTrunkLocalPort.setStatus("mandatory")
_SvTrunkLocalLine_Type = Integer32
_SvTrunkLocalLine_Object = MibTableColumn
svTrunkLocalLine = _SvTrunkLocalLine_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 3, 2, 1, 3),
    _SvTrunkLocalLine_Type()
)
svTrunkLocalLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svTrunkLocalLine.setStatus("mandatory")


class _SvTrunkCardType_Type(Integer32):
    """Custom type svTrunkCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              22,
              31,
              34,
              41,
              103,
              104,
              110,
              117,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              220,
              221,
              222,
              223,
              224,
              225)
        )
    )
    namedValues = NamedValues(
        *(("txr", 3),
          ("bni", 4),
          ("ntc", 22),
          ("atm", 31),
          ("ait", 34),
          ("uxm", 41),
          ("bni-t3", 103),
          ("bni-e3", 104),
          ("bni-oc3", 110),
          ("bxm", 117),
          ("bxm-t3-8-smf", 180),
          ("bxm-t3-8-mmf", 181),
          ("bxm-t3-8-smflr", 182),
          ("bxm-t3-8-snm", 183),
          ("bxm-t3-12-smf", 184),
          ("bxm-t3-12-mmf", 185),
          ("bxm-t3-12-smflr", 186),
          ("bxm-t3-12-snm", 187),
          ("bxm-e3-8-smf", 188),
          ("bxm-e3-8-mmf", 189),
          ("bxm-e3-8-smflr", 190),
          ("bxm-e3-8-snm", 191),
          ("bxm-e3-12-smf", 192),
          ("bxm-e3-12-mmf", 193),
          ("bxm-e3-12-smflr", 194),
          ("bxm-e3-12-snm", 195),
          ("bxm-oc3-4-smf", 196),
          ("bxm-oc3-4-mmf", 197),
          ("bxm-oc3-4-smflr", 198),
          ("bxm-oc3-4-snm", 199),
          ("bxm-oc3-8-smf", 200),
          ("bxm-oc3-8-mmf", 201),
          ("bxm-oc3-8-smflr", 202),
          ("bxm-oc3-8-snm", 203),
          ("bxm-oc12-1-smf", 204),
          ("bxm-oc12-1-mmf", 205),
          ("bxm-oc12-1-smflr", 206),
          ("bxm-oc12-1-snm", 207),
          ("bxm-oc12-2-smf", 208),
          ("bxm-oc12-2-mmf", 209),
          ("bxm-oc12-2-smflr", 210),
          ("bxm-oc12-2-snm", 211),
          ("bxm-oc3-4-stm1e", 220),
          ("bxm-oc3-8-stm1e", 221),
          ("bxm-oc3-4-xlr", 222),
          ("bxm-oc3-8-xlr", 223),
          ("bxm-oc12-1-xlr", 224),
          ("bxm-oc12-2-xlr", 225))
    )


_SvTrunkCardType_Type.__name__ = "Integer32"
_SvTrunkCardType_Object = MibTableColumn
svTrunkCardType = _SvTrunkCardType_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 3, 2, 1, 4),
    _SvTrunkCardType_Type()
)
svTrunkCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svTrunkCardType.setStatus("mandatory")


class _SvTrunkInterface_Type(Integer32):
    """Custom type svTrunkInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("t1", 2),
          ("e1", 3),
          ("subrate", 4),
          ("oc3", 5),
          ("oc12", 6),
          ("t3", 7),
          ("e3", 8),
          ("broadband", 9))
    )


_SvTrunkInterface_Type.__name__ = "Integer32"
_SvTrunkInterface_Object = MibTableColumn
svTrunkInterface = _SvTrunkInterface_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 3, 2, 1, 5),
    _SvTrunkInterface_Type()
)
svTrunkInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svTrunkInterface.setStatus("mandatory")
_SvTrunkLineLoad_Type = Integer32
_SvTrunkLineLoad_Object = MibTableColumn
svTrunkLineLoad = _SvTrunkLineLoad_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 3, 2, 1, 6),
    _SvTrunkLineLoad_Type()
)
svTrunkLineLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svTrunkLineLoad.setStatus("mandatory")
_SvTrunkRemNodeId_Type = Integer32
_SvTrunkRemNodeId_Object = MibTableColumn
svTrunkRemNodeId = _SvTrunkRemNodeId_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 3, 2, 1, 7),
    _SvTrunkRemNodeId_Type()
)
svTrunkRemNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svTrunkRemNodeId.setStatus("mandatory")
_SvTrunkRemLineNumber_Type = Integer32
_SvTrunkRemLineNumber_Object = MibTableColumn
svTrunkRemLineNumber = _SvTrunkRemLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 3, 2, 1, 8),
    _SvTrunkRemLineNumber_Type()
)
svTrunkRemLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svTrunkRemLineNumber.setStatus("mandatory")
_SvTrunkRemSlot_Type = Integer32
_SvTrunkRemSlot_Object = MibTableColumn
svTrunkRemSlot = _SvTrunkRemSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 3, 2, 1, 9),
    _SvTrunkRemSlot_Type()
)
svTrunkRemSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svTrunkRemSlot.setStatus("mandatory")
_SvTrunkRemPort_Type = Integer32
_SvTrunkRemPort_Object = MibTableColumn
svTrunkRemPort = _SvTrunkRemPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 3, 2, 1, 10),
    _SvTrunkRemPort_Type()
)
svTrunkRemPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svTrunkRemPort.setStatus("mandatory")


class _SvTrunkAlarmState_Type(Integer32):
    """Custom type svTrunkAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("minor", 2),
          ("major", 3))
    )


_SvTrunkAlarmState_Type.__name__ = "Integer32"
_SvTrunkAlarmState_Object = MibTableColumn
svTrunkAlarmState = _SvTrunkAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 3, 2, 1, 11),
    _SvTrunkAlarmState_Type()
)
svTrunkAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svTrunkAlarmState.setStatus("mandatory")
_SvTrunkActive_Type = Active
_SvTrunkActive_Object = MibTableColumn
svTrunkActive = _SvTrunkActive_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 3, 2, 1, 13),
    _SvTrunkActive_Type()
)
svTrunkActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svTrunkActive.setStatus("mandatory")


class _SvTrunkStatus_Type(Integer32):
    """Custom type svTrunkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("clear", 2),
          ("fail", 3),
          ("down", 4))
    )


_SvTrunkStatus_Type.__name__ = "Integer32"
_SvTrunkStatus_Object = MibTableColumn
svTrunkStatus = _SvTrunkStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 3, 2, 1, 14),
    _SvTrunkStatus_Type()
)
svTrunkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svTrunkStatus.setStatus("mandatory")
_SvTrunkStatReserve_Type = Integer32
_SvTrunkStatReserve_Object = MibTableColumn
svTrunkStatReserve = _SvTrunkStatReserve_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 3, 2, 1, 15),
    _SvTrunkStatReserve_Type()
)
svTrunkStatReserve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svTrunkStatReserve.setStatus("mandatory")
_SvTrunkBurstyDataBQDepth_Type = Integer32
_SvTrunkBurstyDataBQDepth_Object = MibTableColumn
svTrunkBurstyDataBQDepth = _SvTrunkBurstyDataBQDepth_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 3, 2, 1, 16),
    _SvTrunkBurstyDataBQDepth_Type()
)
svTrunkBurstyDataBQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svTrunkBurstyDataBQDepth.setStatus("mandatory")
_SvTrunkBurstyDataBQEfcnThreshold_Type = Integer32
_SvTrunkBurstyDataBQEfcnThreshold_Object = MibTableColumn
svTrunkBurstyDataBQEfcnThreshold = _SvTrunkBurstyDataBQEfcnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 3, 2, 1, 17),
    _SvTrunkBurstyDataBQEfcnThreshold_Type()
)
svTrunkBurstyDataBQEfcnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svTrunkBurstyDataBQEfcnThreshold.setStatus("mandatory")
_SvTrunkClpHighDropThreshold_Type = Integer32
_SvTrunkClpHighDropThreshold_Object = MibTableColumn
svTrunkClpHighDropThreshold = _SvTrunkClpHighDropThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 3, 2, 1, 18),
    _SvTrunkClpHighDropThreshold_Type()
)
svTrunkClpHighDropThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svTrunkClpHighDropThreshold.setStatus("mandatory")
_SvTrunkClpLowDropThreshold_Type = Integer32
_SvTrunkClpLowDropThreshold_Object = MibTableColumn
svTrunkClpLowDropThreshold = _SvTrunkClpLowDropThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 3, 2, 1, 19),
    _SvTrunkClpLowDropThreshold_Type()
)
svTrunkClpLowDropThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svTrunkClpLowDropThreshold.setStatus("mandatory")
_SvTrunkLocalVtrkId_Type = Integer32
_SvTrunkLocalVtrkId_Object = MibTableColumn
svTrunkLocalVtrkId = _SvTrunkLocalVtrkId_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 3, 2, 1, 20),
    _SvTrunkLocalVtrkId_Type()
)
svTrunkLocalVtrkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svTrunkLocalVtrkId.setStatus("mandatory")
_SvTrunkRemVtrkId_Type = Integer32
_SvTrunkRemVtrkId_Object = MibTableColumn
svTrunkRemVtrkId = _SvTrunkRemVtrkId_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 3, 2, 1, 21),
    _SvTrunkRemVtrkId_Type()
)
svTrunkRemVtrkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svTrunkRemVtrkId.setStatus("mandatory")


class _SvTrunkRemNodeName_Type(DisplayString):
    """Custom type svTrunkRemNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SvTrunkRemNodeName_Type.__name__ = "DisplayString"
_SvTrunkRemNodeName_Object = MibTableColumn
svTrunkRemNodeName = _SvTrunkRemNodeName_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 3, 2, 1, 22),
    _SvTrunkRemNodeName_Type()
)
svTrunkRemNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svTrunkRemNodeName.setStatus("mandatory")
_LineGroup_ObjectIdentity = ObjectIdentity
lineGroup = _LineGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 4)
)
_LineTable_Object = MibTable
lineTable = _LineTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 4, 1)
)
if mibBuilder.loadTexts:
    lineTable.setStatus("mandatory")
_LineEntry_Object = MibTableRow
lineEntry = _LineEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 4, 1, 1)
)
lineEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "lineLineNumber"),
    (0, "STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "linePortNumber"),
)
if mibBuilder.loadTexts:
    lineEntry.setStatus("mandatory")
_LineSlotNumber_Type = Integer32
_LineSlotNumber_Object = MibTableColumn
lineSlotNumber = _LineSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 4, 1, 1, 2),
    _LineSlotNumber_Type()
)
lineSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineSlotNumber.setStatus("mandatory")
_LineLineNumber_Type = Integer32
_LineLineNumber_Object = MibTableColumn
lineLineNumber = _LineLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 4, 1, 1, 3),
    _LineLineNumber_Type()
)
lineLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineLineNumber.setStatus("mandatory")


class _LineCardType_Type(Integer32):
    """Custom type lineCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              21,
              25,
              29,
              41,
              106,
              107,
              110,
              111,
              117,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              220,
              221,
              222,
              223,
              224,
              225)
        )
    )
    namedValues = NamedValues(
        *(("txr", 3),
          ("cip", 21),
          ("frp", 25),
          ("cdp", 29),
          ("uxm", 41),
          ("asi-t3-2", 106),
          ("asi-e3-2", 107),
          ("asi-oc3-smf", 110),
          ("asi-oc3-mmf", 111),
          ("bxm", 117),
          ("bxm-t3-8-smf", 180),
          ("bxm-t3-8-mmf", 181),
          ("bxm-t3-8-smflr", 182),
          ("bxm-t3-8-snm", 183),
          ("bxm-t3-12-smf", 184),
          ("bxm-t3-12-mmf", 185),
          ("bxm-t3-12-smflr", 186),
          ("bxm-t3-12-snm", 187),
          ("bxm-e3-8-smf", 188),
          ("bxm-e3-8-mmf", 189),
          ("bxm-e3-8-smflr", 190),
          ("bxm-e3-8-snm", 191),
          ("bxm-e3-12-smf", 192),
          ("bxm-e3-12-mmf", 193),
          ("bxm-e3-12-smflr", 194),
          ("bxm-e3-12-snm", 195),
          ("bxm-oc3-4-smf", 196),
          ("bxm-oc3-4-mmf", 197),
          ("bxm-oc3-4-smflr", 198),
          ("bxm-oc3-4-snm", 199),
          ("bxm-oc3-8-smf", 200),
          ("bxm-oc3-8-mmf", 201),
          ("bxm-oc3-8-smflr", 202),
          ("bxm-oc3-8-snm", 203),
          ("bxm-oc12-1-smf", 204),
          ("bxm-oc12-1-mmf", 205),
          ("bxm-oc12-1-smflr", 206),
          ("bxm-oc12-1-snm", 207),
          ("bxm-oc12-2-smf", 208),
          ("bxm-oc12-2-mmf", 209),
          ("bxm-oc12-2-smflr", 210),
          ("bxm-oc12-2-snm", 211),
          ("bxm-oc3-4-stm1e", 220),
          ("bxm-oc3-8-stm1e", 221),
          ("bxm-oc3-4-xlr", 222),
          ("bxm-oc3-8-xlr", 223),
          ("bxm-oc12-1-xlr", 224),
          ("bxm-oc12-2-xlr", 225))
    )


_LineCardType_Type.__name__ = "Integer32"
_LineCardType_Object = MibTableColumn
lineCardType = _LineCardType_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 4, 1, 1, 4),
    _LineCardType_Type()
)
lineCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineCardType.setStatus("mandatory")


class _LineInterface_Type(Integer32):
    """Custom type lineInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5,
              8,
              9,
              10,
              200)
        )
    )
    namedValues = NamedValues(
        *(("t1", 1),
          ("oc3", 4),
          ("e1", 5),
          ("e3", 8),
          ("t3", 9),
          ("oc12", 10),
          ("unknown", 200))
    )


_LineInterface_Type.__name__ = "Integer32"
_LineInterface_Object = MibTableColumn
lineInterface = _LineInterface_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 4, 1, 1, 5),
    _LineInterface_Type()
)
lineInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineInterface.setStatus("mandatory")
_LineActive_Type = Active
_LineActive_Object = MibTableColumn
lineActive = _LineActive_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 4, 1, 1, 7),
    _LineActive_Type()
)
lineActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineActive.setStatus("mandatory")


class _LineStatus_Type(Integer32):
    """Custom type lineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("clear", 2),
          ("fail", 3),
          ("down", 4))
    )


_LineStatus_Type.__name__ = "Integer32"
_LineStatus_Object = MibTableColumn
lineStatus = _LineStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 4, 1, 1, 8),
    _LineStatus_Type()
)
lineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineStatus.setStatus("mandatory")
_LinePortNumber_Type = Integer32
_LinePortNumber_Object = MibTableColumn
linePortNumber = _LinePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 4, 1, 1, 9),
    _LinePortNumber_Type()
)
linePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linePortNumber.setStatus("mandatory")


class _SvNodeGrpName_Type(DisplayString):
    """Custom type svNodeGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SvNodeGrpName_Type.__name__ = "DisplayString"
_SvNodeGrpName_Object = MibScalar
svNodeGrpName = _SvNodeGrpName_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 5),
    _SvNodeGrpName_Type()
)
svNodeGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svNodeGrpName.setStatus("mandatory")


class _SvNodeGrpNetName_Type(DisplayString):
    """Custom type svNodeGrpNetName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SvNodeGrpNetName_Type.__name__ = "DisplayString"
_SvNodeGrpNetName_Object = MibScalar
svNodeGrpNetName = _SvNodeGrpNetName_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 6),
    _SvNodeGrpNetName_Type()
)
svNodeGrpNetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svNodeGrpNetName.setStatus("mandatory")


class _SvNodeGrpAlarmState_Type(Integer32):
    """Custom type svNodeGrpAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("minor", 2),
          ("major", 3),
          ("unreachable", 4))
    )


_SvNodeGrpAlarmState_Type.__name__ = "Integer32"
_SvNodeGrpAlarmState_Object = MibScalar
svNodeGrpAlarmState = _SvNodeGrpAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 7),
    _SvNodeGrpAlarmState_Type()
)
svNodeGrpAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svNodeGrpAlarmState.setStatus("mandatory")


class _SvNodeGrpGateway_Type(Integer32):
    """Custom type svNodeGrpGateway based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-a-gateway", 1),
          ("gateway", 2))
    )


_SvNodeGrpGateway_Type.__name__ = "Integer32"
_SvNodeGrpGateway_Object = MibScalar
svNodeGrpGateway = _SvNodeGrpGateway_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 8),
    _SvNodeGrpGateway_Type()
)
svNodeGrpGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svNodeGrpGateway.setStatus("mandatory")
_SvNodeGrpActive_Type = Active
_SvNodeGrpActive_Object = MibScalar
svNodeGrpActive = _SvNodeGrpActive_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 9),
    _SvNodeGrpActive_Type()
)
svNodeGrpActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svNodeGrpActive.setStatus("mandatory")


class _SvNodeGrpPlatform_Type(Integer32):
    """Custom type svNodeGrpPlatform based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("ipx-platform", 1),
          ("bpx-platform", 2),
          ("igx-platform", 3),
          ("axis-platform", 4),
          ("ins-platform", 5),
          ("vns-platform", 6),
          ("insd-platform", 7),
          ("esp-platform", 13),
          ("c3810-platform", 14))
    )


_SvNodeGrpPlatform_Type.__name__ = "Integer32"
_SvNodeGrpPlatform_Object = MibScalar
svNodeGrpPlatform = _SvNodeGrpPlatform_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 10),
    _SvNodeGrpPlatform_Type()
)
svNodeGrpPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svNodeGrpPlatform.setStatus("mandatory")


class _SvNodeGrpRelease_Type(DisplayString):
    """Custom type svNodeGrpRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SvNodeGrpRelease_Type.__name__ = "DisplayString"
_SvNodeGrpRelease_Object = MibScalar
svNodeGrpRelease = _SvNodeGrpRelease_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 11),
    _SvNodeGrpRelease_Type()
)
svNodeGrpRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svNodeGrpRelease.setStatus("mandatory")
_SvNodeFsIncRate_Type = Integer32
_SvNodeFsIncRate_Object = MibScalar
svNodeFsIncRate = _SvNodeFsIncRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 12),
    _SvNodeFsIncRate_Type()
)
svNodeFsIncRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svNodeFsIncRate.setStatus("mandatory")
_SvNodeFsDecRate_Type = Integer32
_SvNodeFsDecRate_Object = MibScalar
svNodeFsDecRate = _SvNodeFsDecRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 13),
    _SvNodeFsDecRate_Type()
)
svNodeFsDecRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svNodeFsDecRate.setStatus("mandatory")
_SvNodeFsFastRate_Type = Integer32
_SvNodeFsFastRate_Object = MibScalar
svNodeFsFastRate = _SvNodeFsFastRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 14),
    _SvNodeFsFastRate_Type()
)
svNodeFsFastRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svNodeFsFastRate.setStatus("mandatory")
_SvNodeRstTimeout_Type = Integer32
_SvNodeRstTimeout_Object = MibScalar
svNodeRstTimeout = _SvNodeRstTimeout_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 15),
    _SvNodeRstTimeout_Type()
)
svNodeRstTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svNodeRstTimeout.setStatus("mandatory")


class _SvNodeSubtype_Type(Integer32):
    """Custom type svNodeSubtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("routing-node", 1),
          ("feeder-node", 2),
          ("access-node", 3))
    )


_SvNodeSubtype_Type.__name__ = "Integer32"
_SvNodeSubtype_Object = MibScalar
svNodeSubtype = _SvNodeSubtype_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 16),
    _SvNodeSubtype_Type()
)
svNodeSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svNodeSubtype.setStatus("mandatory")
_SvNodeTable_Object = MibTable
svNodeTable = _SvNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 20)
)
if mibBuilder.loadTexts:
    svNodeTable.setStatus("mandatory")
_SvNodeEntry_Object = MibTableRow
svNodeEntry = _SvNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 20, 1)
)
svNodeEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svNodeNetworkName"),
    (0, "STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svNodeName"),
)
if mibBuilder.loadTexts:
    svNodeEntry.setStatus("mandatory")


class _SvNodeNetworkName_Type(DisplayString):
    """Custom type svNodeNetworkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SvNodeNetworkName_Type.__name__ = "DisplayString"
_SvNodeNetworkName_Object = MibTableColumn
svNodeNetworkName = _SvNodeNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 20, 1, 1),
    _SvNodeNetworkName_Type()
)
svNodeNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svNodeNetworkName.setStatus("mandatory")


class _SvNodeName_Type(DisplayString):
    """Custom type svNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SvNodeName_Type.__name__ = "DisplayString"
_SvNodeName_Object = MibTableColumn
svNodeName = _SvNodeName_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 20, 1, 2),
    _SvNodeName_Type()
)
svNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svNodeName.setStatus("mandatory")
_SvNodeIpAddress_Type = IpAddress
_SvNodeIpAddress_Object = MibScalar
svNodeIpAddress = _SvNodeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 1, 21),
    _SvNodeIpAddress_Type()
)
svNodeIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svNodeIpAddress.setStatus("mandatory")
_SvNetworkGroup_ObjectIdentity = ObjectIdentity
svNetworkGroup = _SvNetworkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 2)
)
_SvNetworkTable_Object = MibTable
svNetworkTable = _SvNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 2, 1)
)
if mibBuilder.loadTexts:
    svNetworkTable.setStatus("mandatory")
_SvNetworkEntry_Object = MibTableRow
svNetworkEntry = _SvNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 2, 1, 1)
)
svNetworkEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svNetworkName"),
)
if mibBuilder.loadTexts:
    svNetworkEntry.setStatus("mandatory")


class _SvNetworkName_Type(DisplayString):
    """Custom type svNetworkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SvNetworkName_Type.__name__ = "DisplayString"
_SvNetworkName_Object = MibTableColumn
svNetworkName = _SvNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 2, 1, 1, 1),
    _SvNetworkName_Type()
)
svNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svNetworkName.setStatus("mandatory")
_SvNetworkId_Type = Integer32
_SvNetworkId_Object = MibTableColumn
svNetworkId = _SvNetworkId_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 2, 1, 1, 2),
    _SvNetworkId_Type()
)
svNetworkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svNetworkId.setStatus("mandatory")
_SvNetworkIpxId_Type = Integer32
_SvNetworkIpxId_Object = MibTableColumn
svNetworkIpxId = _SvNetworkIpxId_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 100, 2, 1, 1, 3),
    _SvNetworkIpxId_Type()
)
svNetworkIpxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svNetworkIpxId.setStatus("mandatory")
_AagTrapsGroup_ObjectIdentity = ObjectIdentity
aagTrapsGroup = _AagTrapsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 1, 102)
)


class _TrapSeverity_Type(Integer32):
    """Custom type trapSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("warning", 2),
          ("minor", 3),
          ("major", 4),
          ("critical", 5),
          ("info", 6))
    )


_TrapSeverity_Type.__name__ = "Integer32"
_TrapSeverity_Object = MibScalar
trapSeverity = _TrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 102, 1),
    _TrapSeverity_Type()
)
trapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSeverity.setStatus("mandatory")


class _TrapReason_Type(Integer32):
    """Custom type trapReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              83,
              84,
              85,
              86,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              997,
              998,
              999,
              1001,
              1002,
              1003,
              1004,
              2001,
              2002,
              2003,
              3001,
              3002,
              3003,
              3004,
              3005,
              3006,
              3007,
              3008,
              3009,
              3010,
              3011,
              3012,
              3013,
              3014,
              3015,
              3016,
              3017,
              3018,
              3019,
              3020,
              3021,
              3022,
              3023,
              3024,
              3025,
              3026,
              3027,
              3028,
              3029,
              3030,
              3031,
              3032,
              3035,
              3036,
              3037,
              3038,
              3039,
              3040,
              3041,
              3042,
              3043,
              3044,
              3045,
              3046,
              3047,
              3048,
              3049,
              3050,
              3051,
              3052,
              3053,
              3054,
              3055,
              3056,
              3057,
              3058,
              3059,
              3060,
              3061,
              3062,
              3063,
              3064,
              3065,
              3066,
              3067,
              3068,
              3069,
              3070,
              3071,
              3072,
              3073,
              3074,
              3075,
              3076,
              3077,
              3078,
              3079,
              3080,
              3081,
              3082,
              3083,
              3084,
              3085,
              3086,
              3087,
              3088,
              3089,
              3090,
              3091,
              3092,
              3093,
              3094,
              3095,
              3096,
              3097,
              3098,
              3099,
              3100,
              3101,
              3102,
              3103,
              3104,
              3105,
              3106,
              3109,
              4001,
              4002,
              4003,
              4004,
              4005,
              4006,
              4007,
              4008,
              4009,
              4010,
              5001,
              5002,
              5003,
              5004,
              5005,
              5006,
              5007,
              5008,
              5009,
              5010,
              5011,
              5012,
              5013,
              5014,
              5015,
              5016,
              5017,
              5018)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("deactivated", 2),
          ("activated", 3),
          ("bipolar-violations", 4),
          ("tx-voice-packets-dropped", 5),
          ("tx-ts-packets-dropped", 6),
          ("tx-bda-packets", 7),
          ("tx-bdb-packets", 8),
          ("frames-slips", 9),
          ("frames-bit-errors", 10),
          ("packet-out-of-frames", 11),
          ("out-of-frames", 12),
          ("losses-of-signal", 13),
          ("bad-clock-errors", 14),
          ("crc-errors", 15),
          ("tx-nts-packets", 16),
          ("packet-crc-errors", 17),
          ("out-of-multi-frames", 18),
          ("all-ones-in-timeslot-16", 19),
          ("line-code-violations", 20),
          ("line-parity-errors", 21),
          ("path-parity-errors", 22),
          ("bip-8-code-violations", 23),
          ("rx-voice-pkts-dropped", 24),
          ("rx-ts-pkts-dropped", 25),
          ("rx-bda-pkts-dropped", 26),
          ("rx-bdb-pkts-dropped", 27),
          ("rx-nts-pkts-dropped", 28),
          ("rx-hi-pri-pkts-dropped", 29),
          ("atm-cell-header-hec-errs", 30),
          ("frame-sync-errors", 31),
          ("rx-spacer-pkts-drpd", 32),
          ("bad-clock-path", 33),
          ("bad-clock-source", 34),
          ("communication-failure", 35),
          ("looped-back", 36),
          ("remote-cga", 37),
          ("remote-framing", 38),
          ("rmt-oom", 39),
          ("remote-alarm", 40),
          ("remote-yellow", 41),
          ("remote-e3-ferf", 42),
          ("path-yellow", 43),
          ("rmt-oof", 44),
          ("local-cga", 45),
          ("frame-sync-alarm", 46),
          ("out-of-mfm", 47),
          ("loss-of-cell", 48),
          ("loss-of-pointer", 49),
          ("path-ais", 50),
          ("ais-16", 51),
          ("out-of-pkt-frm", 52),
          ("frm-err-rate", 53),
          ("ais", 54),
          ("out-of-frm", 55),
          ("loss-of-signal", 56),
          ("bad-clock", 57),
          ("txr-missing", 58),
          ("pic-missing", 59),
          ("backcard-missing", 60),
          ("cip-missing", 61),
          ("ntc-missing", 62),
          ("cdp-missing", 63),
          ("frp-missing", 64),
          ("atm-missing", 65),
          ("bni-t3-missing", 66),
          ("bni-e3-missing", 67),
          ("asi-t3-missing", 68),
          ("asi-e3-missing", 69),
          ("ait-missing", 70),
          ("asi0-t3-missing", 71),
          ("asi0-e3-missing", 72),
          ("asi-oc3-missing", 73),
          ("bni-oc3-missing", 74),
          ("ftc-missing", 75),
          ("bxm-missing", 76),
          ("btm-hp-missing", 77),
          ("path-trace-failure", 78),
          ("section-trace-failure", 79),
          ("cgw-discard-pkts", 80),
          ("cgw-discard-cells", 81),
          ("tx-hp-cells-dropped", 83),
          ("tx-vbr-cells-dropped", 84),
          ("tx-ubr-abr-cells-dropped", 85),
          ("tx-cbr-cells-dropped", 86),
          ("rmt-path-trace-failure", 91),
          ("rmt-section-trace-failure", 92),
          ("qbin-tx-nts-cells-discarded", 93),
          ("qbin-tx-hi-pri-cells-discarded", 94),
          ("qbin-tx-voice-cells-discarded", 95),
          ("qbin-tx-ts-cells-discarded", 96),
          ("qbin-tx-bdata-a-cells-discarded", 97),
          ("qbin-tx-bdata-b-cells-discarded", 98),
          ("qbin-tx-vbr-cells-discarded", 99),
          ("qbin-tx-abr-cells-discarded", 100),
          ("qbin-tx-cbr-cells-discarded", 101),
          ("inverse-mux-failure", 102),
          ("inverse-mux-link-disabled", 103),
          ("front-card-missing", 104),
          ("card-mismatch", 105),
          ("comm-break-node-degraded", 997),
          ("comm-break-clear", 998),
          ("comm-break-alarm", 999),
          ("port-communication-failure", 1001),
          ("communication-failure-cleared", 1002),
          ("ftc-communication-failure", 1003),
          ("ftc-communication-failure-cleared", 1004),
          ("connection-failed", 2001),
          ("connection-down", 2002),
          ("connection-clear", 2003),
          ("programming-aborted", 3001),
          ("failure-cleared", 3002),
          ("intermittent-failure", 3003),
          ("failed", 3004),
          ("failed-no-backup-available", 3005),
          ("failed-activated-backup", 3006),
          ("missing-card-freed", 3007),
          ("removed", 3008),
          ("removed-no-backup-available", 3009),
          ("removed-activated-failed-backup", 3010),
          ("failed-card-removed", 3011),
          ("failed-card-removed-no-backup-available", 3012),
          ("failed-card-removed-activated-failed-backup", 3013),
          ("hardware-failure", 3014),
          ("hardware-failure-no-backup-available", 3015),
          ("hardware-failure-activated-backup", 3016),
          ("hardware-failure-activated-failed-backup", 3017),
          ("failed-due-to-hardware-failure", 3018),
          ("failed-due-to-hardware-failure-no-backup-available", 3019),
          ("failed-due-to-hardware-failure-activated-backup", 3020),
          ("failed-due-to-hardware-failure-activ-failed-backup", 3021),
          ("power-supply-monitor-hardware-failure", 3022),
          ("failed-power-supply-monitor-hardware-failure", 3023),
          ("asm-hardware-failure", 3024),
          ("card-inserted", 3025),
          ("failed-card-inserted", 3026),
          ("power-supply-monitor-failure-cleared", 3027),
          ("asm-failure-cleared", 3028),
          ("power-supply-monitor-intermittent-failure", 3029),
          ("asm-intermittent-failure", 3030),
          ("power-supply-monitor-failed", 3031),
          ("asm-failed", 3032),
          ("power-supply-monitor-inserted", 3035),
          ("asm-inserted", 3036),
          ("power-supply-monitor-removed", 3037),
          ("failed-power-supply-monitor-removed", 3038),
          ("asm-removed", 3039),
          ("failed-asm-removed", 3040),
          ("bus-failed", 3041),
          ("bus-failed-no-backup-available", 3042),
          ("bus-failed-activated-backup", 3043),
          ("bus-failed-activated-failed-backup", 3044),
          ("card-not-responding", 3045),
          ("failed-card-freed", 3046),
          ("card-freed", 3047),
          ("card-sar-failure", 3048),
          ("card-sar-clear", 3049),
          ("card-up-failure", 3050),
          ("card-up-clear", 3051),
          ("card-arbiter-failure", 3052),
          ("card-arbiter-clear", 3053),
          ("card-down", 3054),
          ("card-standby", 3055),
          ("card-active", 3056),
          ("card-update", 3057),
          ("card-cleared", 3058),
          ("card-unavailable", 3059),
          ("card-downloading", 3060),
          ("card-downloader", 3061),
          ("card-downloaded", 3062),
          ("card-program", 3063),
          ("card-upgrading", 3064),
          ("card-upgraded", 3065),
          ("card-mismatch1", 3066),
          ("card-frozen", 3067),
          ("controlcard-restarted", 3068),
          ("controlcard-restarted-probe-reset", 3069),
          ("controlcard-restarted-system-reset", 3070),
          ("controlcard-restarted-powerfailure", 3071),
          ("controlcard-restarted-watchdog-timeout", 3072),
          ("controlcard-restarted-software-abort", 3073),
          ("controlcard-restarted-switchover", 3074),
          ("controlcard-restarted-clear-all-config", 3075),
          ("controlcard-restarted-user-reset-request", 3076),
          ("controlcard-restarted-reset-request", 3077),
          ("controlcard-restarted-reset-bus-diagnostics", 3078),
          ("controlcard-restarted-bus-diagnostics", 3079),
          ("controlcard-restarted-manual-bus-diagnostics", 3080),
          ("controlcard-restarted-bus-diag-cc-switch", 3081),
          ("controlcard-restarted-clear-partial-config", 3082),
          ("controlcard-restarted-cc-failure", 3083),
          ("controlcard-restarted-incomplete-nvc-memory", 3084),
          ("controlcard-restarted-primary-revision-change", 3085),
          ("controlcard-restarted-revision-change", 3086),
          ("controlcard-restarted-bad-crc", 3087),
          ("controlcard-restarted-completed-download", 3088),
          ("controlcard-restarted-configuration-restoral", 3089),
          ("controlcard-restarted-soft-reset", 3090),
          ("controlcard-restarted-rebuild-fail", 3091),
          ("controlcard-restarted-y-redundancy-alarm", 3092),
          ("controlcard-restarted-cc-redundancy-alarm", 3093),
          ("standby-PRBS-err", 3094),
          ("rx-invalid-port-err", 3095),
          ("poll-A-parity-err", 3096),
          ("poll-B-parity-err", 3097),
          ("bad-grant-err", 3098),
          ("tx-bip-16-err", 3099),
          ("rx-bip-16-err", 3100),
          ("bframe-parity-err", 3101),
          ("siu-phase-err", 3102),
          ("rx-fifo-sync-err", 3103),
          ("polling-clock-err", 3104),
          ("clock-192-err", 3105),
          ("suspected-card-failure", 3106),
          ("informational-message", 3109),
          ("power-supply-clear", 4001),
          ("power-supply-failed", 4002),
          ("power-supply-removed", 4003),
          ("failed-power-supply-removed", 4004),
          ("power-supply-hardware-failure", 4005),
          ("power-supply-inserted", 4006),
          ("cabinet-fans-alarm", 4007),
          ("cabinet-temperature-alarm", 4008),
          ("cabinet-fan-alarm-cleared", 4009),
          ("cabinet-temperature-alarm-cleared", 4010),
          ("ipx-fdr-communication-failure", 5001),
          ("axis-fdr-communication-failure", 5002),
          ("ipx-hub-communication-failure", 5003),
          ("bpx-hub-communication-failure", 5004),
          ("ipx-fdr-alarm-cleared", 5005),
          ("axis-fdr-alarm-cleared", 5006),
          ("ipx-hub-alarm-cleared", 5007),
          ("bpx-hub-alarm-cleared", 5008),
          ("ipx-fdr-major-alarm", 5009),
          ("axis-fdr-major-alarm", 5010),
          ("ipx-hub-major-alarm", 5011),
          ("bpx-hub-major-alarm", 5012),
          ("igx-hub-communication-failure", 5013),
          ("igx-hub-alarm-cleared", 5014),
          ("igx-hub-major-alarm", 5015),
          ("igx-fdr-communication-failure", 5016),
          ("igx-fdr-alarm-cleared", 5017),
          ("igx-fdr-major-alarm", 5018))
    )


_TrapReason_Type.__name__ = "Integer32"
_TrapReason_Object = MibScalar
trapReason = _TrapReason_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 102, 2),
    _TrapReason_Type()
)
trapReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapReason.setStatus("mandatory")
_TrapConnEndPointString_Type = DisplayString
_TrapConnEndPointString_Object = MibScalar
trapConnEndPointString = _TrapConnEndPointString_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 102, 3),
    _TrapConnEndPointString_Type()
)
trapConnEndPointString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapConnEndPointString.setStatus("mandatory")
_TrapLineIdString_Type = DisplayString
_TrapLineIdString_Object = MibScalar
trapLineIdString = _TrapLineIdString_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 102, 4),
    _TrapLineIdString_Type()
)
trapLineIdString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapLineIdString.setStatus("mandatory")


class _TrapTrunkType_Type(Integer32):
    """Custom type trapTrunkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("physical-trunk", 2),
          ("virtual-trunk", 3),
          ("feeder-trunk", 4),
          ("ima-trunk", 5))
    )


_TrapTrunkType_Type.__name__ = "Integer32"
_TrapTrunkType_Object = MibScalar
trapTrunkType = _TrapTrunkType_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 102, 5),
    _TrapTrunkType_Type()
)
trapTrunkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapTrunkType.setStatus("mandatory")
_TrapVirtualTrunkId_Type = Integer32
_TrapVirtualTrunkId_Object = MibScalar
trapVirtualTrunkId = _TrapVirtualTrunkId_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 102, 6),
    _TrapVirtualTrunkId_Type()
)
trapVirtualTrunkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapVirtualTrunkId.setStatus("mandatory")
_TrapTrunkIdString_Type = DisplayString
_TrapTrunkIdString_Object = MibScalar
trapTrunkIdString = _TrapTrunkIdString_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 102, 7),
    _TrapTrunkIdString_Type()
)
trapTrunkIdString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapTrunkIdString.setStatus("mandatory")
_TrapPortIdString_Type = DisplayString
_TrapPortIdString_Object = MibScalar
trapPortIdString = _TrapPortIdString_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 102, 8),
    _TrapPortIdString_Type()
)
trapPortIdString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapPortIdString.setStatus("mandatory")


class _TrapCardStatus_Type(Integer32):
    """Custom type trapCardStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("failed", 2),
          ("down", 3),
          ("standby", 4),
          ("mismatch", 5),
          ("failed-no-backup", 6),
          ("no-card", 7),
          ("update", 8),
          ("cleared", 9),
          ("unavailable", 10),
          ("downloading", 11),
          ("downloader", 12),
          ("downloaded", 13),
          ("locked", 14),
          ("program", 15),
          ("upgrading", 16),
          ("upgraded", 17),
          ("frozen", 18))
    )


_TrapCardStatus_Type.__name__ = "Integer32"
_TrapCardStatus_Object = MibScalar
trapCardStatus = _TrapCardStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 102, 9),
    _TrapCardStatus_Type()
)
trapCardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapCardStatus.setStatus("mandatory")


class _TrapCardType_Type(Integer32):
    """Custom type trapCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              117,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              220,
              221,
              222,
              223,
              224,
              225)
        )
    )
    namedValues = NamedValues(
        *(("ipx-pcc", 1),
          ("vdp", 2),
          ("txr", 3),
          ("pic", 4),
          ("vcd", 5),
          ("vdp-vcd", 6),
          ("psm", 7),
          ("ps", 8),
          ("sdp", 9),
          ("bslot", 10),
          ("mback", 11),
          ("sdp-back-cd", 12),
          ("txr2", 13),
          ("xdp", 14),
          ("ldp", 15),
          ("xdp-back-cd", 16),
          ("ldp-back-cd", 17),
          ("sback-cd", 18),
          ("lback-cd", 19),
          ("fdp", 20),
          ("cip", 21),
          ("ntc", 22),
          ("uback-cd", 23),
          ("uni", 24),
          ("frp", 25),
          ("fback-cd", 26),
          ("frp-back-cd", 27),
          ("mt3", 28),
          ("cdp", 29),
          ("e1t1-port", 30),
          ("atm", 31),
          ("npc", 32),
          ("arc", 33),
          ("ait", 34),
          ("ftc", 35),
          ("ftcback-cd", 36),
          ("ufm1", 37),
          ("ufm1-u", 38),
          ("btm-hp", 39),
          ("bcc", 101),
          ("asm", 102),
          ("bni-t3", 103),
          ("bin-e3", 104),
          ("mfrp", 105),
          ("asi-t3-2", 106),
          ("asi-e3-2", 107),
          ("asi0-t3", 108),
          ("asi0-e3", 109),
          ("bni-oc3", 110),
          ("asi-oc3", 111),
          ("bpx-bslot", 112),
          ("bcc3", 113),
          ("unknown", 114),
          ("bxm", 117),
          ("bxm-t3-8-smf", 180),
          ("bxm-t3-8-mmf", 181),
          ("bxm-t3-8-smflr", 182),
          ("bxm-t3-8-snm", 183),
          ("bxm-t3-12-smf", 184),
          ("bxm-t3-12-mmf", 185),
          ("bxm-t3-12-smflr", 186),
          ("bxm-t3-12-snm", 187),
          ("bxm-e3-8-smf", 188),
          ("bxm-e3-8-mmf", 189),
          ("bxm-e3-8-smflr", 190),
          ("bxm-e3-8-snm", 191),
          ("bxm-e3-12-smf", 192),
          ("bxm-e3-12-mmf", 193),
          ("bxm-e3-12-smflr", 194),
          ("bxm-e3-12-snm", 195),
          ("bxm-oc3-4-smf", 196),
          ("bxm-oc3-4-mmf", 197),
          ("bxm-oc3-4-smflr", 198),
          ("bxm-oc3-4-snm", 199),
          ("bxm-oc3-8-smf", 200),
          ("bxm-oc3-8-mmf", 201),
          ("bxm-oc3-8-smflr", 202),
          ("bxm-oc3-8-snm", 203),
          ("bxm-oc12-1-smf", 204),
          ("bxm-oc12-1-mmf", 205),
          ("bxm-oc12-1-smflr", 206),
          ("bxm-oc12-1-snm", 207),
          ("bxm-oc12-2-smf", 208),
          ("bxm-oc12-2-mmf", 209),
          ("bxm-oc12-2-smflr", 210),
          ("bxm-oc12-2-snm", 211),
          ("bxm-oc3-4-stm1e", 220),
          ("bxm-oc3-8-stm1e", 221),
          ("bxm-oc3-4-xlr", 222),
          ("bxm-oc3-8-xlr", 223),
          ("bxm-oc12-1-xlr", 224),
          ("bxm-oc12-2-xlr", 225))
    )


_TrapCardType_Type.__name__ = "Integer32"
_TrapCardType_Object = MibScalar
trapCardType = _TrapCardType_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 102, 10),
    _TrapCardType_Type()
)
trapCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapCardType.setStatus("mandatory")
_TrapCardSlotNumber_Type = Integer32
_TrapCardSlotNumber_Object = MibScalar
trapCardSlotNumber = _TrapCardSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 102, 11),
    _TrapCardSlotNumber_Type()
)
trapCardSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapCardSlotNumber.setStatus("mandatory")


class _TrapPeripheralType_Type(Integer32):
    """Custom type trapPeripheralType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("power-supply", 2),
          ("cabinate-fan", 3),
          ("local-bus", 4),
          ("temperature-sensor", 5))
    )


_TrapPeripheralType_Type.__name__ = "Integer32"
_TrapPeripheralType_Object = MibScalar
trapPeripheralType = _TrapPeripheralType_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 102, 12),
    _TrapPeripheralType_Type()
)
trapPeripheralType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapPeripheralType.setStatus("mandatory")


class _TrapPeripheralStatus_Type(Integer32):
    """Custom type trapPeripheralStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("failed", 2))
    )


_TrapPeripheralStatus_Type.__name__ = "Integer32"
_TrapPeripheralStatus_Object = MibScalar
trapPeripheralStatus = _TrapPeripheralStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 102, 13),
    _TrapPeripheralStatus_Type()
)
trapPeripheralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapPeripheralStatus.setStatus("mandatory")
_TrapPeripheralUnitNumber_Type = Integer32
_TrapPeripheralUnitNumber_Object = MibScalar
trapPeripheralUnitNumber = _TrapPeripheralUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 102, 14),
    _TrapPeripheralUnitNumber_Type()
)
trapPeripheralUnitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapPeripheralUnitNumber.setStatus("mandatory")


class _TrapFeederStatus_Type(Integer32):
    """Custom type trapFeederStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("failed", 2))
    )


_TrapFeederStatus_Type.__name__ = "Integer32"
_TrapFeederStatus_Object = MibScalar
trapFeederStatus = _TrapFeederStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 102, 15),
    _TrapFeederStatus_Type()
)
trapFeederStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapFeederStatus.setStatus("mandatory")


class _TrapPhysicalLineIdString_Type(DisplayString):
    """Custom type trapPhysicalLineIdString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_TrapPhysicalLineIdString_Type.__name__ = "DisplayString"
_TrapPhysicalLineIdString_Object = MibScalar
trapPhysicalLineIdString = _TrapPhysicalLineIdString_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 102, 16),
    _TrapPhysicalLineIdString_Type()
)
trapPhysicalLineIdString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapPhysicalLineIdString.setStatus("mandatory")


class _TrapCommBreakNode_Type(DisplayString):
    """Custom type trapCommBreakNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_TrapCommBreakNode_Type.__name__ = "DisplayString"
_TrapCommBreakNode_Object = MibScalar
trapCommBreakNode = _TrapCommBreakNode_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 102, 17),
    _TrapCommBreakNode_Type()
)
trapCommBreakNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapCommBreakNode.setStatus("mandatory")


class _TrapCommBreakRptNode_Type(DisplayString):
    """Custom type trapCommBreakRptNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_TrapCommBreakRptNode_Type.__name__ = "DisplayString"
_TrapCommBreakRptNode_Object = MibScalar
trapCommBreakRptNode = _TrapCommBreakRptNode_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 102, 18),
    _TrapCommBreakRptNode_Type()
)
trapCommBreakRptNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapCommBreakRptNode.setStatus("mandatory")
_TrapOccurTime_Type = DisplayString
_TrapOccurTime_Object = MibScalar
trapOccurTime = _TrapOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 102, 20),
    _TrapOccurTime_Type()
)
trapOccurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapOccurTime.setStatus("mandatory")
_TrapMsgFormatTime_Type = DisplayString
_TrapMsgFormatTime_Object = MibScalar
trapMsgFormatTime = _TrapMsgFormatTime_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 102, 21),
    _TrapMsgFormatTime_Type()
)
trapMsgFormatTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapMsgFormatTime.setStatus("mandatory")
_TrapTimeZone_Type = DisplayString
_TrapTimeZone_Object = MibScalar
trapTimeZone = _TrapTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 102, 22),
    _TrapTimeZone_Type()
)
trapTimeZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapTimeZone.setStatus("mandatory")
_TrapSeverityStr_Type = DisplayString
_TrapSeverityStr_Object = MibScalar
trapSeverityStr = _TrapSeverityStr_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 102, 23),
    _TrapSeverityStr_Type()
)
trapSeverityStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSeverityStr.setStatus("mandatory")


class _TrapMsgStr_Type(DisplayString):
    """Custom type trapMsgStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TrapMsgStr_Type.__name__ = "DisplayString"
_TrapMsgStr_Object = MibScalar
trapMsgStr = _TrapMsgStr_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 102, 24),
    _TrapMsgStr_Type()
)
trapMsgStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapMsgStr.setStatus("mandatory")
_Rtm_ObjectIdentity = ObjectIdentity
rtm = _Rtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 120)
)
_TrapsConfig_ObjectIdentity = ObjectIdentity
trapsConfig = _TrapsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 120, 1)
)
_TrapConfigTable_Object = MibTable
trapConfigTable = _TrapConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 1)
)
if mibBuilder.loadTexts:
    trapConfigTable.setStatus("mandatory")
_TrapConfigEntry_Object = MibTableRow
trapConfigEntry = _TrapConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1)
)
trapConfigEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "managerIPaddress"),
)
if mibBuilder.loadTexts:
    trapConfigEntry.setStatus("mandatory")
_ManagerIPaddress_Type = IpAddress
_ManagerIPaddress_Object = MibTableColumn
managerIPaddress = _ManagerIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1, 1),
    _ManagerIPaddress_Type()
)
managerIPaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managerIPaddress.setStatus("mandatory")
_ManagerPortNumber_Type = Integer32
_ManagerPortNumber_Object = MibTableColumn
managerPortNumber = _ManagerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1, 2),
    _ManagerPortNumber_Type()
)
managerPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managerPortNumber.setStatus("mandatory")


class _ManagerRowStatus_Type(Integer32):
    """Custom type managerRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("addRow", 1),
          ("delRow", 2))
    )


_ManagerRowStatus_Type.__name__ = "Integer32"
_ManagerRowStatus_Object = MibTableColumn
managerRowStatus = _ManagerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1, 3),
    _ManagerRowStatus_Type()
)
managerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managerRowStatus.setStatus("mandatory")


class _ReadingTrapFlag_Type(Integer32):
    """Custom type readingTrapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_ReadingTrapFlag_Type.__name__ = "Integer32"
_ReadingTrapFlag_Object = MibTableColumn
readingTrapFlag = _ReadingTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1, 4),
    _ReadingTrapFlag_Type()
)
readingTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    readingTrapFlag.setStatus("mandatory")
_NextTrapSeqNum_Type = Integer32
_NextTrapSeqNum_Object = MibTableColumn
nextTrapSeqNum = _NextTrapSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1, 5),
    _NextTrapSeqNum_Type()
)
nextTrapSeqNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nextTrapSeqNum.setStatus("mandatory")


class _ManagerNumOfValidEntries_Type(Integer32):
    """Custom type managerNumOfValidEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ManagerNumOfValidEntries_Type.__name__ = "Integer32"
_ManagerNumOfValidEntries_Object = MibScalar
managerNumOfValidEntries = _ManagerNumOfValidEntries_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 2),
    _ManagerNumOfValidEntries_Type()
)
managerNumOfValidEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managerNumOfValidEntries.setStatus("mandatory")
_LastSequenceNumber_Type = Integer32
_LastSequenceNumber_Object = MibScalar
lastSequenceNumber = _LastSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 3),
    _LastSequenceNumber_Type()
)
lastSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastSequenceNumber.setStatus("mandatory")
_TrapUploadTable_Object = MibTable
trapUploadTable = _TrapUploadTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 4)
)
if mibBuilder.loadTexts:
    trapUploadTable.setStatus("mandatory")
_TrapUploadEntry_Object = MibTableRow
trapUploadEntry = _TrapUploadEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 4, 1)
)
trapUploadEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "mgrIpAddress"),
)
if mibBuilder.loadTexts:
    trapUploadEntry.setStatus("mandatory")
_MgrIpAddress_Type = IpAddress
_MgrIpAddress_Object = MibTableColumn
mgrIpAddress = _MgrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 4, 1, 1),
    _MgrIpAddress_Type()
)
mgrIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgrIpAddress.setStatus("mandatory")
_TrapSequenceNum_Type = Integer32
_TrapSequenceNum_Object = MibTableColumn
trapSequenceNum = _TrapSequenceNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 4, 1, 2),
    _TrapSequenceNum_Type()
)
trapSequenceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSequenceNum.setStatus("mandatory")
_TrapPduString_Type = OctetString
_TrapPduString_Object = MibTableColumn
trapPduString = _TrapPduString_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 4, 1, 3),
    _TrapPduString_Type()
)
trapPduString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapPduString.setStatus("mandatory")


class _EndOfQueueFlag_Type(Integer32):
    """Custom type endOfQueueFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_EndOfQueueFlag_Type.__name__ = "Integer32"
_EndOfQueueFlag_Object = MibTableColumn
endOfQueueFlag = _EndOfQueueFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 4, 1, 4),
    _EndOfQueueFlag_Type()
)
endOfQueueFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfQueueFlag.setStatus("mandatory")
_StrataviewEvents_ObjectIdentity = ObjectIdentity
strataviewEvents = _StrataviewEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 920)
)

# Managed Objects groups


# Notification objects

normalSwitchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 1004)
)
normalSwitchEvent.setObjects(
      *(("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svNodeGrpNetName"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svNodeGrpName"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapOccurTime"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapMsgFormatTime"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapTimeZone"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapSeverityStr"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapMsgStr"))
)
if mibBuilder.loadTexts:
    normalSwitchEvent.setStatus(
        ""
    )

minorSwitchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 1005)
)
minorSwitchEvent.setObjects(
      *(("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svNodeGrpNetName"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svNodeGrpName"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapOccurTime"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapMsgFormatTime"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapTimeZone"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapSeverityStr"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapMsgStr"))
)
if mibBuilder.loadTexts:
    minorSwitchEvent.setStatus(
        ""
    )

majorSwitchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 1006)
)
majorSwitchEvent.setObjects(
      *(("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svNodeGrpNetName"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svNodeGrpName"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapOccurTime"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapMsgFormatTime"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapTimeZone"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapSeverityStr"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapMsgStr"))
)
if mibBuilder.loadTexts:
    majorSwitchEvent.setStatus(
        ""
    )

criticalSwitchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 1007)
)
criticalSwitchEvent.setObjects(
      *(("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svNodeGrpNetName"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svNodeGrpName"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapOccurTime"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapMsgFormatTime"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapTimeZone"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapSeverityStr"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapMsgStr"))
)
if mibBuilder.loadTexts:
    criticalSwitchEvent.setStatus(
        ""
    )

connectionAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 20000)
)
connectionAlarm.setObjects(
      *(("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "lastSequenceNumber"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svNodeGrpName"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapSeverity"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapReason"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svConnOpStatus"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svConnType"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapConnEndPointString"))
)
if mibBuilder.loadTexts:
    connectionAlarm.setStatus(
        ""
    )

lineAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 20001)
)
lineAlarm.setObjects(
      *(("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "lastSequenceNumber"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svNodeGrpName"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapSeverity"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapReason"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "lineStatus"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "lineCardType"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "lineInterface"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "lineLineNumber"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "linePortNumber"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapLineIdString"))
)
if mibBuilder.loadTexts:
    lineAlarm.setStatus(
        ""
    )

trunkAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 20002)
)
trunkAlarm.setObjects(
      *(("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "lastSequenceNumber"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svNodeGrpName"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapSeverity"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapReason"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svTrunkStatus"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svTrunkCardType"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapTrunkType"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svTrunkLocalSlot"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svTrunkLocalPort"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapVirtualTrunkId"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapTrunkIdString"))
)
if mibBuilder.loadTexts:
    trunkAlarm.setStatus(
        ""
    )

cardAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 20004)
)
cardAlarm.setObjects(
      *(("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "lastSequenceNumber"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svNodeGrpName"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapSeverity"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapReason"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapCardStatus"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapCardType"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapCardSlotNumber"))
)
if mibBuilder.loadTexts:
    cardAlarm.setStatus(
        ""
    )

peripheralAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 20005)
)
peripheralAlarm.setObjects(
      *(("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "lastSequenceNumber"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svNodeGrpName"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapSeverity"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapReason"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapPeripheralStatus"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapPeripheralType"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapPeripheralUnitNumber"))
)
if mibBuilder.loadTexts:
    peripheralAlarm.setStatus(
        ""
    )

feederAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 20008)
)
feederAlarm.setObjects(
      *(("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "lastSequenceNumber"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svNodeGrpName"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapSeverity"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapReason"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapFeederStatus"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svTrunkLocalSlot"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svTrunkLocalPort"))
)
if mibBuilder.loadTexts:
    feederAlarm.setStatus(
        ""
    )

physicalLineAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 20009)
)
physicalLineAlarm.setObjects(
      *(("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "lastSequenceNumber"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svNodeGrpName"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapSeverity"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapReason"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "lineStatus"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "lineCardType"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "lineInterface"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "lineSlotNumber"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "lineLineNumber"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "linePortNumber"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapLineIdString"))
)
if mibBuilder.loadTexts:
    physicalLineAlarm.setStatus(
        ""
    )

imaTrunkAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 20010)
)
imaTrunkAlarm.setObjects(
      *(("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "lastSequenceNumber"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svNodeGrpName"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapSeverity"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapReason"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svTrunkStatus"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svTrunkCardType"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapTrunkType"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svTrunkLocalSlot"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svTrunkLocalPort"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapVirtualTrunkId"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapTrunkIdString"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapPhysicalLineIdString"))
)
if mibBuilder.loadTexts:
    imaTrunkAlarm.setStatus(
        ""
    )

portAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 20011)
)
portAlarm.setObjects(
      *(("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "lastSequenceNumber"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svNodeGrpName"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapSeverity"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapReason"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svPortState"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapCardType"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svPortSlot"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svPortLine"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svPortPort"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svPortPhysicalPort"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapPortIdString"))
)
if mibBuilder.loadTexts:
    portAlarm.setStatus(
        ""
    )

commBreakAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 20016)
)
commBreakAlarm.setObjects(
      *(("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "lastSequenceNumber"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapCommBreakRptNode"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapCommBreakNode"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapReason"))
)
if mibBuilder.loadTexts:
    commBreakAlarm.setStatus(
        ""
    )

commBreakClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 20017)
)
commBreakClear.setObjects(
      *(("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "lastSequenceNumber"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapCommBreakRptNode"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapCommBreakNode"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapReason"))
)
if mibBuilder.loadTexts:
    commBreakClear.setStatus(
        ""
    )

newSvUserConnCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 25010)
)
newSvUserConnCleared.setObjects(
      *(("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "lastSequenceNumber"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svConnLocalEndPt"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svConnLocalStr"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svConnAlarmLocalEndNNI"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svConnRemoteEndPt"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svConnRemoteStr"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svConnAlarmRemoteEndNNI"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svConnOpStatus"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svConnAbitStatus"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svConnType"))
)
if mibBuilder.loadTexts:
    newSvUserConnCleared.setStatus(
        ""
    )

newSvUserConnFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 25011)
)
newSvUserConnFailed.setObjects(
      *(("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "lastSequenceNumber"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svConnLocalEndPt"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svConnLocalStr"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svConnAlarmLocalEndNNI"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svConnRemoteEndPt"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svConnRemoteStr"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svConnAlarmRemoteEndNNI"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svConnOpStatus"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svConnAbitStatus"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svConnType"))
)
if mibBuilder.loadTexts:
    newSvUserConnFailed.setStatus(
        ""
    )

newSvUserConnDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 25012)
)
newSvUserConnDown.setObjects(
      *(("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "lastSequenceNumber"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svConnLocalEndPt"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svConnLocalStr"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svConnAlarmLocalEndNNI"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svConnRemoteEndPt"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svConnRemoteStr"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svConnAlarmRemoteEndNNI"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svConnOpStatus"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svConnAbitStatus"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB-REL9-1", "svConnType"))
)
if mibBuilder.loadTexts:
    newSvUserConnDown.setStatus(
        ""
    )

svNodeIpUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 25300)
)
svNodeIpUnreachable.setObjects(
      *(("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "lastSequenceNumber"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svNodeGrpNetName"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svNodeGrpName"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svNodeIpAddress"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svNodeGrpPlatform"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svNodeSubtype"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapOccurTime"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapTimeZone"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapSeverity"))
)
if mibBuilder.loadTexts:
    svNodeIpUnreachable.setStatus(
        ""
    )

svNodeIpReachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 25301)
)
svNodeIpReachable.setObjects(
      *(("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "lastSequenceNumber"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svNodeGrpNetName"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svNodeGrpName"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svNodeIpAddress"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svNodeGrpPlatform"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "svNodeSubtype"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapOccurTime"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapTimeZone"),
        ("STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1", "trapSeverity"))
)
if mibBuilder.loadTexts:
    svNodeIpReachable.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STRATACOM-STRATAVIEW-NETWORK-MIB-REL9-1",
    **{"Active": Active,
       "normalSwitchEvent": normalSwitchEvent,
       "minorSwitchEvent": minorSwitchEvent,
       "majorSwitchEvent": majorSwitchEvent,
       "criticalSwitchEvent": criticalSwitchEvent,
       "connectionAlarm": connectionAlarm,
       "lineAlarm": lineAlarm,
       "trunkAlarm": trunkAlarm,
       "cardAlarm": cardAlarm,
       "peripheralAlarm": peripheralAlarm,
       "feederAlarm": feederAlarm,
       "physicalLineAlarm": physicalLineAlarm,
       "imaTrunkAlarm": imaTrunkAlarm,
       "portAlarm": portAlarm,
       "commBreakAlarm": commBreakAlarm,
       "commBreakClear": commBreakClear,
       "newSvUserConnCleared": newSvUserConnCleared,
       "newSvUserConnFailed": newSvUserConnFailed,
       "newSvUserConnDown": newSvUserConnDown,
       "svNodeIpUnreachable": svNodeIpUnreachable,
       "svNodeIpReachable": svNodeIpReachable,
       "topologyGroup": topologyGroup,
       "svNodeGroup": svNodeGroup,
       "trunkGroup": trunkGroup,
       "svTrunkTable": svTrunkTable,
       "svTrunkEntry": svTrunkEntry,
       "svTrunkLocalSlot": svTrunkLocalSlot,
       "svTrunkLocalPort": svTrunkLocalPort,
       "svTrunkLocalLine": svTrunkLocalLine,
       "svTrunkCardType": svTrunkCardType,
       "svTrunkInterface": svTrunkInterface,
       "svTrunkLineLoad": svTrunkLineLoad,
       "svTrunkRemNodeId": svTrunkRemNodeId,
       "svTrunkRemLineNumber": svTrunkRemLineNumber,
       "svTrunkRemSlot": svTrunkRemSlot,
       "svTrunkRemPort": svTrunkRemPort,
       "svTrunkAlarmState": svTrunkAlarmState,
       "svTrunkActive": svTrunkActive,
       "svTrunkStatus": svTrunkStatus,
       "svTrunkStatReserve": svTrunkStatReserve,
       "svTrunkBurstyDataBQDepth": svTrunkBurstyDataBQDepth,
       "svTrunkBurstyDataBQEfcnThreshold": svTrunkBurstyDataBQEfcnThreshold,
       "svTrunkClpHighDropThreshold": svTrunkClpHighDropThreshold,
       "svTrunkClpLowDropThreshold": svTrunkClpLowDropThreshold,
       "svTrunkLocalVtrkId": svTrunkLocalVtrkId,
       "svTrunkRemVtrkId": svTrunkRemVtrkId,
       "svTrunkRemNodeName": svTrunkRemNodeName,
       "lineGroup": lineGroup,
       "lineTable": lineTable,
       "lineEntry": lineEntry,
       "lineSlotNumber": lineSlotNumber,
       "lineLineNumber": lineLineNumber,
       "lineCardType": lineCardType,
       "lineInterface": lineInterface,
       "lineActive": lineActive,
       "lineStatus": lineStatus,
       "linePortNumber": linePortNumber,
       "svNodeGrpName": svNodeGrpName,
       "svNodeGrpNetName": svNodeGrpNetName,
       "svNodeGrpAlarmState": svNodeGrpAlarmState,
       "svNodeGrpGateway": svNodeGrpGateway,
       "svNodeGrpActive": svNodeGrpActive,
       "svNodeGrpPlatform": svNodeGrpPlatform,
       "svNodeGrpRelease": svNodeGrpRelease,
       "svNodeFsIncRate": svNodeFsIncRate,
       "svNodeFsDecRate": svNodeFsDecRate,
       "svNodeFsFastRate": svNodeFsFastRate,
       "svNodeRstTimeout": svNodeRstTimeout,
       "svNodeSubtype": svNodeSubtype,
       "svNodeTable": svNodeTable,
       "svNodeEntry": svNodeEntry,
       "svNodeNetworkName": svNodeNetworkName,
       "svNodeName": svNodeName,
       "svNodeIpAddress": svNodeIpAddress,
       "svNetworkGroup": svNetworkGroup,
       "svNetworkTable": svNetworkTable,
       "svNetworkEntry": svNetworkEntry,
       "svNetworkName": svNetworkName,
       "svNetworkId": svNetworkId,
       "svNetworkIpxId": svNetworkIpxId,
       "aagTrapsGroup": aagTrapsGroup,
       "trapSeverity": trapSeverity,
       "trapReason": trapReason,
       "trapConnEndPointString": trapConnEndPointString,
       "trapLineIdString": trapLineIdString,
       "trapTrunkType": trapTrunkType,
       "trapVirtualTrunkId": trapVirtualTrunkId,
       "trapTrunkIdString": trapTrunkIdString,
       "trapPortIdString": trapPortIdString,
       "trapCardStatus": trapCardStatus,
       "trapCardType": trapCardType,
       "trapCardSlotNumber": trapCardSlotNumber,
       "trapPeripheralType": trapPeripheralType,
       "trapPeripheralStatus": trapPeripheralStatus,
       "trapPeripheralUnitNumber": trapPeripheralUnitNumber,
       "trapFeederStatus": trapFeederStatus,
       "trapPhysicalLineIdString": trapPhysicalLineIdString,
       "trapCommBreakNode": trapCommBreakNode,
       "trapCommBreakRptNode": trapCommBreakRptNode,
       "trapOccurTime": trapOccurTime,
       "trapMsgFormatTime": trapMsgFormatTime,
       "trapTimeZone": trapTimeZone,
       "trapSeverityStr": trapSeverityStr,
       "trapMsgStr": trapMsgStr,
       "rtm": rtm,
       "trapsConfig": trapsConfig,
       "trapConfigTable": trapConfigTable,
       "trapConfigEntry": trapConfigEntry,
       "managerIPaddress": managerIPaddress,
       "managerPortNumber": managerPortNumber,
       "managerRowStatus": managerRowStatus,
       "readingTrapFlag": readingTrapFlag,
       "nextTrapSeqNum": nextTrapSeqNum,
       "managerNumOfValidEntries": managerNumOfValidEntries,
       "lastSequenceNumber": lastSequenceNumber,
       "trapUploadTable": trapUploadTable,
       "trapUploadEntry": trapUploadEntry,
       "mgrIpAddress": mgrIpAddress,
       "trapSequenceNum": trapSequenceNum,
       "trapPduString": trapPduString,
       "endOfQueueFlag": endOfQueueFlag,
       "strataviewEvents": strataviewEvents}
)
