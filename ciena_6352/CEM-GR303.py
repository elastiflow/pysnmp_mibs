# SNMP MIB module (CEM-GR303) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_6352/CEM-GR303.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:49:21 2025
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

(Cn1000ConfigurationStatus,
 Cn1000ShelfRange) = mibBuilder.importSymbols(
    "CEM-CN1000",
    "Cn1000ConfigurationStatus",
    "Cn1000ShelfRange")

(CnIfGroupIndexRange,
 CnIfGroupLinkType,
 cnGR303) = mibBuilder.importSymbols(
    "CEM-INTERFACES",
    "CnIfGroupIndexRange",
    "CnIfGroupLinkType",
    "cnGR303")

(CnSlotGroupNameType,) = mibBuilder.importSymbols(
    "CEM-TEXTUAL-CONVENTIONS",
    "CnSlotGroupNameType")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Bits,
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
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
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
    "iso")

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

cnGR303Module = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CnGR303IDTType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cnGR303idt5ESS", 0),
          ("cnGR303idtDMSSuperNode", 1),
          ("cnGR303idtEWSD", 2),
          ("cnGR303idtGTD5", 3),
          ("cnGR303idtDMS10", 4))
    )



class CnGR303LinkSecondaryServiceStateType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("cnGR303secServStateTs", 0),
          ("cnGR303secServStateMt", 1),
          ("cnGR303secServStateMa", 2),
          ("cnGR303secServStateAnr", 3),
          ("cnGR303secServStateUeq", 4),
          ("cnGR303secServStateFef", 5),
          ("cnGR303secServStateBusy", 6),
          ("cnGR303secServStateLpbk", 7),
          ("cnGR303secServStateMea", 8),
          ("cnGR303secServStateMon", 9),
          ("cnGR303secServStatePwr", 10),
          ("cnGR303secServStateSea", 11),
          ("cnGR303secServStateAct", 12),
          ("cnGR303secServStateCcsf", 13),
          ("cnGR303secServStateComb", 14),
          ("cnGR303secServStateDgn", 15),
          ("cnGR303secServStateDsbld", 16),
          ("cnGR303secServStateErranal", 17),
          ("cnGR303secServStateEx", 18),
          ("cnGR303secServStateFaf", 19),
          ("cnGR303secServStateFepro", 20),
          ("cnGR303secServStateFlt", 21),
          ("cnGR303secServStateFrcd", 22),
          ("cnGR303secServStateHd", 23),
          ("cnGR303secServStateHw", 24),
          ("cnGR303secServStateInhip", 25),
          ("cnGR303secServStateLkdo", 26),
          ("cnGR303secServStateLock", 27),
          ("cnGR303secServStateMtce", 28),
          ("cnGR303secServStateMtcelim", 29),
          ("cnGR303secServStateNm", 30),
          ("cnGR303secServStatePctf", 31),
          ("cnGR303secServStatePri", 32),
          ("cnGR303secServStatePrtcl", 33),
          ("cnGR303secServStateSec", 34),
          ("cnGR303secServStateStby", 35),
          ("cnGR303secServStateTermf", 36),
          ("cnGR303secServStateTmt", 37),
          ("cnGR303secServStateTrd", 38),
          ("cnGR303secServStateTstf", 39),
          ("cnGR303secServStateSof", 40),
          ("cnGR303secServStateSwtch", 41))
    )


class CnGR303LinkStatusType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cnGR303LinkStatusDown", 0),
          ("cnGR303LinkStatusUp", 1))
    )



class CnGR303LinkStatusActivePath(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cnGR303LinkStatusActivePathNone", 0),
          ("cnGR303LinkStatusActivePathPrimary", 1),
          ("cnGR303LinkStatusActivePathSecondary", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CnGR303IfGroupConfigTable_Object = MibTable
cnGR303IfGroupConfigTable = _CnGR303IfGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cnGR303IfGroupConfigTable.setStatus("current")
_CnGR303IfGroupConfigEntry_Object = MibTableRow
cnGR303IfGroupConfigEntry = _CnGR303IfGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 1, 1)
)
cnGR303IfGroupConfigEntry.setIndexNames(
    (0, "CEM-GR303", "cnGR303IfGroupIndex"),
)
if mibBuilder.loadTexts:
    cnGR303IfGroupConfigEntry.setStatus("current")
_CnGR303IfGroupShelf_Type = Cn1000ShelfRange
_CnGR303IfGroupShelf_Object = MibTableColumn
cnGR303IfGroupShelf = _CnGR303IfGroupShelf_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 1, 1, 1),
    _CnGR303IfGroupShelf_Type()
)
cnGR303IfGroupShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnGR303IfGroupShelf.setStatus("current")
_CnGR303IfGroupSlotGroup_Type = CnSlotGroupNameType
_CnGR303IfGroupSlotGroup_Object = MibTableColumn
cnGR303IfGroupSlotGroup = _CnGR303IfGroupSlotGroup_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 1, 1, 2),
    _CnGR303IfGroupSlotGroup_Type()
)
cnGR303IfGroupSlotGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnGR303IfGroupSlotGroup.setStatus("current")


class _CnGR303IfGroupIndex_Type(Integer32):
    """Custom type cnGR303IfGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CnGR303IfGroupIndex_Type.__name__ = "Integer32"
_CnGR303IfGroupIndex_Object = MibTableColumn
cnGR303IfGroupIndex = _CnGR303IfGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 1, 1, 3),
    _CnGR303IfGroupIndex_Type()
)
cnGR303IfGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGR303IfGroupIndex.setStatus("current")


class _CnGR303IfGroupConnectionIndex_Type(Integer32):
    """Custom type cnGR303IfGroupConnectionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_CnGR303IfGroupConnectionIndex_Type.__name__ = "Integer32"
