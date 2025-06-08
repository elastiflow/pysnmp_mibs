# SNMP MIB module (FORTINET-FORTIWAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/fortinet_12356/FORTINET-FORTIWAN-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 15:36:32 2025
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

(FnBoolState,
 FnIndex,
 fortinet) = mibBuilder.importSymbols(
    "FORTINET-CORE-MIB",
    "FnBoolState",
    "FnIndex",
    "fortinet")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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


# MODULE-IDENTITY

fnFortiWANMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118)
)
if mibBuilder.loadTexts:
    fnFortiWANMib.setRevisions(
        ("2017-12-18 00:00",
         "2015-11-09 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FnHAModeVal(TextualConvention, Integer32):
    status = "current"
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
        *(("standalone", 1),
          ("activePassive", 2),
          ("activeActive", 3),
          ("activeActiveVrrp", 4))
    )



class FnVdIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class FnHaState(TextualConvention, Integer32):
    status = "current"
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
        *(("master", 1),
          ("backup", 2),
          ("standalone", 3),
          ("unknown", 4))
    )



# MIB Managed Objects in the order of their OIDs

_FwnTraps_ObjectIdentity = ObjectIdentity
fwnTraps = _FwnTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0)
)
_FwnSystem_ObjectIdentity = ObjectIdentity
fwnSystem = _FwnSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 1)
)


class _FwnSysModel_Type(DisplayString):
    """Custom type fwnSysModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FwnSysModel_Type.__name__ = "DisplayString"
_FwnSysModel_Object = MibScalar
fwnSysModel = _FwnSysModel_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 1, 1),
    _FwnSysModel_Type()
)
fwnSysModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnSysModel.setStatus("current")


class _FwnSysSerial_Type(DisplayString):
    """Custom type fwnSysSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FwnSysSerial_Type.__name__ = "DisplayString"
_FwnSysSerial_Object = MibScalar
fwnSysSerial = _FwnSysSerial_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 1, 2),
    _FwnSysSerial_Type()
)
fwnSysSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnSysSerial.setStatus("current")


class _FwnSysVersion_Type(DisplayString):
    """Custom type fwnSysVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FwnSysVersion_Type.__name__ = "DisplayString"
_FwnSysVersion_Object = MibScalar
fwnSysVersion = _FwnSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 1, 3),
    _FwnSysVersion_Type()
)
fwnSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnSysVersion.setStatus("current")
_FwnSysCpuUsage_Type = Gauge32
_FwnSysCpuUsage_Object = MibScalar
fwnSysCpuUsage = _FwnSysCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 1, 4),
    _FwnSysCpuUsage_Type()
)
fwnSysCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnSysCpuUsage.setStatus("current")
_FwnSysMemUsage_Type = Gauge32
_FwnSysMemUsage_Object = MibScalar
fwnSysMemUsage = _FwnSysMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 1, 5),
    _FwnSysMemUsage_Type()
)
fwnSysMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnSysMemUsage.setStatus("current")
_FwnSysLogDiskUsage_Type = Gauge32
_FwnSysLogDiskUsage_Object = MibScalar
fwnSysLogDiskUsage = _FwnSysLogDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 1, 6),
    _FwnSysLogDiskUsage_Type()
)
fwnSysLogDiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnSysLogDiskUsage.setStatus("current")
_FwnSysLoad_Type = Gauge32
_FwnSysLoad_Object = MibScalar
fwnSysLoad = _FwnSysLoad_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 1, 7),
    _FwnSysLoad_Type()
)
fwnSysLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnSysLoad.setStatus("current")
_FwnSysCpuUsageTable_Object = MibTable
fwnSysCpuUsageTable = _FwnSysCpuUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 1, 8)
)
if mibBuilder.loadTexts:
    fwnSysCpuUsageTable.setStatus("current")
_FwnSysCpuUsageEntry_Object = MibTableRow
fwnSysCpuUsageEntry = _FwnSysCpuUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 1, 8, 1)
)
fwnSysCpuUsageEntry.setIndexNames(
    (0, "FORTINET-FORTIWAN-MIB", "fwnSysCpuIndex"),
)
if mibBuilder.loadTexts:
    fwnSysCpuUsageEntry.setStatus("current")


class _FwnSysCpuIndex_Type(Integer32):
    """Custom type fwnSysCpuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FwnSysCpuIndex_Type.__name__ = "Integer32"
_FwnSysCpuIndex_Object = MibTableColumn
fwnSysCpuIndex = _FwnSysCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 1, 8, 1, 1),
    _FwnSysCpuIndex_Type()
)
fwnSysCpuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwnSysCpuIndex.setStatus("current")
_FwnSysCpuName_Type = DisplayString
_FwnSysCpuName_Object = MibTableColumn
fwnSysCpuName = _FwnSysCpuName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 1, 8, 1, 2),
    _FwnSysCpuName_Type()
)
fwnSysCpuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnSysCpuName.setStatus("current")
_FwnSysCpu2secAvgUsage_Type = Gauge32
_FwnSysCpu2secAvgUsage_Object = MibTableColumn
fwnSysCpu2secAvgUsage = _FwnSysCpu2secAvgUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 1, 8, 1, 3),
    _FwnSysCpu2secAvgUsage_Type()
)
fwnSysCpu2secAvgUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnSysCpu2secAvgUsage.setStatus("current")
_FwnSysCpu1minAvgUsage_Type = Gauge32
_FwnSysCpu1minAvgUsage_Object = MibTableColumn
fwnSysCpu1minAvgUsage = _FwnSysCpu1minAvgUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 1, 8, 1, 4),
    _FwnSysCpu1minAvgUsage_Type()
)
fwnSysCpu1minAvgUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnSysCpu1minAvgUsage.setStatus("current")
_FwnSysCpu5minAvgUsage_Type = Gauge32
_FwnSysCpu5minAvgUsage_Object = MibTableColumn
fwnSysCpu5minAvgUsage = _FwnSysCpu5minAvgUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 1, 8, 1, 5),
    _FwnSysCpu5minAvgUsage_Type()
)
fwnSysCpu5minAvgUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnSysCpu5minAvgUsage.setStatus("current")
_FwnSysOptions_ObjectIdentity = ObjectIdentity
fwnSysOptions = _FwnSysOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 1, 9)
)
_FwnSysOptIdleTimeout_Type = Integer32
_FwnSysOptIdleTimeout_Object = MibScalar
fwnSysOptIdleTimeout = _FwnSysOptIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 1, 9, 1),
    _FwnSysOptIdleTimeout_Type()
)
fwnSysOptIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnSysOptIdleTimeout.setStatus("current")
_FwnSysHA_ObjectIdentity = ObjectIdentity
fwnSysHA = _FwnSysHA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 1, 10)
)
_FwnHAMode_Type = FnHAModeVal
_FwnHAMode_Object = MibScalar
fwnHAMode = _FwnHAMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 1, 10, 1),
    _FwnHAMode_Type()
)
fwnHAMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnHAMode.setStatus("current")
_FwnVirtualDomain_ObjectIdentity = ObjectIdentity
fwnVirtualDomain = _FwnVirtualDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2)
)
_FwnVdMaxVdoms_Type = Integer32
_FwnVdMaxVdoms_Object = MibScalar
fwnVdMaxVdoms = _FwnVdMaxVdoms_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 1),
    _FwnVdMaxVdoms_Type()
)
fwnVdMaxVdoms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnVdMaxVdoms.setStatus("current")
_FwnVdEnabled_Type = FnBoolState
_FwnVdEnabled_Object = MibScalar
fwnVdEnabled = _FwnVdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 2),
    _FwnVdEnabled_Type()
)
fwnVdEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnVdEnabled.setStatus("current")
_FwnVdNumber_Type = Integer32
_FwnVdNumber_Object = MibScalar
fwnVdNumber = _FwnVdNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 3),
    _FwnVdNumber_Type()
)
fwnVdNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnVdNumber.setStatus("current")
_FwnVdTable_Object = MibTable
fwnVdTable = _FwnVdTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 4)
)
if mibBuilder.loadTexts:
    fwnVdTable.setStatus("current")
_FwnVdEntry_Object = MibTableRow
fwnVdEntry = _FwnVdEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 4, 1)
)
fwnVdEntry.setIndexNames(
    (0, "FORTINET-FORTIWAN-MIB", "fwnVdEntryIndex"),
)
if mibBuilder.loadTexts:
    fwnVdEntry.setStatus("current")
_FwnVdEntryIndex_Type = FnVdIndex
_FwnVdEntryIndex_Object = MibTableColumn
fwnVdEntryIndex = _FwnVdEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 4, 1, 1),
    _FwnVdEntryIndex_Type()
)
fwnVdEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwnVdEntryIndex.setStatus("current")
_FwnVdEntryName_Type = DisplayString
_FwnVdEntryName_Object = MibTableColumn
fwnVdEntryName = _FwnVdEntryName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 4, 1, 2),
    _FwnVdEntryName_Type()
)
fwnVdEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnVdEntryName.setStatus("current")
_FwnVdEntHaState_Type = FnHaState
_FwnVdEntHaState_Object = MibTableColumn
fwnVdEntHaState = _FwnVdEntHaState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 2, 4, 1, 3),
    _FwnVdEntHaState_Type()
)
fwnVdEntHaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwnVdEntHaState.setStatus("current")
_FwnVirtualServer_ObjectIdentity = ObjectIdentity
fwnVirtualServer = _FwnVirtualServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3)
)
_FadcVSNumber_Type = Integer32
_FadcVSNumber_Object = MibScalar
fadcVSNumber = _FadcVSNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 1),
    _FadcVSNumber_Type()
)
fadcVSNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVSNumber.setStatus("current")
_FadcVSTable_Object = MibTable
fadcVSTable = _FadcVSTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 2)
)
if mibBuilder.loadTexts:
    fadcVSTable.setStatus("current")
_FadcVSEntry_Object = MibTableRow
fadcVSEntry = _FadcVSEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 2, 1)
)
fadcVSEntry.setIndexNames(
    (0, "FORTINET-FORTIWAN-MIB", "fadcVSIndex"),
)
if mibBuilder.loadTexts:
    fadcVSEntry.setStatus("current")


class _FadcVSIndex_Type(Integer32):
    """Custom type fadcVSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcVSIndex_Type.__name__ = "Integer32"
_FadcVSIndex_Object = MibTableColumn
fadcVSIndex = _FadcVSIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 2, 1, 1),
    _FadcVSIndex_Type()
)
fadcVSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcVSIndex.setStatus("current")
_FadcVSName_Type = DisplayString
_FadcVSName_Object = MibTableColumn
fadcVSName = _FadcVSName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 2, 1, 2),
    _FadcVSName_Type()
)
fadcVSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVSName.setStatus("current")
_FadcVSStatus_Type = DisplayString
_FadcVSStatus_Object = MibTableColumn
fadcVSStatus = _FadcVSStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 2, 1, 3),
    _FadcVSStatus_Type()
)
fadcVSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVSStatus.setStatus("current")
_FadcVSHealth_Type = DisplayString
_FadcVSHealth_Object = MibTableColumn
fadcVSHealth = _FadcVSHealth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 2, 1, 4),
    _FadcVSHealth_Type()
)
fadcVSHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVSHealth.setStatus("current")


class _FadcVSNewConnections_Type(Integer32):
    """Custom type fadcVSNewConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcVSNewConnections_Type.__name__ = "Integer32"
_FadcVSNewConnections_Object = MibTableColumn
fadcVSNewConnections = _FadcVSNewConnections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 2, 1, 5),
    _FadcVSNewConnections_Type()
)
fadcVSNewConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVSNewConnections.setStatus("current")


class _FadcVSConcurrent_Type(Integer32):
    """Custom type fadcVSConcurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcVSConcurrent_Type.__name__ = "Integer32"
_FadcVSConcurrent_Object = MibTableColumn
fadcVSConcurrent = _FadcVSConcurrent_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 2, 1, 6),
    _FadcVSConcurrent_Type()
)
fadcVSConcurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVSConcurrent.setStatus("current")


class _FadcVSThroughputKbps_Type(Integer32):
    """Custom type fadcVSThroughputKbps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcVSThroughputKbps_Type.__name__ = "Integer32"
_FadcVSThroughputKbps_Object = MibTableColumn
fadcVSThroughputKbps = _FadcVSThroughputKbps_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 2, 1, 7),
    _FadcVSThroughputKbps_Type()
)
fadcVSThroughputKbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVSThroughputKbps.setStatus("current")
_FadcVSVdom_Type = DisplayString
_FadcVSVdom_Object = MibTableColumn
fadcVSVdom = _FadcVSVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 3, 2, 1, 8),
    _FadcVSVdom_Type()
)
fadcVSVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVSVdom.setStatus("current")
_FadcIntf_ObjectIdentity = ObjectIdentity
fadcIntf = _FadcIntf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 4)
)
_FadcIntfTable_Object = MibTable
fadcIntfTable = _FadcIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 4, 1)
)
if mibBuilder.loadTexts:
    fadcIntfTable.setStatus("current")
