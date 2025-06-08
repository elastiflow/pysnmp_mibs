# SNMP MIB module (CISCO-UNIFIED-FIREWALL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-UNIFIED-FIREWALL-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:02:39 2025
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

(dot1dTpFdbPort,
 dot1dTpFdbStatus) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dTpFdbPort",
    "dot1dTpFdbStatus")

(Hardware,
 HardwareStatus) = mibBuilder.importSymbols(
    "CISCO-FIREWALL-MIB",
    "Hardware",
    "HardwareStatus")

(CFWApplicationProtocol,
 CFWNetworkProtocol,
 CFWPolicy,
 CFWPolicyTarget,
 CFWPolicyTargetType,
 CFWUrlServerStatus,
 CFWUrlfVendorId) = mibBuilder.importSymbols(
    "CISCO-FIREWALL-TC",
    "CFWApplicationProtocol",
    "CFWNetworkProtocol",
    "CFWPolicy",
    "CFWPolicyTarget",
    "CFWPolicyTargetType",
    "CFWUrlServerStatus",
    "CFWUrlfVendorId")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoUnifiedFirewallMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491)
)
if mibBuilder.loadTexts:
    ciscoUnifiedFirewallMIB.setRevisions(
        ("2021-03-18 00:00",
         "2020-10-29 00:00",
         "2020-03-06 00:00",
         "2020-01-07 00:00",
         "2019-12-12 00:00",
         "2005-09-22 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CUfwFOState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("init", 0),
          ("disabled", 1),
          ("failed", 2),
          ("negotiation", 3),
          ("standbyCold", 4),
          ("standbyConfig", 5),
          ("standbyFilesys", 6),
          ("standbyBulk", 7),
          ("standby", 8),
          ("activeFast", 9),
          ("activeDrain", 10),
          ("activePreConf", 11),
          ("activePostConf", 12),
          ("active", 13),
          ("invalid", 14))
    )



class CUfwInterfaceMonitor(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("monitored", 1),
          ("notMonitored", 2),
          ("waiting", 3),
          ("autostateDown", 4),
          ("shutdown", 5))
    )



class CUfwInterfaceHealth(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("normal", 1),
          ("testing", 2),
          ("linkDown", 3),
          ("failed", 4),
          ("noLink", 5))
    )



class CUfwFOGroupId(TextualConvention, Integer32):
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
        *(("default", 0),
          ("group1", 1),
          ("group2", 2))
    )



class CUfwCluState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("election", 1),
          ("onCall", 2),
          ("slaveCold", 3),
          ("slaveAppSync", 4),
          ("slaveConfig", 5),
          ("slaveFilesys", 6),
          ("slaveBulkSync", 7),
          ("slave", 8),
          ("slavePending", 9),
          ("deputyBulkSync", 10),
          ("deputy", 11),
          ("masterFast", 12),
          ("masterDrain", 13),
          ("masterConfig", 14),
          ("masterPostConfig", 15),
          ("master", 16),
          ("masterDefer", 17))
    )



class CUfwCluHealth(TextualConvention, Integer32):
    status = "current"
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
        *(("init", 0),
          ("up", 1),
          ("down", 2),
          ("goingDown", 3),
          ("goingUp", 4),
          ("noLicense", 5),
          ("none", 6))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoUnifiedFirewallMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoUnifiedFirewallMIBNotifs = _CiscoUnifiedFirewallMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 0)
)
_CiscoUnifiedFirewallMIBObjects_ObjectIdentity = ObjectIdentity
ciscoUnifiedFirewallMIBObjects = _CiscoUnifiedFirewallMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1)
)
_CuFwConnectionGrp_ObjectIdentity = ObjectIdentity
cuFwConnectionGrp = _CuFwConnectionGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1)
)
_CuFwConnectionGlobals_ObjectIdentity = ObjectIdentity
cuFwConnectionGlobals = _CuFwConnectionGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 1)
)
_CufwConnGlobalNumAttempted_Type = Counter64
_CufwConnGlobalNumAttempted_Object = MibScalar
cufwConnGlobalNumAttempted = _CufwConnGlobalNumAttempted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 1, 1),
    _CufwConnGlobalNumAttempted_Type()
)
cufwConnGlobalNumAttempted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnGlobalNumAttempted.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnGlobalNumAttempted.setUnits("Connections")
_CufwConnGlobalNumSetupsAborted_Type = Counter64
_CufwConnGlobalNumSetupsAborted_Object = MibScalar
cufwConnGlobalNumSetupsAborted = _CufwConnGlobalNumSetupsAborted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 1, 2),
    _CufwConnGlobalNumSetupsAborted_Type()
)
cufwConnGlobalNumSetupsAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnGlobalNumSetupsAborted.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnGlobalNumSetupsAborted.setUnits("Connections")
_CufwConnGlobalNumPolicyDeclined_Type = Counter64
_CufwConnGlobalNumPolicyDeclined_Object = MibScalar
cufwConnGlobalNumPolicyDeclined = _CufwConnGlobalNumPolicyDeclined_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 1, 3),
    _CufwConnGlobalNumPolicyDeclined_Type()
)
cufwConnGlobalNumPolicyDeclined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnGlobalNumPolicyDeclined.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnGlobalNumPolicyDeclined.setUnits("Connections")
_CufwConnGlobalNumResDeclined_Type = Counter64
_CufwConnGlobalNumResDeclined_Object = MibScalar
cufwConnGlobalNumResDeclined = _CufwConnGlobalNumResDeclined_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 1, 4),
    _CufwConnGlobalNumResDeclined_Type()
)
cufwConnGlobalNumResDeclined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnGlobalNumResDeclined.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnGlobalNumResDeclined.setUnits("Connections")
_CufwConnGlobalNumHalfOpen_Type = Gauge32
_CufwConnGlobalNumHalfOpen_Object = MibScalar
cufwConnGlobalNumHalfOpen = _CufwConnGlobalNumHalfOpen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 1, 5),
    _CufwConnGlobalNumHalfOpen_Type()
)
cufwConnGlobalNumHalfOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnGlobalNumHalfOpen.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnGlobalNumHalfOpen.setUnits("Connections")
_CufwConnGlobalNumActive_Type = Gauge32
_CufwConnGlobalNumActive_Object = MibScalar
cufwConnGlobalNumActive = _CufwConnGlobalNumActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 1, 6),
    _CufwConnGlobalNumActive_Type()
)
cufwConnGlobalNumActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnGlobalNumActive.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnGlobalNumActive.setUnits("Connections")
_CufwConnGlobalNumExpired_Type = Counter64
_CufwConnGlobalNumExpired_Object = MibScalar
cufwConnGlobalNumExpired = _CufwConnGlobalNumExpired_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 1, 7),
    _CufwConnGlobalNumExpired_Type()
)
cufwConnGlobalNumExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnGlobalNumExpired.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnGlobalNumExpired.setUnits("Connections")
_CufwConnGlobalNumAborted_Type = Counter64
_CufwConnGlobalNumAborted_Object = MibScalar
cufwConnGlobalNumAborted = _CufwConnGlobalNumAborted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 1, 8),
    _CufwConnGlobalNumAborted_Type()
)
cufwConnGlobalNumAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnGlobalNumAborted.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnGlobalNumAborted.setUnits("Connections")
_CufwConnGlobalNumEmbryonic_Type = Gauge32
_CufwConnGlobalNumEmbryonic_Object = MibScalar
cufwConnGlobalNumEmbryonic = _CufwConnGlobalNumEmbryonic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 1, 9),
    _CufwConnGlobalNumEmbryonic_Type()
)
cufwConnGlobalNumEmbryonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnGlobalNumEmbryonic.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnGlobalNumEmbryonic.setUnits("Connections")
_CufwConnGlobalConnSetupRate1_Type = Gauge32
_CufwConnGlobalConnSetupRate1_Object = MibScalar
cufwConnGlobalConnSetupRate1 = _CufwConnGlobalConnSetupRate1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 1, 10),
    _CufwConnGlobalConnSetupRate1_Type()
)
cufwConnGlobalConnSetupRate1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnGlobalConnSetupRate1.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnGlobalConnSetupRate1.setUnits("Connections per second")
_CufwConnGlobalConnSetupRate5_Type = Gauge32
_CufwConnGlobalConnSetupRate5_Object = MibScalar
cufwConnGlobalConnSetupRate5 = _CufwConnGlobalConnSetupRate5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 1, 11),
    _CufwConnGlobalConnSetupRate5_Type()
)
cufwConnGlobalConnSetupRate5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnGlobalConnSetupRate5.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnGlobalConnSetupRate5.setUnits("Connections per second")
_CufwConnGlobalNumRemoteAccess_Type = Gauge32
_CufwConnGlobalNumRemoteAccess_Object = MibScalar
cufwConnGlobalNumRemoteAccess = _CufwConnGlobalNumRemoteAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 1, 12),
    _CufwConnGlobalNumRemoteAccess_Type()
)
cufwConnGlobalNumRemoteAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnGlobalNumRemoteAccess.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnGlobalNumRemoteAccess.setUnits("Connections")
_CuFwConnectionResources_ObjectIdentity = ObjectIdentity
cuFwConnectionResources = _CuFwConnectionResources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 2)
)
_CufwConnResMemoryUsage_Type = Gauge32
_CufwConnResMemoryUsage_Object = MibScalar
cufwConnResMemoryUsage = _CufwConnResMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 2, 1),
    _CufwConnResMemoryUsage_Type()
)
cufwConnResMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnResMemoryUsage.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnResMemoryUsage.setUnits("KBytes")
_CufwConnResActiveConnMemoryUsage_Type = Gauge32
_CufwConnResActiveConnMemoryUsage_Object = MibScalar
cufwConnResActiveConnMemoryUsage = _CufwConnResActiveConnMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 2, 2),
    _CufwConnResActiveConnMemoryUsage_Type()
)
cufwConnResActiveConnMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnResActiveConnMemoryUsage.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnResActiveConnMemoryUsage.setUnits("KBytes")
_CufwConnResHOConnMemoryUsage_Type = Gauge32
_CufwConnResHOConnMemoryUsage_Object = MibScalar
cufwConnResHOConnMemoryUsage = _CufwConnResHOConnMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 2, 3),
    _CufwConnResHOConnMemoryUsage_Type()
)
cufwConnResHOConnMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnResHOConnMemoryUsage.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnResHOConnMemoryUsage.setUnits("KBytes")
_CufwConnResEmbrConnMemoryUsage_Type = Gauge32
_CufwConnResEmbrConnMemoryUsage_Object = MibScalar
cufwConnResEmbrConnMemoryUsage = _CufwConnResEmbrConnMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 2, 4),
    _CufwConnResEmbrConnMemoryUsage_Type()
)
cufwConnResEmbrConnMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnResEmbrConnMemoryUsage.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnResEmbrConnMemoryUsage.setUnits("KBytes")
_CuFwConnectionReportSettings_ObjectIdentity = ObjectIdentity
cuFwConnectionReportSettings = _CuFwConnectionReportSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 3)
)


class _CufwConnReptAppStats_Type(TruthValue):
    """Custom type cufwConnReptAppStats based on TruthValue"""
    defaultValue = 2


_CufwConnReptAppStats_Type.__name__ = "TruthValue"
_CufwConnReptAppStats_Object = MibScalar
cufwConnReptAppStats = _CufwConnReptAppStats_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 3, 1),
    _CufwConnReptAppStats_Type()
)
cufwConnReptAppStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cufwConnReptAppStats.setStatus("current")
_CufwConnReptAppStatsLastChanged_Type = TimeStamp
_CufwConnReptAppStatsLastChanged_Object = MibScalar
cufwConnReptAppStatsLastChanged = _CufwConnReptAppStatsLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 3, 2),
    _CufwConnReptAppStatsLastChanged_Type()
)
cufwConnReptAppStatsLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnReptAppStatsLastChanged.setStatus("current")
_CuFwConnectionSummaryTables_ObjectIdentity = ObjectIdentity
cuFwConnectionSummaryTables = _CuFwConnectionSummaryTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4)
)
_CufwConnSummaryTable_Object = MibTable
cufwConnSummaryTable = _CufwConnSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cufwConnSummaryTable.setStatus("current")
_CufwConnSummaryEntry_Object = MibTableRow
cufwConnSummaryEntry = _CufwConnSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 1, 1)
)
cufwConnSummaryEntry.setIndexNames(
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwConnProtocol"),
)
if mibBuilder.loadTexts:
    cufwConnSummaryEntry.setStatus("current")
_CufwConnProtocol_Type = CFWNetworkProtocol
_CufwConnProtocol_Object = MibTableColumn
cufwConnProtocol = _CufwConnProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 1, 1, 1),
    _CufwConnProtocol_Type()
)
cufwConnProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cufwConnProtocol.setStatus("current")
_CufwConnNumAttempted_Type = Counter64
_CufwConnNumAttempted_Object = MibTableColumn
cufwConnNumAttempted = _CufwConnNumAttempted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 1, 1, 2),
    _CufwConnNumAttempted_Type()
)
cufwConnNumAttempted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnNumAttempted.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnNumAttempted.setUnits("Connections")
_CufwConnNumSetupsAborted_Type = Counter64
_CufwConnNumSetupsAborted_Object = MibTableColumn
cufwConnNumSetupsAborted = _CufwConnNumSetupsAborted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 1, 1, 3),
    _CufwConnNumSetupsAborted_Type()
)
cufwConnNumSetupsAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnNumSetupsAborted.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnNumSetupsAborted.setUnits("Connections")
_CufwConnNumPolicyDeclined_Type = Counter64
_CufwConnNumPolicyDeclined_Object = MibTableColumn
cufwConnNumPolicyDeclined = _CufwConnNumPolicyDeclined_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 1, 1, 4),
    _CufwConnNumPolicyDeclined_Type()
)
cufwConnNumPolicyDeclined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnNumPolicyDeclined.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnNumPolicyDeclined.setUnits("Connections")
_CufwConnNumResDeclined_Type = Counter64
_CufwConnNumResDeclined_Object = MibTableColumn
cufwConnNumResDeclined = _CufwConnNumResDeclined_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 1, 1, 5),
    _CufwConnNumResDeclined_Type()
)
cufwConnNumResDeclined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnNumResDeclined.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnNumResDeclined.setUnits("Connections")
_CufwConnNumHalfOpen_Type = Gauge32
_CufwConnNumHalfOpen_Object = MibTableColumn
cufwConnNumHalfOpen = _CufwConnNumHalfOpen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 1, 1, 6),
    _CufwConnNumHalfOpen_Type()
)
cufwConnNumHalfOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnNumHalfOpen.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnNumHalfOpen.setUnits("Connections")
_CufwConnNumActive_Type = Gauge32
_CufwConnNumActive_Object = MibTableColumn
cufwConnNumActive = _CufwConnNumActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 1, 1, 7),
    _CufwConnNumActive_Type()
)
cufwConnNumActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnNumActive.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnNumActive.setUnits("Connections")
_CufwConnNumAborted_Type = Counter64
_CufwConnNumAborted_Object = MibTableColumn
cufwConnNumAborted = _CufwConnNumAborted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 1, 1, 8),
    _CufwConnNumAborted_Type()
)
cufwConnNumAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnNumAborted.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnNumAborted.setUnits("Connections")
_CufwConnSetupRate1_Type = Gauge32
_CufwConnSetupRate1_Object = MibTableColumn
cufwConnSetupRate1 = _CufwConnSetupRate1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 1, 1, 9),
    _CufwConnSetupRate1_Type()
)
cufwConnSetupRate1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnSetupRate1.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnSetupRate1.setUnits("Connections Per Second")
_CufwConnSetupRate5_Type = Gauge32
_CufwConnSetupRate5_Object = MibTableColumn
cufwConnSetupRate5 = _CufwConnSetupRate5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 1, 1, 10),
    _CufwConnSetupRate5_Type()
)
cufwConnSetupRate5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnSetupRate5.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnSetupRate5.setUnits("Connections Per Second")
_CufwAppConnSummaryTable_Object = MibTable
cufwAppConnSummaryTable = _CufwAppConnSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cufwAppConnSummaryTable.setStatus("current")
_CufwAppConnSummaryEntry_Object = MibTableRow
cufwAppConnSummaryEntry = _CufwAppConnSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 2, 1)
)
cufwAppConnSummaryEntry.setIndexNames(
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwAppConnProtocol"),
)
if mibBuilder.loadTexts:
    cufwAppConnSummaryEntry.setStatus("current")
_CufwAppConnProtocol_Type = CFWApplicationProtocol
_CufwAppConnProtocol_Object = MibTableColumn
cufwAppConnProtocol = _CufwAppConnProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 2, 1, 1),
    _CufwAppConnProtocol_Type()
)
cufwAppConnProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cufwAppConnProtocol.setStatus("current")
_CufwAppConnNumAttempted_Type = Counter64
_CufwAppConnNumAttempted_Object = MibTableColumn
cufwAppConnNumAttempted = _CufwAppConnNumAttempted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 2, 1, 2),
    _CufwAppConnNumAttempted_Type()
)
cufwAppConnNumAttempted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAppConnNumAttempted.setStatus("current")
if mibBuilder.loadTexts:
    cufwAppConnNumAttempted.setUnits("Connections")
_CufwAppConnNumSetupsAborted_Type = Counter64
_CufwAppConnNumSetupsAborted_Object = MibTableColumn
cufwAppConnNumSetupsAborted = _CufwAppConnNumSetupsAborted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 2, 1, 3),
    _CufwAppConnNumSetupsAborted_Type()
)
cufwAppConnNumSetupsAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAppConnNumSetupsAborted.setStatus("current")
if mibBuilder.loadTexts:
    cufwAppConnNumSetupsAborted.setUnits("Connections")
