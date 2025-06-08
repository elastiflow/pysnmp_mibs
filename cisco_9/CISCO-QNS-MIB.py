# SNMP MIB module (CISCO-QNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-QNS-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:18:37 2025
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

(broadhopProducts,) = mibBuilder.importSymbols(
    "BROADHOP-MIB",
    "broadhopProducts")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ciscoProductsQNS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 3)
)
if mibBuilder.loadTexts:
    ciscoProductsQNS.setRevisions(
        ("2014-07-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoProductsQNSComponents_ObjectIdentity = ObjectIdentity
ciscoProductsQNSComponents = _CiscoProductsQNSComponents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 3, 2)
)
_CiscoProductsQNSComponents70_ObjectIdentity = ObjectIdentity
ciscoProductsQNSComponents70 = _CiscoProductsQNSComponents70_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 3, 2, 70)
)
_CiscoProductsQNSComponentsSystemStats_ObjectIdentity = ObjectIdentity
ciscoProductsQNSComponentsSystemStats = _CiscoProductsQNSComponentsSystemStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 3, 2, 70, 1)
)
_ComponentCpuUser_Type = Integer32
_ComponentCpuUser_Object = MibScalar
componentCpuUser = _ComponentCpuUser_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 3, 2, 70, 1, 1),
    _ComponentCpuUser_Type()
)
componentCpuUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentCpuUser.setStatus("current")
_ComponentCpuSystem_Type = Integer32
_ComponentCpuSystem_Object = MibScalar
componentCpuSystem = _ComponentCpuSystem_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 3, 2, 70, 1, 2),
    _ComponentCpuSystem_Type()
)
componentCpuSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentCpuSystem.setStatus("current")
_ComponentCpuIdle_Type = Integer32
_ComponentCpuIdle_Object = MibScalar
componentCpuIdle = _ComponentCpuIdle_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 3, 2, 70, 1, 3),
    _ComponentCpuIdle_Type()
)
componentCpuIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentCpuIdle.setStatus("current")
_ComponentLoadAverage1_Type = Integer32
_ComponentLoadAverage1_Object = MibScalar
componentLoadAverage1 = _ComponentLoadAverage1_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 3, 2, 70, 1, 4),
    _ComponentLoadAverage1_Type()
)
componentLoadAverage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLoadAverage1.setStatus("current")
_ComponentLoadAverage5_Type = Integer32
_ComponentLoadAverage5_Object = MibScalar
componentLoadAverage5 = _ComponentLoadAverage5_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 3, 2, 70, 1, 5),
    _ComponentLoadAverage5_Type()
)
componentLoadAverage5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLoadAverage5.setStatus("current")
_ComponentLoadAverage15_Type = Integer32
_ComponentLoadAverage15_Object = MibScalar
componentLoadAverage15 = _ComponentLoadAverage15_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 3, 2, 70, 1, 6),
    _ComponentLoadAverage15_Type()
)
componentLoadAverage15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLoadAverage15.setStatus("current")
_ComponentMemoryTotal_Type = Integer32
_ComponentMemoryTotal_Object = MibScalar
componentMemoryTotal = _ComponentMemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 3, 2, 70, 1, 7),
    _ComponentMemoryTotal_Type()
)
componentMemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentMemoryTotal.setStatus("current")
_ComponentMemoryAvailable_Type = Integer32
_ComponentMemoryAvailable_Object = MibScalar
componentMemoryAvailable = _ComponentMemoryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 3, 2, 70, 1, 8),
    _ComponentMemoryAvailable_Type()
)
componentMemoryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentMemoryAvailable.setStatus("current")
_ComponentSwapTotal_Type = Integer32
_ComponentSwapTotal_Object = MibScalar
componentSwapTotal = _ComponentSwapTotal_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 3, 2, 70, 1, 9),
    _ComponentSwapTotal_Type()
)
componentSwapTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentSwapTotal.setStatus("current")
_ComponentSwapAvailable_Type = Integer32
_ComponentSwapAvailable_Object = MibScalar
componentSwapAvailable = _ComponentSwapAvailable_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 3, 2, 70, 1, 10),
    _ComponentSwapAvailable_Type()
)
componentSwapAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentSwapAvailable.setStatus("current")
_CiscoProductsQNSConsolidatedKPIVersion_ObjectIdentity = ObjectIdentity
ciscoProductsQNSConsolidatedKPIVersion = _CiscoProductsQNSConsolidatedKPIVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 3, 3)
)
_CiscoProductsQNSKPI70_ObjectIdentity = ObjectIdentity
ciscoProductsQNSKPI70 = _CiscoProductsQNSKPI70_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 3, 3, 70)
)
_CiscoProductsQNSKPILB_ObjectIdentity = ObjectIdentity
ciscoProductsQNSKPILB = _CiscoProductsQNSKPILB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 3, 3, 70, 11)
)
_KpiLBPCRFProxyExternalCurrentSessions_Type = DisplayString
_KpiLBPCRFProxyExternalCurrentSessions_Object = MibScalar
kpiLBPCRFProxyExternalCurrentSessions = _KpiLBPCRFProxyExternalCurrentSessions_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 3, 3, 70, 11, 1),
    _KpiLBPCRFProxyExternalCurrentSessions_Type()
)
kpiLBPCRFProxyExternalCurrentSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpiLBPCRFProxyExternalCurrentSessions.setStatus("current")
_KpiLBPCRFProxyInternalCurrentSessions_Type = DisplayString
_KpiLBPCRFProxyInternalCurrentSessions_Object = MibScalar
kpiLBPCRFProxyInternalCurrentSessions = _KpiLBPCRFProxyInternalCurrentSessions_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 3, 3, 70, 11, 2),
    _KpiLBPCRFProxyInternalCurrentSessions_Type()
)
kpiLBPCRFProxyInternalCurrentSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpiLBPCRFProxyInternalCurrentSessions.setStatus("current")
_CiscoProductsQNSKPISessionMgr_ObjectIdentity = ObjectIdentity
ciscoProductsQNSKPISessionMgr = _CiscoProductsQNSKPISessionMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 3, 3, 70, 14)
)
_CiscoProductsQNSKPIQNS_ObjectIdentity = ObjectIdentity
ciscoProductsQNSKPIQNS = _CiscoProductsQNSKPIQNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26878, 200, 3, 3, 70, 15)
)
_KpiQNSPolicyCount_Type = DisplayString
_KpiQNSPolicyCount_Object = MibScalar
kpiQNSPolicyCount = _KpiQNSPolicyCount_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 3, 3, 70, 15, 20),
    _KpiQNSPolicyCount_Type()
)
kpiQNSPolicyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpiQNSPolicyCount.setStatus("current")
_KpiQNSQueueSize_Type = DisplayString
_KpiQNSQueueSize_Object = MibScalar
kpiQNSQueueSize = _KpiQNSQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 3, 3, 70, 15, 21),
    _KpiQNSQueueSize_Type()
)
kpiQNSQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpiQNSQueueSize.setStatus("current")
_KpiQNSFailedEnqueueCount_Type = DisplayString
_KpiQNSFailedEnqueueCount_Object = MibScalar
kpiQNSFailedEnqueueCount = _KpiQNSFailedEnqueueCount_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 3, 3, 70, 15, 22),
    _KpiQNSFailedEnqueueCount_Type()
)
kpiQNSFailedEnqueueCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpiQNSFailedEnqueueCount.setStatus("current")
_KpiQNSErrorCount_Type = DisplayString
_KpiQNSErrorCount_Object = MibScalar
kpiQNSErrorCount = _KpiQNSErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 3, 3, 70, 15, 23),
    _KpiQNSErrorCount_Type()
)
kpiQNSErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpiQNSErrorCount.setStatus("current")
_KpiQNSAggregateSessionCount_Type = DisplayString
_KpiQNSAggregateSessionCount_Object = MibScalar
kpiQNSAggregateSessionCount = _KpiQNSAggregateSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 3, 3, 70, 15, 24),
    _KpiQNSAggregateSessionCount_Type()
)
kpiQNSAggregateSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpiQNSAggregateSessionCount.setStatus("current")
_KpiQNSFreeMemory_Type = DisplayString
_KpiQNSFreeMemory_Object = MibScalar
kpiQNSFreeMemory = _KpiQNSFreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 26878, 200, 3, 3, 70, 15, 25),
    _KpiQNSFreeMemory_Type()
)
kpiQNSFreeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kpiQNSFreeMemory.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-QNS-MIB",
    **{"ciscoProductsQNS": ciscoProductsQNS,
       "ciscoProductsQNSComponents": ciscoProductsQNSComponents,
       "ciscoProductsQNSComponents70": ciscoProductsQNSComponents70,
       "ciscoProductsQNSComponentsSystemStats": ciscoProductsQNSComponentsSystemStats,
       "componentCpuUser": componentCpuUser,
       "componentCpuSystem": componentCpuSystem,
       "componentCpuIdle": componentCpuIdle,
       "componentLoadAverage1": componentLoadAverage1,
       "componentLoadAverage5": componentLoadAverage5,
       "componentLoadAverage15": componentLoadAverage15,
       "componentMemoryTotal": componentMemoryTotal,
       "componentMemoryAvailable": componentMemoryAvailable,
       "componentSwapTotal": componentSwapTotal,
       "componentSwapAvailable": componentSwapAvailable,
       "ciscoProductsQNSConsolidatedKPIVersion": ciscoProductsQNSConsolidatedKPIVersion,
       "ciscoProductsQNSKPI70": ciscoProductsQNSKPI70,
       "ciscoProductsQNSKPILB": ciscoProductsQNSKPILB,
       "kpiLBPCRFProxyExternalCurrentSessions": kpiLBPCRFProxyExternalCurrentSessions,
       "kpiLBPCRFProxyInternalCurrentSessions": kpiLBPCRFProxyInternalCurrentSessions,
       "ciscoProductsQNSKPISessionMgr": ciscoProductsQNSKPISessionMgr,
       "ciscoProductsQNSKPIQNS": ciscoProductsQNSKPIQNS,
       "kpiQNSPolicyCount": kpiQNSPolicyCount,
       "kpiQNSQueueSize": kpiQNSQueueSize,
       "kpiQNSFailedEnqueueCount": kpiQNSFailedEnqueueCount,
       "kpiQNSErrorCount": kpiQNSErrorCount,
       "kpiQNSAggregateSessionCount": kpiQNSAggregateSessionCount,
       "kpiQNSFreeMemory": kpiQNSFreeMemory}
)