_FadcIntfEntry_Object = MibTableRow
fadcIntfEntry = _FadcIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 4, 1, 1)
)
fadcIntfEntry.setIndexNames(
    (0, "FORTINET-FORTIWAN-MIB", "fadcIntfIndex"),
)
if mibBuilder.loadTexts:
    fadcIntfEntry.setStatus("current")


class _FadcIntfIndex_Type(Integer32):
    """Custom type fadcIntfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcIntfIndex_Type.__name__ = "Integer32"
_FadcIntfIndex_Object = MibTableColumn
fadcIntfIndex = _FadcIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 4, 1, 1, 1),
    _FadcIntfIndex_Type()
)
fadcIntfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcIntfIndex.setStatus("current")
_FadcIntfName_Type = DisplayString
_FadcIntfName_Object = MibTableColumn
fadcIntfName = _FadcIntfName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 4, 1, 1, 2),
    _FadcIntfName_Type()
)
fadcIntfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcIntfName.setStatus("current")
_FadcIntfVdom_Type = DisplayString
_FadcIntfVdom_Object = MibTableColumn
fadcIntfVdom = _FadcIntfVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 4, 1, 1, 3),
    _FadcIntfVdom_Type()
)
fadcIntfVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcIntfVdom.setStatus("current")
_FadcAdmin_ObjectIdentity = ObjectIdentity
fadcAdmin = _FadcAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 5)
)
_FadcAdminTable_Object = MibTable
fadcAdminTable = _FadcAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 5, 1)
)
if mibBuilder.loadTexts:
    fadcAdminTable.setStatus("current")
_FadcAdminEntry_Object = MibTableRow
fadcAdminEntry = _FadcAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 5, 1, 1)
)
fadcAdminEntry.setIndexNames(
    (0, "FORTINET-FORTIWAN-MIB", "fadcAdminIndex"),
)
if mibBuilder.loadTexts:
    fadcAdminEntry.setStatus("current")
_FadcAdminIndex_Type = Integer32
_FadcAdminIndex_Object = MibTableColumn
fadcAdminIndex = _FadcAdminIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 5, 1, 1, 1),
    _FadcAdminIndex_Type()
)
fadcAdminIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcAdminIndex.setStatus("current")
_FadcAdminName_Type = DisplayString
_FadcAdminName_Object = MibTableColumn
fadcAdminName = _FadcAdminName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 5, 1, 1, 2),
    _FadcAdminName_Type()
)
fadcAdminName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcAdminName.setStatus("current")
_FadcAdminVdom_Type = DisplayString
_FadcAdminVdom_Object = MibTableColumn
fadcAdminVdom = _FadcAdminVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 5, 1, 1, 3),
    _FadcAdminVdom_Type()
)
fadcAdminVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcAdminVdom.setStatus("current")
_FadcHardware_ObjectIdentity = ObjectIdentity
fadcHardware = _FadcHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6)
)
_FadcCPUInfo_ObjectIdentity = ObjectIdentity
fadcCPUInfo = _FadcCPUInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 1)
)
_FadcCPUTable_Object = MibTable
fadcCPUTable = _FadcCPUTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 1, 1)
)
if mibBuilder.loadTexts:
    fadcCPUTable.setStatus("current")
_FadcCPUEntry_Object = MibTableRow
fadcCPUEntry = _FadcCPUEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 1, 1, 1)
)
fadcCPUEntry.setIndexNames(
    (0, "FORTINET-FORTIWAN-MIB", "fadcCPUIndex"),
)
if mibBuilder.loadTexts:
    fadcCPUEntry.setStatus("current")
_FadcCPUIndex_Type = Integer32
_FadcCPUIndex_Object = MibTableColumn
fadcCPUIndex = _FadcCPUIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 1, 1, 1, 1),
    _FadcCPUIndex_Type()
)
fadcCPUIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcCPUIndex.setStatus("current")
_FadcCPUName_Type = DisplayString
_FadcCPUName_Object = MibTableColumn
fadcCPUName = _FadcCPUName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 1, 1, 1, 2),
    _FadcCPUName_Type()
)
fadcCPUName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcCPUName.setStatus("current")
_FadcCPUTemp_Type = Integer32
_FadcCPUTemp_Object = MibTableColumn
fadcCPUTemp = _FadcCPUTemp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 1, 1, 1, 3),
    _FadcCPUTemp_Type()
)
fadcCPUTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcCPUTemp.setStatus("current")
_FadcPSUInfo_ObjectIdentity = ObjectIdentity
fadcPSUInfo = _FadcPSUInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 2)
)
_FadcPSUTable_Object = MibTable
fadcPSUTable = _FadcPSUTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 2, 1)
)
if mibBuilder.loadTexts:
    fadcPSUTable.setStatus("current")
_FadcPSUEntry_Object = MibTableRow
fadcPSUEntry = _FadcPSUEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 2, 1, 1)
)
fadcPSUEntry.setIndexNames(
    (0, "FORTINET-FORTIWAN-MIB", "fadcPSUIndex"),
)
if mibBuilder.loadTexts:
    fadcPSUEntry.setStatus("current")
_FadcPSUIndex_Type = Integer32
_FadcPSUIndex_Object = MibTableColumn
fadcPSUIndex = _FadcPSUIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 2, 1, 1, 1),
    _FadcPSUIndex_Type()
)
fadcPSUIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcPSUIndex.setStatus("current")
_FadcPSUName_Type = DisplayString
_FadcPSUName_Object = MibTableColumn
fadcPSUName = _FadcPSUName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 2, 1, 1, 2),
    _FadcPSUName_Type()
)
fadcPSUName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcPSUName.setStatus("current")
_FadcPSUTemp_Type = Integer32
_FadcPSUTemp_Object = MibTableColumn
fadcPSUTemp = _FadcPSUTemp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 2, 1, 1, 3),
    _FadcPSUTemp_Type()
)
fadcPSUTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcPSUTemp.setStatus("current")
_FadcPSUFanSpeed_Type = Integer32
_FadcPSUFanSpeed_Object = MibTableColumn
fadcPSUFanSpeed = _FadcPSUFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 2, 1, 1, 4),
    _FadcPSUFanSpeed_Type()
)
fadcPSUFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcPSUFanSpeed.setStatus("current")
_FadcPSUFanStatus_Type = DisplayString
_FadcPSUFanStatus_Object = MibTableColumn
fadcPSUFanStatus = _FadcPSUFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 2, 1, 1, 5),
    _FadcPSUFanStatus_Type()
)
fadcPSUFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcPSUFanStatus.setStatus("current")
_FadcPSUVoltage_Type = Integer32
_FadcPSUVoltage_Object = MibTableColumn
fadcPSUVoltage = _FadcPSUVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 2, 1, 1, 6),
    _FadcPSUVoltage_Type()
)
fadcPSUVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcPSUVoltage.setStatus("current")
_FadcPSUStatus_Type = DisplayString
_FadcPSUStatus_Object = MibTableColumn
fadcPSUStatus = _FadcPSUStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 2, 1, 1, 7),
    _FadcPSUStatus_Type()
)
fadcPSUStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcPSUStatus.setStatus("current")
_FadcNetworkInfo_ObjectIdentity = ObjectIdentity
fadcNetworkInfo = _FadcNetworkInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 3)
)
_FadcNetworkTable_Object = MibTable
fadcNetworkTable = _FadcNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 3, 1)
)
if mibBuilder.loadTexts:
    fadcNetworkTable.setStatus("current")
_FadcNetworkEntry_Object = MibTableRow
fadcNetworkEntry = _FadcNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 3, 1, 1)
)
fadcNetworkEntry.setIndexNames(
    (0, "FORTINET-FORTIWAN-MIB", "fadcNetworkIndex"),
)
if mibBuilder.loadTexts:
    fadcNetworkEntry.setStatus("current")
_FadcNetworkIndex_Type = Integer32
_FadcNetworkIndex_Object = MibTableColumn
fadcNetworkIndex = _FadcNetworkIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 3, 1, 1, 1),
    _FadcNetworkIndex_Type()
)
fadcNetworkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcNetworkIndex.setStatus("current")
_FadcPortLinkName_Type = DisplayString
_FadcPortLinkName_Object = MibTableColumn
fadcPortLinkName = _FadcPortLinkName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 3, 1, 1, 2),
    _FadcPortLinkName_Type()
)
fadcPortLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcPortLinkName.setStatus("current")
_FadcPortLinkStatus_Type = DisplayString
_FadcPortLinkStatus_Object = MibTableColumn
fadcPortLinkStatus = _FadcPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 3, 1, 1, 3),
    _FadcPortLinkStatus_Type()
)
fadcPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcPortLinkStatus.setStatus("current")
_FadcDeviceInfo_ObjectIdentity = ObjectIdentity
fadcDeviceInfo = _FadcDeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 4)
)
_FadcDeviceTempTables_ObjectIdentity = ObjectIdentity
fadcDeviceTempTables = _FadcDeviceTempTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 4, 1)
)
_FadcDeviceTempTable_Object = MibTable
fadcDeviceTempTable = _FadcDeviceTempTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 4, 1, 1)
)
if mibBuilder.loadTexts:
    fadcDeviceTempTable.setStatus("current")
_FadcDeviceTempEntry_Object = MibTableRow
fadcDeviceTempEntry = _FadcDeviceTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 4, 1, 1, 1)
)
fadcDeviceTempEntry.setIndexNames(
    (0, "FORTINET-FORTIWAN-MIB", "fadcDeviceTempIndex"),
)
if mibBuilder.loadTexts:
    fadcDeviceTempEntry.setStatus("current")
_FadcDeviceTempIndex_Type = Integer32
_FadcDeviceTempIndex_Object = MibTableColumn
fadcDeviceTempIndex = _FadcDeviceTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 4, 1, 1, 1, 1),
    _FadcDeviceTempIndex_Type()
)
fadcDeviceTempIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcDeviceTempIndex.setStatus("current")
_FadcDeviceTempName_Type = DisplayString
_FadcDeviceTempName_Object = MibTableColumn
fadcDeviceTempName = _FadcDeviceTempName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 4, 1, 1, 1, 2),
    _FadcDeviceTempName_Type()
)
fadcDeviceTempName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcDeviceTempName.setStatus("current")
_FadcDeviceTempValue_Type = Integer32
_FadcDeviceTempValue_Object = MibTableColumn
fadcDeviceTempValue = _FadcDeviceTempValue_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 4, 1, 1, 1, 3),
    _FadcDeviceTempValue_Type()
)
fadcDeviceTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcDeviceTempValue.setStatus("current")
_FadcDeviceFanTables_ObjectIdentity = ObjectIdentity
fadcDeviceFanTables = _FadcDeviceFanTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 4, 2)
)
_FadcDeviceFanTable_Object = MibTable
fadcDeviceFanTable = _FadcDeviceFanTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 4, 2, 1)
)
if mibBuilder.loadTexts:
    fadcDeviceFanTable.setStatus("current")
_FadcDeviceFanEntry_Object = MibTableRow
fadcDeviceFanEntry = _FadcDeviceFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 4, 2, 1, 1)
)
fadcDeviceFanEntry.setIndexNames(
    (0, "FORTINET-FORTIWAN-MIB", "fadcDeviceFanIndex"),
)
if mibBuilder.loadTexts:
    fadcDeviceFanEntry.setStatus("current")
_FadcDeviceFanIndex_Type = Integer32
_FadcDeviceFanIndex_Object = MibTableColumn
fadcDeviceFanIndex = _FadcDeviceFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 4, 2, 1, 1, 1),
    _FadcDeviceFanIndex_Type()
)
fadcDeviceFanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcDeviceFanIndex.setStatus("current")
_FadcDeviceFanName_Type = DisplayString
_FadcDeviceFanName_Object = MibTableColumn
fadcDeviceFanName = _FadcDeviceFanName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 4, 2, 1, 1, 2),
    _FadcDeviceFanName_Type()
)
fadcDeviceFanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcDeviceFanName.setStatus("current")
_FadcDeviceFanSpeed_Type = Integer32
_FadcDeviceFanSpeed_Object = MibTableColumn
fadcDeviceFanSpeed = _FadcDeviceFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 4, 2, 1, 1, 3),
    _FadcDeviceFanSpeed_Type()
)
fadcDeviceFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcDeviceFanSpeed.setStatus("current")
_FadcDeviceFanStatus_Type = DisplayString
_FadcDeviceFanStatus_Object = MibTableColumn
fadcDeviceFanStatus = _FadcDeviceFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 4, 2, 1, 1, 4),
    _FadcDeviceFanStatus_Type()
)
fadcDeviceFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcDeviceFanStatus.setStatus("current")
_FadcHA_ObjectIdentity = ObjectIdentity
fadcHA = _FadcHA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 5)
)
_FadcHACurMode_Type = FnHAModeVal
_FadcHACurMode_Object = MibScalar
fadcHACurMode = _FadcHACurMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 5, 1),
    _FadcHACurMode_Type()
)
fadcHACurMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcHACurMode.setStatus("current")
_FadcHACurState_Type = DisplayString
_FadcHACurState_Object = MibScalar
fadcHACurState = _FadcHACurState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 5, 2),
    _FadcHACurState_Type()
)
fadcHACurState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcHACurState.setStatus("current")
_FadcHAPeerCount_Type = Integer32
_FadcHAPeerCount_Object = MibScalar
fadcHAPeerCount = _FadcHAPeerCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 5, 3),
    _FadcHAPeerCount_Type()
)
fadcHAPeerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcHAPeerCount.setStatus("current")
_FadcMoniterIntfCount_Type = Integer32
_FadcMoniterIntfCount_Object = MibScalar
fadcMoniterIntfCount = _FadcMoniterIntfCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 5, 4),
    _FadcMoniterIntfCount_Type()
)
fadcMoniterIntfCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcMoniterIntfCount.setStatus("current")
_FadcDiskState_Type = Integer32
_FadcDiskState_Object = MibScalar
fadcDiskState = _FadcDiskState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 5, 5),
    _FadcDiskState_Type()
)
fadcDiskState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcDiskState.setStatus("current")
_FadcHALastChangedTime_Type = DisplayString
_FadcHALastChangedTime_Object = MibScalar
fadcHALastChangedTime = _FadcHALastChangedTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 5, 6),
    _FadcHALastChangedTime_Type()
)
fadcHALastChangedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcHALastChangedTime.setStatus("current")
_FadcHALastChangedReason_Type = DisplayString
_FadcHALastChangedReason_Object = MibScalar
fadcHALastChangedReason = _FadcHALastChangedReason_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 5, 7),
    _FadcHALastChangedReason_Type()
)
fadcHALastChangedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcHALastChangedReason.setStatus("current")
_FadcSyncStats_ObjectIdentity = ObjectIdentity
fadcSyncStats = _FadcSyncStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 5, 20)
)
_FadcHASyncStatsTable_Object = MibTable
fadcHASyncStatsTable = _FadcHASyncStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 5, 20, 1)
)
if mibBuilder.loadTexts:
    fadcHASyncStatsTable.setStatus("current")
_FadcHASyncStatsEntry_Object = MibTableRow
fadcHASyncStatsEntry = _FadcHASyncStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 5, 20, 1, 1)
)
fadcHASyncStatsEntry.setIndexNames(
    (0, "FORTINET-FORTIWAN-MIB", "fadcSyncTypeIndex"),
)
if mibBuilder.loadTexts:
    fadcHASyncStatsEntry.setStatus("current")


class _FadcSyncTypeIndex_Type(Integer32):
    """Custom type fadcSyncTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcSyncTypeIndex_Type.__name__ = "Integer32"
