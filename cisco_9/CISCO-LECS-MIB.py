# SNMP MIB module (CISCO-LECS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-LECS-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:47:33 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(AtmLaneAddress,
 VciInteger,
 VpiInteger) = mibBuilder.importSymbols(
    "LAN-EMULATION-CLIENT-MIB",
    "AtmLaneAddress",
    "VciInteger",
    "VpiInteger")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoLecsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 38)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLecsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLecsMIBObjects = _CiscoLecsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1)
)
_Lecs_ObjectIdentity = ObjectIdentity
lecs = _Lecs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1)
)
_LecsTable_Object = MibTable
lecsTable = _LecsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lecsTable.setStatus("current")
_LecsEntry_Object = MibTableRow
lecsEntry = _LecsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 1, 1)
)
lecsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lecsEntry.setStatus("current")


class _LecsConfigTableName_Type(DisplayString):
    """Custom type lecsConfigTableName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LecsConfigTableName_Type.__name__ = "DisplayString"
_LecsConfigTableName_Object = MibTableColumn
lecsConfigTableName = _LecsConfigTableName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 1, 1, 1),
    _LecsConfigTableName_Type()
)
lecsConfigTableName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsConfigTableName.setStatus("current")
_LecsUpTime_Type = TimeStamp
_LecsUpTime_Object = MibTableColumn
lecsUpTime = _LecsUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 1, 1, 2),
    _LecsUpTime_Type()
)
lecsUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsUpTime.setStatus("current")
_LecsInConfigReqs_Type = Counter32
_LecsInConfigReqs_Object = MibTableColumn
lecsInConfigReqs = _LecsInConfigReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 1, 1, 3),
    _LecsInConfigReqs_Type()
)
lecsInConfigReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsInConfigReqs.setStatus("current")
_LecsInConfigErrors_Type = Counter32
_LecsInConfigErrors_Object = MibTableColumn
lecsInConfigErrors = _LecsInConfigErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 1, 1, 4),
    _LecsInConfigErrors_Type()
)
lecsInConfigErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsInConfigErrors.setStatus("current")
_LecsOutConfigFails_Type = Counter32
_LecsOutConfigFails_Object = MibTableColumn
lecsOutConfigFails = _LecsOutConfigFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 1, 1, 5),
    _LecsOutConfigFails_Type()
)
lecsOutConfigFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsOutConfigFails.setStatus("current")
_LecsLastFailCause_Type = Integer32
_LecsLastFailCause_Object = MibTableColumn
lecsLastFailCause = _LecsLastFailCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 1, 1, 6),
    _LecsLastFailCause_Type()
)
lecsLastFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsLastFailCause.setStatus("current")
_LecsLastFailLec_Type = AtmLaneAddress
_LecsLastFailLec_Object = MibTableColumn
lecsLastFailLec = _LecsLastFailLec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 1, 1, 7),
    _LecsLastFailLec_Type()
)
lecsLastFailLec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsLastFailLec.setStatus("current")


class _LecsOperStatus_Type(Integer32):
    """Custom type lecsOperStatus based on Integer32"""
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


_LecsOperStatus_Type.__name__ = "Integer32"
_LecsOperStatus_Object = MibTableColumn
lecsOperStatus = _LecsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 1, 1, 8),
    _LecsOperStatus_Type()
)
lecsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsOperStatus.setStatus("current")


class _LecsAdminStatus_Type(Integer32):
    """Custom type lecsAdminStatus based on Integer32"""
    defaultValue = 1

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


_LecsAdminStatus_Type.__name__ = "Integer32"
_LecsAdminStatus_Object = MibTableColumn
lecsAdminStatus = _LecsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 1, 1, 9),
    _LecsAdminStatus_Type()
)
lecsAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsAdminStatus.setStatus("current")
_LecsStatus_Type = RowStatus
_LecsStatus_Object = MibTableColumn
lecsStatus = _LecsStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 1, 1, 10),
    _LecsStatus_Type()
)
lecsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsStatus.setStatus("current")
_LecsMasterState_Type = TruthValue
_LecsMasterState_Object = MibTableColumn
lecsMasterState = _LecsMasterState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 1, 1, 11),
    _LecsMasterState_Type()
)
lecsMasterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsMasterState.setStatus("current")
_LecsAtmAddrTable_Object = MibTable
lecsAtmAddrTable = _LecsAtmAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 2)
)
if mibBuilder.loadTexts:
    lecsAtmAddrTable.setStatus("current")
_LecsAtmAddrEntry_Object = MibTableRow
lecsAtmAddrEntry = _LecsAtmAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 2, 1)
)
lecsAtmAddrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-LECS-MIB", "lecsAtmAddrIndex"),
)
if mibBuilder.loadTexts:
    lecsAtmAddrEntry.setStatus("current")


class _LecsAtmAddrIndex_Type(Integer32):
    """Custom type lecsAtmAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LecsAtmAddrIndex_Type.__name__ = "Integer32"
