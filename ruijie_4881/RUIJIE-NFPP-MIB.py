# SNMP MIB module (RUIJIE-NFPP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-NFPP-MIB.mib
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ruijieNFPPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 43)
)
if mibBuilder.loadTexts:
    ruijieNFPPMIB.setRevisions(
        ("2009-07-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieNFPPMIBObjects_ObjectIdentity = ObjectIdentity
ruijieNFPPMIBObjects = _RuijieNFPPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 43, 1)
)


class _RuijieNFPPMessageContent_Type(OctetString):
    """Custom type ruijieNFPPMessageContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_RuijieNFPPMessageContent_Type.__name__ = "OctetString"
_RuijieNFPPMessageContent_Object = MibScalar
ruijieNFPPMessageContent = _RuijieNFPPMessageContent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 43, 1, 0),
    _RuijieNFPPMessageContent_Type()
)
ruijieNFPPMessageContent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieNFPPMessageContent.setStatus("current")
_RuijieNFPPMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ruijieNFPPMIBNotificationPrefix = _RuijieNFPPMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 43, 2)
)
_RuijieNFPPMIBNotifications_ObjectIdentity = ObjectIdentity
ruijieNFPPMIBNotifications = _RuijieNFPPMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 43, 2, 0)
)
_RuijieNFPPMIBConformance_ObjectIdentity = ObjectIdentity
ruijieNFPPMIBConformance = _RuijieNFPPMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 43, 3)
)
_RuijieNFPPMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieNFPPMIBCompliances = _RuijieNFPPMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 43, 3, 1)
)
_RuijieNFPPMIBGroups_ObjectIdentity = ObjectIdentity
ruijieNFPPMIBGroups = _RuijieNFPPMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 43, 3, 2)
)

# Managed Objects groups

ruijieNFPPNotifObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 43, 3, 2, 1)
)
ruijieNFPPNotifObjectsGroup.setObjects(
    ("RUIJIE-NFPP-MIB", "ruijieNFPPMessageContent")
)
if mibBuilder.loadTexts:
    ruijieNFPPNotifObjectsGroup.setStatus("current")


# Notification objects

ruijieNFPPMessageGenerated = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 43, 2, 0, 1)
)
ruijieNFPPMessageGenerated.setObjects(
    ("RUIJIE-NFPP-MIB", "ruijieNFPPMessageContent")
)
if mibBuilder.loadTexts:
    ruijieNFPPMessageGenerated.setStatus(
        "current"
    )


# Notifications groups

ruijieNFPPNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 43, 3, 2, 2)
)
ruijieNFPPNotificationsGroup.setObjects(
    ("RUIJIE-NFPP-MIB", "ruijieNFPPMessageGenerated")
)
if mibBuilder.loadTexts:
    ruijieNFPPNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ruijieNFPPMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 43, 3, 1, 1)
)
ruijieNFPPMIBCompliance.setObjects(
      *(("RUIJIE-NFPP-MIB", "ruijieNFPPNotifObjectsGroup"),
        ("RUIJIE-NFPP-MIB", "ruijieNFPPNotificationsGroup"))
)
if mibBuilder.loadTexts:
    ruijieNFPPMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-NFPP-MIB",
    **{"ruijieNFPPMIB": ruijieNFPPMIB,
       "ruijieNFPPMIBObjects": ruijieNFPPMIBObjects,
       "ruijieNFPPMessageContent": ruijieNFPPMessageContent,
       "ruijieNFPPMIBNotificationPrefix": ruijieNFPPMIBNotificationPrefix,
       "ruijieNFPPMIBNotifications": ruijieNFPPMIBNotifications,
       "ruijieNFPPMessageGenerated": ruijieNFPPMessageGenerated,
       "ruijieNFPPMIBConformance": ruijieNFPPMIBConformance,
       "ruijieNFPPMIBCompliances": ruijieNFPPMIBCompliances,
       "ruijieNFPPMIBCompliance": ruijieNFPPMIBCompliance,
       "ruijieNFPPMIBGroups": ruijieNFPPMIBGroups,
       "ruijieNFPPNotifObjectsGroup": ruijieNFPPNotifObjectsGroup,
       "ruijieNFPPNotificationsGroup": ruijieNFPPNotificationsGroup}
)
