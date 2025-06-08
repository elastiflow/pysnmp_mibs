# SNMP MIB module (COSMOS-SDIAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/caf_50072/COSMOS-SDIAG-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:32:19 2025
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

cosmosSdiag = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 50072, 1, 1)
)
if mibBuilder.loadTexts:
    cosmosSdiag.setRevisions(
        ("2018-02-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cafpower_ObjectIdentity = ObjectIdentity
cafpower = _Cafpower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50072)
)
_Cosmos_ObjectIdentity = ObjectIdentity
cosmos = _Cosmos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50072, 1)
)
_CosmosSdiagNotifications_ObjectIdentity = ObjectIdentity
cosmosSdiagNotifications = _CosmosSdiagNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50072, 1, 1, 1)
)
_CosmosSdiagNotificationPrefix_ObjectIdentity = ObjectIdentity
cosmosSdiagNotificationPrefix = _CosmosSdiagNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50072, 1, 1, 1, 1)
)
_CosmosSdiagNotificationObjects_ObjectIdentity = ObjectIdentity
cosmosSdiagNotificationObjects = _CosmosSdiagNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50072, 1, 1, 1, 2)
)
_CosmosSdiagAlarmId_Type = Integer32
_CosmosSdiagAlarmId_Object = MibScalar
cosmosSdiagAlarmId = _CosmosSdiagAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 50072, 1, 1, 1, 2, 1),
    _CosmosSdiagAlarmId_Type()
)
cosmosSdiagAlarmId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cosmosSdiagAlarmId.setStatus("current")


class _CosmosSdiagAlarmStatus_Type(Integer32):
    """Custom type cosmosSdiagAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deactivation", 0),
          ("activation", 1))
    )


_CosmosSdiagAlarmStatus_Type.__name__ = "Integer32"
_CosmosSdiagAlarmStatus_Object = MibScalar
cosmosSdiagAlarmStatus = _CosmosSdiagAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 50072, 1, 1, 1, 2, 2),
    _CosmosSdiagAlarmStatus_Type()
)
cosmosSdiagAlarmStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cosmosSdiagAlarmStatus.setStatus("current")
_CosmosSdiagAlarmTimestamp_Type = Gauge32
_CosmosSdiagAlarmTimestamp_Object = MibScalar
cosmosSdiagAlarmTimestamp = _CosmosSdiagAlarmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 50072, 1, 1, 1, 2, 3),
    _CosmosSdiagAlarmTimestamp_Type()
)
cosmosSdiagAlarmTimestamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cosmosSdiagAlarmTimestamp.setStatus("current")
_CosmosSdiagAlarmDeviceId_Type = OctetString
_CosmosSdiagAlarmDeviceId_Object = MibScalar
cosmosSdiagAlarmDeviceId = _CosmosSdiagAlarmDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 50072, 1, 1, 1, 2, 4),
    _CosmosSdiagAlarmDeviceId_Type()
)
cosmosSdiagAlarmDeviceId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cosmosSdiagAlarmDeviceId.setStatus("current")

# Managed Objects groups

cosmosSdiagObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 50072, 1, 1, 1, 3)
)
cosmosSdiagObjGroup.setObjects(
      *(("COSMOS-SDIAG-MIB", "cosmosSdiagAlarmId"),
        ("COSMOS-SDIAG-MIB", "cosmosSdiagAlarmStatus"),
        ("COSMOS-SDIAG-MIB", "cosmosSdiagAlarmTimestamp"),
        ("COSMOS-SDIAG-MIB", "cosmosSdiagAlarmDeviceId"))
)
if mibBuilder.loadTexts:
    cosmosSdiagObjGroup.setStatus("current")


# Notification objects

cosmosSdiagAlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 50072, 1, 1, 1, 1, 1)
)
cosmosSdiagAlarmNotification.setObjects(
      *(("COSMOS-SDIAG-MIB", "cosmosSdiagAlarmId"),
        ("COSMOS-SDIAG-MIB", "cosmosSdiagAlarmStatus"),
        ("COSMOS-SDIAG-MIB", "cosmosSdiagAlarmTimestamp"),
        ("COSMOS-SDIAG-MIB", "cosmosSdiagAlarmDeviceId"))
)
if mibBuilder.loadTexts:
    cosmosSdiagAlarmNotification.setStatus(
        "current"
    )


# Notifications groups

cosmosSdiagNotGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 50072, 1, 1, 1, 4)
)
cosmosSdiagNotGroup.setObjects(
    ("COSMOS-SDIAG-MIB", "cosmosSdiagAlarmNotification")
)
if mibBuilder.loadTexts:
    cosmosSdiagNotGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COSMOS-SDIAG-MIB",
    **{"cafpower": cafpower,
       "cosmos": cosmos,
       "cosmosSdiag": cosmosSdiag,
       "cosmosSdiagNotifications": cosmosSdiagNotifications,
       "cosmosSdiagNotificationPrefix": cosmosSdiagNotificationPrefix,
       "cosmosSdiagAlarmNotification": cosmosSdiagAlarmNotification,
       "cosmosSdiagNotificationObjects": cosmosSdiagNotificationObjects,
       "cosmosSdiagAlarmId": cosmosSdiagAlarmId,
       "cosmosSdiagAlarmStatus": cosmosSdiagAlarmStatus,
       "cosmosSdiagAlarmTimestamp": cosmosSdiagAlarmTimestamp,
       "cosmosSdiagAlarmDeviceId": cosmosSdiagAlarmDeviceId,
       "cosmosSdiagObjGroup": cosmosSdiagObjGroup,
       "cosmosSdiagNotGroup": cosmosSdiagNotGroup}
)
