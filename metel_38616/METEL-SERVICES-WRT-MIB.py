# SNMP MIB module (METEL-SERVICES-WRT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/metel_38616/METEL-SERVICES-WRT-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:24:38 2025
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

(services,) = mibBuilder.importSymbols(
    "METEL-SERVICES-MIB",
    "services")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

wrt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 38616, 1, 8, 111)
)
if mibBuilder.loadTexts:
    wrt.setRevisions(
        ("2021-11-16 00:00",
         "2021-07-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Config_ObjectIdentity = ObjectIdentity
config = _Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38616, 1, 8, 111, 1)
)
_WrtConfigTable_Object = MibTable
wrtConfigTable = _WrtConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 8, 111, 1, 1)
)
if mibBuilder.loadTexts:
    wrtConfigTable.setStatus("current")
_WrtConfigEntry_Object = MibTableRow
wrtConfigEntry = _WrtConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 8, 111, 1, 1, 1)
)
wrtConfigEntry.setIndexNames(
    (0, "METEL-SERVICES-WRT-MIB", "configSectionName"),
    (0, "METEL-SERVICES-WRT-MIB", "configSectionIdxName"),
    (0, "METEL-SERVICES-WRT-MIB", "configOptionName"),
)
if mibBuilder.loadTexts:
    wrtConfigEntry.setStatus("current")
_ConfigSectionName_Type = DisplayString
_ConfigSectionName_Object = MibTableColumn
configSectionName = _ConfigSectionName_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 8, 111, 1, 1, 1, 1),
    _ConfigSectionName_Type()
)
configSectionName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    configSectionName.setStatus("current")
_ConfigSectionIdxName_Type = DisplayString
_ConfigSectionIdxName_Object = MibTableColumn
configSectionIdxName = _ConfigSectionIdxName_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 8, 111, 1, 1, 1, 2),
    _ConfigSectionIdxName_Type()
)
configSectionIdxName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    configSectionIdxName.setStatus("current")
_ConfigOptionName_Type = DisplayString
_ConfigOptionName_Object = MibTableColumn
configOptionName = _ConfigOptionName_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 8, 111, 1, 1, 1, 3),
    _ConfigOptionName_Type()
)
configOptionName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    configOptionName.setStatus("current")
_ConfigRowStatus_Type = RowStatus
_ConfigRowStatus_Object = MibTableColumn
configRowStatus = _ConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 8, 111, 1, 1, 1, 4),
    _ConfigRowStatus_Type()
)
configRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    configRowStatus.setStatus("current")
_ConfigStartUpValue_Type = DisplayString
_ConfigStartUpValue_Object = MibTableColumn
configStartUpValue = _ConfigStartUpValue_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 8, 111, 1, 1, 1, 5),
    _ConfigStartUpValue_Type()
)
configStartUpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configStartUpValue.setStatus("current")
_ConfigRunningValue_Type = DisplayString
_ConfigRunningValue_Object = MibTableColumn
configRunningValue = _ConfigRunningValue_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 8, 111, 1, 1, 1, 6),
    _ConfigRunningValue_Type()
)
configRunningValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configRunningValue.setStatus("current")
_ConfigDefaultValue_Type = DisplayString
_ConfigDefaultValue_Object = MibTableColumn
configDefaultValue = _ConfigDefaultValue_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 8, 111, 1, 1, 1, 7),
    _ConfigDefaultValue_Type()
)
configDefaultValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configDefaultValue.setStatus("current")
_ConfigNewValue_Type = DisplayString
_ConfigNewValue_Object = MibTableColumn
configNewValue = _ConfigNewValue_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 8, 111, 1, 1, 1, 8),
    _ConfigNewValue_Type()
)
configNewValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configNewValue.setStatus("current")


