# SNMP MIB module (RUIJIE-LLDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-LLDP-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:12 2025
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "IfIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ruijieLldpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32)
)
if mibBuilder.loadTexts:
    ruijieLldpMIB.setRevisions(
        ("2003-04-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LldpMibObjects_ObjectIdentity = ObjectIdentity
lldpMibObjects = _LldpMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32, 1)
)
_LldpConfig_ObjectIdentity = ObjectIdentity
lldpConfig = _LldpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32, 1, 1)
)


class _LldpAdminStatus_Type(EnabledStatus):
    """Custom type lldpAdminStatus based on EnabledStatus"""
    defaultValue = 1


_LldpAdminStatus_Type.__name__ = "EnabledStatus"
_LldpAdminStatus_Object = MibScalar
lldpAdminStatus = _LldpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32, 1, 1, 1),
    _LldpAdminStatus_Type()
)
lldpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpAdminStatus.setStatus("current")
_LldpOperStatus_Type = EnabledStatus
_LldpOperStatus_Object = MibScalar
lldpOperStatus = _LldpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32, 1, 1, 2),
    _LldpOperStatus_Type()
)
lldpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpOperStatus.setStatus("current")


class _LldpMessageTxInterval_Type(Integer32):
    """Custom type lldpMessageTxInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 299),
    )


_LldpMessageTxInterval_Type.__name__ = "Integer32"
_LldpMessageTxInterval_Object = MibScalar
lldpMessageTxInterval = _LldpMessageTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32, 1, 1, 3),
    _LldpMessageTxInterval_Type()
)
lldpMessageTxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpMessageTxInterval.setStatus("current")
if mibBuilder.loadTexts:
    lldpMessageTxInterval.setUnits("seconds")


class _LldpMessageTxHoldTime_Type(Integer32):
    """Custom type lldpMessageTxHoldTime based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_LldpMessageTxHoldTime_Type.__name__ = "Integer32"
_LldpMessageTxHoldTime_Object = MibScalar
lldpMessageTxHoldTime = _LldpMessageTxHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32, 1, 1, 4),
    _LldpMessageTxHoldTime_Type()
)
lldpMessageTxHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpMessageTxHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    lldpMessageTxHoldTime.setUnits("seconds")
_LldpDeviceID_Type = MacAddress
_LldpDeviceID_Object = MibScalar
lldpDeviceID = _LldpDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32, 1, 1, 5),
    _LldpDeviceID_Type()
)
lldpDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpDeviceID.setStatus("current")
_LldpSuppressTable_Object = MibTable
lldpSuppressTable = _LldpSuppressTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32, 1, 1, 6)
)
if mibBuilder.loadTexts:
    lldpSuppressTable.setStatus("current")
_LldpSuppressEntry_Object = MibTableRow
lldpSuppressEntry = _LldpSuppressEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32, 1, 1, 6, 1)
)
lldpSuppressEntry.setIndexNames(
    (0, "RUIJIE-LLDP-MIB", "lldpSuppressPortIfIndex"),
)
if mibBuilder.loadTexts:
    lldpSuppressEntry.setStatus("current")
_LldpSuppressPortIfIndex_Type = IfIndex
_LldpSuppressPortIfIndex_Object = MibTableColumn
lldpSuppressPortIfIndex = _LldpSuppressPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32, 1, 1, 6, 1, 1),
    _LldpSuppressPortIfIndex_Type()
)
lldpSuppressPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpSuppressPortIfIndex.setStatus("current")


class _LldpSuppressPortStatus_Type(EnabledStatus):
    """Custom type lldpSuppressPortStatus based on EnabledStatus"""
    defaultValue = 1


