# SNMP MIB module (SAPRIV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/schneider_3833/SAPRIV-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 20:06:19 2025
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
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Groupeschneider_ObjectIdentity = ObjectIdentity
groupeschneider = _Groupeschneider_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833)
)
_TransparentFactoryEthernet_ObjectIdentity = ObjectIdentity
transparentFactoryEthernet = _TransparentFactoryEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1)
)
_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1)
)
_SaConfiguration_ObjectIdentity = ObjectIdentity
saConfiguration = _SaConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14)
)
_SaChassis_ObjectIdentity = ObjectIdentity
saChassis = _SaChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1)
)
_SaSystemTable_ObjectIdentity = ObjectIdentity
saSystemTable = _SaSystemTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1)
)


class _SaSysProduct_Type(Integer32):
    """Custom type saSysProduct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("nes07100", 1),
          ("nos07100", 2),
          ("nes17100", 4),
          ("nos17100", 5))
    )


_SaSysProduct_Type.__name__ = "Integer32"
_SaSysProduct_Object = MibScalar
saSysProduct = _SaSysProduct_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 1),
    _SaSysProduct_Type()
)
saSysProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saSysProduct.setStatus("mandatory")
_SaSysVersion_Type = DisplayString
_SaSysVersion_Object = MibScalar
saSysVersion = _SaSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 2),
    _SaSysVersion_Type()
)
saSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saSysVersion.setStatus("mandatory")
_SaSysGroupCapacity_Type = Integer32
_SaSysGroupCapacity_Object = MibScalar
saSysGroupCapacity = _SaSysGroupCapacity_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 3),
    _SaSysGroupCapacity_Type()
)
saSysGroupCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saSysGroupCapacity.setStatus("mandatory")
_SaSysGroupMap_Type = DisplayString
_SaSysGroupMap_Object = MibScalar
saSysGroupMap = _SaSysGroupMap_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 4),
    _SaSysGroupMap_Type()
)
saSysGroupMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saSysGroupMap.setStatus("mandatory")
_SaSysMaxPowerSupply_Type = Integer32
_SaSysMaxPowerSupply_Object = MibScalar
saSysMaxPowerSupply = _SaSysMaxPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 5),
    _SaSysMaxPowerSupply_Type()
)
saSysMaxPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saSysMaxPowerSupply.setStatus("mandatory")
_SaSysMaxFan_Type = Integer32
_SaSysMaxFan_Object = MibScalar
saSysMaxFan = _SaSysMaxFan_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 6),
    _SaSysMaxFan_Type()
)
saSysMaxFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saSysMaxFan.setStatus("mandatory")
_SaSysGroupModuleCapacity_Type = Integer32
_SaSysGroupModuleCapacity_Object = MibScalar
saSysGroupModuleCapacity = _SaSysGroupModuleCapacity_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 7),
    _SaSysGroupModuleCapacity_Type()
)
saSysGroupModuleCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saSysGroupModuleCapacity.setStatus("mandatory")
_SaSysModulePortCapacity_Type = Integer32
_SaSysModulePortCapacity_Object = MibScalar
saSysModulePortCapacity = _SaSysModulePortCapacity_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 8),
    _SaSysModulePortCapacity_Type()
)
saSysModulePortCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saSysModulePortCapacity.setStatus("mandatory")
_SaSysGroupTable_Object = MibTable
saSysGroupTable = _SaSysGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 9)
)
if mibBuilder.loadTexts:
    saSysGroupTable.setStatus("mandatory")
_SaSysGroupEntry_Object = MibTableRow
saSysGroupEntry = _SaSysGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 9, 1)
)
saSysGroupEntry.setIndexNames(
    (0, "SAPRIV-MIB", "saSysGroupID"),
)
if mibBuilder.loadTexts:
    saSysGroupEntry.setStatus("mandatory")


class _SaSysGroupID_Type(Integer32):
    """Custom type saSysGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SaSysGroupID_Type.__name__ = "Integer32"
_SaSysGroupID_Object = MibTableColumn
saSysGroupID = _SaSysGroupID_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 9, 1, 1),
    _SaSysGroupID_Type()
)
saSysGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saSysGroupID.setStatus("mandatory")


class _SaSysGroupType_Type(Integer32):
    """Custom type saSysGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              20)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("m-basic4", 10),
          ("icc8", 20))
    )


_SaSysGroupType_Type.__name__ = "Integer32"
_SaSysGroupType_Object = MibTableColumn
saSysGroupType = _SaSysGroupType_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 9, 1, 2),
    _SaSysGroupType_Type()
)
saSysGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saSysGroupType.setStatus("mandatory")
_SaSysGroupDescription_Type = DisplayString
_SaSysGroupDescription_Object = MibTableColumn
saSysGroupDescription = _SaSysGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 9, 1, 3),
    _SaSysGroupDescription_Type()
)
saSysGroupDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saSysGroupDescription.setStatus("mandatory")
_SaSysGroupHwVersion_Type = DisplayString
_SaSysGroupHwVersion_Object = MibTableColumn
saSysGroupHwVersion = _SaSysGroupHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 9, 1, 4),
    _SaSysGroupHwVersion_Type()
)
saSysGroupHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saSysGroupHwVersion.setStatus("mandatory")
_SaSysGroupSwVersion_Type = DisplayString
_SaSysGroupSwVersion_Object = MibTableColumn
saSysGroupSwVersion = _SaSysGroupSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 9, 1, 5),
    _SaSysGroupSwVersion_Type()
)
saSysGroupSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saSysGroupSwVersion.setStatus("mandatory")
_SaSysGroupModuleMap_Type = DisplayString
_SaSysGroupModuleMap_Object = MibTableColumn
saSysGroupModuleMap = _SaSysGroupModuleMap_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 9, 1, 6),
    _SaSysGroupModuleMap_Type()
)
saSysGroupModuleMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saSysGroupModuleMap.setStatus("mandatory")


class _SaSysGroupAction_Type(Integer32):
    """Custom type saSysGroupAction based on Integer32"""
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
        *(("other", 1),
          ("reset", 2),
          ("resetStats", 3),
          ("resetFDB", 4))
    )


_SaSysGroupAction_Type.__name__ = "Integer32"
_SaSysGroupAction_Object = MibTableColumn
saSysGroupAction = _SaSysGroupAction_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 9, 1, 7),
    _SaSysGroupAction_Type()
)
saSysGroupAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saSysGroupAction.setStatus("mandatory")
_SaSysGroupActionResult_Type = Integer32
_SaSysGroupActionResult_Object = MibTableColumn
saSysGroupActionResult = _SaSysGroupActionResult_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 9, 1, 8),
    _SaSysGroupActionResult_Type()
)
saSysGroupActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saSysGroupActionResult.setStatus("mandatory")
_SaSysModuleTable_Object = MibTable
saSysModuleTable = _SaSysModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 10)
)
if mibBuilder.loadTexts:
    saSysModuleTable.setStatus("mandatory")
_SaSysModuleEntry_Object = MibTableRow
saSysModuleEntry = _SaSysModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 10, 1)
)
saSysModuleEntry.setIndexNames(
    (0, "SAPRIV-MIB", "saSysModGroupID"),
    (0, "SAPRIV-MIB", "saSysModID"),
)
if mibBuilder.loadTexts:
    saSysModuleEntry.setStatus("mandatory")


class _SaSysModGroupID_Type(Integer32):
    """Custom type saSysModGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SaSysModGroupID_Type.__name__ = "Integer32"
_SaSysModGroupID_Object = MibTableColumn
saSysModGroupID = _SaSysModGroupID_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 10, 1, 1),
    _SaSysModGroupID_Type()
)
saSysModGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saSysModGroupID.setStatus("mandatory")


class _SaSysModID_Type(Integer32):
    """Custom type saSysModID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SaSysModID_Type.__name__ = "Integer32"
_SaSysModID_Object = MibTableColumn
saSysModID = _SaSysModID_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 10, 1, 2),
    _SaSysModID_Type()
)
saSysModID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saSysModID.setStatus("mandatory")


class _SaSysModType_Type(Integer32):
    """Custom type saSysModType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              100,
              101,
              102,
              103,
              104,
              200,
              201,
              300,
              1000,
              1001,
              1100,
              1101,
              1200)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("m-fast-8tp-rj", 100),
          ("m-fast-8mm-mt", 101),
          ("m-fast-2mm-sc", 102),
          ("m-fast-2sm-sc", 103),
          ("m-eth-4mm-st", 104),
          ("m-giga-2sx-sc", 200),
          ("m-giga-1lx-sc", 201),
          ("m-router", 300),
          ("icc-fast-4tp-rj", 1000),
          ("icc-eth-2mm-st", 1001),
          ("icc-fast-4mm-mt", 1100),
          ("icc-fast-2mm-sc", 1101),
          ("icc-fast-2mm-mt-fast-2tp-rj", 1200))
    )