class _ConfigIsChanged_Type(Integer32):
    """Custom type configIsChanged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", 0),
          ("yes", 1),
          ("no", 2))
    )


_ConfigIsChanged_Type.__name__ = "Integer32"
_ConfigIsChanged_Object = MibTableColumn
configIsChanged = _ConfigIsChanged_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 8, 111, 1, 1, 1, 9),
    _ConfigIsChanged_Type()
)
configIsChanged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIsChanged.setStatus("current")


class _WrtConfigWriteNew2StartUp_Type(Integer32):
    """Custom type wrtConfigWriteNew2StartUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("write", 1)
    )


_WrtConfigWriteNew2StartUp_Type.__name__ = "Integer32"
_WrtConfigWriteNew2StartUp_Object = MibScalar
wrtConfigWriteNew2StartUp = _WrtConfigWriteNew2StartUp_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 8, 111, 1, 2),
    _WrtConfigWriteNew2StartUp_Type()
)
wrtConfigWriteNew2StartUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wrtConfigWriteNew2StartUp.setStatus("current")


class _WrtConfigWriteNew2RunningAsync_Type(Integer32):
    """Custom type wrtConfigWriteNew2RunningAsync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("write", 1)
    )


_WrtConfigWriteNew2RunningAsync_Type.__name__ = "Integer32"
_WrtConfigWriteNew2RunningAsync_Object = MibScalar
wrtConfigWriteNew2RunningAsync = _WrtConfigWriteNew2RunningAsync_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 8, 111, 1, 3),
    _WrtConfigWriteNew2RunningAsync_Type()
)
wrtConfigWriteNew2RunningAsync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wrtConfigWriteNew2RunningAsync.setStatus("current")


class _WrtConfigWriteRunnig2StartUp_Type(Integer32):
    """Custom type wrtConfigWriteRunnig2StartUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("write", 1)
    )


_WrtConfigWriteRunnig2StartUp_Type.__name__ = "Integer32"
_WrtConfigWriteRunnig2StartUp_Object = MibScalar
wrtConfigWriteRunnig2StartUp = _WrtConfigWriteRunnig2StartUp_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 8, 111, 1, 4),
    _WrtConfigWriteRunnig2StartUp_Type()
)
wrtConfigWriteRunnig2StartUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wrtConfigWriteRunnig2StartUp.setStatus("current")


class _WrtConfigWriteStartUp2RunningAsync_Type(Integer32):
    """Custom type wrtConfigWriteStartUp2RunningAsync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("write", 1)
    )


_WrtConfigWriteStartUp2RunningAsync_Type.__name__ = "Integer32"
_WrtConfigWriteStartUp2RunningAsync_Object = MibScalar
wrtConfigWriteStartUp2RunningAsync = _WrtConfigWriteStartUp2RunningAsync_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 8, 111, 1, 5),
    _WrtConfigWriteStartUp2RunningAsync_Type()
)
wrtConfigWriteStartUp2RunningAsync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wrtConfigWriteStartUp2RunningAsync.setStatus("current")


class _WrtConfigWriteDefault2StartUp_Type(Integer32):
    """Custom type wrtConfigWriteDefault2StartUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("write", 1)
    )


_WrtConfigWriteDefault2StartUp_Type.__name__ = "Integer32"
_WrtConfigWriteDefault2StartUp_Object = MibScalar
wrtConfigWriteDefault2StartUp = _WrtConfigWriteDefault2StartUp_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 8, 111, 1, 6),
    _WrtConfigWriteDefault2StartUp_Type()
)
wrtConfigWriteDefault2StartUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wrtConfigWriteDefault2StartUp.setStatus("current")


class _WrtConfigWriteDefault2RunningAsync_Type(Integer32):
    """Custom type wrtConfigWriteDefault2RunningAsync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("write", 1)
    )


_WrtConfigWriteDefault2RunningAsync_Type.__name__ = "Integer32"
_WrtConfigWriteDefault2RunningAsync_Object = MibScalar
wrtConfigWriteDefault2RunningAsync = _WrtConfigWriteDefault2RunningAsync_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 8, 111, 1, 7),
    _WrtConfigWriteDefault2RunningAsync_Type()
)
wrtConfigWriteDefault2RunningAsync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wrtConfigWriteDefault2RunningAsync.setStatus("current")


class _WrtConfigClearNew_Type(Integer32):
    """Custom type wrtConfigClearNew based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("write", 1)
    )


