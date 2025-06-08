# SNMP MIB module (RD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/iptivia_25406/RD-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 10:49:45 2025
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

iptiviaMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25406)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RdRoot_ObjectIdentity = ObjectIdentity
rdRoot = _RdRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25406, 1)
)
_Rd_ObjectIdentity = ObjectIdentity
rd = _Rd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1)
)
_RdAlarmVars_ObjectIdentity = ObjectIdentity
rdAlarmVars = _RdAlarmVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25406, 1, 2)
)
_RdAlarmSeverity_Type = DisplayString
_RdAlarmSeverity_Object = MibScalar
rdAlarmSeverity = _RdAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 25406, 1, 2, 1),
    _RdAlarmSeverity_Type()
)
rdAlarmSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rdAlarmSeverity.setStatus("current")
_RdAlarmDescription_Type = DisplayString
_RdAlarmDescription_Object = MibScalar
rdAlarmDescription = _RdAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 25406, 1, 2, 2),
    _RdAlarmDescription_Type()
)
rdAlarmDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rdAlarmDescription.setStatus("current")
_RdAlarmInfo_Type = DisplayString
_RdAlarmInfo_Object = MibScalar
rdAlarmInfo = _RdAlarmInfo_Object(
    (1, 3, 6, 1, 4, 1, 25406, 1, 2, 3),
    _RdAlarmInfo_Type()
)
rdAlarmInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rdAlarmInfo.setStatus("current")
_RdAlarmEventIds_Type = DisplayString
_RdAlarmEventIds_Object = MibScalar
rdAlarmEventIds = _RdAlarmEventIds_Object(
    (1, 3, 6, 1, 4, 1, 25406, 1, 2, 4),
    _RdAlarmEventIds_Type()
)
rdAlarmEventIds.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rdAlarmEventIds.setStatus("current")

# Managed Objects groups


# Notification objects

rdAlmOSPFRouterActivity = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 1)
)
rdAlmOSPFRouterActivity.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"),
        ("RD-MIB", "rdAlarmInfo"),
        ("RD-MIB", "rdAlarmEventIds"))
)
if mibBuilder.loadTexts:
    rdAlmOSPFRouterActivity.setStatus(
        "current"
    )

rdAlmOSPFStubAdvertActivity = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 2)
)
rdAlmOSPFStubAdvertActivity.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"),
        ("RD-MIB", "rdAlarmInfo"),
        ("RD-MIB", "rdAlarmEventIds"))
)
if mibBuilder.loadTexts:
    rdAlmOSPFStubAdvertActivity.setStatus(
        "current"
    )

rdAlmOSPFNumP2PActivity = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 3)
)
rdAlmOSPFNumP2PActivity.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"),
        ("RD-MIB", "rdAlarmInfo"),
        ("RD-MIB", "rdAlarmEventIds"))
)
if mibBuilder.loadTexts:
    rdAlmOSPFNumP2PActivity.setStatus(
        "current"
    )

rdAlmOSPFUnnumP2PActivity = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 4)
)
rdAlmOSPFUnnumP2PActivity.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"),
        ("RD-MIB", "rdAlarmInfo"),
        ("RD-MIB", "rdAlarmEventIds"))
)
if mibBuilder.loadTexts:
    rdAlmOSPFUnnumP2PActivity.setStatus(
        "current"
    )

rdAlmOSPFTransitIfActivity = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 5)
)
rdAlmOSPFTransitIfActivity.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"),
        ("RD-MIB", "rdAlarmInfo"),
        ("RD-MIB", "rdAlarmEventIds"))
)
if mibBuilder.loadTexts:
    rdAlmOSPFTransitIfActivity.setStatus(
        "current"
    )

rdAlmOSPFTransitNetworkActivity = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 6)
)
rdAlmOSPFTransitNetworkActivity.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"),
        ("RD-MIB", "rdAlarmInfo"),
        ("RD-MIB", "rdAlarmEventIds"))
)
if mibBuilder.loadTexts:
    rdAlmOSPFTransitNetworkActivity.setStatus(
        "current"
    )

rdAlmOSPFExtRouteActivity = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 7)
)
rdAlmOSPFExtRouteActivity.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"),
        ("RD-MIB", "rdAlarmInfo"),
        ("RD-MIB", "rdAlarmEventIds"))
)
if mibBuilder.loadTexts:
    rdAlmOSPFExtRouteActivity.setStatus(
        "current"
    )