_CufwAppConnNumPolicyDeclined_Type = Counter64
_CufwAppConnNumPolicyDeclined_Object = MibTableColumn
cufwAppConnNumPolicyDeclined = _CufwAppConnNumPolicyDeclined_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 2, 1, 4),
    _CufwAppConnNumPolicyDeclined_Type()
)
cufwAppConnNumPolicyDeclined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAppConnNumPolicyDeclined.setStatus("current")
if mibBuilder.loadTexts:
    cufwAppConnNumPolicyDeclined.setUnits("Connections")
_CufwAppConnNumResDeclined_Type = Counter64
_CufwAppConnNumResDeclined_Object = MibTableColumn
cufwAppConnNumResDeclined = _CufwAppConnNumResDeclined_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 2, 1, 5),
    _CufwAppConnNumResDeclined_Type()
)
cufwAppConnNumResDeclined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAppConnNumResDeclined.setStatus("current")
if mibBuilder.loadTexts:
    cufwAppConnNumResDeclined.setUnits("Connections")
_CufwAppConnNumHalfOpen_Type = Gauge32
_CufwAppConnNumHalfOpen_Object = MibTableColumn
cufwAppConnNumHalfOpen = _CufwAppConnNumHalfOpen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 2, 1, 6),
    _CufwAppConnNumHalfOpen_Type()
)
cufwAppConnNumHalfOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAppConnNumHalfOpen.setStatus("current")
if mibBuilder.loadTexts:
    cufwAppConnNumHalfOpen.setUnits("Connections")
_CufwAppConnNumActive_Type = Gauge32
_CufwAppConnNumActive_Object = MibTableColumn
cufwAppConnNumActive = _CufwAppConnNumActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 2, 1, 7),
    _CufwAppConnNumActive_Type()
)
cufwAppConnNumActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAppConnNumActive.setStatus("current")
if mibBuilder.loadTexts:
    cufwAppConnNumActive.setUnits("Connections")
_CufwAppConnNumAborted_Type = Counter64
_CufwAppConnNumAborted_Object = MibTableColumn
cufwAppConnNumAborted = _CufwAppConnNumAborted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 2, 1, 8),
    _CufwAppConnNumAborted_Type()
)
cufwAppConnNumAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAppConnNumAborted.setStatus("current")
if mibBuilder.loadTexts:
    cufwAppConnNumAborted.setUnits("Connections")
_CufwAppConnSetupRate1_Type = Gauge32
_CufwAppConnSetupRate1_Object = MibTableColumn
cufwAppConnSetupRate1 = _CufwAppConnSetupRate1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 2, 1, 9),
    _CufwAppConnSetupRate1_Type()
)
cufwAppConnSetupRate1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAppConnSetupRate1.setStatus("current")
if mibBuilder.loadTexts:
    cufwAppConnSetupRate1.setUnits("Connections Per Second")
_CufwAppConnSetupRate5_Type = Gauge32
_CufwAppConnSetupRate5_Object = MibTableColumn
cufwAppConnSetupRate5 = _CufwAppConnSetupRate5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 2, 1, 10),
    _CufwAppConnSetupRate5_Type()
)
cufwAppConnSetupRate5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAppConnSetupRate5.setStatus("current")
if mibBuilder.loadTexts:
    cufwAppConnSetupRate5.setUnits("Connections Per Second")
_CufwPolicyConnSummaryTable_Object = MibTable
cufwPolicyConnSummaryTable = _CufwPolicyConnSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 3)
)
if mibBuilder.loadTexts:
    cufwPolicyConnSummaryTable.setStatus("current")
_CufwPolicyConnSummaryEntry_Object = MibTableRow
cufwPolicyConnSummaryEntry = _CufwPolicyConnSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 3, 1)
)
cufwPolicyConnSummaryEntry.setIndexNames(
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwPolConnPolicy"),
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwPolConnPolicyTargetType"),
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwPolConnPolicyTarget"),
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwPolConnProtocol"),
)
if mibBuilder.loadTexts:
    cufwPolicyConnSummaryEntry.setStatus("current")
_CufwPolConnPolicy_Type = CFWPolicy
_CufwPolConnPolicy_Object = MibTableColumn
cufwPolConnPolicy = _CufwPolConnPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 3, 1, 1),
    _CufwPolConnPolicy_Type()
)
cufwPolConnPolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cufwPolConnPolicy.setStatus("current")
_CufwPolConnPolicyTargetType_Type = CFWPolicyTargetType
_CufwPolConnPolicyTargetType_Object = MibTableColumn
cufwPolConnPolicyTargetType = _CufwPolConnPolicyTargetType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 3, 1, 2),
    _CufwPolConnPolicyTargetType_Type()
)
cufwPolConnPolicyTargetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cufwPolConnPolicyTargetType.setStatus("current")


class _CufwPolConnPolicyTarget_Type(CFWPolicyTarget):
    """Custom type cufwPolConnPolicyTarget based on CFWPolicyTarget"""
    subtypeSpec = CFWPolicyTarget.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CufwPolConnPolicyTarget_Type.__name__ = "CFWPolicyTarget"
_CufwPolConnPolicyTarget_Object = MibTableColumn
cufwPolConnPolicyTarget = _CufwPolConnPolicyTarget_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 3, 1, 3),
    _CufwPolConnPolicyTarget_Type()
)
cufwPolConnPolicyTarget.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cufwPolConnPolicyTarget.setStatus("current")
_CufwPolConnProtocol_Type = CFWNetworkProtocol
_CufwPolConnProtocol_Object = MibTableColumn
cufwPolConnProtocol = _CufwPolConnProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 3, 1, 4),
    _CufwPolConnProtocol_Type()
)
cufwPolConnProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cufwPolConnProtocol.setStatus("current")
_CufwPolConnNumAttempted_Type = Counter64
_CufwPolConnNumAttempted_Object = MibTableColumn
cufwPolConnNumAttempted = _CufwPolConnNumAttempted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 3, 1, 5),
    _CufwPolConnNumAttempted_Type()
)
cufwPolConnNumAttempted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwPolConnNumAttempted.setStatus("current")
if mibBuilder.loadTexts:
    cufwPolConnNumAttempted.setUnits("Connections")
_CufwPolConnNumSetupsAborted_Type = Counter64
_CufwPolConnNumSetupsAborted_Object = MibTableColumn
cufwPolConnNumSetupsAborted = _CufwPolConnNumSetupsAborted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 3, 1, 6),
    _CufwPolConnNumSetupsAborted_Type()
)
cufwPolConnNumSetupsAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwPolConnNumSetupsAborted.setStatus("current")
if mibBuilder.loadTexts:
    cufwPolConnNumSetupsAborted.setUnits("Connections")
_CufwPolConnNumPolicyDeclined_Type = Counter64
_CufwPolConnNumPolicyDeclined_Object = MibTableColumn
cufwPolConnNumPolicyDeclined = _CufwPolConnNumPolicyDeclined_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 3, 1, 7),
    _CufwPolConnNumPolicyDeclined_Type()
)
cufwPolConnNumPolicyDeclined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwPolConnNumPolicyDeclined.setStatus("current")
if mibBuilder.loadTexts:
    cufwPolConnNumPolicyDeclined.setUnits("Connections")
_CufwPolConnNumResDeclined_Type = Counter64
_CufwPolConnNumResDeclined_Object = MibTableColumn
cufwPolConnNumResDeclined = _CufwPolConnNumResDeclined_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 3, 1, 8),
    _CufwPolConnNumResDeclined_Type()
)
cufwPolConnNumResDeclined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwPolConnNumResDeclined.setStatus("current")
if mibBuilder.loadTexts:
    cufwPolConnNumResDeclined.setUnits("Connections")
_CufwPolConnNumHalfOpen_Type = Gauge32
_CufwPolConnNumHalfOpen_Object = MibTableColumn
cufwPolConnNumHalfOpen = _CufwPolConnNumHalfOpen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 3, 1, 9),
    _CufwPolConnNumHalfOpen_Type()
)
cufwPolConnNumHalfOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwPolConnNumHalfOpen.setStatus("current")
if mibBuilder.loadTexts:
    cufwPolConnNumHalfOpen.setUnits("Connections")
_CufwPolConnNumActive_Type = Gauge32
_CufwPolConnNumActive_Object = MibTableColumn
cufwPolConnNumActive = _CufwPolConnNumActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 3, 1, 10),
    _CufwPolConnNumActive_Type()
)
cufwPolConnNumActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwPolConnNumActive.setStatus("current")
if mibBuilder.loadTexts:
    cufwPolConnNumActive.setUnits("Connections")
_CufwPolConnNumAborted_Type = Counter64
_CufwPolConnNumAborted_Object = MibTableColumn
cufwPolConnNumAborted = _CufwPolConnNumAborted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 3, 1, 11),
    _CufwPolConnNumAborted_Type()
)
cufwPolConnNumAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwPolConnNumAborted.setStatus("current")
if mibBuilder.loadTexts:
    cufwPolConnNumAborted.setUnits("Connections")
_CufwPolicyAppConnSummaryTable_Object = MibTable
cufwPolicyAppConnSummaryTable = _CufwPolicyAppConnSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 4)
)
if mibBuilder.loadTexts:
    cufwPolicyAppConnSummaryTable.setStatus("current")
_CufwPolicyAppConnSummaryEntry_Object = MibTableRow
cufwPolicyAppConnSummaryEntry = _CufwPolicyAppConnSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 4, 1)
)
cufwPolicyAppConnSummaryEntry.setIndexNames(
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwPolAppConnPolicy"),
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwPolAppConnPolicyTargetType"),
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwPolAppConnPolicyTarget"),
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwPolAppConnProtocol"),
)
if mibBuilder.loadTexts:
    cufwPolicyAppConnSummaryEntry.setStatus("current")
_CufwPolAppConnPolicy_Type = CFWPolicy
_CufwPolAppConnPolicy_Object = MibTableColumn
cufwPolAppConnPolicy = _CufwPolAppConnPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 4, 1, 1),
    _CufwPolAppConnPolicy_Type()
)
cufwPolAppConnPolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cufwPolAppConnPolicy.setStatus("current")
_CufwPolAppConnPolicyTargetType_Type = CFWPolicyTargetType
_CufwPolAppConnPolicyTargetType_Object = MibTableColumn
cufwPolAppConnPolicyTargetType = _CufwPolAppConnPolicyTargetType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 4, 1, 2),
    _CufwPolAppConnPolicyTargetType_Type()
)
cufwPolAppConnPolicyTargetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cufwPolAppConnPolicyTargetType.setStatus("current")


class _CufwPolAppConnPolicyTarget_Type(CFWPolicyTarget):
    """Custom type cufwPolAppConnPolicyTarget based on CFWPolicyTarget"""
    subtypeSpec = CFWPolicyTarget.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CufwPolAppConnPolicyTarget_Type.__name__ = "CFWPolicyTarget"
_CufwPolAppConnPolicyTarget_Object = MibTableColumn
cufwPolAppConnPolicyTarget = _CufwPolAppConnPolicyTarget_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 4, 1, 3),
    _CufwPolAppConnPolicyTarget_Type()
)
cufwPolAppConnPolicyTarget.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cufwPolAppConnPolicyTarget.setStatus("current")
_CufwPolAppConnProtocol_Type = CFWApplicationProtocol
_CufwPolAppConnProtocol_Object = MibTableColumn
cufwPolAppConnProtocol = _CufwPolAppConnProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 4, 1, 4),
    _CufwPolAppConnProtocol_Type()
)
cufwPolAppConnProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cufwPolAppConnProtocol.setStatus("current")
_CufwPolAppConnNumAttempted_Type = Counter64
_CufwPolAppConnNumAttempted_Object = MibTableColumn
cufwPolAppConnNumAttempted = _CufwPolAppConnNumAttempted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 4, 1, 5),
    _CufwPolAppConnNumAttempted_Type()
)
cufwPolAppConnNumAttempted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwPolAppConnNumAttempted.setStatus("current")
if mibBuilder.loadTexts:
    cufwPolAppConnNumAttempted.setUnits("Connections")
_CufwPolAppConnNumSetupsAborted_Type = Counter64
_CufwPolAppConnNumSetupsAborted_Object = MibTableColumn
cufwPolAppConnNumSetupsAborted = _CufwPolAppConnNumSetupsAborted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 4, 1, 6),
    _CufwPolAppConnNumSetupsAborted_Type()
)
cufwPolAppConnNumSetupsAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwPolAppConnNumSetupsAborted.setStatus("current")
if mibBuilder.loadTexts:
    cufwPolAppConnNumSetupsAborted.setUnits("Connections")
_CufwPolAppConnNumPolicyDeclined_Type = Counter64
_CufwPolAppConnNumPolicyDeclined_Object = MibTableColumn
cufwPolAppConnNumPolicyDeclined = _CufwPolAppConnNumPolicyDeclined_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 4, 1, 7),
    _CufwPolAppConnNumPolicyDeclined_Type()
)
cufwPolAppConnNumPolicyDeclined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwPolAppConnNumPolicyDeclined.setStatus("current")
if mibBuilder.loadTexts:
    cufwPolAppConnNumPolicyDeclined.setUnits("Connections")
_CufwPolAppConnNumResDeclined_Type = Counter64
_CufwPolAppConnNumResDeclined_Object = MibTableColumn
cufwPolAppConnNumResDeclined = _CufwPolAppConnNumResDeclined_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 4, 1, 8),
    _CufwPolAppConnNumResDeclined_Type()
)
cufwPolAppConnNumResDeclined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwPolAppConnNumResDeclined.setStatus("current")
if mibBuilder.loadTexts:
    cufwPolAppConnNumResDeclined.setUnits("Connections")
_CufwPolAppConnNumHalfOpen_Type = Gauge32
_CufwPolAppConnNumHalfOpen_Object = MibTableColumn
cufwPolAppConnNumHalfOpen = _CufwPolAppConnNumHalfOpen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 4, 1, 9),
    _CufwPolAppConnNumHalfOpen_Type()
)
cufwPolAppConnNumHalfOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwPolAppConnNumHalfOpen.setStatus("current")
if mibBuilder.loadTexts:
    cufwPolAppConnNumHalfOpen.setUnits("Connections")
_CufwPolAppConnNumActive_Type = Gauge32
_CufwPolAppConnNumActive_Object = MibTableColumn
cufwPolAppConnNumActive = _CufwPolAppConnNumActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 4, 1, 10),
    _CufwPolAppConnNumActive_Type()
)
cufwPolAppConnNumActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwPolAppConnNumActive.setStatus("current")
if mibBuilder.loadTexts:
    cufwPolAppConnNumActive.setUnits("Connections")
_CufwPolAppConnNumAborted_Type = Counter64
_CufwPolAppConnNumAborted_Object = MibTableColumn
cufwPolAppConnNumAborted = _CufwPolAppConnNumAborted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 4, 1, 11),
    _CufwPolAppConnNumAborted_Type()
)
cufwPolAppConnNumAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwPolAppConnNumAborted.setStatus("current")
if mibBuilder.loadTexts:
    cufwPolAppConnNumAborted.setUnits("Connections")
_CuFwApplInspectionGrp_ObjectIdentity = ObjectIdentity
cuFwApplInspectionGrp = _CuFwApplInspectionGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 2)
)
_CufwAIAuditTrailEnabled_Type = TruthValue
_CufwAIAuditTrailEnabled_Object = MibScalar
cufwAIAuditTrailEnabled = _CufwAIAuditTrailEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 2, 1),
    _CufwAIAuditTrailEnabled_Type()
)
cufwAIAuditTrailEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cufwAIAuditTrailEnabled.setStatus("current")
_CufwAIAlertEnabled_Type = TruthValue
_CufwAIAlertEnabled_Object = MibScalar
cufwAIAlertEnabled = _CufwAIAlertEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 2, 2),
    _CufwAIAlertEnabled_Type()
)
cufwAIAlertEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cufwAIAlertEnabled.setStatus("current")
_CufwInspectionTable_Object = MibTable
cufwInspectionTable = _CufwInspectionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cufwInspectionTable.setStatus("current")
_CufwInspectionEntry_Object = MibTableRow
cufwInspectionEntry = _CufwInspectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 2, 3, 1)
)
cufwInspectionEntry.setIndexNames(
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwInspectionPolicyName"),
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwInspectionProtocol"),
)
if mibBuilder.loadTexts:
    cufwInspectionEntry.setStatus("current")


class _CufwInspectionPolicyName_Type(CFWPolicy):
    """Custom type cufwInspectionPolicyName based on CFWPolicy"""
    subtypeSpec = CFWPolicy.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CufwInspectionPolicyName_Type.__name__ = "CFWPolicy"