_CnGR303IfGroupConnectionIndex_Object = MibTableColumn
cnGR303IfGroupConnectionIndex = _CnGR303IfGroupConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 1, 1, 4),
    _CnGR303IfGroupConnectionIndex_Type()
)
cnGR303IfGroupConnectionIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnGR303IfGroupConnectionIndex.setStatus("current")


class _CnGR303IfGroupDescription_Type(OctetString):
    """Custom type cnGR303IfGroupDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CnGR303IfGroupDescription_Type.__name__ = "OctetString"
_CnGR303IfGroupDescription_Object = MibTableColumn
cnGR303IfGroupDescription = _CnGR303IfGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 1, 1, 5),
    _CnGR303IfGroupDescription_Type()
)
cnGR303IfGroupDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnGR303IfGroupDescription.setStatus("current")


class _CnGR303IfGroupAdminState_Type(Integer32):
    """Custom type cnGR303IfGroupAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undetermined", 0),
          ("up", 1),
          ("down", 2))
    )


_CnGR303IfGroupAdminState_Type.__name__ = "Integer32"
_CnGR303IfGroupAdminState_Object = MibTableColumn
cnGR303IfGroupAdminState = _CnGR303IfGroupAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 1, 1, 6),
    _CnGR303IfGroupAdminState_Type()
)
cnGR303IfGroupAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnGR303IfGroupAdminState.setStatus("current")
_CnGR303IfGroupConfigStatus_Type = Cn1000ConfigurationStatus
_CnGR303IfGroupConfigStatus_Object = MibTableColumn
cnGR303IfGroupConfigStatus = _CnGR303IfGroupConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 1, 1, 7),
    _CnGR303IfGroupConfigStatus_Type()
)
cnGR303IfGroupConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGR303IfGroupConfigStatus.setStatus("current")
_CnGR303IfGroupIdtType_Type = CnGR303IDTType
_CnGR303IfGroupIdtType_Object = MibTableColumn
cnGR303IfGroupIdtType = _CnGR303IfGroupIdtType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 1, 1, 8),
    _CnGR303IfGroupIdtType_Type()
)
cnGR303IfGroupIdtType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnGR303IfGroupIdtType.setStatus("current")


class _CnGR303IfGroupFlowThruProv_Type(Integer32):
    """Custom type cnGR303IfGroupFlowThruProv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_CnGR303IfGroupFlowThruProv_Type.__name__ = "Integer32"
_CnGR303IfGroupFlowThruProv_Object = MibTableColumn
cnGR303IfGroupFlowThruProv = _CnGR303IfGroupFlowThruProv_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 1, 1, 9),
    _CnGR303IfGroupFlowThruProv_Type()
)
cnGR303IfGroupFlowThruProv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnGR303IfGroupFlowThruProv.setStatus("current")


class _CnGR303IfGroupQ931t303_Type(Integer32):
    """Custom type cnGR303IfGroupQ931t303 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(700, 700),
        ValueRangeConstraint(1200, 1200),
        ValueRangeConstraint(1700, 1700),
        ValueRangeConstraint(2200, 2200),
        ValueRangeConstraint(2700, 2700),
        ValueRangeConstraint(3200, 3200),
        ValueRangeConstraint(3700, 3700),
        ValueRangeConstraint(4200, 4200),
        ValueRangeConstraint(4700, 4700),
    )


_CnGR303IfGroupQ931t303_Type.__name__ = "Integer32"
_CnGR303IfGroupQ931t303_Object = MibTableColumn
cnGR303IfGroupQ931t303 = _CnGR303IfGroupQ931t303_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 1, 1, 10),
    _CnGR303IfGroupQ931t303_Type()
)
cnGR303IfGroupQ931t303.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnGR303IfGroupQ931t303.setStatus("current")


class _CnGR303IfGroupQ931t308_Type(Integer32):
    """Custom type cnGR303IfGroupQ931t308 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 2000),
        ValueRangeConstraint(4000, 4000),
        ValueRangeConstraint(5000, 5000),
    )


_CnGR303IfGroupQ931t308_Type.__name__ = "Integer32"
_CnGR303IfGroupQ931t308_Object = MibTableColumn
cnGR303IfGroupQ931t308 = _CnGR303IfGroupQ931t308_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 1, 1, 11),
    _CnGR303IfGroupQ931t308_Type()
)
cnGR303IfGroupQ931t308.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnGR303IfGroupQ931t308.setStatus("current")


class _CnGR303IfGroupQ931t396_Type(Integer32):
    """Custom type cnGR303IfGroupQ931t396 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(700, 700),
        ValueRangeConstraint(1700, 1700),
        ValueRangeConstraint(2700, 2700),
        ValueRangeConstraint(3700, 3700),
        ValueRangeConstraint(4700, 4700),
        ValueRangeConstraint(5700, 5700),
        ValueRangeConstraint(6700, 6700),
        ValueRangeConstraint(7700, 7700),
        ValueRangeConstraint(8700, 8700),
        ValueRangeConstraint(9700, 9700),
        ValueRangeConstraint(10700, 10700),
        ValueRangeConstraint(11700, 11700),
        ValueRangeConstraint(12700, 12700),
        ValueRangeConstraint(13700, 13700),
        ValueRangeConstraint(14700, 14700),
    )


_CnGR303IfGroupQ931t396_Type.__name__ = "Integer32"
_CnGR303IfGroupQ931t396_Object = MibTableColumn
cnGR303IfGroupQ931t396 = _CnGR303IfGroupQ931t396_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 1, 1, 12),
    _CnGR303IfGroupQ931t396_Type()
)
cnGR303IfGroupQ931t396.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnGR303IfGroupQ931t396.setStatus("current")