_LecsAtmAddrIndex_Object = MibTableColumn
lecsAtmAddrIndex = _LecsAtmAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 2, 1, 1),
    _LecsAtmAddrIndex_Type()
)
lecsAtmAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecsAtmAddrIndex.setStatus("current")
_LecsAtmAddrSpec_Type = AtmLaneAddress
_LecsAtmAddrSpec_Object = MibTableColumn
lecsAtmAddrSpec = _LecsAtmAddrSpec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 2, 1, 2),
    _LecsAtmAddrSpec_Type()
)
lecsAtmAddrSpec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsAtmAddrSpec.setStatus("current")


class _LecsAtmAddrMask_Type(OctetString):
    """Custom type lecsAtmAddrMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(20, 20),
    )


_LecsAtmAddrMask_Type.__name__ = "OctetString"
_LecsAtmAddrMask_Object = MibTableColumn
lecsAtmAddrMask = _LecsAtmAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 2, 1, 3),
    _LecsAtmAddrMask_Type()
)
lecsAtmAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsAtmAddrMask.setStatus("current")
_LecsAtmAddrActual_Type = AtmLaneAddress
_LecsAtmAddrActual_Object = MibTableColumn
lecsAtmAddrActual = _LecsAtmAddrActual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 2, 1, 4),
    _LecsAtmAddrActual_Type()
)
lecsAtmAddrActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsAtmAddrActual.setStatus("current")


class _LecsAtmAddrState_Type(Integer32):
    """Custom type lecsAtmAddrState based on Integer32"""
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
        *(("actualValueInvalid", 1),
          ("actualValueValid", 2),
          ("registeredWithSignalling", 3),
          ("regSigAndValid", 4),
          ("registeredWithIlmi", 5),
          ("regIlmiAndValid", 6),
          ("regSigandIlmi", 7),
          ("regSigIlmiAndValid", 8))
    )


_LecsAtmAddrState_Type.__name__ = "Integer32"
_LecsAtmAddrState_Object = MibTableColumn
lecsAtmAddrState = _LecsAtmAddrState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 2, 1, 5),
    _LecsAtmAddrState_Type()
)
lecsAtmAddrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsAtmAddrState.setStatus("current")
_LecsAtmAddrStatus_Type = RowStatus
_LecsAtmAddrStatus_Object = MibTableColumn
lecsAtmAddrStatus = _LecsAtmAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 2, 1, 6),
    _LecsAtmAddrStatus_Type()
)
lecsAtmAddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsAtmAddrStatus.setStatus("current")
_LecsConfigDirectConnTable_Object = MibTable
lecsConfigDirectConnTable = _LecsConfigDirectConnTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 3)
)
if mibBuilder.loadTexts:
    lecsConfigDirectConnTable.setStatus("current")
_LecsConfigDirectConnEntry_Object = MibTableRow
lecsConfigDirectConnEntry = _LecsConfigDirectConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 3, 1)
)
lecsConfigDirectConnEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-LECS-MIB", "lecsConfigDirectConnVpi"),
    (0, "CISCO-LECS-MIB", "lecsConfigDirectConnVci"),
)
if mibBuilder.loadTexts:
    lecsConfigDirectConnEntry.setStatus("current")
_LecsConfigDirectConnVpi_Type = VpiInteger
_LecsConfigDirectConnVpi_Object = MibTableColumn
lecsConfigDirectConnVpi = _LecsConfigDirectConnVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 3, 1, 1),
    _LecsConfigDirectConnVpi_Type()
)
lecsConfigDirectConnVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecsConfigDirectConnVpi.setStatus("current")
_LecsConfigDirectConnVci_Type = VciInteger
_LecsConfigDirectConnVci_Object = MibTableColumn
lecsConfigDirectConnVci = _LecsConfigDirectConnVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 3, 1, 2),
    _LecsConfigDirectConnVci_Type()
)
lecsConfigDirectConnVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecsConfigDirectConnVci.setStatus("current")


class _LecsConfigDirectConnVCType_Type(Integer32):
    """Custom type lecsConfigDirectConnVCType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 1),
          ("svc", 2))
    )