_CufwInspectionPolicyName_Object = MibTableColumn
cufwInspectionPolicyName = _CufwInspectionPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 2, 3, 1, 1),
    _CufwInspectionPolicyName_Type()
)
cufwInspectionPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cufwInspectionPolicyName.setStatus("current")
_CufwInspectionProtocol_Type = CFWApplicationProtocol
_CufwInspectionProtocol_Object = MibTableColumn
cufwInspectionProtocol = _CufwInspectionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 2, 3, 1, 2),
    _CufwInspectionProtocol_Type()
)
cufwInspectionProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cufwInspectionProtocol.setStatus("current")
_CufwInspectionStatus_Type = TruthValue
_CufwInspectionStatus_Object = MibTableColumn
cufwInspectionStatus = _CufwInspectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 2, 3, 1, 3),
    _CufwInspectionStatus_Type()
)
cufwInspectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwInspectionStatus.setStatus("current")
_CuFwUrlFilterGrp_ObjectIdentity = ObjectIdentity
cuFwUrlFilterGrp = _CuFwUrlFilterGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3)
)
_CufwUrlFilterGlobals_ObjectIdentity = ObjectIdentity
cufwUrlFilterGlobals = _CufwUrlFilterGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1)
)
_CufwUrlfFunctionEnabled_Type = TruthValue
_CufwUrlfFunctionEnabled_Object = MibScalar
cufwUrlfFunctionEnabled = _CufwUrlfFunctionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1, 1),
    _CufwUrlfFunctionEnabled_Type()
)
cufwUrlfFunctionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cufwUrlfFunctionEnabled.setStatus("current")
_CufwUrlfRequestsNumProcessed_Type = Counter64
_CufwUrlfRequestsNumProcessed_Object = MibScalar
cufwUrlfRequestsNumProcessed = _CufwUrlfRequestsNumProcessed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1, 2),
    _CufwUrlfRequestsNumProcessed_Type()
)
cufwUrlfRequestsNumProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfRequestsNumProcessed.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfRequestsNumProcessed.setUnits("Requests")
_CufwUrlfRequestsProcRate1_Type = Gauge32
_CufwUrlfRequestsProcRate1_Object = MibScalar
cufwUrlfRequestsProcRate1 = _CufwUrlfRequestsProcRate1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1, 3),
    _CufwUrlfRequestsProcRate1_Type()
)
cufwUrlfRequestsProcRate1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfRequestsProcRate1.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfRequestsProcRate1.setUnits("Requests per second")
_CufwUrlfRequestsProcRate5_Type = Gauge32
_CufwUrlfRequestsProcRate5_Object = MibScalar
cufwUrlfRequestsProcRate5 = _CufwUrlfRequestsProcRate5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1, 4),
    _CufwUrlfRequestsProcRate5_Type()
)
cufwUrlfRequestsProcRate5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfRequestsProcRate5.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfRequestsProcRate5.setUnits("Requests per second")
_CufwUrlfRequestsNumAllowed_Type = Counter64
_CufwUrlfRequestsNumAllowed_Object = MibScalar
cufwUrlfRequestsNumAllowed = _CufwUrlfRequestsNumAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1, 5),
    _CufwUrlfRequestsNumAllowed_Type()
)
cufwUrlfRequestsNumAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfRequestsNumAllowed.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfRequestsNumAllowed.setUnits("Requests")
_CufwUrlfRequestsNumDenied_Type = Counter64
_CufwUrlfRequestsNumDenied_Object = MibScalar
cufwUrlfRequestsNumDenied = _CufwUrlfRequestsNumDenied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1, 6),
    _CufwUrlfRequestsNumDenied_Type()
)
cufwUrlfRequestsNumDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfRequestsNumDenied.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfRequestsNumDenied.setUnits("Requests")
_CufwUrlfRequestsDeniedRate1_Type = Gauge32
_CufwUrlfRequestsDeniedRate1_Object = MibScalar
cufwUrlfRequestsDeniedRate1 = _CufwUrlfRequestsDeniedRate1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1, 7),
    _CufwUrlfRequestsDeniedRate1_Type()
)
cufwUrlfRequestsDeniedRate1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfRequestsDeniedRate1.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfRequestsDeniedRate1.setUnits("Requests per second")
_CufwUrlfRequestsDeniedRate5_Type = Gauge32
_CufwUrlfRequestsDeniedRate5_Object = MibScalar
cufwUrlfRequestsDeniedRate5 = _CufwUrlfRequestsDeniedRate5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1, 8),
    _CufwUrlfRequestsDeniedRate5_Type()
)
cufwUrlfRequestsDeniedRate5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfRequestsDeniedRate5.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfRequestsDeniedRate5.setUnits("Requests Per Second")
_CufwUrlfRequestsNumCacheAllowed_Type = Counter64
_CufwUrlfRequestsNumCacheAllowed_Object = MibScalar
cufwUrlfRequestsNumCacheAllowed = _CufwUrlfRequestsNumCacheAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1, 9),
    _CufwUrlfRequestsNumCacheAllowed_Type()
)
cufwUrlfRequestsNumCacheAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfRequestsNumCacheAllowed.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfRequestsNumCacheAllowed.setUnits("Requests")
_CufwUrlfRequestsNumCacheDenied_Type = Counter64
_CufwUrlfRequestsNumCacheDenied_Object = MibScalar
cufwUrlfRequestsNumCacheDenied = _CufwUrlfRequestsNumCacheDenied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1, 10),
    _CufwUrlfRequestsNumCacheDenied_Type()
)
cufwUrlfRequestsNumCacheDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfRequestsNumCacheDenied.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfRequestsNumCacheDenied.setUnits("Requests")
_CufwUrlfAllowModeReqNumAllowed_Type = Counter64
_CufwUrlfAllowModeReqNumAllowed_Object = MibScalar
cufwUrlfAllowModeReqNumAllowed = _CufwUrlfAllowModeReqNumAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1, 11),
    _CufwUrlfAllowModeReqNumAllowed_Type()
)
cufwUrlfAllowModeReqNumAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfAllowModeReqNumAllowed.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfAllowModeReqNumAllowed.setUnits("Requests")
_CufwUrlfAllowModeReqNumDenied_Type = Counter64
_CufwUrlfAllowModeReqNumDenied_Object = MibScalar
cufwUrlfAllowModeReqNumDenied = _CufwUrlfAllowModeReqNumDenied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1, 12),
    _CufwUrlfAllowModeReqNumDenied_Type()
)
cufwUrlfAllowModeReqNumDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfAllowModeReqNumDenied.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfAllowModeReqNumDenied.setUnits("Requests")
_CufwUrlfRequestsNumResDropped_Type = Counter64
_CufwUrlfRequestsNumResDropped_Object = MibScalar
cufwUrlfRequestsNumResDropped = _CufwUrlfRequestsNumResDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1, 13),
    _CufwUrlfRequestsNumResDropped_Type()
)
cufwUrlfRequestsNumResDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfRequestsNumResDropped.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfRequestsNumResDropped.setUnits("Requests")
_CufwUrlfRequestsResDropRate1_Type = Gauge32
_CufwUrlfRequestsResDropRate1_Object = MibScalar
cufwUrlfRequestsResDropRate1 = _CufwUrlfRequestsResDropRate1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1, 14),
    _CufwUrlfRequestsResDropRate1_Type()
)
cufwUrlfRequestsResDropRate1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfRequestsResDropRate1.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfRequestsResDropRate1.setUnits("Requests Per Second")
_CufwUrlfRequestsResDropRate5_Type = Gauge32
_CufwUrlfRequestsResDropRate5_Object = MibScalar
cufwUrlfRequestsResDropRate5 = _CufwUrlfRequestsResDropRate5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1, 15),
    _CufwUrlfRequestsResDropRate5_Type()
)
cufwUrlfRequestsResDropRate5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfRequestsResDropRate5.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfRequestsResDropRate5.setUnits("Requests Per Second")
_CufwUrlfNumServerTimeouts_Type = Counter64
_CufwUrlfNumServerTimeouts_Object = MibScalar
cufwUrlfNumServerTimeouts = _CufwUrlfNumServerTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1, 16),
    _CufwUrlfNumServerTimeouts_Type()
)
cufwUrlfNumServerTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfNumServerTimeouts.setStatus("current")
_CufwUrlfNumServerRetries_Type = Counter64
_CufwUrlfNumServerRetries_Object = MibScalar
cufwUrlfNumServerRetries = _CufwUrlfNumServerRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1, 17),
    _CufwUrlfNumServerRetries_Type()
)
cufwUrlfNumServerRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfNumServerRetries.setStatus("current")
_CufwUrlfResponsesNumLate_Type = Counter64
_CufwUrlfResponsesNumLate_Object = MibScalar
cufwUrlfResponsesNumLate = _CufwUrlfResponsesNumLate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1, 18),
    _CufwUrlfResponsesNumLate_Type()
)
cufwUrlfResponsesNumLate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfResponsesNumLate.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfResponsesNumLate.setUnits("Responses")
_CufwUrlfUrlAccRespsNumResDropped_Type = Counter64
_CufwUrlfUrlAccRespsNumResDropped_Object = MibScalar
cufwUrlfUrlAccRespsNumResDropped = _CufwUrlfUrlAccRespsNumResDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1, 19),
    _CufwUrlfUrlAccRespsNumResDropped_Type()
)
cufwUrlfUrlAccRespsNumResDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfUrlAccRespsNumResDropped.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfUrlAccRespsNumResDropped.setUnits("Responses")
_CufwUrlFilterResourceUsage_ObjectIdentity = ObjectIdentity
cufwUrlFilterResourceUsage = _CufwUrlFilterResourceUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 2)
)
_CufwUrlfResTotalRequestCacheSize_Type = Gauge32
_CufwUrlfResTotalRequestCacheSize_Object = MibScalar
cufwUrlfResTotalRequestCacheSize = _CufwUrlfResTotalRequestCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 2, 1),
    _CufwUrlfResTotalRequestCacheSize_Type()
)
cufwUrlfResTotalRequestCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfResTotalRequestCacheSize.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfResTotalRequestCacheSize.setUnits("KBytes")
_CufwUrlfResTotalRespCacheSize_Type = Gauge32
_CufwUrlfResTotalRespCacheSize_Object = MibScalar
cufwUrlfResTotalRespCacheSize = _CufwUrlfResTotalRespCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 2, 2),
    _CufwUrlfResTotalRespCacheSize_Type()
)
cufwUrlfResTotalRespCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfResTotalRespCacheSize.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfResTotalRespCacheSize.setUnits("KBytes")
_CufwUrlFilterServers_ObjectIdentity = ObjectIdentity
cufwUrlFilterServers = _CufwUrlFilterServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 3)
)
_CufwUrlfServerTable_Object = MibTable
cufwUrlfServerTable = _CufwUrlfServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    cufwUrlfServerTable.setStatus("current")
_CufwUrlfServerEntry_Object = MibTableRow
cufwUrlfServerEntry = _CufwUrlfServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 3, 1, 1)
)
cufwUrlfServerEntry.setIndexNames(
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfServerAddrType"),
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfServerAddress"),
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfServerPort"),
)
if mibBuilder.loadTexts:
    cufwUrlfServerEntry.setStatus("current")
_CufwUrlfServerAddrType_Type = InetAddressType
_CufwUrlfServerAddrType_Object = MibTableColumn
cufwUrlfServerAddrType = _CufwUrlfServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 3, 1, 1, 1),
    _CufwUrlfServerAddrType_Type()
)
cufwUrlfServerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cufwUrlfServerAddrType.setStatus("current")
_CufwUrlfServerAddress_Type = InetAddress
_CufwUrlfServerAddress_Object = MibTableColumn
cufwUrlfServerAddress = _CufwUrlfServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 3, 1, 1, 2),
    _CufwUrlfServerAddress_Type()
)
cufwUrlfServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cufwUrlfServerAddress.setStatus("current")
_CufwUrlfServerPort_Type = InetPortNumber
_CufwUrlfServerPort_Object = MibTableColumn
cufwUrlfServerPort = _CufwUrlfServerPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 3, 1, 1, 3),
    _CufwUrlfServerPort_Type()
)
cufwUrlfServerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cufwUrlfServerPort.setStatus("current")
_CufwUrlfServerVendor_Type = CFWUrlfVendorId
_CufwUrlfServerVendor_Object = MibTableColumn
cufwUrlfServerVendor = _CufwUrlfServerVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 3, 1, 1, 4),
    _CufwUrlfServerVendor_Type()
)
cufwUrlfServerVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfServerVendor.setStatus("current")
_CufwUrlfServerStatus_Type = CFWUrlServerStatus
_CufwUrlfServerStatus_Object = MibTableColumn
cufwUrlfServerStatus = _CufwUrlfServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 3, 1, 1, 5),
    _CufwUrlfServerStatus_Type()
)
cufwUrlfServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfServerStatus.setStatus("current")
_CufwUrlfServerReqsNumProcessed_Type = Counter64
_CufwUrlfServerReqsNumProcessed_Object = MibTableColumn
cufwUrlfServerReqsNumProcessed = _CufwUrlfServerReqsNumProcessed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 3, 1, 1, 6),
    _CufwUrlfServerReqsNumProcessed_Type()
)
cufwUrlfServerReqsNumProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfServerReqsNumProcessed.setStatus("current")
_CufwUrlfServerReqsNumAllowed_Type = Counter64
_CufwUrlfServerReqsNumAllowed_Object = MibTableColumn
cufwUrlfServerReqsNumAllowed = _CufwUrlfServerReqsNumAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 3, 1, 1, 7),
    _CufwUrlfServerReqsNumAllowed_Type()
)
cufwUrlfServerReqsNumAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfServerReqsNumAllowed.setStatus("current")
_CufwUrlfServerReqsNumDenied_Type = Counter64
_CufwUrlfServerReqsNumDenied_Object = MibTableColumn
cufwUrlfServerReqsNumDenied = _CufwUrlfServerReqsNumDenied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 3, 1, 1, 8),
    _CufwUrlfServerReqsNumDenied_Type()
)
cufwUrlfServerReqsNumDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfServerReqsNumDenied.setStatus("current")
_CufwUrlfServerNumTimeouts_Type = Counter64
_CufwUrlfServerNumTimeouts_Object = MibTableColumn
cufwUrlfServerNumTimeouts = _CufwUrlfServerNumTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 3, 1, 1, 9),
    _CufwUrlfServerNumTimeouts_Type()
)
cufwUrlfServerNumTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfServerNumTimeouts.setStatus("current")
_CufwUrlfServerNumRetries_Type = Counter64
_CufwUrlfServerNumRetries_Object = MibTableColumn
cufwUrlfServerNumRetries = _CufwUrlfServerNumRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 3, 1, 1, 10),
    _CufwUrlfServerNumRetries_Type()
)
cufwUrlfServerNumRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfServerNumRetries.setStatus("current")
_CufwUrlfServerRespsNumReceived_Type = Counter64
_CufwUrlfServerRespsNumReceived_Object = MibTableColumn
cufwUrlfServerRespsNumReceived = _CufwUrlfServerRespsNumReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 3, 1, 1, 11),
    _CufwUrlfServerRespsNumReceived_Type()
)
cufwUrlfServerRespsNumReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfServerRespsNumReceived.setStatus("current")
_CufwUrlfServerRespsNumLate_Type = Counter64
_CufwUrlfServerRespsNumLate_Object = MibTableColumn
cufwUrlfServerRespsNumLate = _CufwUrlfServerRespsNumLate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 3, 1, 1, 12),
    _CufwUrlfServerRespsNumLate_Type()
)
cufwUrlfServerRespsNumLate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfServerRespsNumLate.setStatus("current")
_CufwUrlfServerAvgRespTime1_Type = Gauge32
_CufwUrlfServerAvgRespTime1_Object = MibTableColumn
cufwUrlfServerAvgRespTime1 = _CufwUrlfServerAvgRespTime1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 3, 1, 1, 13),
    _CufwUrlfServerAvgRespTime1_Type()
)
cufwUrlfServerAvgRespTime1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfServerAvgRespTime1.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfServerAvgRespTime1.setUnits("seconds")
_CufwUrlfServerAvgRespTime5_Type = Gauge32
_CufwUrlfServerAvgRespTime5_Object = MibTableColumn
cufwUrlfServerAvgRespTime5 = _CufwUrlfServerAvgRespTime5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 3, 1, 1, 14),
    _CufwUrlfServerAvgRespTime5_Type()
)
cufwUrlfServerAvgRespTime5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfServerAvgRespTime5.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfServerAvgRespTime5.setUnits("seconds")
_CuFwFailoverGrp_ObjectIdentity = ObjectIdentity
cuFwFailoverGrp = _CuFwFailoverGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4)
)
_CuFwFailoverGlobals_ObjectIdentity = ObjectIdentity
cuFwFailoverGlobals = _CuFwFailoverGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 1)
)
_CufwFOEnabled_Type = TruthValue
_CufwFOEnabled_Object = MibScalar
cufwFOEnabled = _CufwFOEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 1, 1),
    _CufwFOEnabled_Type()
)
cufwFOEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOEnabled.setStatus("current")
_CufwFOUnitDesignation_Type = Hardware
_CufwFOUnitDesignation_Object = MibScalar
cufwFOUnitDesignation = _CufwFOUnitDesignation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 1, 2),
    _CufwFOUnitDesignation_Type()
)
cufwFOUnitDesignation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOUnitDesignation.setStatus("current")
_CufwFOLink_Type = InterfaceIndex
_CufwFOLink_Object = MibScalar
cufwFOLink = _CufwFOLink_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 1, 3),
    _CufwFOLink_Type()
)
cufwFOLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOLink.setStatus("current")
_CufwFOStateLink_Type = InterfaceIndex
_CufwFOStateLink_Object = MibScalar
cufwFOStateLink = _CufwFOStateLink_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 1, 4),
    _CufwFOStateLink_Type()
)
cufwFOStateLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOStateLink.setStatus("current")
_CufwFOStdbyConfigLocked_Type = TruthValue
_CufwFOStdbyConfigLocked_Object = MibScalar
cufwFOStdbyConfigLocked = _CufwFOStdbyConfigLocked_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 1, 5),
    _CufwFOStdbyConfigLocked_Type()
)
cufwFOStdbyConfigLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOStdbyConfigLocked.setStatus("current")