class _CnGR303IfGroupQ931t397_Type(Integer32):
    """Custom type cnGR303IfGroupQ931t397 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(120, 120),
        ValueRangeConstraint(180, 180),
    )


_CnGR303IfGroupQ931t397_Type.__name__ = "Integer32"
_CnGR303IfGroupQ931t397_Object = MibTableColumn
cnGR303IfGroupQ931t397 = _CnGR303IfGroupQ931t397_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 1, 1, 13),
    _CnGR303IfGroupQ931t397_Type()
)
cnGR303IfGroupQ931t397.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnGR303IfGroupQ931t397.setStatus("current")
if mibBuilder.loadTexts:
    cnGR303IfGroupQ931t397.setUnits("sec")


class _CnGR303IfGroupLapdSapi0k_Type(Integer32):
    """Custom type cnGR303IfGroupLapdSapi0k based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_CnGR303IfGroupLapdSapi0k_Type.__name__ = "Integer32"
_CnGR303IfGroupLapdSapi0k_Object = MibTableColumn
cnGR303IfGroupLapdSapi0k = _CnGR303IfGroupLapdSapi0k_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 1, 1, 14),
    _CnGR303IfGroupLapdSapi0k_Type()
)
cnGR303IfGroupLapdSapi0k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnGR303IfGroupLapdSapi0k.setStatus("current")


class _CnGR303IfGroupLapdSapi0n200_Type(Integer32):
    """Custom type cnGR303IfGroupLapdSapi0n200 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CnGR303IfGroupLapdSapi0n200_Type.__name__ = "Integer32"
_CnGR303IfGroupLapdSapi0n200_Object = MibTableColumn
cnGR303IfGroupLapdSapi0n200 = _CnGR303IfGroupLapdSapi0n200_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 1, 1, 15),
    _CnGR303IfGroupLapdSapi0n200_Type()
)
cnGR303IfGroupLapdSapi0n200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnGR303IfGroupLapdSapi0n200.setStatus("current")


class _CnGR303IfGroupLapdSapi0t200_Type(Integer32):
    """Custom type cnGR303IfGroupLapdSapi0t200 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(150, 150),
        ValueRangeConstraint(200, 200),
        ValueRangeConstraint(250, 250),
        ValueRangeConstraint(300, 300),
        ValueRangeConstraint(350, 350),
    )


_CnGR303IfGroupLapdSapi0t200_Type.__name__ = "Integer32"
_CnGR303IfGroupLapdSapi0t200_Object = MibTableColumn
cnGR303IfGroupLapdSapi0t200 = _CnGR303IfGroupLapdSapi0t200_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 1, 1, 16),
    _CnGR303IfGroupLapdSapi0t200_Type()
)
cnGR303IfGroupLapdSapi0t200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnGR303IfGroupLapdSapi0t200.setStatus("current")


class _CnGR303IfGroupLapdSapi0t203_Type(Integer32):
    """Custom type cnGR303IfGroupLapdSapi0t203 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(70, 70),
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(90, 90),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(110, 110),
        ValueRangeConstraint(120, 120),
        ValueRangeConstraint(130, 130),
        ValueRangeConstraint(140, 140),
        ValueRangeConstraint(150, 150),
        ValueRangeConstraint(160, 160),
        ValueRangeConstraint(170, 170),
        ValueRangeConstraint(180, 180),
        ValueRangeConstraint(190, 190),
        ValueRangeConstraint(200, 200),
        ValueRangeConstraint(210, 210),
        ValueRangeConstraint(220, 220),
        ValueRangeConstraint(230, 230),
        ValueRangeConstraint(240, 240),
        ValueRangeConstraint(250, 250),
        ValueRangeConstraint(260, 260),
        ValueRangeConstraint(270, 270),
        ValueRangeConstraint(280, 280),
        ValueRangeConstraint(290, 290),
        ValueRangeConstraint(300, 300),
    )


_CnGR303IfGroupLapdSapi0t203_Type.__name__ = "Integer32"
_CnGR303IfGroupLapdSapi0t203_Object = MibTableColumn
cnGR303IfGroupLapdSapi0t203 = _CnGR303IfGroupLapdSapi0t203_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 1, 1, 17),
    _CnGR303IfGroupLapdSapi0t203_Type()
)
cnGR303IfGroupLapdSapi0t203.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnGR303IfGroupLapdSapi0t203.setStatus("current")


class _CnGR303IfGroupLapdSapi1k_Type(Integer32):
    """Custom type cnGR303IfGroupLapdSapi1k based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_CnGR303IfGroupLapdSapi1k_Type.__name__ = "Integer32"
_CnGR303IfGroupLapdSapi1k_Object = MibTableColumn
cnGR303IfGroupLapdSapi1k = _CnGR303IfGroupLapdSapi1k_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 1, 1, 18),
    _CnGR303IfGroupLapdSapi1k_Type()
)
cnGR303IfGroupLapdSapi1k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnGR303IfGroupLapdSapi1k.setStatus("current")


class _CnGR303IfGroupLapdSapi1n200_Type(Integer32):
    """Custom type cnGR303IfGroupLapdSapi1n200 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CnGR303IfGroupLapdSapi1n200_Type.__name__ = "Integer32"
_CnGR303IfGroupLapdSapi1n200_Object = MibTableColumn
cnGR303IfGroupLapdSapi1n200 = _CnGR303IfGroupLapdSapi1n200_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 1, 1, 19),
    _CnGR303IfGroupLapdSapi1n200_Type()
)
cnGR303IfGroupLapdSapi1n200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnGR303IfGroupLapdSapi1n200.setStatus("current")


class _CnGR303IfGroupLapdSapi1t200_Type(Integer32):
    """Custom type cnGR303IfGroupLapdSapi1t200 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(150, 150),
        ValueRangeConstraint(200, 200),
        ValueRangeConstraint(250, 250),
        ValueRangeConstraint(300, 300),
        ValueRangeConstraint(350, 350),
    )