_FadcSyncTypeIndex_Object = MibTableColumn
fadcSyncTypeIndex = _FadcSyncTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 5, 20, 1, 1, 1),
    _FadcSyncTypeIndex_Type()
)
fadcSyncTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcSyncTypeIndex.setStatus("current")
_FadcSyncType_Type = DisplayString
_FadcSyncType_Object = MibTableColumn
fadcSyncType = _FadcSyncType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 5, 20, 1, 1, 2),
    _FadcSyncType_Type()
)
fadcSyncType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcSyncType.setStatus("current")
_FadcSyncSent_Type = Integer32
_FadcSyncSent_Object = MibTableColumn
fadcSyncSent = _FadcSyncSent_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 5, 20, 1, 1, 3),
    _FadcSyncSent_Type()
)
fadcSyncSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcSyncSent.setStatus("current")
_FadcSyncReceived_Type = Integer32
_FadcSyncReceived_Object = MibTableColumn
fadcSyncReceived = _FadcSyncReceived_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 5, 20, 1, 1, 4),
    _FadcSyncReceived_Type()
)
fadcSyncReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcSyncReceived.setStatus("current")
_FadcDeviceErrCount_ObjectIdentity = ObjectIdentity
fadcDeviceErrCount = _FadcDeviceErrCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 5, 21)
)
_FadcDuplicateNodeID_Type = Integer32
_FadcDuplicateNodeID_Object = MibScalar
fadcDuplicateNodeID = _FadcDuplicateNodeID_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 5, 21, 1),
    _FadcDuplicateNodeID_Type()
)
fadcDuplicateNodeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcDuplicateNodeID.setStatus("current")
_FadcVersionMismatch_Type = Integer32
_FadcVersionMismatch_Object = MibScalar
fadcVersionMismatch = _FadcVersionMismatch_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 5, 21, 2),
    _FadcVersionMismatch_Type()
)
fadcVersionMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVersionMismatch.setStatus("current")
_FadcHAPeerInfo_ObjectIdentity = ObjectIdentity
fadcHAPeerInfo = _FadcHAPeerInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 5, 22)
)
_FadcHAPeerTable_Object = MibTable
fadcHAPeerTable = _FadcHAPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 5, 22, 1)
)
if mibBuilder.loadTexts:
    fadcHAPeerTable.setStatus("current")
_FadcHAPeerEntry_Object = MibTableRow
fadcHAPeerEntry = _FadcHAPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 5, 22, 1, 1)
)
fadcHAPeerEntry.setIndexNames(
    (0, "FORTINET-FORTIWAN-MIB", "fadcHAPeerIndex"),
)
if mibBuilder.loadTexts:
    fadcHAPeerEntry.setStatus("current")


class _FadcPeerIndex_Type(Integer32):
    """Custom type fadcPeerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcPeerIndex_Type.__name__ = "Integer32"
_FadcPeerIndex_Object = MibTableColumn
fadcPeerIndex = _FadcPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 5, 22, 1, 1, 1),
    _FadcPeerIndex_Type()
)
fadcPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcPeerIndex.setStatus("current")
_FadcPeerSerialNumber_Type = DisplayString
_FadcPeerSerialNumber_Object = MibTableColumn
fadcPeerSerialNumber = _FadcPeerSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 5, 22, 1, 1, 2),
    _FadcPeerSerialNumber_Type()
)
fadcPeerSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcPeerSerialNumber.setStatus("current")
_FadcPeerStatus_Type = DisplayString
_FadcPeerStatus_Object = MibTableColumn
fadcPeerStatus = _FadcPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 5, 22, 1, 1, 3),
    _FadcPeerStatus_Type()
)
fadcPeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcPeerStatus.setStatus("current")
_FadcNodeID_Type = Integer32
_FadcNodeID_Object = MibTableColumn
fadcNodeID = _FadcNodeID_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 5, 22, 1, 1, 4),
    _FadcNodeID_Type()
)
fadcNodeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcNodeID.setStatus("current")
_FadcIPAddress_Type = DisplayString
_FadcIPAddress_Object = MibTableColumn
fadcIPAddress = _FadcIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 5, 22, 1, 1, 5),
    _FadcIPAddress_Type()
)
fadcIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcIPAddress.setStatus("current")
_FadcVoltage_Type = Integer32
_FadcVoltage_Object = MibScalar
fadcVoltage = _FadcVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 6),
    _FadcVoltage_Type()
)
fadcVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVoltage.setStatus("current")
_FadcPowerSupplyVoltage_Type = Integer32
_FadcPowerSupplyVoltage_Object = MibScalar
fadcPowerSupplyVoltage = _FadcPowerSupplyVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 7),
    _FadcPowerSupplyVoltage_Type()
)
fadcPowerSupplyVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcPowerSupplyVoltage.setStatus("current")
_FadcLogDiskStatus_Type = Integer32
_FadcLogDiskStatus_Object = MibScalar
fadcLogDiskStatus = _FadcLogDiskStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 6, 8),
    _FadcLogDiskStatus_Type()
)
fadcLogDiskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcLogDiskStatus.setStatus("current")
_FadcSecurity_ObjectIdentity = ObjectIdentity
fadcSecurity = _FadcSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 7)
)
_FadcDDoSAttackStatus_Type = Gauge32
_FadcDDoSAttackStatus_Object = MibScalar
fadcDDoSAttackStatus = _FadcDDoSAttackStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 7, 1),
    _FadcDDoSAttackStatus_Type()
)
fadcDDoSAttackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcDDoSAttackStatus.setStatus("current")
_FadcApplication_ObjectIdentity = ObjectIdentity
fadcApplication = _FadcApplication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8)
)
_FadcRS_ObjectIdentity = ObjectIdentity
fadcRS = _FadcRS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 1)
)
_FadcPoolNumber_Type = Integer32
_FadcPoolNumber_Object = MibScalar
fadcPoolNumber = _FadcPoolNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 1, 1),
    _FadcPoolNumber_Type()
)
fadcPoolNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcPoolNumber.setStatus("current")
_FadcRSNumber_Type = Integer32
_FadcRSNumber_Object = MibScalar
fadcRSNumber = _FadcRSNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 1, 2),
    _FadcRSNumber_Type()
)
fadcRSNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcRSNumber.setStatus("current")
_FadcRSTable_Object = MibTable
fadcRSTable = _FadcRSTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 1, 3)
)
if mibBuilder.loadTexts:
    fadcRSTable.setStatus("current")
_FadcRSEntry_Object = MibTableRow
fadcRSEntry = _FadcRSEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 1, 3, 1)
)
fadcRSEntry.setIndexNames(
    (0, "FORTINET-FORTIWAN-MIB", "fadcRSIndex"),
)
if mibBuilder.loadTexts:
    fadcRSEntry.setStatus("current")


class _FadcRSIndex_Type(Integer32):
    """Custom type fadcRSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcRSIndex_Type.__name__ = "Integer32"
_FadcRSIndex_Object = MibTableColumn
fadcRSIndex = _FadcRSIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 1, 3, 1, 1),
    _FadcRSIndex_Type()
)
fadcRSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcRSIndex.setStatus("current")
_FadcPoolName_Type = DisplayString
_FadcPoolName_Object = MibTableColumn
fadcPoolName = _FadcPoolName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 1, 3, 1, 2),
    _FadcPoolName_Type()
)
fadcPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcPoolName.setStatus("current")
_FadcRSStatus_Type = DisplayString
_FadcRSStatus_Object = MibTableColumn
fadcRSStatus = _FadcRSStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 1, 3, 1, 3),
    _FadcRSStatus_Type()
)
fadcRSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcRSStatus.setStatus("current")
_FadcRSHealth_Type = DisplayString
_FadcRSHealth_Object = MibTableColumn
fadcRSHealth = _FadcRSHealth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 1, 3, 1, 4),
    _FadcRSHealth_Type()
)
fadcRSHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcRSHealth.setStatus("current")
_FadcRSVdom_Type = DisplayString
_FadcRSVdom_Object = MibTableColumn
fadcRSVdom = _FadcRSVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 1, 3, 1, 5),
    _FadcRSVdom_Type()
)
fadcRSVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcRSVdom.setStatus("current")
_FadcVS_ObjectIdentity = ObjectIdentity
fadcVS = _FadcVS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 2)
)
_FadcVirturalServerNumber_Type = Integer32
_FadcVirturalServerNumber_Object = MibScalar
fadcVirturalServerNumber = _FadcVirturalServerNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 2, 1),
    _FadcVirturalServerNumber_Type()
)
fadcVirturalServerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVirturalServerNumber.setStatus("current")
_FadcVirturalServerTable_Object = MibTable
fadcVirturalServerTable = _FadcVirturalServerTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 2, 2)
)
if mibBuilder.loadTexts:
    fadcVirturalServerTable.setStatus("current")
_FadcVirturalServerEntry_Object = MibTableRow
fadcVirturalServerEntry = _FadcVirturalServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 2, 2, 1)
)
fadcVirturalServerEntry.setIndexNames(
    (0, "FORTINET-FORTIWAN-MIB", "fadcVirturalServerIndex"),
)
if mibBuilder.loadTexts:
    fadcVirturalServerEntry.setStatus("current")