class _CufwFOEncryption_Type(Integer32):
    """Custom type cufwFOEncryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_CufwFOEncryption_Type.__name__ = "Integer32"
_CufwFOEncryption_Object = MibScalar
cufwFOEncryption = _CufwFOEncryption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 1, 6),
    _CufwFOEncryption_Type()
)
cufwFOEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOEncryption.setStatus("current")
_CufwFOSerialNumOurs_Type = SnmpAdminString
_CufwFOSerialNumOurs_Object = MibScalar
cufwFOSerialNumOurs = _CufwFOSerialNumOurs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 1, 7),
    _CufwFOSerialNumOurs_Type()
)
cufwFOSerialNumOurs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOSerialNumOurs.setStatus("current")
_CufwFOSerialNumMate_Type = SnmpAdminString
_CufwFOSerialNumMate_Object = MibScalar
cufwFOSerialNumMate = _CufwFOSerialNumMate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 1, 8),
    _CufwFOSerialNumMate_Type()
)
cufwFOSerialNumMate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOSerialNumMate.setStatus("current")
_CufwFOSwVersionOurs_Type = SnmpAdminString
_CufwFOSwVersionOurs_Object = MibScalar
cufwFOSwVersionOurs = _CufwFOSwVersionOurs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 1, 9),
    _CufwFOSwVersionOurs_Type()
)
cufwFOSwVersionOurs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOSwVersionOurs.setStatus("current")
_CufwFOSwVersionMate_Type = SnmpAdminString
_CufwFOSwVersionMate_Object = MibScalar
cufwFOSwVersionMate = _CufwFOSwVersionMate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 1, 10),
    _CufwFOSwVersionMate_Type()
)
cufwFOSwVersionMate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOSwVersionMate.setStatus("current")


class _CufwFOUnitPolltime_Type(Integer32):
    """Custom type cufwFOUnitPolltime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 15000),
    )


_CufwFOUnitPolltime_Type.__name__ = "Integer32"
_CufwFOUnitPolltime_Object = MibScalar
cufwFOUnitPolltime = _CufwFOUnitPolltime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 1, 11),
    _CufwFOUnitPolltime_Type()
)
cufwFOUnitPolltime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOUnitPolltime.setStatus("current")
if mibBuilder.loadTexts:
    cufwFOUnitPolltime.setUnits("millisec")


class _CufwFOUnitHoldtime_Type(Integer32):
    """Custom type cufwFOUnitHoldtime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(800, 45000),
    )


_CufwFOUnitHoldtime_Type.__name__ = "Integer32"
_CufwFOUnitHoldtime_Object = MibScalar
cufwFOUnitHoldtime = _CufwFOUnitHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 1, 12),
    _CufwFOUnitHoldtime_Type()
)
cufwFOUnitHoldtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOUnitHoldtime.setStatus("current")
if mibBuilder.loadTexts:
    cufwFOUnitHoldtime.setUnits("millisec")
_CufwFOUnitBfdEnabled_Type = TruthValue
_CufwFOUnitBfdEnabled_Object = MibScalar
cufwFOUnitBfdEnabled = _CufwFOUnitBfdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 1, 13),
    _CufwFOUnitBfdEnabled_Type()
)
cufwFOUnitBfdEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOUnitBfdEnabled.setStatus("current")


class _CufwFOLinkStatePolltime_Type(Integer32):
    """Custom type cufwFOLinkStatePolltime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 799),
    )


_CufwFOLinkStatePolltime_Type.__name__ = "Integer32"
_CufwFOLinkStatePolltime_Object = MibScalar
cufwFOLinkStatePolltime = _CufwFOLinkStatePolltime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 1, 14),
    _CufwFOLinkStatePolltime_Type()
)
cufwFOLinkStatePolltime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOLinkStatePolltime.setStatus("current")
if mibBuilder.loadTexts:
    cufwFOLinkStatePolltime.setUnits("millisec")


class _CufwFOInterfacePolicy_Type(Integer32):
    """Custom type cufwFOInterfacePolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1025),
    )


_CufwFOInterfacePolicy_Type.__name__ = "Integer32"
_CufwFOInterfacePolicy_Object = MibScalar
cufwFOInterfacePolicy = _CufwFOInterfacePolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 1, 15),
    _CufwFOInterfacePolicy_Type()
)
cufwFOInterfacePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOInterfacePolicy.setStatus("current")
_CufwFOMonitoredInterfaces_Type = Gauge32
_CufwFOMonitoredInterfaces_Object = MibScalar
cufwFOMonitoredInterfaces = _CufwFOMonitoredInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 1, 16),
    _CufwFOMonitoredInterfaces_Type()
)
cufwFOMonitoredInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOMonitoredInterfaces.setStatus("current")


class _CufwFOInterfacePolltime_Type(Integer32):
    """Custom type cufwFOInterfacePolltime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 15000),
    )


_CufwFOInterfacePolltime_Type.__name__ = "Integer32"
_CufwFOInterfacePolltime_Object = MibScalar
cufwFOInterfacePolltime = _CufwFOInterfacePolltime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 1, 17),
    _CufwFOInterfacePolltime_Type()
)
cufwFOInterfacePolltime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOInterfacePolltime.setStatus("current")
if mibBuilder.loadTexts:
    cufwFOInterfacePolltime.setUnits("millisec")


class _CufwFOInterfaceHoldtime_Type(Integer32):
    """Custom type cufwFOInterfaceHoldtime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000, 75000),
    )


_CufwFOInterfaceHoldtime_Type.__name__ = "Integer32"
_CufwFOInterfaceHoldtime_Object = MibScalar
cufwFOInterfaceHoldtime = _CufwFOInterfaceHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 1, 18),
    _CufwFOInterfaceHoldtime_Type()
)
cufwFOInterfaceHoldtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOInterfaceHoldtime.setStatus("current")
if mibBuilder.loadTexts:
    cufwFOInterfaceHoldtime.setUnits("millisec")
_CufwFOReplicationHttp_Type = TruthValue
_CufwFOReplicationHttp_Object = MibScalar
cufwFOReplicationHttp = _CufwFOReplicationHttp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 1, 19),
    _CufwFOReplicationHttp_Type()
)
cufwFOReplicationHttp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOReplicationHttp.setStatus("current")
_CufwFOReplicationRate_Type = Gauge32
_CufwFOReplicationRate_Object = MibScalar
cufwFOReplicationRate = _CufwFOReplicationRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 1, 20),
    _CufwFOReplicationRate_Type()
)
cufwFOReplicationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOReplicationRate.setStatus("current")
if mibBuilder.loadTexts:
    cufwFOReplicationRate.setUnits("Connections Per Second")
_CuFwFailoverStatus_ObjectIdentity = ObjectIdentity
cuFwFailoverStatus = _CuFwFailoverStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 2)
)
_CufwFOGrpStatusTable_Object = MibTable
cufwFOGrpStatusTable = _CufwFOGrpStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    cufwFOGrpStatusTable.setStatus("current")
_CufwFOGrpStatusEntry_Object = MibTableRow
cufwFOGrpStatusEntry = _CufwFOGrpStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 2, 1, 1)
)
cufwFOGrpStatusEntry.setIndexNames(
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwFOGroupIndex"),
)
if mibBuilder.loadTexts:
    cufwFOGrpStatusEntry.setStatus("current")
_CufwFOGroupIndex_Type = CUfwFOGroupId
_CufwFOGroupIndex_Object = MibTableColumn
cufwFOGroupIndex = _CufwFOGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 2, 1, 1, 1),
    _CufwFOGroupIndex_Type()
)
cufwFOGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOGroupIndex.setStatus("current")
_CufwFOGrpLastFailoverAt_Type = DisplayString
_CufwFOGrpLastFailoverAt_Object = MibTableColumn
cufwFOGrpLastFailoverAt = _CufwFOGrpLastFailoverAt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 2, 1, 1, 2),
    _CufwFOGrpLastFailoverAt_Type()
)
cufwFOGrpLastFailoverAt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOGrpLastFailoverAt.setStatus("current")
_CufwFOGrpHAstate_Type = HardwareStatus
_CufwFOGrpHAstate_Object = MibTableColumn
cufwFOGrpHAstate = _CufwFOGrpHAstate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 2, 1, 1, 3),
    _CufwFOGrpHAstate_Type()
)
cufwFOGrpHAstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOGrpHAstate.setStatus("current")
_CufwFOGrpUpTime_Type = Gauge32
_CufwFOGrpUpTime_Object = MibTableColumn
cufwFOGrpUpTime = _CufwFOGrpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 2, 1, 1, 4),
    _CufwFOGrpUpTime_Type()
)
cufwFOGrpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOGrpUpTime.setStatus("current")
if mibBuilder.loadTexts:
    cufwFOGrpUpTime.setUnits("Seconds")
_CufwFOGrpContextCount_Type = Gauge32
_CufwFOGrpContextCount_Object = MibTableColumn
cufwFOGrpContextCount = _CufwFOGrpContextCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 2, 1, 1, 5),
    _CufwFOGrpContextCount_Type()
)
cufwFOGrpContextCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOGrpContextCount.setStatus("current")
_CufwFOInterfaceTable_Object = MibTable
cufwFOInterfaceTable = _CufwFOInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    cufwFOInterfaceTable.setStatus("current")
_CufwFOInterfaceEntry_Object = MibTableRow
cufwFOInterfaceEntry = _CufwFOInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 2, 2, 1)
)
cufwFOInterfaceEntry.setIndexNames(
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwFOGroupIndex"),
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwContextId"),
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwContextifIndex"),
)
if mibBuilder.loadTexts:
    cufwFOInterfaceEntry.setStatus("current")
_CufwFOGrpId_Type = CUfwFOGroupId
_CufwFOGrpId_Object = MibTableColumn
cufwFOGrpId = _CufwFOGrpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 2, 2, 1, 1),
    _CufwFOGrpId_Type()
)
cufwFOGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOGrpId.setStatus("current")


class _CufwContextId_Type(Integer32):
    """Custom type cufwContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_CufwContextId_Type.__name__ = "Integer32"
_CufwContextId_Object = MibTableColumn
cufwContextId = _CufwContextId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 2, 2, 1, 2),
    _CufwContextId_Type()
)
cufwContextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwContextId.setStatus("current")
_CufwContextifIndex_Type = InterfaceIndex
_CufwContextifIndex_Object = MibTableColumn
cufwContextifIndex = _CufwContextifIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 2, 2, 1, 3),
    _CufwContextifIndex_Type()
)
cufwContextifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwContextifIndex.setStatus("current")
_CufwFOInterfaceMonitoring_Type = CUfwInterfaceMonitor
_CufwFOInterfaceMonitoring_Object = MibTableColumn
cufwFOInterfaceMonitoring = _CufwFOInterfaceMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 2, 2, 1, 4),
    _CufwFOInterfaceMonitoring_Type()
)
cufwFOInterfaceMonitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOInterfaceMonitoring.setStatus("current")
_CufwFOInterfaceStatus_Type = CUfwInterfaceHealth
_CufwFOInterfaceStatus_Object = MibTableColumn
cufwFOInterfaceStatus = _CufwFOInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 2, 2, 1, 5),
    _CufwFOInterfaceStatus_Type()
)
cufwFOInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOInterfaceStatus.setStatus("current")
_CuFwFailoverStatistics_ObjectIdentity = ObjectIdentity
cuFwFailoverStatistics = _CuFwFailoverStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 3)
)
_CufwFOStatefulUpdateEnabled_Type = TruthValue
_CufwFOStatefulUpdateEnabled_Object = MibScalar
cufwFOStatefulUpdateEnabled = _CufwFOStatefulUpdateEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 3, 1),
    _CufwFOStatefulUpdateEnabled_Type()
)
cufwFOStatefulUpdateEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOStatefulUpdateEnabled.setStatus("current")
_CufwFOLogicalUpdatesTable_Object = MibTable
cufwFOLogicalUpdatesTable = _CufwFOLogicalUpdatesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 3, 2)
)
if mibBuilder.loadTexts:
    cufwFOLogicalUpdatesTable.setStatus("current")
_CufwFOLogicalUpdateEntry_Object = MibTableRow
cufwFOLogicalUpdateEntry = _CufwFOLogicalUpdateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 3, 2, 1)
)
cufwFOLogicalUpdateEntry.setIndexNames(
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwFOGroupIdx"),
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwFOCLientId"),
)
if mibBuilder.loadTexts:
    cufwFOLogicalUpdateEntry.setStatus("current")
_CufwFOGroupIdx_Type = CUfwFOGroupId
_CufwFOGroupIdx_Object = MibTableColumn
cufwFOGroupIdx = _CufwFOGroupIdx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 3, 2, 1, 1),
    _CufwFOGroupIdx_Type()
)
cufwFOGroupIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOGroupIdx.setStatus("current")


class _CufwFOCLientId_Type(Integer32):
    """Custom type cufwFOCLientId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_CufwFOCLientId_Type.__name__ = "Integer32"
_CufwFOCLientId_Object = MibTableColumn
cufwFOCLientId = _CufwFOCLientId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 3, 2, 1, 2),
    _CufwFOCLientId_Type()
)
cufwFOCLientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOCLientId.setStatus("current")


class _CufwFOCLientName_Type(DisplayString):
    """Custom type cufwFOCLientName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CufwFOCLientName_Type.__name__ = "DisplayString"
_CufwFOCLientName_Object = MibTableColumn
cufwFOCLientName = _CufwFOCLientName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 3, 2, 1, 3),
    _CufwFOCLientName_Type()
)
cufwFOCLientName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOCLientName.setStatus("current")
_CufwFOLUTransmitCount_Type = Counter32
_CufwFOLUTransmitCount_Object = MibTableColumn
cufwFOLUTransmitCount = _CufwFOLUTransmitCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 3, 2, 1, 4),
    _CufwFOLUTransmitCount_Type()
)
cufwFOLUTransmitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOLUTransmitCount.setStatus("current")
_CufwFOLUTransmitErrors_Type = Counter32
_CufwFOLUTransmitErrors_Object = MibTableColumn
cufwFOLUTransmitErrors = _CufwFOLUTransmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 3, 2, 1, 5),
    _CufwFOLUTransmitErrors_Type()
)
cufwFOLUTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOLUTransmitErrors.setStatus("current")
_CufwFOLUReceiveCount_Type = Counter32
_CufwFOLUReceiveCount_Object = MibTableColumn
cufwFOLUReceiveCount = _CufwFOLUReceiveCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 3, 2, 1, 6),
    _CufwFOLUReceiveCount_Type()
)
cufwFOLUReceiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOLUReceiveCount.setStatus("current")
_CufwFOLUReceiveErrors_Type = Counter32
_CufwFOLUReceiveErrors_Object = MibTableColumn
cufwFOLUReceiveErrors = _CufwFOLUReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 3, 2, 1, 7),
    _CufwFOLUReceiveErrors_Type()
)
cufwFOLUReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOLUReceiveErrors.setStatus("current")
_CuFwFailoverHistory_ObjectIdentity = ObjectIdentity
cuFwFailoverHistory = _CuFwFailoverHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 4)
)
_CuFwFOMaxStateEvents_Type = Integer32
_CuFwFOMaxStateEvents_Object = MibScalar
cuFwFOMaxStateEvents = _CuFwFOMaxStateEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 4, 1),
    _CuFwFOMaxStateEvents_Type()
)
cuFwFOMaxStateEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuFwFOMaxStateEvents.setStatus("current")
_CufwFOHistoryEvTable_Object = MibTable
cufwFOHistoryEvTable = _CufwFOHistoryEvTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 4, 3)
)
if mibBuilder.loadTexts:
    cufwFOHistoryEvTable.setStatus("current")
_CufwFOHistoryEvEntry_Object = MibTableRow
cufwFOHistoryEvEntry = _CufwFOHistoryEvEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 4, 3, 1)
)
cufwFOHistoryEvEntry.setIndexNames(
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwFOGrpIndex"),
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwFOHistoryIndex"),
)
if mibBuilder.loadTexts:
    cufwFOHistoryEvEntry.setStatus("current")
_CufwFOGrpIndex_Type = CUfwFOGroupId
_CufwFOGrpIndex_Object = MibTableColumn
cufwFOGrpIndex = _CufwFOGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 4, 3, 1, 1),
    _CufwFOGrpIndex_Type()
)
cufwFOGrpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOGrpIndex.setStatus("current")
_CufwFOHistoryIndex_Type = Integer32
_CufwFOHistoryIndex_Object = MibTableColumn
cufwFOHistoryIndex = _CufwFOHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 4, 3, 1, 2),
    _CufwFOHistoryIndex_Type()
)
cufwFOHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOHistoryIndex.setStatus("current")
_CufwFOGrpHAFromState_Type = CUfwFOState
_CufwFOGrpHAFromState_Object = MibTableColumn
cufwFOGrpHAFromState = _CufwFOGrpHAFromState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 4, 3, 1, 3),
    _CufwFOGrpHAFromState_Type()
)
cufwFOGrpHAFromState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOGrpHAFromState.setStatus("current")
_CufwFOGrpHAToState_Type = CUfwFOState
_CufwFOGrpHAToState_Object = MibTableColumn
cufwFOGrpHAToState = _CufwFOGrpHAToState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 4, 3, 1, 4),
    _CufwFOGrpHAToState_Type()
)
cufwFOGrpHAToState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOGrpHAToState.setStatus("current")
_CufwFOGrpTransitionAt_Type = DisplayString
_CufwFOGrpTransitionAt_Object = MibTableColumn
cufwFOGrpTransitionAt = _CufwFOGrpTransitionAt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 4, 3, 1, 5),
    _CufwFOGrpTransitionAt_Type()
)
cufwFOGrpTransitionAt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOGrpTransitionAt.setStatus("current")
_CufwFOGrpTransitionReason_Type = DisplayString
_CufwFOGrpTransitionReason_Object = MibTableColumn
cufwFOGrpTransitionReason = _CufwFOGrpTransitionReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4, 4, 3, 1, 6),
    _CufwFOGrpTransitionReason_Type()
)
cufwFOGrpTransitionReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwFOGrpTransitionReason.setStatus("current")
_CuFwAaicGrp_ObjectIdentity = ObjectIdentity
cuFwAaicGrp = _CuFwAaicGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5)
)
_CufwAaicGlobals_ObjectIdentity = ObjectIdentity
cufwAaicGlobals = _CufwAaicGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 1)
)
_CufwAaicGlobalNumBadProtocolOps_Type = Counter64
_CufwAaicGlobalNumBadProtocolOps_Object = MibScalar
cufwAaicGlobalNumBadProtocolOps = _CufwAaicGlobalNumBadProtocolOps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 1, 1),
    _CufwAaicGlobalNumBadProtocolOps_Type()
)
cufwAaicGlobalNumBadProtocolOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAaicGlobalNumBadProtocolOps.setStatus("current")
if mibBuilder.loadTexts:
    cufwAaicGlobalNumBadProtocolOps.setUnits("Protocol Data Units")