_CnGR303IfGroupLapdSapi1t200_Type.__name__ = "Integer32"
_CnGR303IfGroupLapdSapi1t200_Object = MibTableColumn
cnGR303IfGroupLapdSapi1t200 = _CnGR303IfGroupLapdSapi1t200_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 1, 1, 20),
    _CnGR303IfGroupLapdSapi1t200_Type()
)
cnGR303IfGroupLapdSapi1t200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnGR303IfGroupLapdSapi1t200.setStatus("current")


class _CnGR303IfGroupLapdSapi1t203_Type(Integer32):
    """Custom type cnGR303IfGroupLapdSapi1t203 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(70, 70),
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(90, 90),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(110, 110),
        ValueRangeConstraint(120, 120),
        ValueRangeConstraint(130, 130),
        ValueRangeConstraint(140, 140),
        ValueRangeConstraint(150, 150),
        ValueRangeConstraint(160, 160),
        ValueRangeConstraint(170, 170),
        ValueRangeConstraint(180, 180),
        ValueRangeConstraint(190, 190),
        ValueRangeConstraint(200, 200),
        ValueRangeConstraint(210, 210),
        ValueRangeConstraint(220, 220),
        ValueRangeConstraint(230, 230),
        ValueRangeConstraint(240, 240),
        ValueRangeConstraint(250, 250),
        ValueRangeConstraint(260, 260),
        ValueRangeConstraint(270, 270),
        ValueRangeConstraint(280, 280),
        ValueRangeConstraint(290, 290),
        ValueRangeConstraint(300, 300),
    )


_CnGR303IfGroupLapdSapi1t203_Type.__name__ = "Integer32"
_CnGR303IfGroupLapdSapi1t203_Object = MibTableColumn
cnGR303IfGroupLapdSapi1t203 = _CnGR303IfGroupLapdSapi1t203_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 1, 1, 21),
    _CnGR303IfGroupLapdSapi1t203_Type()
)
cnGR303IfGroupLapdSapi1t203.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnGR303IfGroupLapdSapi1t203.setStatus("current")


class _CnGR303IfGroupEOCActivePath_Type(Integer32):
    """Custom type cnGR303IfGroupEOCActivePath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unavailable", 0),
          ("switch", 1),
          ("forceSwitch", 2),
          ("primary", 3),
          ("secondary", 4))
    )


_CnGR303IfGroupEOCActivePath_Type.__name__ = "Integer32"
_CnGR303IfGroupEOCActivePath_Object = MibTableColumn
cnGR303IfGroupEOCActivePath = _CnGR303IfGroupEOCActivePath_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 1, 1, 22),
    _CnGR303IfGroupEOCActivePath_Type()
)
cnGR303IfGroupEOCActivePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnGR303IfGroupEOCActivePath.setStatus("current")


class _CnGR303IfGroupTMCActivePath_Type(Integer32):
    """Custom type cnGR303IfGroupTMCActivePath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unavailable", 0),
          ("switch", 1),
          ("forceSwitch", 2),
          ("primary", 3),
          ("secondary", 4))
    )


_CnGR303IfGroupTMCActivePath_Type.__name__ = "Integer32"
_CnGR303IfGroupTMCActivePath_Object = MibTableColumn
cnGR303IfGroupTMCActivePath = _CnGR303IfGroupTMCActivePath_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 1, 1, 23),
    _CnGR303IfGroupTMCActivePath_Type()
)
cnGR303IfGroupTMCActivePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnGR303IfGroupTMCActivePath.setStatus("current")


class _CnGR303IfGroupEOCppsInhibit_Type(Integer32):
    """Custom type cnGR303IfGroupEOCppsInhibit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inhibit", 1),
          ("noInhibit", 2))
    )


_CnGR303IfGroupEOCppsInhibit_Type.__name__ = "Integer32"
_CnGR303IfGroupEOCppsInhibit_Object = MibTableColumn
cnGR303IfGroupEOCppsInhibit = _CnGR303IfGroupEOCppsInhibit_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 1, 1, 25),
    _CnGR303IfGroupEOCppsInhibit_Type()
)
cnGR303IfGroupEOCppsInhibit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnGR303IfGroupEOCppsInhibit.setStatus("current")


class _CnGR303IfGroupTMCppsInhibit_Type(Integer32):
    """Custom type cnGR303IfGroupTMCppsInhibit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inhibit", 1),
          ("noInhibit", 2))
    )


_CnGR303IfGroupTMCppsInhibit_Type.__name__ = "Integer32"
_CnGR303IfGroupTMCppsInhibit_Object = MibTableColumn
cnGR303IfGroupTMCppsInhibit = _CnGR303IfGroupTMCppsInhibit_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 1, 1, 26),
    _CnGR303IfGroupTMCppsInhibit_Type()
)
cnGR303IfGroupTMCppsInhibit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnGR303IfGroupTMCppsInhibit.setStatus("current")


class _CnGR303IfGroupF1Cable_Type(Integer32):
    """Custom type cnGR303IfGroupF1Cable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_CnGR303IfGroupF1Cable_Type.__name__ = "Integer32"
_CnGR303IfGroupF1Cable_Object = MibTableColumn
cnGR303IfGroupF1Cable = _CnGR303IfGroupF1Cable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 1, 1, 27),
    _CnGR303IfGroupF1Cable_Type()
)
cnGR303IfGroupF1Cable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnGR303IfGroupF1Cable.setStatus("current")