class _FadcVirturalServerIndex_Type(Integer32):
    """Custom type fadcVirturalServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcVirturalServerIndex_Type.__name__ = "Integer32"
_FadcVirturalServerIndex_Object = MibTableColumn
fadcVirturalServerIndex = _FadcVirturalServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 2, 2, 1, 1),
    _FadcVirturalServerIndex_Type()
)
fadcVirturalServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcVirturalServerIndex.setStatus("current")
_FadcVirturalServerName_Type = DisplayString
_FadcVirturalServerName_Object = MibTableColumn
fadcVirturalServerName = _FadcVirturalServerName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 2, 2, 1, 2),
    _FadcVirturalServerName_Type()
)
fadcVirturalServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVirturalServerName.setStatus("current")
_FadcVirturalServerStatus_Type = DisplayString
_FadcVirturalServerStatus_Object = MibTableColumn
fadcVirturalServerStatus = _FadcVirturalServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 2, 2, 1, 3),
    _FadcVirturalServerStatus_Type()
)
fadcVirturalServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVirturalServerStatus.setStatus("current")
_FadcVirturalServerHealth_Type = DisplayString
_FadcVirturalServerHealth_Object = MibTableColumn
fadcVirturalServerHealth = _FadcVirturalServerHealth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 2, 2, 1, 4),
    _FadcVirturalServerHealth_Type()
)
fadcVirturalServerHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVirturalServerHealth.setStatus("current")


class _FadcVirturalServerNewConnections_Type(Integer32):
    """Custom type fadcVirturalServerNewConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcVirturalServerNewConnections_Type.__name__ = "Integer32"
_FadcVirturalServerNewConnections_Object = MibTableColumn
fadcVirturalServerNewConnections = _FadcVirturalServerNewConnections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 2, 2, 1, 5),
    _FadcVirturalServerNewConnections_Type()
)
fadcVirturalServerNewConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVirturalServerNewConnections.setStatus("current")


class _FadcVirturalServerConcurrent_Type(Integer32):
    """Custom type fadcVirturalServerConcurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcVirturalServerConcurrent_Type.__name__ = "Integer32"
_FadcVirturalServerConcurrent_Object = MibTableColumn
fadcVirturalServerConcurrent = _FadcVirturalServerConcurrent_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 2, 2, 1, 6),
    _FadcVirturalServerConcurrent_Type()
)
fadcVirturalServerConcurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVirturalServerConcurrent.setStatus("current")


class _FadcVirturalServerThroughput_Kbps_Type(Integer32):
    """Custom type fadcVirturalServerThroughput_Kbps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcVirturalServerThroughput_Kbps_Type.__name__ = "Integer32"
_FadcVirturalServerThroughput_Kbps_Object = MibTableColumn
fadcVirturalServerThroughput_Kbps = _FadcVirturalServerThroughput_Kbps_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 2, 2, 1, 7),
    _FadcVirturalServerThroughput_Kbps_Type()
)
fadcVirturalServerThroughput_Kbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVirturalServerThroughput_Kbps.setStatus("current")
_FadcVirturalServerVdom_Type = DisplayString
_FadcVirturalServerVdom_Object = MibTableColumn
fadcVirturalServerVdom = _FadcVirturalServerVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 2, 2, 1, 8),
    _FadcVirturalServerVdom_Type()
)
fadcVirturalServerVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVirturalServerVdom.setStatus("current")


class _FadcVirturalServerWAF_Type(Integer32):
    """Custom type fadcVirturalServerWAF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcVirturalServerWAF_Type.__name__ = "Integer32"
_FadcVirturalServerWAF_Object = MibTableColumn
fadcVirturalServerWAF = _FadcVirturalServerWAF_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 2, 2, 1, 9),
    _FadcVirturalServerWAF_Type()
)
fadcVirturalServerWAF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcVirturalServerWAF.setStatus("current")
_FadcLinkLoadBalance_ObjectIdentity = ObjectIdentity
fadcLinkLoadBalance = _FadcLinkLoadBalance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 3)
)
_FadcGatewayTables_ObjectIdentity = ObjectIdentity
fadcGatewayTables = _FadcGatewayTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 3, 1)
)
_FadcGatewayTable_Object = MibTable
fadcGatewayTable = _FadcGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 3, 1, 1)
)
if mibBuilder.loadTexts:
    fadcGatewayTable.setStatus("current")
_FadcGatewayEntry_Object = MibTableRow
fadcGatewayEntry = _FadcGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 3, 1, 1, 1)
)
fadcGatewayEntry.setIndexNames(
    (0, "FORTINET-FORTIWAN-MIB", "fadcGatewayIndex"),
)
if mibBuilder.loadTexts:
    fadcGatewayEntry.setStatus("current")


class _FadcGatewayIndex_Type(Integer32):
    """Custom type fadcGatewayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcGatewayIndex_Type.__name__ = "Integer32"
_FadcGatewayIndex_Object = MibTableColumn
fadcGatewayIndex = _FadcGatewayIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 3, 1, 1, 1, 1),
    _FadcGatewayIndex_Type()
)
fadcGatewayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcGatewayIndex.setStatus("current")
_FadcGatewayName_Type = DisplayString
_FadcGatewayName_Object = MibTableColumn
fadcGatewayName = _FadcGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 3, 1, 1, 1, 2),
    _FadcGatewayName_Type()
)
fadcGatewayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcGatewayName.setStatus("current")
_FadcGatewayHCStatus_Type = DisplayString
_FadcGatewayHCStatus_Object = MibTableColumn
fadcGatewayHCStatus = _FadcGatewayHCStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 3, 1, 1, 1, 3),
    _FadcGatewayHCStatus_Type()
)
fadcGatewayHCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcGatewayHCStatus.setStatus("current")
_FadcGatewayInboundBandWidth_Type = DisplayString
_FadcGatewayInboundBandWidth_Object = MibTableColumn
fadcGatewayInboundBandWidth = _FadcGatewayInboundBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 3, 1, 1, 1, 4),
    _FadcGatewayInboundBandWidth_Type()
)
fadcGatewayInboundBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcGatewayInboundBandWidth.setStatus("current")
_FadcGatewayOutboundBandWidth_Type = DisplayString
_FadcGatewayOutboundBandWidth_Object = MibTableColumn
fadcGatewayOutboundBandWidth = _FadcGatewayOutboundBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 3, 1, 1, 1, 5),
    _FadcGatewayOutboundBandWidth_Type()
)
fadcGatewayOutboundBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcGatewayOutboundBandWidth.setStatus("current")
_FadcGatewayVdom_Type = DisplayString
_FadcGatewayVdom_Object = MibTableColumn
fadcGatewayVdom = _FadcGatewayVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 3, 1, 1, 1, 6),
    _FadcGatewayVdom_Type()
)
fadcGatewayVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcGatewayVdom.setStatus("current")
_FadcLinkGroupTables_ObjectIdentity = ObjectIdentity
fadcLinkGroupTables = _FadcLinkGroupTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 3, 2)
)
_FadcLinkGroupTable_Object = MibTable
fadcLinkGroupTable = _FadcLinkGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 3, 2, 1)
)
if mibBuilder.loadTexts:
    fadcLinkGroupTable.setStatus("current")
_FadcLinkGroupEntry_Object = MibTableRow
fadcLinkGroupEntry = _FadcLinkGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 3, 2, 1, 1)
)
fadcLinkGroupEntry.setIndexNames(
    (0, "FORTINET-FORTIWAN-MIB", "fadcLinkGroupIndex"),
)
if mibBuilder.loadTexts:
    fadcLinkGroupEntry.setStatus("current")


class _FadcLinkGroupIndex_Type(Integer32):
    """Custom type fadcLinkGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcLinkGroupIndex_Type.__name__ = "Integer32"
_FadcLinkGroupIndex_Object = MibTableColumn
fadcLinkGroupIndex = _FadcLinkGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 3, 2, 1, 1, 1),
    _FadcLinkGroupIndex_Type()
)
fadcLinkGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcLinkGroupIndex.setStatus("current")
_FadcLinkGroupName_Type = DisplayString
_FadcLinkGroupName_Object = MibTableColumn
fadcLinkGroupName = _FadcLinkGroupName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 3, 2, 1, 1, 2),
    _FadcLinkGroupName_Type()
)
fadcLinkGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcLinkGroupName.setStatus("current")
_FadcLinkGroupHCStatus_Type = DisplayString
_FadcLinkGroupHCStatus_Object = MibTableColumn
fadcLinkGroupHCStatus = _FadcLinkGroupHCStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 3, 2, 1, 1, 3),
    _FadcLinkGroupHCStatus_Type()
)
fadcLinkGroupHCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcLinkGroupHCStatus.setStatus("current")
_FadcLinkGroupMode_Type = DisplayString
_FadcLinkGroupMode_Object = MibTableColumn
fadcLinkGroupMode = _FadcLinkGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 3, 2, 1, 1, 4),
    _FadcLinkGroupMode_Type()
)
fadcLinkGroupMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcLinkGroupMode.setStatus("current")
_FadcLinkGroupVdom_Type = DisplayString
_FadcLinkGroupVdom_Object = MibTableColumn
fadcLinkGroupVdom = _FadcLinkGroupVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 3, 2, 1, 1, 5),
    _FadcLinkGroupVdom_Type()
)
fadcLinkGroupVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcLinkGroupVdom.setStatus("current")
_FadcGlobalLoadBalance_ObjectIdentity = ObjectIdentity
fadcGlobalLoadBalance = _FadcGlobalLoadBalance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 4)
)
_FadcGLBVSTables_ObjectIdentity = ObjectIdentity
fadcGLBVSTables = _FadcGLBVSTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 4, 1)
)
_FadcGLBVSTable_Object = MibTable
fadcGLBVSTable = _FadcGLBVSTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 4, 1, 1)
)
if mibBuilder.loadTexts:
    fadcGLBVSTable.setStatus("current")
_FadcGLBVSEntry_Object = MibTableRow
fadcGLBVSEntry = _FadcGLBVSEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 4, 1, 1, 1)
)
fadcGLBVSEntry.setIndexNames(
    (0, "FORTINET-FORTIWAN-MIB", "fadcGLBVSIndex"),
)
if mibBuilder.loadTexts:
    fadcGLBVSEntry.setStatus("current")


class _FadcGLBVSIndex_Type(Integer32):
    """Custom type fadcGLBVSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcGLBVSIndex_Type.__name__ = "Integer32"
_FadcGLBVSIndex_Object = MibTableColumn
fadcGLBVSIndex = _FadcGLBVSIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 4, 1, 1, 1, 1),
    _FadcGLBVSIndex_Type()
)
fadcGLBVSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcGLBVSIndex.setStatus("current")
_FadcGLBVSName_Type = DisplayString
_FadcGLBVSName_Object = MibTableColumn
fadcGLBVSName = _FadcGLBVSName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 4, 1, 1, 1, 2),
    _FadcGLBVSName_Type()
)
fadcGLBVSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcGLBVSName.setStatus("current")
_FadcGLBVSStatus_Type = DisplayString
_FadcGLBVSStatus_Object = MibTableColumn
fadcGLBVSStatus = _FadcGLBVSStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 4, 1, 1, 1, 3),
    _FadcGLBVSStatus_Type()
)
fadcGLBVSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcGLBVSStatus.setStatus("current")
_FadcGLBVSServerName_Type = DisplayString
_FadcGLBVSServerName_Object = MibTableColumn
fadcGLBVSServerName = _FadcGLBVSServerName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 4, 1, 1, 1, 4),
    _FadcGLBVSServerName_Type()
)
fadcGLBVSServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcGLBVSServerName.setStatus("current")
_FadcGLBVSVdom_Type = DisplayString
_FadcGLBVSVdom_Object = MibTableColumn
fadcGLBVSVdom = _FadcGLBVSVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 4, 1, 1, 1, 5),
    _FadcGLBVSVdom_Type()
)
fadcGLBVSVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcGLBVSVdom.setStatus("current")
_FadcGLBServerTables_ObjectIdentity = ObjectIdentity
fadcGLBServerTables = _FadcGLBServerTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 4, 2)
)
_FadcGLBServerTable_Object = MibTable
fadcGLBServerTable = _FadcGLBServerTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 4, 2, 1)
)
if mibBuilder.loadTexts:
    fadcGLBServerTable.setStatus("current")
_FadcGLBServerEntry_Object = MibTableRow
fadcGLBServerEntry = _FadcGLBServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 4, 2, 1, 1)
)
fadcGLBServerEntry.setIndexNames(
    (0, "FORTINET-FORTIWAN-MIB", "fadcGLBServerIndex"),
)
if mibBuilder.loadTexts:
    fadcGLBServerEntry.setStatus("current")


