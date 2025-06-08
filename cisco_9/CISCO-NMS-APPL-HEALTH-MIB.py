# SNMP MIB module (CISCO-NMS-APPL-HEALTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-NMS-APPL-HEALTH-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:13:24 2025
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

(Percent,) = mibBuilder.importSymbols(
    "CISCO-QOS-PIB-MIB",
    "Percent")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoAlarmSeverity,
 CiscoMilliSeconds,
 TimeIntervalSec) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoAlarmSeverity",
    "CiscoMilliSeconds",
    "TimeIntervalSec")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ciscoNmsApplHealthMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 237)
)
if mibBuilder.loadTexts:
    ciscoNmsApplHealthMIB.setRevisions(
        ("2019-09-03 00:00",
         "2001-10-25 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoNmsApplHealthNotifs_ObjectIdentity = ObjectIdentity
ciscoNmsApplHealthNotifs = _CiscoNmsApplHealthNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 0)
)
_CiscoNmsApplHealthMIBObjects_ObjectIdentity = ObjectIdentity
ciscoNmsApplHealthMIBObjects = _CiscoNmsApplHealthMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 1)
)
_CnaHealthObj_ObjectIdentity = ObjectIdentity
cnaHealthObj = _CnaHealthObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1)
)
_CnaHealthNotifSeqNum_Type = Counter32
_CnaHealthNotifSeqNum_Object = MibScalar
cnaHealthNotifSeqNum = _CnaHealthNotifSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 1),
    _CnaHealthNotifSeqNum_Type()
)
cnaHealthNotifSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnaHealthNotifSeqNum.setStatus("current")
_CnaHealthTable_Object = MibTable
cnaHealthTable = _CnaHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cnaHealthTable.setStatus("current")
_CnaHealthTableEntry_Object = MibTableRow
cnaHealthTableEntry = _CnaHealthTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 2, 1)
)
cnaHealthTableEntry.setIndexNames(
    (0, "CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthTableIndex"),
)
if mibBuilder.loadTexts:
    cnaHealthTableEntry.setStatus("current")


class _CnaHealthTableIndex_Type(Unsigned32):
    """Custom type cnaHealthTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CnaHealthTableIndex_Type.__name__ = "Unsigned32"
_CnaHealthTableIndex_Object = MibTableColumn
cnaHealthTableIndex = _CnaHealthTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 2, 1, 1),
    _CnaHealthTableIndex_Type()
)
cnaHealthTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnaHealthTableIndex.setStatus("current")
_CnaHealthStatusChangeTime_Type = DateAndTime
_CnaHealthStatusChangeTime_Object = MibTableColumn
cnaHealthStatusChangeTime = _CnaHealthStatusChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 2, 1, 2),
    _CnaHealthStatusChangeTime_Type()
)
cnaHealthStatusChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnaHealthStatusChangeTime.setStatus("current")


class _CnaHealthName_Type(SnmpAdminString):
    """Custom type cnaHealthName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CnaHealthName_Type.__name__ = "SnmpAdminString"
_CnaHealthName_Object = MibTableColumn
cnaHealthName = _CnaHealthName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 2, 1, 3),
    _CnaHealthName_Type()
)
cnaHealthName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnaHealthName.setStatus("current")


class _CnaHealthStatus_Type(Integer32):
    """Custom type cnaHealthStatus based on Integer32"""
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
        *(("started", 1),
          ("stopped", 2),
          ("busy", 3),
          ("failed", 4),
          ("exited", 5))
    )


_CnaHealthStatus_Type.__name__ = "Integer32"
_CnaHealthStatus_Object = MibTableColumn
cnaHealthStatus = _CnaHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 2, 1, 4),
    _CnaHealthStatus_Type()
)
cnaHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnaHealthStatus.setStatus("current")


class _CnaHealthSevLevel_Type(CiscoAlarmSeverity):
    """Custom type cnaHealthSevLevel based on CiscoAlarmSeverity"""
    defaultValue = 7


_CnaHealthSevLevel_Type.__name__ = "CiscoAlarmSeverity"
_CnaHealthSevLevel_Object = MibTableColumn
cnaHealthSevLevel = _CnaHealthSevLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 2, 1, 5),
    _CnaHealthSevLevel_Type()
)
cnaHealthSevLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnaHealthSevLevel.setStatus("current")