rdAlmIfIPAddrConflictActivity = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 8)
)
rdAlmIfIPAddrConflictActivity.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"),
        ("RD-MIB", "rdAlarmInfo"),
        ("RD-MIB", "rdAlarmEventIds"))
)
if mibBuilder.loadTexts:
    rdAlmIfIPAddrConflictActivity.setStatus(
        "current"
    )

rdAlmOSPFCorePrefixActivity = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 20)
)
rdAlmOSPFCorePrefixActivity.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"),
        ("RD-MIB", "rdAlarmInfo"),
        ("RD-MIB", "rdAlarmEventIds"))
)
if mibBuilder.loadTexts:
    rdAlmOSPFCorePrefixActivity.setStatus(
        "current"
    )

rdAlmOSPFExtPrefixActivity = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 21)
)
rdAlmOSPFExtPrefixActivity.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"),
        ("RD-MIB", "rdAlarmInfo"),
        ("RD-MIB", "rdAlarmEventIds"))
)
if mibBuilder.loadTexts:
    rdAlmOSPFExtPrefixActivity.setStatus(
        "current"
    )

rdAlmBGPRouteActivity = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 30)
)
rdAlmBGPRouteActivity.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"),
        ("RD-MIB", "rdAlarmInfo"),
        ("RD-MIB", "rdAlarmEventIds"))
)
if mibBuilder.loadTexts:
    rdAlmBGPRouteActivity.setStatus(
        "current"
    )

rdAlmBGPPrevixActivity = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 40)
)
rdAlmBGPPrevixActivity.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"),
        ("RD-MIB", "rdAlarmInfo"),
        ("RD-MIB", "rdAlarmEventIds"))
)
if mibBuilder.loadTexts:
    rdAlmBGPPrevixActivity.setStatus(
        "current"
    )

rdAlmEndtoEndServiceActivity = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 100)
)
rdAlmEndtoEndServiceActivity.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"),
        ("RD-MIB", "rdAlarmInfo"),
        ("RD-MIB", "rdAlarmEventIds"))
)
if mibBuilder.loadTexts:
    rdAlmEndtoEndServiceActivity.setStatus(
        "current"
    )

rdAlmEndtoEndServicePathActivity = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 101)
)
rdAlmEndtoEndServicePathActivity.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"),
        ("RD-MIB", "rdAlarmInfo"),
        ("RD-MIB", "rdAlarmEventIds"))
)
if mibBuilder.loadTexts:
    rdAlmEndtoEndServicePathActivity.setStatus(
        "current"
    )

rdAlmEndtoEndStaticMcastServiceActivity = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 110)
)
rdAlmEndtoEndStaticMcastServiceActivity.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"),
        ("RD-MIB", "rdAlarmInfo"),
        ("RD-MIB", "rdAlarmEventIds"))
)
if mibBuilder.loadTexts:
    rdAlmEndtoEndStaticMcastServiceActivity.setStatus(
        "current"
    )

rdAlmEndtoEndStaticMcastGroupActivity = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 111)
)
rdAlmEndtoEndStaticMcastGroupActivity.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"),
        ("RD-MIB", "rdAlarmInfo"),
        ("RD-MIB", "rdAlarmEventIds"))
)
if mibBuilder.loadTexts:
    rdAlmEndtoEndStaticMcastGroupActivity.setStatus(
        "current"
    )

rdAlmDynamicMcastFlowActivity = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 113)
)
rdAlmDynamicMcastFlowActivity.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"),
        ("RD-MIB", "rdAlarmInfo"),
        ("RD-MIB", "rdAlarmEventIds"))
)
if mibBuilder.loadTexts:
    rdAlmDynamicMcastFlowActivity.setStatus(
        "current"
    )

rdAlmOSPFUnnumP2PIfEventRateThrshld = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 211)
)
rdAlmOSPFUnnumP2PIfEventRateThrshld.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"),
        ("RD-MIB", "rdAlarmInfo"),
        ("RD-MIB", "rdAlarmEventIds"))
)
if mibBuilder.loadTexts:
    rdAlmOSPFUnnumP2PIfEventRateThrshld.setStatus(
        "current"
    )