_LecsConfigDirectConnVCType_Type.__name__ = "Integer32"
_LecsConfigDirectConnVCType_Object = MibTableColumn
lecsConfigDirectConnVCType = _LecsConfigDirectConnVCType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 3, 1, 3),
    _LecsConfigDirectConnVCType_Type()
)
lecsConfigDirectConnVCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsConfigDirectConnVCType.setStatus("current")
_LecsConfigDirectConnSrc_Type = AtmLaneAddress
_LecsConfigDirectConnSrc_Object = MibTableColumn
lecsConfigDirectConnSrc = _LecsConfigDirectConnSrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 3, 1, 4),
    _LecsConfigDirectConnSrc_Type()
)
lecsConfigDirectConnSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsConfigDirectConnSrc.setStatus("current")
_LecsConfigDirectConnDst_Type = AtmLaneAddress
_LecsConfigDirectConnDst_Object = MibTableColumn
lecsConfigDirectConnDst = _LecsConfigDirectConnDst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 3, 1, 5),
    _LecsConfigDirectConnDst_Type()
)
lecsConfigDirectConnDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsConfigDirectConnDst.setStatus("current")


class _LecsConfigDirectDstType_Type(Integer32):
    """Custom type lecsConfigDirectDstType based on Integer32"""
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
        *(("laneClient", 1),
          ("laneServer", 2),
          ("laneConfig", 3),
          ("unknown", 4))
    )


_LecsConfigDirectDstType_Type.__name__ = "Integer32"
_LecsConfigDirectDstType_Object = MibTableColumn
lecsConfigDirectDstType = _LecsConfigDirectDstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 3, 1, 6),
    _LecsConfigDirectDstType_Type()
)
lecsConfigDirectDstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsConfigDirectDstType.setStatus("current")
_Config_ObjectIdentity = ObjectIdentity
config = _Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2)
)
_LecsConfigTblTable_Object = MibTable
lecsConfigTblTable = _LecsConfigTblTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 1)
)
if mibBuilder.loadTexts:
    lecsConfigTblTable.setStatus("current")
_LecsConfigTblEntry_Object = MibTableRow
lecsConfigTblEntry = _LecsConfigTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 1, 1)
)
lecsConfigTblEntry.setIndexNames(
    (1, "CISCO-LECS-MIB", "lecsConfigTblName"),
)
if mibBuilder.loadTexts:
    lecsConfigTblEntry.setStatus("current")


class _LecsConfigTblName_Type(DisplayString):
    """Custom type lecsConfigTblName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LecsConfigTblName_Type.__name__ = "DisplayString"
_LecsConfigTblName_Object = MibTableColumn
lecsConfigTblName = _LecsConfigTblName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 1, 1, 1),
    _LecsConfigTblName_Type()
)
lecsConfigTblName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecsConfigTblName.setStatus("current")


class _LecsConfigTblDefaultElanName_Type(DisplayString):
    """Custom type lecsConfigTblDefaultElanName based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LecsConfigTblDefaultElanName_Type.__name__ = "DisplayString"
_LecsConfigTblDefaultElanName_Object = MibTableColumn
lecsConfigTblDefaultElanName = _LecsConfigTblDefaultElanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 1, 1, 2),
    _LecsConfigTblDefaultElanName_Type()
)
lecsConfigTblDefaultElanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsConfigTblDefaultElanName.setStatus("current")
_LecsConfigTblStatus_Type = RowStatus
_LecsConfigTblStatus_Object = MibTableColumn
lecsConfigTblStatus = _LecsConfigTblStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 1, 1, 3),
    _LecsConfigTblStatus_Type()
)
lecsConfigTblStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsConfigTblStatus.setStatus("current")
_LecsElanConfigTable_Object = MibTable
lecsElanConfigTable = _LecsElanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 2)
)
if mibBuilder.loadTexts:
    lecsElanConfigTable.setStatus("current")
