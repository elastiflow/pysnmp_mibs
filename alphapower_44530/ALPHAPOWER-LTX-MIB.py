# SNMP MIB module (ALPHAPOWER-LTX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/alphapower_44530/ALPHAPOWER-LTX-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 09:22:36 2025
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Alphapower_ObjectIdentity = ObjectIdentity
alphapower = _Alphapower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44530)
)
_AlphapowerTable_Object = MibTable
alphapowerTable = _AlphapowerTable_Object(
    (1, 3, 6, 1, 4, 1, 44530, 1)
)
if mibBuilder.loadTexts:
    alphapowerTable.setStatus("current")
_AlphapowerEntry_Object = MibTableRow
alphapowerEntry = _AlphapowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 44530, 1, 1)
)
alphapowerEntry.setIndexNames(
    (0, "ALPHAPOWER-LTX-MIB", "alphapowerIndex"),
)
if mibBuilder.loadTexts:
    alphapowerEntry.setStatus("current")


class _AlphapowerIndex_Type(Integer32):
    """Custom type alphapowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AlphapowerIndex_Type.__name__ = "Integer32"
_AlphapowerIndex_Object = MibTableColumn
alphapowerIndex = _AlphapowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 44530, 1, 1, 1),
    _AlphapowerIndex_Type()
)
alphapowerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alphapowerIndex.setStatus("current")


class _ApIPAddress_Type(DisplayString):
    """Custom type apIPAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApIPAddress_Type.__name__ = "DisplayString"
_ApIPAddress_Object = MibTableColumn
apIPAddress = _ApIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 44530, 1, 1, 2),
    _ApIPAddress_Type()
)
apIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIPAddress.setStatus("current")


class _ApIPPort_Type(Integer32):
    """Custom type apIPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_ApIPPort_Type.__name__ = "Integer32"
_ApIPPort_Object = MibTableColumn
apIPPort = _ApIPPort_Object(
    (1, 3, 6, 1, 4, 1, 44530, 1, 1, 3),
    _ApIPPort_Type()
)
apIPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIPPort.setStatus("current")


class _ApInputVolts_Type(DisplayString):
    """Custom type apInputVolts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ApInputVolts_Type.__name__ = "DisplayString"
_ApInputVolts_Object = MibTableColumn
apInputVolts = _ApInputVolts_Object(
    (1, 3, 6, 1, 4, 1, 44530, 1, 1, 4),
    _ApInputVolts_Type()
)
apInputVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInputVolts.setStatus("current")


class _ApInputFaultVolts_Type(DisplayString):
    """Custom type apInputFaultVolts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ApInputFaultVolts_Type.__name__ = "DisplayString"
_ApInputFaultVolts_Object = MibTableColumn
apInputFaultVolts = _ApInputFaultVolts_Object(
    (1, 3, 6, 1, 4, 1, 44530, 1, 1, 5),
    _ApInputFaultVolts_Type()
)
apInputFaultVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInputFaultVolts.setStatus("current")


class _ApOutputVolts_Type(DisplayString):
    """Custom type apOutputVolts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ApOutputVolts_Type.__name__ = "DisplayString"
_ApOutputVolts_Object = MibTableColumn
apOutputVolts = _ApOutputVolts_Object(
    (1, 3, 6, 1, 4, 1, 44530, 1, 1, 6),
    _ApOutputVolts_Type()
)
apOutputVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutputVolts.setStatus("current")
_ApOutputCurrent_Type = Gauge32
_ApOutputCurrent_Object = MibTableColumn
apOutputCurrent = _ApOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 44530, 1, 1, 7),
    _ApOutputCurrent_Type()
)
apOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutputCurrent.setStatus("current")


class _ApOutputFrequency_Type(DisplayString):
    """Custom type apOutputFrequency based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_ApOutputFrequency_Type.__name__ = "DisplayString"
_ApOutputFrequency_Object = MibTableColumn
apOutputFrequency = _ApOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 44530, 1, 1, 8),
    _ApOutputFrequency_Type()
)
apOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutputFrequency.setStatus("current")


class _ApDCVolts_Type(DisplayString):
    """Custom type apDCVolts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_ApDCVolts_Type.__name__ = "DisplayString"