class _CnGR303IfGroupF1PairRangeStart_Type(Integer32):
    """Custom type cnGR303IfGroupF1PairRangeStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_CnGR303IfGroupF1PairRangeStart_Type.__name__ = "Integer32"
_CnGR303IfGroupF1PairRangeStart_Object = MibTableColumn
cnGR303IfGroupF1PairRangeStart = _CnGR303IfGroupF1PairRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 1, 1, 28),
    _CnGR303IfGroupF1PairRangeStart_Type()
)
cnGR303IfGroupF1PairRangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnGR303IfGroupF1PairRangeStart.setStatus("current")


class _CnGR303IfGroupF1PairRangeEnd_Type(Integer32):
    """Custom type cnGR303IfGroupF1PairRangeEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_CnGR303IfGroupF1PairRangeEnd_Type.__name__ = "Integer32"
_CnGR303IfGroupF1PairRangeEnd_Object = MibTableColumn
cnGR303IfGroupF1PairRangeEnd = _CnGR303IfGroupF1PairRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 1, 1, 29),
    _CnGR303IfGroupF1PairRangeEnd_Type()
)
cnGR303IfGroupF1PairRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnGR303IfGroupF1PairRangeEnd.setStatus("current")
_CnGR303IfGroupRowStatus_Type = RowStatus
_CnGR303IfGroupRowStatus_Object = MibTableColumn
cnGR303IfGroupRowStatus = _CnGR303IfGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 1, 1, 30),
    _CnGR303IfGroupRowStatus_Type()
)
cnGR303IfGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnGR303IfGroupRowStatus.setStatus("current")
_CnGR303LinkTable_Object = MibTable
cnGR303LinkTable = _CnGR303LinkTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cnGR303LinkTable.setStatus("current")
_CnGR303LinkEntry_Object = MibTableRow
cnGR303LinkEntry = _CnGR303LinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 4, 1)
)
cnGR303LinkEntry.setIndexNames(
    (0, "CEM-GR303", "cnGR303LinkIfGroupIndex"),
    (0, "CEM-GR303", "cnGR303LinkIfIndex"),
)
if mibBuilder.loadTexts:
    cnGR303LinkEntry.setStatus("current")
_CnGR303LinkIfGroupIndex_Type = CnIfGroupIndexRange
_CnGR303LinkIfGroupIndex_Object = MibTableColumn
cnGR303LinkIfGroupIndex = _CnGR303LinkIfGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 4, 1, 1),
    _CnGR303LinkIfGroupIndex_Type()
)
cnGR303LinkIfGroupIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnGR303LinkIfGroupIndex.setStatus("current")
_CnGR303LinkIfIndex_Type = InterfaceIndex
_CnGR303LinkIfIndex_Object = MibTableColumn
cnGR303LinkIfIndex = _CnGR303LinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 4, 1, 2),
    _CnGR303LinkIfIndex_Type()
)
cnGR303LinkIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnGR303LinkIfIndex.setStatus("current")
_CnGR303LinkType_Type = CnIfGroupLinkType
_CnGR303LinkType_Object = MibTableColumn
cnGR303LinkType = _CnGR303LinkType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 4, 1, 3),
    _CnGR303LinkType_Type()
)
cnGR303LinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnGR303LinkType.setStatus("current")


class _CnGR303LinkLogicalNumber_Type(Integer32):
    """Custom type cnGR303LinkLogicalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_CnGR303LinkLogicalNumber_Type.__name__ = "Integer32"
_CnGR303LinkLogicalNumber_Object = MibTableColumn
cnGR303LinkLogicalNumber = _CnGR303LinkLogicalNumber_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 4, 1, 4),
    _CnGR303LinkLogicalNumber_Type()
)
cnGR303LinkLogicalNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnGR303LinkLogicalNumber.setStatus("current")


class _CnGR303LinkPrimaryServiceState_Type(Integer32):
    """Custom type cnGR303LinkPrimaryServiceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("outOfService", 2))
    )


_CnGR303LinkPrimaryServiceState_Type.__name__ = "Integer32"
_CnGR303LinkPrimaryServiceState_Object = MibTableColumn
cnGR303LinkPrimaryServiceState = _CnGR303LinkPrimaryServiceState_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 4, 1, 6),
    _CnGR303LinkPrimaryServiceState_Type()
)
cnGR303LinkPrimaryServiceState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnGR303LinkPrimaryServiceState.setStatus("current")
_CnGR303LinkSecondaryServiceState_Type = CnGR303LinkSecondaryServiceStateType
_CnGR303LinkSecondaryServiceState_Object = MibTableColumn
cnGR303LinkSecondaryServiceState = _CnGR303LinkSecondaryServiceState_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 4, 1, 7),
    _CnGR303LinkSecondaryServiceState_Type()
)
cnGR303LinkSecondaryServiceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGR303LinkSecondaryServiceState.setStatus("current")
_CnGR303LinkConfigStatus_Type = Cn1000ConfigurationStatus
_CnGR303LinkConfigStatus_Object = MibTableColumn
cnGR303LinkConfigStatus = _CnGR303LinkConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 4, 1, 8),
    _CnGR303LinkConfigStatus_Type()
)
cnGR303LinkConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGR303LinkConfigStatus.setStatus("current")
_CnGR303LinkRowStatus_Type = RowStatus
_CnGR303LinkRowStatus_Object = MibTableColumn
cnGR303LinkRowStatus = _CnGR303LinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 4, 1, 9),
    _CnGR303LinkRowStatus_Type()
)
cnGR303LinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnGR303LinkRowStatus.setStatus("current")
_CnGR303LapdStatusTable_Object = MibTable
cnGR303LapdStatusTable = _CnGR303LapdStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 9)
)
if mibBuilder.loadTexts:
    cnGR303LapdStatusTable.setStatus("current")