_LecsElanConfigEntry_Object = MibTableRow
lecsElanConfigEntry = _LecsElanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 2, 1)
)
lecsElanConfigEntry.setIndexNames(
    (0, "CISCO-LECS-MIB", "lecsConfigTblName"),
    (1, "CISCO-LECS-MIB", "lecsElanConfigName"),
)
if mibBuilder.loadTexts:
    lecsElanConfigEntry.setStatus("current")


class _LecsElanConfigName_Type(DisplayString):
    """Custom type lecsElanConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LecsElanConfigName_Type.__name__ = "DisplayString"
_LecsElanConfigName_Object = MibTableColumn
lecsElanConfigName = _LecsElanConfigName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 2, 1, 1),
    _LecsElanConfigName_Type()
)
lecsElanConfigName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecsElanConfigName.setStatus("current")
_LecsElanLesAtmAddr_Type = AtmLaneAddress
_LecsElanLesAtmAddr_Object = MibTableColumn
lecsElanLesAtmAddr = _LecsElanLesAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 2, 1, 2),
    _LecsElanLesAtmAddr_Type()
)
lecsElanLesAtmAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsElanLesAtmAddr.setStatus("current")


class _LecsElanAccess_Type(Integer32):
    """Custom type lecsElanAccess based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("closed", 2))
    )


_LecsElanAccess_Type.__name__ = "Integer32"
_LecsElanAccess_Object = MibTableColumn
lecsElanAccess = _LecsElanAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 2, 1, 3),
    _LecsElanAccess_Type()
)
lecsElanAccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsElanAccess.setStatus("current")
_LecsElanConfigStatus_Type = RowStatus
_LecsElanConfigStatus_Object = MibTableColumn
lecsElanConfigStatus = _LecsElanConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 2, 1, 4),
    _LecsElanConfigStatus_Type()
)
lecsElanConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsElanConfigStatus.setStatus("current")


class _LecsElanSegmentId_Type(Integer32):
    """Custom type lecsElanSegmentId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_LecsElanSegmentId_Type.__name__ = "Integer32"
_LecsElanSegmentId_Object = MibTableColumn
lecsElanSegmentId = _LecsElanSegmentId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 2, 1, 5),
    _LecsElanSegmentId_Type()
)
lecsElanSegmentId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsElanSegmentId.setStatus("current")
_LecsMacConfigTable_Object = MibTable
lecsMacConfigTable = _LecsMacConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 3)
)
if mibBuilder.loadTexts:
    lecsMacConfigTable.setStatus("current")
_LecsMacConfigEntry_Object = MibTableRow
lecsMacConfigEntry = _LecsMacConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 3, 1)
)
lecsMacConfigEntry.setIndexNames(
    (0, "CISCO-LECS-MIB", "lecsConfigTblName"),
    (0, "CISCO-LECS-MIB", "lecsMacConfigAddress"),
)
if mibBuilder.loadTexts:
    lecsMacConfigEntry.setStatus("current")
_LecsMacConfigAddress_Type = MacAddress
_LecsMacConfigAddress_Object = MibTableColumn
lecsMacConfigAddress = _LecsMacConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 3, 1, 1),
    _LecsMacConfigAddress_Type()
)
lecsMacConfigAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecsMacConfigAddress.setStatus("current")


class _LecsMacConfigElanName_Type(DisplayString):
    """Custom type lecsMacConfigElanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LecsMacConfigElanName_Type.__name__ = "DisplayString"
_LecsMacConfigElanName_Object = MibTableColumn
lecsMacConfigElanName = _LecsMacConfigElanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 3, 1, 2),
    _LecsMacConfigElanName_Type()
)
lecsMacConfigElanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsMacConfigElanName.setStatus("current")
_LecsMacConfigLastUsed_Type = TimeStamp
_LecsMacConfigLastUsed_Object = MibTableColumn
lecsMacConfigLastUsed = _LecsMacConfigLastUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 3, 1, 3),
    _LecsMacConfigLastUsed_Type()
)
lecsMacConfigLastUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsMacConfigLastUsed.setStatus("current")
_LecsMacConfigStatus_Type = RowStatus
_LecsMacConfigStatus_Object = MibTableColumn
lecsMacConfigStatus = _LecsMacConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 3, 1, 4),
    _LecsMacConfigStatus_Type()
)
lecsMacConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsMacConfigStatus.setStatus("current")
_LecsAtmAddrConfigTable_Object = MibTable
lecsAtmAddrConfigTable = _LecsAtmAddrConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 4)
)
if mibBuilder.loadTexts:
    lecsAtmAddrConfigTable.setStatus("current")