_ApDCVolts_Object = MibTableColumn
apDCVolts = _ApDCVolts_Object(
    (1, 3, 6, 1, 4, 1, 44530, 1, 1, 9),
    _ApDCVolts_Type()
)
apDCVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDCVolts.setStatus("current")


class _ApTemperature_Type(DisplayString):
    """Custom type apTemperature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_ApTemperature_Type.__name__ = "DisplayString"
_ApTemperature_Object = MibTableColumn
apTemperature = _ApTemperature_Object(
    (1, 3, 6, 1, 4, 1, 44530, 1, 1, 10),
    _ApTemperature_Type()
)
apTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTemperature.setStatus("current")
_ApLsUtilityFail_Type = TruthValue
_ApLsUtilityFail_Object = MibTableColumn
apLsUtilityFail = _ApLsUtilityFail_Object(
    (1, 3, 6, 1, 4, 1, 44530, 1, 1, 11),
    _ApLsUtilityFail_Type()
)
apLsUtilityFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLsUtilityFail.setStatus("current")
_ApLsDcLow_Type = TruthValue
_ApLsDcLow_Object = MibScalar
apLsDcLow = _ApLsDcLow_Object(
    (1, 3, 6, 1, 4, 1, 44530, 1, 1, 12),
    _ApLsDcLow_Type()
)
apLsDcLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLsDcLow.setStatus("current")
_ApLsAVR_Type = TruthValue
_ApLsAVR_Object = MibTableColumn
apLsAVR = _ApLsAVR_Object(
    (1, 3, 6, 1, 4, 1, 44530, 1, 1, 13),
    _ApLsAVR_Type()
)
apLsAVR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLsAVR.setStatus("current")
_ApLsInverterFail_Type = TruthValue
_ApLsInverterFail_Object = MibTableColumn
apLsInverterFail = _ApLsInverterFail_Object(
    (1, 3, 6, 1, 4, 1, 44530, 1, 1, 14),
    _ApLsInverterFail_Type()
)
apLsInverterFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLsInverterFail.setStatus("current")
_ApLsInverterOffline_Type = TruthValue
_ApLsInverterOffline_Object = MibTableColumn
apLsInverterOffline = _ApLsInverterOffline_Object(
    (1, 3, 6, 1, 4, 1, 44530, 1, 1, 15),
    _ApLsInverterOffline_Type()
)
apLsInverterOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLsInverterOffline.setStatus("current")
_ApLsTesting_Type = TruthValue
_ApLsTesting_Object = MibTableColumn
apLsTesting = _ApLsTesting_Object(
    (1, 3, 6, 1, 4, 1, 44530, 1, 1, 16),
    _ApLsTesting_Type()
)
apLsTesting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLsTesting.setStatus("current")
_ApLsShutdownActive_Type = TruthValue
_ApLsShutdownActive_Object = MibTableColumn
apLsShutdownActive = _ApLsShutdownActive_Object(
    (1, 3, 6, 1, 4, 1, 44530, 1, 1, 17),
    _ApLsShutdownActive_Type()
)
apLsShutdownActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLsShutdownActive.setStatus("current")
_ApLsBeeping_Type = TruthValue
_ApLsBeeping_Object = MibTableColumn
apLsBeeping = _ApLsBeeping_Object(
    (1, 3, 6, 1, 4, 1, 44530, 1, 1, 18),
    _ApLsBeeping_Type()
)
apLsBeeping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLsBeeping.setStatus("current")
_ApTraps_ObjectIdentity = ObjectIdentity
apTraps = _ApTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44530, 2)
)

# Managed Objects groups


# Notification objects

apTrapUtilityFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 44530, 2, 1)
)
apTrapUtilityFail.setObjects(
      *(("ALPHAPOWER-LTX-MIB", "apIPAddress"),
        ("ALPHAPOWER-LTX-MIB", "apIPPort"))
)
if mibBuilder.loadTexts:
    apTrapUtilityFail.setStatus(
        "current"
    )

apTrapDCLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 44530, 2, 2)
)
apTrapDCLow.setObjects(
      *(("ALPHAPOWER-LTX-MIB", "apIPAddress"),
        ("ALPHAPOWER-LTX-MIB", "apIPPort"))
)
if mibBuilder.loadTexts:
    apTrapDCLow.setStatus(
        "current"
    )

apTrapInverterFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 44530, 2, 3)
)
apTrapInverterFailed.setObjects(
      *(("ALPHAPOWER-LTX-MIB", "apIPAddress"),
        ("ALPHAPOWER-LTX-MIB", "apIPPort"))
)
if mibBuilder.loadTexts:
    apTrapInverterFailed.setStatus(
        "current"
    )

apTrapInverterLineInteractive = NotificationType(
    (1, 3, 6, 1, 4, 1, 44530, 2, 4)
)
apTrapInverterLineInteractive.setObjects(
      *(("ALPHAPOWER-LTX-MIB", "apIPAddress"),
        ("ALPHAPOWER-LTX-MIB", "apIPPort"))
)
if mibBuilder.loadTexts:
    apTrapInverterLineInteractive.setStatus(
        "current"
    )

apRFU = NotificationType(
    (1, 3, 6, 1, 4, 1, 44530, 2, 5)
)
apRFU.setObjects(
      *(("ALPHAPOWER-LTX-MIB", "apIPAddress"),
        ("ALPHAPOWER-LTX-MIB", "apIPPort"))
)
if mibBuilder.loadTexts:
    apRFU.setStatus(
        "current"
    )

apTrapShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 44530, 2, 6)
)
apTrapShutdown.setObjects(
      *(("ALPHAPOWER-LTX-MIB", "apIPAddress"),
        ("ALPHAPOWER-LTX-MIB", "apIPPort"))
)
if mibBuilder.loadTexts:
    apTrapShutdown.setStatus(
        "current"
    )

apTrapBeeper = NotificationType(
    (1, 3, 6, 1, 4, 1, 44530, 2, 7)
)
apTrapBeeper.setObjects(
      *(("ALPHAPOWER-LTX-MIB", "apIPAddress"),
        ("ALPHAPOWER-LTX-MIB", "apIPPort"))
)
if mibBuilder.loadTexts:
    apTrapBeeper.setStatus(
        "current"
    )

apTrapOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 44530, 2, 8)
)
apTrapOverload.setObjects(
      *(("ALPHAPOWER-LTX-MIB", "apIPAddress"),
        ("ALPHAPOWER-LTX-MIB", "apIPPort"),
        ("ALPHAPOWER-LTX-MIB", "apOutputCurrent"))
)
if mibBuilder.loadTexts:
    apTrapOverload.setStatus(
        "current"
    )

apTrapThermal = NotificationType(
    (1, 3, 6, 1, 4, 1, 44530, 2, 9)
)
apTrapThermal.setObjects(
      *(("ALPHAPOWER-LTX-MIB", "apIPAddress"),
        ("ALPHAPOWER-LTX-MIB", "apIPPort"),
        ("ALPHAPOWER-LTX-MIB", "apTemperature"))
)
if mibBuilder.loadTexts:
    apTrapThermal.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALPHAPOWER-LTX-MIB",
    **{"alphapower": alphapower,
       "alphapowerTable": alphapowerTable,
       "alphapowerEntry": alphapowerEntry,
       "alphapowerIndex": alphapowerIndex,
       "apIPAddress": apIPAddress,
       "apIPPort": apIPPort,
       "apInputVolts": apInputVolts,
       "apInputFaultVolts": apInputFaultVolts,
       "apOutputVolts": apOutputVolts,
       "apOutputCurrent": apOutputCurrent,
       "apOutputFrequency": apOutputFrequency,
       "apDCVolts": apDCVolts,
       "apTemperature": apTemperature,
       "apLsUtilityFail": apLsUtilityFail,
       "apLsDcLow": apLsDcLow,
       "apLsAVR": apLsAVR,
       "apLsInverterFail": apLsInverterFail,
       "apLsInverterOffline": apLsInverterOffline,
       "apLsTesting": apLsTesting,
       "apLsShutdownActive": apLsShutdownActive,
       "apLsBeeping": apLsBeeping,
       "apTraps": apTraps,
       "apTrapUtilityFail": apTrapUtilityFail,
       "apTrapDCLow": apTrapDCLow,
       "apTrapInverterFailed": apTrapInverterFailed,
       "apTrapInverterLineInteractive": apTrapInverterLineInteractive,
       "apRFU": apRFU,
       "apTrapShutdown": apTrapShutdown,
       "apTrapBeeper": apTrapBeeper,
       "apTrapOverload": apTrapOverload,
       "apTrapThermal": apTrapThermal}
)