_CnGR303LapdStatusEntry_Object = MibTableRow
cnGR303LapdStatusEntry = _CnGR303LapdStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 9, 1)
)
cnGR303LapdStatusEntry.setIndexNames(
    (0, "CEM-GR303", "cnGR303LapdStatusIfGroupIndex"),
)
if mibBuilder.loadTexts:
    cnGR303LapdStatusEntry.setStatus("current")
_CnGR303LapdStatusShelf_Type = Cn1000ShelfRange
_CnGR303LapdStatusShelf_Object = MibTableColumn
cnGR303LapdStatusShelf = _CnGR303LapdStatusShelf_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 9, 1, 1),
    _CnGR303LapdStatusShelf_Type()
)
cnGR303LapdStatusShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnGR303LapdStatusShelf.setStatus("current")
_CnGR303LapdStatusSlotGroup_Type = CnSlotGroupNameType
_CnGR303LapdStatusSlotGroup_Object = MibTableColumn
cnGR303LapdStatusSlotGroup = _CnGR303LapdStatusSlotGroup_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 9, 1, 2),
    _CnGR303LapdStatusSlotGroup_Type()
)
cnGR303LapdStatusSlotGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnGR303LapdStatusSlotGroup.setStatus("current")
_CnGR303LapdStatusIfGroupIndex_Type = CnIfGroupIndexRange
_CnGR303LapdStatusIfGroupIndex_Object = MibTableColumn
cnGR303LapdStatusIfGroupIndex = _CnGR303LapdStatusIfGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 9, 1, 3),
    _CnGR303LapdStatusIfGroupIndex_Type()
)
cnGR303LapdStatusIfGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnGR303LapdStatusIfGroupIndex.setStatus("current")
_CnGR303LapdStatusPrimaryEocOamp_Type = CnGR303LinkStatusType
_CnGR303LapdStatusPrimaryEocOamp_Object = MibTableColumn
cnGR303LapdStatusPrimaryEocOamp = _CnGR303LapdStatusPrimaryEocOamp_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 9, 1, 4),
    _CnGR303LapdStatusPrimaryEocOamp_Type()
)
cnGR303LapdStatusPrimaryEocOamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGR303LapdStatusPrimaryEocOamp.setStatus("current")
_CnGR303LapdStatusPrimaryEocPps_Type = CnGR303LinkStatusType
_CnGR303LapdStatusPrimaryEocPps_Object = MibTableColumn
cnGR303LapdStatusPrimaryEocPps = _CnGR303LapdStatusPrimaryEocPps_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 9, 1, 5),
    _CnGR303LapdStatusPrimaryEocPps_Type()
)
cnGR303LapdStatusPrimaryEocPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGR303LapdStatusPrimaryEocPps.setStatus("current")
_CnGR303LapdStatusPrimaryTmcCallp_Type = CnGR303LinkStatusType
_CnGR303LapdStatusPrimaryTmcCallp_Object = MibTableColumn
cnGR303LapdStatusPrimaryTmcCallp = _CnGR303LapdStatusPrimaryTmcCallp_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 9, 1, 6),
    _CnGR303LapdStatusPrimaryTmcCallp_Type()
)
cnGR303LapdStatusPrimaryTmcCallp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGR303LapdStatusPrimaryTmcCallp.setStatus("current")
_CnGR303LapdStatusPrimaryTmcPps_Type = CnGR303LinkStatusType
_CnGR303LapdStatusPrimaryTmcPps_Object = MibTableColumn
cnGR303LapdStatusPrimaryTmcPps = _CnGR303LapdStatusPrimaryTmcPps_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 9, 1, 7),
    _CnGR303LapdStatusPrimaryTmcPps_Type()
)
cnGR303LapdStatusPrimaryTmcPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGR303LapdStatusPrimaryTmcPps.setStatus("current")
_CnGR303LapdStatusSecondaryEocOamp_Type = CnGR303LinkStatusType
_CnGR303LapdStatusSecondaryEocOamp_Object = MibTableColumn
cnGR303LapdStatusSecondaryEocOamp = _CnGR303LapdStatusSecondaryEocOamp_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 9, 1, 8),
    _CnGR303LapdStatusSecondaryEocOamp_Type()
)
cnGR303LapdStatusSecondaryEocOamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGR303LapdStatusSecondaryEocOamp.setStatus("current")
_CnGR303LapdStatusSecondaryEocPps_Type = CnGR303LinkStatusType
_CnGR303LapdStatusSecondaryEocPps_Object = MibTableColumn
cnGR303LapdStatusSecondaryEocPps = _CnGR303LapdStatusSecondaryEocPps_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 9, 1, 9),
    _CnGR303LapdStatusSecondaryEocPps_Type()
)
cnGR303LapdStatusSecondaryEocPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGR303LapdStatusSecondaryEocPps.setStatus("current")
_CnGR303LapdStatusSecondaryTmcCallp_Type = CnGR303LinkStatusType
_CnGR303LapdStatusSecondaryTmcCallp_Object = MibTableColumn
cnGR303LapdStatusSecondaryTmcCallp = _CnGR303LapdStatusSecondaryTmcCallp_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 9, 1, 10),
    _CnGR303LapdStatusSecondaryTmcCallp_Type()
)
cnGR303LapdStatusSecondaryTmcCallp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGR303LapdStatusSecondaryTmcCallp.setStatus("current")
_CnGR303LapdStatusSecondaryTmcPps_Type = CnGR303LinkStatusType
_CnGR303LapdStatusSecondaryTmcPps_Object = MibTableColumn
cnGR303LapdStatusSecondaryTmcPps = _CnGR303LapdStatusSecondaryTmcPps_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 9, 1, 11),
    _CnGR303LapdStatusSecondaryTmcPps_Type()
)
cnGR303LapdStatusSecondaryTmcPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGR303LapdStatusSecondaryTmcPps.setStatus("current")
_CnGR303LapdStatusActiveEocPath_Type = CnGR303LinkStatusActivePath
_CnGR303LapdStatusActiveEocPath_Object = MibTableColumn
cnGR303LapdStatusActiveEocPath = _CnGR303LapdStatusActiveEocPath_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 9, 1, 12),
    _CnGR303LapdStatusActiveEocPath_Type()
)
cnGR303LapdStatusActiveEocPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGR303LapdStatusActiveEocPath.setStatus("current")
_CnGR303LapdStatusActiveTmcPath_Type = CnGR303LinkStatusActivePath
_CnGR303LapdStatusActiveTmcPath_Object = MibTableColumn
cnGR303LapdStatusActiveTmcPath = _CnGR303LapdStatusActiveTmcPath_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 9, 1, 13),
    _CnGR303LapdStatusActiveTmcPath_Type()
)
cnGR303LapdStatusActiveTmcPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGR303LapdStatusActiveTmcPath.setStatus("current")

