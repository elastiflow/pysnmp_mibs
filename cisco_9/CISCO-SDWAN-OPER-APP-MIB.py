# SNMP MIB module (CISCO-SDWAN-OPER-APP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-SDWAN-OPER-APP-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:52:58 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoSdwanOperAppMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1007)
)
if mibBuilder.loadTexts:
    ciscoSdwanOperAppMIB.setRevisions(
        ("2021-05-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoSdwanOperAppMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoSdwanOperAppMIBNotifs = _CiscoSdwanOperAppMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1007, 0)
)
_CiscoSdwanOperAppMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSdwanOperAppMIBObjects = _CiscoSdwanOperAppMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1007, 1)
)
_App_ObjectIdentity = ObjectIdentity
app = _App_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1007, 1, 6)
)
_AppCflowd_ObjectIdentity = ObjectIdentity
appCflowd = _AppCflowd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1007, 1, 6, 1)
)
_AppCflowdStatistics_ObjectIdentity = ObjectIdentity
appCflowdStatistics = _AppCflowdStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1007, 1, 6, 1, 3)
)
_AppCflowdStatisticsDataPackets_Type = Counter64
_AppCflowdStatisticsDataPackets_Object = MibScalar
appCflowdStatisticsDataPackets = _AppCflowdStatisticsDataPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1007, 1, 6, 1, 3, 1),
    _AppCflowdStatisticsDataPackets_Type()
)
appCflowdStatisticsDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdStatisticsDataPackets.setStatus("current")
_AppCflowdStatisticsTemplatePackets_Type = Counter64
_AppCflowdStatisticsTemplatePackets_Object = MibScalar
appCflowdStatisticsTemplatePackets = _AppCflowdStatisticsTemplatePackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1007, 1, 6, 1, 3, 2),
    _AppCflowdStatisticsTemplatePackets_Type()
)
appCflowdStatisticsTemplatePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdStatisticsTemplatePackets.setStatus("current")
_AppCflowdStatisticsTotalPackets_Type = Counter64
_AppCflowdStatisticsTotalPackets_Object = MibScalar
appCflowdStatisticsTotalPackets = _AppCflowdStatisticsTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1007, 1, 6, 1, 3, 3),
    _AppCflowdStatisticsTotalPackets_Type()
)
appCflowdStatisticsTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdStatisticsTotalPackets.setStatus("current")
_AppCflowdStatisticsFlowRefresh_Type = Counter64
_AppCflowdStatisticsFlowRefresh_Object = MibScalar
appCflowdStatisticsFlowRefresh = _AppCflowdStatisticsFlowRefresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1007, 1, 6, 1, 3, 4),
    _AppCflowdStatisticsFlowRefresh_Type()
)
appCflowdStatisticsFlowRefresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdStatisticsFlowRefresh.setStatus("current")
_AppCflowdStatisticsFlowAgeout_Type = Counter64
_AppCflowdStatisticsFlowAgeout_Object = MibScalar
appCflowdStatisticsFlowAgeout = _AppCflowdStatisticsFlowAgeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1007, 1, 6, 1, 3, 5),
    _AppCflowdStatisticsFlowAgeout_Type()
)
appCflowdStatisticsFlowAgeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdStatisticsFlowAgeout.setStatus("current")
_AppCflowdStatisticsFlowEndDetected_Type = Counter64
_AppCflowdStatisticsFlowEndDetected_Object = MibScalar
appCflowdStatisticsFlowEndDetected = _AppCflowdStatisticsFlowEndDetected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1007, 1, 6, 1, 3, 6),
    _AppCflowdStatisticsFlowEndDetected_Type()
)
appCflowdStatisticsFlowEndDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdStatisticsFlowEndDetected.setStatus("current")
_AppCflowdStatisticsFlowEndForced_Type = Counter64
_AppCflowdStatisticsFlowEndForced_Object = MibScalar
appCflowdStatisticsFlowEndForced = _AppCflowdStatisticsFlowEndForced_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1007, 1, 6, 1, 3, 7),
    _AppCflowdStatisticsFlowEndForced_Type()
)
appCflowdStatisticsFlowEndForced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdStatisticsFlowEndForced.setStatus("current")
_AppCflowdStatisticsFlowRateLimitDrop_Type = Counter64
_AppCflowdStatisticsFlowRateLimitDrop_Object = MibScalar
appCflowdStatisticsFlowRateLimitDrop = _AppCflowdStatisticsFlowRateLimitDrop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1007, 1, 6, 1, 3, 8),
    _AppCflowdStatisticsFlowRateLimitDrop_Type()
)
appCflowdStatisticsFlowRateLimitDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdStatisticsFlowRateLimitDrop.setStatus("current")
_AppCflowdTemplate_ObjectIdentity = ObjectIdentity
appCflowdTemplate = _AppCflowdTemplate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1007, 1, 6, 1, 4)
)
_AppCflowdTemplateName_Type = OctetString
_AppCflowdTemplateName_Object = MibScalar
appCflowdTemplateName = _AppCflowdTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1007, 1, 6, 1, 4, 1),
    _AppCflowdTemplateName_Type()
)
appCflowdTemplateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdTemplateName.setStatus("current")
_AppCflowdTemplateFlowActiveTimeout_Type = Unsigned32
_AppCflowdTemplateFlowActiveTimeout_Object = MibScalar
appCflowdTemplateFlowActiveTimeout = _AppCflowdTemplateFlowActiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1007, 1, 6, 1, 4, 2),
    _AppCflowdTemplateFlowActiveTimeout_Type()
)
appCflowdTemplateFlowActiveTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdTemplateFlowActiveTimeout.setStatus("current")
_AppCflowdTemplateFlowInactiveTimeout_Type = Unsigned32
_AppCflowdTemplateFlowInactiveTimeout_Object = MibScalar
appCflowdTemplateFlowInactiveTimeout = _AppCflowdTemplateFlowInactiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1007, 1, 6, 1, 4, 3),
    _AppCflowdTemplateFlowInactiveTimeout_Type()
)
appCflowdTemplateFlowInactiveTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdTemplateFlowInactiveTimeout.setStatus("current")
_AppCflowdTemplateTemplateRefresh_Type = Unsigned32
_AppCflowdTemplateTemplateRefresh_Object = MibScalar
appCflowdTemplateTemplateRefresh = _AppCflowdTemplateTemplateRefresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1007, 1, 6, 1, 4, 4),
    _AppCflowdTemplateTemplateRefresh_Type()
)
appCflowdTemplateTemplateRefresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdTemplateTemplateRefresh.setStatus("current")
_CiscoSdwanOperAppMIBNotifObjects_ObjectIdentity = ObjectIdentity
ciscoSdwanOperAppMIBNotifObjects = _CiscoSdwanOperAppMIBNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1007, 2)
)
_CiscoSdwanOperAppMIBConform_ObjectIdentity = ObjectIdentity
ciscoSdwanOperAppMIBConform = _CiscoSdwanOperAppMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1007, 3)
)
_CiscoSdwanOperAppMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSdwanOperAppMIBCompliances = _CiscoSdwanOperAppMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1007, 3, 1)
)
_CiscoSdwanOperAppMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSdwanOperAppMIBGroups = _CiscoSdwanOperAppMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1007, 3, 2)
)