_CufwAaicGlobalNumBadPDUSize_Type = Counter64
_CufwAaicGlobalNumBadPDUSize_Object = MibScalar
cufwAaicGlobalNumBadPDUSize = _CufwAaicGlobalNumBadPDUSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 1, 2),
    _CufwAaicGlobalNumBadPDUSize_Type()
)
cufwAaicGlobalNumBadPDUSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAaicGlobalNumBadPDUSize.setStatus("current")
if mibBuilder.loadTexts:
    cufwAaicGlobalNumBadPDUSize.setUnits("Protocol Data Units")
_CufwAaicGlobalNumBadPortRange_Type = Counter64
_CufwAaicGlobalNumBadPortRange_Object = MibScalar
cufwAaicGlobalNumBadPortRange = _CufwAaicGlobalNumBadPortRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 1, 3),
    _CufwAaicGlobalNumBadPortRange_Type()
)
cufwAaicGlobalNumBadPortRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAaicGlobalNumBadPortRange.setStatus("current")
if mibBuilder.loadTexts:
    cufwAaicGlobalNumBadPortRange.setUnits("Protocol Data Units")
_CufwAaicProtocolStats_ObjectIdentity = ObjectIdentity
cufwAaicProtocolStats = _CufwAaicProtocolStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 2)
)
_CufwAaicHttpProtocolStats_ObjectIdentity = ObjectIdentity
cufwAaicHttpProtocolStats = _CufwAaicHttpProtocolStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 2, 1)
)
_CufwAaicHttpNumBadProtocolOps_Type = Counter64
_CufwAaicHttpNumBadProtocolOps_Object = MibScalar
cufwAaicHttpNumBadProtocolOps = _CufwAaicHttpNumBadProtocolOps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 2, 1, 1),
    _CufwAaicHttpNumBadProtocolOps_Type()
)
cufwAaicHttpNumBadProtocolOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAaicHttpNumBadProtocolOps.setStatus("current")
if mibBuilder.loadTexts:
    cufwAaicHttpNumBadProtocolOps.setUnits("HTTP Protocol Data Units")
_CufwAaicHttpNumBadPDUSize_Type = Counter64
_CufwAaicHttpNumBadPDUSize_Object = MibScalar
cufwAaicHttpNumBadPDUSize = _CufwAaicHttpNumBadPDUSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 2, 1, 2),
    _CufwAaicHttpNumBadPDUSize_Type()
)
cufwAaicHttpNumBadPDUSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAaicHttpNumBadPDUSize.setStatus("current")
if mibBuilder.loadTexts:
    cufwAaicHttpNumBadPDUSize.setUnits("HTTP Protocol Data Units")
_CufwAaicHttpNumTunneledConns_Type = Counter64
_CufwAaicHttpNumTunneledConns_Object = MibScalar
cufwAaicHttpNumTunneledConns = _CufwAaicHttpNumTunneledConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 2, 1, 3),
    _CufwAaicHttpNumTunneledConns_Type()
)
cufwAaicHttpNumTunneledConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAaicHttpNumTunneledConns.setStatus("current")
if mibBuilder.loadTexts:
    cufwAaicHttpNumTunneledConns.setUnits("Connections")
_CufwAaicHttpNumLargeURIs_Type = Counter64
_CufwAaicHttpNumLargeURIs_Object = MibScalar
cufwAaicHttpNumLargeURIs = _CufwAaicHttpNumLargeURIs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 2, 1, 4),
    _CufwAaicHttpNumLargeURIs_Type()
)
cufwAaicHttpNumLargeURIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAaicHttpNumLargeURIs.setStatus("current")
if mibBuilder.loadTexts:
    cufwAaicHttpNumLargeURIs.setUnits("HTTP Protocol Data Units")
_CufwAaicHttpNumBadContent_Type = Counter64
_CufwAaicHttpNumBadContent_Object = MibScalar
cufwAaicHttpNumBadContent = _CufwAaicHttpNumBadContent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 2, 1, 5),
    _CufwAaicHttpNumBadContent_Type()
)
cufwAaicHttpNumBadContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAaicHttpNumBadContent.setStatus("current")
if mibBuilder.loadTexts:
    cufwAaicHttpNumBadContent.setUnits("HTTP Protocol Data Units")
_CufwAaicHttpNumMismatchContent_Type = Counter64
_CufwAaicHttpNumMismatchContent_Object = MibScalar
cufwAaicHttpNumMismatchContent = _CufwAaicHttpNumMismatchContent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 2, 1, 6),
    _CufwAaicHttpNumMismatchContent_Type()
)
cufwAaicHttpNumMismatchContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAaicHttpNumMismatchContent.setStatus("current")
if mibBuilder.loadTexts:
    cufwAaicHttpNumMismatchContent.setUnits("HTTP Protocol Data Units")
_CufwAaicHttpNumDoubleEncodedPkts_Type = Counter64
_CufwAaicHttpNumDoubleEncodedPkts_Object = MibScalar
cufwAaicHttpNumDoubleEncodedPkts = _CufwAaicHttpNumDoubleEncodedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 2, 1, 7),
    _CufwAaicHttpNumDoubleEncodedPkts_Type()
)
cufwAaicHttpNumDoubleEncodedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAaicHttpNumDoubleEncodedPkts.setStatus("current")
if mibBuilder.loadTexts:
    cufwAaicHttpNumDoubleEncodedPkts.setUnits("HTTP Protocol Data Units")
_CufwAaicEngineStats_ObjectIdentity = ObjectIdentity
cufwAaicEngineStats = _CufwAaicEngineStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 3)
)
_CufwAaicLinaSnortStats_ObjectIdentity = ObjectIdentity
cufwAaicLinaSnortStats = _CufwAaicLinaSnortStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 3, 1)
)
_CufwAaicPassedSnortCount_Type = Counter64
_CufwAaicPassedSnortCount_Object = MibScalar
cufwAaicPassedSnortCount = _CufwAaicPassedSnortCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 3, 1, 1),
    _CufwAaicPassedSnortCount_Type()
)
cufwAaicPassedSnortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAaicPassedSnortCount.setStatus("current")
if mibBuilder.loadTexts:
    cufwAaicPassedSnortCount.setUnits("Packets")
_CufwAaicBlockedSnortCount_Type = Counter64
_CufwAaicBlockedSnortCount_Object = MibScalar
cufwAaicBlockedSnortCount = _CufwAaicBlockedSnortCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 3, 1, 2),
    _CufwAaicBlockedSnortCount_Type()
)
cufwAaicBlockedSnortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAaicBlockedSnortCount.setStatus("current")
if mibBuilder.loadTexts:
    cufwAaicBlockedSnortCount.setUnits("Packets")
_CufwAaicInjbySnortCount_Type = Counter64
_CufwAaicInjbySnortCount_Object = MibScalar
cufwAaicInjbySnortCount = _CufwAaicInjbySnortCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 3, 1, 3),
    _CufwAaicInjbySnortCount_Type()
)
cufwAaicInjbySnortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAaicInjbySnortCount.setStatus("current")
if mibBuilder.loadTexts:
    cufwAaicInjbySnortCount.setUnits("Packets")
_CufwAaicBypassSnortDownCount_Type = Counter64
_CufwAaicBypassSnortDownCount_Object = MibScalar
cufwAaicBypassSnortDownCount = _CufwAaicBypassSnortDownCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 3, 1, 4),
    _CufwAaicBypassSnortDownCount_Type()
)
cufwAaicBypassSnortDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAaicBypassSnortDownCount.setStatus("current")
if mibBuilder.loadTexts:
    cufwAaicBypassSnortDownCount.setUnits("Packets")
_CufwAaicBypassSnortBusyCount_Type = Counter64
_CufwAaicBypassSnortBusyCount_Object = MibScalar
cufwAaicBypassSnortBusyCount = _CufwAaicBypassSnortBusyCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 3, 1, 5),
    _CufwAaicBypassSnortBusyCount_Type()
)
cufwAaicBypassSnortBusyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAaicBypassSnortBusyCount.setStatus("current")
if mibBuilder.loadTexts:
    cufwAaicBypassSnortBusyCount.setUnits("Packets")
_CufwAaicFastfwdFlowsCount_Type = Counter64
_CufwAaicFastfwdFlowsCount_Object = MibScalar
cufwAaicFastfwdFlowsCount = _CufwAaicFastfwdFlowsCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 3, 1, 6),
    _CufwAaicFastfwdFlowsCount_Type()
)
cufwAaicFastfwdFlowsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAaicFastfwdFlowsCount.setStatus("current")
if mibBuilder.loadTexts:
    cufwAaicFastfwdFlowsCount.setUnits("Flow")
_CufwAaicBlacklistedFlowsCount_Type = Counter64
_CufwAaicBlacklistedFlowsCount_Object = MibScalar
cufwAaicBlacklistedFlowsCount = _CufwAaicBlacklistedFlowsCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 3, 1, 7),
    _CufwAaicBlacklistedFlowsCount_Type()
)
cufwAaicBlacklistedFlowsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAaicBlacklistedFlowsCount.setStatus("current")
if mibBuilder.loadTexts:
    cufwAaicBlacklistedFlowsCount.setUnits("Flow")
_CufwAaicStartofFlowEvCount_Type = Counter64
_CufwAaicStartofFlowEvCount_Object = MibScalar
cufwAaicStartofFlowEvCount = _CufwAaicStartofFlowEvCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 3, 1, 8),
    _CufwAaicStartofFlowEvCount_Type()
)
cufwAaicStartofFlowEvCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAaicStartofFlowEvCount.setStatus("current")
if mibBuilder.loadTexts:
    cufwAaicStartofFlowEvCount.setUnits("Event")
_CufwAaicEndofFlowEvCount_Type = Counter64
_CufwAaicEndofFlowEvCount_Object = MibScalar
cufwAaicEndofFlowEvCount = _CufwAaicEndofFlowEvCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 3, 1, 9),
    _CufwAaicEndofFlowEvCount_Type()
)
cufwAaicEndofFlowEvCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAaicEndofFlowEvCount.setStatus("current")
if mibBuilder.loadTexts:
    cufwAaicEndofFlowEvCount.setUnits("Event")
_CufwAaicDeniedFlowEvCount_Type = Counter64
_CufwAaicDeniedFlowEvCount_Object = MibScalar
cufwAaicDeniedFlowEvCount = _CufwAaicDeniedFlowEvCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 3, 1, 10),
    _CufwAaicDeniedFlowEvCount_Type()
)
cufwAaicDeniedFlowEvCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAaicDeniedFlowEvCount.setStatus("current")
if mibBuilder.loadTexts:
    cufwAaicDeniedFlowEvCount.setUnits("Event")
_CufwAaicFwdbeforeDropCount_Type = Counter64
_CufwAaicFwdbeforeDropCount_Object = MibScalar
cufwAaicFwdbeforeDropCount = _CufwAaicFwdbeforeDropCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 3, 1, 11),
    _CufwAaicFwdbeforeDropCount_Type()
)
cufwAaicFwdbeforeDropCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAaicFwdbeforeDropCount.setStatus("current")
if mibBuilder.loadTexts:
    cufwAaicFwdbeforeDropCount.setUnits("Packet")
_CufwAaicInjDropCount_Type = Counter64
_CufwAaicInjDropCount_Object = MibScalar
cufwAaicInjDropCount = _CufwAaicInjDropCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 3, 1, 12),
    _CufwAaicInjDropCount_Type()
)
cufwAaicInjDropCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAaicInjDropCount.setStatus("current")
if mibBuilder.loadTexts:
    cufwAaicInjDropCount.setUnits("Packet")
_CufwAaicSnortEvRates_ObjectIdentity = ObjectIdentity
cufwAaicSnortEvRates = _CufwAaicSnortEvRates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 3, 2)
)
_CufwAaicIntrusionEvtRate_Type = Gauge32
_CufwAaicIntrusionEvtRate_Object = MibScalar
cufwAaicIntrusionEvtRate = _CufwAaicIntrusionEvtRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 3, 2, 1),
    _CufwAaicIntrusionEvtRate_Type()
)
cufwAaicIntrusionEvtRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAaicIntrusionEvtRate.setStatus("current")
if mibBuilder.loadTexts:
    cufwAaicIntrusionEvtRate.setUnits("Events per second")
_CufwAspFrameDropsTable_Object = MibTable
cufwAspFrameDropsTable = _CufwAspFrameDropsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 3, 3)
)
if mibBuilder.loadTexts:
    cufwAspFrameDropsTable.setStatus("current")
_CufwAspFrameDropsEntry_Object = MibTableRow
cufwAspFrameDropsEntry = _CufwAspFrameDropsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 3, 3, 1)
)
cufwAspFrameDropsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwAspFrameDropIndex"),
)
if mibBuilder.loadTexts:
    cufwAspFrameDropsEntry.setStatus("current")
_CufwAspFrameDropIndex_Type = Integer32
_CufwAspFrameDropIndex_Object = MibTableColumn
cufwAspFrameDropIndex = _CufwAspFrameDropIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 3, 3, 1, 1),
    _CufwAspFrameDropIndex_Type()
)
cufwAspFrameDropIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAspFrameDropIndex.setStatus("current")
_CufwAspFrameDropName_Type = SnmpAdminString
_CufwAspFrameDropName_Object = MibTableColumn
cufwAspFrameDropName = _CufwAspFrameDropName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 3, 3, 1, 2),
    _CufwAspFrameDropName_Type()
)
cufwAspFrameDropName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAspFrameDropName.setStatus("current")
_CufwAspFrameDropDescription_Type = SnmpAdminString
_CufwAspFrameDropDescription_Object = MibTableColumn
cufwAspFrameDropDescription = _CufwAspFrameDropDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 3, 3, 1, 3),
    _CufwAspFrameDropDescription_Type()
)
cufwAspFrameDropDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAspFrameDropDescription.setStatus("current")
_CufwAspFrameDropValue_Type = Counter32
_CufwAspFrameDropValue_Object = MibTableColumn
cufwAspFrameDropValue = _CufwAspFrameDropValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 3, 3, 1, 4),
    _CufwAspFrameDropValue_Type()
)
cufwAspFrameDropValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAspFrameDropValue.setStatus("current")
_CufwAspFlowDropsTable_Object = MibTable
cufwAspFlowDropsTable = _CufwAspFlowDropsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 3, 4)
)
if mibBuilder.loadTexts:
    cufwAspFlowDropsTable.setStatus("current")
_CufwAspFlowDropsEntry_Object = MibTableRow
cufwAspFlowDropsEntry = _CufwAspFlowDropsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 3, 4, 1)
)
cufwAspFlowDropsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwAspFlowDropIndex"),
)
if mibBuilder.loadTexts:
    cufwAspFlowDropsEntry.setStatus("current")
_CufwAspFlowDropIndex_Type = Integer32
_CufwAspFlowDropIndex_Object = MibTableColumn
cufwAspFlowDropIndex = _CufwAspFlowDropIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 3, 4, 1, 1),
    _CufwAspFlowDropIndex_Type()
)
cufwAspFlowDropIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAspFlowDropIndex.setStatus("current")
_CufwAspFlowDropName_Type = SnmpAdminString
_CufwAspFlowDropName_Object = MibTableColumn
cufwAspFlowDropName = _CufwAspFlowDropName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 3, 4, 1, 2),
    _CufwAspFlowDropName_Type()
)
cufwAspFlowDropName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAspFlowDropName.setStatus("current")
_CufwAspFlowDropDescription_Type = SnmpAdminString
_CufwAspFlowDropDescription_Object = MibTableColumn
cufwAspFlowDropDescription = _CufwAspFlowDropDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 3, 4, 1, 3),
    _CufwAspFlowDropDescription_Type()
)
cufwAspFlowDropDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAspFlowDropDescription.setStatus("current")
_CufwAspFlowDropValue_Type = Counter32
_CufwAspFlowDropValue_Object = MibTableColumn
cufwAspFlowDropValue = _CufwAspFlowDropValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 3, 4, 1, 4),
    _CufwAspFlowDropValue_Type()
)
cufwAspFlowDropValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAspFlowDropValue.setStatus("current")
_CuFwL2FwGrp_ObjectIdentity = ObjectIdentity
cuFwL2FwGrp = _CuFwL2FwGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 6)
)
_CufwL2FwGlobals_ObjectIdentity = ObjectIdentity
cufwL2FwGlobals = _CufwL2FwGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 6, 1)
)
_CufwL2GlobalEnableStealthMode_Type = TruthValue
_CufwL2GlobalEnableStealthMode_Object = MibScalar
cufwL2GlobalEnableStealthMode = _CufwL2GlobalEnableStealthMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 6, 1, 1),
    _CufwL2GlobalEnableStealthMode_Type()
)
cufwL2GlobalEnableStealthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwL2GlobalEnableStealthMode.setStatus("current")


