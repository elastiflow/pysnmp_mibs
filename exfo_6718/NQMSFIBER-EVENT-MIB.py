# SNMP MIB module (NQMSFIBER-EVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/exfo_6718/NQMSFIBER-EVENT-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 22:54:13 2025
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

(exfoModules,) = mibBuilder.importSymbols(
    "EXFO-SMI-REG",
    "exfoModules")

(nqmsFiber,) = mibBuilder.importSymbols(
    "NQMSFIBER-MIB",
    "nqmsFiber")

(defaultHelixFactorValue,
 defaultIORValue,
 faultDescription,
 faultDistanceEstimated,
 faultDistanceMax,
 faultDistanceMin,
 faultDistanceToRS,
 faultIdentifier,
 faultType,
 freeDiskSpace,
 level,
 messageIdentifier,
 opticalRouteGISReference,
 opticalRouteNumber,
 remoteSwitchNumber,
 remoteSwitchPort,
 rtuName,
 rtuOpticalSwitchPort,
 systemUptime) = mibBuilder.importSymbols(
    "NQMSFIBER-VARIABLES-MIB",
    "defaultHelixFactorValue",
    "defaultIORValue",
    "faultDescription",
    "faultDistanceEstimated",
    "faultDistanceMax",
    "faultDistanceMin",
    "faultDistanceToRS",
    "faultIdentifier",
    "faultType",
    "freeDiskSpace",
    "level",
    "messageIdentifier",
    "opticalRouteGISReference",
    "opticalRouteNumber",
    "remoteSwitchNumber",
    "remoteSwitchPort",
    "rtuName",
    "rtuOpticalSwitchPort",
    "systemUptime")

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

nqmsFiberEvents = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 1, 1, 32)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NqmsFiberEventTypes_ObjectIdentity = ObjectIdentity
nqmsFiberEventTypes = _NqmsFiberEventTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 2)
)
if mibBuilder.loadTexts:
    nqmsFiberEventTypes.setStatus("current")

# Managed Objects groups


# Notification objects

measurementTypeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 2, 1)
)
measurementTypeAlarm.setObjects(
      *(("NQMSFIBER-VARIABLES-MIB", "messageIdentifier"),
        ("NQMSFIBER-VARIABLES-MIB", "faultIdentifier"),
        ("NQMSFIBER-VARIABLES-MIB", "faultDescription"),
        ("NQMSFIBER-VARIABLES-MIB", "faultType"),
        ("NQMSFIBER-VARIABLES-MIB", "level"),
        ("NQMSFIBER-VARIABLES-MIB", "rtuName"),
        ("NQMSFIBER-VARIABLES-MIB", "rtuOpticalSwitchPort"),
        ("NQMSFIBER-VARIABLES-MIB", "faultDistanceEstimated"),
        ("NQMSFIBER-VARIABLES-MIB", "faultDistanceMin"),
        ("NQMSFIBER-VARIABLES-MIB", "faultDistanceMax"),
        ("NQMSFIBER-VARIABLES-MIB", "remoteSwitchNumber"),
        ("NQMSFIBER-VARIABLES-MIB", "remoteSwitchPort"),
        ("NQMSFIBER-VARIABLES-MIB", "faultDistanceToRS"),
        ("NQMSFIBER-VARIABLES-MIB", "opticalRouteNumber"),
        ("NQMSFIBER-VARIABLES-MIB", "opticalRouteGISReference"),
        ("NQMSFIBER-VARIABLES-MIB", "defaultIORValue"),
        ("NQMSFIBER-VARIABLES-MIB", "defaultHelixFactorValue"))
)
if mibBuilder.loadTexts:
    measurementTypeAlarm.setStatus(
        "current"
    )

systemTypeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 2, 2)
)
systemTypeAlarm.setObjects(
      *(("NQMSFIBER-EVENT-MIB", "freeDiskSpaceSystem"),
        ("NQMSFIBER-VARIABLES-MIB", "systemUptime"))
)
if mibBuilder.loadTexts:
    systemTypeAlarm.setStatus(
        "current"
    )

nqmsFiberFaultTypeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 2, 3)
)
nqmsFiberFaultTypeAlarm.setObjects(
      *(("NQMSFIBER-EVENT-MIB", "alertTime"),
        ("NQMSFIBER-EVENT-MIB", "alertType"),
        ("NQMSFIBER-EVENT-MIB", "alertProvider"),
        ("NQMSFIBER-EVENT-MIB", "alertRecipient"),
        ("NQMSFIBER-EVENT-MIB", "alertDeliveryAddress"),
        ("NQMSFIBER-EVENT-MIB", "alarmId"),
        ("NQMSFIBER-EVENT-MIB", "alarmType"),
        ("NQMSFIBER-EVENT-MIB", "alarmTime"),
        ("NQMSFIBER-EVENT-MIB", "alarmSeverity"),
        ("NQMSFIBER-EVENT-MIB", "alarmState"),
        ("NQMSFIBER-EVENT-MIB", "alarmEvent"),
        ("NQMSFIBER-EVENT-MIB", "alarmEventTime"),
        ("NQMSFIBER-VARIABLES-MIB", "faultType"),
        ("NQMSFIBER-EVENT-MIB", "faultStatus"),
        ("NQMSFIBER-EVENT-MIB", "faultConfirmations"),
        ("NQMSFIBER-EVENT-MIB", "faultPositionKM"),
        ("NQMSFIBER-EVENT-MIB", "faultMinimumPositionKM"),
        ("NQMSFIBER-EVENT-MIB", "faultMaximumPositionKm"),
        ("NQMSFIBER-EVENT-MIB", "faultLoss"),
        ("NQMSFIBER-EVENT-MIB", "faultThresholdType"),
        ("NQMSFIBER-EVENT-MIB", "faultThresholdValueDB"),
        ("NQMSFIBER-EVENT-MIB", "faultAppliedThresholdDB"),
        ("NQMSFIBER-EVENT-MIB", "faultEventTime"),
        ("NQMSFIBER-VARIABLES-MIB", "rtuName"),
        ("NQMSFIBER-EVENT-MIB", "rtuSiteName"),
        ("NQMSFIBER-EVENT-MIB", "otdrSerialNumber"),
        ("NQMSFIBER-EVENT-MIB", "othSerialNumber"),
        ("NQMSFIBER-EVENT-MIB", "otauPort"),
        ("NQMSFIBER-EVENT-MIB", "rotauPort"),
        ("NQMSFIBER-EVENT-MIB", "opticalRouteName"),
        ("NQMSFIBER-EVENT-MIB", "cableTemplateName"),
        ("NQMSFIBER-EVENT-MIB", "ospRouteId"),
        ("NQMSFIBER-EVENT-MIB", "externalNMSrouteref1"),
        ("NQMSFIBER-EVENT-MIB", "externalNMSrouteref2"),
        ("NQMSFIBER-EVENT-MIB", "fiberCode"),
        ("NQMSFIBER-EVENT-MIB", "testSetupName"),
        ("NQMSFIBER-EVENT-MIB", "testSetupType"),
        ("NQMSFIBER-EVENT-MIB", "testSetupWavelength"),
        ("NQMSFIBER-EVENT-MIB", "nearestSite"),
        ("NQMSFIBER-EVENT-MIB", "distanceFromNearestSiteKM"),
        ("NQMSFIBER-EVENT-MIB", "affectedClient"),
        ("NQMSFIBER-EVENT-MIB", "assignee"),
        ("NQMSFIBER-EVENT-MIB", "troubleTicketDescription"))
)
if mibBuilder.loadTexts:
    nqmsFiberFaultTypeAlarm.setStatus(
        "current"
    )

nqmsFiberRtuStatusTypeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 2, 4)
)
nqmsFiberRtuStatusTypeAlarm.setObjects(
      *(("NQMSFIBER-VARIABLES-MIB", "rtuName"),
        ("NQMSFIBER-EVENT-MIB", "freeDiskSpaceSystem"),
        ("NQMSFIBER-EVENT-MIB", "sourceDataSet"),
        ("NQMSFIBER-EVENT-MIB", "alarmType"),
        ("NQMSFIBER-EVENT-MIB", "primaryAlarmSource"),
        ("NQMSFIBER-EVENT-MIB", "alarmSeverity"),
        ("NQMSFIBER-EVENT-MIB", "alarmStatus"),
        ("NQMSFIBER-EVENT-MIB", "alarmEvent"),
        ("NQMSFIBER-EVENT-MIB", "alarmEventTime"),
        ("NQMSFIBER-EVENT-MIB", "secondaryAlarmSource"),
        ("NQMSFIBER-EVENT-MIB", "alarmDetails"),
        ("NQMSFIBER-EVENT-MIB", "alertTime"),
        ("NQMSFIBER-EVENT-MIB", "alertRecipient"),
        ("NQMSFIBER-EVENT-MIB", "alertDeliveryAddress"),
        ("NQMSFIBER-EVENT-MIB", "assignee"),
        ("NQMSFIBER-EVENT-MIB", "troubleTicketDescription"))
)
if mibBuilder.loadTexts:
    nqmsFiberRtuStatusTypeAlarm.setStatus(
        "current"
    )

nqmsFiberStatusTypeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 2, 5)
)
nqmsFiberStatusTypeAlarm.setObjects(
      *(("NQMSFIBER-EVENT-MIB", "freeDiskSpaceSystem"),
        ("NQMSFIBER-EVENT-MIB", "sourceDataSet"),
        ("NQMSFIBER-EVENT-MIB", "alarmType"),
        ("NQMSFIBER-EVENT-MIB", "primaryAlarmSource"),
        ("NQMSFIBER-EVENT-MIB", "alarmSeverity"),
        ("NQMSFIBER-EVENT-MIB", "alarmStatus"),
        ("NQMSFIBER-EVENT-MIB", "alarmEvent"),
        ("NQMSFIBER-EVENT-MIB", "alarmEventTime"),
        ("NQMSFIBER-EVENT-MIB", "secondaryAlarmSource"),
        ("NQMSFIBER-EVENT-MIB", "alarmDetails"),
        ("NQMSFIBER-EVENT-MIB", "alertTime"),
        ("NQMSFIBER-EVENT-MIB", "alertRecipient"),
        ("NQMSFIBER-EVENT-MIB", "alertDeliveryAddress"),
        ("NQMSFIBER-EVENT-MIB", "assignee"),
        ("NQMSFIBER-EVENT-MIB", "troubleTicketDescription"))
)
if mibBuilder.loadTexts:
    nqmsFiberStatusTypeAlarm.setStatus(
        "current"
    )

nqmsFiberRtuLogTypeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6718, 3, 2, 2, 6)
)
nqmsFiberRtuLogTypeAlarm.setObjects(
      *(("NQMSFIBER-VARIABLES-MIB", "rtuName"),
        ("NQMSFIBER-EVENT-MIB", "sourceDataSet"),
        ("NQMSFIBER-EVENT-MIB", "alarmType"),
        ("NQMSFIBER-EVENT-MIB", "primaryAlarmSource"),
        ("NQMSFIBER-EVENT-MIB", "alarmSeverity"),
        ("NQMSFIBER-EVENT-MIB", "alarmStatus"),
        ("NQMSFIBER-EVENT-MIB", "alarmEvent"),
        ("NQMSFIBER-EVENT-MIB", "alarmEventTime"),
        ("NQMSFIBER-EVENT-MIB", "secondaryAlarmSource"),
        ("NQMSFIBER-EVENT-MIB", "alarmDetails"),
        ("NQMSFIBER-EVENT-MIB", "alertTime"),
        ("NQMSFIBER-EVENT-MIB", "alertRecipient"),
        ("NQMSFIBER-EVENT-MIB", "alertDeliveryAddress"),
        ("NQMSFIBER-EVENT-MIB", "assignee"),
        ("NQMSFIBER-EVENT-MIB", "troubleTicketDescription"))
)
if mibBuilder.loadTexts:
    nqmsFiberRtuLogTypeAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NQMSFIBER-EVENT-MIB",
    **{"nqmsFiberEvents": nqmsFiberEvents,
       "nqmsFiberEventTypes": nqmsFiberEventTypes,
       "measurementTypeAlarm": measurementTypeAlarm,
       "systemTypeAlarm": systemTypeAlarm,
       "nqmsFiberFaultTypeAlarm": nqmsFiberFaultTypeAlarm,
       "nqmsFiberRtuStatusTypeAlarm": nqmsFiberRtuStatusTypeAlarm,
       "nqmsFiberStatusTypeAlarm": nqmsFiberStatusTypeAlarm,
       "nqmsFiberRtuLogTypeAlarm": nqmsFiberRtuLogTypeAlarm}
)
