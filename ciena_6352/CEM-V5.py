# SNMP MIB module (CEM-V5) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_6352/CEM-V5.mib
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

(Cn1000ConfigurationStatus,) = mibBuilder.importSymbols(
    "CEM-CN1000",
    "Cn1000ConfigurationStatus")

(CnIfGroupIndexRange,
 CnIfGroupLinkType,
 cnInterfacesModule) = mibBuilder.importSymbols(
    "CEM-INTERFACES",
    "CnIfGroupIndexRange",
    "CnIfGroupLinkType",
    "cnInterfacesModule")

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

cnV5Module = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CnV5LapvChannelStatus(TextualConvention, Integer32):
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
        *(("unavailable", 0),
          ("up", 1),
          ("down", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CnV5_ObjectIdentity = ObjectIdentity
cnV5 = _CnV5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9)
)
_CnV5IfGroupConfigTable_Object = MibTable
cnV5IfGroupConfigTable = _CnV5IfGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    cnV5IfGroupConfigTable.setStatus("current")
_CnV5IfGroupConfigEntry_Object = MibTableRow
cnV5IfGroupConfigEntry = _CnV5IfGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 1, 1)
)
cnV5IfGroupConfigEntry.setIndexNames(
    (0, "CEM-V5", "cnV5IfGroupIndex"),
)
if mibBuilder.loadTexts:
    cnV5IfGroupConfigEntry.setStatus("current")
_CnV5IfGroupIndex_Type = CnIfGroupIndexRange
_CnV5IfGroupIndex_Object = MibTableColumn
cnV5IfGroupIndex = _CnV5IfGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 1, 1, 1),
    _CnV5IfGroupIndex_Type()
)
cnV5IfGroupIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnV5IfGroupIndex.setStatus("current")


class _CnV5IfGroupShelf_Type(Integer32):
    """Custom type cnV5IfGroupShelf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_CnV5IfGroupShelf_Type.__name__ = "Integer32"
_CnV5IfGroupShelf_Object = MibTableColumn
cnV5IfGroupShelf = _CnV5IfGroupShelf_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 1, 1, 2),
    _CnV5IfGroupShelf_Type()
)
cnV5IfGroupShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnV5IfGroupShelf.setStatus("current")
_CnV5IfGroupSlotGroup_Type = CnSlotGroupNameType
_CnV5IfGroupSlotGroup_Object = MibTableColumn
cnV5IfGroupSlotGroup = _CnV5IfGroupSlotGroup_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 1, 1, 3),
    _CnV5IfGroupSlotGroup_Type()
)
cnV5IfGroupSlotGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnV5IfGroupSlotGroup.setStatus("current")


class _CnV5IfGroupConnectionIndex_Type(Integer32):
    """Custom type cnV5IfGroupConnectionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_CnV5IfGroupConnectionIndex_Type.__name__ = "Integer32"
_CnV5IfGroupConnectionIndex_Object = MibTableColumn
cnV5IfGroupConnectionIndex = _CnV5IfGroupConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 1, 1, 4),
    _CnV5IfGroupConnectionIndex_Type()
)
cnV5IfGroupConnectionIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnV5IfGroupConnectionIndex.setStatus("current")


