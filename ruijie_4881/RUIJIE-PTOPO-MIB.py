# SNMP MIB module (RUIJIE-PTOPO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-PTOPO-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:07 2025
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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ruijiePotopoMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 33)
)
if mibBuilder.loadTexts:
    ruijiePotopoMIB.setRevisions(
        ("2003-04-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PtopoMIBObjects_ObjectIdentity = ObjectIdentity
ptopoMIBObjects = _PtopoMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 33, 1)
)
_PtopoConnData_ObjectIdentity = ObjectIdentity
ptopoConnData = _PtopoConnData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 33, 1, 1)
)
_PtopoConnTable_Object = MibTable
ptopoConnTable = _PtopoConnTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 33, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ptopoConnTable.setStatus("current")
_PtopoConnEntry_Object = MibTableRow
ptopoConnEntry = _PtopoConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 33, 1, 1, 1, 1)
)
ptopoConnEntry.setIndexNames(
    (0, "RUIJIE-PTOPO-MIB", "ptopoConnIndex"),
)
if mibBuilder.loadTexts:
    ptopoConnEntry.setStatus("current")


class _PtopoConnIndex_Type(Integer32):
    """Custom type ptopoConnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PtopoConnIndex_Type.__name__ = "Integer32"
_PtopoConnIndex_Object = MibTableColumn
ptopoConnIndex = _PtopoConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 33, 1, 1, 1, 1, 1),
    _PtopoConnIndex_Type()
)
ptopoConnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptopoConnIndex.setStatus("current")
_PtopoConnLocalDevice_Type = MacAddress
_PtopoConnLocalDevice_Object = MibTableColumn
ptopoConnLocalDevice = _PtopoConnLocalDevice_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 33, 1, 1, 1, 1, 2),
    _PtopoConnLocalDevice_Type()
)
ptopoConnLocalDevice.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptopoConnLocalDevice.setStatus("current")


class _PtopoConnLocalPort_Type(DisplayString):
    """Custom type ptopoConnLocalPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PtopoConnLocalPort_Type.__name__ = "DisplayString"
_PtopoConnLocalPort_Object = MibTableColumn
ptopoConnLocalPort = _PtopoConnLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 33, 1, 1, 1, 1, 3),
    _PtopoConnLocalPort_Type()
)
ptopoConnLocalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptopoConnLocalPort.setStatus("current")
_PtopoConnRemoteDevice_Type = MacAddress
_PtopoConnRemoteDevice_Object = MibTableColumn
ptopoConnRemoteDevice = _PtopoConnRemoteDevice_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 33, 1, 1, 1, 1, 4),
    _PtopoConnRemoteDevice_Type()
)
ptopoConnRemoteDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptopoConnRemoteDevice.setStatus("current")


class _PtopoConnRemotePort_Type(DisplayString):
    """Custom type ptopoConnRemotePort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PtopoConnRemotePort_Type.__name__ = "DisplayString"
_PtopoConnRemotePort_Object = MibTableColumn
ptopoConnRemotePort = _PtopoConnRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 33, 1, 1, 1, 1, 5),
    _PtopoConnRemotePort_Type()
)
ptopoConnRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptopoConnRemotePort.setStatus("current")


class _PtopoConnIsUpStream_Type(Integer32):
    """Custom type ptopoConnIsUpStream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("upstream", 1),
          ("nonupstream", 2))
    )


_PtopoConnIsUpStream_Type.__name__ = "Integer32"
_PtopoConnIsUpStream_Object = MibTableColumn
ptopoConnIsUpStream = _PtopoConnIsUpStream_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 33, 1, 1, 1, 1, 6),
    _PtopoConnIsUpStream_Type()
)
ptopoConnIsUpStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptopoConnIsUpStream.setStatus("current")
_PtopoDevData_ObjectIdentity = ObjectIdentity
ptopoDevData = _PtopoDevData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 33, 1, 2)
)
_PtopoDevTable_Object = MibTable
ptopoDevTable = _PtopoDevTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 33, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ptopoDevTable.setStatus("current")
_PtopoDevEntry_Object = MibTableRow
ptopoDevEntry = _PtopoDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 33, 1, 2, 1, 1)
)
ptopoDevEntry.setIndexNames(
    (0, "RUIJIE-PTOPO-MIB", "ptopoDevID"),
)
if mibBuilder.loadTexts:
    ptopoDevEntry.setStatus("current")