_SaSysModType_Type.__name__ = "Integer32"
_SaSysModType_Object = MibTableColumn
saSysModType = _SaSysModType_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 10, 1, 3),
    _SaSysModType_Type()
)
saSysModType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saSysModType.setStatus("mandatory")
_SaSysModDescription_Type = DisplayString
_SaSysModDescription_Object = MibTableColumn
saSysModDescription = _SaSysModDescription_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 10, 1, 4),
    _SaSysModDescription_Type()
)
saSysModDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saSysModDescription.setStatus("mandatory")
_SaSysModVersion_Type = DisplayString
_SaSysModVersion_Object = MibTableColumn
saSysModVersion = _SaSysModVersion_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 10, 1, 5),
    _SaSysModVersion_Type()
)
saSysModVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saSysModVersion.setStatus("mandatory")
_SaSysModNumOfPorts_Type = Integer32
_SaSysModNumOfPorts_Object = MibTableColumn
saSysModNumOfPorts = _SaSysModNumOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 10, 1, 6),
    _SaSysModNumOfPorts_Type()
)
saSysModNumOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saSysModNumOfPorts.setStatus("mandatory")
_SaSysModFirstMauIndex_Type = Integer32
_SaSysModFirstMauIndex_Object = MibTableColumn
saSysModFirstMauIndex = _SaSysModFirstMauIndex_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 10, 1, 7),
    _SaSysModFirstMauIndex_Type()
)
saSysModFirstMauIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saSysModFirstMauIndex.setStatus("mandatory")
_SaInterfaceTable_Object = MibTable
saInterfaceTable = _SaInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 11)
)
if mibBuilder.loadTexts:
    saInterfaceTable.setStatus("mandatory")
_SaIfEntry_Object = MibTableRow
saIfEntry = _SaIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 11, 1)
)
saIfEntry.setIndexNames(
    (0, "SAPRIV-MIB", "saIfaceGroupID"),
    (0, "SAPRIV-MIB", "saIfaceID"),
)
if mibBuilder.loadTexts:
    saIfEntry.setStatus("mandatory")


class _SaIfaceGroupID_Type(Integer32):
    """Custom type saIfaceGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SaIfaceGroupID_Type.__name__ = "Integer32"
_SaIfaceGroupID_Object = MibTableColumn
saIfaceGroupID = _SaIfaceGroupID_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 11, 1, 1),
    _SaIfaceGroupID_Type()
)
saIfaceGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saIfaceGroupID.setStatus("mandatory")


class _SaIfaceID_Type(Integer32):
    """Custom type saIfaceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SaIfaceID_Type.__name__ = "Integer32"
_SaIfaceID_Object = MibTableColumn
saIfaceID = _SaIfaceID_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 11, 1, 2),
    _SaIfaceID_Type()
)
saIfaceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saIfaceID.setStatus("mandatory")


class _SaIfaceStpEnable_Type(Integer32):
    """Custom type saIfaceStpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SaIfaceStpEnable_Type.__name__ = "Integer32"
_SaIfaceStpEnable_Object = MibTableColumn
saIfaceStpEnable = _SaIfaceStpEnable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 11, 1, 3),
    _SaIfaceStpEnable_Type()
)
saIfaceStpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saIfaceStpEnable.setStatus("mandatory")


class _SaIfaceLinkType_Type(Integer32):
    """Custom type saIfaceLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("user", 1),
          ("uplink", 2))
    )


_SaIfaceLinkType_Type.__name__ = "Integer32"
_SaIfaceLinkType_Object = MibTableColumn
saIfaceLinkType = _SaIfaceLinkType_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 11, 1, 4),
    _SaIfaceLinkType_Type()
)
saIfaceLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saIfaceLinkType.setStatus("mandatory")


class _SaIfaceAction_Type(Integer32):
    """Custom type saIfaceAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("resetStats", 2))
    )


_SaIfaceAction_Type.__name__ = "Integer32"
_SaIfaceAction_Object = MibTableColumn
saIfaceAction = _SaIfaceAction_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 11, 1, 5),
    _SaIfaceAction_Type()
)
saIfaceAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saIfaceAction.setStatus("mandatory")
_SaIfaceNextHopMacAddress_Type = PhysAddress
_SaIfaceNextHopMacAddress_Object = MibTableColumn
saIfaceNextHopMacAddress = _SaIfaceNextHopMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 11, 1, 6),
    _SaIfaceNextHopMacAddress_Type()
)
saIfaceNextHopMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saIfaceNextHopMacAddress.setStatus("mandatory")


class _SaIfaceFlowControl_Type(Integer32):
    """Custom type saIfaceFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SaIfaceFlowControl_Type.__name__ = "Integer32"
_SaIfaceFlowControl_Object = MibTableColumn
saIfaceFlowControl = _SaIfaceFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 11, 1, 7),
    _SaIfaceFlowControl_Type()
)
saIfaceFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saIfaceFlowControl.setStatus("mandatory")
_SaIfacePriorityThreshold_Type = Integer32
_SaIfacePriorityThreshold_Object = MibTableColumn
saIfacePriorityThreshold = _SaIfacePriorityThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 11, 1, 8),
    _SaIfacePriorityThreshold_Type()
)
saIfacePriorityThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saIfacePriorityThreshold.setStatus("mandatory")


class _SaIfaceName_Type(DisplayString):
    """Custom type saIfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SaIfaceName_Type.__name__ = "DisplayString"
_SaIfaceName_Object = MibTableColumn
saIfaceName = _SaIfaceName_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 11, 1, 9),
    _SaIfaceName_Type()
)
saIfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saIfaceName.setStatus("mandatory")
_SaIfaceTrunkID_Type = Integer32
_SaIfaceTrunkID_Object = MibTableColumn
saIfaceTrunkID = _SaIfaceTrunkID_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 11, 1, 10),
    _SaIfaceTrunkID_Type()
)
saIfaceTrunkID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saIfaceTrunkID.setStatus("mandatory")


class _SaIfacePrioTOSEnable_Type(Integer32):
    """Custom type saIfacePrioTOSEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SaIfacePrioTOSEnable_Type.__name__ = "Integer32"
_SaIfacePrioTOSEnable_Object = MibTableColumn
saIfacePrioTOSEnable = _SaIfacePrioTOSEnable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 11, 1, 11),
    _SaIfacePrioTOSEnable_Type()
)
saIfacePrioTOSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saIfacePrioTOSEnable.setStatus("mandatory")


class _SaIfaceBcastLimit_Type(Integer32):
    """Custom type saIfaceBcastLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_SaIfaceBcastLimit_Type.__name__ = "Integer32"
_SaIfaceBcastLimit_Object = MibTableColumn
saIfaceBcastLimit = _SaIfaceBcastLimit_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 11, 1, 12),
    _SaIfaceBcastLimit_Type()
)
saIfaceBcastLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saIfaceBcastLimit.setStatus("mandatory")


class _SaIfaceUtilization_Type(Integer32):
    """Custom type saIfaceUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_SaIfaceUtilization_Type.__name__ = "Integer32"
_SaIfaceUtilization_Object = MibTableColumn
saIfaceUtilization = _SaIfaceUtilization_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 11, 1, 13),
    _SaIfaceUtilization_Type()
)
saIfaceUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saIfaceUtilization.setStatus("mandatory")