class _CnV5IfGroupDescription_Type(OctetString):
    """Custom type cnV5IfGroupDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_CnV5IfGroupDescription_Type.__name__ = "OctetString"
_CnV5IfGroupDescription_Object = MibTableColumn
cnV5IfGroupDescription = _CnV5IfGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 1, 1, 5),
    _CnV5IfGroupDescription_Type()
)
cnV5IfGroupDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnV5IfGroupDescription.setStatus("current")


class _CnV5IfGroupLeType_Type(Integer32):
    """Custom type cnV5IfGroupLeType based on Integer32"""
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
        *(("cn5ESS", 1),
          ("cnDMS", 2),
          ("cnEWSD", 3),
          ("cnE10", 4),
          ("cnS12", 5),
          ("cnDX220", 6),
          ("cnAXE10", 7),
          ("cnHJD04", 8),
          ("cnHUAWEI", 9))
    )


_CnV5IfGroupLeType_Type.__name__ = "Integer32"
_CnV5IfGroupLeType_Object = MibTableColumn
cnV5IfGroupLeType = _CnV5IfGroupLeType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 1, 1, 6),
    _CnV5IfGroupLeType_Type()
)
cnV5IfGroupLeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnV5IfGroupLeType.setStatus("current")
_CnV5IfGroupConfigStatus_Type = Cn1000ConfigurationStatus
_CnV5IfGroupConfigStatus_Object = MibTableColumn
cnV5IfGroupConfigStatus = _CnV5IfGroupConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 1, 1, 7),
    _CnV5IfGroupConfigStatus_Type()
)
cnV5IfGroupConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnV5IfGroupConfigStatus.setStatus("current")


class _CnV5IfGroupAdminState_Type(Integer32):
    """Custom type cnV5IfGroupAdminState based on Integer32"""
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


_CnV5IfGroupAdminState_Type.__name__ = "Integer32"
_CnV5IfGroupAdminState_Object = MibTableColumn
cnV5IfGroupAdminState = _CnV5IfGroupAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 1, 1, 8),
    _CnV5IfGroupAdminState_Type()
)
cnV5IfGroupAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnV5IfGroupAdminState.setStatus("current")


class _CnV5IfGroupOperState_Type(Integer32):
    """Custom type cnV5IfGroupOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unavailable", 0),
          ("unprovisioned", 1),
          ("idle", 2),
          ("startup", 3),
          ("activating", 4),
          ("restart", 5),
          ("active", 6))
    )


_CnV5IfGroupOperState_Type.__name__ = "Integer32"
_CnV5IfGroupOperState_Object = MibTableColumn
cnV5IfGroupOperState = _CnV5IfGroupOperState_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 1, 1, 9),
    _CnV5IfGroupOperState_Type()
)
cnV5IfGroupOperState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnV5IfGroupOperState.setStatus("current")


class _CnV5IfGroupProtocol_Type(Integer32):
    """Custom type cnV5IfGroupProtocol based on Integer32"""
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
        *(("cnV511", 1),
          ("cnV512", 2),
          ("cnV521", 3),
          ("cnV522", 4))
    )


_CnV5IfGroupProtocol_Type.__name__ = "Integer32"
_CnV5IfGroupProtocol_Object = MibTableColumn
cnV5IfGroupProtocol = _CnV5IfGroupProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 1, 1, 10),
    _CnV5IfGroupProtocol_Type()
)
cnV5IfGroupProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnV5IfGroupProtocol.setStatus("current")


class _CnV5IfGroupInterfaceId_Type(Integer32):
    """Custom type cnV5IfGroupInterfaceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_CnV5IfGroupInterfaceId_Type.__name__ = "Integer32"
_CnV5IfGroupInterfaceId_Object = MibTableColumn
cnV5IfGroupInterfaceId = _CnV5IfGroupInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 1, 1, 11),
    _CnV5IfGroupInterfaceId_Type()
)
cnV5IfGroupInterfaceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnV5IfGroupInterfaceId.setStatus("current")


class _CnV5IfGroupProvisioningVariant_Type(Integer32):
    """Custom type cnV5IfGroupProvisioningVariant based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_CnV5IfGroupProvisioningVariant_Type.__name__ = "Integer32"
_CnV5IfGroupProvisioningVariant_Object = MibTableColumn
cnV5IfGroupProvisioningVariant = _CnV5IfGroupProvisioningVariant_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 1, 1, 12),
    _CnV5IfGroupProvisioningVariant_Type()
)
cnV5IfGroupProvisioningVariant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnV5IfGroupProvisioningVariant.setStatus("current")