_PtopoDevID_Type = MacAddress
_PtopoDevID_Object = MibTableColumn
ptopoDevID = _PtopoDevID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 33, 1, 2, 1, 1, 1),
    _PtopoDevID_Type()
)
ptopoDevID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptopoDevID.setStatus("current")


class _PtopoDevHostname_Type(DisplayString):
    """Custom type ptopoDevHostname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_PtopoDevHostname_Type.__name__ = "DisplayString"
_PtopoDevHostname_Object = MibTableColumn
ptopoDevHostname = _PtopoDevHostname_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 33, 1, 2, 1, 1, 2),
    _PtopoDevHostname_Type()
)
ptopoDevHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptopoDevHostname.setStatus("current")
_PtopoDevClusStatus_Type = EnabledStatus
_PtopoDevClusStatus_Object = MibTableColumn
ptopoDevClusStatus = _PtopoDevClusStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 33, 1, 2, 1, 1, 3),
    _PtopoDevClusStatus_Type()
)
ptopoDevClusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptopoDevClusStatus.setStatus("current")


class _PtopoDevClusMode_Type(Integer32):
    """Custom type ptopoDevClusMode based on Integer32"""
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


_PtopoDevClusMode_Type.__name__ = "Integer32"
_PtopoDevClusMode_Object = MibTableColumn
ptopoDevClusMode = _PtopoDevClusMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 33, 1, 2, 1, 1, 4),
    _PtopoDevClusMode_Type()
)
ptopoDevClusMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptopoDevClusMode.setStatus("current")


class _PtopoDevClusName_Type(DisplayString):
    """Custom type ptopoDevClusName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PtopoDevClusName_Type.__name__ = "DisplayString"
_PtopoDevClusName_Object = MibTableColumn
ptopoDevClusName = _PtopoDevClusName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 33, 1, 2, 1, 1, 5),
    _PtopoDevClusName_Type()
)
ptopoDevClusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptopoDevClusName.setStatus("current")
_PtopoDevCSMac_Type = MacAddress
_PtopoDevCSMac_Object = MibTableColumn
ptopoDevCSMac = _PtopoDevCSMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 33, 1, 2, 1, 1, 6),
    _PtopoDevCSMac_Type()
)
ptopoDevCSMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptopoDevCSMac.setStatus("current")


class _PtopoDevHopsToCs_Type(Integer32):
    """Custom type ptopoDevHopsToCs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_PtopoDevHopsToCs_Type.__name__ = "Integer32"
_PtopoDevHopsToCs_Object = MibTableColumn
ptopoDevHopsToCs = _PtopoDevHopsToCs_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 33, 1, 2, 1, 1, 7),
    _PtopoDevHopsToCs_Type()
)
ptopoDevHopsToCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptopoDevHopsToCs.setStatus("current")
_PtopoDevLastVerifyTime_Type = TimeStamp
_PtopoDevLastVerifyTime_Object = MibTableColumn
ptopoDevLastVerifyTime = _PtopoDevLastVerifyTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 33, 1, 2, 1, 1, 8),
    _PtopoDevLastVerifyTime_Type()
)
ptopoDevLastVerifyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptopoDevLastVerifyTime.setStatus("current")
_PtopoConfig_ObjectIdentity = ObjectIdentity
ptopoConfig = _PtopoConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 33, 1, 3)
)


class _PtopoConfigInterval_Type(Integer32):
    """Custom type ptopoConfigInterval based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_PtopoConfigInterval_Type.__name__ = "Integer32"
_PtopoConfigInterval_Object = MibScalar
ptopoConfigInterval = _PtopoConfigInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 33, 1, 3, 1),
    _PtopoConfigInterval_Type()
)
ptopoConfigInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptopoConfigInterval.setStatus("current")
if mibBuilder.loadTexts:
    ptopoConfigInterval.setUnits("seconds")


class _PtopoConfigMaxHoldTime_Type(Integer32):
    """Custom type ptopoConfigMaxHoldTime based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_PtopoConfigMaxHoldTime_Type.__name__ = "Integer32"
_PtopoConfigMaxHoldTime_Object = MibScalar
ptopoConfigMaxHoldTime = _PtopoConfigMaxHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 33, 1, 3, 2),
    _PtopoConfigMaxHoldTime_Type()
)
ptopoConfigMaxHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptopoConfigMaxHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    ptopoConfigMaxHoldTime.setUnits("seconds")


class _PtopoConfigHopCount_Type(Integer32):
    """Custom type ptopoConfigHopCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_PtopoConfigHopCount_Type.__name__ = "Integer32"