_LecsAtmAddrConfigEntry_Object = MibTableRow
lecsAtmAddrConfigEntry = _LecsAtmAddrConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 4, 1)
)
lecsAtmAddrConfigEntry.setIndexNames(
    (0, "CISCO-LECS-MIB", "lecsConfigTblName"),
    (0, "CISCO-LECS-MIB", "lecsAtmAddrConfigAddress"),
    (0, "CISCO-LECS-MIB", "lecsAtmAddrConfigMask"),
)
if mibBuilder.loadTexts:
    lecsAtmAddrConfigEntry.setStatus("current")


class _LecsAtmAddrConfigAddress_Type(OctetString):
    """Custom type lecsAtmAddrConfigAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixedLength = 20


_LecsAtmAddrConfigAddress_Type.__name__ = "OctetString"
_LecsAtmAddrConfigAddress_Object = MibTableColumn
lecsAtmAddrConfigAddress = _LecsAtmAddrConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 4, 1, 1),
    _LecsAtmAddrConfigAddress_Type()
)
lecsAtmAddrConfigAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecsAtmAddrConfigAddress.setStatus("current")


class _LecsAtmAddrConfigMask_Type(OctetString):
    """Custom type lecsAtmAddrConfigMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixedLength = 20


_LecsAtmAddrConfigMask_Type.__name__ = "OctetString"
_LecsAtmAddrConfigMask_Object = MibTableColumn
lecsAtmAddrConfigMask = _LecsAtmAddrConfigMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 4, 1, 2),
    _LecsAtmAddrConfigMask_Type()
)
lecsAtmAddrConfigMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecsAtmAddrConfigMask.setStatus("current")


class _LecsAtmAddrConfigElanName_Type(DisplayString):
    """Custom type lecsAtmAddrConfigElanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LecsAtmAddrConfigElanName_Type.__name__ = "DisplayString"
_LecsAtmAddrConfigElanName_Object = MibTableColumn
lecsAtmAddrConfigElanName = _LecsAtmAddrConfigElanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 4, 1, 3),
    _LecsAtmAddrConfigElanName_Type()
)
lecsAtmAddrConfigElanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsAtmAddrConfigElanName.setStatus("current")
_LecsAtmAddrLastUsed_Type = TimeStamp
_LecsAtmAddrLastUsed_Object = MibTableColumn
lecsAtmAddrLastUsed = _LecsAtmAddrLastUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 4, 1, 4),
    _LecsAtmAddrLastUsed_Type()
)
lecsAtmAddrLastUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsAtmAddrLastUsed.setStatus("current")
_LecsAtmAddrConfigStatus_Type = RowStatus
_LecsAtmAddrConfigStatus_Object = MibTableColumn
lecsAtmAddrConfigStatus = _LecsAtmAddrConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 4, 1, 5),
    _LecsAtmAddrConfigStatus_Type()
)
lecsAtmAddrConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsAtmAddrConfigStatus.setStatus("current")
_LecsLesConfigTable_Object = MibTable
lecsLesConfigTable = _LecsLesConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 5)
)
if mibBuilder.loadTexts:
    lecsLesConfigTable.setStatus("current")
_LecsLesConfigEntry_Object = MibTableRow
lecsLesConfigEntry = _LecsLesConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 5, 1)
)
lecsLesConfigEntry.setIndexNames(
    (0, "CISCO-LECS-MIB", "lecsConfigTblName"),
    (0, "CISCO-LECS-MIB", "lecsElanConfigName"),
    (0, "CISCO-LECS-MIB", "lecsLesAtmAddr"),
)
if mibBuilder.loadTexts:
    lecsLesConfigEntry.setStatus("current")


class _LecsLesAtmAddr_Type(OctetString):
    """Custom type lecsLesAtmAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixedLength = 20


_LecsLesAtmAddr_Type.__name__ = "OctetString"
_LecsLesAtmAddr_Object = MibTableColumn
lecsLesAtmAddr = _LecsLesAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 5, 1, 1),
    _LecsLesAtmAddr_Type()
)
lecsLesAtmAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecsLesAtmAddr.setStatus("current")