rdAlmOSPFNumP2PEventRateThrshld = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 212)
)
rdAlmOSPFNumP2PEventRateThrshld.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"),
        ("RD-MIB", "rdAlarmInfo"),
        ("RD-MIB", "rdAlarmEventIds"))
)
if mibBuilder.loadTexts:
    rdAlmOSPFNumP2PEventRateThrshld.setStatus(
        "current"
    )

rdAlmOSPFTransitIfEventRateThrshld = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 213)
)
rdAlmOSPFTransitIfEventRateThrshld.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"),
        ("RD-MIB", "rdAlarmInfo"),
        ("RD-MIB", "rdAlarmEventIds"))
)
if mibBuilder.loadTexts:
    rdAlmOSPFTransitIfEventRateThrshld.setStatus(
        "current"
    )

rdAlmOSPFTransitRtr2RtrLinkEventRateThrshld = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 214)
)
rdAlmOSPFTransitRtr2RtrLinkEventRateThrshld.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"),
        ("RD-MIB", "rdAlarmInfo"),
        ("RD-MIB", "rdAlarmEventIds"))
)
if mibBuilder.loadTexts:
    rdAlmOSPFTransitRtr2RtrLinkEventRateThrshld.setStatus(
        "current"
    )

rdAlmOSPFTransitNetworkEventRateThrshld = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 215)
)
rdAlmOSPFTransitNetworkEventRateThrshld.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"),
        ("RD-MIB", "rdAlarmInfo"),
        ("RD-MIB", "rdAlarmEventIds"))
)
if mibBuilder.loadTexts:
    rdAlmOSPFTransitNetworkEventRateThrshld.setStatus(
        "current"
    )

rdAlmOSPFStubRouteEventRateThrshld = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 216)
)
rdAlmOSPFStubRouteEventRateThrshld.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"),
        ("RD-MIB", "rdAlarmInfo"),
        ("RD-MIB", "rdAlarmEventIds"))
)
if mibBuilder.loadTexts:
    rdAlmOSPFStubRouteEventRateThrshld.setStatus(
        "current"
    )

rdAlmOSPFExtRouteEventRateThrshld = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 217)
)
rdAlmOSPFExtRouteEventRateThrshld.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"),
        ("RD-MIB", "rdAlarmInfo"),
        ("RD-MIB", "rdAlarmEventIds"))
)
if mibBuilder.loadTexts:
    rdAlmOSPFExtRouteEventRateThrshld.setStatus(
        "current"
    )

rdAlmOSPFRouterEventRateThrshld = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 218)
)
rdAlmOSPFRouterEventRateThrshld.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"),
        ("RD-MIB", "rdAlarmInfo"),
        ("RD-MIB", "rdAlarmEventIds"))
)
if mibBuilder.loadTexts:
    rdAlmOSPFRouterEventRateThrshld.setStatus(
        "current"
    )

rdAlmAdjacentOSPFUnnumP2PIfThrshld = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 221)
)
rdAlmAdjacentOSPFUnnumP2PIfThrshld.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"),
        ("RD-MIB", "rdAlarmInfo"),
        ("RD-MIB", "rdAlarmEventIds"))
)
if mibBuilder.loadTexts:
    rdAlmAdjacentOSPFUnnumP2PIfThrshld.setStatus(
        "current"
    )

rdAlmAdjacentOSPFNumP2PIfThrshld = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 222)
)
rdAlmAdjacentOSPFNumP2PIfThrshld.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"),
        ("RD-MIB", "rdAlarmInfo"),
        ("RD-MIB", "rdAlarmEventIds"))
)
if mibBuilder.loadTexts:
    rdAlmAdjacentOSPFNumP2PIfThrshld.setStatus(
        "current"
    )

rdAlmAdjacentOSPFTransitIfThrshld = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 223)
)
rdAlmAdjacentOSPFTransitIfThrshld.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"),
        ("RD-MIB", "rdAlarmInfo"),
        ("RD-MIB", "rdAlarmEventIds"))
)
if mibBuilder.loadTexts:
    rdAlmAdjacentOSPFTransitIfThrshld.setStatus(
        "current"
    )

rdAlmAdjacentOSPFTransitRouterLinkThrshld = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 224)
)
rdAlmAdjacentOSPFTransitRouterLinkThrshld.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"),
        ("RD-MIB", "rdAlarmInfo"),
        ("RD-MIB", "rdAlarmEventIds"))
)
if mibBuilder.loadTexts:
    rdAlmAdjacentOSPFTransitRouterLinkThrshld.setStatus(
        "current"
    )