class _CufwL2GlobalArpCacheSize_Type(Integer32):
    """Custom type cufwL2GlobalArpCacheSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CufwL2GlobalArpCacheSize_Type.__name__ = "Integer32"
_CufwL2GlobalArpCacheSize_Object = MibScalar
cufwL2GlobalArpCacheSize = _CufwL2GlobalArpCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 6, 1, 2),
    _CufwL2GlobalArpCacheSize_Type()
)
cufwL2GlobalArpCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwL2GlobalArpCacheSize.setStatus("current")
if mibBuilder.loadTexts:
    cufwL2GlobalArpCacheSize.setUnits("ARP entries")
_CufwL2GlobalEnableArpInspection_Type = TruthValue
_CufwL2GlobalEnableArpInspection_Object = MibScalar
cufwL2GlobalEnableArpInspection = _CufwL2GlobalEnableArpInspection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 6, 1, 3),
    _CufwL2GlobalEnableArpInspection_Type()
)
cufwL2GlobalEnableArpInspection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cufwL2GlobalEnableArpInspection.setStatus("current")
_CufwL2GlobalNumArpRequests_Type = Counter64
_CufwL2GlobalNumArpRequests_Object = MibScalar
cufwL2GlobalNumArpRequests = _CufwL2GlobalNumArpRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 6, 1, 5),
    _CufwL2GlobalNumArpRequests_Type()
)
cufwL2GlobalNumArpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwL2GlobalNumArpRequests.setStatus("current")
if mibBuilder.loadTexts:
    cufwL2GlobalNumArpRequests.setUnits("ARP Requests")
_CufwL2GlobalNumIcmpRequests_Type = Counter64
_CufwL2GlobalNumIcmpRequests_Object = MibScalar
cufwL2GlobalNumIcmpRequests = _CufwL2GlobalNumIcmpRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 6, 1, 6),
    _CufwL2GlobalNumIcmpRequests_Type()
)
cufwL2GlobalNumIcmpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwL2GlobalNumIcmpRequests.setStatus("current")
if mibBuilder.loadTexts:
    cufwL2GlobalNumIcmpRequests.setUnits("ICMP Traceroute Requests")
_CufwL2GlobalNumFloods_Type = Counter64
_CufwL2GlobalNumFloods_Object = MibScalar
cufwL2GlobalNumFloods = _CufwL2GlobalNumFloods_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 6, 1, 7),
    _CufwL2GlobalNumFloods_Type()
)
cufwL2GlobalNumFloods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwL2GlobalNumFloods.setStatus("current")
_CufwL2GlobalNumDrops_Type = Counter64
_CufwL2GlobalNumDrops_Object = MibScalar
cufwL2GlobalNumDrops = _CufwL2GlobalNumDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 6, 1, 8),
    _CufwL2GlobalNumDrops_Type()
)
cufwL2GlobalNumDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwL2GlobalNumDrops.setStatus("current")
_CufwL2GlobalArpOverflowRate5_Type = Gauge32
_CufwL2GlobalArpOverflowRate5_Object = MibScalar
cufwL2GlobalArpOverflowRate5 = _CufwL2GlobalArpOverflowRate5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 6, 1, 9),
    _CufwL2GlobalArpOverflowRate5_Type()
)
cufwL2GlobalArpOverflowRate5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwL2GlobalArpOverflowRate5.setStatus("current")
_CufwL2GlobalNumBadArpResponses_Type = Counter64
_CufwL2GlobalNumBadArpResponses_Object = MibScalar
cufwL2GlobalNumBadArpResponses = _CufwL2GlobalNumBadArpResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 6, 1, 10),
    _CufwL2GlobalNumBadArpResponses_Type()
)
cufwL2GlobalNumBadArpResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwL2GlobalNumBadArpResponses.setStatus("current")
if mibBuilder.loadTexts:
    cufwL2GlobalNumBadArpResponses.setUnits("ARP Responses")
_CufwL2GlobalNumSpoofedArpResps_Type = Counter64
_CufwL2GlobalNumSpoofedArpResps_Object = MibScalar
cufwL2GlobalNumSpoofedArpResps = _CufwL2GlobalNumSpoofedArpResps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 6, 1, 11),
    _CufwL2GlobalNumSpoofedArpResps_Type()
)
cufwL2GlobalNumSpoofedArpResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwL2GlobalNumSpoofedArpResps.setStatus("current")
if mibBuilder.loadTexts:
    cufwL2GlobalNumSpoofedArpResps.setUnits("ARP Responses")
_CuFwNotifCntlGrp_ObjectIdentity = ObjectIdentity
cuFwNotifCntlGrp = _CuFwNotifCntlGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 7)
)


class _CufwCntlUrlfServerStatusChange_Type(TruthValue):
    """Custom type cufwCntlUrlfServerStatusChange based on TruthValue"""
    defaultValue = 2


_CufwCntlUrlfServerStatusChange_Type.__name__ = "TruthValue"
_CufwCntlUrlfServerStatusChange_Object = MibScalar
cufwCntlUrlfServerStatusChange = _CufwCntlUrlfServerStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 7, 1),
    _CufwCntlUrlfServerStatusChange_Type()
)
cufwCntlUrlfServerStatusChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cufwCntlUrlfServerStatusChange.setStatus("current")


class _CufwCntlL2StaticMacAddressMoved_Type(TruthValue):
    """Custom type cufwCntlL2StaticMacAddressMoved based on TruthValue"""
    defaultValue = 1


_CufwCntlL2StaticMacAddressMoved_Type.__name__ = "TruthValue"
_CufwCntlL2StaticMacAddressMoved_Object = MibScalar
cufwCntlL2StaticMacAddressMoved = _CufwCntlL2StaticMacAddressMoved_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 7, 2),
    _CufwCntlL2StaticMacAddressMoved_Type()
)
cufwCntlL2StaticMacAddressMoved.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cufwCntlL2StaticMacAddressMoved.setStatus("current")


class _CufwCntlFOstateChange_Type(TruthValue):
    """Custom type cufwCntlFOstateChange based on TruthValue"""
    defaultValue = 1


_CufwCntlFOstateChange_Type.__name__ = "TruthValue"
_CufwCntlFOstateChange_Object = MibScalar
cufwCntlFOstateChange = _CufwCntlFOstateChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 7, 3),
    _CufwCntlFOstateChange_Type()
)
cufwCntlFOstateChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cufwCntlFOstateChange.setStatus("current")


class _CufwCntlCluStateChange_Type(TruthValue):
    """Custom type cufwCntlCluStateChange based on TruthValue"""
    defaultValue = 1


_CufwCntlCluStateChange_Type.__name__ = "TruthValue"
_CufwCntlCluStateChange_Object = MibScalar
cufwCntlCluStateChange = _CufwCntlCluStateChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 7, 4),
    _CufwCntlCluStateChange_Type()
)
cufwCntlCluStateChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cufwCntlCluStateChange.setStatus("current")
_CuFwClusterGrp_ObjectIdentity = ObjectIdentity
cuFwClusterGrp = _CuFwClusterGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 8)
)
_CuFwClusterGlobals_ObjectIdentity = ObjectIdentity
cuFwClusterGlobals = _CuFwClusterGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 8, 1)
)
_CufwCluEnabled_Type = TruthValue
_CufwCluEnabled_Object = MibScalar
cufwCluEnabled = _CufwCluEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 8, 1, 1),
    _CufwCluEnabled_Type()
)
cufwCluEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwCluEnabled.setStatus("current")


class _CufwCluInterfaceMode_Type(Integer32):
    """Custom type cufwCluInterfaceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_CufwCluInterfaceMode_Type.__name__ = "Integer32"
_CufwCluInterfaceMode_Object = MibScalar
cufwCluInterfaceMode = _CufwCluInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 8, 1, 2),
    _CufwCluInterfaceMode_Type()
)
cufwCluInterfaceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwCluInterfaceMode.setStatus("current")
_CufwCluUnitState_Type = CUfwCluState
_CufwCluUnitState_Object = MibScalar
cufwCluUnitState = _CufwCluUnitState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 8, 1, 3),
    _CufwCluUnitState_Type()
)
cufwCluUnitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwCluUnitState.setStatus("current")
_CufwCCLink_Type = InterfaceIndex
_CufwCCLink_Object = MibScalar
cufwCCLink = _CufwCCLink_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 8, 1, 4),
    _CufwCCLink_Type()
)
cufwCCLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwCCLink.setStatus("current")
_CufwCluGroupName_Type = SnmpAdminString
_CufwCluGroupName_Object = MibScalar
cufwCluGroupName = _CufwCluGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 8, 1, 5),
    _CufwCluGroupName_Type()
)
cufwCluGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwCluGroupName.setStatus("current")
_CufwCluUnitName_Type = SnmpAdminString
_CufwCluUnitName_Object = MibScalar
cufwCluUnitName = _CufwCluUnitName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 8, 1, 6),
    _CufwCluUnitName_Type()
)
cufwCluUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwCluUnitName.setStatus("current")
_CufwCluConsoleReplicate_Type = TruthValue
_CufwCluConsoleReplicate_Object = MibScalar
cufwCluConsoleReplicate = _CufwCluConsoleReplicate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 8, 1, 7),
    _CufwCluConsoleReplicate_Type()
)
cufwCluConsoleReplicate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwCluConsoleReplicate.setStatus("current")


class _CufwCluSiteID_Type(Integer32):
    """Custom type cufwCluSiteID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_CufwCluSiteID_Type.__name__ = "Integer32"
_CufwCluSiteID_Object = MibScalar
cufwCluSiteID = _CufwCluSiteID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 8, 1, 8),
    _CufwCluSiteID_Type()
)
cufwCluSiteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwCluSiteID.setStatus("current")


class _CufwCluPriority_Type(Integer32):
    """Custom type cufwCluPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CufwCluPriority_Type.__name__ = "Integer32"
_CufwCluPriority_Object = MibScalar
cufwCluPriority = _CufwCluPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 8, 1, 9),
    _CufwCluPriority_Type()
)
cufwCluPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwCluPriority.setStatus("current")
_CufwCluSerialNum_Type = SnmpAdminString
_CufwCluSerialNum_Object = MibScalar
cufwCluSerialNum = _CufwCluSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 8, 1, 10),
    _CufwCluSerialNum_Type()
)
cufwCluSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwCluSerialNum.setStatus("current")
_CufwCCLipAddr_Type = InetAddress
_CufwCCLipAddr_Object = MibScalar
cufwCCLipAddr = _CufwCCLipAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 8, 1, 11),
    _CufwCCLipAddr_Type()
)
cufwCCLipAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwCCLipAddr.setStatus("current")
_CufwCCLmacAddr_Type = PhysAddress
_CufwCCLmacAddr_Object = MibScalar
cufwCCLmacAddr = _CufwCCLmacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 8, 1, 12),
    _CufwCCLmacAddr_Type()
)
cufwCCLmacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwCCLmacAddr.setStatus("current")
_CufwCluSwVersion_Type = SnmpAdminString
_CufwCluSwVersion_Object = MibScalar
cufwCluSwVersion = _CufwCluSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 8, 1, 13),
    _CufwCluSwVersion_Type()
)
cufwCluSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwCluSwVersion.setStatus("current")