_LldpSuppressPortStatus_Type.__name__ = "EnabledStatus"
_LldpSuppressPortStatus_Object = MibTableColumn
lldpSuppressPortStatus = _LldpSuppressPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32, 1, 1, 6, 1, 2),
    _LldpSuppressPortStatus_Type()
)
lldpSuppressPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpSuppressPortStatus.setStatus("current")
_LldpStats_ObjectIdentity = ObjectIdentity
lldpStats = _LldpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32, 1, 2)
)
_LldpStatsTable_Object = MibTable
lldpStatsTable = _LldpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32, 1, 2, 1)
)
if mibBuilder.loadTexts:
    lldpStatsTable.setStatus("current")
_LldpStatsEntry_Object = MibTableRow
lldpStatsEntry = _LldpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32, 1, 2, 1, 1)
)
lldpStatsEntry.setIndexNames(
    (0, "RUIJIE-LLDP-MIB", "lldpStatsPortIfIndex"),
)
if mibBuilder.loadTexts:
    lldpStatsEntry.setStatus("current")
_LldpStatsPortIfIndex_Type = IfIndex
_LldpStatsPortIfIndex_Object = MibTableColumn
lldpStatsPortIfIndex = _LldpStatsPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32, 1, 2, 1, 1, 1),
    _LldpStatsPortIfIndex_Type()
)
lldpStatsPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpStatsPortIfIndex.setStatus("current")
_LldpStatsInGoodPkts_Type = Counter32
_LldpStatsInGoodPkts_Object = MibTableColumn
lldpStatsInGoodPkts = _LldpStatsInGoodPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32, 1, 2, 1, 1, 2),
    _LldpStatsInGoodPkts_Type()
)
lldpStatsInGoodPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsInGoodPkts.setStatus("current")
_LldpStatsInErrors_Type = Counter32
_LldpStatsInErrors_Object = MibTableColumn
lldpStatsInErrors = _LldpStatsInErrors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32, 1, 2, 1, 1, 3),
    _LldpStatsInErrors_Type()
)
lldpStatsInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsInErrors.setStatus("current")
_LldpStatsOutPkts_Type = Counter32
_LldpStatsOutPkts_Object = MibTableColumn
lldpStatsOutPkts = _LldpStatsOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32, 1, 2, 1, 1, 4),
    _LldpStatsOutPkts_Type()
)
lldpStatsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsOutPkts.setStatus("current")
_LldpStatsClear_Type = Integer32
_LldpStatsClear_Object = MibTableColumn
lldpStatsClear = _LldpStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32, 1, 2, 1, 1, 5),
    _LldpStatsClear_Type()
)
lldpStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpStatsClear.setStatus("current")
_LldpRcvObjects_ObjectIdentity = ObjectIdentity
lldpRcvObjects = _LldpRcvObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32, 1, 3)
)
_LldpRcvTable_Object = MibTable
lldpRcvTable = _LldpRcvTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32, 1, 3, 1)
)
if mibBuilder.loadTexts:
    lldpRcvTable.setStatus("current")
_LldpRcvEntry_Object = MibTableRow
lldpRcvEntry = _LldpRcvEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32, 1, 3, 1, 1)
)
lldpRcvEntry.setIndexNames(
    (0, "RUIJIE-LLDP-MIB", "lldpRcvIfIndex"),
    (0, "RUIJIE-LLDP-MIB", "lldpRcvDeviceID"),
)
if mibBuilder.loadTexts:
    lldpRcvEntry.setStatus("current")