class _LecsLesPriority_Type(Integer32):
    """Custom type lecsLesPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_LecsLesPriority_Type.__name__ = "Integer32"
_LecsLesPriority_Object = MibTableColumn
lecsLesPriority = _LecsLesPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 5, 1, 2),
    _LecsLesPriority_Type()
)
lecsLesPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsLesPriority.setStatus("current")


class _LecsLesConnState_Type(Integer32):
    """Custom type lecsLesConnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("notConnected", 3))
    )


_LecsLesConnState_Type.__name__ = "Integer32"
_LecsLesConnState_Object = MibTableColumn
lecsLesConnState = _LecsLesConnState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 5, 1, 3),
    _LecsLesConnState_Type()
)
lecsLesConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsLesConnState.setStatus("current")
_LecsLesConfigStatus_Type = RowStatus
_LecsLesConfigStatus_Object = MibTableColumn
lecsLesConfigStatus = _LecsLesConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 5, 1, 4),
    _LecsLesConfigStatus_Type()
)
lecsLesConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsLesConfigStatus.setStatus("current")
_LecsRDConfigTable_Object = MibTable
lecsRDConfigTable = _LecsRDConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 6)
)
if mibBuilder.loadTexts:
    lecsRDConfigTable.setStatus("current")
_LecsRDConfigEntry_Object = MibTableRow
lecsRDConfigEntry = _LecsRDConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 6, 1)
)
lecsRDConfigEntry.setIndexNames(
    (0, "CISCO-LECS-MIB", "lecsConfigTblName"),
    (0, "CISCO-LECS-MIB", "lecsRDConfigSegmentId"),
    (0, "CISCO-LECS-MIB", "lecsRDConfigBridgeNum"),
)
if mibBuilder.loadTexts:
    lecsRDConfigEntry.setStatus("current")


class _LecsRDConfigSegmentId_Type(Integer32):
    """Custom type lecsRDConfigSegmentId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_LecsRDConfigSegmentId_Type.__name__ = "Integer32"
_LecsRDConfigSegmentId_Object = MibTableColumn
lecsRDConfigSegmentId = _LecsRDConfigSegmentId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 6, 1, 1),
    _LecsRDConfigSegmentId_Type()
)
lecsRDConfigSegmentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecsRDConfigSegmentId.setStatus("current")


class _LecsRDConfigBridgeNum_Type(Integer32):
    """Custom type lecsRDConfigBridgeNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_LecsRDConfigBridgeNum_Type.__name__ = "Integer32"
_LecsRDConfigBridgeNum_Object = MibTableColumn
lecsRDConfigBridgeNum = _LecsRDConfigBridgeNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 6, 1, 2),
    _LecsRDConfigBridgeNum_Type()
)
lecsRDConfigBridgeNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecsRDConfigBridgeNum.setStatus("current")