class _CufwCluUnitHoldtime_Type(Integer32):
    """Custom type cufwCluUnitHoldtime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(800, 45000),
    )


_CufwCluUnitHoldtime_Type.__name__ = "Integer32"
_CufwCluUnitHoldtime_Object = MibScalar
cufwCluUnitHoldtime = _CufwCluUnitHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 8, 1, 14),
    _CufwCluUnitHoldtime_Type()
)
cufwCluUnitHoldtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwCluUnitHoldtime.setStatus("current")
if mibBuilder.loadTexts:
    cufwCluUnitHoldtime.setUnits("millisec")
_CufwCluLastJoinAt_Type = DisplayString
_CufwCluLastJoinAt_Object = MibScalar
cufwCluLastJoinAt = _CufwCluLastJoinAt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 8, 1, 15),
    _CufwCluLastJoinAt_Type()
)
cufwCluLastJoinAt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwCluLastJoinAt.setStatus("current")
_CufwCluLastLeaveAt_Type = DisplayString
_CufwCluLastLeaveAt_Object = MibScalar
cufwCluLastLeaveAt = _CufwCluLastLeaveAt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 8, 1, 16),
    _CufwCluLastLeaveAt_Type()
)
cufwCluLastLeaveAt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwCluLastLeaveAt.setStatus("current")
_CuFwClusterStatus_ObjectIdentity = ObjectIdentity
cuFwClusterStatus = _CuFwClusterStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 8, 2)
)
_CuFwCluUnitHealth_Type = DisplayString
_CuFwCluUnitHealth_Object = MibScalar
cuFwCluUnitHealth = _CuFwCluUnitHealth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 8, 2, 1),
    _CuFwCluUnitHealth_Type()
)
cuFwCluUnitHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuFwCluUnitHealth.setStatus("current")
_CufwCluOverallHealth_Type = DisplayString
_CufwCluOverallHealth_Object = MibScalar
cufwCluOverallHealth = _CufwCluOverallHealth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 8, 2, 2),
    _CufwCluOverallHealth_Type()
)
cufwCluOverallHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwCluOverallHealth.setStatus("current")
_CufwCluInterfaceTable_Object = MibTable
cufwCluInterfaceTable = _CufwCluInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 8, 2, 3)
)
if mibBuilder.loadTexts:
    cufwCluInterfaceTable.setStatus("current")
_CufwCluInterfaceEntry_Object = MibTableRow
cufwCluInterfaceEntry = _CufwCluInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 8, 2, 3, 1)
)
cufwCluInterfaceEntry.setIndexNames(
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cuCluIfcIndex"),
)
if mibBuilder.loadTexts:
    cufwCluInterfaceEntry.setStatus("current")
_CuCluIfcIndex_Type = InterfaceIndex
_CuCluIfcIndex_Object = MibTableColumn
cuCluIfcIndex = _CuCluIfcIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 8, 2, 3, 1, 1),
    _CuCluIfcIndex_Type()
)
cuCluIfcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuCluIfcIndex.setStatus("current")
_CufwCluHealthStatus_Type = CUfwCluHealth
_CufwCluHealthStatus_Object = MibTableColumn
cufwCluHealthStatus = _CufwCluHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 8, 2, 3, 1, 2),
    _CufwCluHealthStatus_Type()
)
cufwCluHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwCluHealthStatus.setStatus("current")
_CufwCluHealthCheck_Type = CUfwInterfaceMonitor
_CufwCluHealthCheck_Object = MibTableColumn
cufwCluHealthCheck = _CufwCluHealthCheck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 8, 2, 3, 1, 3),
    _CufwCluHealthCheck_Type()
)
cufwCluHealthCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwCluHealthCheck.setStatus("current")
_CuFwClusterHistory_ObjectIdentity = ObjectIdentity
cuFwClusterHistory = _CuFwClusterHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 8, 3)
)
_CuFwCluMaxStateEvents_Type = Integer32
_CuFwCluMaxStateEvents_Object = MibScalar
cuFwCluMaxStateEvents = _CuFwCluMaxStateEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 8, 3, 1),
    _CuFwCluMaxStateEvents_Type()
)
cuFwCluMaxStateEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuFwCluMaxStateEvents.setStatus("current")
_CufwCluHistEvTable_Object = MibTable
cufwCluHistEvTable = _CufwCluHistEvTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 8, 3, 2)
)
if mibBuilder.loadTexts:
    cufwCluHistEvTable.setStatus("current")
_CufwCluHistEvEntry_Object = MibTableRow
cufwCluHistEvEntry = _CufwCluHistEvEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 8, 3, 2, 1)
)
cufwCluHistEvEntry.setIndexNames(
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwCluHistIndex"),
)
if mibBuilder.loadTexts:
    cufwCluHistEvEntry.setStatus("current")
_CufwCluHistIndex_Type = Integer32
_CufwCluHistIndex_Object = MibTableColumn
cufwCluHistIndex = _CufwCluHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 8, 3, 2, 1, 1),
    _CufwCluHistIndex_Type()
)
cufwCluHistIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwCluHistIndex.setStatus("current")
_CufwCluFromState_Type = CUfwCluState
_CufwCluFromState_Object = MibTableColumn
cufwCluFromState = _CufwCluFromState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 8, 3, 2, 1, 2),
    _CufwCluFromState_Type()
)
cufwCluFromState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwCluFromState.setStatus("current")
_CufwCluToState_Type = CUfwCluState
_CufwCluToState_Object = MibTableColumn
cufwCluToState = _CufwCluToState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 8, 3, 2, 1, 3),
    _CufwCluToState_Type()
)
cufwCluToState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwCluToState.setStatus("current")
_CufwCluTransitionAt_Type = DateAndTime
_CufwCluTransitionAt_Object = MibTableColumn
cufwCluTransitionAt = _CufwCluTransitionAt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 8, 3, 2, 1, 4),
    _CufwCluTransitionAt_Type()
)
cufwCluTransitionAt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwCluTransitionAt.setStatus("current")
_CufwCluTransitionReason_Type = DisplayString
_CufwCluTransitionReason_Object = MibTableColumn
cufwCluTransitionReason = _CufwCluTransitionReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 8, 3, 2, 1, 5),
    _CufwCluTransitionReason_Type()
)
cufwCluTransitionReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwCluTransitionReason.setStatus("current")
_CiscoUnifiedFirewallMIBConform_ObjectIdentity = ObjectIdentity
ciscoUnifiedFirewallMIBConform = _CiscoUnifiedFirewallMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 2)
)
_CiscoUniFirewallMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoUniFirewallMIBCompliances = _CiscoUniFirewallMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 2, 1)
)
_CiscoUniFirewallMIBGroups_ObjectIdentity = ObjectIdentity
ciscoUniFirewallMIBGroups = _CiscoUniFirewallMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 2, 2)
)

# Managed Objects groups

ciscoFwConnectionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 2, 2, 1)
)
ciscoFwConnectionGroup.setObjects(
      *(("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnGlobalNumAttempted"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnGlobalNumSetupsAborted"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnGlobalNumPolicyDeclined"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnGlobalNumResDeclined"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnGlobalNumHalfOpen"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnGlobalNumActive"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnGlobalNumAborted"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnGlobalNumExpired"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnGlobalNumEmbryonic"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnGlobalConnSetupRate1"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnGlobalConnSetupRate5"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnGlobalNumRemoteAccess"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnNumAttempted"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnNumSetupsAborted"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnNumPolicyDeclined"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnNumResDeclined"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnNumHalfOpen"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnNumActive"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnNumAborted"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnSetupRate1"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnSetupRate5"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwAppConnNumAttempted"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwAppConnNumSetupsAborted"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwAppConnNumPolicyDeclined"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwAppConnNumResDeclined"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwAppConnNumHalfOpen"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwAppConnNumActive"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwAppConnNumAborted"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwAppConnSetupRate1"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwAppConnSetupRate5"))
)
if mibBuilder.loadTexts:
    ciscoFwConnectionGroup.setStatus("current")

ciscoFwConnResourceUsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 2, 2, 2)
)
ciscoFwConnResourceUsageGroup.setObjects(
      *(("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnResMemoryUsage"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnResActiveConnMemoryUsage"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnResHOConnMemoryUsage"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnResEmbrConnMemoryUsage"))
)
if mibBuilder.loadTexts:
    ciscoFwConnResourceUsageGroup.setStatus("current")

ciscoFwPolicyConnectionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 2, 2, 3)
)
ciscoFwPolicyConnectionGroup.setObjects(
      *(("CISCO-UNIFIED-FIREWALL-MIB", "cufwPolConnNumAttempted"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwPolConnNumSetupsAborted"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwPolConnNumPolicyDeclined"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwPolConnNumResDeclined"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwPolConnNumHalfOpen"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwPolConnNumActive"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwPolConnNumAborted"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwPolAppConnNumAttempted"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwPolAppConnNumSetupsAborted"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwPolAppConnNumPolicyDeclined"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwPolAppConnNumResDeclined"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwPolAppConnNumHalfOpen"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwPolAppConnNumActive"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwPolAppConnNumAborted"))
)
if mibBuilder.loadTexts:
    ciscoFwPolicyConnectionGroup.setStatus("current")

ciscoFwApplInspectionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 2, 2, 4)
)
ciscoFwApplInspectionGroup.setObjects(
      *(("CISCO-UNIFIED-FIREWALL-MIB", "cufwAIAuditTrailEnabled"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwAIAlertEnabled"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwInspectionStatus"))
)
if mibBuilder.loadTexts:
    ciscoFwApplInspectionGroup.setStatus("current")

ciscoFwUrlFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 2, 2, 5)
)
ciscoFwUrlFilterGroup.setObjects(
      *(("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfFunctionEnabled"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfRequestsNumProcessed"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfRequestsProcRate1"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfRequestsProcRate5"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfRequestsNumAllowed"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfRequestsNumDenied"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfRequestsDeniedRate1"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfRequestsDeniedRate5"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfRequestsNumCacheAllowed"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfRequestsNumCacheDenied"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfAllowModeReqNumAllowed"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfAllowModeReqNumDenied"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfRequestsNumResDropped"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfRequestsResDropRate1"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfRequestsResDropRate5"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfNumServerTimeouts"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfNumServerRetries"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfResponsesNumLate"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfUrlAccRespsNumResDropped"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfServerVendor"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfServerStatus"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfServerReqsNumProcessed"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfServerReqsNumAllowed"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfServerReqsNumDenied"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfServerNumTimeouts"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfServerNumRetries"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfServerRespsNumReceived"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfServerRespsNumLate"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfServerAvgRespTime1"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfServerAvgRespTime5"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwCntlUrlfServerStatusChange"))
)
if mibBuilder.loadTexts:
    ciscoFwUrlFilterGroup.setStatus("current")

ciscoFwUrlFilterResourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 2, 2, 6)
)
ciscoFwUrlFilterResourceGroup.setObjects(
      *(("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfResTotalRequestCacheSize"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfResTotalRespCacheSize"))
)
if mibBuilder.loadTexts:
    ciscoFwUrlFilterResourceGroup.setStatus("current")

ciscoFwTransparentFwGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 2, 2, 7)
)
ciscoFwTransparentFwGroup.setObjects(
      *(("CISCO-UNIFIED-FIREWALL-MIB", "cufwL2GlobalEnableStealthMode"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwL2GlobalArpCacheSize"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwL2GlobalEnableArpInspection"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwL2GlobalNumArpRequests"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwL2GlobalNumIcmpRequests"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwL2GlobalNumFloods"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwL2GlobalNumDrops"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwL2GlobalArpOverflowRate5"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwL2GlobalNumBadArpResponses"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwL2GlobalNumSpoofedArpResps"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwCntlL2StaticMacAddressMoved"))
)
if mibBuilder.loadTexts:
    ciscoFwTransparentFwGroup.setStatus("current")

ciscoFwBasicAaicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 2, 2, 10)
)
ciscoFwBasicAaicGroup.setObjects(
      *(("CISCO-UNIFIED-FIREWALL-MIB", "cufwAaicGlobalNumBadProtocolOps"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwAaicGlobalNumBadPDUSize"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwAaicGlobalNumBadPortRange"))
)
if mibBuilder.loadTexts:
    ciscoFwBasicAaicGroup.setStatus("current")

ciscoFwAaicHttpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 2, 2, 11)
)
ciscoFwAaicHttpGroup.setObjects(
      *(("CISCO-UNIFIED-FIREWALL-MIB", "cufwAaicHttpNumBadProtocolOps"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwAaicHttpNumBadPDUSize"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwAaicHttpNumTunneledConns"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwAaicHttpNumLargeURIs"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwAaicHttpNumBadContent"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwAaicHttpNumMismatchContent"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwAaicHttpNumDoubleEncodedPkts"))
)
if mibBuilder.loadTexts:
    ciscoFwAaicHttpGroup.setStatus("current")

ciscoFwMibReportingControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 2, 2, 12)
)
ciscoFwMibReportingControlGroup.setObjects(
      *(("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnReptAppStats"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnReptAppStatsLastChanged"))
)
if mibBuilder.loadTexts:
    ciscoFwMibReportingControlGroup.setStatus("current")

ciscoFwFailoverGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 2, 2, 13)
)
ciscoFwFailoverGroup.setObjects(
      *(("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOEnabled"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOUnitDesignation"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOLink"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOStateLink"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOStdbyConfigLocked"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOEncryption"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOSerialNumOurs"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOSerialNumMate"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOSwVersionOurs"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOSwVersionMate"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOUnitPolltime"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOUnitHoldtime"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOUnitBfdEnabled"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOLinkStatePolltime"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOInterfacePolicy"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOMonitoredInterfaces"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOInterfacePolltime"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOInterfaceHoldtime"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOReplicationHttp"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOReplicationRate"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOGroupIdx"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOCLientId"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOCLientName"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOLUTransmitCount"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOLUTransmitErrors"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOLUReceiveCount"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOLUReceiveErrors"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOStatefulUpdateEnabled"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOGroupIndex"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwContextId"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwContextifIndex"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOInterfaceMonitoring"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOInterfaceStatus"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOGroupIndex"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOGrpLastFailoverAt"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOGrpHAstate"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOGrpUpTime"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOGrpContextCount"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOGrpIndex"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOHistoryIndex"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOGrpHAFromState"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOGrpHAToState"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOGrpTransitionAt"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOGrpTransitionReason"))
)
if mibBuilder.loadTexts:
    ciscoFwFailoverGroup.setStatus("current")


# Notification objects

ciscoUFwUrlfServerStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 0, 1)
)
ciscoUFwUrlfServerStateChange.setObjects(
    ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfServerStatus")
)
if mibBuilder.loadTexts:
    ciscoUFwUrlfServerStateChange.setStatus(
        "current"
    )

ciscoUFwL2StaticMacAddressMoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 0, 2)
)
ciscoUFwL2StaticMacAddressMoved.setObjects(
      *(("BRIDGE-MIB", "dot1dTpFdbPort"),
        ("BRIDGE-MIB", "dot1dTpFdbStatus"))
)
if mibBuilder.loadTexts:
    ciscoUFwL2StaticMacAddressMoved.setStatus(
        "current"
    )

cufwFailoverStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 0, 3)
)
cufwFailoverStateChanged.setObjects(
      *(("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOGroupIndex"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwFOGrpHAstate"))
)
if mibBuilder.loadTexts:
    cufwFailoverStateChanged.setStatus(
        "current"
    )

cufwClusterStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 0, 4)
)
cufwClusterStateChanged.setObjects(
    ("CISCO-UNIFIED-FIREWALL-MIB", "cufwCluUnitState")
)
if mibBuilder.loadTexts:
    cufwClusterStateChanged.setStatus(
        "current"
    )


# Notifications groups

ciscoFwNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 2, 2, 8)
)
ciscoFwNotificationsGroup.setObjects(
    ("CISCO-UNIFIED-FIREWALL-MIB", "ciscoUFwUrlfServerStateChange")
)
if mibBuilder.loadTexts:
    ciscoFwNotificationsGroup.setStatus(
        "current"
    )

ciscoFwTransparentNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 2, 2, 9)
)
ciscoFwTransparentNotifGroup.setObjects(
    ("CISCO-UNIFIED-FIREWALL-MIB", "ciscoUFwL2StaticMacAddressMoved")
)
if mibBuilder.loadTexts:
    ciscoFwTransparentNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoUniFirewallMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 2, 1, 1)
)
ciscoUniFirewallMIBCompliance.setObjects(
      *(("CISCO-UNIFIED-FIREWALL-MIB", "ciscoFwConnectionGroup"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "ciscoFwMibReportingControlGroup"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "ciscoFwApplInspectionGroup"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "ciscoFwConnResourceUsageGroup"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "ciscoFwFailoverGroup"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "ciscoFwPolicyConnectionGroup"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "ciscoFwUrlFilterGroup"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "ciscoFwUrlFilterResourceGroup"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "ciscoFwTransparentFwGroup"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "ciscoFwTransparentNotifGroup"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "ciscoFwBasicAaicGroup"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "ciscoFwAaicHttpGroup"))
)
if mibBuilder.loadTexts:
    ciscoUniFirewallMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-FIREWALL-MIB",
    **{"CUfwFOState": CUfwFOState,
       "CUfwInterfaceMonitor": CUfwInterfaceMonitor,
       "CUfwInterfaceHealth": CUfwInterfaceHealth,
       "CUfwFOGroupId": CUfwFOGroupId,
       "CUfwCluState": CUfwCluState,
       "CUfwCluHealth": CUfwCluHealth,
       "ciscoUnifiedFirewallMIB": ciscoUnifiedFirewallMIB,
       "ciscoUnifiedFirewallMIBNotifs": ciscoUnifiedFirewallMIBNotifs,
       "ciscoUFwUrlfServerStateChange": ciscoUFwUrlfServerStateChange,
       "ciscoUFwL2StaticMacAddressMoved": ciscoUFwL2StaticMacAddressMoved,
       "cufwFailoverStateChanged": cufwFailoverStateChanged,
       "cufwClusterStateChanged": cufwClusterStateChanged,
       "ciscoUnifiedFirewallMIBObjects": ciscoUnifiedFirewallMIBObjects,
       "cuFwConnectionGrp": cuFwConnectionGrp,
       "cuFwConnectionGlobals": cuFwConnectionGlobals,
       "cufwConnGlobalNumAttempted": cufwConnGlobalNumAttempted,
       "cufwConnGlobalNumSetupsAborted": cufwConnGlobalNumSetupsAborted,
       "cufwConnGlobalNumPolicyDeclined": cufwConnGlobalNumPolicyDeclined,
       "cufwConnGlobalNumResDeclined": cufwConnGlobalNumResDeclined,
       "cufwConnGlobalNumHalfOpen": cufwConnGlobalNumHalfOpen,
       "cufwConnGlobalNumActive": cufwConnGlobalNumActive,
       "cufwConnGlobalNumExpired": cufwConnGlobalNumExpired,
       "cufwConnGlobalNumAborted": cufwConnGlobalNumAborted,
       "cufwConnGlobalNumEmbryonic": cufwConnGlobalNumEmbryonic,
       "cufwConnGlobalConnSetupRate1": cufwConnGlobalConnSetupRate1,
       "cufwConnGlobalConnSetupRate5": cufwConnGlobalConnSetupRate5,
       "cufwConnGlobalNumRemoteAccess": cufwConnGlobalNumRemoteAccess,
       "cuFwConnectionResources": cuFwConnectionResources,
       "cufwConnResMemoryUsage": cufwConnResMemoryUsage,
       "cufwConnResActiveConnMemoryUsage": cufwConnResActiveConnMemoryUsage,
       "cufwConnResHOConnMemoryUsage": cufwConnResHOConnMemoryUsage,
       "cufwConnResEmbrConnMemoryUsage": cufwConnResEmbrConnMemoryUsage,
       "cuFwConnectionReportSettings": cuFwConnectionReportSettings,
       "cufwConnReptAppStats": cufwConnReptAppStats,
       "cufwConnReptAppStatsLastChanged": cufwConnReptAppStatsLastChanged,
       "cuFwConnectionSummaryTables": cuFwConnectionSummaryTables,
       "cufwConnSummaryTable": cufwConnSummaryTable,
       "cufwConnSummaryEntry": cufwConnSummaryEntry,
       "cufwConnProtocol": cufwConnProtocol,
       "cufwConnNumAttempted": cufwConnNumAttempted,
       "cufwConnNumSetupsAborted": cufwConnNumSetupsAborted,
       "cufwConnNumPolicyDeclined": cufwConnNumPolicyDeclined,
       "cufwConnNumResDeclined": cufwConnNumResDeclined,
       "cufwConnNumHalfOpen": cufwConnNumHalfOpen,
       "cufwConnNumActive": cufwConnNumActive,
       "cufwConnNumAborted": cufwConnNumAborted,
       "cufwConnSetupRate1": cufwConnSetupRate1,
       "cufwConnSetupRate5": cufwConnSetupRate5,
       "cufwAppConnSummaryTable": cufwAppConnSummaryTable,
       "cufwAppConnSummaryEntry": cufwAppConnSummaryEntry,
       "cufwAppConnProtocol": cufwAppConnProtocol,
       "cufwAppConnNumAttempted": cufwAppConnNumAttempted,
       "cufwAppConnNumSetupsAborted": cufwAppConnNumSetupsAborted,
       "cufwAppConnNumPolicyDeclined": cufwAppConnNumPolicyDeclined,
       "cufwAppConnNumResDeclined": cufwAppConnNumResDeclined,
       "cufwAppConnNumHalfOpen": cufwAppConnNumHalfOpen,
       "cufwAppConnNumActive": cufwAppConnNumActive,
       "cufwAppConnNumAborted": cufwAppConnNumAborted,
       "cufwAppConnSetupRate1": cufwAppConnSetupRate1,
       "cufwAppConnSetupRate5": cufwAppConnSetupRate5,
       "cufwPolicyConnSummaryTable": cufwPolicyConnSummaryTable,
       "cufwPolicyConnSummaryEntry": cufwPolicyConnSummaryEntry,
       "cufwPolConnPolicy": cufwPolConnPolicy,
       "cufwPolConnPolicyTargetType": cufwPolConnPolicyTargetType,
       "cufwPolConnPolicyTarget": cufwPolConnPolicyTarget,
       "cufwPolConnProtocol": cufwPolConnProtocol,
       "cufwPolConnNumAttempted": cufwPolConnNumAttempted,
       "cufwPolConnNumSetupsAborted": cufwPolConnNumSetupsAborted,
       "cufwPolConnNumPolicyDeclined": cufwPolConnNumPolicyDeclined,
       "cufwPolConnNumResDeclined": cufwPolConnNumResDeclined,
       "cufwPolConnNumHalfOpen": cufwPolConnNumHalfOpen,
       "cufwPolConnNumActive": cufwPolConnNumActive,
       "cufwPolConnNumAborted": cufwPolConnNumAborted,
       "cufwPolicyAppConnSummaryTable": cufwPolicyAppConnSummaryTable,
       "cufwPolicyAppConnSummaryEntry": cufwPolicyAppConnSummaryEntry,
       "cufwPolAppConnPolicy": cufwPolAppConnPolicy,
       "cufwPolAppConnPolicyTargetType": cufwPolAppConnPolicyTargetType,
       "cufwPolAppConnPolicyTarget": cufwPolAppConnPolicyTarget,
       "cufwPolAppConnProtocol": cufwPolAppConnProtocol,
       "cufwPolAppConnNumAttempted": cufwPolAppConnNumAttempted,
       "cufwPolAppConnNumSetupsAborted": cufwPolAppConnNumSetupsAborted,
       "cufwPolAppConnNumPolicyDeclined": cufwPolAppConnNumPolicyDeclined,
       "cufwPolAppConnNumResDeclined": cufwPolAppConnNumResDeclined,
       "cufwPolAppConnNumHalfOpen": cufwPolAppConnNumHalfOpen,
       "cufwPolAppConnNumActive": cufwPolAppConnNumActive,
       "cufwPolAppConnNumAborted": cufwPolAppConnNumAborted,
       "cuFwApplInspectionGrp": cuFwApplInspectionGrp,
       "cufwAIAuditTrailEnabled": cufwAIAuditTrailEnabled,
       "cufwAIAlertEnabled": cufwAIAlertEnabled,
       "cufwInspectionTable": cufwInspectionTable,
       "cufwInspectionEntry": cufwInspectionEntry,
       "cufwInspectionPolicyName": cufwInspectionPolicyName,
       "cufwInspectionProtocol": cufwInspectionProtocol,
       "cufwInspectionStatus": cufwInspectionStatus,
       "cuFwUrlFilterGrp": cuFwUrlFilterGrp,
       "cufwUrlFilterGlobals": cufwUrlFilterGlobals,
       "cufwUrlfFunctionEnabled": cufwUrlfFunctionEnabled,
       "cufwUrlfRequestsNumProcessed": cufwUrlfRequestsNumProcessed,
       "cufwUrlfRequestsProcRate1": cufwUrlfRequestsProcRate1,
       "cufwUrlfRequestsProcRate5": cufwUrlfRequestsProcRate5,
       "cufwUrlfRequestsNumAllowed": cufwUrlfRequestsNumAllowed,
       "cufwUrlfRequestsNumDenied": cufwUrlfRequestsNumDenied,
       "cufwUrlfRequestsDeniedRate1": cufwUrlfRequestsDeniedRate1,
       "cufwUrlfRequestsDeniedRate5": cufwUrlfRequestsDeniedRate5,
       "cufwUrlfRequestsNumCacheAllowed": cufwUrlfRequestsNumCacheAllowed,
       "cufwUrlfRequestsNumCacheDenied": cufwUrlfRequestsNumCacheDenied,
       "cufwUrlfAllowModeReqNumAllowed": cufwUrlfAllowModeReqNumAllowed,
       "cufwUrlfAllowModeReqNumDenied": cufwUrlfAllowModeReqNumDenied,
       "cufwUrlfRequestsNumResDropped": cufwUrlfRequestsNumResDropped,
       "cufwUrlfRequestsResDropRate1": cufwUrlfRequestsResDropRate1,
       "cufwUrlfRequestsResDropRate5": cufwUrlfRequestsResDropRate5,
       "cufwUrlfNumServerTimeouts": cufwUrlfNumServerTimeouts,
       "cufwUrlfNumServerRetries": cufwUrlfNumServerRetries,
       "cufwUrlfResponsesNumLate": cufwUrlfResponsesNumLate,
       "cufwUrlfUrlAccRespsNumResDropped": cufwUrlfUrlAccRespsNumResDropped,
       "cufwUrlFilterResourceUsage": cufwUrlFilterResourceUsage,
       "cufwUrlfResTotalRequestCacheSize": cufwUrlfResTotalRequestCacheSize,
       "cufwUrlfResTotalRespCacheSize": cufwUrlfResTotalRespCacheSize,
       "cufwUrlFilterServers": cufwUrlFilterServers,
       "cufwUrlfServerTable": cufwUrlfServerTable,
       "cufwUrlfServerEntry": cufwUrlfServerEntry,
       "cufwUrlfServerAddrType": cufwUrlfServerAddrType,
       "cufwUrlfServerAddress": cufwUrlfServerAddress,
       "cufwUrlfServerPort": cufwUrlfServerPort,
       "cufwUrlfServerVendor": cufwUrlfServerVendor,
       "cufwUrlfServerStatus": cufwUrlfServerStatus,
       "cufwUrlfServerReqsNumProcessed": cufwUrlfServerReqsNumProcessed,
       "cufwUrlfServerReqsNumAllowed": cufwUrlfServerReqsNumAllowed,
       "cufwUrlfServerReqsNumDenied": cufwUrlfServerReqsNumDenied,
       "cufwUrlfServerNumTimeouts": cufwUrlfServerNumTimeouts,
       "cufwUrlfServerNumRetries": cufwUrlfServerNumRetries,
       "cufwUrlfServerRespsNumReceived": cufwUrlfServerRespsNumReceived,
       "cufwUrlfServerRespsNumLate": cufwUrlfServerRespsNumLate,
       "cufwUrlfServerAvgRespTime1": cufwUrlfServerAvgRespTime1,
       "cufwUrlfServerAvgRespTime5": cufwUrlfServerAvgRespTime5,
       "cuFwFailoverGrp": cuFwFailoverGrp,
       "cuFwFailoverGlobals": cuFwFailoverGlobals,
       "cufwFOEnabled": cufwFOEnabled,
       "cufwFOUnitDesignation": cufwFOUnitDesignation,
       "cufwFOLink": cufwFOLink,
       "cufwFOStateLink": cufwFOStateLink,
       "cufwFOStdbyConfigLocked": cufwFOStdbyConfigLocked,
       "cufwFOEncryption": cufwFOEncryption,
       "cufwFOSerialNumOurs": cufwFOSerialNumOurs,
       "cufwFOSerialNumMate": cufwFOSerialNumMate,
       "cufwFOSwVersionOurs": cufwFOSwVersionOurs,
       "cufwFOSwVersionMate": cufwFOSwVersionMate,
       "cufwFOUnitPolltime": cufwFOUnitPolltime,
       "cufwFOUnitHoldtime": cufwFOUnitHoldtime,
       "cufwFOUnitBfdEnabled": cufwFOUnitBfdEnabled,
       "cufwFOLinkStatePolltime": cufwFOLinkStatePolltime,
       "cufwFOInterfacePolicy": cufwFOInterfacePolicy,
       "cufwFOMonitoredInterfaces": cufwFOMonitoredInterfaces,
       "cufwFOInterfacePolltime": cufwFOInterfacePolltime,
       "cufwFOInterfaceHoldtime": cufwFOInterfaceHoldtime,
       "cufwFOReplicationHttp": cufwFOReplicationHttp,
       "cufwFOReplicationRate": cufwFOReplicationRate,
       "cuFwFailoverStatus": cuFwFailoverStatus,
       "cufwFOGrpStatusTable": cufwFOGrpStatusTable,
       "cufwFOGrpStatusEntry": cufwFOGrpStatusEntry,
       "cufwFOGroupIndex": cufwFOGroupIndex,
       "cufwFOGrpLastFailoverAt": cufwFOGrpLastFailoverAt,
       "cufwFOGrpHAstate": cufwFOGrpHAstate,
       "cufwFOGrpUpTime": cufwFOGrpUpTime,
       "cufwFOGrpContextCount": cufwFOGrpContextCount,
       "cufwFOInterfaceTable": cufwFOInterfaceTable,
       "cufwFOInterfaceEntry": cufwFOInterfaceEntry,
       "cufwFOGrpId": cufwFOGrpId,
       "cufwContextId": cufwContextId,
       "cufwContextifIndex": cufwContextifIndex,
       "cufwFOInterfaceMonitoring": cufwFOInterfaceMonitoring,
       "cufwFOInterfaceStatus": cufwFOInterfaceStatus,
       "cuFwFailoverStatistics": cuFwFailoverStatistics,
       "cufwFOStatefulUpdateEnabled": cufwFOStatefulUpdateEnabled,
       "cufwFOLogicalUpdatesTable": cufwFOLogicalUpdatesTable,
       "cufwFOLogicalUpdateEntry": cufwFOLogicalUpdateEntry,
       "cufwFOGroupIdx": cufwFOGroupIdx,
       "cufwFOCLientId": cufwFOCLientId,
       "cufwFOCLientName": cufwFOCLientName,
       "cufwFOLUTransmitCount": cufwFOLUTransmitCount,
       "cufwFOLUTransmitErrors": cufwFOLUTransmitErrors,
       "cufwFOLUReceiveCount": cufwFOLUReceiveCount,
       "cufwFOLUReceiveErrors": cufwFOLUReceiveErrors,
       "cuFwFailoverHistory": cuFwFailoverHistory,
       "cuFwFOMaxStateEvents": cuFwFOMaxStateEvents,
       "cufwFOHistoryEvTable": cufwFOHistoryEvTable,
       "cufwFOHistoryEvEntry": cufwFOHistoryEvEntry,
       "cufwFOGrpIndex": cufwFOGrpIndex,
       "cufwFOHistoryIndex": cufwFOHistoryIndex,
       "cufwFOGrpHAFromState": cufwFOGrpHAFromState,
       "cufwFOGrpHAToState": cufwFOGrpHAToState,
       "cufwFOGrpTransitionAt": cufwFOGrpTransitionAt,
       "cufwFOGrpTransitionReason": cufwFOGrpTransitionReason,
       "cuFwAaicGrp": cuFwAaicGrp,
       "cufwAaicGlobals": cufwAaicGlobals,
       "cufwAaicGlobalNumBadProtocolOps": cufwAaicGlobalNumBadProtocolOps,
       "cufwAaicGlobalNumBadPDUSize": cufwAaicGlobalNumBadPDUSize,
       "cufwAaicGlobalNumBadPortRange": cufwAaicGlobalNumBadPortRange,
       "cufwAaicProtocolStats": cufwAaicProtocolStats,
       "cufwAaicHttpProtocolStats": cufwAaicHttpProtocolStats,
       "cufwAaicHttpNumBadProtocolOps": cufwAaicHttpNumBadProtocolOps,
       "cufwAaicHttpNumBadPDUSize": cufwAaicHttpNumBadPDUSize,
       "cufwAaicHttpNumTunneledConns": cufwAaicHttpNumTunneledConns,
       "cufwAaicHttpNumLargeURIs": cufwAaicHttpNumLargeURIs,
       "cufwAaicHttpNumBadContent": cufwAaicHttpNumBadContent,
       "cufwAaicHttpNumMismatchContent": cufwAaicHttpNumMismatchContent,
       "cufwAaicHttpNumDoubleEncodedPkts": cufwAaicHttpNumDoubleEncodedPkts,
       "cufwAaicEngineStats": cufwAaicEngineStats,
       "cufwAaicLinaSnortStats": cufwAaicLinaSnortStats,
       "cufwAaicPassedSnortCount": cufwAaicPassedSnortCount,
       "cufwAaicBlockedSnortCount": cufwAaicBlockedSnortCount,
       "cufwAaicInjbySnortCount": cufwAaicInjbySnortCount,
       "cufwAaicBypassSnortDownCount": cufwAaicBypassSnortDownCount,
       "cufwAaicBypassSnortBusyCount": cufwAaicBypassSnortBusyCount,
       "cufwAaicFastfwdFlowsCount": cufwAaicFastfwdFlowsCount,
       "cufwAaicBlacklistedFlowsCount": cufwAaicBlacklistedFlowsCount,
       "cufwAaicStartofFlowEvCount": cufwAaicStartofFlowEvCount,
       "cufwAaicEndofFlowEvCount": cufwAaicEndofFlowEvCount,
       "cufwAaicDeniedFlowEvCount": cufwAaicDeniedFlowEvCount,
       "cufwAaicFwdbeforeDropCount": cufwAaicFwdbeforeDropCount,
       "cufwAaicInjDropCount": cufwAaicInjDropCount,
       "cufwAaicSnortEvRates": cufwAaicSnortEvRates,
       "cufwAaicIntrusionEvtRate": cufwAaicIntrusionEvtRate,
       "cufwAspFrameDropsTable": cufwAspFrameDropsTable,
       "cufwAspFrameDropsEntry": cufwAspFrameDropsEntry,
       "cufwAspFrameDropIndex": cufwAspFrameDropIndex,
       "cufwAspFrameDropName": cufwAspFrameDropName,
       "cufwAspFrameDropDescription": cufwAspFrameDropDescription,
       "cufwAspFrameDropValue": cufwAspFrameDropValue,
       "cufwAspFlowDropsTable": cufwAspFlowDropsTable,
       "cufwAspFlowDropsEntry": cufwAspFlowDropsEntry,
       "cufwAspFlowDropIndex": cufwAspFlowDropIndex,
       "cufwAspFlowDropName": cufwAspFlowDropName,
       "cufwAspFlowDropDescription": cufwAspFlowDropDescription,
       "cufwAspFlowDropValue": cufwAspFlowDropValue,
       "cuFwL2FwGrp": cuFwL2FwGrp,
       "cufwL2FwGlobals": cufwL2FwGlobals,
       "cufwL2GlobalEnableStealthMode": cufwL2GlobalEnableStealthMode,
       "cufwL2GlobalArpCacheSize": cufwL2GlobalArpCacheSize,
       "cufwL2GlobalEnableArpInspection": cufwL2GlobalEnableArpInspection,
       "cufwL2GlobalNumArpRequests": cufwL2GlobalNumArpRequests,
       "cufwL2GlobalNumIcmpRequests": cufwL2GlobalNumIcmpRequests,
       "cufwL2GlobalNumFloods": cufwL2GlobalNumFloods,
       "cufwL2GlobalNumDrops": cufwL2GlobalNumDrops,
       "cufwL2GlobalArpOverflowRate5": cufwL2GlobalArpOverflowRate5,
       "cufwL2GlobalNumBadArpResponses": cufwL2GlobalNumBadArpResponses,
       "cufwL2GlobalNumSpoofedArpResps": cufwL2GlobalNumSpoofedArpResps,
       "cuFwNotifCntlGrp": cuFwNotifCntlGrp,
       "cufwCntlUrlfServerStatusChange": cufwCntlUrlfServerStatusChange,
       "cufwCntlL2StaticMacAddressMoved": cufwCntlL2StaticMacAddressMoved,
       "cufwCntlFOstateChange": cufwCntlFOstateChange,
       "cufwCntlCluStateChange": cufwCntlCluStateChange,
       "cuFwClusterGrp": cuFwClusterGrp,
       "cuFwClusterGlobals": cuFwClusterGlobals,
       "cufwCluEnabled": cufwCluEnabled,
       "cufwCluInterfaceMode": cufwCluInterfaceMode,
       "cufwCluUnitState": cufwCluUnitState,
       "cufwCCLink": cufwCCLink,
       "cufwCluGroupName": cufwCluGroupName,
       "cufwCluUnitName": cufwCluUnitName,
       "cufwCluConsoleReplicate": cufwCluConsoleReplicate,
       "cufwCluSiteID": cufwCluSiteID,
       "cufwCluPriority": cufwCluPriority,
       "cufwCluSerialNum": cufwCluSerialNum,
       "cufwCCLipAddr": cufwCCLipAddr,
       "cufwCCLmacAddr": cufwCCLmacAddr,
       "cufwCluSwVersion": cufwCluSwVersion,
       "cufwCluUnitHoldtime": cufwCluUnitHoldtime,
       "cufwCluLastJoinAt": cufwCluLastJoinAt,
       "cufwCluLastLeaveAt": cufwCluLastLeaveAt,
       "cuFwClusterStatus": cuFwClusterStatus,
       "cuFwCluUnitHealth": cuFwCluUnitHealth,
       "cufwCluOverallHealth": cufwCluOverallHealth,
       "cufwCluInterfaceTable": cufwCluInterfaceTable,
       "cufwCluInterfaceEntry": cufwCluInterfaceEntry,
       "cuCluIfcIndex": cuCluIfcIndex,
       "cufwCluHealthStatus": cufwCluHealthStatus,
       "cufwCluHealthCheck": cufwCluHealthCheck,
       "cuFwClusterHistory": cuFwClusterHistory,
       "cuFwCluMaxStateEvents": cuFwCluMaxStateEvents,
       "cufwCluHistEvTable": cufwCluHistEvTable,
       "cufwCluHistEvEntry": cufwCluHistEvEntry,
       "cufwCluHistIndex": cufwCluHistIndex,
       "cufwCluFromState": cufwCluFromState,
       "cufwCluToState": cufwCluToState,
       "cufwCluTransitionAt": cufwCluTransitionAt,
       "cufwCluTransitionReason": cufwCluTransitionReason,
       "ciscoUnifiedFirewallMIBConform": ciscoUnifiedFirewallMIBConform,
       "ciscoUniFirewallMIBCompliances": ciscoUniFirewallMIBCompliances,
       "ciscoUniFirewallMIBCompliance": ciscoUniFirewallMIBCompliance,
       "ciscoUniFirewallMIBGroups": ciscoUniFirewallMIBGroups,
       "ciscoFwConnectionGroup": ciscoFwConnectionGroup,
       "ciscoFwConnResourceUsageGroup": ciscoFwConnResourceUsageGroup,
       "ciscoFwPolicyConnectionGroup": ciscoFwPolicyConnectionGroup,
       "ciscoFwApplInspectionGroup": ciscoFwApplInspectionGroup,
       "ciscoFwUrlFilterGroup": ciscoFwUrlFilterGroup,
       "ciscoFwUrlFilterResourceGroup": ciscoFwUrlFilterResourceGroup,
       "ciscoFwTransparentFwGroup": ciscoFwTransparentFwGroup,
       "ciscoFwNotificationsGroup": ciscoFwNotificationsGroup,
       "ciscoFwTransparentNotifGroup": ciscoFwTransparentNotifGroup,
       "ciscoFwBasicAaicGroup": ciscoFwBasicAaicGroup,
       "ciscoFwAaicHttpGroup": ciscoFwAaicHttpGroup,
       "ciscoFwMibReportingControlGroup": ciscoFwMibReportingControlGroup,
       "ciscoFwFailoverGroup": ciscoFwFailoverGroup}
)