rdAlmAvailOSPFTransitNetworkThrshld = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 225)
)
rdAlmAvailOSPFTransitNetworkThrshld.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"),
        ("RD-MIB", "rdAlarmInfo"),
        ("RD-MIB", "rdAlarmEventIds"))
)
if mibBuilder.loadTexts:
    rdAlmAvailOSPFTransitNetworkThrshld.setStatus(
        "current"
    )

rdAlmAvailOSPFStubRouteThrshld = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 226)
)
rdAlmAvailOSPFStubRouteThrshld.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"),
        ("RD-MIB", "rdAlarmInfo"),
        ("RD-MIB", "rdAlarmEventIds"))
)
if mibBuilder.loadTexts:
    rdAlmAvailOSPFStubRouteThrshld.setStatus(
        "current"
    )

rdAlmAvailOSPFExtRouteEntityThrshld = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 227)
)
rdAlmAvailOSPFExtRouteEntityThrshld.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"),
        ("RD-MIB", "rdAlarmInfo"),
        ("RD-MIB", "rdAlarmEventIds"))
)
if mibBuilder.loadTexts:
    rdAlmAvailOSPFExtRouteEntityThrshld.setStatus(
        "current"
    )

rdAlmAvailOSPFRouterThrshld = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 228)
)
rdAlmAvailOSPFRouterThrshld.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"),
        ("RD-MIB", "rdAlarmInfo"),
        ("RD-MIB", "rdAlarmEventIds"))
)
if mibBuilder.loadTexts:
    rdAlmAvailOSPFRouterThrshld.setStatus(
        "current"
    )

rdAlmAvailBGPRoutesDomainThrshld = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 231)
)
rdAlmAvailBGPRoutesDomainThrshld.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"),
        ("RD-MIB", "rdAlarmInfo"),
        ("RD-MIB", "rdAlarmEventIds"))
)
if mibBuilder.loadTexts:
    rdAlmAvailBGPRoutesDomainThrshld.setStatus(
        "current"
    )

rdAlmBGPRoutesDomainEventRateThrshld = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 232)
)
rdAlmBGPRoutesDomainEventRateThrshld.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"),
        ("RD-MIB", "rdAlarmInfo"),
        ("RD-MIB", "rdAlarmEventIds"))
)
if mibBuilder.loadTexts:
    rdAlmBGPRoutesDomainEventRateThrshld.setStatus(
        "current"
    )

rdAlmAvailBGPRoutesSpeakerThrshld = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 233)
)
rdAlmAvailBGPRoutesSpeakerThrshld.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"),
        ("RD-MIB", "rdAlarmInfo"),
        ("RD-MIB", "rdAlarmEventIds"))
)
if mibBuilder.loadTexts:
    rdAlmAvailBGPRoutesSpeakerThrshld.setStatus(
        "current"
    )

rdAlmBGPRoutesSpeakerEventRateThrshld = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 234)
)
rdAlmBGPRoutesSpeakerEventRateThrshld.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"),
        ("RD-MIB", "rdAlarmInfo"),
        ("RD-MIB", "rdAlarmEventIds"))
)
if mibBuilder.loadTexts:
    rdAlmBGPRoutesSpeakerEventRateThrshld.setStatus(
        "current"
    )

rdAlmCollectorDownTrapId = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 500)
)
rdAlmCollectorDownTrapId.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"))
)
if mibBuilder.loadTexts:
    rdAlmCollectorDownTrapId.setStatus(
        "current"
    )

rdAlmCollectorUpTrapId = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 501)
)
rdAlmCollectorUpTrapId.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"))
)
if mibBuilder.loadTexts:
    rdAlmCollectorUpTrapId.setStatus(
        "current"
    )

rdAlmConfigurationTrapId = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 510)
)
rdAlmConfigurationTrapId.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"))
)
if mibBuilder.loadTexts:
    rdAlmConfigurationTrapId.setStatus(
        "current"
    )

rdAlmCpuHighTrapId = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 600)
)
rdAlmCpuHighTrapId.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"))
)
if mibBuilder.loadTexts:
    rdAlmCpuHighTrapId.setStatus(
        "current"
    )

rdAlmCpuLowTrapId = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 601)
)
rdAlmCpuLowTrapId.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"))
)
if mibBuilder.loadTexts:
    rdAlmCpuLowTrapId.setStatus(
        "current"
    )