class _LecsRDConfigElanName_Type(DisplayString):
    """Custom type lecsRDConfigElanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LecsRDConfigElanName_Type.__name__ = "DisplayString"
_LecsRDConfigElanName_Object = MibTableColumn
lecsRDConfigElanName = _LecsRDConfigElanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 6, 1, 3),
    _LecsRDConfigElanName_Type()
)
lecsRDConfigElanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsRDConfigElanName.setStatus("current")
_LecsRDConfigLastUsed_Type = TimeStamp
_LecsRDConfigLastUsed_Object = MibTableColumn
lecsRDConfigLastUsed = _LecsRDConfigLastUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 6, 1, 4),
    _LecsRDConfigLastUsed_Type()
)
lecsRDConfigLastUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsRDConfigLastUsed.setStatus("current")
_LecsRDConfigStatus_Type = RowStatus
_LecsRDConfigStatus_Object = MibTableColumn
lecsRDConfigStatus = _LecsRDConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 6, 1, 5),
    _LecsRDConfigStatus_Type()
)
lecsRDConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecsRDConfigStatus.setStatus("current")
_LecsMIBConformance_ObjectIdentity = ObjectIdentity
lecsMIBConformance = _LecsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 2)
)
_LecsMIBCompliances_ObjectIdentity = ObjectIdentity
lecsMIBCompliances = _LecsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 2, 1)
)
_LecsMIBGroups_ObjectIdentity = ObjectIdentity
lecsMIBGroups = _LecsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 2, 2)
)

# Managed Objects groups

lecsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 2, 2, 1)
)
lecsMIBGroup.setObjects(
      *(("CISCO-LECS-MIB", "lecsConfigTableName"),
        ("CISCO-LECS-MIB", "lecsUpTime"),
        ("CISCO-LECS-MIB", "lecsInConfigReqs"),
        ("CISCO-LECS-MIB", "lecsInConfigErrors"),
        ("CISCO-LECS-MIB", "lecsOutConfigFails"),
        ("CISCO-LECS-MIB", "lecsLastFailCause"),
        ("CISCO-LECS-MIB", "lecsLastFailLec"),
        ("CISCO-LECS-MIB", "lecsOperStatus"),
        ("CISCO-LECS-MIB", "lecsAdminStatus"),
        ("CISCO-LECS-MIB", "lecsStatus"),
        ("CISCO-LECS-MIB", "lecsAtmAddrSpec"),
        ("CISCO-LECS-MIB", "lecsAtmAddrMask"),
        ("CISCO-LECS-MIB", "lecsAtmAddrActual"),
        ("CISCO-LECS-MIB", "lecsAtmAddrState"),
        ("CISCO-LECS-MIB", "lecsAtmAddrStatus"),
        ("CISCO-LECS-MIB", "lecsConfigDirectConnSrc"),
        ("CISCO-LECS-MIB", "lecsConfigDirectConnDst"),
        ("CISCO-LECS-MIB", "lecsConfigTblStatus"),
        ("CISCO-LECS-MIB", "lecsElanLesAtmAddr"),
        ("CISCO-LECS-MIB", "lecsElanConfigStatus"),
        ("CISCO-LECS-MIB", "lecsMacConfigElanName"),
        ("CISCO-LECS-MIB", "lecsMacConfigLastUsed"),
        ("CISCO-LECS-MIB", "lecsMacConfigStatus"),
        ("CISCO-LECS-MIB", "lecsAtmAddrConfigElanName"),
        ("CISCO-LECS-MIB", "lecsAtmAddrLastUsed"),
        ("CISCO-LECS-MIB", "lecsAtmAddrConfigStatus"),
        ("CISCO-LECS-MIB", "lecsConfigDirectConnVCType"),
        ("CISCO-LECS-MIB", "lecsConfigTblDefaultElanName"),
        ("CISCO-LECS-MIB", "lecsElanAccess"))
)
if mibBuilder.loadTexts:
    lecsMIBGroup.setStatus("current")

lecsTokenRingMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 2, 2, 2)
)
lecsTokenRingMIBGroup.setObjects(
      *(("CISCO-LECS-MIB", "lecsElanSegmentId"),
        ("CISCO-LECS-MIB", "lecsRDConfigElanName"),
        ("CISCO-LECS-MIB", "lecsRDConfigLastUsed"),
        ("CISCO-LECS-MIB", "lecsRDConfigStatus"))
)
if mibBuilder.loadTexts:
    lecsTokenRingMIBGroup.setStatus("current")

lecsRedundancyMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 2, 2, 3)
)
lecsRedundancyMIBGroup.setObjects(
      *(("CISCO-LECS-MIB", "lecsMasterState"),
        ("CISCO-LECS-MIB", "lecsConfigDirectDstType"),
        ("CISCO-LECS-MIB", "lecsLesPriority"),
        ("CISCO-LECS-MIB", "lecsLesConnState"),
        ("CISCO-LECS-MIB", "lecsLesConfigStatus"))
)
if mibBuilder.loadTexts:
    lecsRedundancyMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lecsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 2, 1, 1)
)
lecsMIBCompliance.setObjects(
    ("CISCO-LECS-MIB", "lecsMIBGroup")
)
if mibBuilder.loadTexts:
    lecsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LECS-MIB",
    **{"ciscoLecsMIB": ciscoLecsMIB,
       "ciscoLecsMIBObjects": ciscoLecsMIBObjects,
       "lecs": lecs,
       "lecsTable": lecsTable,
       "lecsEntry": lecsEntry,
       "lecsConfigTableName": lecsConfigTableName,
       "lecsUpTime": lecsUpTime,
       "lecsInConfigReqs": lecsInConfigReqs,
       "lecsInConfigErrors": lecsInConfigErrors,
       "lecsOutConfigFails": lecsOutConfigFails,
       "lecsLastFailCause": lecsLastFailCause,
       "lecsLastFailLec": lecsLastFailLec,
       "lecsOperStatus": lecsOperStatus,
       "lecsAdminStatus": lecsAdminStatus,
       "lecsStatus": lecsStatus,
       "lecsMasterState": lecsMasterState,
       "lecsAtmAddrTable": lecsAtmAddrTable,
       "lecsAtmAddrEntry": lecsAtmAddrEntry,
       "lecsAtmAddrIndex": lecsAtmAddrIndex,
       "lecsAtmAddrSpec": lecsAtmAddrSpec,
       "lecsAtmAddrMask": lecsAtmAddrMask,
       "lecsAtmAddrActual": lecsAtmAddrActual,
       "lecsAtmAddrState": lecsAtmAddrState,
       "lecsAtmAddrStatus": lecsAtmAddrStatus,
       "lecsConfigDirectConnTable": lecsConfigDirectConnTable,
       "lecsConfigDirectConnEntry": lecsConfigDirectConnEntry,
       "lecsConfigDirectConnVpi": lecsConfigDirectConnVpi,
       "lecsConfigDirectConnVci": lecsConfigDirectConnVci,
       "lecsConfigDirectConnVCType": lecsConfigDirectConnVCType,
       "lecsConfigDirectConnSrc": lecsConfigDirectConnSrc,
       "lecsConfigDirectConnDst": lecsConfigDirectConnDst,
       "lecsConfigDirectDstType": lecsConfigDirectDstType,
       "config": config,
       "lecsConfigTblTable": lecsConfigTblTable,
       "lecsConfigTblEntry": lecsConfigTblEntry,
       "lecsConfigTblName": lecsConfigTblName,
       "lecsConfigTblDefaultElanName": lecsConfigTblDefaultElanName,
       "lecsConfigTblStatus": lecsConfigTblStatus,
       "lecsElanConfigTable": lecsElanConfigTable,
       "lecsElanConfigEntry": lecsElanConfigEntry,
       "lecsElanConfigName": lecsElanConfigName,
       "lecsElanLesAtmAddr": lecsElanLesAtmAddr,
       "lecsElanAccess": lecsElanAccess,
       "lecsElanConfigStatus": lecsElanConfigStatus,
       "lecsElanSegmentId": lecsElanSegmentId,
       "lecsMacConfigTable": lecsMacConfigTable,
       "lecsMacConfigEntry": lecsMacConfigEntry,
       "lecsMacConfigAddress": lecsMacConfigAddress,
       "lecsMacConfigElanName": lecsMacConfigElanName,
       "lecsMacConfigLastUsed": lecsMacConfigLastUsed,
       "lecsMacConfigStatus": lecsMacConfigStatus,
       "lecsAtmAddrConfigTable": lecsAtmAddrConfigTable,
       "lecsAtmAddrConfigEntry": lecsAtmAddrConfigEntry,
       "lecsAtmAddrConfigAddress": lecsAtmAddrConfigAddress,
       "lecsAtmAddrConfigMask": lecsAtmAddrConfigMask,
       "lecsAtmAddrConfigElanName": lecsAtmAddrConfigElanName,
       "lecsAtmAddrLastUsed": lecsAtmAddrLastUsed,
       "lecsAtmAddrConfigStatus": lecsAtmAddrConfigStatus,
       "lecsLesConfigTable": lecsLesConfigTable,
       "lecsLesConfigEntry": lecsLesConfigEntry,
       "lecsLesAtmAddr": lecsLesAtmAddr,
       "lecsLesPriority": lecsLesPriority,
       "lecsLesConnState": lecsLesConnState,
       "lecsLesConfigStatus": lecsLesConfigStatus,
       "lecsRDConfigTable": lecsRDConfigTable,
       "lecsRDConfigEntry": lecsRDConfigEntry,
       "lecsRDConfigSegmentId": lecsRDConfigSegmentId,
       "lecsRDConfigBridgeNum": lecsRDConfigBridgeNum,
       "lecsRDConfigElanName": lecsRDConfigElanName,
       "lecsRDConfigLastUsed": lecsRDConfigLastUsed,
       "lecsRDConfigStatus": lecsRDConfigStatus,
       "lecsMIBConformance": lecsMIBConformance,
       "lecsMIBCompliances": lecsMIBCompliances,
       "lecsMIBCompliance": lecsMIBCompliance,
       "lecsMIBGroups": lecsMIBGroups,
       "lecsMIBGroup": lecsMIBGroup,
       "lecsTokenRingMIBGroup": lecsTokenRingMIBGroup,
       "lecsRedundancyMIBGroup": lecsRedundancyMIBGroup}
)