class _CnV5IfGroupLinkNumberingType_Type(Integer32):
    """Custom type cnV5IfGroupLinkNumberingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cnZeroBased", 0),
          ("cnOneBased", 1))
    )


_CnV5IfGroupLinkNumberingType_Type.__name__ = "Integer32"
_CnV5IfGroupLinkNumberingType_Object = MibTableColumn
cnV5IfGroupLinkNumberingType = _CnV5IfGroupLinkNumberingType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 1, 1, 13),
    _CnV5IfGroupLinkNumberingType_Type()
)
cnV5IfGroupLinkNumberingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnV5IfGroupLinkNumberingType.setStatus("current")


class _CnV5IfGroupProtGroup1LogChan_Type(Integer32):
    """Custom type cnV5IfGroupProtGroup1LogChan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CnV5IfGroupProtGroup1LogChan_Type.__name__ = "Integer32"
_CnV5IfGroupProtGroup1LogChan_Object = MibTableColumn
cnV5IfGroupProtGroup1LogChan = _CnV5IfGroupProtGroup1LogChan_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 1, 1, 14),
    _CnV5IfGroupProtGroup1LogChan_Type()
)
cnV5IfGroupProtGroup1LogChan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnV5IfGroupProtGroup1LogChan.setStatus("current")


class _CnV5IfGroupPstnLogChan_Type(Integer32):
    """Custom type cnV5IfGroupPstnLogChan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CnV5IfGroupPstnLogChan_Type.__name__ = "Integer32"
_CnV5IfGroupPstnLogChan_Object = MibTableColumn
cnV5IfGroupPstnLogChan = _CnV5IfGroupPstnLogChan_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 1, 1, 15),
    _CnV5IfGroupPstnLogChan_Type()
)
cnV5IfGroupPstnLogChan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnV5IfGroupPstnLogChan.setStatus("current")
_CnV5IfGroupLapvPstnChanState_Type = CnV5LapvChannelStatus
_CnV5IfGroupLapvPstnChanState_Object = MibTableColumn
cnV5IfGroupLapvPstnChanState = _CnV5IfGroupLapvPstnChanState_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 1, 1, 18),
    _CnV5IfGroupLapvPstnChanState_Type()
)
cnV5IfGroupLapvPstnChanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnV5IfGroupLapvPstnChanState.setStatus("current")
_CnV5IfGroupLapvCtrlChanState_Type = CnV5LapvChannelStatus
_CnV5IfGroupLapvCtrlChanState_Object = MibTableColumn
cnV5IfGroupLapvCtrlChanState = _CnV5IfGroupLapvCtrlChanState_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 1, 1, 19),
    _CnV5IfGroupLapvCtrlChanState_Type()
)
cnV5IfGroupLapvCtrlChanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnV5IfGroupLapvCtrlChanState.setStatus("current")
_CnV5IfGroupLapvBccChanState_Type = CnV5LapvChannelStatus
_CnV5IfGroupLapvBccChanState_Object = MibTableColumn
cnV5IfGroupLapvBccChanState = _CnV5IfGroupLapvBccChanState_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 1, 1, 20),
    _CnV5IfGroupLapvBccChanState_Type()
)
cnV5IfGroupLapvBccChanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnV5IfGroupLapvBccChanState.setStatus("current")
_CnV5IfGroupLapvLinkChanState_Type = CnV5LapvChannelStatus
_CnV5IfGroupLapvLinkChanState_Object = MibTableColumn
cnV5IfGroupLapvLinkChanState = _CnV5IfGroupLapvLinkChanState_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 1, 1, 21),
    _CnV5IfGroupLapvLinkChanState_Type()
)
cnV5IfGroupLapvLinkChanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnV5IfGroupLapvLinkChanState.setStatus("current")
_CnV5IfGroupLapvPrimaryPgState_Type = CnV5LapvChannelStatus
_CnV5IfGroupLapvPrimaryPgState_Object = MibTableColumn
cnV5IfGroupLapvPrimaryPgState = _CnV5IfGroupLapvPrimaryPgState_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 1, 1, 23),
    _CnV5IfGroupLapvPrimaryPgState_Type()
)
cnV5IfGroupLapvPrimaryPgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnV5IfGroupLapvPrimaryPgState.setStatus("current")
_CnV5IfGroupLapvSecondaryPgState_Type = CnV5LapvChannelStatus
_CnV5IfGroupLapvSecondaryPgState_Object = MibTableColumn
cnV5IfGroupLapvSecondaryPgState = _CnV5IfGroupLapvSecondaryPgState_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 1, 1, 24),
    _CnV5IfGroupLapvSecondaryPgState_Type()
)
cnV5IfGroupLapvSecondaryPgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnV5IfGroupLapvSecondaryPgState.setStatus("current")


class _CnV5IfGroupLapvActivePg1Chan_Type(Integer32):
    """Custom type cnV5IfGroupLapvActivePg1Chan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CnV5IfGroupLapvActivePg1Chan_Type.__name__ = "Integer32"
