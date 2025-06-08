# SNMP MIB module (CIENA-CES-RSTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_1271/CIENA-CES-RSTP-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:39:47 2025
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

(dot1dStpPort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dStpPort")

(cienaCesPortPgIdMappingNotifChassisIndex,
 cienaCesPortPgIdMappingNotifPortNumber,
 cienaCesPortPgIdMappingNotifShelfIndex,
 cienaCesPortPgIdMappingNotifSlotIndex) = mibBuilder.importSymbols(
    "CIENA-CES-PORT-MIB",
    "cienaCesPortPgIdMappingNotifChassisIndex",
    "cienaCesPortPgIdMappingNotifPortNumber",
    "cienaCesPortPgIdMappingNotifShelfIndex",
    "cienaCesPortPgIdMappingNotifSlotIndex")

(cienaGlobalMacAddress,
 cienaGlobalSeverity) = mibBuilder.importSymbols(
    "CIENA-GLOBAL-MIB",
    "cienaGlobalMacAddress",
    "cienaGlobalSeverity")

(cienaCesConfig,
 cienaCesNotifications) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesConfig",
    "cienaCesNotifications")

(dot1dStpPortOperEdgePort,) = mibBuilder.importSymbols(
    "RSTP-MIB",
    "dot1dStpPortOperEdgePort")

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

cienaCesRstpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 10)
)
if mibBuilder.loadTexts:
    cienaCesRstpMIB.setRevisions(
        ("2010-03-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CienaCesRstpMIBConformance_ObjectIdentity = ObjectIdentity
cienaCesRstpMIBConformance = _CienaCesRstpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 10, 2)
)
_CienaCesRstpMIBCompliances_ObjectIdentity = ObjectIdentity
cienaCesRstpMIBCompliances = _CienaCesRstpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 10, 2, 1)
)
_CienaCesRstpMIBGroups_ObjectIdentity = ObjectIdentity
cienaCesRstpMIBGroups = _CienaCesRstpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 10, 2, 2)
)
_CienaCesRstpMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cienaCesRstpMIBNotificationPrefix = _CienaCesRstpMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 10)
)
_CienaCesRstpMIBNotifications_ObjectIdentity = ObjectIdentity
cienaCesRstpMIBNotifications = _CienaCesRstpMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 10, 0)
)

# Managed Objects groups


# Notification objects

cienaCesRstpPortBackupNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 10, 0, 1)
)
cienaCesRstpPortBackupNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifChassisIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifShelfIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifSlotIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifPortNumber"),
        ("BRIDGE-MIB", "dot1dStpPort"))
)
if mibBuilder.loadTexts:
    cienaCesRstpPortBackupNotification.setStatus(
        "current"
    )

cienaCesRstpPvstBpduReceivedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 10, 0, 2)
)
cienaCesRstpPvstBpduReceivedNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifChassisIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifShelfIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifSlotIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifPortNumber"),
        ("BRIDGE-MIB", "dot1dStpPort"))
)
if mibBuilder.loadTexts:
    cienaCesRstpPvstBpduReceivedNotification.setStatus(
        "current"
    )

cienaCesRstpSelfLoopNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 10, 0, 3)
)
cienaCesRstpSelfLoopNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifChassisIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifShelfIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifSlotIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifPortNumber"),
        ("BRIDGE-MIB", "dot1dStpPort"))
)
if mibBuilder.loadTexts:
    cienaCesRstpSelfLoopNotification.setStatus(
        "current"
    )

cienaCesRstpPortOperEdgeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 10, 0, 4)
)
cienaCesRstpPortOperEdgeNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifChassisIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifShelfIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifSlotIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifPortNumber"),
        ("BRIDGE-MIB", "dot1dStpPort"),
        ("RSTP-MIB", "dot1dStpPortOperEdgePort"))
)
if mibBuilder.loadTexts:
    cienaCesRstpPortOperEdgeNotification.setStatus(
        "current"
    )

cienaCesRstpPortFlapNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 10, 0, 5)
)
cienaCesRstpPortFlapNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifChassisIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifShelfIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifSlotIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifPortNumber"),
        ("BRIDGE-MIB", "dot1dStpPort"))
)
if mibBuilder.loadTexts:
    cienaCesRstpPortFlapNotification.setStatus(
        "current"
    )

cienaCesRstpBridgeRootPortLostNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 10, 0, 6)
)
cienaCesRstpBridgeRootPortLostNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifChassisIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifShelfIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifSlotIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifPortNumber"),
        ("BRIDGE-MIB", "dot1dStpPort"))
)
if mibBuilder.loadTexts:
    cienaCesRstpBridgeRootPortLostNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-RSTP-MIB",
    **{"cienaCesRstpMIB": cienaCesRstpMIB,
       "cienaCesRstpMIBConformance": cienaCesRstpMIBConformance,
       "cienaCesRstpMIBCompliances": cienaCesRstpMIBCompliances,
       "cienaCesRstpMIBGroups": cienaCesRstpMIBGroups,
       "cienaCesRstpMIBNotificationPrefix": cienaCesRstpMIBNotificationPrefix,
       "cienaCesRstpMIBNotifications": cienaCesRstpMIBNotifications,
       "cienaCesRstpPortBackupNotification": cienaCesRstpPortBackupNotification,
       "cienaCesRstpPvstBpduReceivedNotification": cienaCesRstpPvstBpduReceivedNotification,
       "cienaCesRstpSelfLoopNotification": cienaCesRstpSelfLoopNotification,
       "cienaCesRstpPortOperEdgeNotification": cienaCesRstpPortOperEdgeNotification,
       "cienaCesRstpPortFlapNotification": cienaCesRstpPortFlapNotification,
       "cienaCesRstpBridgeRootPortLostNotification": cienaCesRstpBridgeRootPortLostNotification}
)