class _CnaHealthComLineArgs_Type(SnmpAdminString):
    """Custom type cnaHealthComLineArgs based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CnaHealthComLineArgs_Type.__name__ = "SnmpAdminString"
_CnaHealthComLineArgs_Object = MibTableColumn
cnaHealthComLineArgs = _CnaHealthComLineArgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 2, 1, 6),
    _CnaHealthComLineArgs_Type()
)
cnaHealthComLineArgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnaHealthComLineArgs.setStatus("current")


class _CnaHealthStatusDesc_Type(SnmpAdminString):
    """Custom type cnaHealthStatusDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CnaHealthStatusDesc_Type.__name__ = "SnmpAdminString"
_CnaHealthStatusDesc_Object = MibTableColumn
cnaHealthStatusDesc = _CnaHealthStatusDesc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 2, 1, 7),
    _CnaHealthStatusDesc_Type()
)
cnaHealthStatusDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnaHealthStatusDesc.setStatus("current")
_CnaHealthUpTime_Type = TimeIntervalSec
_CnaHealthUpTime_Object = MibTableColumn
cnaHealthUpTime = _CnaHealthUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 2, 1, 8),
    _CnaHealthUpTime_Type()
)
cnaHealthUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnaHealthUpTime.setStatus("current")
if mibBuilder.loadTexts:
    cnaHealthUpTime.setUnits("Seconds")
_CnahPerformanceTable_Object = MibTable
cnahPerformanceTable = _CnahPerformanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cnahPerformanceTable.setStatus("current")
_CnahPerformanceEntry_Object = MibTableRow
cnahPerformanceEntry = _CnahPerformanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 3, 1)
)
cnahPerformanceEntry.setIndexNames(
    (0, "CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthTableIndex"),
)
if mibBuilder.loadTexts:
    cnahPerformanceEntry.setStatus("current")
_CnahPerfCpuUtilization_Type = Percent
_CnahPerfCpuUtilization_Object = MibTableColumn
cnahPerfCpuUtilization = _CnahPerfCpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 3, 1, 1),
    _CnahPerfCpuUtilization_Type()
)
cnahPerfCpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnahPerfCpuUtilization.setStatus("current")
if mibBuilder.loadTexts:
    cnahPerfCpuUtilization.setUnits("%")
_CnahPerfMemoryUtilization_Type = Percent
_CnahPerfMemoryUtilization_Object = MibTableColumn
cnahPerfMemoryUtilization = _CnahPerfMemoryUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 3, 1, 2),
    _CnahPerfMemoryUtilization_Type()
)
cnahPerfMemoryUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnahPerfMemoryUtilization.setStatus("current")
if mibBuilder.loadTexts:
    cnahPerfMemoryUtilization.setUnits("%")
_CnahPerfLatency_Type = CiscoMilliSeconds
_CnahPerfLatency_Object = MibTableColumn
cnahPerfLatency = _CnahPerfLatency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 3, 1, 3),
    _CnahPerfLatency_Type()
)
cnahPerfLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnahPerfLatency.setStatus("current")
if mibBuilder.loadTexts:
    cnahPerfLatency.setUnits("msec")
_CnahPerfHeapUsed_Type = Gauge32
_CnahPerfHeapUsed_Object = MibTableColumn
cnahPerfHeapUsed = _CnahPerfHeapUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 3, 1, 4),
    _CnahPerfHeapUsed_Type()
)
cnahPerfHeapUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnahPerfHeapUsed.setStatus("current")
if mibBuilder.loadTexts:
    cnahPerfHeapUsed.setUnits("KBytes")
_CnahPerfDataIn_Type = Gauge32
_CnahPerfDataIn_Object = MibTableColumn
cnahPerfDataIn = _CnahPerfDataIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 3, 1, 5),
    _CnahPerfDataIn_Type()
)
cnahPerfDataIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnahPerfDataIn.setStatus("current")
if mibBuilder.loadTexts:
    cnahPerfDataIn.setUnits("KBytes")
_CnahPerfDataOut_Type = Gauge32
_CnahPerfDataOut_Object = MibTableColumn
cnahPerfDataOut = _CnahPerfDataOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 3, 1, 6),
    _CnahPerfDataOut_Type()
)
cnahPerfDataOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnahPerfDataOut.setStatus("current")
if mibBuilder.loadTexts:
    cnahPerfDataOut.setUnits("KBytes")