_CnV5IfGroupLapvActivePg1Chan_Object = MibTableColumn
cnV5IfGroupLapvActivePg1Chan = _CnV5IfGroupLapvActivePg1Chan_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 1, 1, 25),
    _CnV5IfGroupLapvActivePg1Chan_Type()
)
cnV5IfGroupLapvActivePg1Chan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnV5IfGroupLapvActivePg1Chan.setStatus("current")


class _CnV5IfGroupLapvActivePstnChan_Type(Integer32):
    """Custom type cnV5IfGroupLapvActivePstnChan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CnV5IfGroupLapvActivePstnChan_Type.__name__ = "Integer32"
_CnV5IfGroupLapvActivePstnChan_Object = MibTableColumn
cnV5IfGroupLapvActivePstnChan = _CnV5IfGroupLapvActivePstnChan_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 1, 1, 26),
    _CnV5IfGroupLapvActivePstnChan_Type()
)
cnV5IfGroupLapvActivePstnChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnV5IfGroupLapvActivePstnChan.setStatus("current")
_CnV5IfGroupRowStatus_Type = RowStatus
_CnV5IfGroupRowStatus_Object = MibTableColumn
cnV5IfGroupRowStatus = _CnV5IfGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 1, 1, 27),
    _CnV5IfGroupRowStatus_Type()
)
cnV5IfGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnV5IfGroupRowStatus.setStatus("current")


class _CnV5IfGroupPstnPrimaryLogLink_Type(Integer32):
    """Custom type cnV5IfGroupPstnPrimaryLogLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CnV5IfGroupPstnPrimaryLogLink_Type.__name__ = "Integer32"
_CnV5IfGroupPstnPrimaryLogLink_Object = MibTableColumn
cnV5IfGroupPstnPrimaryLogLink = _CnV5IfGroupPstnPrimaryLogLink_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 1, 1, 28),
    _CnV5IfGroupPstnPrimaryLogLink_Type()
)
cnV5IfGroupPstnPrimaryLogLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnV5IfGroupPstnPrimaryLogLink.setStatus("current")


class _CnV5IfGroupPstnPrimaryTimeSlot_Type(Integer32):
    """Custom type cnV5IfGroupPstnPrimaryTimeSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_CnV5IfGroupPstnPrimaryTimeSlot_Type.__name__ = "Integer32"
_CnV5IfGroupPstnPrimaryTimeSlot_Object = MibTableColumn
cnV5IfGroupPstnPrimaryTimeSlot = _CnV5IfGroupPstnPrimaryTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 1, 1, 29),
    _CnV5IfGroupPstnPrimaryTimeSlot_Type()
)
cnV5IfGroupPstnPrimaryTimeSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnV5IfGroupPstnPrimaryTimeSlot.setStatus("current")


class _CnV5IfGroupPstnSecondaryLogLink_Type(Integer32):
    """Custom type cnV5IfGroupPstnSecondaryLogLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CnV5IfGroupPstnSecondaryLogLink_Type.__name__ = "Integer32"
_CnV5IfGroupPstnSecondaryLogLink_Object = MibTableColumn
cnV5IfGroupPstnSecondaryLogLink = _CnV5IfGroupPstnSecondaryLogLink_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 1, 1, 30),
    _CnV5IfGroupPstnSecondaryLogLink_Type()
)
cnV5IfGroupPstnSecondaryLogLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnV5IfGroupPstnSecondaryLogLink.setStatus("current")