rdAlmDatabaseFullTrapId = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 610)
)
rdAlmDatabaseFullTrapId.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"))
)
if mibBuilder.loadTexts:
    rdAlmDatabaseFullTrapId.setStatus(
        "current"
    )

rdAlmDatabaseNotFullTrapId = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 611)
)
rdAlmDatabaseNotFullTrapId.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"))
)
if mibBuilder.loadTexts:
    rdAlmDatabaseNotFullTrapId.setStatus(
        "current"
    )

rdAlmDiskFullTrapId = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 620)
)
rdAlmDiskFullTrapId.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"))
)
if mibBuilder.loadTexts:
    rdAlmDiskFullTrapId.setStatus(
        "current"
    )

rdAlmDiskNotFullTrapId = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 621)
)
rdAlmDiskNotFullTrapId.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"))
)
if mibBuilder.loadTexts:
    rdAlmDiskNotFullTrapId.setStatus(
        "current"
    )

rdAlmMapStartedTrapId = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 800)
)
rdAlmMapStartedTrapId.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"))
)
if mibBuilder.loadTexts:
    rdAlmMapStartedTrapId.setStatus(
        "current"
    )

rdAlmMapShutdownTrapId = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 801)
)
rdAlmMapShutdownTrapId.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"))
)
if mibBuilder.loadTexts:
    rdAlmMapShutdownTrapId.setStatus(
        "current"
    )

rdAlmListenerStartedTrapId = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 810)
)
rdAlmListenerStartedTrapId.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"))
)
if mibBuilder.loadTexts:
    rdAlmListenerStartedTrapId.setStatus(
        "current"
    )

rdAlmListenerShutdownTrapId = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 811)
)
rdAlmListenerShutdownTrapId.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"))
)
if mibBuilder.loadTexts:
    rdAlmListenerShutdownTrapId.setStatus(
        "current"
    )

rdAlmDbServerConnectedTrapId = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 820)
)
rdAlmDbServerConnectedTrapId.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"))
)
if mibBuilder.loadTexts:
    rdAlmDbServerConnectedTrapId.setStatus(
        "current"
    )