_LldpRcvIfIndex_Type = IfIndex
_LldpRcvIfIndex_Object = MibTableColumn
lldpRcvIfIndex = _LldpRcvIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32, 1, 3, 1, 1, 1),
    _LldpRcvIfIndex_Type()
)
lldpRcvIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpRcvIfIndex.setStatus("current")
_LldpRcvDeviceID_Type = MacAddress
_LldpRcvDeviceID_Object = MibTableColumn
lldpRcvDeviceID = _LldpRcvDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32, 1, 3, 1, 1, 2),
    _LldpRcvDeviceID_Type()
)
lldpRcvDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRcvDeviceID.setStatus("current")
_LldpRcvMgmtAddress_Type = MacAddress
_LldpRcvMgmtAddress_Object = MibTableColumn
lldpRcvMgmtAddress = _LldpRcvMgmtAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32, 1, 3, 1, 1, 3),
    _LldpRcvMgmtAddress_Type()
)
lldpRcvMgmtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRcvMgmtAddress.setStatus("current")
_LldpRcvPortIDSubtype_Type = Integer32
_LldpRcvPortIDSubtype_Object = MibTableColumn
lldpRcvPortIDSubtype = _LldpRcvPortIDSubtype_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32, 1, 3, 1, 1, 4),
    _LldpRcvPortIDSubtype_Type()
)
lldpRcvPortIDSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRcvPortIDSubtype.setStatus("current")


class _LldpRcvPortInfo_Type(DisplayString):
    """Custom type lldpRcvPortInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpRcvPortInfo_Type.__name__ = "DisplayString"
_LldpRcvPortInfo_Object = MibTableColumn
lldpRcvPortInfo = _LldpRcvPortInfo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32, 1, 3, 1, 1, 5),
    _LldpRcvPortInfo_Type()
)
lldpRcvPortInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRcvPortInfo.setStatus("current")


class _LldpRcvClusterMode_Type(Integer32):
    """Custom type lldpRcvClusterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("commandDevice", 1),
          ("memberDevice", 2),
          ("none", 3))
    )


_LldpRcvClusterMode_Type.__name__ = "Integer32"
_LldpRcvClusterMode_Object = MibTableColumn
lldpRcvClusterMode = _LldpRcvClusterMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32, 1, 3, 1, 1, 6),
    _LldpRcvClusterMode_Type()
)
lldpRcvClusterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRcvClusterMode.setStatus("current")
_LldpRcvClusterStatus_Type = EnabledStatus
_LldpRcvClusterStatus_Object = MibTableColumn
lldpRcvClusterStatus = _LldpRcvClusterStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32, 1, 3, 1, 1, 7),
    _LldpRcvClusterStatus_Type()
)
lldpRcvClusterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRcvClusterStatus.setStatus("current")


class _LldpRcvClusterName_Type(DisplayString):
    """Custom type lldpRcvClusterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LldpRcvClusterName_Type.__name__ = "DisplayString"
_LldpRcvClusterName_Object = MibTableColumn
lldpRcvClusterName = _LldpRcvClusterName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32, 1, 3, 1, 1, 8),
    _LldpRcvClusterName_Type()
)
lldpRcvClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRcvClusterName.setStatus("current")


class _LldpRcvHostName_Type(DisplayString):
    """Custom type lldpRcvHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_LldpRcvHostName_Type.__name__ = "DisplayString"
_LldpRcvHostName_Object = MibTableColumn
lldpRcvHostName = _LldpRcvHostName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32, 1, 3, 1, 1, 9),
    _LldpRcvHostName_Type()
)
lldpRcvHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRcvHostName.setStatus("current")
_LldpRcvCommandAddress_Type = MacAddress
_LldpRcvCommandAddress_Object = MibTableColumn
lldpRcvCommandAddress = _LldpRcvCommandAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32, 1, 3, 1, 1, 10),
    _LldpRcvCommandAddress_Type()
)
lldpRcvCommandAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRcvCommandAddress.setStatus("current")
_LldpRcvTableClear_Type = Integer32
_LldpRcvTableClear_Object = MibScalar
lldpRcvTableClear = _LldpRcvTableClear_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32, 1, 3, 2),
    _LldpRcvTableClear_Type()
)
lldpRcvTableClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpRcvTableClear.setStatus("current")
_LldpMIBConformance_ObjectIdentity = ObjectIdentity
lldpMIBConformance = _LldpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32, 2)
)
_LldpMIBCompliances_ObjectIdentity = ObjectIdentity
lldpMIBCompliances = _LldpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32, 2, 1)
)
_LldpMIBGroups_ObjectIdentity = ObjectIdentity
lldpMIBGroups = _LldpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32, 2, 2)
)