class _CnV5IfGroupPstnSecondaryTimeSlot_Type(Integer32):
    """Custom type cnV5IfGroupPstnSecondaryTimeSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_CnV5IfGroupPstnSecondaryTimeSlot_Type.__name__ = "Integer32"
_CnV5IfGroupPstnSecondaryTimeSlot_Object = MibTableColumn
cnV5IfGroupPstnSecondaryTimeSlot = _CnV5IfGroupPstnSecondaryTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 1, 1, 31),
    _CnV5IfGroupPstnSecondaryTimeSlot_Type()
)
cnV5IfGroupPstnSecondaryTimeSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnV5IfGroupPstnSecondaryTimeSlot.setStatus("current")
_CnV5IfGroupLinkTable_Object = MibTable
cnV5IfGroupLinkTable = _CnV5IfGroupLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 2)
)
if mibBuilder.loadTexts:
    cnV5IfGroupLinkTable.setStatus("current")
_CnV5IfGroupLinkEntry_Object = MibTableRow
cnV5IfGroupLinkEntry = _CnV5IfGroupLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 2, 1)
)
cnV5IfGroupLinkEntry.setIndexNames(
    (0, "CEM-V5", "cnV5IfGroupLinkIfGroupIndex"),
    (0, "CEM-V5", "cnV5IfGroupLinkIfIndex"),
)
if mibBuilder.loadTexts:
    cnV5IfGroupLinkEntry.setStatus("current")
_CnV5IfGroupLinkIfGroupIndex_Type = CnIfGroupIndexRange
_CnV5IfGroupLinkIfGroupIndex_Object = MibTableColumn
cnV5IfGroupLinkIfGroupIndex = _CnV5IfGroupLinkIfGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 2, 1, 1),
    _CnV5IfGroupLinkIfGroupIndex_Type()
)
cnV5IfGroupLinkIfGroupIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnV5IfGroupLinkIfGroupIndex.setStatus("current")
_CnV5IfGroupLinkIfIndex_Type = InterfaceIndex
_CnV5IfGroupLinkIfIndex_Object = MibTableColumn
cnV5IfGroupLinkIfIndex = _CnV5IfGroupLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 2, 1, 2),
    _CnV5IfGroupLinkIfIndex_Type()
)
cnV5IfGroupLinkIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnV5IfGroupLinkIfIndex.setStatus("current")


class _CnV5IfGroupLinkLogicalNumber_Type(Integer32):
    """Custom type cnV5IfGroupLinkLogicalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CnV5IfGroupLinkLogicalNumber_Type.__name__ = "Integer32"
_CnV5IfGroupLinkLogicalNumber_Object = MibTableColumn
cnV5IfGroupLinkLogicalNumber = _CnV5IfGroupLinkLogicalNumber_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 2, 1, 3),
    _CnV5IfGroupLinkLogicalNumber_Type()
)
cnV5IfGroupLinkLogicalNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnV5IfGroupLinkLogicalNumber.setStatus("current")
_CnV5IfGroupLinkType_Type = CnIfGroupLinkType
_CnV5IfGroupLinkType_Object = MibTableColumn
cnV5IfGroupLinkType = _CnV5IfGroupLinkType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 2, 1, 4),
    _CnV5IfGroupLinkType_Type()
)
cnV5IfGroupLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnV5IfGroupLinkType.setStatus("current")


class _CnV5IfGroupLinkStatus_Type(Integer32):
    """Custom type cnV5IfGroupLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("block", 0),
          ("unblock", 1),
          ("localUnblock", 2),
          ("remoteUnblock", 3))
    )


_CnV5IfGroupLinkStatus_Type.__name__ = "Integer32"
_CnV5IfGroupLinkStatus_Object = MibTableColumn
cnV5IfGroupLinkStatus = _CnV5IfGroupLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 2, 1, 5),
    _CnV5IfGroupLinkStatus_Type()
)
cnV5IfGroupLinkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnV5IfGroupLinkStatus.setStatus("current")


class _CnV5IfGroupLinkStatusData_Type(Integer32):
    """Custom type cnV5IfGroupLinkStatusData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deferred", 0),
          ("nonDeferred", 1))
    )