class _FadcGLBServerIndex_Type(Integer32):
    """Custom type fadcGLBServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcGLBServerIndex_Type.__name__ = "Integer32"
_FadcGLBServerIndex_Object = MibTableColumn
fadcGLBServerIndex = _FadcGLBServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 4, 2, 1, 1, 1),
    _FadcGLBServerIndex_Type()
)
fadcGLBServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcGLBServerIndex.setStatus("current")
_FadcGLBServerName_Type = DisplayString
_FadcGLBServerName_Object = MibTableColumn
fadcGLBServerName = _FadcGLBServerName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 4, 2, 1, 1, 2),
    _FadcGLBServerName_Type()
)
fadcGLBServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcGLBServerName.setStatus("current")
_FadcGLBServerStatus_Type = DisplayString
_FadcGLBServerStatus_Object = MibTableColumn
fadcGLBServerStatus = _FadcGLBServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 4, 2, 1, 1, 3),
    _FadcGLBServerStatus_Type()
)
fadcGLBServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcGLBServerStatus.setStatus("current")
_FadcGLBServerVdom_Type = DisplayString
_FadcGLBServerVdom_Object = MibTableColumn
fadcGLBServerVdom = _FadcGLBServerVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 4, 2, 1, 1, 4),
    _FadcGLBServerVdom_Type()
)
fadcGLBServerVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcGLBServerVdom.setStatus("current")
_FadcGLBGatewayTables_ObjectIdentity = ObjectIdentity
fadcGLBGatewayTables = _FadcGLBGatewayTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 4, 3)
)
_FadcGLBGatewayTable_Object = MibTable
fadcGLBGatewayTable = _FadcGLBGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 4, 3, 1)
)
if mibBuilder.loadTexts:
    fadcGLBGatewayTable.setStatus("current")
_FadcGLBGatewayEntry_Object = MibTableRow
fadcGLBGatewayEntry = _FadcGLBGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 4, 3, 1, 1)
)
fadcGLBGatewayEntry.setIndexNames(
    (0, "FORTINET-FORTIWAN-MIB", "fadcGLBGatewayIndex"),
)
if mibBuilder.loadTexts:
    fadcGLBGatewayEntry.setStatus("current")


class _FadcGLBGatewayIndex_Type(Integer32):
    """Custom type fadcGLBGatewayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcGLBGatewayIndex_Type.__name__ = "Integer32"
_FadcGLBGatewayIndex_Object = MibTableColumn
fadcGLBGatewayIndex = _FadcGLBGatewayIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 4, 3, 1, 1, 1),
    _FadcGLBGatewayIndex_Type()
)
fadcGLBGatewayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcGLBGatewayIndex.setStatus("current")
_FadcGLBGatewayName_Type = DisplayString
_FadcGLBGatewayName_Object = MibTableColumn
fadcGLBGatewayName = _FadcGLBGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 4, 3, 1, 1, 2),
    _FadcGLBGatewayName_Type()
)
fadcGLBGatewayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcGLBGatewayName.setStatus("current")
_FadcGLBGatewayStatus_Type = DisplayString
_FadcGLBGatewayStatus_Object = MibTableColumn
fadcGLBGatewayStatus = _FadcGLBGatewayStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 4, 3, 1, 1, 3),
    _FadcGLBGatewayStatus_Type()
)
fadcGLBGatewayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcGLBGatewayStatus.setStatus("current")
_FadcGLBGatewayServerName_Type = DisplayString
_FadcGLBGatewayServerName_Object = MibTableColumn
fadcGLBGatewayServerName = _FadcGLBGatewayServerName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 4, 3, 1, 1, 4),
    _FadcGLBGatewayServerName_Type()
)
fadcGLBGatewayServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcGLBGatewayServerName.setStatus("current")
_FadcGLBGatewayVdom_Type = DisplayString
_FadcGLBGatewayVdom_Object = MibTableColumn
fadcGLBGatewayVdom = _FadcGLBGatewayVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 4, 3, 1, 1, 5),
    _FadcGLBGatewayVdom_Type()
)
fadcGLBGatewayVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcGLBGatewayVdom.setStatus("current")
_FadcServerLoadBalance_ObjectIdentity = ObjectIdentity
fadcServerLoadBalance = _FadcServerLoadBalance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 5)
)


class _FadcClientSideCPS_Type(Integer32):
    """Custom type fadcClientSideCPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcClientSideCPS_Type.__name__ = "Integer32"
_FadcClientSideCPS_Object = MibScalar
fadcClientSideCPS = _FadcClientSideCPS_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 5, 1),
    _FadcClientSideCPS_Type()
)
fadcClientSideCPS.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcClientSideCPS.setStatus("current")


class _FadcClientSideRPS_Type(Integer32):
    """Custom type fadcClientSideRPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcClientSideRPS_Type.__name__ = "Integer32"
_FadcClientSideRPS_Object = MibScalar
fadcClientSideRPS = _FadcClientSideRPS_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 5, 2),
    _FadcClientSideRPS_Type()
)
fadcClientSideRPS.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcClientSideRPS.setStatus("current")


class _FadcClientSideSSLCPS_Type(Integer32):
    """Custom type fadcClientSideSSLCPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcClientSideSSLCPS_Type.__name__ = "Integer32"
_FadcClientSideSSLCPS_Object = MibScalar
fadcClientSideSSLCPS = _FadcClientSideSSLCPS_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 5, 3),
    _FadcClientSideSSLCPS_Type()
)
fadcClientSideSSLCPS.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcClientSideSSLCPS.setStatus("current")


class _FadcClientSideSSLRPS_Type(Integer32):
    """Custom type fadcClientSideSSLRPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcClientSideSSLRPS_Type.__name__ = "Integer32"
_FadcClientSideSSLRPS_Object = MibScalar
fadcClientSideSSLRPS = _FadcClientSideSSLRPS_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 5, 4),
    _FadcClientSideSSLRPS_Type()
)
fadcClientSideSSLRPS.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcClientSideSSLRPS.setStatus("current")


class _FadcClientSideThroughput_Type(Integer32):
    """Custom type fadcClientSideThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcClientSideThroughput_Type.__name__ = "Integer32"
_FadcClientSideThroughput_Object = MibScalar
fadcClientSideThroughput = _FadcClientSideThroughput_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 5, 5),
    _FadcClientSideThroughput_Type()
)
fadcClientSideThroughput.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcClientSideThroughput.setStatus("current")


class _FadcClientSideSSLThroughput_Type(Integer32):
    """Custom type fadcClientSideSSLThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcClientSideSSLThroughput_Type.__name__ = "Integer32"
_FadcClientSideSSLThroughput_Object = MibScalar
fadcClientSideSSLThroughput = _FadcClientSideSSLThroughput_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 5, 6),
    _FadcClientSideSSLThroughput_Type()
)
fadcClientSideSSLThroughput.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcClientSideSSLThroughput.setStatus("current")


class _FadcConcurrentClientSideConnections_Type(Integer32):
    """Custom type fadcConcurrentClientSideConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcConcurrentClientSideConnections_Type.__name__ = "Integer32"
_FadcConcurrentClientSideConnections_Object = MibScalar
fadcConcurrentClientSideConnections = _FadcConcurrentClientSideConnections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 5, 7),
    _FadcConcurrentClientSideConnections_Type()
)
fadcConcurrentClientSideConnections.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcConcurrentClientSideConnections.setStatus("current")


class _FadcConcurrentClientSideSSLSessions_Type(Integer32):
    """Custom type fadcConcurrentClientSideSSLSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcConcurrentClientSideSSLSessions_Type.__name__ = "Integer32"
_FadcConcurrentClientSideSSLSessions_Object = MibScalar
fadcConcurrentClientSideSSLSessions = _FadcConcurrentClientSideSSLSessions_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 5, 8),
    _FadcConcurrentClientSideSSLSessions_Type()
)
fadcConcurrentClientSideSSLSessions.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcConcurrentClientSideSSLSessions.setStatus("current")
_FadcClientSSLCacheUtilizationTables_ObjectIdentity = ObjectIdentity
fadcClientSSLCacheUtilizationTables = _FadcClientSSLCacheUtilizationTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 5, 20)
)
_FadcClientSSLCacheUtilizationTable_Object = MibTable
fadcClientSSLCacheUtilizationTable = _FadcClientSSLCacheUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 5, 20, 1)
)
if mibBuilder.loadTexts:
    fadcClientSSLCacheUtilizationTable.setStatus("current")
_FadcClientSSLCacheUtilizationEntry_Object = MibTableRow
fadcClientSSLCacheUtilizationEntry = _FadcClientSSLCacheUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 5, 20, 1, 1)
)
fadcClientSSLCacheUtilizationEntry.setIndexNames(
    (0, "FORTINET-FORTIWAN-MIB", "fadcSLBVSIndex"),
)
if mibBuilder.loadTexts:
    fadcClientSSLCacheUtilizationEntry.setStatus("current")


class _FadcSLBVSIndex_Type(Integer32):
    """Custom type fadcSLBVSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcSLBVSIndex_Type.__name__ = "Integer32"
_FadcSLBVSIndex_Object = MibTableColumn
fadcSLBVSIndex = _FadcSLBVSIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 5, 20, 1, 1, 1),
    _FadcSLBVSIndex_Type()
)
fadcSLBVSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fadcSLBVSIndex.setStatus("current")
_FadcSLBVSName_Type = DisplayString
_FadcSLBVSName_Object = MibTableColumn
fadcSLBVSName = _FadcSLBVSName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 5, 20, 1, 1, 2),
    _FadcSLBVSName_Type()
)
fadcSLBVSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcSLBVSName.setStatus("current")


class _FadcSLBTotalCacheItems_Type(Integer32):
    """Custom type fadcSLBTotalCacheItems based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcSLBTotalCacheItems_Type.__name__ = "Integer32"
_FadcSLBTotalCacheItems_Object = MibTableColumn
fadcSLBTotalCacheItems = _FadcSLBTotalCacheItems_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 5, 20, 1, 1, 3),
    _FadcSLBTotalCacheItems_Type()
)
fadcSLBTotalCacheItems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcSLBTotalCacheItems.setStatus("current")


class _FadcSLBTotalCacheSize_Type(Integer32):
    """Custom type fadcSLBTotalCacheSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcSLBTotalCacheSize_Type.__name__ = "Integer32"
_FadcSLBTotalCacheSize_Object = MibTableColumn
fadcSLBTotalCacheSize = _FadcSLBTotalCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 5, 20, 1, 1, 4),
    _FadcSLBTotalCacheSize_Type()
)
fadcSLBTotalCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcSLBTotalCacheSize.setStatus("current")


class _FadcSLBCacheHitCount_Type(Integer32):
    """Custom type fadcSLBCacheHitCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcSLBCacheHitCount_Type.__name__ = "Integer32"
_FadcSLBCacheHitCount_Object = MibTableColumn
fadcSLBCacheHitCount = _FadcSLBCacheHitCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 5, 20, 1, 1, 5),
    _FadcSLBCacheHitCount_Type()
)
fadcSLBCacheHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcSLBCacheHitCount.setStatus("current")


class _FadcSLBCacheHitBytes_Type(Integer32):
    """Custom type fadcSLBCacheHitBytes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcSLBCacheHitBytes_Type.__name__ = "Integer32"
_FadcSLBCacheHitBytes_Object = MibTableColumn
fadcSLBCacheHitBytes = _FadcSLBCacheHitBytes_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 5, 20, 1, 1, 6),
    _FadcSLBCacheHitBytes_Type()
)
fadcSLBCacheHitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcSLBCacheHitBytes.setStatus("current")


class _FadcSLBTatalCertCacheItems_Type(Integer32):
    """Custom type fadcSLBTatalCertCacheItems based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcSLBTatalCertCacheItems_Type.__name__ = "Integer32"
_FadcSLBTatalCertCacheItems_Object = MibTableColumn
fadcSLBTatalCertCacheItems = _FadcSLBTatalCertCacheItems_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 5, 20, 1, 1, 7),
    _FadcSLBTatalCertCacheItems_Type()
)
fadcSLBTatalCertCacheItems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcSLBTatalCertCacheItems.setStatus("current")


class _FadcSLBTotalCertCacheSize_Type(Integer32):
    """Custom type fadcSLBTotalCertCacheSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcSLBTotalCertCacheSize_Type.__name__ = "Integer32"
_FadcSLBTotalCertCacheSize_Object = MibTableColumn
fadcSLBTotalCertCacheSize = _FadcSLBTotalCertCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 5, 20, 1, 1, 8),
    _FadcSLBTotalCertCacheSize_Type()
)
fadcSLBTotalCertCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcSLBTotalCertCacheSize.setStatus("current")


class _FadcSLBHitCertCacheCount_Type(Integer32):
    """Custom type fadcSLBHitCertCacheCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcSLBHitCertCacheCount_Type.__name__ = "Integer32"
_FadcSLBHitCertCacheCount_Object = MibTableColumn
fadcSLBHitCertCacheCount = _FadcSLBHitCertCacheCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 5, 20, 1, 1, 9),
    _FadcSLBHitCertCacheCount_Type()
)
fadcSLBHitCertCacheCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcSLBHitCertCacheCount.setStatus("current")


