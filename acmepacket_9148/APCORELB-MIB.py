# SNMP MIB module (APCORELB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/acmepacket_9148/APCORELB-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 15:10:25 2025
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

(acmepacketMgmt,) = mibBuilder.importSymbols(
    "ACMEPACKET-SMI",
    "acmepacketMgmt")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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

apCORELBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 19)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApCORELBMIBObjects_ObjectIdentity = ObjectIdentity
apCORELBMIBObjects = _ApCORELBMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 19, 1)
)
_ApCORELBMIBGeneralObjects_ObjectIdentity = ObjectIdentity
apCORELBMIBGeneralObjects = _ApCORELBMIBGeneralObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 19, 1, 1)
)
_ApCoreLBMemberAddress_Type = InetAddress
_ApCoreLBMemberAddress_Object = MibScalar
apCoreLBMemberAddress = _ApCoreLBMemberAddress_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 19, 1, 1, 1),
    _ApCoreLBMemberAddress_Type()
)
apCoreLBMemberAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCoreLBMemberAddress.setStatus("current")
_ApCoreLBMemberAddressType_Type = InetAddressType
_ApCoreLBMemberAddressType_Object = MibScalar
apCoreLBMemberAddressType = _ApCoreLBMemberAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 19, 1, 1, 2),
    _ApCoreLBMemberAddressType_Type()
)
apCoreLBMemberAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCoreLBMemberAddressType.setStatus("current")
_ApCoreLBMemberPort_Type = InetPortNumber
_ApCoreLBMemberPort_Object = MibScalar
apCoreLBMemberPort = _ApCoreLBMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 19, 1, 1, 3),
    _ApCoreLBMemberPort_Type()
)
apCoreLBMemberPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apCoreLBMemberPort.setStatus("current")


class _ApCoreLBMemberId_Type(DisplayString):
    """Custom type apCoreLBMemberId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApCoreLBMemberId_Type.__name__ = "DisplayString"
_ApCoreLBMemberId_Object = MibScalar
apCoreLBMemberId = _ApCoreLBMemberId_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 19, 1, 1, 4),
    _ApCoreLBMemberId_Type()
)
apCoreLBMemberId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apCoreLBMemberId.setStatus("current")


class _ApCoreLBReasonCode_Type(Integer32):
    """Custom type apCoreLBReasonCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("service-assoc-terminated", 0),
          ("service-assoc-timeout", 1),
          ("connection-down", 2))
    )


_ApCoreLBReasonCode_Type.__name__ = "Integer32"
_ApCoreLBReasonCode_Object = MibScalar
apCoreLBReasonCode = _ApCoreLBReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 19, 1, 1, 5),
    _ApCoreLBReasonCode_Type()
)
apCoreLBReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apCoreLBReasonCode.setStatus("current")
_ApCORELBNotificationObjects_ObjectIdentity = ObjectIdentity
apCORELBNotificationObjects = _ApCORELBNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 19, 2)
)
_ApCORELBNotificationPrefix_ObjectIdentity = ObjectIdentity
apCORELBNotificationPrefix = _ApCORELBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 19, 3)
)
_ApCORELBNotifications_ObjectIdentity = ObjectIdentity
apCORELBNotifications = _ApCORELBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 19, 3, 0)
)
_ApCORELBConformance_ObjectIdentity = ObjectIdentity
apCORELBConformance = _ApCORELBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 19, 4)
)
_ApCORELBObjectGroups_ObjectIdentity = ObjectIdentity
apCORELBObjectGroups = _ApCORELBObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 19, 4, 1)
)
_ApCORELBNotificationGroups_ObjectIdentity = ObjectIdentity
apCORELBNotificationGroups = _ApCORELBNotificationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 19, 4, 2)
)

# Managed Objects groups


# Notification objects

apCoreLBMemberInServiceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 19, 3, 0, 1)
)
apCoreLBMemberInServiceTrap.setObjects(
      *(("APCORELB-MIB", "apCoreLBMemberAddressType"),
        ("APCORELB-MIB", "apCoreLBMemberAddress"),
        ("APCORELB-MIB", "apCoreLBMemberPort"),
        ("APCORELB-MIB", "apCoreLBMemberId"))
)
if mibBuilder.loadTexts:
    apCoreLBMemberInServiceTrap.setStatus(
        "current"
    )

apCoreLBMemberOOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 19, 3, 0, 2)
)
apCoreLBMemberOOSTrap.setObjects(
      *(("APCORELB-MIB", "apCoreLBMemberAddressType"),
        ("APCORELB-MIB", "apCoreLBMemberAddress"),
        ("APCORELB-MIB", "apCoreLBMemberPort"),
        ("APCORELB-MIB", "apCoreLBMemberId"),
        ("APCORELB-MIB", "apCoreLBReasonCode"))
)
if mibBuilder.loadTexts:
    apCoreLBMemberOOSTrap.setStatus(
        "current"
    )


# Notifications groups

apCoreLBMemberStatusNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 19, 4, 2, 1)
)
apCoreLBMemberStatusNotificationsGroup.setObjects(
      *(("APCORELB-MIB", "apCoreLBMemberInServiceTrap"),
        ("APCORELB-MIB", "apCoreLBMemberOOSTrap"))
)
if mibBuilder.loadTexts:
    apCoreLBMemberStatusNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APCORELB-MIB",
    **{"apCORELBModule": apCORELBModule,
       "apCORELBMIBObjects": apCORELBMIBObjects,
       "apCORELBMIBGeneralObjects": apCORELBMIBGeneralObjects,
       "apCoreLBMemberAddress": apCoreLBMemberAddress,
       "apCoreLBMemberAddressType": apCoreLBMemberAddressType,
       "apCoreLBMemberPort": apCoreLBMemberPort,
       "apCoreLBMemberId": apCoreLBMemberId,
       "apCoreLBReasonCode": apCoreLBReasonCode,
       "apCORELBNotificationObjects": apCORELBNotificationObjects,
       "apCORELBNotificationPrefix": apCORELBNotificationPrefix,
       "apCORELBNotifications": apCORELBNotifications,
       "apCoreLBMemberInServiceTrap": apCoreLBMemberInServiceTrap,
       "apCoreLBMemberOOSTrap": apCoreLBMemberOOSTrap,
       "apCORELBConformance": apCORELBConformance,
       "apCORELBObjectGroups": apCORELBObjectGroups,
       "apCORELBNotificationGroups": apCORELBNotificationGroups,
       "apCoreLBMemberStatusNotificationsGroup": apCoreLBMemberStatusNotificationsGroup}
)