_CnV5IfGroupLinkStatusData_Type.__name__ = "Integer32"
_CnV5IfGroupLinkStatusData_Object = MibTableColumn
cnV5IfGroupLinkStatusData = _CnV5IfGroupLinkStatusData_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 2, 1, 6),
    _CnV5IfGroupLinkStatusData_Type()
)
cnV5IfGroupLinkStatusData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnV5IfGroupLinkStatusData.setStatus("current")
_CnV5IfGroupLinkConfigStatus_Type = Cn1000ConfigurationStatus
_CnV5IfGroupLinkConfigStatus_Object = MibTableColumn
cnV5IfGroupLinkConfigStatus = _CnV5IfGroupLinkConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 2, 1, 7),
    _CnV5IfGroupLinkConfigStatus_Type()
)
cnV5IfGroupLinkConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnV5IfGroupLinkConfigStatus.setStatus("current")
_CnV5IfGroupLinkRowStatus_Type = RowStatus
_CnV5IfGroupLinkRowStatus_Object = MibTableColumn
cnV5IfGroupLinkRowStatus = _CnV5IfGroupLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 2, 1, 8),
    _CnV5IfGroupLinkRowStatus_Type()
)
cnV5IfGroupLinkRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnV5IfGroupLinkRowStatus.setStatus("current")

# Managed Objects groups