class _SaIfaceUtilizationControlInterval_Type(Integer32):
    """Custom type saIfaceUtilizationControlInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_SaIfaceUtilizationControlInterval_Type.__name__ = "Integer32"
_SaIfaceUtilizationControlInterval_Object = MibTableColumn
saIfaceUtilizationControlInterval = _SaIfaceUtilizationControlInterval_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 11, 1, 14),
    _SaIfaceUtilizationControlInterval_Type()
)
saIfaceUtilizationControlInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saIfaceUtilizationControlInterval.setStatus("mandatory")
_SaSysChassisName_Type = DisplayString
_SaSysChassisName_Object = MibScalar
saSysChassisName = _SaSysChassisName_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 20),
    _SaSysChassisName_Type()
)
saSysChassisName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saSysChassisName.setStatus("mandatory")


class _SaSysStpEnable_Type(Integer32):
    """Custom type saSysStpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SaSysStpEnable_Type.__name__ = "Integer32"
_SaSysStpEnable_Object = MibScalar
saSysStpEnable = _SaSysStpEnable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 21),
    _SaSysStpEnable_Type()
)
saSysStpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saSysStpEnable.setStatus("mandatory")


class _SaSysFlowControl_Type(Integer32):
    """Custom type saSysFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SaSysFlowControl_Type.__name__ = "Integer32"
_SaSysFlowControl_Object = MibScalar
saSysFlowControl = _SaSysFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 22),
    _SaSysFlowControl_Type()
)
saSysFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saSysFlowControl.setStatus("mandatory")


class _SaSysBOOTPEnable_Type(Integer32):
    """Custom type saSysBOOTPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SaSysBOOTPEnable_Type.__name__ = "Integer32"
_SaSysBOOTPEnable_Object = MibScalar
saSysBOOTPEnable = _SaSysBOOTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 23),
    _SaSysBOOTPEnable_Type()
)
saSysBOOTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saSysBOOTPEnable.setStatus("mandatory")


class _SaSysDHCPEnable_Type(Integer32):
    """Custom type saSysDHCPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SaSysDHCPEnable_Type.__name__ = "Integer32"
_SaSysDHCPEnable_Object = MibScalar
saSysDHCPEnable = _SaSysDHCPEnable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 24),
    _SaSysDHCPEnable_Type()
)
saSysDHCPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saSysDHCPEnable.setStatus("mandatory")


class _SaSysTelnetEnable_Type(Integer32):
    """Custom type saSysTelnetEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SaSysTelnetEnable_Type.__name__ = "Integer32"
_SaSysTelnetEnable_Object = MibScalar
saSysTelnetEnable = _SaSysTelnetEnable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 25),
    _SaSysTelnetEnable_Type()
)
saSysTelnetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saSysTelnetEnable.setStatus("mandatory")


class _SaSysHTTPEnable_Type(Integer32):
    """Custom type saSysHTTPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SaSysHTTPEnable_Type.__name__ = "Integer32"
_SaSysHTTPEnable_Object = MibScalar
saSysHTTPEnable = _SaSysHTTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 1, 26),
    _SaSysHTTPEnable_Type()
)
saSysHTTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saSysHTTPEnable.setStatus("mandatory")
_SaPSTable_Object = MibTable
saPSTable = _SaPSTable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 2)
)
if mibBuilder.loadTexts:
    saPSTable.setStatus("mandatory")
_SaPSEntry_Object = MibTableRow
saPSEntry = _SaPSEntry_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 2, 1)
)
saPSEntry.setIndexNames(
    (0, "SAPRIV-MIB", "saPSSysID"),
    (0, "SAPRIV-MIB", "saPSID"),
)
if mibBuilder.loadTexts:
    saPSEntry.setStatus("mandatory")
_SaPSSysID_Type = Integer32
_SaPSSysID_Object = MibTableColumn
saPSSysID = _SaPSSysID_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 2, 1, 1),
    _SaPSSysID_Type()
)
saPSSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saPSSysID.setStatus("mandatory")
_SaPSID_Type = Integer32
_SaPSID_Object = MibTableColumn
saPSID = _SaPSID_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 2, 1, 2),
    _SaPSID_Type()
)
saPSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saPSID.setStatus("mandatory")


class _SaPSState_Type(Integer32):
    """Custom type saPSState based on Integer32"""
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
        *(("ok", 1),
          ("failed", 2),
          ("notInstalled", 3),
          ("unknown", 4))
    )


_SaPSState_Type.__name__ = "Integer32"
_SaPSState_Object = MibTableColumn
saPSState = _SaPSState_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 2, 1, 3),
    _SaPSState_Type()
)
saPSState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saPSState.setStatus("mandatory")
_SaCurrentAddressTable_Object = MibTable
saCurrentAddressTable = _SaCurrentAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 5)
)
if mibBuilder.loadTexts:
    saCurrentAddressTable.setStatus("mandatory")
_SaCurrentAddressEntry_Object = MibTableRow
saCurrentAddressEntry = _SaCurrentAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 5, 1)
)
saCurrentAddressEntry.setIndexNames(
    (0, "SAPRIV-MIB", "saCurrentAddress"),
    (0, "SAPRIV-MIB", "saCurrentAddressReceivePort"),
)
if mibBuilder.loadTexts:
    saCurrentAddressEntry.setStatus("mandatory")
_SaCurrentAddress_Type = PhysAddress
_SaCurrentAddress_Object = MibTableColumn
saCurrentAddress = _SaCurrentAddress_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 5, 1, 1),
    _SaCurrentAddress_Type()
)
saCurrentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saCurrentAddress.setStatus("mandatory")
_SaCurrentAddressReceivePort_Type = Integer32
_SaCurrentAddressReceivePort_Object = MibTableColumn
saCurrentAddressReceivePort = _SaCurrentAddressReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 5, 1, 2),
    _SaCurrentAddressReceivePort_Type()
)
saCurrentAddressReceivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saCurrentAddressReceivePort.setStatus("mandatory")
_SaCurrentAddressStaticEgressPorts_Type = OctetString
_SaCurrentAddressStaticEgressPorts_Object = MibTableColumn
saCurrentAddressStaticEgressPorts = _SaCurrentAddressStaticEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 5, 1, 3),
    _SaCurrentAddressStaticEgressPorts_Type()
)
saCurrentAddressStaticEgressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saCurrentAddressStaticEgressPorts.setStatus("mandatory")
_SaCurrentAddressEgressPorts_Type = OctetString
_SaCurrentAddressEgressPorts_Object = MibTableColumn
saCurrentAddressEgressPorts = _SaCurrentAddressEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 5, 1, 4),
    _SaCurrentAddressEgressPorts_Type()
)
saCurrentAddressEgressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saCurrentAddressEgressPorts.setStatus("mandatory")


class _SaCurrentAddressStatus_Type(Integer32):
    """Custom type saCurrentAddressStatus based on Integer32"""
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
        *(("other", 1),
          ("invalid", 2),
          ("permanent", 3),
          ("deleteOnReset", 4),
          ("deleteOnTimeout", 5))
    )


_SaCurrentAddressStatus_Type.__name__ = "Integer32"
_SaCurrentAddressStatus_Object = MibTableColumn
saCurrentAddressStatus = _SaCurrentAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 5, 1, 5),
    _SaCurrentAddressStatus_Type()
)
saCurrentAddressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saCurrentAddressStatus.setStatus("mandatory")
_SaNXSext_ObjectIdentity = ObjectIdentity
saNXSext = _SaNXSext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 10)
)


class _SaNXSOperMode_Type(Integer32):
    """Custom type saNXSOperMode based on Integer32"""
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
        *(("normal", 1),
          ("standby-active", 2),
          ("standby-inactive", 3),
          ("redundancy-manager-active", 4),
          ("redundancy-manager-inactive", 5))
    )


_SaNXSOperMode_Type.__name__ = "Integer32"
_SaNXSOperMode_Object = MibScalar
saNXSOperMode = _SaNXSOperMode_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 10, 1),
    _SaNXSOperMode_Type()
)
saNXSOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saNXSOperMode.setStatus("mandatory")


class _SaNXSConfigError_Type(Integer32):
    """Custom type saNXSConfigError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-error", 1),
          ("error", 2))
    )


_SaNXSConfigError_Type.__name__ = "Integer32"
_SaNXSConfigError_Object = MibScalar
saNXSConfigError = _SaNXSConfigError_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 10, 2),
    _SaNXSConfigError_Type()
)
saNXSConfigError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saNXSConfigError.setStatus("mandatory")