class _FadcSLBHitCertTotalCheck_Type(Integer32):
    """Custom type fadcSLBHitCertTotalCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcSLBHitCertTotalCheck_Type.__name__ = "Integer32"
_FadcSLBHitCertTotalCheck_Object = MibTableColumn
fadcSLBHitCertTotalCheck = _FadcSLBHitCertTotalCheck_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 5, 20, 1, 1, 10),
    _FadcSLBHitCertTotalCheck_Type()
)
fadcSLBHitCertTotalCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcSLBHitCertTotalCheck.setStatus("current")


class _FadcSLBHitCertPercentage_Type(Integer32):
    """Custom type fadcSLBHitCertPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FadcSLBHitCertPercentage_Type.__name__ = "Integer32"
_FadcSLBHitCertPercentage_Object = MibTableColumn
fadcSLBHitCertPercentage = _FadcSLBHitCertPercentage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 118, 8, 5, 20, 1, 1, 11),
    _FadcSLBHitCertPercentage_Type()
)
fadcSLBHitCertPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fadcSLBHitCertPercentage.setStatus("current")
_FadcMIBConformance_ObjectIdentity = ObjectIdentity
fadcMIBConformance = _FadcMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 118, 600)
)

# Managed Objects groups

fwnSystemConformanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 118, 600, 1)
)
fwnSystemConformanceGroup.setObjects(
      *(("FORTINET-FORTIWAN-MIB", "fwnSysModel"),
        ("FORTINET-FORTIWAN-MIB", "fwnSysSerial"),
        ("FORTINET-FORTIWAN-MIB", "fwnSysVersion"),
        ("FORTINET-FORTIWAN-MIB", "fwnSysCpuUsage"),
        ("FORTINET-FORTIWAN-MIB", "fwnSysMemUsage"),
        ("FORTINET-FORTIWAN-MIB", "fwnSysLogDiskUsage"),
        ("FORTINET-FORTIWAN-MIB", "fwnSysLoad"))
)
if mibBuilder.loadTexts:
    fwnSystemConformanceGroup.setStatus("current")

fwnSysOptionsConformanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 118, 600, 2)
)
fwnSysOptionsConformanceGroup.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysOptIdleTimeout")
)
if mibBuilder.loadTexts:
    fwnSysOptionsConformanceGroup.setStatus("current")

fwnHAModeConformanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 118, 600, 6)
)
fwnHAModeConformanceGroup.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnHAMode")
)
if mibBuilder.loadTexts:
    fwnHAModeConformanceGroup.setStatus("current")


# Notification objects

fadcTrapCpuHighThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 101)
)
fadcTrapCpuHighThreshold.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapCpuHighThreshold.setStatus(
        "current"
    )

fadcTrapMemLowThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 102)
)
fadcTrapMemLowThreshold.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapMemLowThreshold.setStatus(
        "current"
    )

fadcTrapLogDiskHighThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 103)
)
fadcTrapLogDiskHighThreshold.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapLogDiskHighThreshold.setStatus(
        "current"
    )

fadcTrapDosAttackStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 401)
)
fadcTrapDosAttackStart.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapDosAttackStart.setStatus(
        "current"
    )

fadcTrapDosAttackStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 402)
)
fadcTrapDosAttackStop.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapDosAttackStop.setStatus(
        "current"
    )

fadcTrapFwConnectionLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 403)
)
fadcTrapFwConnectionLimit.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapFwConnectionLimit.setStatus(
        "current"
    )

fadcTrapFwSnatLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 404)
)
fadcTrapFwSnatLimit.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapFwSnatLimit.setStatus(
        "current"
    )

fadcTrapRequestBlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 405)
)
fadcTrapRequestBlocked.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapRequestBlocked.setStatus(
        "current"
    )

fadcTrapXSSAttackDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 406)
)
fadcTrapXSSAttackDetected.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapXSSAttackDetected.setStatus(
        "current"
    )

fadcTrapSQLInjectionAttackDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 407)
)
fadcTrapSQLInjectionAttackDetected.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapSQLInjectionAttackDetected.setStatus(
        "current"
    )

fadcTrapGenericAttackDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 408)
)
fadcTrapGenericAttackDetected.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapGenericAttackDetected.setStatus(
        "current"
    )

fadcTrapExploitsAttackDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 409)
)
fadcTrapExploitsAttackDetected.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapExploitsAttackDetected.setStatus(
        "current"
    )

fadcTrapTrojansAttackDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 410)
)
fadcTrapTrojansAttackDetected.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapTrojansAttackDetected.setStatus(
        "current"
    )

fadcTrapInfoDisclosureAttackDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 411)
)
fadcTrapInfoDisclosureAttackDetected.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapInfoDisclosureAttackDetected.setStatus(
        "current"
    )

fadcTrapURLPattenViolateDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 412)
)
fadcTrapURLPattenViolateDetected.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapURLPattenViolateDetected.setStatus(
        "current"
    )

fadcTrapProtocolContraintDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 413)
)
fadcTrapProtocolContraintDetected.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapProtocolContraintDetected.setStatus(
        "current"
    )

fadcTrapGeoViolateDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 414)
)
fadcTrapGeoViolateDetected.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapGeoViolateDetected.setStatus(
        "current"
    )

fadcTrapReputaionViolateDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 415)
)
fadcTrapReputaionViolateDetected.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapReputaionViolateDetected.setStatus(
        "current"
    )

fadcTrapCPUTempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 501)
)
fadcTrapCPUTempHigh.setObjects(
      *(("FORTINET-FORTIWAN-MIB", "fwnSysSerial"),
        ("FORTINET-FORTIWAN-MIB", "fadcCPUTempIndex"))
)
if mibBuilder.loadTexts:
    fadcTrapCPUTempHigh.setStatus(
        "current"
    )

fadcTrapCPUTempNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 502)
)
fadcTrapCPUTempNormal.setObjects(
      *(("FORTINET-FORTIWAN-MIB", "fwnSysSerial"),
        ("FORTINET-FORTIWAN-MIB", "fadcCPUTempIndex"))
)
if mibBuilder.loadTexts:
    fadcTrapCPUTempNormal.setStatus(
        "current"
    )

fadcTrapDeviceTempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 503)
)
fadcTrapDeviceTempHigh.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapDeviceTempHigh.setStatus(
        "current"
    )

fadcTrapDeviceTempNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 504)
)
fadcTrapDeviceTempNormal.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapDeviceTempNormal.setStatus(
        "current"
    )

fadcTrapPSUTempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 505)
)
fadcTrapPSUTempHigh.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapPSUTempHigh.setStatus(
        "current"
    )

fadcTrapPSUTempNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 506)
)
fadcTrapPSUTempNormal.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapPSUTempNormal.setStatus(
        "current"
    )

fadcTrapPSUFanSlow = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 507)
)
fadcTrapPSUFanSlow.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapPSUFanSlow.setStatus(
        "current"
    )

fadcTrapDeviceFanSlow = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 508)
)
fadcTrapDeviceFanSlow.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapDeviceFanSlow.setStatus(
        "current"
    )

fadcTrapPSUFanBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 509)
)
fadcTrapPSUFanBad.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapPSUFanBad.setStatus(
        "current"
    )

fadcTrapPSUFanGood = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 510)
)
fadcTrapPSUFanGood.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapPSUFanGood.setStatus(
        "current"
    )

fadcTrapDeviceFanBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 511)
)
fadcTrapDeviceFanBad.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapDeviceFanBad.setStatus(
        "current"
    )

fadcTrapDeviceFanGood = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 512)
)
fadcTrapDeviceFanGood.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapDeviceFanGood.setStatus(
        "current"
    )

fadcTrapVoltageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 513)
)
fadcTrapVoltageHigh.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapVoltageHigh.setStatus(
        "current"
    )

fadcTrapPowerSupplyHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 514)
)
fadcTrapPowerSupplyHigh.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapPowerSupplyHigh.setStatus(
        "current"
    )

fadcTrapPSUVoltageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 515)
)
fadcTrapPSUVoltageHigh.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapPSUVoltageHigh.setStatus(
        "current"
    )

fadcTrapVoltageLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 516)
)
fadcTrapVoltageLow.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapVoltageLow.setStatus(
        "current"
    )

fadcTrapPowerSupplyLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 517)
)
fadcTrapPowerSupplyLow.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapPowerSupplyLow.setStatus(
        "current"
    )

fadcTrapPSUVoltageLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 518)
)
fadcTrapPSUVoltageLow.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapPSUVoltageLow.setStatus(
        "current"
    )

fadcTrapPSUFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 519)
)
fadcTrapPSUFailure.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapPSUFailure.setStatus(
        "current"
    )

fadcTrapARPConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 520)
)
fadcTrapARPConflict.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapARPConflict.setStatus(
        "current"
    )

fadcTrapExternalLinkChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 521)
)
fadcTrapExternalLinkChange.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapExternalLinkChange.setStatus(
        "current"
    )

fadcTrapLogDiskCloseThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 522)
)
fadcTrapLogDiskCloseThreshold.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapLogDiskCloseThreshold.setStatus(
        "current"
    )

fadcTrapLogDiskLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 523)
)
fadcTrapLogDiskLost.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapLogDiskLost.setStatus(
        "current"
    )

fadcTrapSsdMwiNearThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 524)
)
fadcTrapSsdMwiNearThreshold.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapSsdMwiNearThreshold.setStatus(
        "current"
    )

fadcTrapSsdMwiReachedThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 525)
)
fadcTrapSsdMwiReachedThreshold.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapSsdMwiReachedThreshold.setStatus(
        "current"
    )

fadcTrapHAPeerLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 526)
)
fadcTrapHAPeerLost.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapHAPeerLost.setStatus(
        "current"
    )

fadcTrapHAMasterFailover = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 527)
)
fadcTrapHAMasterFailover.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapHAMasterFailover.setStatus(
        "current"
    )

fadcTrapPortStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 528)
)
fadcTrapPortStatusChange.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapPortStatusChange.setStatus(
        "current"
    )

fadcTrapDiskStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 529)
)
fadcTrapDiskStatusChange.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapDiskStatusChange.setStatus(
        "current"
    )

fadcTrapInetPortExhaustion = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 530)
)
fadcTrapInetPortExhaustion.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapInetPortExhaustion.setStatus(
        "current"
    )

fadcTrapCertExpire = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 531)
)
fadcTrapCertExpire.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapCertExpire.setStatus(
        "current"
    )

fadcTrapLogicalInterfaceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 532)
)
fadcTrapLogicalInterfaceUp.setObjects(
      *(("FORTINET-FORTIWAN-MIB", "fwnSysSerial"),
        ("FORTINET-FORTIWAN-MIB", "fadcIntfName"))
)
if mibBuilder.loadTexts:
    fadcTrapLogicalInterfaceUp.setStatus(
        "current"
    )

fadcTrapLogicalInterfaceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 533)
)
fadcTrapLogicalInterfaceDown.setObjects(
      *(("FORTINET-FORTIWAN-MIB", "fwnSysSerial"),
        ("FORTINET-FORTIWAN-MIB", "fadcIntfName"))
)
if mibBuilder.loadTexts:
    fadcTrapLogicalInterfaceDown.setStatus(
        "current"
    )

fadcTrapLogicalInterfaceDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 534)
)
fadcTrapLogicalInterfaceDisabled.setObjects(
      *(("FORTINET-FORTIWAN-MIB", "fwnSysSerial"),
        ("FORTINET-FORTIWAN-MIB", "fadcIntfName"))
)
if mibBuilder.loadTexts:
    fadcTrapLogicalInterfaceDisabled.setStatus(
        "current"
    )

fadcTrapMemberConnectionRateStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 600)
)
fadcTrapMemberConnectionRateStart.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapMemberConnectionRateStart.setStatus(
        "current"
    )

fadcTrapVirtualServerConnectionRateStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 601)
)
fadcTrapVirtualServerConnectionRateStart.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapVirtualServerConnectionRateStart.setStatus(
        "current"
    )

fadcTrapMemberConnectionLimitStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 602)
)
fadcTrapMemberConnectionLimitStart.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapMemberConnectionLimitStart.setStatus(
        "current"
    )

fadcTrapVirtualServerConnectionLimitStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 603)
)
fadcTrapVirtualServerConnectionLimitStart.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapVirtualServerConnectionLimitStart.setStatus(
        "current"
    )

fadcTrapMemberConnectionRateStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 604)
)
fadcTrapMemberConnectionRateStop.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapMemberConnectionRateStop.setStatus(
        "current"
    )

fadcTrapVirtualServerConnectionRateStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 605)
)
fadcTrapVirtualServerConnectionRateStop.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapVirtualServerConnectionRateStop.setStatus(
        "current"
    )

fadcTrapMemberConnectionLimitStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 606)
)
fadcTrapMemberConnectionLimitStop.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapMemberConnectionLimitStop.setStatus(
        "current"
    )

fadcTrapVirtualServerConnectionLimitStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 607)
)
fadcTrapVirtualServerConnectionLimitStop.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapVirtualServerConnectionLimitStop.setStatus(
        "current"
    )

fadcTrapVirtualServerTransactionRateStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 608)
)
fadcTrapVirtualServerTransactionRateStart.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapVirtualServerTransactionRateStart.setStatus(
        "current"
    )

fadcTrapVirtualServerTransactionRateStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 609)
)
fadcTrapVirtualServerTransactionRateStop.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapVirtualServerTransactionRateStop.setStatus(
        "current"
    )

fadcTrapMemberHCDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 610)
)
fadcTrapMemberHCDown.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapMemberHCDown.setStatus(
        "current"
    )

fadcTrapVirtualServerHealthChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 611)
)
fadcTrapVirtualServerHealthChange.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapVirtualServerHealthChange.setStatus(
        "current"
    )

fadcTrapMemberHCUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 612)
)
fadcTrapMemberHCUp.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapMemberHCUp.setStatus(
        "current"
    )

fadcTrapVirtualServerAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 613)
)
fadcTrapVirtualServerAuthFail.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapVirtualServerAuthFail.setStatus(
        "current"
    )

fadcTrapVirtualServerIPPoolLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 614)
)
fadcTrapVirtualServerIPPoolLimit.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapVirtualServerIPPoolLimit.setStatus(
        "current"
    )

adcTrapGatewayHCDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 615)
)
adcTrapGatewayHCDown.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    adcTrapGatewayHCDown.setStatus(
        "current"
    )

fadcTrapLinkGroupHCDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 616)
)
fadcTrapLinkGroupHCDown.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapLinkGroupHCDown.setStatus(
        "current"
    )

fadcTrapGatewayHCUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 617)
)
fadcTrapGatewayHCUp.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapGatewayHCUp.setStatus(
        "current"
    )

fadcTrapLinkGroupHCUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 618)
)
fadcTrapLinkGroupHCUp.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapLinkGroupHCUp.setStatus(
        "current"
    )

fadcTrapGatewayInboundBandwidth = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 619)
)
fadcTrapGatewayInboundBandwidth.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapGatewayInboundBandwidth.setStatus(
        "current"
    )

fadcTrapGatewayOutboundBandwidth = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 620)
)
fadcTrapGatewayOutboundBandwidth.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapGatewayOutboundBandwidth.setStatus(
        "current"
    )

fadcTrapGatewayInboundSpillover = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 621)
)
fadcTrapGatewayInboundSpillover.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapGatewayInboundSpillover.setStatus(
        "current"
    )

fadcTrapGatewayOutboundSpillover = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 622)
)
fadcTrapGatewayOutboundSpillover.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapGatewayOutboundSpillover.setStatus(
        "current"
    )

fadcTrapGatewayTotalSpillover = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 623)
)
fadcTrapGatewayTotalSpillover.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapGatewayTotalSpillover.setStatus(
        "current"
    )

fadcTrapGlbServerNotAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 624)
)
fadcTrapGlbServerNotAvail.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapGlbServerNotAvail.setStatus(
        "current"
    )

fadcTrapGlbServerAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 625)
)
fadcTrapGlbServerAvail.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapGlbServerAvail.setStatus(
        "current"
    )

fadcTrapGlbVSNotAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 626)
)
fadcTrapGlbVSNotAvail.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapGlbVSNotAvail.setStatus(
        "current"
    )

fadcTrapGlbVSAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 627)
)
fadcTrapGlbVSAvail.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapGlbVSAvail.setStatus(
        "current"
    )

fadcTrapGlbGWNotAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 633)
)
fadcTrapGlbGWNotAvail.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapGlbGWNotAvail.setStatus(
        "current"
    )

fadcTrapGlbGWAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 118, 0, 634)
)
fadcTrapGlbGWAvail.setObjects(
    ("FORTINET-FORTIWAN-MIB", "fwnSysSerial")
)
if mibBuilder.loadTexts:
    fadcTrapGlbGWAvail.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

fadcMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12356, 118, 600, 100)
)
fadcMIBCompliance.setObjects(
      *(("FORTINET-FORTIWAN-MIB", "fwnSystemConformanceGroup"),
        ("FORTINET-FORTIWAN-MIB", "fwnSysOptionsConformanceGroup"),
        ("FORTINET-FORTIWAN-MIB", "fwnHAModeConformanceGroup"))
)
if mibBuilder.loadTexts:
    fadcMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FORTINET-FORTIWAN-MIB",
    **{"FnHAModeVal": FnHAModeVal,
       "FnVdIndex": FnVdIndex,
       "FnHaState": FnHaState,
       "fnFortiWANMib": fnFortiWANMib,
       "fwnTraps": fwnTraps,
       "fadcTrapCpuHighThreshold": fadcTrapCpuHighThreshold,
       "fadcTrapMemLowThreshold": fadcTrapMemLowThreshold,
       "fadcTrapLogDiskHighThreshold": fadcTrapLogDiskHighThreshold,
       "fadcTrapDosAttackStart": fadcTrapDosAttackStart,
       "fadcTrapDosAttackStop": fadcTrapDosAttackStop,
       "fadcTrapFwConnectionLimit": fadcTrapFwConnectionLimit,
       "fadcTrapFwSnatLimit": fadcTrapFwSnatLimit,
       "fadcTrapRequestBlocked": fadcTrapRequestBlocked,
       "fadcTrapXSSAttackDetected": fadcTrapXSSAttackDetected,
       "fadcTrapSQLInjectionAttackDetected": fadcTrapSQLInjectionAttackDetected,
       "fadcTrapGenericAttackDetected": fadcTrapGenericAttackDetected,
       "fadcTrapExploitsAttackDetected": fadcTrapExploitsAttackDetected,
       "fadcTrapTrojansAttackDetected": fadcTrapTrojansAttackDetected,
       "fadcTrapInfoDisclosureAttackDetected": fadcTrapInfoDisclosureAttackDetected,
       "fadcTrapURLPattenViolateDetected": fadcTrapURLPattenViolateDetected,
       "fadcTrapProtocolContraintDetected": fadcTrapProtocolContraintDetected,
       "fadcTrapGeoViolateDetected": fadcTrapGeoViolateDetected,
       "fadcTrapReputaionViolateDetected": fadcTrapReputaionViolateDetected,
       "fadcTrapCPUTempHigh": fadcTrapCPUTempHigh,
       "fadcTrapCPUTempNormal": fadcTrapCPUTempNormal,
       "fadcTrapDeviceTempHigh": fadcTrapDeviceTempHigh,
       "fadcTrapDeviceTempNormal": fadcTrapDeviceTempNormal,
       "fadcTrapPSUTempHigh": fadcTrapPSUTempHigh,
       "fadcTrapPSUTempNormal": fadcTrapPSUTempNormal,
       "fadcTrapPSUFanSlow": fadcTrapPSUFanSlow,
       "fadcTrapDeviceFanSlow": fadcTrapDeviceFanSlow,
       "fadcTrapPSUFanBad": fadcTrapPSUFanBad,
       "fadcTrapPSUFanGood": fadcTrapPSUFanGood,
       "fadcTrapDeviceFanBad": fadcTrapDeviceFanBad,
       "fadcTrapDeviceFanGood": fadcTrapDeviceFanGood,
       "fadcTrapVoltageHigh": fadcTrapVoltageHigh,
       "fadcTrapPowerSupplyHigh": fadcTrapPowerSupplyHigh,
       "fadcTrapPSUVoltageHigh": fadcTrapPSUVoltageHigh,
       "fadcTrapVoltageLow": fadcTrapVoltageLow,
       "fadcTrapPowerSupplyLow": fadcTrapPowerSupplyLow,
       "fadcTrapPSUVoltageLow": fadcTrapPSUVoltageLow,
       "fadcTrapPSUFailure": fadcTrapPSUFailure,
       "fadcTrapARPConflict": fadcTrapARPConflict,
       "fadcTrapExternalLinkChange": fadcTrapExternalLinkChange,
       "fadcTrapLogDiskCloseThreshold": fadcTrapLogDiskCloseThreshold,
       "fadcTrapLogDiskLost": fadcTrapLogDiskLost,
       "fadcTrapSsdMwiNearThreshold": fadcTrapSsdMwiNearThreshold,
       "fadcTrapSsdMwiReachedThreshold": fadcTrapSsdMwiReachedThreshold,
       "fadcTrapHAPeerLost": fadcTrapHAPeerLost,
       "fadcTrapHAMasterFailover": fadcTrapHAMasterFailover,
       "fadcTrapPortStatusChange": fadcTrapPortStatusChange,
       "fadcTrapDiskStatusChange": fadcTrapDiskStatusChange,
       "fadcTrapInetPortExhaustion": fadcTrapInetPortExhaustion,
       "fadcTrapCertExpire": fadcTrapCertExpire,
       "fadcTrapLogicalInterfaceUp": fadcTrapLogicalInterfaceUp,
       "fadcTrapLogicalInterfaceDown": fadcTrapLogicalInterfaceDown,
       "fadcTrapLogicalInterfaceDisabled": fadcTrapLogicalInterfaceDisabled,
       "fadcTrapMemberConnectionRateStart": fadcTrapMemberConnectionRateStart,
       "fadcTrapVirtualServerConnectionRateStart": fadcTrapVirtualServerConnectionRateStart,
       "fadcTrapMemberConnectionLimitStart": fadcTrapMemberConnectionLimitStart,
       "fadcTrapVirtualServerConnectionLimitStart": fadcTrapVirtualServerConnectionLimitStart,
       "fadcTrapMemberConnectionRateStop": fadcTrapMemberConnectionRateStop,
       "fadcTrapVirtualServerConnectionRateStop": fadcTrapVirtualServerConnectionRateStop,
       "fadcTrapMemberConnectionLimitStop": fadcTrapMemberConnectionLimitStop,
       "fadcTrapVirtualServerConnectionLimitStop": fadcTrapVirtualServerConnectionLimitStop,
       "fadcTrapVirtualServerTransactionRateStart": fadcTrapVirtualServerTransactionRateStart,
       "fadcTrapVirtualServerTransactionRateStop": fadcTrapVirtualServerTransactionRateStop,
       "fadcTrapMemberHCDown": fadcTrapMemberHCDown,
       "fadcTrapVirtualServerHealthChange": fadcTrapVirtualServerHealthChange,
       "fadcTrapMemberHCUp": fadcTrapMemberHCUp,
       "fadcTrapVirtualServerAuthFail": fadcTrapVirtualServerAuthFail,
       "fadcTrapVirtualServerIPPoolLimit": fadcTrapVirtualServerIPPoolLimit,
       "adcTrapGatewayHCDown": adcTrapGatewayHCDown,
       "fadcTrapLinkGroupHCDown": fadcTrapLinkGroupHCDown,
       "fadcTrapGatewayHCUp": fadcTrapGatewayHCUp,
       "fadcTrapLinkGroupHCUp": fadcTrapLinkGroupHCUp,
       "fadcTrapGatewayInboundBandwidth": fadcTrapGatewayInboundBandwidth,
       "fadcTrapGatewayOutboundBandwidth": fadcTrapGatewayOutboundBandwidth,
       "fadcTrapGatewayInboundSpillover": fadcTrapGatewayInboundSpillover,
       "fadcTrapGatewayOutboundSpillover": fadcTrapGatewayOutboundSpillover,
       "fadcTrapGatewayTotalSpillover": fadcTrapGatewayTotalSpillover,
       "fadcTrapGlbServerNotAvail": fadcTrapGlbServerNotAvail,
       "fadcTrapGlbServerAvail": fadcTrapGlbServerAvail,
       "fadcTrapGlbVSNotAvail": fadcTrapGlbVSNotAvail,
       "fadcTrapGlbVSAvail": fadcTrapGlbVSAvail,
       "fadcTrapGlbGWNotAvail": fadcTrapGlbGWNotAvail,
       "fadcTrapGlbGWAvail": fadcTrapGlbGWAvail,
       "fwnSystem": fwnSystem,
       "fwnSysModel": fwnSysModel,
       "fwnSysSerial": fwnSysSerial,
       "fwnSysVersion": fwnSysVersion,
       "fwnSysCpuUsage": fwnSysCpuUsage,
       "fwnSysMemUsage": fwnSysMemUsage,
       "fwnSysLogDiskUsage": fwnSysLogDiskUsage,
       "fwnSysLoad": fwnSysLoad,
       "fwnSysCpuUsageTable": fwnSysCpuUsageTable,
       "fwnSysCpuUsageEntry": fwnSysCpuUsageEntry,
       "fwnSysCpuIndex": fwnSysCpuIndex,
       "fwnSysCpuName": fwnSysCpuName,
       "fwnSysCpu2secAvgUsage": fwnSysCpu2secAvgUsage,
       "fwnSysCpu1minAvgUsage": fwnSysCpu1minAvgUsage,
       "fwnSysCpu5minAvgUsage": fwnSysCpu5minAvgUsage,
       "fwnSysOptions": fwnSysOptions,
       "fwnSysOptIdleTimeout": fwnSysOptIdleTimeout,
       "fwnSysHA": fwnSysHA,
       "fwnHAMode": fwnHAMode,
       "fwnVirtualDomain": fwnVirtualDomain,
       "fwnVdMaxVdoms": fwnVdMaxVdoms,
       "fwnVdEnabled": fwnVdEnabled,
       "fwnVdNumber": fwnVdNumber,
       "fwnVdTable": fwnVdTable,
       "fwnVdEntry": fwnVdEntry,
       "fwnVdEntryIndex": fwnVdEntryIndex,
       "fwnVdEntryName": fwnVdEntryName,
       "fwnVdEntHaState": fwnVdEntHaState,
       "fwnVirtualServer": fwnVirtualServer,
       "fadcVSNumber": fadcVSNumber,
       "fadcVSTable": fadcVSTable,
       "fadcVSEntry": fadcVSEntry,
       "fadcVSIndex": fadcVSIndex,
       "fadcVSName": fadcVSName,
       "fadcVSStatus": fadcVSStatus,
       "fadcVSHealth": fadcVSHealth,
       "fadcVSNewConnections": fadcVSNewConnections,
       "fadcVSConcurrent": fadcVSConcurrent,
       "fadcVSThroughputKbps": fadcVSThroughputKbps,
       "fadcVSVdom": fadcVSVdom,
       "fadcIntf": fadcIntf,
       "fadcIntfTable": fadcIntfTable,
       "fadcIntfEntry": fadcIntfEntry,
       "fadcIntfIndex": fadcIntfIndex,
       "fadcIntfName": fadcIntfName,
       "fadcIntfVdom": fadcIntfVdom,
       "fadcAdmin": fadcAdmin,
       "fadcAdminTable": fadcAdminTable,
       "fadcAdminEntry": fadcAdminEntry,
       "fadcAdminIndex": fadcAdminIndex,
       "fadcAdminName": fadcAdminName,
       "fadcAdminVdom": fadcAdminVdom,
       "fadcHardware": fadcHardware,
       "fadcCPUInfo": fadcCPUInfo,
       "fadcCPUTable": fadcCPUTable,
       "fadcCPUEntry": fadcCPUEntry,
       "fadcCPUIndex": fadcCPUIndex,
       "fadcCPUName": fadcCPUName,
       "fadcCPUTemp": fadcCPUTemp,
       "fadcPSUInfo": fadcPSUInfo,
       "fadcPSUTable": fadcPSUTable,
       "fadcPSUEntry": fadcPSUEntry,
       "fadcPSUIndex": fadcPSUIndex,
       "fadcPSUName": fadcPSUName,
       "fadcPSUTemp": fadcPSUTemp,
       "fadcPSUFanSpeed": fadcPSUFanSpeed,
       "fadcPSUFanStatus": fadcPSUFanStatus,
       "fadcPSUVoltage": fadcPSUVoltage,
       "fadcPSUStatus": fadcPSUStatus,
       "fadcNetworkInfo": fadcNetworkInfo,
       "fadcNetworkTable": fadcNetworkTable,
       "fadcNetworkEntry": fadcNetworkEntry,
       "fadcNetworkIndex": fadcNetworkIndex,
       "fadcPortLinkName": fadcPortLinkName,
       "fadcPortLinkStatus": fadcPortLinkStatus,
       "fadcDeviceInfo": fadcDeviceInfo,
       "fadcDeviceTempTables": fadcDeviceTempTables,
       "fadcDeviceTempTable": fadcDeviceTempTable,
       "fadcDeviceTempEntry": fadcDeviceTempEntry,
       "fadcDeviceTempIndex": fadcDeviceTempIndex,
       "fadcDeviceTempName": fadcDeviceTempName,
       "fadcDeviceTempValue": fadcDeviceTempValue,
       "fadcDeviceFanTables": fadcDeviceFanTables,
       "fadcDeviceFanTable": fadcDeviceFanTable,
       "fadcDeviceFanEntry": fadcDeviceFanEntry,
       "fadcDeviceFanIndex": fadcDeviceFanIndex,
       "fadcDeviceFanName": fadcDeviceFanName,
       "fadcDeviceFanSpeed": fadcDeviceFanSpeed,
       "fadcDeviceFanStatus": fadcDeviceFanStatus,
       "fadcHA": fadcHA,
       "fadcHACurMode": fadcHACurMode,
       "fadcHACurState": fadcHACurState,
       "fadcHAPeerCount": fadcHAPeerCount,
       "fadcMoniterIntfCount": fadcMoniterIntfCount,
       "fadcDiskState": fadcDiskState,
       "fadcHALastChangedTime": fadcHALastChangedTime,
       "fadcHALastChangedReason": fadcHALastChangedReason,
       "fadcSyncStats": fadcSyncStats,
       "fadcHASyncStatsTable": fadcHASyncStatsTable,
       "fadcHASyncStatsEntry": fadcHASyncStatsEntry,
       "fadcSyncTypeIndex": fadcSyncTypeIndex,
       "fadcSyncType": fadcSyncType,
       "fadcSyncSent": fadcSyncSent,
       "fadcSyncReceived": fadcSyncReceived,
       "fadcDeviceErrCount": fadcDeviceErrCount,
       "fadcDuplicateNodeID": fadcDuplicateNodeID,
       "fadcVersionMismatch": fadcVersionMismatch,
       "fadcHAPeerInfo": fadcHAPeerInfo,
       "fadcHAPeerTable": fadcHAPeerTable,
       "fadcHAPeerEntry": fadcHAPeerEntry,
       "fadcPeerIndex": fadcPeerIndex,
       "fadcPeerSerialNumber": fadcPeerSerialNumber,
       "fadcPeerStatus": fadcPeerStatus,
       "fadcNodeID": fadcNodeID,
       "fadcIPAddress": fadcIPAddress,
       "fadcVoltage": fadcVoltage,
       "fadcPowerSupplyVoltage": fadcPowerSupplyVoltage,
       "fadcLogDiskStatus": fadcLogDiskStatus,
       "fadcSecurity": fadcSecurity,
       "fadcDDoSAttackStatus": fadcDDoSAttackStatus,
       "fadcApplication": fadcApplication,
       "fadcRS": fadcRS,
       "fadcPoolNumber": fadcPoolNumber,
       "fadcRSNumber": fadcRSNumber,
       "fadcRSTable": fadcRSTable,
       "fadcRSEntry": fadcRSEntry,
       "fadcRSIndex": fadcRSIndex,
       "fadcPoolName": fadcPoolName,
       "fadcRSStatus": fadcRSStatus,
       "fadcRSHealth": fadcRSHealth,
       "fadcRSVdom": fadcRSVdom,
       "fadcVS": fadcVS,
       "fadcVirturalServerNumber": fadcVirturalServerNumber,
       "fadcVirturalServerTable": fadcVirturalServerTable,
       "fadcVirturalServerEntry": fadcVirturalServerEntry,
       "fadcVirturalServerIndex": fadcVirturalServerIndex,
       "fadcVirturalServerName": fadcVirturalServerName,
       "fadcVirturalServerStatus": fadcVirturalServerStatus,
       "fadcVirturalServerHealth": fadcVirturalServerHealth,
       "fadcVirturalServerNewConnections": fadcVirturalServerNewConnections,
       "fadcVirturalServerConcurrent": fadcVirturalServerConcurrent,
       "fadcVirturalServerThroughput_Kbps": fadcVirturalServerThroughput_Kbps,
       "fadcVirturalServerVdom": fadcVirturalServerVdom,
       "fadcVirturalServerWAF": fadcVirturalServerWAF,
       "fadcLinkLoadBalance": fadcLinkLoadBalance,
       "fadcGatewayTables": fadcGatewayTables,
       "fadcGatewayTable": fadcGatewayTable,
       "fadcGatewayEntry": fadcGatewayEntry,
       "fadcGatewayIndex": fadcGatewayIndex,
       "fadcGatewayName": fadcGatewayName,
       "fadcGatewayHCStatus": fadcGatewayHCStatus,
       "fadcGatewayInboundBandWidth": fadcGatewayInboundBandWidth,
       "fadcGatewayOutboundBandWidth": fadcGatewayOutboundBandWidth,
       "fadcGatewayVdom": fadcGatewayVdom,
       "fadcLinkGroupTables": fadcLinkGroupTables,
       "fadcLinkGroupTable": fadcLinkGroupTable,
       "fadcLinkGroupEntry": fadcLinkGroupEntry,
       "fadcLinkGroupIndex": fadcLinkGroupIndex,
       "fadcLinkGroupName": fadcLinkGroupName,
       "fadcLinkGroupHCStatus": fadcLinkGroupHCStatus,
       "fadcLinkGroupMode": fadcLinkGroupMode,
       "fadcLinkGroupVdom": fadcLinkGroupVdom,
       "fadcGlobalLoadBalance": fadcGlobalLoadBalance,
       "fadcGLBVSTables": fadcGLBVSTables,
       "fadcGLBVSTable": fadcGLBVSTable,
       "fadcGLBVSEntry": fadcGLBVSEntry,
       "fadcGLBVSIndex": fadcGLBVSIndex,
       "fadcGLBVSName": fadcGLBVSName,
       "fadcGLBVSStatus": fadcGLBVSStatus,
       "fadcGLBVSServerName": fadcGLBVSServerName,
       "fadcGLBVSVdom": fadcGLBVSVdom,
       "fadcGLBServerTables": fadcGLBServerTables,
       "fadcGLBServerTable": fadcGLBServerTable,
       "fadcGLBServerEntry": fadcGLBServerEntry,
       "fadcGLBServerIndex": fadcGLBServerIndex,
       "fadcGLBServerName": fadcGLBServerName,
       "fadcGLBServerStatus": fadcGLBServerStatus,
       "fadcGLBServerVdom": fadcGLBServerVdom,
       "fadcGLBGatewayTables": fadcGLBGatewayTables,
       "fadcGLBGatewayTable": fadcGLBGatewayTable,
       "fadcGLBGatewayEntry": fadcGLBGatewayEntry,
       "fadcGLBGatewayIndex": fadcGLBGatewayIndex,
       "fadcGLBGatewayName": fadcGLBGatewayName,
       "fadcGLBGatewayStatus": fadcGLBGatewayStatus,
       "fadcGLBGatewayServerName": fadcGLBGatewayServerName,
       "fadcGLBGatewayVdom": fadcGLBGatewayVdom,
       "fadcServerLoadBalance": fadcServerLoadBalance,
       "fadcClientSideCPS": fadcClientSideCPS,
       "fadcClientSideRPS": fadcClientSideRPS,
       "fadcClientSideSSLCPS": fadcClientSideSSLCPS,
       "fadcClientSideSSLRPS": fadcClientSideSSLRPS,
       "fadcClientSideThroughput": fadcClientSideThroughput,
       "fadcClientSideSSLThroughput": fadcClientSideSSLThroughput,
       "fadcConcurrentClientSideConnections": fadcConcurrentClientSideConnections,
       "fadcConcurrentClientSideSSLSessions": fadcConcurrentClientSideSSLSessions,
       "fadcClientSSLCacheUtilizationTables": fadcClientSSLCacheUtilizationTables,
       "fadcClientSSLCacheUtilizationTable": fadcClientSSLCacheUtilizationTable,
       "fadcClientSSLCacheUtilizationEntry": fadcClientSSLCacheUtilizationEntry,
       "fadcSLBVSIndex": fadcSLBVSIndex,
       "fadcSLBVSName": fadcSLBVSName,
       "fadcSLBTotalCacheItems": fadcSLBTotalCacheItems,
       "fadcSLBTotalCacheSize": fadcSLBTotalCacheSize,
       "fadcSLBCacheHitCount": fadcSLBCacheHitCount,
       "fadcSLBCacheHitBytes": fadcSLBCacheHitBytes,
       "fadcSLBTatalCertCacheItems": fadcSLBTatalCertCacheItems,
       "fadcSLBTotalCertCacheSize": fadcSLBTotalCertCacheSize,
       "fadcSLBHitCertCacheCount": fadcSLBHitCertCacheCount,
       "fadcSLBHitCertTotalCheck": fadcSLBHitCertTotalCheck,
       "fadcSLBHitCertPercentage": fadcSLBHitCertPercentage,
       "fadcMIBConformance": fadcMIBConformance,
       "fwnSystemConformanceGroup": fwnSystemConformanceGroup,
       "fwnSysOptionsConformanceGroup": fwnSysOptionsConformanceGroup,
       "fwnHAModeConformanceGroup": fwnHAModeConformanceGroup,
       "fadcMIBCompliance": fadcMIBCompliance}
)