cnV5ObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 12, 1, 9, 1, 3)
)
cnV5ObjectsGroup.setObjects(
      *(("CEM-V5", "cnV5IfGroupIndex"),
        ("CEM-V5", "cnV5IfGroupShelf"),
        ("CEM-V5", "cnV5IfGroupSlotGroup"),
        ("CEM-V5", "cnV5IfGroupConnectionIndex"),
        ("CEM-V5", "cnV5IfGroupDescription"),
        ("CEM-V5", "cnV5IfGroupLeType"),
        ("CEM-V5", "cnV5IfGroupConfigStatus"),
        ("CEM-V5", "cnV5IfGroupAdminState"),
        ("CEM-V5", "cnV5IfGroupOperState"),
        ("CEM-V5", "cnV5IfGroupProtocol"),
        ("CEM-V5", "cnV5IfGroupInterfaceId"),
        ("CEM-V5", "cnV5IfGroupProvisioningVariant"),
        ("CEM-V5", "cnV5IfGroupLinkNumberingType"),
        ("CEM-V5", "cnV5IfGroupProtGroup1LogChan"),
        ("CEM-V5", "cnV5IfGroupPstnLogChan"),
        ("CEM-V5", "cnV5IfGroupLapvPstnChanState"),
        ("CEM-V5", "cnV5IfGroupLapvCtrlChanState"),
        ("CEM-V5", "cnV5IfGroupLapvBccChanState"),
        ("CEM-V5", "cnV5IfGroupLapvLinkChanState"),
        ("CEM-V5", "cnV5IfGroupLapvPrimaryPgState"),
        ("CEM-V5", "cnV5IfGroupLapvSecondaryPgState"),
        ("CEM-V5", "cnV5IfGroupLapvActivePg1Chan"),
        ("CEM-V5", "cnV5IfGroupLapvActivePstnChan"),
        ("CEM-V5", "cnV5IfGroupRowStatus"),
        ("CEM-V5", "cnV5IfGroupLinkIfGroupIndex"),
        ("CEM-V5", "cnV5IfGroupLinkIfIndex"),
        ("CEM-V5", "cnV5IfGroupLinkLogicalNumber"),
        ("CEM-V5", "cnV5IfGroupLinkType"),
        ("CEM-V5", "cnV5IfGroupLinkStatus"),
        ("CEM-V5", "cnV5IfGroupLinkStatusData"),
        ("CEM-V5", "cnV5IfGroupLinkConfigStatus"),
        ("CEM-V5", "cnV5IfGroupLinkRowStatus"))
)
if mibBuilder.loadTexts:
    cnV5ObjectsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CEM-V5",
    **{"CnV5LapvChannelStatus": CnV5LapvChannelStatus,
       "cnV5": cnV5,
       "cnV5Module": cnV5Module,
       "cnV5IfGroupConfigTable": cnV5IfGroupConfigTable,
       "cnV5IfGroupConfigEntry": cnV5IfGroupConfigEntry,
       "cnV5IfGroupIndex": cnV5IfGroupIndex,
       "cnV5IfGroupShelf": cnV5IfGroupShelf,
       "cnV5IfGroupSlotGroup": cnV5IfGroupSlotGroup,
       "cnV5IfGroupConnectionIndex": cnV5IfGroupConnectionIndex,
       "cnV5IfGroupDescription": cnV5IfGroupDescription,
       "cnV5IfGroupLeType": cnV5IfGroupLeType,
       "cnV5IfGroupConfigStatus": cnV5IfGroupConfigStatus,
       "cnV5IfGroupAdminState": cnV5IfGroupAdminState,
       "cnV5IfGroupOperState": cnV5IfGroupOperState,
       "cnV5IfGroupProtocol": cnV5IfGroupProtocol,
       "cnV5IfGroupInterfaceId": cnV5IfGroupInterfaceId,
       "cnV5IfGroupProvisioningVariant": cnV5IfGroupProvisioningVariant,
       "cnV5IfGroupLinkNumberingType": cnV5IfGroupLinkNumberingType,
       "cnV5IfGroupProtGroup1LogChan": cnV5IfGroupProtGroup1LogChan,
       "cnV5IfGroupPstnLogChan": cnV5IfGroupPstnLogChan,
       "cnV5IfGroupLapvPstnChanState": cnV5IfGroupLapvPstnChanState,
       "cnV5IfGroupLapvCtrlChanState": cnV5IfGroupLapvCtrlChanState,
       "cnV5IfGroupLapvBccChanState": cnV5IfGroupLapvBccChanState,
       "cnV5IfGroupLapvLinkChanState": cnV5IfGroupLapvLinkChanState,
       "cnV5IfGroupLapvPrimaryPgState": cnV5IfGroupLapvPrimaryPgState,
       "cnV5IfGroupLapvSecondaryPgState": cnV5IfGroupLapvSecondaryPgState,
       "cnV5IfGroupLapvActivePg1Chan": cnV5IfGroupLapvActivePg1Chan,
       "cnV5IfGroupLapvActivePstnChan": cnV5IfGroupLapvActivePstnChan,
       "cnV5IfGroupRowStatus": cnV5IfGroupRowStatus,
       "cnV5IfGroupPstnPrimaryLogLink": cnV5IfGroupPstnPrimaryLogLink,
       "cnV5IfGroupPstnPrimaryTimeSlot": cnV5IfGroupPstnPrimaryTimeSlot,
       "cnV5IfGroupPstnSecondaryLogLink": cnV5IfGroupPstnSecondaryLogLink,
       "cnV5IfGroupPstnSecondaryTimeSlot": cnV5IfGroupPstnSecondaryTimeSlot,
       "cnV5IfGroupLinkTable": cnV5IfGroupLinkTable,
       "cnV5IfGroupLinkEntry": cnV5IfGroupLinkEntry,
       "cnV5IfGroupLinkIfGroupIndex": cnV5IfGroupLinkIfGroupIndex,
       "cnV5IfGroupLinkIfIndex": cnV5IfGroupLinkIfIndex,
       "cnV5IfGroupLinkLogicalNumber": cnV5IfGroupLinkLogicalNumber,
       "cnV5IfGroupLinkType": cnV5IfGroupLinkType,
       "cnV5IfGroupLinkStatus": cnV5IfGroupLinkStatus,
       "cnV5IfGroupLinkStatusData": cnV5IfGroupLinkStatusData,
       "cnV5IfGroupLinkConfigStatus": cnV5IfGroupLinkConfigStatus,
       "cnV5IfGroupLinkRowStatus": cnV5IfGroupLinkRowStatus,
       "cnV5ObjectsGroup": cnV5ObjectsGroup}
)