class _SaNXSSigRelayState_Type(Integer32):
    """Custom type saNXSSigRelayState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_SaNXSSigRelayState_Type.__name__ = "Integer32"
_SaNXSSigRelayState_Object = MibScalar
saNXSSigRelayState = _SaNXSSigRelayState_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 10, 3),
    _SaNXSSigRelayState_Type()
)
saNXSSigRelayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saNXSSigRelayState.setStatus("mandatory")
_SaSigLinkTable_Object = MibTable
saSigLinkTable = _SaSigLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 10, 4)
)
if mibBuilder.loadTexts:
    saSigLinkTable.setStatus("mandatory")
_SaSigLinkEntry_Object = MibTableRow
saSigLinkEntry = _SaSigLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 10, 4, 1)
)
saSigLinkEntry.setIndexNames(
    (0, "SAPRIV-MIB", "saSigLinkID"),
)
if mibBuilder.loadTexts:
    saSigLinkEntry.setStatus("mandatory")


class _SaSigLinkID_Type(Integer32):
    """Custom type saSigLinkID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_SaSigLinkID_Type.__name__ = "Integer32"
_SaSigLinkID_Object = MibTableColumn
saSigLinkID = _SaSigLinkID_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 10, 4, 1, 1),
    _SaSigLinkID_Type()
)
saSigLinkID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saSigLinkID.setStatus("mandatory")


class _SaSigLinkAlarm_Type(Integer32):
    """Custom type saSigLinkAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_SaSigLinkAlarm_Type.__name__ = "Integer32"
_SaSigLinkAlarm_Object = MibTableColumn
saSigLinkAlarm = _SaSigLinkAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 10, 4, 1, 2),
    _SaSigLinkAlarm_Type()
)
saSigLinkAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saSigLinkAlarm.setStatus("mandatory")
_SaSigTrapReason_Type = ObjectIdentifier
_SaSigTrapReason_Object = MibScalar
saSigTrapReason = _SaSigTrapReason_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 10, 5),
    _SaSigTrapReason_Type()
)
saSigTrapReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saSigTrapReason.setStatus("mandatory")
_SaSigReasonIndex_Type = Integer32
_SaSigReasonIndex_Object = MibScalar
saSigReasonIndex = _SaSigReasonIndex_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 10, 6),
    _SaSigReasonIndex_Type()
)
saSigReasonIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saSigReasonIndex.setStatus("mandatory")
_SaNXSTopologyGroup_ObjectIdentity = ObjectIdentity
saNXSTopologyGroup = _SaNXSTopologyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 10, 7)
)
_SaNXSPartnerIpAddress_Type = IpAddress
_SaNXSPartnerIpAddress_Object = MibScalar
saNXSPartnerIpAddress = _SaNXSPartnerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 10, 7, 1),
    _SaNXSPartnerIpAddress_Type()
)
saNXSPartnerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saNXSPartnerIpAddress.setStatus("mandatory")
_SaNXSTopologyTable_Object = MibTable
saNXSTopologyTable = _SaNXSTopologyTable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 10, 7, 2)
)
if mibBuilder.loadTexts:
    saNXSTopologyTable.setStatus("mandatory")
_SaNXSTopologyEntry_Object = MibTableRow
saNXSTopologyEntry = _SaNXSTopologyEntry_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 10, 7, 2, 1)
)
saNXSTopologyEntry.setIndexNames(
    (0, "SAPRIV-MIB", "saNXSTopologyLinkID"),
)
if mibBuilder.loadTexts:
    saNXSTopologyEntry.setStatus("mandatory")


class _SaNXSTopologyLinkID_Type(Integer32):
    """Custom type saNXSTopologyLinkID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_SaNXSTopologyLinkID_Type.__name__ = "Integer32"
_SaNXSTopologyLinkID_Object = MibTableColumn
saNXSTopologyLinkID = _SaNXSTopologyLinkID_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 10, 7, 2, 1, 1),
    _SaNXSTopologyLinkID_Type()
)
saNXSTopologyLinkID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saNXSTopologyLinkID.setStatus("mandatory")
_SaNXSTopologyIpAddress_Type = IpAddress
_SaNXSTopologyIpAddress_Object = MibTableColumn
saNXSTopologyIpAddress = _SaNXSTopologyIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 10, 7, 2, 1, 2),
    _SaNXSTopologyIpAddress_Type()
)
saNXSTopologyIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saNXSTopologyIpAddress.setStatus("mandatory")
_SaNXSConnectionMirroringGroup_ObjectIdentity = ObjectIdentity
saNXSConnectionMirroringGroup = _SaNXSConnectionMirroringGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 10, 8)
)


class _SaNXSConnectionMirroringStatus_Type(Integer32):
    """Custom type saNXSConnectionMirroringStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_SaNXSConnectionMirroringStatus_Type.__name__ = "Integer32"
_SaNXSConnectionMirroringStatus_Object = MibScalar
saNXSConnectionMirroringStatus = _SaNXSConnectionMirroringStatus_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 10, 8, 1),
    _SaNXSConnectionMirroringStatus_Type()
)
saNXSConnectionMirroringStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saNXSConnectionMirroringStatus.setStatus("mandatory")
_SaNXSConnectionMirroringPortOne_Type = Integer32
_SaNXSConnectionMirroringPortOne_Object = MibScalar
saNXSConnectionMirroringPortOne = _SaNXSConnectionMirroringPortOne_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 10, 8, 2),
    _SaNXSConnectionMirroringPortOne_Type()
)
saNXSConnectionMirroringPortOne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saNXSConnectionMirroringPortOne.setStatus("mandatory")
_SaNXSConnectionMirroringPortTwo_Type = Integer32
_SaNXSConnectionMirroringPortTwo_Object = MibScalar
saNXSConnectionMirroringPortTwo = _SaNXSConnectionMirroringPortTwo_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 10, 8, 3),
    _SaNXSConnectionMirroringPortTwo_Type()
)
saNXSConnectionMirroringPortTwo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saNXSConnectionMirroringPortTwo.setStatus("mandatory")
_SaNXSDisableLearningGroup_ObjectIdentity = ObjectIdentity
saNXSDisableLearningGroup = _SaNXSDisableLearningGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 10, 9)
)


class _SaNXSDisableLearningStatus_Type(Integer32):
    """Custom type saNXSDisableLearningStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_SaNXSDisableLearningStatus_Type.__name__ = "Integer32"
_SaNXSDisableLearningStatus_Object = MibScalar
saNXSDisableLearningStatus = _SaNXSDisableLearningStatus_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 10, 9, 1),
    _SaNXSDisableLearningStatus_Type()
)
saNXSDisableLearningStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saNXSDisableLearningStatus.setStatus("mandatory")
_SaAgent_ObjectIdentity = ObjectIdentity
saAgent = _SaAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2)
)


class _SaAction_Type(Integer32):
    """Custom type saAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2),
          ("resetFDB", 4))
    )


_SaAction_Type.__name__ = "Integer32"
_SaAction_Object = MibScalar
saAction = _SaAction_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 1),
    _SaAction_Type()
)
saAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saAction.setStatus("mandatory")
_SaActionResult_Type = Integer32
_SaActionResult_Object = MibScalar
saActionResult = _SaActionResult_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 2),
    _SaActionResult_Type()
)
saActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saActionResult.setStatus("mandatory")
_SaNetwork_ObjectIdentity = ObjectIdentity
saNetwork = _SaNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 3)
)
_SaNetLocalIPAddr_Type = IpAddress
_SaNetLocalIPAddr_Object = MibScalar
saNetLocalIPAddr = _SaNetLocalIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 3, 1),
    _SaNetLocalIPAddr_Type()
)
saNetLocalIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saNetLocalIPAddr.setStatus("mandatory")
_SaNetLocalPhysAddr_Type = PhysAddress
_SaNetLocalPhysAddr_Object = MibScalar
saNetLocalPhysAddr = _SaNetLocalPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 3, 2),
    _SaNetLocalPhysAddr_Type()
)
saNetLocalPhysAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saNetLocalPhysAddr.setStatus("mandatory")
_SaNetGatewayIPAddr_Type = IpAddress
_SaNetGatewayIPAddr_Object = MibScalar
saNetGatewayIPAddr = _SaNetGatewayIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 3, 3),
    _SaNetGatewayIPAddr_Type()
)
saNetGatewayIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saNetGatewayIPAddr.setStatus("mandatory")
_SaNetMask_Type = IpAddress
_SaNetMask_Object = MibScalar
saNetMask = _SaNetMask_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 3, 4),
    _SaNetMask_Type()
)
saNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saNetMask.setStatus("mandatory")


class _SaNetAction_Type(Integer32):
    """Custom type saNetAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("activate", 2))
    )


