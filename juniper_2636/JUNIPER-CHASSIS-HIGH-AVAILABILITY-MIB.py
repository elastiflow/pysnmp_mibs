# SNMP MIB module (JUNIPER-CHASSIS-HIGH-AVAILABILITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/juniper_2636/JUNIPER-CHASSIS-HIGH-AVAILABILITY-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:48:42 2025
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

(jnxJsChassisHA,) = mibBuilder.importSymbols(
    "JUNIPER-JS-SMI",
    "jnxJsChassisHA")

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

jnxJsChassisHAMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 19, 1)
)
if mibBuilder.loadTexts:
    jnxJsChassisHAMIB.setRevisions(
        ("2020-03-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxJsChassisHANotifications_ObjectIdentity = ObjectIdentity
jnxJsChassisHANotifications = _JnxJsChassisHANotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 19, 1, 0)
)
_JnxJsChassisHATrapObjects_ObjectIdentity = ObjectIdentity
jnxJsChassisHATrapObjects = _JnxJsChassisHATrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 19, 1, 1)
)
_JnxJsChHASwitchoverInfoServicesRedundancyGroup_Type = DisplayString
_JnxJsChHASwitchoverInfoServicesRedundancyGroup_Object = MibScalar
jnxJsChHASwitchoverInfoServicesRedundancyGroup = _JnxJsChHASwitchoverInfoServicesRedundancyGroup_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 19, 1, 1, 1),
    _JnxJsChHASwitchoverInfoServicesRedundancyGroup_Type()
)
jnxJsChHASwitchoverInfoServicesRedundancyGroup.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChHASwitchoverInfoServicesRedundancyGroup.setStatus("current")
_JnxJsChHASwitchoverInfoNodeId_Type = DisplayString
_JnxJsChHASwitchoverInfoNodeId_Object = MibScalar
jnxJsChHASwitchoverInfoNodeId = _JnxJsChHASwitchoverInfoNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 19, 1, 1, 2),
    _JnxJsChHASwitchoverInfoNodeId_Type()
)
jnxJsChHASwitchoverInfoNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChHASwitchoverInfoNodeId.setStatus("current")
_JnxJsChHASwitchoverInfoPreviousState_Type = DisplayString
_JnxJsChHASwitchoverInfoPreviousState_Object = MibScalar
jnxJsChHASwitchoverInfoPreviousState = _JnxJsChHASwitchoverInfoPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 19, 1, 1, 3),
    _JnxJsChHASwitchoverInfoPreviousState_Type()
)
jnxJsChHASwitchoverInfoPreviousState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChHASwitchoverInfoPreviousState.setStatus("current")
_JnxJsChHASwitchoverInfoCurrentState_Type = DisplayString
_JnxJsChHASwitchoverInfoCurrentState_Object = MibScalar
jnxJsChHASwitchoverInfoCurrentState = _JnxJsChHASwitchoverInfoCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 19, 1, 1, 4),
    _JnxJsChHASwitchoverInfoCurrentState_Type()
)
jnxJsChHASwitchoverInfoCurrentState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChHASwitchoverInfoCurrentState.setStatus("current")
_JnxJsChHASwitchoverInfoReason_Type = DisplayString
_JnxJsChHASwitchoverInfoReason_Object = MibScalar
jnxJsChHASwitchoverInfoReason = _JnxJsChHASwitchoverInfoReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 19, 1, 1, 5),
    _JnxJsChHASwitchoverInfoReason_Type()
)
jnxJsChHASwitchoverInfoReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChHASwitchoverInfoReason.setStatus("current")
_JnxJsChHAPeerLinkTrapName_Type = DisplayString
_JnxJsChHAPeerLinkTrapName_Object = MibScalar
jnxJsChHAPeerLinkTrapName = _JnxJsChHAPeerLinkTrapName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 19, 1, 1, 6),
    _JnxJsChHAPeerLinkTrapName_Type()
)
jnxJsChHAPeerLinkTrapName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChHAPeerLinkTrapName.setStatus("current")
_JnxJsChHAPeerLinkTrapState_Type = DisplayString
_JnxJsChHAPeerLinkTrapState_Object = MibScalar
jnxJsChHAPeerLinkTrapState = _JnxJsChHAPeerLinkTrapState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 19, 1, 1, 7),
    _JnxJsChHAPeerLinkTrapState_Type()
)
jnxJsChHAPeerLinkTrapState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChHAPeerLinkTrapState.setStatus("current")
_JnxJsChHAPeerLinkTrapSeverity_Type = DisplayString
_JnxJsChHAPeerLinkTrapSeverity_Object = MibScalar
jnxJsChHAPeerLinkTrapSeverity = _JnxJsChHAPeerLinkTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 19, 1, 1, 8),
    _JnxJsChHAPeerLinkTrapSeverity_Type()
)
jnxJsChHAPeerLinkTrapSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChHAPeerLinkTrapSeverity.setStatus("current")
_JnxJsChHAPeerLinkTrapStateReason_Type = DisplayString
_JnxJsChHAPeerLinkTrapStateReason_Object = MibScalar
jnxJsChHAPeerLinkTrapStateReason = _JnxJsChHAPeerLinkTrapStateReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 19, 1, 1, 9),
    _JnxJsChHAPeerLinkTrapStateReason_Type()
)
jnxJsChHAPeerLinkTrapStateReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChHAPeerLinkTrapStateReason.setStatus("current")
_JnxJsChHANodeHealthStatusNodeID_Type = DisplayString
_JnxJsChHANodeHealthStatusNodeID_Object = MibScalar
jnxJsChHANodeHealthStatusNodeID = _JnxJsChHANodeHealthStatusNodeID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 19, 1, 1, 10),
    _JnxJsChHANodeHealthStatusNodeID_Type()
)
jnxJsChHANodeHealthStatusNodeID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChHANodeHealthStatusNodeID.setStatus("current")
_JnxJsChHANodeHealthStatusSeverity_Type = DisplayString
_JnxJsChHANodeHealthStatusSeverity_Object = MibScalar
jnxJsChHANodeHealthStatusSeverity = _JnxJsChHANodeHealthStatusSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 19, 1, 1, 11),
    _JnxJsChHANodeHealthStatusSeverity_Type()
)
jnxJsChHANodeHealthStatusSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChHANodeHealthStatusSeverity.setStatus("current")
_JnxJsChHANodeHealthStatusReason_Type = DisplayString
_JnxJsChHANodeHealthStatusReason_Object = MibScalar
jnxJsChHANodeHealthStatusReason = _JnxJsChHANodeHealthStatusReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 19, 1, 1, 12),
    _JnxJsChHANodeHealthStatusReason_Type()
)
jnxJsChHANodeHealthStatusReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChHANodeHealthStatusReason.setStatus("current")
_JnxJsChHAPeerID_Type = DisplayString
_JnxJsChHAPeerID_Object = MibScalar
jnxJsChHAPeerID = _JnxJsChHAPeerID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 19, 1, 1, 13),
    _JnxJsChHAPeerID_Type()
)
jnxJsChHAPeerID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChHAPeerID.setStatus("current")
_JnxJsChHAPeerBfdSeverity_Type = DisplayString
_JnxJsChHAPeerBfdSeverity_Object = MibScalar
jnxJsChHAPeerBfdSeverity = _JnxJsChHAPeerBfdSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 19, 1, 1, 14),
    _JnxJsChHAPeerBfdSeverity_Type()
)
jnxJsChHAPeerBfdSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChHAPeerBfdSeverity.setStatus("current")
_JnxJsChHAPeerBfdReason_Type = DisplayString
_JnxJsChHAPeerBfdReason_Object = MibScalar
jnxJsChHAPeerBfdReason = _JnxJsChHAPeerBfdReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 19, 1, 1, 15),
    _JnxJsChHAPeerBfdReason_Type()
)
jnxJsChHAPeerBfdReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChHAPeerBfdReason.setStatus("current")
_JnxJsChHASrgHealthStatusNodeID_Type = DisplayString
_JnxJsChHASrgHealthStatusNodeID_Object = MibScalar
jnxJsChHASrgHealthStatusNodeID = _JnxJsChHASrgHealthStatusNodeID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 19, 1, 1, 16),
    _JnxJsChHASrgHealthStatusNodeID_Type()
)
jnxJsChHASrgHealthStatusNodeID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChHASrgHealthStatusNodeID.setStatus("current")
_JnxJsChHASrgHealthStatusServicesRedundancyGroup_Type = DisplayString
_JnxJsChHASrgHealthStatusServicesRedundancyGroup_Object = MibScalar
jnxJsChHASrgHealthStatusServicesRedundancyGroup = _JnxJsChHASrgHealthStatusServicesRedundancyGroup_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 19, 1, 1, 17),
    _JnxJsChHASrgHealthStatusServicesRedundancyGroup_Type()
)
jnxJsChHASrgHealthStatusServicesRedundancyGroup.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChHASrgHealthStatusServicesRedundancyGroup.setStatus("current")
_JnxJsChHASrgHealthStatusReason_Type = DisplayString
_JnxJsChHASrgHealthStatusReason_Object = MibScalar
jnxJsChHASrgHealthStatusReason = _JnxJsChHASrgHealthStatusReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 19, 1, 1, 18),
    _JnxJsChHASrgHealthStatusReason_Type()
)
jnxJsChHASrgHealthStatusReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChHASrgHealthStatusReason.setStatus("current")
_JnxJsChHASrgActEnfFlrTrapSrgID_Type = DisplayString
_JnxJsChHASrgActEnfFlrTrapSrgID_Object = MibScalar
jnxJsChHASrgActEnfFlrTrapSrgID = _JnxJsChHASrgActEnfFlrTrapSrgID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 19, 1, 1, 19),
    _JnxJsChHASrgActEnfFlrTrapSrgID_Type()
)
jnxJsChHASrgActEnfFlrTrapSrgID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChHASrgActEnfFlrTrapSrgID.setStatus("current")
_JnxJsChHASrgActEnfFlrTrapNodeID_Type = DisplayString
_JnxJsChHASrgActEnfFlrTrapNodeID_Object = MibScalar
jnxJsChHASrgActEnfFlrTrapNodeID = _JnxJsChHASrgActEnfFlrTrapNodeID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 19, 1, 1, 20),
    _JnxJsChHASrgActEnfFlrTrapNodeID_Type()
)
jnxJsChHASrgActEnfFlrTrapNodeID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChHASrgActEnfFlrTrapNodeID.setStatus("current")
_JnxJsChHASrgActEnfFlrTrapCurrentState_Type = DisplayString
_JnxJsChHASrgActEnfFlrTrapCurrentState_Object = MibScalar
jnxJsChHASrgActEnfFlrTrapCurrentState = _JnxJsChHASrgActEnfFlrTrapCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 19, 1, 1, 21),
    _JnxJsChHASrgActEnfFlrTrapCurrentState_Type()
)
jnxJsChHASrgActEnfFlrTrapCurrentState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChHASrgActEnfFlrTrapCurrentState.setStatus("current")