# Managed Objects groups

cnGR303ObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 1, 1, 10)
)
cnGR303ObjectsGroup.setObjects(
      *(("CEM-GR303", "cnGR303IfGroupShelf"),
        ("CEM-GR303", "cnGR303IfGroupSlotGroup"),
        ("CEM-GR303", "cnGR303IfGroupIndex"),
        ("CEM-GR303", "cnGR303IfGroupConnectionIndex"),
        ("CEM-GR303", "cnGR303IfGroupDescription"),
        ("CEM-GR303", "cnGR303IfGroupAdminState"),
        ("CEM-GR303", "cnGR303IfGroupConfigStatus"),
        ("CEM-GR303", "cnGR303IfGroupIdtType"),
        ("CEM-GR303", "cnGR303IfGroupFlowThruProv"),
        ("CEM-GR303", "cnGR303IfGroupQ931t303"),
        ("CEM-GR303", "cnGR303IfGroupQ931t308"),
        ("CEM-GR303", "cnGR303IfGroupQ931t396"),
        ("CEM-GR303", "cnGR303IfGroupQ931t397"),
        ("CEM-GR303", "cnGR303IfGroupLapdSapi0k"),
        ("CEM-GR303", "cnGR303IfGroupLapdSapi0n200"),
        ("CEM-GR303", "cnGR303IfGroupLapdSapi0t200"),
        ("CEM-GR303", "cnGR303IfGroupLapdSapi0t203"),
        ("CEM-GR303", "cnGR303IfGroupLapdSapi1k"),
        ("CEM-GR303", "cnGR303IfGroupLapdSapi1n200"),
        ("CEM-GR303", "cnGR303IfGroupLapdSapi1t200"),
        ("CEM-GR303", "cnGR303IfGroupLapdSapi1t203"),
        ("CEM-GR303", "cnGR303IfGroupEOCActivePath"),
        ("CEM-GR303", "cnGR303IfGroupTMCActivePath"),
        ("CEM-GR303", "cnGR303IfGroupEOCppsInhibit"),
        ("CEM-GR303", "cnGR303IfGroupTMCppsInhibit"),
        ("CEM-GR303", "cnGR303IfGroupF1Cable"),
        ("CEM-GR303", "cnGR303IfGroupF1PairRangeStart"),
        ("CEM-GR303", "cnGR303IfGroupF1PairRangeEnd"),
        ("CEM-GR303", "cnGR303IfGroupRowStatus"),
        ("CEM-GR303", "cnGR303LinkIfGroupIndex"),
        ("CEM-GR303", "cnGR303LinkIfIndex"),
        ("CEM-GR303", "cnGR303LinkType"),
        ("CEM-GR303", "cnGR303LinkLogicalNumber"),
        ("CEM-GR303", "cnGR303LinkPrimaryServiceState"),
        ("CEM-GR303", "cnGR303LinkSecondaryServiceState"),
        ("CEM-GR303", "cnGR303LinkConfigStatus"),
        ("CEM-GR303", "cnGR303LinkRowStatus"),
        ("CEM-GR303", "cnGR303LapdStatusShelf"),
        ("CEM-GR303", "cnGR303LapdStatusSlotGroup"),
        ("CEM-GR303", "cnGR303LapdStatusIfGroupIndex"),
        ("CEM-GR303", "cnGR303LapdStatusPrimaryEocOamp"),
        ("CEM-GR303", "cnGR303LapdStatusPrimaryEocPps"),
        ("CEM-GR303", "cnGR303LapdStatusPrimaryTmcCallp"),
        ("CEM-GR303", "cnGR303LapdStatusPrimaryTmcPps"),
        ("CEM-GR303", "cnGR303LapdStatusSecondaryEocOamp"),
        ("CEM-GR303", "cnGR303LapdStatusSecondaryEocPps"),
        ("CEM-GR303", "cnGR303LapdStatusSecondaryTmcCallp"),
        ("CEM-GR303", "cnGR303LapdStatusSecondaryTmcPps"),
        ("CEM-GR303", "cnGR303LapdStatusActiveEocPath"),
        ("CEM-GR303", "cnGR303LapdStatusActiveTmcPath"))
)
if mibBuilder.loadTexts:
    cnGR303ObjectsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CEM-GR303",
    **{"CnGR303IDTType": CnGR303IDTType,
       "CnGR303LinkSecondaryServiceStateType": CnGR303LinkSecondaryServiceStateType,
       "CnGR303LinkStatusType": CnGR303LinkStatusType,
       "CnGR303LinkStatusActivePath": CnGR303LinkStatusActivePath,
       "cnGR303Module": cnGR303Module,
       "cnGR303IfGroupConfigTable": cnGR303IfGroupConfigTable,
       "cnGR303IfGroupConfigEntry": cnGR303IfGroupConfigEntry,
       "cnGR303IfGroupShelf": cnGR303IfGroupShelf,
       "cnGR303IfGroupSlotGroup": cnGR303IfGroupSlotGroup,
       "cnGR303IfGroupIndex": cnGR303IfGroupIndex,
       "cnGR303IfGroupConnectionIndex": cnGR303IfGroupConnectionIndex,
       "cnGR303IfGroupDescription": cnGR303IfGroupDescription,
       "cnGR303IfGroupAdminState": cnGR303IfGroupAdminState,
       "cnGR303IfGroupConfigStatus": cnGR303IfGroupConfigStatus,
       "cnGR303IfGroupIdtType": cnGR303IfGroupIdtType,
       "cnGR303IfGroupFlowThruProv": cnGR303IfGroupFlowThruProv,
       "cnGR303IfGroupQ931t303": cnGR303IfGroupQ931t303,
       "cnGR303IfGroupQ931t308": cnGR303IfGroupQ931t308,
       "cnGR303IfGroupQ931t396": cnGR303IfGroupQ931t396,
       "cnGR303IfGroupQ931t397": cnGR303IfGroupQ931t397,
       "cnGR303IfGroupLapdSapi0k": cnGR303IfGroupLapdSapi0k,
       "cnGR303IfGroupLapdSapi0n200": cnGR303IfGroupLapdSapi0n200,
       "cnGR303IfGroupLapdSapi0t200": cnGR303IfGroupLapdSapi0t200,
       "cnGR303IfGroupLapdSapi0t203": cnGR303IfGroupLapdSapi0t203,
       "cnGR303IfGroupLapdSapi1k": cnGR303IfGroupLapdSapi1k,
       "cnGR303IfGroupLapdSapi1n200": cnGR303IfGroupLapdSapi1n200,
       "cnGR303IfGroupLapdSapi1t200": cnGR303IfGroupLapdSapi1t200,
       "cnGR303IfGroupLapdSapi1t203": cnGR303IfGroupLapdSapi1t203,
       "cnGR303IfGroupEOCActivePath": cnGR303IfGroupEOCActivePath,
       "cnGR303IfGroupTMCActivePath": cnGR303IfGroupTMCActivePath,
       "cnGR303IfGroupEOCppsInhibit": cnGR303IfGroupEOCppsInhibit,
       "cnGR303IfGroupTMCppsInhibit": cnGR303IfGroupTMCppsInhibit,
       "cnGR303IfGroupF1Cable": cnGR303IfGroupF1Cable,
       "cnGR303IfGroupF1PairRangeStart": cnGR303IfGroupF1PairRangeStart,
       "cnGR303IfGroupF1PairRangeEnd": cnGR303IfGroupF1PairRangeEnd,
       "cnGR303IfGroupRowStatus": cnGR303IfGroupRowStatus,
       "cnGR303LinkTable": cnGR303LinkTable,
       "cnGR303LinkEntry": cnGR303LinkEntry,
       "cnGR303LinkIfGroupIndex": cnGR303LinkIfGroupIndex,
       "cnGR303LinkIfIndex": cnGR303LinkIfIndex,
       "cnGR303LinkType": cnGR303LinkType,
       "cnGR303LinkLogicalNumber": cnGR303LinkLogicalNumber,
       "cnGR303LinkPrimaryServiceState": cnGR303LinkPrimaryServiceState,
       "cnGR303LinkSecondaryServiceState": cnGR303LinkSecondaryServiceState,
       "cnGR303LinkConfigStatus": cnGR303LinkConfigStatus,
       "cnGR303LinkRowStatus": cnGR303LinkRowStatus,
       "cnGR303LapdStatusTable": cnGR303LapdStatusTable,
       "cnGR303LapdStatusEntry": cnGR303LapdStatusEntry,
       "cnGR303LapdStatusShelf": cnGR303LapdStatusShelf,
       "cnGR303LapdStatusSlotGroup": cnGR303LapdStatusSlotGroup,
       "cnGR303LapdStatusIfGroupIndex": cnGR303LapdStatusIfGroupIndex,
       "cnGR303LapdStatusPrimaryEocOamp": cnGR303LapdStatusPrimaryEocOamp,
       "cnGR303LapdStatusPrimaryEocPps": cnGR303LapdStatusPrimaryEocPps,
       "cnGR303LapdStatusPrimaryTmcCallp": cnGR303LapdStatusPrimaryTmcCallp,
       "cnGR303LapdStatusPrimaryTmcPps": cnGR303LapdStatusPrimaryTmcPps,
       "cnGR303LapdStatusSecondaryEocOamp": cnGR303LapdStatusSecondaryEocOamp,
       "cnGR303LapdStatusSecondaryEocPps": cnGR303LapdStatusSecondaryEocPps,
       "cnGR303LapdStatusSecondaryTmcCallp": cnGR303LapdStatusSecondaryTmcCallp,
       "cnGR303LapdStatusSecondaryTmcPps": cnGR303LapdStatusSecondaryTmcPps,
       "cnGR303LapdStatusActiveEocPath": cnGR303LapdStatusActiveEocPath,
       "cnGR303LapdStatusActiveTmcPath": cnGR303LapdStatusActiveTmcPath,
       "cnGR303ObjectsGroup": cnGR303ObjectsGroup}
)