_SaNetAction_Type.__name__ = "Integer32"
_SaNetAction_Object = MibScalar
saNetAction = _SaNetAction_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 3, 7),
    _SaNetAction_Type()
)
saNetAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saNetAction.setStatus("mandatory")
_SaFSTable_ObjectIdentity = ObjectIdentity
saFSTable = _SaFSTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 4)
)


class _SaFSUpdFileName_Type(DisplayString):
    """Custom type saFSUpdFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_SaFSUpdFileName_Type.__name__ = "DisplayString"
_SaFSUpdFileName_Object = MibScalar
saFSUpdFileName = _SaFSUpdFileName_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 4, 1),
    _SaFSUpdFileName_Type()
)
saFSUpdFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saFSUpdFileName.setStatus("mandatory")


class _SaFSConfFileName_Type(DisplayString):
    """Custom type saFSConfFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_SaFSConfFileName_Type.__name__ = "DisplayString"
_SaFSConfFileName_Object = MibScalar
saFSConfFileName = _SaFSConfFileName_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 4, 2),
    _SaFSConfFileName_Type()
)
saFSConfFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saFSConfFileName.setStatus("mandatory")


class _SaFSLogFileName_Type(DisplayString):
    """Custom type saFSLogFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_SaFSLogFileName_Type.__name__ = "DisplayString"
_SaFSLogFileName_Object = MibScalar
saFSLogFileName = _SaFSLogFileName_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 4, 3),
    _SaFSLogFileName_Type()
)
saFSLogFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saFSLogFileName.setStatus("mandatory")


class _SaFSUserName_Type(OctetString):
    """Custom type saFSUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SaFSUserName_Type.__name__ = "OctetString"
_SaFSUserName_Object = MibScalar
saFSUserName = _SaFSUserName_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 4, 4),
    _SaFSUserName_Type()
)
saFSUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saFSUserName.setStatus("mandatory")


class _SaFSTPPassword_Type(OctetString):
    """Custom type saFSTPPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SaFSTPPassword_Type.__name__ = "OctetString"
_SaFSTPPassword_Object = MibScalar
saFSTPPassword = _SaFSTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 4, 5),
    _SaFSTPPassword_Type()
)
saFSTPPassword.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    saFSTPPassword.setStatus("mandatory")


class _SaFSAction_Type(Integer32):
    """Custom type saFSAction based on Integer32"""
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
        *(("other", 1),
          ("update", 2),
          ("config-load", 3),
          ("config-save", 4),
          ("config-load-remote", 5),
          ("config-save-remote", 6))
    )


_SaFSAction_Type.__name__ = "Integer32"
_SaFSAction_Object = MibScalar
saFSAction = _SaFSAction_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 4, 6),
    _SaFSAction_Type()
)
saFSAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saFSAction.setStatus("mandatory")


class _SaFSActionResult_Type(Integer32):
    """Custom type saFSActionResult based on Integer32"""
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
        *(("other", 1),
          ("pending", 2),
          ("ok", 3),
          ("failed", 4))
    )


_SaFSActionResult_Type.__name__ = "Integer32"
_SaFSActionResult_Object = MibScalar
saFSActionResult = _SaFSActionResult_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 4, 8),
    _SaFSActionResult_Type()
)
saFSActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saFSActionResult.setStatus("mandatory")


class _SaFSBootConfiguration_Type(Integer32):
    """Custom type saFSBootConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("local", 2))
    )


_SaFSBootConfiguration_Type.__name__ = "Integer32"
_SaFSBootConfiguration_Object = MibScalar
saFSBootConfiguration = _SaFSBootConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 4, 9),
    _SaFSBootConfiguration_Type()
)
saFSBootConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saFSBootConfiguration.setStatus("mandatory")


class _SaFSRunningConfiguration_Type(Integer32):
    """Custom type saFSRunningConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("boot", 1),
          ("remote", 3))
    )


_SaFSRunningConfiguration_Type.__name__ = "Integer32"
_SaFSRunningConfiguration_Object = MibScalar
saFSRunningConfiguration = _SaFSRunningConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 4, 10),
    _SaFSRunningConfiguration_Type()
)
saFSRunningConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saFSRunningConfiguration.setStatus("mandatory")
_SaAutoconfigGroup_ObjectIdentity = ObjectIdentity
saAutoconfigGroup = _SaAutoconfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 4, 200)
)


class _SaAutoconfigAdapterStatus_Type(Integer32):
    """Custom type saAutoconfigAdapterStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 1),
          ("removed", 2),
          ("ok", 3),
          ("notInSync", 4),
          ("outOfMemory", 5),
          ("wrongMachine", 6),
          ("checksumErr", 7),
          ("genericErr", 8))
    )


_SaAutoconfigAdapterStatus_Type.__name__ = "Integer32"
_SaAutoconfigAdapterStatus_Object = MibScalar
saAutoconfigAdapterStatus = _SaAutoconfigAdapterStatus_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 4, 200, 1),
    _SaAutoconfigAdapterStatus_Type()
)
saAutoconfigAdapterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saAutoconfigAdapterStatus.setStatus("mandatory")
_SaAuthGroup_ObjectIdentity = ObjectIdentity
saAuthGroup = _SaAuthGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 7)
)


class _SaAuthHostTableEntriesMax_Type(Integer32):
    """Custom type saAuthHostTableEntriesMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SaAuthHostTableEntriesMax_Type.__name__ = "Integer32"
_SaAuthHostTableEntriesMax_Object = MibScalar
saAuthHostTableEntriesMax = _SaAuthHostTableEntriesMax_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 7, 1),
    _SaAuthHostTableEntriesMax_Type()
)
saAuthHostTableEntriesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saAuthHostTableEntriesMax.setStatus("mandatory")


class _SaAuthCommTableEntriesMax_Type(Integer32):
    """Custom type saAuthCommTableEntriesMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SaAuthCommTableEntriesMax_Type.__name__ = "Integer32"
_SaAuthCommTableEntriesMax_Object = MibScalar
saAuthCommTableEntriesMax = _SaAuthCommTableEntriesMax_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 7, 2),
    _SaAuthCommTableEntriesMax_Type()
)
saAuthCommTableEntriesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saAuthCommTableEntriesMax.setStatus("mandatory")
_SaAuthCommTable_Object = MibTable
saAuthCommTable = _SaAuthCommTable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 7, 3)
)
if mibBuilder.loadTexts:
    saAuthCommTable.setStatus("mandatory")
_SaAuthCommEntry_Object = MibTableRow
saAuthCommEntry = _SaAuthCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 7, 3, 1)
)
saAuthCommEntry.setIndexNames(
    (0, "SAPRIV-MIB", "saAuthCommIndex"),
)
if mibBuilder.loadTexts:
    saAuthCommEntry.setStatus("mandatory")


class _SaAuthCommIndex_Type(Integer32):
    """Custom type saAuthCommIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SaAuthCommIndex_Type.__name__ = "Integer32"
_SaAuthCommIndex_Object = MibTableColumn
saAuthCommIndex = _SaAuthCommIndex_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 7, 3, 1, 1),
    _SaAuthCommIndex_Type()
)
saAuthCommIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saAuthCommIndex.setStatus("mandatory")


class _SaAuthCommName_Type(DisplayString):
    """Custom type saAuthCommName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_SaAuthCommName_Type.__name__ = "DisplayString"
_SaAuthCommName_Object = MibTableColumn
saAuthCommName = _SaAuthCommName_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 7, 3, 1, 2),
    _SaAuthCommName_Type()
)
saAuthCommName.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    saAuthCommName.setStatus("mandatory")