# Managed Objects groups


# Notification objects

jnxJsChHASwitchover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 19, 1, 0, 1)
)
jnxJsChHASwitchover.setObjects(
      *(("JUNIPER-CHASSIS-HIGH-AVAILABILITY-MIB", "jnxJsChHASwitchoverInfoServicesRedundancyGroup"),
        ("JUNIPER-CHASSIS-HIGH-AVAILABILITY-MIB", "jnxJsChHASwitchoverInfoNodeId"),
        ("JUNIPER-CHASSIS-HIGH-AVAILABILITY-MIB", "jnxJsChHASwitchoverInfoPreviousState"),
        ("JUNIPER-CHASSIS-HIGH-AVAILABILITY-MIB", "jnxJsChHASwitchoverInfoCurrentState"),
        ("JUNIPER-CHASSIS-HIGH-AVAILABILITY-MIB", "jnxJsChHASwitchoverInfoReason"))
)
if mibBuilder.loadTexts:
    jnxJsChHASwitchover.setStatus(
        "current"
    )

jnxJsChHAPeerLinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 19, 1, 0, 2)
)
jnxJsChHAPeerLinkTrap.setObjects(
      *(("JUNIPER-CHASSIS-HIGH-AVAILABILITY-MIB", "jnxJsChHAPeerLinkTrapName"),
        ("JUNIPER-CHASSIS-HIGH-AVAILABILITY-MIB", "jnxJsChHAPeerLinkTrapState"),
        ("JUNIPER-CHASSIS-HIGH-AVAILABILITY-MIB", "jnxJsChHAPeerLinkTrapSeverity"),
        ("JUNIPER-CHASSIS-HIGH-AVAILABILITY-MIB", "jnxJsChHAPeerLinkTrapStateReason"))
)
if mibBuilder.loadTexts:
    jnxJsChHAPeerLinkTrap.setStatus(
        "current"
    )

jnxJsChHANodeHealthStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 19, 1, 0, 3)
)
jnxJsChHANodeHealthStatus.setObjects(
      *(("JUNIPER-CHASSIS-HIGH-AVAILABILITY-MIB", "jnxJsChHANodeHealthStatusNodeID"),
        ("JUNIPER-CHASSIS-HIGH-AVAILABILITY-MIB", "jnxJsChHANodeHealthStatusSeverity"),
        ("JUNIPER-CHASSIS-HIGH-AVAILABILITY-MIB", "jnxJsChHANodeHealthStatusReason"))
)
if mibBuilder.loadTexts:
    jnxJsChHANodeHealthStatus.setStatus(
        "current"
    )

jnxJsChHAPeerBfdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 19, 1, 0, 4)
)
jnxJsChHAPeerBfdTrap.setObjects(
      *(("JUNIPER-CHASSIS-HIGH-AVAILABILITY-MIB", "jnxJsChHAPeerID"),
        ("JUNIPER-CHASSIS-HIGH-AVAILABILITY-MIB", "jnxJsChHAPeerBfdSeverity"),
        ("JUNIPER-CHASSIS-HIGH-AVAILABILITY-MIB", "jnxJsChHAPeerBfdReason"))
)
if mibBuilder.loadTexts:
    jnxJsChHAPeerBfdTrap.setStatus(
        "current"
    )

jnxJsChHASrgHealthStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 19, 1, 0, 5)
)
jnxJsChHASrgHealthStatus.setObjects(
      *(("JUNIPER-CHASSIS-HIGH-AVAILABILITY-MIB", "jnxJsChHASrgHealthStatusNodeID"),
        ("JUNIPER-CHASSIS-HIGH-AVAILABILITY-MIB", "jnxJsChHASrgHealthStatusServicesRedundancyGroup"),
        ("JUNIPER-CHASSIS-HIGH-AVAILABILITY-MIB", "jnxJsChHASrgHealthStatusReason"))
)
if mibBuilder.loadTexts:
    jnxJsChHASrgHealthStatus.setStatus(
        "current"
    )

jnxJsChHASrgActEnfFlrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 19, 1, 0, 6)
)
jnxJsChHASrgActEnfFlrTrap.setObjects(
      *(("JUNIPER-CHASSIS-HIGH-AVAILABILITY-MIB", "jnxJsChHASrgActEnfFlrTrapSrgID"),
        ("JUNIPER-CHASSIS-HIGH-AVAILABILITY-MIB", "jnxJsChHASrgActEnfFlrTrapNodeID"),
        ("JUNIPER-CHASSIS-HIGH-AVAILABILITY-MIB", "jnxJsChHASrgActEnfFlrTrapCurrentState"))
)
if mibBuilder.loadTexts:
    jnxJsChHASrgActEnfFlrTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-CHASSIS-HIGH-AVAILABILITY-MIB",
    **{"jnxJsChassisHAMIB": jnxJsChassisHAMIB,
       "jnxJsChassisHANotifications": jnxJsChassisHANotifications,
       "jnxJsChHASwitchover": jnxJsChHASwitchover,
       "jnxJsChHAPeerLinkTrap": jnxJsChHAPeerLinkTrap,
       "jnxJsChHANodeHealthStatus": jnxJsChHANodeHealthStatus,
       "jnxJsChHAPeerBfdTrap": jnxJsChHAPeerBfdTrap,
       "jnxJsChHASrgHealthStatus": jnxJsChHASrgHealthStatus,
       "jnxJsChHASrgActEnfFlrTrap": jnxJsChHASrgActEnfFlrTrap,
       "jnxJsChassisHATrapObjects": jnxJsChassisHATrapObjects,
       "jnxJsChHASwitchoverInfoServicesRedundancyGroup": jnxJsChHASwitchoverInfoServicesRedundancyGroup,
       "jnxJsChHASwitchoverInfoNodeId": jnxJsChHASwitchoverInfoNodeId,
       "jnxJsChHASwitchoverInfoPreviousState": jnxJsChHASwitchoverInfoPreviousState,
       "jnxJsChHASwitchoverInfoCurrentState": jnxJsChHASwitchoverInfoCurrentState,
       "jnxJsChHASwitchoverInfoReason": jnxJsChHASwitchoverInfoReason,
       "jnxJsChHAPeerLinkTrapName": jnxJsChHAPeerLinkTrapName,
       "jnxJsChHAPeerLinkTrapState": jnxJsChHAPeerLinkTrapState,
       "jnxJsChHAPeerLinkTrapSeverity": jnxJsChHAPeerLinkTrapSeverity,
       "jnxJsChHAPeerLinkTrapStateReason": jnxJsChHAPeerLinkTrapStateReason,
       "jnxJsChHANodeHealthStatusNodeID": jnxJsChHANodeHealthStatusNodeID,
       "jnxJsChHANodeHealthStatusSeverity": jnxJsChHANodeHealthStatusSeverity,
       "jnxJsChHANodeHealthStatusReason": jnxJsChHANodeHealthStatusReason,
       "jnxJsChHAPeerID": jnxJsChHAPeerID,
       "jnxJsChHAPeerBfdSeverity": jnxJsChHAPeerBfdSeverity,
       "jnxJsChHAPeerBfdReason": jnxJsChHAPeerBfdReason,
       "jnxJsChHASrgHealthStatusNodeID": jnxJsChHASrgHealthStatusNodeID,
       "jnxJsChHASrgHealthStatusServicesRedundancyGroup": jnxJsChHASrgHealthStatusServicesRedundancyGroup,
       "jnxJsChHASrgHealthStatusReason": jnxJsChHASrgHealthStatusReason,
       "jnxJsChHASrgActEnfFlrTrapSrgID": jnxJsChHASrgActEnfFlrTrapSrgID,
       "jnxJsChHASrgActEnfFlrTrapNodeID": jnxJsChHASrgActEnfFlrTrapNodeID,
       "jnxJsChHASrgActEnfFlrTrapCurrentState": jnxJsChHASrgActEnfFlrTrapCurrentState}
)