_CnahPerfMessageIn_Type = Gauge32
_CnahPerfMessageIn_Object = MibTableColumn
cnahPerfMessageIn = _CnahPerfMessageIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 3, 1, 7),
    _CnahPerfMessageIn_Type()
)
cnahPerfMessageIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnahPerfMessageIn.setStatus("current")
if mibBuilder.loadTexts:
    cnahPerfMessageIn.setUnits("messages")
_CnahPerfMessageOut_Type = Gauge32
_CnahPerfMessageOut_Object = MibTableColumn
cnahPerfMessageOut = _CnahPerfMessageOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 3, 1, 8),
    _CnahPerfMessageOut_Type()
)
cnahPerfMessageOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnahPerfMessageOut.setStatus("current")
if mibBuilder.loadTexts:
    cnahPerfMessageOut.setUnits("messages")
_CnahPerfDiskRead_Type = Gauge32
_CnahPerfDiskRead_Object = MibTableColumn
cnahPerfDiskRead = _CnahPerfDiskRead_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 3, 1, 9),
    _CnahPerfDiskRead_Type()
)
cnahPerfDiskRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnahPerfDiskRead.setStatus("current")
if mibBuilder.loadTexts:
    cnahPerfDiskRead.setUnits("KBytes")
_CnahPerfDiskWrite_Type = Gauge32
_CnahPerfDiskWrite_Object = MibTableColumn
cnahPerfDiskWrite = _CnahPerfDiskWrite_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 3, 1, 10),
    _CnahPerfDiskWrite_Type()
)
cnahPerfDiskWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnahPerfDiskWrite.setStatus("current")
if mibBuilder.loadTexts:
    cnahPerfDiskWrite.setUnits("KBytes")
_CnahPerfDiskUsage_Type = Percent
_CnahPerfDiskUsage_Object = MibTableColumn
cnahPerfDiskUsage = _CnahPerfDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 3, 1, 11),
    _CnahPerfDiskUsage_Type()
)
cnahPerfDiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnahPerfDiskUsage.setStatus("current")
if mibBuilder.loadTexts:
    cnahPerfDiskUsage.setUnits("%")
_CnahPerfDiskTotal_Type = Gauge32
_CnahPerfDiskTotal_Object = MibTableColumn
cnahPerfDiskTotal = _CnahPerfDiskTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 1, 1, 3, 1, 12),
    _CnahPerfDiskTotal_Type()
)
cnahPerfDiskTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnahPerfDiskTotal.setStatus("current")
if mibBuilder.loadTexts:
    cnahPerfDiskTotal.setUnits("KBytes")
_CiscoNmsApplHealthMIBConforms_ObjectIdentity = ObjectIdentity
ciscoNmsApplHealthMIBConforms = _CiscoNmsApplHealthMIBConforms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 2)
)
_CnaHealthMIBCompliances_ObjectIdentity = ObjectIdentity
cnaHealthMIBCompliances = _CnaHealthMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 2, 1)
)
_CnaHealthMIBGroups_ObjectIdentity = ObjectIdentity
cnaHealthMIBGroups = _CnaHealthMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 2, 2)
)

# Managed Objects groups

cnaHealthMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 2, 2, 1)
)
cnaHealthMIBGroup.setObjects(
      *(("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthNotifSeqNum"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthTableIndex"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthStatusChangeTime"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthName"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthStatus"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthSevLevel"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthComLineArgs"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthStatusDesc"))
)
if mibBuilder.loadTexts:
    cnaHealthMIBGroup.setStatus("current")

cnaHealthMIBGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 2, 2, 3)
)
cnaHealthMIBGroup2.setObjects(
    ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthUpTime")
)
if mibBuilder.loadTexts:
    cnaHealthMIBGroup2.setStatus("current")

cnahPerformanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 2, 2, 4)
)
cnahPerformanceGroup.setObjects(
      *(("CISCO-NMS-APPL-HEALTH-MIB", "cnahPerfCpuUtilization"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnahPerfMemoryUtilization"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnahPerfLatency"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnahPerfHeapUsed"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnahPerfDataIn"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnahPerfDataOut"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnahPerfMessageIn"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnahPerfMessageOut"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnahPerfDiskRead"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnahPerfDiskWrite"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnahPerfDiskUsage"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnahPerfDiskTotal"))
)
if mibBuilder.loadTexts:
    cnahPerformanceGroup.setStatus("current")


# Notification objects

cnaHealthNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 0, 1)
)
cnaHealthNotif.setObjects(
      *(("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthNotifSeqNum"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthStatusChangeTime"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthName"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthStatus"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthSevLevel"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthComLineArgs"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthStatusDesc"))
)
if mibBuilder.loadTexts:
    cnaHealthNotif.setStatus(
        "current"
    )


# Notifications groups

cnaHealthNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 2, 2, 2)
)
cnaHealthNotifGroup.setObjects(
    ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthNotif")
)
if mibBuilder.loadTexts:
    cnaHealthNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cnaHealthMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 2, 1, 1)
)
cnaHealthMIBCompliance.setObjects(
      *(("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthMIBGroup"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthNotifGroup"))
)
if mibBuilder.loadTexts:
    cnaHealthMIBCompliance.setStatus(
        "deprecated"
    )

cnaHealthMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 237, 2, 1, 2)
)
cnaHealthMIBCompliance2.setObjects(
      *(("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthMIBGroup"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthNotifGroup"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnaHealthMIBGroup2"),
        ("CISCO-NMS-APPL-HEALTH-MIB", "cnahPerformanceGroup"))
)
if mibBuilder.loadTexts:
    cnaHealthMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-NMS-APPL-HEALTH-MIB",
    **{"ciscoNmsApplHealthMIB": ciscoNmsApplHealthMIB,
       "ciscoNmsApplHealthNotifs": ciscoNmsApplHealthNotifs,
       "cnaHealthNotif": cnaHealthNotif,
       "ciscoNmsApplHealthMIBObjects": ciscoNmsApplHealthMIBObjects,
       "cnaHealthObj": cnaHealthObj,
       "cnaHealthNotifSeqNum": cnaHealthNotifSeqNum,
       "cnaHealthTable": cnaHealthTable,
       "cnaHealthTableEntry": cnaHealthTableEntry,
       "cnaHealthTableIndex": cnaHealthTableIndex,
       "cnaHealthStatusChangeTime": cnaHealthStatusChangeTime,
       "cnaHealthName": cnaHealthName,
       "cnaHealthStatus": cnaHealthStatus,
       "cnaHealthSevLevel": cnaHealthSevLevel,
       "cnaHealthComLineArgs": cnaHealthComLineArgs,
       "cnaHealthStatusDesc": cnaHealthStatusDesc,
       "cnaHealthUpTime": cnaHealthUpTime,
       "cnahPerformanceTable": cnahPerformanceTable,
       "cnahPerformanceEntry": cnahPerformanceEntry,
       "cnahPerfCpuUtilization": cnahPerfCpuUtilization,
       "cnahPerfMemoryUtilization": cnahPerfMemoryUtilization,
       "cnahPerfLatency": cnahPerfLatency,
       "cnahPerfHeapUsed": cnahPerfHeapUsed,
       "cnahPerfDataIn": cnahPerfDataIn,
       "cnahPerfDataOut": cnahPerfDataOut,
       "cnahPerfMessageIn": cnahPerfMessageIn,
       "cnahPerfMessageOut": cnahPerfMessageOut,
       "cnahPerfDiskRead": cnahPerfDiskRead,
       "cnahPerfDiskWrite": cnahPerfDiskWrite,
       "cnahPerfDiskUsage": cnahPerfDiskUsage,
       "cnahPerfDiskTotal": cnahPerfDiskTotal,
       "ciscoNmsApplHealthMIBConforms": ciscoNmsApplHealthMIBConforms,
       "cnaHealthMIBCompliances": cnaHealthMIBCompliances,
       "cnaHealthMIBCompliance": cnaHealthMIBCompliance,
       "cnaHealthMIBCompliance2": cnaHealthMIBCompliance2,
       "cnaHealthMIBGroups": cnaHealthMIBGroups,
       "cnaHealthMIBGroup": cnaHealthMIBGroup,
       "cnaHealthNotifGroup": cnaHealthNotifGroup,
       "cnaHealthMIBGroup2": cnaHealthMIBGroup2,
       "cnahPerformanceGroup": cnahPerformanceGroup}
)
