# SNMP MIB module (CLAB-UPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cablelabs_4491/CLAB-UPS-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:39:27 2025
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

(clabCommonMibs,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabCommonMibs")

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

(upsAlarmDescr,
 upsAlarmTime,
 upsAlarmsPresent,
 upsAutoRestart,
 upsBatteryStatus,
 upsConfigAudibleStatus,
 upsConfigInputFreq,
 upsConfigInputVoltage,
 upsConfigLowBattTime,
 upsConfigOutputFreq,
 upsConfigOutputPower,
 upsConfigOutputVA,
 upsConfigOutputVoltage,
 upsEstimatedChargeRemaining,
 upsEstimatedMinutesRemaining,
 upsIdentAgentSoftwareVersion,
 upsIdentAttachedDevices,
 upsIdentManufacturer,
 upsIdentModel,
 upsIdentName,
 upsInputFrequency,
 upsInputLineBads,
 upsInputNumLines,
 upsInputVoltage,
 upsOutputFrequency,
 upsOutputNumLines,
 upsOutputSource,
 upsOutputVoltage,
 upsRebootWithDuration,
 upsSecondsOnBattery,
 upsShutdownAfterDelay,
 upsShutdownType,
 upsStartupAfterDelay) = mibBuilder.importSymbols(
    "UPS-MIB",
    "upsAlarmDescr",
    "upsAlarmTime",
    "upsAlarmsPresent",
    "upsAutoRestart",
    "upsBatteryStatus",
    "upsConfigAudibleStatus",
    "upsConfigInputFreq",
    "upsConfigInputVoltage",
    "upsConfigLowBattTime",
    "upsConfigOutputFreq",
    "upsConfigOutputPower",
    "upsConfigOutputVA",
    "upsConfigOutputVoltage",
    "upsEstimatedChargeRemaining",
    "upsEstimatedMinutesRemaining",
    "upsIdentAgentSoftwareVersion",
    "upsIdentAttachedDevices",
    "upsIdentManufacturer",
    "upsIdentModel",
    "upsIdentName",
    "upsInputFrequency",
    "upsInputLineBads",
    "upsInputNumLines",
    "upsInputVoltage",
    "upsOutputFrequency",
    "upsOutputNumLines",
    "upsOutputSource",
    "upsOutputVoltage",
    "upsRebootWithDuration",
    "upsSecondsOnBattery",
    "upsShutdownAfterDelay",
    "upsShutdownType",
    "upsStartupAfterDelay")


# MODULE-IDENTITY

clabUpsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 1)
)
if mibBuilder.loadTexts:
    clabUpsMib.setRevisions(
        ("2010-04-28 00:00",
         "2009-05-06 00:00",
         "2007-01-19 17:00",
         "2005-01-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ClabUpsNotifications_ObjectIdentity = ObjectIdentity
clabUpsNotifications = _ClabUpsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 1, 0)
)
_ClabUpsObjects_ObjectIdentity = ObjectIdentity
clabUpsObjects = _ClabUpsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 1, 1)
)
_ClabUpsConformance_ObjectIdentity = ObjectIdentity
clabUpsConformance = _ClabUpsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 1, 2)
)
_ClabUpsCompliances_ObjectIdentity = ObjectIdentity
clabUpsCompliances = _ClabUpsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 1, 2, 1)
)
_ClabUpsGroups_ObjectIdentity = ObjectIdentity
clabUpsGroups = _ClabUpsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 1, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

clabUpsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 4, 1, 2, 1, 1)
)
clabUpsMibCompliance.setObjects(
      *(("UPS-MIB", "upsSubsetIdentGroup"),
        ("UPS-MIB", "upsFullBatteryGroup"),
        ("UPS-MIB", "upsBasicInputGroup"),
        ("UPS-MIB", "upsBasicOutputGroup"),
        ("UPS-MIB", "upsBasicAlarmGroup"),
        ("UPS-MIB", "upsBasicControlGroup"),
        ("UPS-MIB", "upsBasicConfigGroup"))
)
if mibBuilder.loadTexts:
    clabUpsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CLAB-UPS-MIB",
    **{"clabUpsMib": clabUpsMib,
       "clabUpsNotifications": clabUpsNotifications,
       "clabUpsObjects": clabUpsObjects,
       "clabUpsConformance": clabUpsConformance,
       "clabUpsCompliances": clabUpsCompliances,
       "clabUpsMibCompliance": clabUpsMibCompliance,
       "clabUpsGroups": clabUpsGroups}
)