rdAlmDbServerNotConnectedTrapId = NotificationType(
    (1, 3, 6, 1, 4, 1, 25406, 1, 1, 821)
)
rdAlmDbServerNotConnectedTrapId.setObjects(
      *(("RD-MIB", "rdAlarmSeverity"),
        ("RD-MIB", "rdAlarmDescription"))
)
if mibBuilder.loadTexts:
    rdAlmDbServerNotConnectedTrapId.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RD-MIB",
    **{"iptiviaMib": iptiviaMib,
       "rdRoot": rdRoot,
       "rd": rd,
       "rdAlmOSPFRouterActivity": rdAlmOSPFRouterActivity,
       "rdAlmOSPFStubAdvertActivity": rdAlmOSPFStubAdvertActivity,
       "rdAlmOSPFNumP2PActivity": rdAlmOSPFNumP2PActivity,
       "rdAlmOSPFUnnumP2PActivity": rdAlmOSPFUnnumP2PActivity,
       "rdAlmOSPFTransitIfActivity": rdAlmOSPFTransitIfActivity,
       "rdAlmOSPFTransitNetworkActivity": rdAlmOSPFTransitNetworkActivity,
       "rdAlmOSPFExtRouteActivity": rdAlmOSPFExtRouteActivity,
       "rdAlmIfIPAddrConflictActivity": rdAlmIfIPAddrConflictActivity,
       "rdAlmOSPFCorePrefixActivity": rdAlmOSPFCorePrefixActivity,
       "rdAlmOSPFExtPrefixActivity": rdAlmOSPFExtPrefixActivity,
       "rdAlmBGPRouteActivity": rdAlmBGPRouteActivity,
       "rdAlmBGPPrevixActivity": rdAlmBGPPrevixActivity,
       "rdAlmEndtoEndServiceActivity": rdAlmEndtoEndServiceActivity,
       "rdAlmEndtoEndServicePathActivity": rdAlmEndtoEndServicePathActivity,
       "rdAlmEndtoEndStaticMcastServiceActivity": rdAlmEndtoEndStaticMcastServiceActivity,
       "rdAlmEndtoEndStaticMcastGroupActivity": rdAlmEndtoEndStaticMcastGroupActivity,
       "rdAlmDynamicMcastFlowActivity": rdAlmDynamicMcastFlowActivity,
       "rdAlmOSPFUnnumP2PIfEventRateThrshld": rdAlmOSPFUnnumP2PIfEventRateThrshld,
       "rdAlmOSPFNumP2PEventRateThrshld": rdAlmOSPFNumP2PEventRateThrshld,
       "rdAlmOSPFTransitIfEventRateThrshld": rdAlmOSPFTransitIfEventRateThrshld,
       "rdAlmOSPFTransitRtr2RtrLinkEventRateThrshld": rdAlmOSPFTransitRtr2RtrLinkEventRateThrshld,
       "rdAlmOSPFTransitNetworkEventRateThrshld": rdAlmOSPFTransitNetworkEventRateThrshld,
       "rdAlmOSPFStubRouteEventRateThrshld": rdAlmOSPFStubRouteEventRateThrshld,
       "rdAlmOSPFExtRouteEventRateThrshld": rdAlmOSPFExtRouteEventRateThrshld,
       "rdAlmOSPFRouterEventRateThrshld": rdAlmOSPFRouterEventRateThrshld,
       "rdAlmAdjacentOSPFUnnumP2PIfThrshld": rdAlmAdjacentOSPFUnnumP2PIfThrshld,
       "rdAlmAdjacentOSPFNumP2PIfThrshld": rdAlmAdjacentOSPFNumP2PIfThrshld,
       "rdAlmAdjacentOSPFTransitIfThrshld": rdAlmAdjacentOSPFTransitIfThrshld,
       "rdAlmAdjacentOSPFTransitRouterLinkThrshld": rdAlmAdjacentOSPFTransitRouterLinkThrshld,
       "rdAlmAvailOSPFTransitNetworkThrshld": rdAlmAvailOSPFTransitNetworkThrshld,
       "rdAlmAvailOSPFStubRouteThrshld": rdAlmAvailOSPFStubRouteThrshld,
       "rdAlmAvailOSPFExtRouteEntityThrshld": rdAlmAvailOSPFExtRouteEntityThrshld,
       "rdAlmAvailOSPFRouterThrshld": rdAlmAvailOSPFRouterThrshld,
       "rdAlmAvailBGPRoutesDomainThrshld": rdAlmAvailBGPRoutesDomainThrshld,
       "rdAlmBGPRoutesDomainEventRateThrshld": rdAlmBGPRoutesDomainEventRateThrshld,
       "rdAlmAvailBGPRoutesSpeakerThrshld": rdAlmAvailBGPRoutesSpeakerThrshld,
       "rdAlmBGPRoutesSpeakerEventRateThrshld": rdAlmBGPRoutesSpeakerEventRateThrshld,
       "rdAlmCollectorDownTrapId": rdAlmCollectorDownTrapId,
       "rdAlmCollectorUpTrapId": rdAlmCollectorUpTrapId,
       "rdAlmConfigurationTrapId": rdAlmConfigurationTrapId,
       "rdAlmCpuHighTrapId": rdAlmCpuHighTrapId,
       "rdAlmCpuLowTrapId": rdAlmCpuLowTrapId,
       "rdAlmDatabaseFullTrapId": rdAlmDatabaseFullTrapId,
       "rdAlmDatabaseNotFullTrapId": rdAlmDatabaseNotFullTrapId,
       "rdAlmDiskFullTrapId": rdAlmDiskFullTrapId,
       "rdAlmDiskNotFullTrapId": rdAlmDiskNotFullTrapId,
       "rdAlmMapStartedTrapId": rdAlmMapStartedTrapId,
       "rdAlmMapShutdownTrapId": rdAlmMapShutdownTrapId,
       "rdAlmListenerStartedTrapId": rdAlmListenerStartedTrapId,
       "rdAlmListenerShutdownTrapId": rdAlmListenerShutdownTrapId,
       "rdAlmDbServerConnectedTrapId": rdAlmDbServerConnectedTrapId,
       "rdAlmDbServerNotConnectedTrapId": rdAlmDbServerNotConnectedTrapId,
       "rdAlarmVars": rdAlarmVars,
       "rdAlarmSeverity": rdAlarmSeverity,
       "rdAlarmDescription": rdAlarmDescription,
       "rdAlarmInfo": rdAlarmInfo,
       "rdAlarmEventIds": rdAlarmEventIds}
)
