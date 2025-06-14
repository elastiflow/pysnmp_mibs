# SNMP MIB module (CISCO-ACCESS-ENVMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-ACCESS-ENVMON-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 20:28:31 2025
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

(ciscoEnvMonSupplyStatusEntry,
 ciscoEnvMonTemperatureState,
 ciscoEnvMonTemperatureStatusDescr,
 ciscoEnvMonVoltageState,
 ciscoEnvMonVoltageStatusDescr) = mibBuilder.importSymbols(
    "CISCO-ENVMON-MIB",
    "ciscoEnvMonSupplyStatusEntry",
    "ciscoEnvMonTemperatureState",
    "ciscoEnvMonTemperatureStatusDescr",
    "ciscoEnvMonVoltageState",
    "ciscoEnvMonVoltageStatusDescr")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ciscoAccessEnvMonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 61)
)
if mibBuilder.loadTexts:
    ciscoAccessEnvMonMIB.setRevisions(
        ("1998-08-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CaemObjects_ObjectIdentity = ObjectIdentity
caemObjects = _CaemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 61, 1)
)
_CaemSupplyStatusTable_Object = MibTable
caemSupplyStatusTable = _CaemSupplyStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 61, 1, 1)
)
if mibBuilder.loadTexts:
    caemSupplyStatusTable.setStatus("current")
_CaemSupplyStatusEntry_Object = MibTableRow
caemSupplyStatusEntry = _CaemSupplyStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 61, 1, 1, 1)
)
if mibBuilder.loadTexts:
    caemSupplyStatusEntry.setStatus("current")


class _CaemSupplyFailedComponent_Type(Integer32):
    """Custom type caemSupplyFailedComponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("inputVoltage", 2),
          ("dcOutputVoltage", 3),
          ("thermal", 4),
          ("multiple", 5),
          ("fan", 6),
          ("overvoltage", 7))
    )


_CaemSupplyFailedComponent_Type.__name__ = "Integer32"
_CaemSupplyFailedComponent_Object = MibTableColumn
caemSupplyFailedComponent = _CaemSupplyFailedComponent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 61, 1, 1, 1, 1),
    _CaemSupplyFailedComponent_Type()
)
caemSupplyFailedComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caemSupplyFailedComponent.setStatus("current")
_CaemMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
caemMIBNotificationPrefix = _CaemMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 61, 2)
)
_CaemMIBNotifications_ObjectIdentity = ObjectIdentity
caemMIBNotifications = _CaemMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 61, 2, 0)
)
_CaemConformance_ObjectIdentity = ObjectIdentity
caemConformance = _CaemConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 61, 3)
)
_CaemCompliances_ObjectIdentity = ObjectIdentity
caemCompliances = _CaemCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 61, 3, 1)
)
_CaemGroups_ObjectIdentity = ObjectIdentity
caemGroups = _CaemGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 61, 3, 2)
)
ciscoEnvMonSupplyStatusEntry.registerAugmentions(
    ("CISCO-ACCESS-ENVMON-MIB",
     "caemSupplyStatusEntry")
)
caemSupplyStatusEntry.setIndexNames(*ciscoEnvMonSupplyStatusEntry.getIndexNames())

# Managed Objects groups

caemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 61, 3, 2, 1)
)
caemGroup.setObjects(
    ("CISCO-ACCESS-ENVMON-MIB", "caemSupplyFailedComponent")
)
if mibBuilder.loadTexts:
    caemGroup.setStatus("current")


# Notification objects

caemTemperatureNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 61, 2, 0, 1)
)
caemTemperatureNotification.setObjects(
      *(("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureStatusDescr"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureState"))
)
if mibBuilder.loadTexts:
    caemTemperatureNotification.setStatus(
        "current"
    )

caemVoltageNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 61, 2, 0, 2)
)
caemVoltageNotification.setObjects(
      *(("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageStatusDescr"),
        ("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageState"))
)
if mibBuilder.loadTexts:
    caemVoltageNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

caemCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 61, 3, 1, 1)
)
caemCompliance.setObjects(
    ("CISCO-ACCESS-ENVMON-MIB", "caemGroup")
)
if mibBuilder.loadTexts:
    caemCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ACCESS-ENVMON-MIB",
    **{"ciscoAccessEnvMonMIB": ciscoAccessEnvMonMIB,
       "caemObjects": caemObjects,
       "caemSupplyStatusTable": caemSupplyStatusTable,
       "caemSupplyStatusEntry": caemSupplyStatusEntry,
       "caemSupplyFailedComponent": caemSupplyFailedComponent,
       "caemMIBNotificationPrefix": caemMIBNotificationPrefix,
       "caemMIBNotifications": caemMIBNotifications,
       "caemTemperatureNotification": caemTemperatureNotification,
       "caemVoltageNotification": caemVoltageNotification,
       "caemConformance": caemConformance,
       "caemCompliances": caemCompliances,
       "caemCompliance": caemCompliance,
       "caemGroups": caemGroups,
       "caemGroup": caemGroup}
)