_WrtConfigClearNew_Type.__name__ = "Integer32"
_WrtConfigClearNew_Object = MibScalar
wrtConfigClearNew = _WrtConfigClearNew_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 8, 111, 1, 8),
    _WrtConfigClearNew_Type()
)
wrtConfigClearNew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wrtConfigClearNew.setStatus("current")


class _WrtConfigAsyncProgress_Type(Integer32):
    """Custom type wrtConfigAsyncProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("busy", 1),
          ("done", 2))
    )


_WrtConfigAsyncProgress_Type.__name__ = "Integer32"
_WrtConfigAsyncProgress_Object = MibScalar
wrtConfigAsyncProgress = _WrtConfigAsyncProgress_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 8, 111, 1, 9),
    _WrtConfigAsyncProgress_Type()
)
wrtConfigAsyncProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrtConfigAsyncProgress.setStatus("current")
_Status_ObjectIdentity = ObjectIdentity
status = _Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38616, 1, 8, 111, 2)
)
_WrtStatusTable_Object = MibTable
wrtStatusTable = _WrtStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 8, 111, 2, 1)
)
if mibBuilder.loadTexts:
    wrtStatusTable.setStatus("current")
_WrtStatusEntry_Object = MibTableRow
wrtStatusEntry = _WrtStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 8, 111, 2, 1, 1)
)
wrtStatusEntry.setIndexNames(
    (0, "METEL-SERVICES-WRT-MIB", "statusSectionName"),
    (0, "METEL-SERVICES-WRT-MIB", "statusSectionIdxName"),
    (0, "METEL-SERVICES-WRT-MIB", "statusOptionName"),
)
if mibBuilder.loadTexts:
    wrtStatusEntry.setStatus("current")
_StatusSectionName_Type = DisplayString
_StatusSectionName_Object = MibTableColumn
statusSectionName = _StatusSectionName_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 8, 111, 2, 1, 1, 1),
    _StatusSectionName_Type()
)
statusSectionName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    statusSectionName.setStatus("current")
_StatusSectionIdxName_Type = DisplayString
_StatusSectionIdxName_Object = MibTableColumn
statusSectionIdxName = _StatusSectionIdxName_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 8, 111, 2, 1, 1, 2),
    _StatusSectionIdxName_Type()
)
statusSectionIdxName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    statusSectionIdxName.setStatus("current")
_StatusOptionName_Type = DisplayString
_StatusOptionName_Object = MibTableColumn
statusOptionName = _StatusOptionName_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 8, 111, 2, 1, 1, 3),
    _StatusOptionName_Type()
)
statusOptionName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    statusOptionName.setStatus("current")
_ActualValue_Type = DisplayString
_ActualValue_Object = MibTableColumn
actualValue = _ActualValue_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 8, 111, 2, 1, 1, 4),
    _ActualValue_Type()
)
actualValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actualValue.setStatus("current")
_Validation_ObjectIdentity = ObjectIdentity
validation = _Validation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38616, 1, 8, 111, 3)
)
_WrtValidationTable_Object = MibTable
wrtValidationTable = _WrtValidationTable_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 8, 111, 3, 1)
)
if mibBuilder.loadTexts:
    wrtValidationTable.setStatus("current")
_WrtValidationEntry_Object = MibTableRow
wrtValidationEntry = _WrtValidationEntry_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 8, 111, 3, 1, 1)
)
wrtValidationEntry.setIndexNames(
    (0, "METEL-SERVICES-WRT-MIB", "validationFailId"),
    (0, "METEL-SERVICES-WRT-MIB", "validationSectionName"),
    (0, "METEL-SERVICES-WRT-MIB", "validationSectionIdxName"),
    (0, "METEL-SERVICES-WRT-MIB", "validationOptionName"),
)
if mibBuilder.loadTexts:
    wrtValidationEntry.setStatus("current")


class _ValidationFailId_Type(Integer32):
    """Custom type validationFailId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ValidationFailId_Type.__name__ = "Integer32"