# Managed Objects groups

lldpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32, 2, 2, 1)
)
lldpConfigGroup.setObjects(
      *(("RUIJIE-LLDP-MIB", "lldpAdminStatus"),
        ("RUIJIE-LLDP-MIB", "lldpOperStatus"),
        ("RUIJIE-LLDP-MIB", "lldpMessageTxInterval"),
        ("RUIJIE-LLDP-MIB", "lldpMessageTxHoldTime"))
)
if mibBuilder.loadTexts:
    lldpConfigGroup.setStatus("current")

lldpStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32, 2, 2, 2)
)
lldpStatsGroup.setObjects(
      *(("RUIJIE-LLDP-MIB", "lldpStatsInGoodPkts"),
        ("RUIJIE-LLDP-MIB", "lldpStatsInErrors"),
        ("RUIJIE-LLDP-MIB", "lldpStatsOutPkts"))
)
if mibBuilder.loadTexts:
    lldpStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lldpCompliances = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 32, 2, 1, 1)
)
lldpCompliances.setObjects(
      *(("RUIJIE-LLDP-MIB", "lldpConfigGroup"),
        ("RUIJIE-LLDP-MIB", "lldpStatsGroup"))
)
if mibBuilder.loadTexts:
    lldpCompliances.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-LLDP-MIB",
    **{"ruijieLldpMIB": ruijieLldpMIB,
       "lldpMibObjects": lldpMibObjects,
       "lldpConfig": lldpConfig,
       "lldpAdminStatus": lldpAdminStatus,
       "lldpOperStatus": lldpOperStatus,
       "lldpMessageTxInterval": lldpMessageTxInterval,
       "lldpMessageTxHoldTime": lldpMessageTxHoldTime,
       "lldpDeviceID": lldpDeviceID,
       "lldpSuppressTable": lldpSuppressTable,
       "lldpSuppressEntry": lldpSuppressEntry,
       "lldpSuppressPortIfIndex": lldpSuppressPortIfIndex,
       "lldpSuppressPortStatus": lldpSuppressPortStatus,
       "lldpStats": lldpStats,
       "lldpStatsTable": lldpStatsTable,
       "lldpStatsEntry": lldpStatsEntry,
       "lldpStatsPortIfIndex": lldpStatsPortIfIndex,
       "lldpStatsInGoodPkts": lldpStatsInGoodPkts,
       "lldpStatsInErrors": lldpStatsInErrors,
       "lldpStatsOutPkts": lldpStatsOutPkts,
       "lldpStatsClear": lldpStatsClear,
       "lldpRcvObjects": lldpRcvObjects,
       "lldpRcvTable": lldpRcvTable,
       "lldpRcvEntry": lldpRcvEntry,
       "lldpRcvIfIndex": lldpRcvIfIndex,
       "lldpRcvDeviceID": lldpRcvDeviceID,
       "lldpRcvMgmtAddress": lldpRcvMgmtAddress,
       "lldpRcvPortIDSubtype": lldpRcvPortIDSubtype,
       "lldpRcvPortInfo": lldpRcvPortInfo,
       "lldpRcvClusterMode": lldpRcvClusterMode,
       "lldpRcvClusterStatus": lldpRcvClusterStatus,
       "lldpRcvClusterName": lldpRcvClusterName,
       "lldpRcvHostName": lldpRcvHostName,
       "lldpRcvCommandAddress": lldpRcvCommandAddress,
       "lldpRcvTableClear": lldpRcvTableClear,
       "lldpMIBConformance": lldpMIBConformance,
       "lldpMIBCompliances": lldpMIBCompliances,
       "lldpCompliances": lldpCompliances,
       "lldpMIBGroups": lldpMIBGroups,
       "lldpConfigGroup": lldpConfigGroup,
       "lldpStatsGroup": lldpStatsGroup}
)