class _SaAuthCommPerm_Type(Integer32):
    """Custom type saAuthCommPerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("perm-ro", 1),
          ("perm-rw", 2))
    )


_SaAuthCommPerm_Type.__name__ = "Integer32"
_SaAuthCommPerm_Object = MibTableColumn
saAuthCommPerm = _SaAuthCommPerm_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 7, 3, 1, 3),
    _SaAuthCommPerm_Type()
)
saAuthCommPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saAuthCommPerm.setStatus("mandatory")


class _SaAuthCommState_Type(Integer32):
    """Custom type saAuthCommState based on Integer32"""
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
        *(("enable", 1),
          ("disable", 2),
          ("delete", 3),
          ("invalid", 4))
    )


_SaAuthCommState_Type.__name__ = "Integer32"
_SaAuthCommState_Object = MibTableColumn
saAuthCommState = _SaAuthCommState_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 7, 3, 1, 4),
    _SaAuthCommState_Type()
)
saAuthCommState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saAuthCommState.setStatus("mandatory")
_SaAuthHostTable_Object = MibTable
saAuthHostTable = _SaAuthHostTable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 7, 4)
)
if mibBuilder.loadTexts:
    saAuthHostTable.setStatus("mandatory")
_SaAuthHostEntry_Object = MibTableRow
saAuthHostEntry = _SaAuthHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 7, 4, 1)
)
saAuthHostEntry.setIndexNames(
    (0, "SAPRIV-MIB", "saAuthHostIndex"),
)
if mibBuilder.loadTexts:
    saAuthHostEntry.setStatus("mandatory")


class _SaAuthHostIndex_Type(Integer32):
    """Custom type saAuthHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SaAuthHostIndex_Type.__name__ = "Integer32"
_SaAuthHostIndex_Object = MibTableColumn
saAuthHostIndex = _SaAuthHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 7, 4, 1, 1),
    _SaAuthHostIndex_Type()
)
saAuthHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saAuthHostIndex.setStatus("mandatory")


class _SaAuthHostName_Type(DisplayString):
    """Custom type saAuthHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_SaAuthHostName_Type.__name__ = "DisplayString"
_SaAuthHostName_Object = MibTableColumn
saAuthHostName = _SaAuthHostName_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 7, 4, 1, 2),
    _SaAuthHostName_Type()
)
saAuthHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saAuthHostName.setStatus("mandatory")
_SaAuthHostCommIndex_Type = Integer32
_SaAuthHostCommIndex_Object = MibTableColumn
saAuthHostCommIndex = _SaAuthHostCommIndex_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 7, 4, 1, 3),
    _SaAuthHostCommIndex_Type()
)
saAuthHostCommIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saAuthHostCommIndex.setStatus("mandatory")
_SaAuthHostIpAddress_Type = IpAddress
_SaAuthHostIpAddress_Object = MibTableColumn
saAuthHostIpAddress = _SaAuthHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 7, 4, 1, 4),
    _SaAuthHostIpAddress_Type()
)
saAuthHostIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saAuthHostIpAddress.setStatus("mandatory")
_SaAuthHostIpMask_Type = IpAddress
_SaAuthHostIpMask_Object = MibTableColumn
saAuthHostIpMask = _SaAuthHostIpMask_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 7, 4, 1, 5),
    _SaAuthHostIpMask_Type()
)
saAuthHostIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saAuthHostIpMask.setStatus("mandatory")


class _SaAuthHostState_Type(Integer32):
    """Custom type saAuthHostState based on Integer32"""
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
        *(("enable", 1),
          ("disable", 2),
          ("delete", 3),
          ("invalid", 4))
    )


_SaAuthHostState_Type.__name__ = "Integer32"
_SaAuthHostState_Object = MibTableColumn
saAuthHostState = _SaAuthHostState_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 7, 4, 1, 6),
    _SaAuthHostState_Type()
)
saAuthHostState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saAuthHostState.setStatus("mandatory")
_SaTrapGroup_ObjectIdentity = ObjectIdentity
saTrapGroup = _SaTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 8)
)


class _SaTrapCommTableEntriesMax_Type(Integer32):
    """Custom type saTrapCommTableEntriesMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SaTrapCommTableEntriesMax_Type.__name__ = "Integer32"
_SaTrapCommTableEntriesMax_Object = MibScalar
saTrapCommTableEntriesMax = _SaTrapCommTableEntriesMax_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 8, 1),
    _SaTrapCommTableEntriesMax_Type()
)
saTrapCommTableEntriesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saTrapCommTableEntriesMax.setStatus("mandatory")


class _SaTrapDestTableEntriesMax_Type(Integer32):
    """Custom type saTrapDestTableEntriesMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SaTrapDestTableEntriesMax_Type.__name__ = "Integer32"
_SaTrapDestTableEntriesMax_Object = MibScalar
saTrapDestTableEntriesMax = _SaTrapDestTableEntriesMax_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 8, 2),
    _SaTrapDestTableEntriesMax_Type()
)
saTrapDestTableEntriesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saTrapDestTableEntriesMax.setStatus("mandatory")
_SaTrapCommTable_Object = MibTable
saTrapCommTable = _SaTrapCommTable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 8, 3)
)
if mibBuilder.loadTexts:
    saTrapCommTable.setStatus("mandatory")
_SaTrapCommEntry_Object = MibTableRow
saTrapCommEntry = _SaTrapCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 8, 3, 1)
)
saTrapCommEntry.setIndexNames(
    (0, "SAPRIV-MIB", "saTrapCommIndex"),
)
if mibBuilder.loadTexts:
    saTrapCommEntry.setStatus("mandatory")


class _SaTrapCommIndex_Type(Integer32):
    """Custom type saTrapCommIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SaTrapCommIndex_Type.__name__ = "Integer32"
_SaTrapCommIndex_Object = MibTableColumn
saTrapCommIndex = _SaTrapCommIndex_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 8, 3, 1, 1),
    _SaTrapCommIndex_Type()
)
saTrapCommIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saTrapCommIndex.setStatus("mandatory")
_SaTrapCommCommIndex_Type = Integer32
_SaTrapCommCommIndex_Object = MibTableColumn
saTrapCommCommIndex = _SaTrapCommCommIndex_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 8, 3, 1, 2),
    _SaTrapCommCommIndex_Type()
)
saTrapCommCommIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saTrapCommCommIndex.setStatus("mandatory")


class _SaTrapCommColdStart_Type(Integer32):
    """Custom type saTrapCommColdStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SaTrapCommColdStart_Type.__name__ = "Integer32"
_SaTrapCommColdStart_Object = MibTableColumn
saTrapCommColdStart = _SaTrapCommColdStart_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 8, 3, 1, 3),
    _SaTrapCommColdStart_Type()
)
saTrapCommColdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saTrapCommColdStart.setStatus("mandatory")


class _SaTrapCommLinkDown_Type(Integer32):
    """Custom type saTrapCommLinkDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SaTrapCommLinkDown_Type.__name__ = "Integer32"
_SaTrapCommLinkDown_Object = MibTableColumn
saTrapCommLinkDown = _SaTrapCommLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 8, 3, 1, 4),
    _SaTrapCommLinkDown_Type()
)
saTrapCommLinkDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saTrapCommLinkDown.setStatus("mandatory")


class _SaTrapCommLinkUp_Type(Integer32):
    """Custom type saTrapCommLinkUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SaTrapCommLinkUp_Type.__name__ = "Integer32"
_SaTrapCommLinkUp_Object = MibTableColumn
saTrapCommLinkUp = _SaTrapCommLinkUp_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 8, 3, 1, 5),
    _SaTrapCommLinkUp_Type()
)
saTrapCommLinkUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saTrapCommLinkUp.setStatus("mandatory")


class _SaTrapCommAuthentication_Type(Integer32):
    """Custom type saTrapCommAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SaTrapCommAuthentication_Type.__name__ = "Integer32"
_SaTrapCommAuthentication_Object = MibTableColumn
saTrapCommAuthentication = _SaTrapCommAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 8, 3, 1, 6),
    _SaTrapCommAuthentication_Type()
)
saTrapCommAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saTrapCommAuthentication.setStatus("mandatory")


class _SaTrapCommBridge_Type(Integer32):
    """Custom type saTrapCommBridge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SaTrapCommBridge_Type.__name__ = "Integer32"
_SaTrapCommBridge_Object = MibTableColumn
saTrapCommBridge = _SaTrapCommBridge_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 8, 3, 1, 7),
    _SaTrapCommBridge_Type()
)
saTrapCommBridge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saTrapCommBridge.setStatus("mandatory")


class _SaTrapCommRMON_Type(Integer32):
    """Custom type saTrapCommRMON based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SaTrapCommRMON_Type.__name__ = "Integer32"
_SaTrapCommRMON_Object = MibTableColumn
saTrapCommRMON = _SaTrapCommRMON_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 8, 3, 1, 8),
    _SaTrapCommRMON_Type()
)
saTrapCommRMON.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saTrapCommRMON.setStatus("mandatory")


