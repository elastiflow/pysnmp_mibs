# SNMP MIB module (F5OS-APPLIANCE-ALERT-NOTIF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/f5_12276/F5OS-APPLIANCE-ALERT-NOTIF-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 22:59:23 2025
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

(alertDescription,
 alertEffect,
 alertSeverity,
 alertSource,
 alertTimeStamp,
 f5AlertNotificationGroup,
 f5Alerts) = mibBuilder.importSymbols(
    "F5-ALERT-DEF-MIB",
    "alertDescription",
    "alertEffect",
    "alertSeverity",
    "alertSource",
    "alertTimeStamp",
    "f5AlertNotificationGroup",
    "f5Alerts")

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

f5AlertNotification = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1)
)
if mibBuilder.loadTexts:
    f5AlertNotification.setRevisions(
        ("2019-08-04 09:41",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

hardware_device_fault = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 65536)
)
hardware_device_fault.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    hardware_device_fault.setStatus(
        "current"
    )

firmware_fault = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 65537)
)
firmware_fault.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    firmware_fault.setStatus(
        "current"
    )

unknown_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 65538)
)
unknown_alarm.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    unknown_alarm.setStatus(
        "current"
    )

memory_fault = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 65539)
)
memory_fault.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    memory_fault.setStatus(
        "current"
    )

drive_fault = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 65540)
)
drive_fault.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    drive_fault.setStatus(
        "current"
    )

cpu_fault = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 65541)
)
cpu_fault.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    cpu_fault.setStatus(
        "current"
    )

pcie_fault = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 65542)
)
pcie_fault.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    pcie_fault.setStatus(
        "current"
    )

aom_fault = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 65543)
)
aom_fault.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    aom_fault.setStatus(
        "current"
    )

drive_capacity_fault = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 65544)
)
drive_capacity_fault.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    drive_capacity_fault.setStatus(
        "current"
    )

power_fault = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 65545)
)
power_fault.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    power_fault.setStatus(
        "current"
    )

thermal_fault = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 65546)
)
thermal_fault.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    thermal_fault.setStatus(
        "current"
    )

drive_thermal_throttle = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 65547)
)
drive_thermal_throttle.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    drive_thermal_throttle.setStatus(
        "current"
    )

blade_thermal_fault = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 65548)
)
blade_thermal_fault.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    blade_thermal_fault.setStatus(
        "current"
    )

blade_hardware_fault = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 65549)
)
blade_hardware_fault.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    blade_hardware_fault.setStatus(
        "current"
    )

firmware_update_status = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 65550)
)
firmware_update_status.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    firmware_update_status.setStatus(
        "current"
    )

drive_utilization = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 65551)
)
drive_utilization.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    drive_utilization.setStatus(
        "current"
    )

service_health = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 65552)
)
service_health.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    service_health.setStatus(
        "current"
    )

module_present = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 66304)
)
module_present.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    module_present.setStatus(
        "current"
    )

psu_fault = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 66305)
)
psu_fault.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    psu_fault.setStatus(
        "current"
    )

lcd_fault = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 66306)
)
lcd_fault.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    lcd_fault.setStatus(
        "current"
    )

module_communication_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 66307)
)
module_communication_error.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    module_communication_error.setStatus(
        "current"
    )

fipsError = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 196608)
)
fipsError.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    fipsError.setStatus(
        "current"
    )

backplane = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 262144)
)
backplane.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    backplane.setStatus(
        "current"
    )

txPwrHiAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 262400)
)
txPwrHiAlarm.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    txPwrHiAlarm.setStatus(
        "current"
    )

txPwrHiWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 262401)
)
txPwrHiWarn.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    txPwrHiWarn.setStatus(
        "current"
    )

txPwrLoAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 262402)
)
txPwrLoAlarm.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    txPwrLoAlarm.setStatus(
        "current"
    )

txPwrLoWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 262403)
)
txPwrLoWarn.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    txPwrLoWarn.setStatus(
        "current"
    )

rxPwrHiAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 262404)
)
rxPwrHiAlarm.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    rxPwrHiAlarm.setStatus(
        "current"
    )

rxPwrHiWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 262405)
)
rxPwrHiWarn.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    rxPwrHiWarn.setStatus(
        "current"
    )

rxPwrLoAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 262406)
)
rxPwrLoAlarm.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    rxPwrLoAlarm.setStatus(
        "current"
    )

rxPwrLoWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 262407)
)
rxPwrLoWarn.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    rxPwrLoWarn.setStatus(
        "current"
    )

txBiasHiAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 262408)
)
txBiasHiAlarm.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    txBiasHiAlarm.setStatus(
        "current"
    )

txBiasHiWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 262409)
)
txBiasHiWarn.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    txBiasHiWarn.setStatus(
        "current"
    )

txBiasLoAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 262410)
)
txBiasLoAlarm.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    txBiasLoAlarm.setStatus(
        "current"
    )

txBiasLoWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 262411)
)
txBiasLoWarn.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    txBiasLoWarn.setStatus(
        "current"
    )

ddmTempHiAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 262412)
)
ddmTempHiAlarm.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    ddmTempHiAlarm.setStatus(
        "current"
    )

ddmTempHiWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 262413)
)
ddmTempHiWarn.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    ddmTempHiWarn.setStatus(
        "current"
    )

ddmTempLoAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 262414)
)
ddmTempLoAlarm.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    ddmTempLoAlarm.setStatus(
        "current"
    )

ddmTempLoWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 262415)
)
ddmTempLoWarn.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    ddmTempLoWarn.setStatus(
        "current"
    )

ddmVccHiAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 262416)
)
ddmVccHiAlarm.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    ddmVccHiAlarm.setStatus(
        "current"
    )

ddmVccHiWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 262417)
)
ddmVccHiWarn.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    ddmVccHiWarn.setStatus(
        "current"
    )

ddmVccLoAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 262418)
)
ddmVccLoAlarm.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    ddmVccLoAlarm.setStatus(
        "current"
    )

ddmVccLoWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 262419)
)
ddmVccLoWarn.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    ddmVccLoWarn.setStatus(
        "current"
    )

core_dump = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 327680)
)
core_dump.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    core_dump.setStatus(
        "current"
    )

raidEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 1, 393216)
)
raidEvent.setObjects(
      *(("F5-ALERT-DEF-MIB", "alertSource"),
        ("F5-ALERT-DEF-MIB", "alertEffect"),
        ("F5-ALERT-DEF-MIB", "alertSeverity"),
        ("F5-ALERT-DEF-MIB", "alertTimeStamp"),
        ("F5-ALERT-DEF-MIB", "alertDescription"))
)
if mibBuilder.loadTexts:
    raidEvent.setStatus(
        "current"
    )


# Notifications groups

f5AlertsNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 3, 1)
)
f5AlertsNotifyGroup.setObjects(
      *(("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "hardware-device-fault"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "firmware-fault"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "unknown-alarm"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "memory-fault"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "drive-fault"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "cpu-fault"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "pcie-fault"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "aom-fault"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "drive-capacity-fault"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "power-fault"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "thermal-fault"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "drive-thermal-throttle"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "blade-thermal-fault"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "blade-hardware-fault"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "firmware-update-status"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "drive-utilization"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "service-health"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "module-present"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "psu-fault"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "lcd-fault"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "module-communication-error"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "fipsError"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "core-dump"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "raidEvent"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "backplane"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "txPwrHiAlarm"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "txPwrHiWarn"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "txPwrLoAlarm"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "txPwrLoWarn"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "rxPwrHiAlarm"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "rxPwrHiWarn"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "rxPwrLoAlarm"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "rxPwrLoWarn"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "txBiasHiAlarm"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "txBiasHiWarn"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "txBiasLoAlarm"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "txBiasLoWarn"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "ddmTempHiAlarm"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "ddmTempHiWarn"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "ddmTempLoAlarm"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "ddmTempLoWarn"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "ddmVccHiAlarm"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "ddmVccHiWarn"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "ddmVccLoAlarm"),
        ("F5OS-APPLIANCE-ALERT-NOTIF-MIB", "ddmVccLoWarn"))
)
if mibBuilder.loadTexts:
    f5AlertsNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F5OS-APPLIANCE-ALERT-NOTIF-MIB",
    **{"f5AlertsNotifyGroup": f5AlertsNotifyGroup,
       "f5AlertNotification": f5AlertNotification,
       "hardware-device-fault": hardware_device_fault,
       "firmware-fault": firmware_fault,
       "unknown-alarm": unknown_alarm,
       "memory-fault": memory_fault,
       "drive-fault": drive_fault,
       "cpu-fault": cpu_fault,
       "pcie-fault": pcie_fault,
       "aom-fault": aom_fault,
       "drive-capacity-fault": drive_capacity_fault,
       "power-fault": power_fault,
       "thermal-fault": thermal_fault,
       "drive-thermal-throttle": drive_thermal_throttle,
       "blade-thermal-fault": blade_thermal_fault,
       "blade-hardware-fault": blade_hardware_fault,
       "firmware-update-status": firmware_update_status,
       "drive-utilization": drive_utilization,
       "service-health": service_health,
       "module-present": module_present,
       "psu-fault": psu_fault,
       "lcd-fault": lcd_fault,
       "module-communication-error": module_communication_error,
       "fipsError": fipsError,
       "backplane": backplane,
       "txPwrHiAlarm": txPwrHiAlarm,
       "txPwrHiWarn": txPwrHiWarn,
       "txPwrLoAlarm": txPwrLoAlarm,
       "txPwrLoWarn": txPwrLoWarn,
       "rxPwrHiAlarm": rxPwrHiAlarm,
       "rxPwrHiWarn": rxPwrHiWarn,
       "rxPwrLoAlarm": rxPwrLoAlarm,
       "rxPwrLoWarn": rxPwrLoWarn,
       "txBiasHiAlarm": txBiasHiAlarm,
       "txBiasHiWarn": txBiasHiWarn,
       "txBiasLoAlarm": txBiasLoAlarm,
       "txBiasLoWarn": txBiasLoWarn,
       "ddmTempHiAlarm": ddmTempHiAlarm,
       "ddmTempHiWarn": ddmTempHiWarn,
       "ddmTempLoAlarm": ddmTempLoAlarm,
       "ddmTempLoWarn": ddmTempLoWarn,
       "ddmVccHiAlarm": ddmVccHiAlarm,
       "ddmVccHiWarn": ddmVccHiWarn,
       "ddmVccLoAlarm": ddmVccLoAlarm,
       "ddmVccLoWarn": ddmVccLoWarn,
       "core-dump": core_dump,
       "raidEvent": raidEvent}
)