_ValidationFailId_Object = MibTableColumn
validationFailId = _ValidationFailId_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 8, 111, 3, 1, 1, 1),
    _ValidationFailId_Type()
)
validationFailId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    validationFailId.setStatus("current")
_ValidationSectionName_Type = DisplayString
_ValidationSectionName_Object = MibTableColumn
validationSectionName = _ValidationSectionName_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 8, 111, 3, 1, 1, 2),
    _ValidationSectionName_Type()
)
validationSectionName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    validationSectionName.setStatus("current")
_ValidationSectionIdxName_Type = DisplayString
_ValidationSectionIdxName_Object = MibTableColumn
validationSectionIdxName = _ValidationSectionIdxName_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 8, 111, 3, 1, 1, 3),
    _ValidationSectionIdxName_Type()
)
validationSectionIdxName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    validationSectionIdxName.setStatus("current")
_ValidationOptionName_Type = DisplayString
_ValidationOptionName_Object = MibTableColumn
validationOptionName = _ValidationOptionName_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 8, 111, 3, 1, 1, 4),
    _ValidationOptionName_Type()
)
validationOptionName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    validationOptionName.setStatus("current")
_ValidationRowStatus_Type = RowStatus
_ValidationRowStatus_Object = MibTableColumn
validationRowStatus = _ValidationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 8, 111, 3, 1, 1, 5),
    _ValidationRowStatus_Type()
)
validationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    validationRowStatus.setStatus("current")
_ValidationRule_Type = DisplayString
_ValidationRule_Object = MibTableColumn
validationRule = _ValidationRule_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 8, 111, 3, 1, 1, 6),
    _ValidationRule_Type()
)
validationRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    validationRule.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "METEL-SERVICES-WRT-MIB",
    **{"wrt": wrt,
       "config": config,
       "wrtConfigTable": wrtConfigTable,
       "wrtConfigEntry": wrtConfigEntry,
       "configSectionName": configSectionName,
       "configSectionIdxName": configSectionIdxName,
       "configOptionName": configOptionName,
       "configRowStatus": configRowStatus,
       "configStartUpValue": configStartUpValue,
       "configRunningValue": configRunningValue,
       "configDefaultValue": configDefaultValue,
       "configNewValue": configNewValue,
       "configIsChanged": configIsChanged,
       "wrtConfigWriteNew2StartUp": wrtConfigWriteNew2StartUp,
       "wrtConfigWriteNew2RunningAsync": wrtConfigWriteNew2RunningAsync,
       "wrtConfigWriteRunnig2StartUp": wrtConfigWriteRunnig2StartUp,
       "wrtConfigWriteStartUp2RunningAsync": wrtConfigWriteStartUp2RunningAsync,
       "wrtConfigWriteDefault2StartUp": wrtConfigWriteDefault2StartUp,
       "wrtConfigWriteDefault2RunningAsync": wrtConfigWriteDefault2RunningAsync,
       "wrtConfigClearNew": wrtConfigClearNew,
       "wrtConfigAsyncProgress": wrtConfigAsyncProgress,
       "status": status,
       "wrtStatusTable": wrtStatusTable,
       "wrtStatusEntry": wrtStatusEntry,
       "statusSectionName": statusSectionName,
       "statusSectionIdxName": statusSectionIdxName,
       "statusOptionName": statusOptionName,
       "actualValue": actualValue,
       "validation": validation,
       "wrtValidationTable": wrtValidationTable,
       "wrtValidationEntry": wrtValidationEntry,
       "validationFailId": validationFailId,
       "validationSectionName": validationSectionName,
       "validationSectionIdxName": validationSectionIdxName,
       "validationOptionName": validationOptionName,
       "validationRowStatus": validationRowStatus,
       "validationRule": validationRule}
)