class _SaTrapCommUsergroup_Type(Integer32):
    """Custom type saTrapCommUsergroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SaTrapCommUsergroup_Type.__name__ = "Integer32"
_SaTrapCommUsergroup_Object = MibTableColumn
saTrapCommUsergroup = _SaTrapCommUsergroup_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 8, 3, 1, 9),
    _SaTrapCommUsergroup_Type()
)
saTrapCommUsergroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saTrapCommUsergroup.setStatus("mandatory")


class _SaTrapCommDualHoming_Type(Integer32):
    """Custom type saTrapCommDualHoming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SaTrapCommDualHoming_Type.__name__ = "Integer32"
_SaTrapCommDualHoming_Object = MibTableColumn
saTrapCommDualHoming = _SaTrapCommDualHoming_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 8, 3, 1, 10),
    _SaTrapCommDualHoming_Type()
)
saTrapCommDualHoming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saTrapCommDualHoming.setStatus("mandatory")


class _SaTrapCommChassis_Type(Integer32):
    """Custom type saTrapCommChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SaTrapCommChassis_Type.__name__ = "Integer32"
_SaTrapCommChassis_Object = MibTableColumn
saTrapCommChassis = _SaTrapCommChassis_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 8, 3, 1, 11),
    _SaTrapCommChassis_Type()
)
saTrapCommChassis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saTrapCommChassis.setStatus("mandatory")


class _SaTrapCommState_Type(Integer32):
    """Custom type saTrapCommState based on Integer32"""
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
        *(("enable", 1),
          ("disable", 2),
          ("delete", 3),
          ("invalid", 4))
    )


_SaTrapCommState_Type.__name__ = "Integer32"
_SaTrapCommState_Object = MibTableColumn
saTrapCommState = _SaTrapCommState_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 8, 3, 1, 12),
    _SaTrapCommState_Type()
)
saTrapCommState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saTrapCommState.setStatus("mandatory")
_SaTrapDestTable_Object = MibTable
saTrapDestTable = _SaTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 8, 4)
)
if mibBuilder.loadTexts:
    saTrapDestTable.setStatus("mandatory")
_SaTrapDestEntry_Object = MibTableRow
saTrapDestEntry = _SaTrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 8, 4, 1)
)
saTrapDestEntry.setIndexNames(
    (0, "SAPRIV-MIB", "saTrapDestIndex"),
)
if mibBuilder.loadTexts:
    saTrapDestEntry.setStatus("mandatory")


class _SaTrapDestIndex_Type(Integer32):
    """Custom type saTrapDestIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SaTrapDestIndex_Type.__name__ = "Integer32"
_SaTrapDestIndex_Object = MibTableColumn
saTrapDestIndex = _SaTrapDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 8, 4, 1, 1),
    _SaTrapDestIndex_Type()
)
saTrapDestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saTrapDestIndex.setStatus("mandatory")


