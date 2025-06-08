# SNMP MIB module (CEM-CN1000-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_6352/CEM-CN1000-COMMON-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:49:20 2025
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

(cnCN1000Temperature,) = mibBuilder.importSymbols(
    "CEM-CN1000",
    "cnCN1000Temperature")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(ifIndex,
 ifOperStatus) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifOperStatus")

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
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "snmpModules")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

cnCN1000TemperatureModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cnCN1000TemperatureModule.setRevisions(
        ("2002-06-03 10:08",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CnCETemperatureRange(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 120),
    )



# MIB Managed Objects in the order of their OIDs

_CnCECommonTemperature_ObjectIdentity = ObjectIdentity
cnCECommonTemperature = _CnCECommonTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 6, 1, 2)
)
_CnCECommonTemperatureObjects_ObjectIdentity = ObjectIdentity
cnCECommonTemperatureObjects = _CnCECommonTemperatureObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 6, 1, 2, 1)
)


class _CnCEPollingConfig_Type(Integer32):
    """Custom type cnCEPollingConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_CnCEPollingConfig_Type.__name__ = "Integer32"
_CnCEPollingConfig_Object = MibScalar
cnCEPollingConfig = _CnCEPollingConfig_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 6, 1, 2, 1, 1),
    _CnCEPollingConfig_Type()
)
cnCEPollingConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnCEPollingConfig.setStatus("current")


class _CnCEHighTemperatureThreshold_Type(CnCETemperatureRange):
    """Custom type cnCEHighTemperatureThreshold based on CnCETemperatureRange"""
    defaultValue = 75


_CnCEHighTemperatureThreshold_Type.__name__ = "CnCETemperatureRange"
_CnCEHighTemperatureThreshold_Object = MibScalar
cnCEHighTemperatureThreshold = _CnCEHighTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 6, 1, 2, 1, 2),
    _CnCEHighTemperatureThreshold_Type()
)
cnCEHighTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnCEHighTemperatureThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cnCEHighTemperatureThreshold.setUnits("Degrees Celsius")
_CnCECurrentTemperature_Type = CnCETemperatureRange
_CnCECurrentTemperature_Object = MibScalar
cnCECurrentTemperature = _CnCECurrentTemperature_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 6, 1, 2, 1, 3),
    _CnCECurrentTemperature_Type()
)
cnCECurrentTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCECurrentTemperature.setStatus("current")
if mibBuilder.loadTexts:
    cnCECurrentTemperature.setUnits("Degrees Celsius")
_CnCECommonTemperatureNotifications_ObjectIdentity = ObjectIdentity
cnCECommonTemperatureNotifications = _CnCECommonTemperatureNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 6, 1, 2, 2)
)
_CnCECommonTemperatureGroups_ObjectIdentity = ObjectIdentity
cnCECommonTemperatureGroups = _CnCECommonTemperatureGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 6, 1, 2, 3)
)

# Managed Objects groups

cnCECommonTemperatureObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 6, 1, 2, 3, 1)
)
cnCECommonTemperatureObjectGroup.setObjects(
      *(("CEM-CN1000-COMMON-MIB", "cnCECurrentTemperature"),
        ("CEM-CN1000-COMMON-MIB", "cnCEPollingConfig"),
        ("CEM-CN1000-COMMON-MIB", "cnCEHighTemperatureThreshold"))
)
if mibBuilder.loadTexts:
    cnCECommonTemperatureObjectGroup.setStatus("current")


# Notification objects

cnCEHighTemperatureThresholdExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 6, 1, 2, 2, 1)
)
cnCEHighTemperatureThresholdExceededCleared.setObjects(
      *(("CEM-CN1000-COMMON-MIB", "cnCECurrentTemperature"),
        ("CEM-CN1000-COMMON-MIB", "cnCEHighTemperatureThreshold"))
)
if mibBuilder.loadTexts:
    cnCEHighTemperatureThresholdExceededCleared.setStatus(
        "current"
    )

cnCEHighTemperatureThresholdExceededRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 6, 1, 2, 2, 2)
)
cnCEHighTemperatureThresholdExceededRaised.setObjects(
      *(("CEM-CN1000-COMMON-MIB", "cnCECurrentTemperature"),
        ("CEM-CN1000-COMMON-MIB", "cnCEHighTemperatureThreshold"))
)
if mibBuilder.loadTexts:
    cnCEHighTemperatureThresholdExceededRaised.setStatus(
        "current"
    )


# Notifications groups

cnCECommonTemperatureNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 6, 1, 2, 3, 2)
)
cnCECommonTemperatureNotificationGroup.setObjects(
      *(("CEM-CN1000-COMMON-MIB", "cnCEHighTemperatureThresholdExceededRaised"),
        ("CEM-CN1000-COMMON-MIB", "cnCEHighTemperatureThresholdExceededCleared"))
)
if mibBuilder.loadTexts:
    cnCECommonTemperatureNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CEM-CN1000-COMMON-MIB",
    **{"CnCETemperatureRange": CnCETemperatureRange,
       "cnCN1000TemperatureModule": cnCN1000TemperatureModule,
       "cnCECommonTemperature": cnCECommonTemperature,
       "cnCECommonTemperatureObjects": cnCECommonTemperatureObjects,
       "cnCEPollingConfig": cnCEPollingConfig,
       "cnCEHighTemperatureThreshold": cnCEHighTemperatureThreshold,
       "cnCECurrentTemperature": cnCECurrentTemperature,
       "cnCECommonTemperatureNotifications": cnCECommonTemperatureNotifications,
       "cnCEHighTemperatureThresholdExceededCleared": cnCEHighTemperatureThresholdExceededCleared,
       "cnCEHighTemperatureThresholdExceededRaised": cnCEHighTemperatureThresholdExceededRaised,
       "cnCECommonTemperatureGroups": cnCECommonTemperatureGroups,
       "cnCECommonTemperatureObjectGroup": cnCECommonTemperatureObjectGroup,
       "cnCECommonTemperatureNotificationGroup": cnCECommonTemperatureNotificationGroup}
)