_PtopoConfigHopCount_Object = MibScalar
ptopoConfigHopCount = _PtopoConfigHopCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 33, 1, 3, 3),
    _PtopoConfigHopCount_Type()
)
ptopoConfigHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptopoConfigHopCount.setStatus("current")
_RuijieptopoMIBConformance_ObjectIdentity = ObjectIdentity
ruijieptopoMIBConformance = _RuijieptopoMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 33, 2)
)
_RuijieptopoMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieptopoMIBCompliances = _RuijieptopoMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 33, 2, 1)
)
_RuijieptopoMIBGroups_ObjectIdentity = ObjectIdentity
ruijieptopoMIBGroups = _RuijieptopoMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 33, 2, 2)
)

# Managed Objects groups

ruijieptopoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 33, 2, 2, 1)
)
ruijieptopoMIBGroup.setObjects(
      *(("RUIJIE-PTOPO-MIB", "ptopoConnRemoteDevice"),
        ("RUIJIE-PTOPO-MIB", "ptopoConnRemotePort"),
        ("RUIJIE-PTOPO-MIB", "ptopoConnIsUpStream"),
        ("RUIJIE-PTOPO-MIB", "ptopoDevHostname"),
        ("RUIJIE-PTOPO-MIB", "ptopoDevClusStatus"),
        ("RUIJIE-PTOPO-MIB", "ptopoDevClusMode"),
        ("RUIJIE-PTOPO-MIB", "ptopoDevClusName"),
        ("RUIJIE-PTOPO-MIB", "ptopoDevCSMac"),
        ("RUIJIE-PTOPO-MIB", "ptopoDevHopsToCs"),
        ("RUIJIE-PTOPO-MIB", "ptopoDevLastVerifyTime"),
        ("RUIJIE-PTOPO-MIB", "ptopoConfigInterval"),
        ("RUIJIE-PTOPO-MIB", "ptopoConfigMaxHoldTime"),
        ("RUIJIE-PTOPO-MIB", "ptopoConfigHopCount"))
)
if mibBuilder.loadTexts:
    ruijieptopoMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieptopoMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 33, 2, 1, 1)
)
ruijieptopoMIBCompliance.setObjects(
    ("RUIJIE-PTOPO-MIB", "ruijieptopoMIBGroup")
)
if mibBuilder.loadTexts:
    ruijieptopoMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-PTOPO-MIB",
    **{"ruijiePotopoMIB": ruijiePotopoMIB,
       "ptopoMIBObjects": ptopoMIBObjects,
       "ptopoConnData": ptopoConnData,
       "ptopoConnTable": ptopoConnTable,
       "ptopoConnEntry": ptopoConnEntry,
       "ptopoConnIndex": ptopoConnIndex,
       "ptopoConnLocalDevice": ptopoConnLocalDevice,
       "ptopoConnLocalPort": ptopoConnLocalPort,
       "ptopoConnRemoteDevice": ptopoConnRemoteDevice,
       "ptopoConnRemotePort": ptopoConnRemotePort,
       "ptopoConnIsUpStream": ptopoConnIsUpStream,
       "ptopoDevData": ptopoDevData,
       "ptopoDevTable": ptopoDevTable,
       "ptopoDevEntry": ptopoDevEntry,
       "ptopoDevID": ptopoDevID,
       "ptopoDevHostname": ptopoDevHostname,
       "ptopoDevClusStatus": ptopoDevClusStatus,
       "ptopoDevClusMode": ptopoDevClusMode,
       "ptopoDevClusName": ptopoDevClusName,
       "ptopoDevCSMac": ptopoDevCSMac,
       "ptopoDevHopsToCs": ptopoDevHopsToCs,
       "ptopoDevLastVerifyTime": ptopoDevLastVerifyTime,
       "ptopoConfig": ptopoConfig,
       "ptopoConfigInterval": ptopoConfigInterval,
       "ptopoConfigMaxHoldTime": ptopoConfigMaxHoldTime,
       "ptopoConfigHopCount": ptopoConfigHopCount,
       "ruijieptopoMIBConformance": ruijieptopoMIBConformance,
       "ruijieptopoMIBCompliances": ruijieptopoMIBCompliances,
       "ruijieptopoMIBCompliance": ruijieptopoMIBCompliance,
       "ruijieptopoMIBGroups": ruijieptopoMIBGroups,
       "ruijieptopoMIBGroup": ruijieptopoMIBGroup}
)