# Managed Objects groups

cSdwanAppCflowdStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1007, 3, 2, 1)
)
cSdwanAppCflowdStatisticsGroup.setObjects(
      *(("CISCO-SDWAN-OPER-APP-MIB", "appCflowdStatisticsDataPackets"),
        ("CISCO-SDWAN-OPER-APP-MIB", "appCflowdStatisticsTemplatePackets"),
        ("CISCO-SDWAN-OPER-APP-MIB", "appCflowdStatisticsTotalPackets"),
        ("CISCO-SDWAN-OPER-APP-MIB", "appCflowdStatisticsFlowRefresh"),
        ("CISCO-SDWAN-OPER-APP-MIB", "appCflowdStatisticsFlowAgeout"),
        ("CISCO-SDWAN-OPER-APP-MIB", "appCflowdStatisticsFlowEndDetected"),
        ("CISCO-SDWAN-OPER-APP-MIB", "appCflowdStatisticsFlowEndForced"),
        ("CISCO-SDWAN-OPER-APP-MIB", "appCflowdStatisticsFlowRateLimitDrop"))
)
if mibBuilder.loadTexts:
    cSdwanAppCflowdStatisticsGroup.setStatus("current")

cSdwanAppCflowdTemplateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1007, 3, 2, 2)
)
cSdwanAppCflowdTemplateGroup.setObjects(
      *(("CISCO-SDWAN-OPER-APP-MIB", "appCflowdTemplateName"),
        ("CISCO-SDWAN-OPER-APP-MIB", "appCflowdTemplateFlowActiveTimeout"),
        ("CISCO-SDWAN-OPER-APP-MIB", "appCflowdTemplateFlowInactiveTimeout"),
        ("CISCO-SDWAN-OPER-APP-MIB", "appCflowdTemplateTemplateRefresh"))
)
if mibBuilder.loadTexts:
    cSdwanAppCflowdTemplateGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoSdwanOperAppMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 1007, 3, 1, 1)
)
ciscoSdwanOperAppMIBCompliance.setObjects(
      *(("CISCO-SDWAN-OPER-APP-MIB", "cSdwanAppCflowdStatisticsGroup"),
        ("CISCO-SDWAN-OPER-APP-MIB", "cSdwanAppCflowdTemplateGroup"))
)
if mibBuilder.loadTexts:
    ciscoSdwanOperAppMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SDWAN-OPER-APP-MIB",
    **{"ciscoSdwanOperAppMIB": ciscoSdwanOperAppMIB,
       "ciscoSdwanOperAppMIBNotifs": ciscoSdwanOperAppMIBNotifs,
       "ciscoSdwanOperAppMIBObjects": ciscoSdwanOperAppMIBObjects,
       "app": app,
       "appCflowd": appCflowd,
       "appCflowdStatistics": appCflowdStatistics,
       "appCflowdStatisticsDataPackets": appCflowdStatisticsDataPackets,
       "appCflowdStatisticsTemplatePackets": appCflowdStatisticsTemplatePackets,
       "appCflowdStatisticsTotalPackets": appCflowdStatisticsTotalPackets,
       "appCflowdStatisticsFlowRefresh": appCflowdStatisticsFlowRefresh,
       "appCflowdStatisticsFlowAgeout": appCflowdStatisticsFlowAgeout,
       "appCflowdStatisticsFlowEndDetected": appCflowdStatisticsFlowEndDetected,
       "appCflowdStatisticsFlowEndForced": appCflowdStatisticsFlowEndForced,
       "appCflowdStatisticsFlowRateLimitDrop": appCflowdStatisticsFlowRateLimitDrop,
       "appCflowdTemplate": appCflowdTemplate,
       "appCflowdTemplateName": appCflowdTemplateName,
       "appCflowdTemplateFlowActiveTimeout": appCflowdTemplateFlowActiveTimeout,
       "appCflowdTemplateFlowInactiveTimeout": appCflowdTemplateFlowInactiveTimeout,
       "appCflowdTemplateTemplateRefresh": appCflowdTemplateTemplateRefresh,
       "ciscoSdwanOperAppMIBNotifObjects": ciscoSdwanOperAppMIBNotifObjects,
       "ciscoSdwanOperAppMIBConform": ciscoSdwanOperAppMIBConform,
       "ciscoSdwanOperAppMIBCompliances": ciscoSdwanOperAppMIBCompliances,
       "ciscoSdwanOperAppMIBCompliance": ciscoSdwanOperAppMIBCompliance,
       "ciscoSdwanOperAppMIBGroups": ciscoSdwanOperAppMIBGroups,
       "cSdwanAppCflowdStatisticsGroup": cSdwanAppCflowdStatisticsGroup,
       "cSdwanAppCflowdTemplateGroup": cSdwanAppCflowdTemplateGroup}
)