class _SaTrapDestName_Type(DisplayString):
    """Custom type saTrapDestName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_SaTrapDestName_Type.__name__ = "DisplayString"
_SaTrapDestName_Object = MibTableColumn
saTrapDestName = _SaTrapDestName_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 8, 4, 1, 2),
    _SaTrapDestName_Type()
)
saTrapDestName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saTrapDestName.setStatus("mandatory")
_SaTrapDestCommIndex_Type = Integer32
_SaTrapDestCommIndex_Object = MibTableColumn
saTrapDestCommIndex = _SaTrapDestCommIndex_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 8, 4, 1, 3),
    _SaTrapDestCommIndex_Type()
)
saTrapDestCommIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saTrapDestCommIndex.setStatus("mandatory")
_SaTrapDestIpAddress_Type = IpAddress
_SaTrapDestIpAddress_Object = MibTableColumn
saTrapDestIpAddress = _SaTrapDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 8, 4, 1, 4),
    _SaTrapDestIpAddress_Type()
)
saTrapDestIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saTrapDestIpAddress.setStatus("mandatory")
_SaTrapDestIpMask_Type = IpAddress
_SaTrapDestIpMask_Object = MibTableColumn
saTrapDestIpMask = _SaTrapDestIpMask_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 8, 4, 1, 5),
    _SaTrapDestIpMask_Type()
)
saTrapDestIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saTrapDestIpMask.setStatus("obsolete")


class _SaTrapDestState_Type(Integer32):
    """Custom type saTrapDestState based on Integer32"""
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
        *(("enable", 1),
          ("disable", 2),
          ("delete", 3),
          ("invalid", 4))
    )


_SaTrapDestState_Type.__name__ = "Integer32"
_SaTrapDestState_Object = MibTableColumn
saTrapDestState = _SaTrapDestState_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 8, 4, 1, 6),
    _SaTrapDestState_Type()
)
saTrapDestState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saTrapDestState.setStatus("mandatory")
_SaLastAccessGroup_ObjectIdentity = ObjectIdentity
saLastAccessGroup = _SaLastAccessGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 9)
)
_SaLastIpAddr_Type = IpAddress
_SaLastIpAddr_Object = MibScalar
saLastIpAddr = _SaLastIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 9, 1),
    _SaLastIpAddr_Type()
)
saLastIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saLastIpAddr.setStatus("mandatory")
_SaLastPort_Type = Integer32
_SaLastPort_Object = MibScalar
saLastPort = _SaLastPort_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 9, 2),
    _SaLastPort_Type()
)
saLastPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saLastPort.setStatus("mandatory")
_SaLastCommunity_Type = DisplayString
_SaLastCommunity_Object = MibScalar
saLastCommunity = _SaLastCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 9, 3),
    _SaLastCommunity_Type()
)
saLastCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saLastCommunity.setStatus("mandatory")
_SaProducts_ObjectIdentity = ObjectIdentity
saProducts = _SaProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 10)
)
_Nxsx7100_ObjectIdentity = ObjectIdentity
nxsx7100 = _Nxsx7100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 10, 2)
)

# Managed Objects groups


# Notification objects

saPowerSupply = NotificationType(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 0, 2)
)
saPowerSupply.setObjects(
    ("SAPRIV-MIB", "saPSState")
)
if mibBuilder.loadTexts:
    saPowerSupply.setStatus(
        ""
    )

saSignallingRelay = NotificationType(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 0, 4)
)
saSignallingRelay.setObjects(
      *(("SAPRIV-MIB", "saNXSSigRelayState"),
        ("SAPRIV-MIB", "saSigTrapReason"),
        ("SAPRIV-MIB", "saSigReasonIndex"))
)
if mibBuilder.loadTexts:
    saSignallingRelay.setStatus(
        ""
    )

saStandby = NotificationType(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 1, 0, 5)
)
saStandby.setObjects(
    ("SAPRIV-MIB", "saNXSOperMode")
)
if mibBuilder.loadTexts:
    saStandby.setStatus(
        ""
    )

saAutoconfigAdapterTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 2, 0, 4)
)
saAutoconfigAdapterTrap.setObjects(
    ("SAPRIV-MIB", "saAutoconfigAdapterStatus")
)
if mibBuilder.loadTexts:
    saAutoconfigAdapterTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SAPRIV-MIB",
    **{"private": private,
       "enterprises": enterprises,
       "groupeschneider": groupeschneider,
       "transparentFactoryEthernet": transparentFactoryEthernet,
       "switch": switch,
       "saConfiguration": saConfiguration,
       "saChassis": saChassis,
       "saPowerSupply": saPowerSupply,
       "saSignallingRelay": saSignallingRelay,
       "saStandby": saStandby,
       "saSystemTable": saSystemTable,
       "saSysProduct": saSysProduct,
       "saSysVersion": saSysVersion,
       "saSysGroupCapacity": saSysGroupCapacity,
       "saSysGroupMap": saSysGroupMap,
       "saSysMaxPowerSupply": saSysMaxPowerSupply,
       "saSysMaxFan": saSysMaxFan,
       "saSysGroupModuleCapacity": saSysGroupModuleCapacity,
       "saSysModulePortCapacity": saSysModulePortCapacity,
       "saSysGroupTable": saSysGroupTable,
       "saSysGroupEntry": saSysGroupEntry,
       "saSysGroupID": saSysGroupID,
       "saSysGroupType": saSysGroupType,
       "saSysGroupDescription": saSysGroupDescription,
       "saSysGroupHwVersion": saSysGroupHwVersion,
       "saSysGroupSwVersion": saSysGroupSwVersion,
       "saSysGroupModuleMap": saSysGroupModuleMap,
       "saSysGroupAction": saSysGroupAction,
       "saSysGroupActionResult": saSysGroupActionResult,
       "saSysModuleTable": saSysModuleTable,
       "saSysModuleEntry": saSysModuleEntry,
       "saSysModGroupID": saSysModGroupID,
       "saSysModID": saSysModID,
       "saSysModType": saSysModType,
       "saSysModDescription": saSysModDescription,
       "saSysModVersion": saSysModVersion,
       "saSysModNumOfPorts": saSysModNumOfPorts,
       "saSysModFirstMauIndex": saSysModFirstMauIndex,
       "saInterfaceTable": saInterfaceTable,
       "saIfEntry": saIfEntry,
       "saIfaceGroupID": saIfaceGroupID,
       "saIfaceID": saIfaceID,
       "saIfaceStpEnable": saIfaceStpEnable,
       "saIfaceLinkType": saIfaceLinkType,
       "saIfaceAction": saIfaceAction,
       "saIfaceNextHopMacAddress": saIfaceNextHopMacAddress,
       "saIfaceFlowControl": saIfaceFlowControl,
       "saIfacePriorityThreshold": saIfacePriorityThreshold,
       "saIfaceName": saIfaceName,
       "saIfaceTrunkID": saIfaceTrunkID,
       "saIfacePrioTOSEnable": saIfacePrioTOSEnable,
       "saIfaceBcastLimit": saIfaceBcastLimit,
       "saIfaceUtilization": saIfaceUtilization,
       "saIfaceUtilizationControlInterval": saIfaceUtilizationControlInterval,
       "saSysChassisName": saSysChassisName,
       "saSysStpEnable": saSysStpEnable,
       "saSysFlowControl": saSysFlowControl,
       "saSysBOOTPEnable": saSysBOOTPEnable,
       "saSysDHCPEnable": saSysDHCPEnable,
       "saSysTelnetEnable": saSysTelnetEnable,
       "saSysHTTPEnable": saSysHTTPEnable,
       "saPSTable": saPSTable,
       "saPSEntry": saPSEntry,
       "saPSSysID": saPSSysID,
       "saPSID": saPSID,
       "saPSState": saPSState,
       "saCurrentAddressTable": saCurrentAddressTable,
       "saCurrentAddressEntry": saCurrentAddressEntry,
       "saCurrentAddress": saCurrentAddress,
       "saCurrentAddressReceivePort": saCurrentAddressReceivePort,
       "saCurrentAddressStaticEgressPorts": saCurrentAddressStaticEgressPorts,
       "saCurrentAddressEgressPorts": saCurrentAddressEgressPorts,
       "saCurrentAddressStatus": saCurrentAddressStatus,
       "saNXSext": saNXSext,
       "saNXSOperMode": saNXSOperMode,
       "saNXSConfigError": saNXSConfigError,
       "saNXSSigRelayState": saNXSSigRelayState,
       "saSigLinkTable": saSigLinkTable,
       "saSigLinkEntry": saSigLinkEntry,
       "saSigLinkID": saSigLinkID,
       "saSigLinkAlarm": saSigLinkAlarm,
       "saSigTrapReason": saSigTrapReason,
       "saSigReasonIndex": saSigReasonIndex,
       "saNXSTopologyGroup": saNXSTopologyGroup,
       "saNXSPartnerIpAddress": saNXSPartnerIpAddress,
       "saNXSTopologyTable": saNXSTopologyTable,
       "saNXSTopologyEntry": saNXSTopologyEntry,
       "saNXSTopologyLinkID": saNXSTopologyLinkID,
       "saNXSTopologyIpAddress": saNXSTopologyIpAddress,
       "saNXSConnectionMirroringGroup": saNXSConnectionMirroringGroup,
       "saNXSConnectionMirroringStatus": saNXSConnectionMirroringStatus,
       "saNXSConnectionMirroringPortOne": saNXSConnectionMirroringPortOne,
       "saNXSConnectionMirroringPortTwo": saNXSConnectionMirroringPortTwo,
       "saNXSDisableLearningGroup": saNXSDisableLearningGroup,
       "saNXSDisableLearningStatus": saNXSDisableLearningStatus,
       "saAgent": saAgent,
       "saAutoconfigAdapterTrap": saAutoconfigAdapterTrap,
       "saAction": saAction,
       "saActionResult": saActionResult,
       "saNetwork": saNetwork,
       "saNetLocalIPAddr": saNetLocalIPAddr,
       "saNetLocalPhysAddr": saNetLocalPhysAddr,
       "saNetGatewayIPAddr": saNetGatewayIPAddr,
       "saNetMask": saNetMask,
       "saNetAction": saNetAction,
       "saFSTable": saFSTable,
       "saFSUpdFileName": saFSUpdFileName,
       "saFSConfFileName": saFSConfFileName,
       "saFSLogFileName": saFSLogFileName,
       "saFSUserName": saFSUserName,
       "saFSTPPassword": saFSTPPassword,
       "saFSAction": saFSAction,
       "saFSActionResult": saFSActionResult,
       "saFSBootConfiguration": saFSBootConfiguration,
       "saFSRunningConfiguration": saFSRunningConfiguration,
       "saAutoconfigGroup": saAutoconfigGroup,
       "saAutoconfigAdapterStatus": saAutoconfigAdapterStatus,
       "saAuthGroup": saAuthGroup,
       "saAuthHostTableEntriesMax": saAuthHostTableEntriesMax,
       "saAuthCommTableEntriesMax": saAuthCommTableEntriesMax,
       "saAuthCommTable": saAuthCommTable,
       "saAuthCommEntry": saAuthCommEntry,
       "saAuthCommIndex": saAuthCommIndex,
       "saAuthCommName": saAuthCommName,
       "saAuthCommPerm": saAuthCommPerm,
       "saAuthCommState": saAuthCommState,
       "saAuthHostTable": saAuthHostTable,
       "saAuthHostEntry": saAuthHostEntry,
       "saAuthHostIndex": saAuthHostIndex,
       "saAuthHostName": saAuthHostName,
       "saAuthHostCommIndex": saAuthHostCommIndex,
       "saAuthHostIpAddress": saAuthHostIpAddress,
       "saAuthHostIpMask": saAuthHostIpMask,
       "saAuthHostState": saAuthHostState,
       "saTrapGroup": saTrapGroup,
       "saTrapCommTableEntriesMax": saTrapCommTableEntriesMax,
       "saTrapDestTableEntriesMax": saTrapDestTableEntriesMax,
       "saTrapCommTable": saTrapCommTable,
       "saTrapCommEntry": saTrapCommEntry,
       "saTrapCommIndex": saTrapCommIndex,
       "saTrapCommCommIndex": saTrapCommCommIndex,
       "saTrapCommColdStart": saTrapCommColdStart,
       "saTrapCommLinkDown": saTrapCommLinkDown,
       "saTrapCommLinkUp": saTrapCommLinkUp,
       "saTrapCommAuthentication": saTrapCommAuthentication,
       "saTrapCommBridge": saTrapCommBridge,
       "saTrapCommRMON": saTrapCommRMON,
       "saTrapCommUsergroup": saTrapCommUsergroup,
       "saTrapCommDualHoming": saTrapCommDualHoming,
       "saTrapCommChassis": saTrapCommChassis,
       "saTrapCommState": saTrapCommState,
       "saTrapDestTable": saTrapDestTable,
       "saTrapDestEntry": saTrapDestEntry,
       "saTrapDestIndex": saTrapDestIndex,
       "saTrapDestName": saTrapDestName,
       "saTrapDestCommIndex": saTrapDestCommIndex,
       "saTrapDestIpAddress": saTrapDestIpAddress,
       "saTrapDestIpMask": saTrapDestIpMask,
       "saTrapDestState": saTrapDestState,
       "saLastAccessGroup": saLastAccessGroup,
       "saLastIpAddr": saLastIpAddr,
       "saLastPort": saLastPort,
       "saLastCommunity": saLastCommunity,
       "saProducts": saProducts,
       "nxsx7100": nxsx7100}
)
