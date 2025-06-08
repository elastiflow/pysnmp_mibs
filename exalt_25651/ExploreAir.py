# SNMP MIB module (ExploreAir) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/exalt_25651/ExploreAir.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:22:49 2025
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

(systemConfig,) = mibBuilder.importSymbols(
    "ExaltComProducts",
    "systemConfig")

(AcmBaseModulationT,
 AcmPolicyT,
 AcmTargetModulationT,
 BandwidthT,
 BuzTimeoutT,
 DiplexerConfigT,
 ExaltEnableT,
 ModulationT,
 PerformanceModeT,
 RadioSourceT,
 RadioTxPwrHP11gT) = mibBuilder.importSymbols(
    "ExaltComm",
    "AcmBaseModulationT",
    "AcmPolicyT",
    "AcmTargetModulationT",
    "BandwidthT",
    "BuzTimeoutT",
    "DiplexerConfigT",
    "ExaltEnableT",
    "ModulationT",
    "PerformanceModeT",
    "RadioSourceT",
    "RadioTxPwrHP11gT")

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

exploreAir = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 54)
)
if mibBuilder.loadTexts:
    exploreAir.setRevisions(
        ("2007-01-30 00:28",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExploreAirTxPower_Type = RadioTxPwrHP11gT
_ExploreAirTxPower_Object = MibScalar
exploreAirTxPower = _ExploreAirTxPower_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 54, 1),
    _ExploreAirTxPower_Type()
)
exploreAirTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exploreAirTxPower.setStatus("current")
if mibBuilder.loadTexts:
    exploreAirTxPower.setUnits("Tenths of dBm.")
_ExploreAirBandwidth_Type = BandwidthT
_ExploreAirBandwidth_Object = MibScalar
exploreAirBandwidth = _ExploreAirBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 54, 2),
    _ExploreAirBandwidth_Type()
)
exploreAirBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exploreAirBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    exploreAirBandwidth.setUnits("kHz")
_ExploreAirModulation_Type = ModulationT
_ExploreAirModulation_Object = MibScalar
exploreAirModulation = _ExploreAirModulation_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 54, 3),
    _ExploreAirModulation_Type()
)
exploreAirModulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exploreAirModulation.setStatus("current")


class _ExploreAirTXfrequency_Type(DisplayString):
    """Custom type exploreAirTXfrequency based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 9),
    )


_ExploreAirTXfrequency_Type.__name__ = "DisplayString"
_ExploreAirTXfrequency_Object = MibScalar
exploreAirTXfrequency = _ExploreAirTXfrequency_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 54, 4),
    _ExploreAirTXfrequency_Type()
)
exploreAirTXfrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exploreAirTXfrequency.setStatus("current")
if mibBuilder.loadTexts:
    exploreAirTXfrequency.setUnits("MHz")


class _ExploreAirRXfrequency_Type(DisplayString):
    """Custom type exploreAirRXfrequency based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 9),
    )


_ExploreAirRXfrequency_Type.__name__ = "DisplayString"
_ExploreAirRXfrequency_Object = MibScalar
exploreAirRXfrequency = _ExploreAirRXfrequency_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 54, 5),
    _ExploreAirRXfrequency_Type()
)
exploreAirRXfrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exploreAirRXfrequency.setStatus("current")
if mibBuilder.loadTexts:
    exploreAirRXfrequency.setUnits("MHz")
_ExploreAirDiplexerConfiguration_Type = DiplexerConfigT
_ExploreAirDiplexerConfiguration_Object = MibScalar
exploreAirDiplexerConfiguration = _ExploreAirDiplexerConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 54, 6),
    _ExploreAirDiplexerConfiguration_Type()
)
exploreAirDiplexerConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exploreAirDiplexerConfiguration.setStatus("current")


class _ExploreAirInsertionLoss_Type(Integer32):
    """Custom type exploreAirInsertionLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ExploreAirInsertionLoss_Type.__name__ = "Integer32"
_ExploreAirInsertionLoss_Object = MibScalar
exploreAirInsertionLoss = _ExploreAirInsertionLoss_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 54, 7),
    _ExploreAirInsertionLoss_Type()
)
exploreAirInsertionLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exploreAirInsertionLoss.setStatus("current")
if mibBuilder.loadTexts:
    exploreAirInsertionLoss.setUnits("Hundredth dBm")
_ExploreAirBuzTimeout_Type = BuzTimeoutT
_ExploreAirBuzTimeout_Object = MibScalar
exploreAirBuzTimeout = _ExploreAirBuzTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 54, 8),
    _ExploreAirBuzTimeout_Type()
)
exploreAirBuzTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exploreAirBuzTimeout.setStatus("current")
_ExploreAirAcmMode_Type = ExaltEnableT
_ExploreAirAcmMode_Object = MibScalar
exploreAirAcmMode = _ExploreAirAcmMode_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 54, 9),
    _ExploreAirAcmMode_Type()
)
exploreAirAcmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exploreAirAcmMode.setStatus("current")
_ExploreAirAcmPolicy_Type = AcmPolicyT
_ExploreAirAcmPolicy_Object = MibScalar
exploreAirAcmPolicy = _ExploreAirAcmPolicy_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 54, 10),
    _ExploreAirAcmPolicy_Type()
)
exploreAirAcmPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exploreAirAcmPolicy.setStatus("current")
_ExploreAirAcmBaseModulation_Type = AcmBaseModulationT
_ExploreAirAcmBaseModulation_Object = MibScalar
exploreAirAcmBaseModulation = _ExploreAirAcmBaseModulation_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 54, 11),
    _ExploreAirAcmBaseModulation_Type()
)
exploreAirAcmBaseModulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exploreAirAcmBaseModulation.setStatus("current")
_ExploreAirAcmTargetModulation_Type = AcmTargetModulationT
_ExploreAirAcmTargetModulation_Object = MibScalar
exploreAirAcmTargetModulation = _ExploreAirAcmTargetModulation_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 54, 12),
    _ExploreAirAcmTargetModulation_Type()
)
exploreAirAcmTargetModulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exploreAirAcmTargetModulation.setStatus("current")
_ExploreAirPerformanceMode_Type = PerformanceModeT
_ExploreAirPerformanceMode_Object = MibScalar
exploreAirPerformanceMode = _ExploreAirPerformanceMode_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 54, 13),
    _ExploreAirPerformanceMode_Type()
)
exploreAirPerformanceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exploreAirPerformanceMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ExploreAir",
    **{"exploreAir": exploreAir,
       "exploreAirTxPower": exploreAirTxPower,
       "exploreAirBandwidth": exploreAirBandwidth,
       "exploreAirModulation": exploreAirModulation,
       "exploreAirTXfrequency": exploreAirTXfrequency,
       "exploreAirRXfrequency": exploreAirRXfrequency,
       "exploreAirDiplexerConfiguration": exploreAirDiplexerConfiguration,
       "exploreAirInsertionLoss": exploreAirInsertionLoss,
       "exploreAirBuzTimeout": exploreAirBuzTimeout,
       "exploreAirAcmMode": exploreAirAcmMode,
       "exploreAirAcmPolicy": exploreAirAcmPolicy,
       "exploreAirAcmBaseModulation": exploreAirAcmBaseModulation,
       "exploreAirAcmTargetModulation": exploreAirAcmTargetModulation,
       "exploreAirPerformanceMode": exploreAirPerformanceMode}
)
