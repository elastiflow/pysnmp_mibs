# SNMP MIB module (EKINOPS-PmMC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-PmMC-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 12:01:48 2025
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

(EkiApiState,
 EkiMeasureType,
 EkiMode,
 EkiOnOff,
 EkiProtocol,
 EkiState,
 EkiSynchroMode,
 ekinops) = mibBuilder.importSymbols(
    "EKINOPS-MIB",
    "EkiApiState",
    "EkiMeasureType",
    "EkiMode",
    "EkiOnOff",
    "EkiProtocol",
    "EkiState",
    "EkiSynchroMode",
    "ekinops")

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

modulePmMC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21)
)
if mibBuilder.loadTexts:
    modulePmMC.setRevisions(
        ("2007-01-10 00:00",
         "2007-06-29 00:00",
         "2007-08-23 00:00",
         "2007-11-21 00:00",
         "2009-04-10 00:00",
         "2009-09-18 00:00",
         "2010-02-25 00:00",
         "2010-11-04 00:00",
         "2010-12-17 00:00",
         "2012-07-04 00:00",
         "2014-03-26 00:00",
         "2014-12-11 00:00",
         "2016-05-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PmmcBitRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("rateSTM16OC48", 0),
          ("rate1GBE", 1),
          ("rateSTM4OC12", 2),
          ("rateSTM1OC3", 3),
          ("rate2GFC", 4),
          ("rate1GFC", 5),
          ("rateFastEthernet", 7),
          ("rateSTM16FEC", 8),
          ("rateSTM4FEC", 9),
          ("rateSTM1FEC", 10))
    )



# MIB Managed Objects in the order of their OIDs

_Pmmcalarms_ObjectIdentity = ObjectIdentity
pmmcalarms = _Pmmcalarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2)
)
_PmmcAlmOther_ObjectIdentity = ObjectIdentity
pmmcAlmOther = _PmmcAlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 1)
)
_PmmcAlmOtherNurg_ObjectIdentity = ObjectIdentity
pmmcAlmOtherNurg = _PmmcAlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 1, 1)
)
_PmmcAlmOtherUrg_ObjectIdentity = ObjectIdentity
pmmcAlmOtherUrg = _PmmcAlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 1, 2)
)
_PmmcAlmOtherCrit_ObjectIdentity = ObjectIdentity
pmmcAlmOtherCrit = _PmmcAlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 1, 3)
)
_PmmcAlmsynthAlm0_ObjectIdentity = ObjectIdentity
pmmcAlmsynthAlm0 = _PmmcAlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 1, 3, 0)
)
_PmmcAlmModuleGlobFailure_Type = EkiOnOff
_PmmcAlmModuleGlobFailure_Object = MibScalar
pmmcAlmModuleGlobFailure = _PmmcAlmModuleGlobFailure_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 1, 3, 0, 9),
    _PmmcAlmModuleGlobFailure_Type()
)
pmmcAlmModuleGlobFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmModuleGlobFailure.setStatus("current")
_PmmcAlmSynUnlock_Type = EkiOnOff
_PmmcAlmSynUnlock_Object = MibScalar
pmmcAlmSynUnlock = _PmmcAlmSynUnlock_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 1, 3, 0, 14),
    _PmmcAlmSynUnlock_Type()
)
pmmcAlmSynUnlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmSynUnlock.setStatus("current")
_PmmcAlmDefFuseA_Type = EkiOnOff
_PmmcAlmDefFuseA_Object = MibScalar
pmmcAlmDefFuseA = _PmmcAlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 1, 3, 0, 15),
    _PmmcAlmDefFuseA_Type()
)
pmmcAlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmDefFuseA.setStatus("current")
_PmmcAlmDefFuseB_Type = EkiOnOff
_PmmcAlmDefFuseB_Object = MibScalar
pmmcAlmDefFuseB = _PmmcAlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 1, 3, 0, 16),
    _PmmcAlmDefFuseB_Type()
)
pmmcAlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmDefFuseB.setStatus("current")
_PmmcAlmClient_ObjectIdentity = ObjectIdentity
pmmcAlmClient = _PmmcAlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2)
)
_PmmcAlmClientNurg_ObjectIdentity = ObjectIdentity
pmmcAlmClientNurg = _PmmcAlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 1)
)
_PmmcAlmline1TrscvWarnDdm_ObjectIdentity = ObjectIdentity
pmmcAlmline1TrscvWarnDdm = _PmmcAlmline1TrscvWarnDdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 1, 20)
)
_PmmcAlmLine1TxPwLowWng_Type = EkiOnOff
_PmmcAlmLine1TxPwLowWng_Object = MibScalar
pmmcAlmLine1TxPwLowWng = _PmmcAlmLine1TxPwLowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 1, 20, 1),
    _PmmcAlmLine1TxPwLowWng_Type()
)
pmmcAlmLine1TxPwLowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine1TxPwLowWng.setStatus("current")
_PmmcAlmLine1TxPwrHighWng_Type = EkiOnOff
_PmmcAlmLine1TxPwrHighWng_Object = MibScalar
pmmcAlmLine1TxPwrHighWng = _PmmcAlmLine1TxPwrHighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 1, 20, 2),
    _PmmcAlmLine1TxPwrHighWng_Type()
)
pmmcAlmLine1TxPwrHighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine1TxPwrHighWng.setStatus("current")
_PmmcAlmLine1TxBiasLowWng_Type = EkiOnOff
_PmmcAlmLine1TxBiasLowWng_Object = MibScalar
pmmcAlmLine1TxBiasLowWng = _PmmcAlmLine1TxBiasLowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 1, 20, 3),
    _PmmcAlmLine1TxBiasLowWng_Type()
)
pmmcAlmLine1TxBiasLowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine1TxBiasLowWng.setStatus("current")
_PmmcAlmLine1TxBiasHighWng_Type = EkiOnOff
_PmmcAlmLine1TxBiasHighWng_Object = MibScalar
pmmcAlmLine1TxBiasHighWng = _PmmcAlmLine1TxBiasHighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 1, 20, 4),
    _PmmcAlmLine1TxBiasHighWng_Type()
)
pmmcAlmLine1TxBiasHighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine1TxBiasHighWng.setStatus("current")
_PmmcAlmLine1VccLowWng_Type = EkiOnOff
_PmmcAlmLine1VccLowWng_Object = MibScalar
pmmcAlmLine1VccLowWng = _PmmcAlmLine1VccLowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 1, 20, 5),
    _PmmcAlmLine1VccLowWng_Type()
)
pmmcAlmLine1VccLowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine1VccLowWng.setStatus("current")
_PmmcAlmLine1VccHighWng_Type = EkiOnOff
_PmmcAlmLine1VccHighWng_Object = MibScalar
pmmcAlmLine1VccHighWng = _PmmcAlmLine1VccHighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 1, 20, 6),
    _PmmcAlmLine1VccHighWng_Type()
)
pmmcAlmLine1VccHighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine1VccHighWng.setStatus("current")
_PmmcAlmLine1TempLowWng_Type = EkiOnOff
_PmmcAlmLine1TempLowWng_Object = MibScalar
pmmcAlmLine1TempLowWng = _PmmcAlmLine1TempLowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 1, 20, 7),
    _PmmcAlmLine1TempLowWng_Type()
)
pmmcAlmLine1TempLowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine1TempLowWng.setStatus("current")
_PmmcAlmLine1TempHighWng_Type = EkiOnOff
_PmmcAlmLine1TempHighWng_Object = MibScalar
pmmcAlmLine1TempHighWng = _PmmcAlmLine1TempHighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 1, 20, 8),
    _PmmcAlmLine1TempHighWng_Type()
)
pmmcAlmLine1TempHighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine1TempHighWng.setStatus("current")
_PmmcAlmLine1RxPwrLowWng_Type = EkiOnOff
_PmmcAlmLine1RxPwrLowWng_Object = MibScalar
pmmcAlmLine1RxPwrLowWng = _PmmcAlmLine1RxPwrLowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 1, 20, 15),
    _PmmcAlmLine1RxPwrLowWng_Type()
)
pmmcAlmLine1RxPwrLowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine1RxPwrLowWng.setStatus("current")
_PmmcAlmLine1RxPwrHighWng_Type = EkiOnOff
_PmmcAlmLine1RxPwrHighWng_Object = MibScalar
pmmcAlmLine1RxPwrHighWng = _PmmcAlmLine1RxPwrHighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 1, 20, 16),
    _PmmcAlmLine1RxPwrHighWng_Type()
)
pmmcAlmLine1RxPwrHighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine1RxPwrHighWng.setStatus("current")
_PmmcAlmline1CdrAlm_ObjectIdentity = ObjectIdentity
pmmcAlmline1CdrAlm = _PmmcAlmline1CdrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 1, 23)
)
_PmmcAlmLine1CdrLossofsignal_Type = EkiOnOff
_PmmcAlmLine1CdrLossofsignal_Object = MibScalar
pmmcAlmLine1CdrLossofsignal = _PmmcAlmLine1CdrLossofsignal_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 1, 23, 1),
    _PmmcAlmLine1CdrLossofsignal_Type()
)
pmmcAlmLine1CdrLossofsignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine1CdrLossofsignal.setStatus("current")
_PmmcAlmLine1CdrLossoflock_Type = EkiOnOff
_PmmcAlmLine1CdrLossoflock_Object = MibScalar
pmmcAlmLine1CdrLossoflock = _PmmcAlmLine1CdrLossoflock_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 1, 23, 2),
    _PmmcAlmLine1CdrLossoflock_Type()
)
pmmcAlmLine1CdrLossoflock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine1CdrLossoflock.setStatus("current")
_PmmcAlmLine1CdrRefAbsent_Type = EkiOnOff
_PmmcAlmLine1CdrRefAbsent_Object = MibScalar
pmmcAlmLine1CdrRefAbsent = _PmmcAlmLine1CdrRefAbsent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 1, 23, 3),
    _PmmcAlmLine1CdrRefAbsent_Type()
)
pmmcAlmLine1CdrRefAbsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine1CdrRefAbsent.setStatus("current")
_PmmcAlmClientUrg_ObjectIdentity = ObjectIdentity
pmmcAlmClientUrg = _PmmcAlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 2)
)
_PmmcAlmline1TrscvAlmDdm_ObjectIdentity = ObjectIdentity
pmmcAlmline1TrscvAlmDdm = _PmmcAlmline1TrscvAlmDdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 2, 18)
)
_PmmcAlmLine1TxPwrLowAla_Type = EkiOnOff
_PmmcAlmLine1TxPwrLowAla_Object = MibScalar
pmmcAlmLine1TxPwrLowAla = _PmmcAlmLine1TxPwrLowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 2, 18, 1),
    _PmmcAlmLine1TxPwrLowAla_Type()
)
pmmcAlmLine1TxPwrLowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine1TxPwrLowAla.setStatus("current")
_PmmcAlmLine1TxPwrHighAla_Type = EkiOnOff
_PmmcAlmLine1TxPwrHighAla_Object = MibScalar
pmmcAlmLine1TxPwrHighAla = _PmmcAlmLine1TxPwrHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 2, 18, 2),
    _PmmcAlmLine1TxPwrHighAla_Type()
)
pmmcAlmLine1TxPwrHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine1TxPwrHighAla.setStatus("current")
_PmmcAlmLine1TxBiasLowAla_Type = EkiOnOff
_PmmcAlmLine1TxBiasLowAla_Object = MibScalar
pmmcAlmLine1TxBiasLowAla = _PmmcAlmLine1TxBiasLowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 2, 18, 3),
    _PmmcAlmLine1TxBiasLowAla_Type()
)
pmmcAlmLine1TxBiasLowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine1TxBiasLowAla.setStatus("current")
_PmmcAlmLine1TxBiasHighAla_Type = EkiOnOff
_PmmcAlmLine1TxBiasHighAla_Object = MibScalar
pmmcAlmLine1TxBiasHighAla = _PmmcAlmLine1TxBiasHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 2, 18, 4),
    _PmmcAlmLine1TxBiasHighAla_Type()
)
pmmcAlmLine1TxBiasHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine1TxBiasHighAla.setStatus("current")
_PmmcAlmLine1VccLowAla_Type = EkiOnOff
_PmmcAlmLine1VccLowAla_Object = MibScalar
pmmcAlmLine1VccLowAla = _PmmcAlmLine1VccLowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 2, 18, 5),
    _PmmcAlmLine1VccLowAla_Type()
)
pmmcAlmLine1VccLowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine1VccLowAla.setStatus("current")
_PmmcAlmLine1VccHighAla_Type = EkiOnOff
_PmmcAlmLine1VccHighAla_Object = MibScalar
pmmcAlmLine1VccHighAla = _PmmcAlmLine1VccHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 2, 18, 6),
    _PmmcAlmLine1VccHighAla_Type()
)
pmmcAlmLine1VccHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine1VccHighAla.setStatus("current")
_PmmcAlmLine1TempLowAla_Type = EkiOnOff
_PmmcAlmLine1TempLowAla_Object = MibScalar
pmmcAlmLine1TempLowAla = _PmmcAlmLine1TempLowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 2, 18, 7),
    _PmmcAlmLine1TempLowAla_Type()
)
pmmcAlmLine1TempLowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine1TempLowAla.setStatus("current")
_PmmcAlmLine1TempHighAla_Type = EkiOnOff
_PmmcAlmLine1TempHighAla_Object = MibScalar
pmmcAlmLine1TempHighAla = _PmmcAlmLine1TempHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 2, 18, 8),
    _PmmcAlmLine1TempHighAla_Type()
)
pmmcAlmLine1TempHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine1TempHighAla.setStatus("current")
_PmmcAlmLine1RxPwrLowAla_Type = EkiOnOff
_PmmcAlmLine1RxPwrLowAla_Object = MibScalar
pmmcAlmLine1RxPwrLowAla = _PmmcAlmLine1RxPwrLowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 2, 18, 15),
    _PmmcAlmLine1RxPwrLowAla_Type()
)
pmmcAlmLine1RxPwrLowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine1RxPwrLowAla.setStatus("current")
_PmmcAlmLine1RxPwrHighAla_Type = EkiOnOff
_PmmcAlmLine1RxPwrHighAla_Object = MibScalar
pmmcAlmLine1RxPwrHighAla = _PmmcAlmLine1RxPwrHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 2, 18, 16),
    _PmmcAlmLine1RxPwrHighAla_Type()
)
pmmcAlmLine1RxPwrHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine1RxPwrHighAla.setStatus("current")
_PmmcAlmClientCrit_ObjectIdentity = ObjectIdentity
pmmcAlmClientCrit = _PmmcAlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 3)
)
_PmmcAlmsynthAlm8_ObjectIdentity = ObjectIdentity
pmmcAlmsynthAlm8 = _PmmcAlmsynthAlm8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 3, 8)
)
_PmmcAlmLine1TrscvAbsent_Type = EkiOnOff
_PmmcAlmLine1TrscvAbsent_Object = MibScalar
pmmcAlmLine1TrscvAbsent = _PmmcAlmLine1TrscvAbsent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 3, 8, 1),
    _PmmcAlmLine1TrscvAbsent_Type()
)
pmmcAlmLine1TrscvAbsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine1TrscvAbsent.setStatus("current")
_PmmcAlmLine1TrscvDdmAbsent_Type = EkiOnOff
_PmmcAlmLine1TrscvDdmAbsent_Object = MibScalar
pmmcAlmLine1TrscvDdmAbsent = _PmmcAlmLine1TrscvDdmAbsent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 3, 8, 2),
    _PmmcAlmLine1TrscvDdmAbsent_Type()
)
pmmcAlmLine1TrscvDdmAbsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine1TrscvDdmAbsent.setStatus("current")
_PmmcAlmLine1HwFail_Type = EkiOnOff
_PmmcAlmLine1HwFail_Object = MibScalar
pmmcAlmLine1HwFail = _PmmcAlmLine1HwFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 3, 8, 4),
    _PmmcAlmLine1HwFail_Type()
)
pmmcAlmLine1HwFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine1HwFail.setStatus("current")
_PmmcAlmLine1TrscvLsd_Type = EkiOnOff
_PmmcAlmLine1TrscvLsd_Object = MibScalar
pmmcAlmLine1TrscvLsd = _PmmcAlmLine1TrscvLsd_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 3, 8, 5),
    _PmmcAlmLine1TrscvLsd_Type()
)
pmmcAlmLine1TrscvLsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine1TrscvLsd.setStatus("current")
_PmmcAlmLine1TrscvDdmWarning_Type = EkiOnOff
_PmmcAlmLine1TrscvDdmWarning_Object = MibScalar
pmmcAlmLine1TrscvDdmWarning = _PmmcAlmLine1TrscvDdmWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 3, 8, 9),
    _PmmcAlmLine1TrscvDdmWarning_Type()
)
pmmcAlmLine1TrscvDdmWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine1TrscvDdmWarning.setStatus("current")
_PmmcAlmLine1TrscvDdmAlm_Type = EkiOnOff
_PmmcAlmLine1TrscvDdmAlm_Object = MibScalar
pmmcAlmLine1TrscvDdmAlm = _PmmcAlmLine1TrscvDdmAlm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 3, 8, 10),
    _PmmcAlmLine1TrscvDdmAlm_Type()
)
pmmcAlmLine1TrscvDdmAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine1TrscvDdmAlm.setStatus("current")
_PmmcAlmLine1Fail_Type = EkiOnOff
_PmmcAlmLine1Fail_Object = MibScalar
pmmcAlmLine1Fail = _PmmcAlmLine1Fail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 3, 8, 12),
    _PmmcAlmLine1Fail_Type()
)
pmmcAlmLine1Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine1Fail.setStatus("current")
_PmmcAlmline1AccessioAlm_ObjectIdentity = ObjectIdentity
pmmcAlmline1AccessioAlm = _PmmcAlmline1AccessioAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 3, 16)
)
_PmmcAlmLine1LasFail_Type = EkiOnOff
_PmmcAlmLine1LasFail_Object = MibScalar
pmmcAlmLine1LasFail = _PmmcAlmLine1LasFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 3, 16, 1),
    _PmmcAlmLine1LasFail_Type()
)
pmmcAlmLine1LasFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine1LasFail.setStatus("current")
_PmmcAlmLine1Los_Type = EkiOnOff
_PmmcAlmLine1Los_Object = MibScalar
pmmcAlmLine1Los = _PmmcAlmLine1Los_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 2, 3, 16, 4),
    _PmmcAlmLine1Los_Type()
)
pmmcAlmLine1Los.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine1Los.setStatus("current")
_PmmcAlmLine_ObjectIdentity = ObjectIdentity
pmmcAlmLine = _PmmcAlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3)
)
_PmmcAlmLineNurg_ObjectIdentity = ObjectIdentity
pmmcAlmLineNurg = _PmmcAlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 1)
)
_PmmcAlmline2TrscvWarnDdm_ObjectIdentity = ObjectIdentity
pmmcAlmline2TrscvWarnDdm = _PmmcAlmline2TrscvWarnDdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 1, 28)
)
_PmmcAlmLine2TxPwLowWng_Type = EkiOnOff
_PmmcAlmLine2TxPwLowWng_Object = MibScalar
pmmcAlmLine2TxPwLowWng = _PmmcAlmLine2TxPwLowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 1, 28, 1),
    _PmmcAlmLine2TxPwLowWng_Type()
)
pmmcAlmLine2TxPwLowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine2TxPwLowWng.setStatus("current")
_PmmcAlmLine2TxPwrHighWng_Type = EkiOnOff
_PmmcAlmLine2TxPwrHighWng_Object = MibScalar
pmmcAlmLine2TxPwrHighWng = _PmmcAlmLine2TxPwrHighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 1, 28, 2),
    _PmmcAlmLine2TxPwrHighWng_Type()
)
pmmcAlmLine2TxPwrHighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine2TxPwrHighWng.setStatus("current")
_PmmcAlmLine2TxBiasLowWng_Type = EkiOnOff
_PmmcAlmLine2TxBiasLowWng_Object = MibScalar
pmmcAlmLine2TxBiasLowWng = _PmmcAlmLine2TxBiasLowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 1, 28, 3),
    _PmmcAlmLine2TxBiasLowWng_Type()
)
pmmcAlmLine2TxBiasLowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine2TxBiasLowWng.setStatus("current")
_PmmcAlmLine2TxBiasHighWng_Type = EkiOnOff
_PmmcAlmLine2TxBiasHighWng_Object = MibScalar
pmmcAlmLine2TxBiasHighWng = _PmmcAlmLine2TxBiasHighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 1, 28, 4),
    _PmmcAlmLine2TxBiasHighWng_Type()
)
pmmcAlmLine2TxBiasHighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine2TxBiasHighWng.setStatus("current")
_PmmcAlmLine2VccLowWng_Type = EkiOnOff
_PmmcAlmLine2VccLowWng_Object = MibScalar
pmmcAlmLine2VccLowWng = _PmmcAlmLine2VccLowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 1, 28, 5),
    _PmmcAlmLine2VccLowWng_Type()
)
pmmcAlmLine2VccLowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine2VccLowWng.setStatus("current")
_PmmcAlmLine2VccHighWng_Type = EkiOnOff
_PmmcAlmLine2VccHighWng_Object = MibScalar
pmmcAlmLine2VccHighWng = _PmmcAlmLine2VccHighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 1, 28, 6),
    _PmmcAlmLine2VccHighWng_Type()
)
pmmcAlmLine2VccHighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine2VccHighWng.setStatus("current")
_PmmcAlmLine2TempLowWng_Type = EkiOnOff
_PmmcAlmLine2TempLowWng_Object = MibScalar
pmmcAlmLine2TempLowWng = _PmmcAlmLine2TempLowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 1, 28, 7),
    _PmmcAlmLine2TempLowWng_Type()
)
pmmcAlmLine2TempLowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine2TempLowWng.setStatus("current")
_PmmcAlmLine2TempHighWng_Type = EkiOnOff
_PmmcAlmLine2TempHighWng_Object = MibScalar
pmmcAlmLine2TempHighWng = _PmmcAlmLine2TempHighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 1, 28, 8),
    _PmmcAlmLine2TempHighWng_Type()
)
pmmcAlmLine2TempHighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine2TempHighWng.setStatus("current")
_PmmcAlmLine2RxPwrLowWng_Type = EkiOnOff
_PmmcAlmLine2RxPwrLowWng_Object = MibScalar
pmmcAlmLine2RxPwrLowWng = _PmmcAlmLine2RxPwrLowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 1, 28, 15),
    _PmmcAlmLine2RxPwrLowWng_Type()
)
pmmcAlmLine2RxPwrLowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine2RxPwrLowWng.setStatus("current")
_PmmcAlmLine2RxPwrHighWng_Type = EkiOnOff
_PmmcAlmLine2RxPwrHighWng_Object = MibScalar
pmmcAlmLine2RxPwrHighWng = _PmmcAlmLine2RxPwrHighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 1, 28, 16),
    _PmmcAlmLine2RxPwrHighWng_Type()
)
pmmcAlmLine2RxPwrHighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine2RxPwrHighWng.setStatus("current")
_PmmcAlmline2CdrAlm_ObjectIdentity = ObjectIdentity
pmmcAlmline2CdrAlm = _PmmcAlmline2CdrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 1, 31)
)
_PmmcAlmLine2CdrLossofsignal_Type = EkiOnOff
_PmmcAlmLine2CdrLossofsignal_Object = MibScalar
pmmcAlmLine2CdrLossofsignal = _PmmcAlmLine2CdrLossofsignal_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 1, 31, 1),
    _PmmcAlmLine2CdrLossofsignal_Type()
)
pmmcAlmLine2CdrLossofsignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine2CdrLossofsignal.setStatus("current")
_PmmcAlmLine2CdrLossoflock_Type = EkiOnOff
_PmmcAlmLine2CdrLossoflock_Object = MibScalar
pmmcAlmLine2CdrLossoflock = _PmmcAlmLine2CdrLossoflock_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 1, 31, 2),
    _PmmcAlmLine2CdrLossoflock_Type()
)
pmmcAlmLine2CdrLossoflock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine2CdrLossoflock.setStatus("current")
_PmmcAlmLine2CdrRefAbsent_Type = EkiOnOff
_PmmcAlmLine2CdrRefAbsent_Object = MibScalar
pmmcAlmLine2CdrRefAbsent = _PmmcAlmLine2CdrRefAbsent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 1, 31, 3),
    _PmmcAlmLine2CdrRefAbsent_Type()
)
pmmcAlmLine2CdrRefAbsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine2CdrRefAbsent.setStatus("current")
_PmmcAlmLineUrg_ObjectIdentity = ObjectIdentity
pmmcAlmLineUrg = _PmmcAlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 2)
)
_PmmcAlmline2TrscvAlmDdm_ObjectIdentity = ObjectIdentity
pmmcAlmline2TrscvAlmDdm = _PmmcAlmline2TrscvAlmDdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 2, 26)
)
_PmmcAlmLine2TxPwrLowAla_Type = EkiOnOff
_PmmcAlmLine2TxPwrLowAla_Object = MibScalar
pmmcAlmLine2TxPwrLowAla = _PmmcAlmLine2TxPwrLowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 2, 26, 1),
    _PmmcAlmLine2TxPwrLowAla_Type()
)
pmmcAlmLine2TxPwrLowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine2TxPwrLowAla.setStatus("current")
_PmmcAlmLine2TxPwrHighAla_Type = EkiOnOff
_PmmcAlmLine2TxPwrHighAla_Object = MibScalar
pmmcAlmLine2TxPwrHighAla = _PmmcAlmLine2TxPwrHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 2, 26, 2),
    _PmmcAlmLine2TxPwrHighAla_Type()
)
pmmcAlmLine2TxPwrHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine2TxPwrHighAla.setStatus("current")
_PmmcAlmLine2TxBiasLowAla_Type = EkiOnOff
_PmmcAlmLine2TxBiasLowAla_Object = MibScalar
pmmcAlmLine2TxBiasLowAla = _PmmcAlmLine2TxBiasLowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 2, 26, 3),
    _PmmcAlmLine2TxBiasLowAla_Type()
)
pmmcAlmLine2TxBiasLowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine2TxBiasLowAla.setStatus("current")
_PmmcAlmLine2TxBiasHighAla_Type = EkiOnOff
_PmmcAlmLine2TxBiasHighAla_Object = MibScalar
pmmcAlmLine2TxBiasHighAla = _PmmcAlmLine2TxBiasHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 2, 26, 4),
    _PmmcAlmLine2TxBiasHighAla_Type()
)
pmmcAlmLine2TxBiasHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine2TxBiasHighAla.setStatus("current")
_PmmcAlmLine2VccLowAla_Type = EkiOnOff
_PmmcAlmLine2VccLowAla_Object = MibScalar
pmmcAlmLine2VccLowAla = _PmmcAlmLine2VccLowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 2, 26, 5),
    _PmmcAlmLine2VccLowAla_Type()
)
pmmcAlmLine2VccLowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine2VccLowAla.setStatus("current")
_PmmcAlmLine2VccHighAla_Type = EkiOnOff
_PmmcAlmLine2VccHighAla_Object = MibScalar
pmmcAlmLine2VccHighAla = _PmmcAlmLine2VccHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 2, 26, 6),
    _PmmcAlmLine2VccHighAla_Type()
)
pmmcAlmLine2VccHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine2VccHighAla.setStatus("current")
_PmmcAlmLine2TempLowAla_Type = EkiOnOff
_PmmcAlmLine2TempLowAla_Object = MibScalar
pmmcAlmLine2TempLowAla = _PmmcAlmLine2TempLowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 2, 26, 7),
    _PmmcAlmLine2TempLowAla_Type()
)
pmmcAlmLine2TempLowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine2TempLowAla.setStatus("current")
_PmmcAlmLine2TempHighAla_Type = EkiOnOff
_PmmcAlmLine2TempHighAla_Object = MibScalar
pmmcAlmLine2TempHighAla = _PmmcAlmLine2TempHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 2, 26, 8),
    _PmmcAlmLine2TempHighAla_Type()
)
pmmcAlmLine2TempHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine2TempHighAla.setStatus("current")
_PmmcAlmLine2RxPwrLowAla_Type = EkiOnOff
_PmmcAlmLine2RxPwrLowAla_Object = MibScalar
pmmcAlmLine2RxPwrLowAla = _PmmcAlmLine2RxPwrLowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 2, 26, 15),
    _PmmcAlmLine2RxPwrLowAla_Type()
)
pmmcAlmLine2RxPwrLowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine2RxPwrLowAla.setStatus("current")
_PmmcAlmLine2RxPwrHighAla_Type = EkiOnOff
_PmmcAlmLine2RxPwrHighAla_Object = MibScalar
pmmcAlmLine2RxPwrHighAla = _PmmcAlmLine2RxPwrHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 2, 26, 16),
    _PmmcAlmLine2RxPwrHighAla_Type()
)
pmmcAlmLine2RxPwrHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine2RxPwrHighAla.setStatus("current")
_PmmcAlmLineCrit_ObjectIdentity = ObjectIdentity
pmmcAlmLineCrit = _PmmcAlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 3)
)
_PmmcAlmsynthAlm7_ObjectIdentity = ObjectIdentity
pmmcAlmsynthAlm7 = _PmmcAlmsynthAlm7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 3, 7)
)
_PmmcAlmLine2TrscvAbsent_Type = EkiOnOff
_PmmcAlmLine2TrscvAbsent_Object = MibScalar
pmmcAlmLine2TrscvAbsent = _PmmcAlmLine2TrscvAbsent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 3, 7, 1),
    _PmmcAlmLine2TrscvAbsent_Type()
)
pmmcAlmLine2TrscvAbsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine2TrscvAbsent.setStatus("current")
_PmmcAlmLine2TrscvDdmAbsent_Type = EkiOnOff
_PmmcAlmLine2TrscvDdmAbsent_Object = MibScalar
pmmcAlmLine2TrscvDdmAbsent = _PmmcAlmLine2TrscvDdmAbsent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 3, 7, 2),
    _PmmcAlmLine2TrscvDdmAbsent_Type()
)
pmmcAlmLine2TrscvDdmAbsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine2TrscvDdmAbsent.setStatus("current")
_PmmcAlmLine2HwFail_Type = EkiOnOff
_PmmcAlmLine2HwFail_Object = MibScalar
pmmcAlmLine2HwFail = _PmmcAlmLine2HwFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 3, 7, 4),
    _PmmcAlmLine2HwFail_Type()
)
pmmcAlmLine2HwFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine2HwFail.setStatus("current")
_PmmcAlmLine2TrscvLsd_Type = EkiOnOff
_PmmcAlmLine2TrscvLsd_Object = MibScalar
pmmcAlmLine2TrscvLsd = _PmmcAlmLine2TrscvLsd_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 3, 7, 5),
    _PmmcAlmLine2TrscvLsd_Type()
)
pmmcAlmLine2TrscvLsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine2TrscvLsd.setStatus("current")
_PmmcAlmLine2TrscvDdmWarning_Type = EkiOnOff
_PmmcAlmLine2TrscvDdmWarning_Object = MibScalar
pmmcAlmLine2TrscvDdmWarning = _PmmcAlmLine2TrscvDdmWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 3, 7, 9),
    _PmmcAlmLine2TrscvDdmWarning_Type()
)
pmmcAlmLine2TrscvDdmWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine2TrscvDdmWarning.setStatus("current")
_PmmcAlmLine2TrscvDdmAlm_Type = EkiOnOff
_PmmcAlmLine2TrscvDdmAlm_Object = MibScalar
pmmcAlmLine2TrscvDdmAlm = _PmmcAlmLine2TrscvDdmAlm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 3, 7, 10),
    _PmmcAlmLine2TrscvDdmAlm_Type()
)
pmmcAlmLine2TrscvDdmAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine2TrscvDdmAlm.setStatus("current")
_PmmcAlmLine2Fail_Type = EkiOnOff
_PmmcAlmLine2Fail_Object = MibScalar
pmmcAlmLine2Fail = _PmmcAlmLine2Fail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 3, 7, 12),
    _PmmcAlmLine2Fail_Type()
)
pmmcAlmLine2Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine2Fail.setStatus("current")
_PmmcAlmline2AccessioAlm_ObjectIdentity = ObjectIdentity
pmmcAlmline2AccessioAlm = _PmmcAlmline2AccessioAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 3, 24)
)
_PmmcAlmLine2LasFail_Type = EkiOnOff
_PmmcAlmLine2LasFail_Object = MibScalar
pmmcAlmLine2LasFail = _PmmcAlmLine2LasFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 3, 24, 1),
    _PmmcAlmLine2LasFail_Type()
)
pmmcAlmLine2LasFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine2LasFail.setStatus("current")
_PmmcAlmLine2Los_Type = EkiOnOff
_PmmcAlmLine2Los_Object = MibScalar
pmmcAlmLine2Los = _PmmcAlmLine2Los_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 2, 3, 3, 24, 4),
    _PmmcAlmLine2Los_Type()
)
pmmcAlmLine2Los.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcAlmLine2Los.setStatus("current")
_Pmmcmeasures_ObjectIdentity = ObjectIdentity
pmmcmeasures = _Pmmcmeasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 3)
)
_PmmcMesrOther_ObjectIdentity = ObjectIdentity
pmmcMesrOther = _PmmcMesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 3, 1)
)
_PmmcMesrClient_ObjectIdentity = ObjectIdentity
pmmcMesrClient = _PmmcMesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 3, 2)
)


class _PmmcMesrline1Temperature_Type(Unsigned32):
    """Custom type pmmcMesrline1Temperature based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmmcMesrline1Temperature_Type.__name__ = "Unsigned32"
_PmmcMesrline1Temperature_Object = MibScalar
pmmcMesrline1Temperature = _PmmcMesrline1Temperature_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 3, 2, 16),
    _PmmcMesrline1Temperature_Type()
)
pmmcMesrline1Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcMesrline1Temperature.setStatus("current")


class _PmmcMesrline1Volt_Type(Unsigned32):
    """Custom type pmmcMesrline1Volt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmmcMesrline1Volt_Type.__name__ = "Unsigned32"
_PmmcMesrline1Volt_Object = MibScalar
pmmcMesrline1Volt = _PmmcMesrline1Volt_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 3, 2, 17),
    _PmmcMesrline1Volt_Type()
)
pmmcMesrline1Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcMesrline1Volt.setStatus("current")


class _PmmcMesrline1TxBias_Type(Unsigned32):
    """Custom type pmmcMesrline1TxBias based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmmcMesrline1TxBias_Type.__name__ = "Unsigned32"
_PmmcMesrline1TxBias_Object = MibScalar
pmmcMesrline1TxBias = _PmmcMesrline1TxBias_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 3, 2, 18),
    _PmmcMesrline1TxBias_Type()
)
pmmcMesrline1TxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcMesrline1TxBias.setStatus("current")


class _PmmcMesrline1TxPower_Type(Unsigned32):
    """Custom type pmmcMesrline1TxPower based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmmcMesrline1TxPower_Type.__name__ = "Unsigned32"
_PmmcMesrline1TxPower_Object = MibScalar
pmmcMesrline1TxPower = _PmmcMesrline1TxPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 3, 2, 19),
    _PmmcMesrline1TxPower_Type()
)
pmmcMesrline1TxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcMesrline1TxPower.setStatus("current")


class _PmmcMesrline1RxPower_Type(Unsigned32):
    """Custom type pmmcMesrline1RxPower based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmmcMesrline1RxPower_Type.__name__ = "Unsigned32"
_PmmcMesrline1RxPower_Object = MibScalar
pmmcMesrline1RxPower = _PmmcMesrline1RxPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 3, 2, 20),
    _PmmcMesrline1RxPower_Type()
)
pmmcMesrline1RxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcMesrline1RxPower.setStatus("current")
_PmmcMesrLine_ObjectIdentity = ObjectIdentity
pmmcMesrLine = _PmmcMesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 3, 3)
)


class _PmmcMesrline2Temperature_Type(Unsigned32):
    """Custom type pmmcMesrline2Temperature based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmmcMesrline2Temperature_Type.__name__ = "Unsigned32"
_PmmcMesrline2Temperature_Object = MibScalar
pmmcMesrline2Temperature = _PmmcMesrline2Temperature_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 3, 3, 24),
    _PmmcMesrline2Temperature_Type()
)
pmmcMesrline2Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcMesrline2Temperature.setStatus("current")


class _PmmcMesrline2Volt_Type(Unsigned32):
    """Custom type pmmcMesrline2Volt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmmcMesrline2Volt_Type.__name__ = "Unsigned32"
_PmmcMesrline2Volt_Object = MibScalar
pmmcMesrline2Volt = _PmmcMesrline2Volt_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 3, 3, 25),
    _PmmcMesrline2Volt_Type()
)
pmmcMesrline2Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcMesrline2Volt.setStatus("current")


class _PmmcMesrline2TxBias_Type(Unsigned32):
    """Custom type pmmcMesrline2TxBias based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmmcMesrline2TxBias_Type.__name__ = "Unsigned32"
_PmmcMesrline2TxBias_Object = MibScalar
pmmcMesrline2TxBias = _PmmcMesrline2TxBias_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 3, 3, 26),
    _PmmcMesrline2TxBias_Type()
)
pmmcMesrline2TxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcMesrline2TxBias.setStatus("current")


class _PmmcMesrline2TxPower_Type(Unsigned32):
    """Custom type pmmcMesrline2TxPower based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmmcMesrline2TxPower_Type.__name__ = "Unsigned32"
_PmmcMesrline2TxPower_Object = MibScalar
pmmcMesrline2TxPower = _PmmcMesrline2TxPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 3, 3, 27),
    _PmmcMesrline2TxPower_Type()
)
pmmcMesrline2TxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcMesrline2TxPower.setStatus("current")


class _PmmcMesrline2RxPower_Type(Unsigned32):
    """Custom type pmmcMesrline2RxPower based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmmcMesrline2RxPower_Type.__name__ = "Unsigned32"
_PmmcMesrline2RxPower_Object = MibScalar
pmmcMesrline2RxPower = _PmmcMesrline2RxPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 3, 3, 28),
    _PmmcMesrline2RxPower_Type()
)
pmmcMesrline2RxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcMesrline2RxPower.setStatus("current")
_PmmccontrolsWrite_ObjectIdentity = ObjectIdentity
pmmccontrolsWrite = _PmmccontrolsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 6)
)
_PmmcCtrlOther_ObjectIdentity = ObjectIdentity
pmmcCtrlOther = _PmmcCtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 6, 1)
)
_PmmcCtrlsynth0_ObjectIdentity = ObjectIdentity
pmmcCtrlsynth0 = _PmmcCtrlsynth0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 6, 1, 0)
)
_PmmcCtrlConfLoad_Type = EkiOnOff
_PmmcCtrlConfLoad_Object = MibScalar
pmmcCtrlConfLoad = _PmmcCtrlConfLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 6, 1, 0, 1),
    _PmmcCtrlConfLoad_Type()
)
pmmcCtrlConfLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmmcCtrlConfLoad.setStatus("current")
_PmmcCtrlConfFlash_Type = EkiOnOff
_PmmcCtrlConfFlash_Object = MibScalar
pmmcCtrlConfFlash = _PmmcCtrlConfFlash_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 6, 1, 0, 9),
    _PmmcCtrlConfFlash_Type()
)
pmmcCtrlConfFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmmcCtrlConfFlash.setStatus("current")
_PmmcCtrlConfClear_Type = EkiOnOff
_PmmcCtrlConfClear_Object = MibScalar
pmmcCtrlConfClear = _PmmcCtrlConfClear_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 6, 1, 0, 13),
    _PmmcCtrlConfClear_Type()
)
pmmcCtrlConfClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmmcCtrlConfClear.setStatus("current")
_PmmcCtrlsynth4_ObjectIdentity = ObjectIdentity
pmmcCtrlsynth4 = _PmmcCtrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 6, 1, 4)
)
_PmmcCtrlCorrelatOn_Type = EkiOnOff
_PmmcCtrlCorrelatOn_Object = MibScalar
pmmcCtrlCorrelatOn = _PmmcCtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 6, 1, 4, 1),
    _PmmcCtrlCorrelatOn_Type()
)
pmmcCtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmmcCtrlCorrelatOn.setStatus("current")
_PmmcCtrlCorrelatOff_Type = EkiOnOff
_PmmcCtrlCorrelatOff_Object = MibScalar
pmmcCtrlCorrelatOff = _PmmcCtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 6, 1, 4, 2),
    _PmmcCtrlCorrelatOff_Type()
)
pmmcCtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmmcCtrlCorrelatOff.setStatus("current")
_PmmcCtrlswMgnt_ObjectIdentity = ObjectIdentity
pmmcCtrlswMgnt = _PmmcCtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 6, 1, 5)
)
_PmmcCtrlColdReset_Type = EkiOnOff
_PmmcCtrlColdReset_Object = MibScalar
pmmcCtrlColdReset = _PmmcCtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 6, 1, 5, 2),
    _PmmcCtrlColdReset_Type()
)
pmmcCtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmmcCtrlColdReset.setStatus("current")
_PmmcCtrlWarmReset_Type = EkiOnOff
_PmmcCtrlWarmReset_Object = MibScalar
pmmcCtrlWarmReset = _PmmcCtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 6, 1, 5, 3),
    _PmmcCtrlWarmReset_Type()
)
pmmcCtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmmcCtrlWarmReset.setStatus("current")
_PmmcCtrlledTest_ObjectIdentity = ObjectIdentity
pmmcCtrlledTest = _PmmcCtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 6, 1, 64)
)
_PmmcCtrlGreenLed_Type = EkiOnOff
_PmmcCtrlGreenLed_Object = MibScalar
pmmcCtrlGreenLed = _PmmcCtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 6, 1, 64, 1),
    _PmmcCtrlGreenLed_Type()
)
pmmcCtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmmcCtrlGreenLed.setStatus("current")
_PmmcCtrlRedLed_Type = EkiOnOff
_PmmcCtrlRedLed_Object = MibScalar
pmmcCtrlRedLed = _PmmcCtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 6, 1, 64, 2),
    _PmmcCtrlRedLed_Type()
)
pmmcCtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmmcCtrlRedLed.setStatus("current")
_PmmcCtrlLedOff_Type = EkiOnOff
_PmmcCtrlLedOff_Object = MibScalar
pmmcCtrlLedOff = _PmmcCtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 6, 1, 64, 3),
    _PmmcCtrlLedOff_Type()
)
pmmcCtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmmcCtrlLedOff.setStatus("current")
_PmmcCtrlClient_ObjectIdentity = ObjectIdentity
pmmcCtrlClient = _PmmcCtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 6, 2)
)
_PmmcCtrlline1TrscvOnoff_ObjectIdentity = ObjectIdentity
pmmcCtrlline1TrscvOnoff = _PmmcCtrlline1TrscvOnoff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 6, 2, 16)
)
_PmmcCtrlLine1TrscvOnoff_Type = EkiOnOff
_PmmcCtrlLine1TrscvOnoff_Object = MibScalar
pmmcCtrlLine1TrscvOnoff = _PmmcCtrlLine1TrscvOnoff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 6, 2, 16, 1),
    _PmmcCtrlLine1TrscvOnoff_Type()
)
pmmcCtrlLine1TrscvOnoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmmcCtrlLine1TrscvOnoff.setStatus("current")
_PmmcCtrlLine_ObjectIdentity = ObjectIdentity
pmmcCtrlLine = _PmmcCtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 6, 3)
)
_PmmcCtrlline2TrscvOnoff_ObjectIdentity = ObjectIdentity
pmmcCtrlline2TrscvOnoff = _PmmcCtrlline2TrscvOnoff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 6, 3, 24)
)
_PmmcCtrlLine2TrscvOnoff_Type = EkiOnOff
_PmmcCtrlLine2TrscvOnoff_Object = MibScalar
pmmcCtrlLine2TrscvOnoff = _PmmcCtrlLine2TrscvOnoff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 6, 3, 24, 1),
    _PmmcCtrlLine2TrscvOnoff_Type()
)
pmmcCtrlLine2TrscvOnoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmmcCtrlLine2TrscvOnoff.setStatus("current")
_Pmmcri_ObjectIdentity = ObjectIdentity
pmmcri = _Pmmcri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 7)
)
_PmmcRinvReloadInventory_Type = EkiOnOff
_PmmcRinvReloadInventory_Object = MibScalar
pmmcRinvReloadInventory = _PmmcRinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 7, 2),
    _PmmcRinvReloadInventory_Type()
)
pmmcRinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmmcRinvReloadInventory.setStatus("current")
_PmmcRinvHwPlatform_Type = DisplayString
_PmmcRinvHwPlatform_Object = MibScalar
pmmcRinvHwPlatform = _PmmcRinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 7, 4),
    _PmmcRinvHwPlatform_Type()
)
pmmcRinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcRinvHwPlatform.setStatus("current")
_PmmcRinvSwPlatform_Type = DisplayString
_PmmcRinvSwPlatform_Object = MibScalar
pmmcRinvSwPlatform = _PmmcRinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 7, 5),
    _PmmcRinvSwPlatform_Type()
)
pmmcRinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcRinvSwPlatform.setStatus("current")
_PmmcRinvLine1SFP_Type = DisplayString
_PmmcRinvLine1SFP_Object = MibScalar
pmmcRinvLine1SFP = _PmmcRinvLine1SFP_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 7, 6),
    _PmmcRinvLine1SFP_Type()
)
pmmcRinvLine1SFP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcRinvLine1SFP.setStatus("current")
_PmmcRinvLine2SFP_Type = DisplayString
_PmmcRinvLine2SFP_Object = MibScalar
pmmcRinvLine2SFP = _PmmcRinvLine2SFP_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 7, 7),
    _PmmcRinvLine2SFP_Type()
)
pmmcRinvLine2SFP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcRinvLine2SFP.setStatus("current")
_PmmcConfig_ObjectIdentity = ObjectIdentity
pmmcConfig = _PmmcConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 9)
)
_PmmcCfgLsd_ObjectIdentity = ObjectIdentity
pmmcCfgLsd = _PmmcCfgLsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 9, 1)
)
_PmmctableclientLsd_ObjectIdentity = ObjectIdentity
pmmctableclientLsd = _PmmctableclientLsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 9, 1, 1)
)


class _PmmcCfglsdMode_Type(Unsigned32):
    """Custom type pmmcCfglsdMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmmcCfglsdMode_Type.__name__ = "Unsigned32"
_PmmcCfglsdMode_Object = MibScalar
pmmcCfglsdMode = _PmmcCfglsdMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 9, 1, 1, 2),
    _PmmcCfglsdMode_Type()
)
pmmcCfglsdMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmmcCfglsdMode.setStatus("current")


class _PmmcCfgline1AccessioCtrb_Type(Unsigned32):
    """Custom type pmmcCfgline1AccessioCtrb based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmmcCfgline1AccessioCtrb_Type.__name__ = "Unsigned32"
_PmmcCfgline1AccessioCtrb_Object = MibScalar
pmmcCfgline1AccessioCtrb = _PmmcCfgline1AccessioCtrb_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 9, 1, 1, 3),
    _PmmcCfgline1AccessioCtrb_Type()
)
pmmcCfgline1AccessioCtrb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmmcCfgline1AccessioCtrb.setStatus("current")


class _PmmcCfgline1CdrCtrb_Type(Unsigned32):
    """Custom type pmmcCfgline1CdrCtrb based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmmcCfgline1CdrCtrb_Type.__name__ = "Unsigned32"
_PmmcCfgline1CdrCtrb_Object = MibScalar
pmmcCfgline1CdrCtrb = _PmmcCfgline1CdrCtrb_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 9, 1, 1, 4),
    _PmmcCfgline1CdrCtrb_Type()
)
pmmcCfgline1CdrCtrb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmmcCfgline1CdrCtrb.setStatus("current")


class _PmmcCfgline2AccessioCtrb_Type(Unsigned32):
    """Custom type pmmcCfgline2AccessioCtrb based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmmcCfgline2AccessioCtrb_Type.__name__ = "Unsigned32"
_PmmcCfgline2AccessioCtrb_Object = MibScalar
pmmcCfgline2AccessioCtrb = _PmmcCfgline2AccessioCtrb_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 9, 1, 1, 5),
    _PmmcCfgline2AccessioCtrb_Type()
)
pmmcCfgline2AccessioCtrb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmmcCfgline2AccessioCtrb.setStatus("current")


class _PmmcCfgline2CdrCtrb_Type(Unsigned32):
    """Custom type pmmcCfgline2CdrCtrb based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmmcCfgline2CdrCtrb_Type.__name__ = "Unsigned32"
_PmmcCfgline2CdrCtrb_Object = MibScalar
pmmcCfgline2CdrCtrb = _PmmcCfgline2CdrCtrb_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 9, 1, 1, 6),
    _PmmcCfgline2CdrCtrb_Type()
)
pmmcCfgline2CdrCtrb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmmcCfgline2CdrCtrb.setStatus("current")
_PmmcCfgStartUp_ObjectIdentity = ObjectIdentity
pmmcCfgStartUp = _PmmcCfgStartUp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 9, 2)
)
_PmmctableclientStartup_ObjectIdentity = ObjectIdentity
pmmctableclientStartup = _PmmctableclientStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 9, 2, 1)
)


class _PmmcCfgline1TrscvCtrl_Type(Unsigned32):
    """Custom type pmmcCfgline1TrscvCtrl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmmcCfgline1TrscvCtrl_Type.__name__ = "Unsigned32"
_PmmcCfgline1TrscvCtrl_Object = MibScalar
pmmcCfgline1TrscvCtrl = _PmmcCfgline1TrscvCtrl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 9, 2, 1, 2),
    _PmmcCfgline1TrscvCtrl_Type()
)
pmmcCfgline1TrscvCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmmcCfgline1TrscvCtrl.setStatus("current")
_PmmctablelineStartup_ObjectIdentity = ObjectIdentity
pmmctablelineStartup = _PmmctablelineStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 9, 2, 2)
)


class _PmmcCfgline2TrscvCtrl_Type(Unsigned32):
    """Custom type pmmcCfgline2TrscvCtrl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmmcCfgline2TrscvCtrl_Type.__name__ = "Unsigned32"
_PmmcCfgline2TrscvCtrl_Object = MibScalar
pmmcCfgline2TrscvCtrl = _PmmcCfgline2TrscvCtrl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 9, 2, 2, 2),
    _PmmcCfgline2TrscvCtrl_Type()
)
pmmcCfgline2TrscvCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmmcCfgline2TrscvCtrl.setStatus("current")


class _PmmcCfgbitrateSelect_Type(Unsigned32):
    """Custom type pmmcCfgbitrateSelect based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmmcCfgbitrateSelect_Type.__name__ = "Unsigned32"
_PmmcCfgbitrateSelect_Object = MibScalar
pmmcCfgbitrateSelect = _PmmcCfgbitrateSelect_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 9, 2, 2, 18),
    _PmmcCfgbitrateSelect_Type()
)
pmmcCfgbitrateSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmmcCfgbitrateSelect.setStatus("current")
_PmmcCfgLabels_ObjectIdentity = ObjectIdentity
pmmcCfgLabels = _PmmcCfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 9, 3)
)
_PmmcCfgLabelclientTable_Object = MibTable
pmmcCfgLabelclientTable = _PmmcCfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 9, 3, 1)
)
if mibBuilder.loadTexts:
    pmmcCfgLabelclientTable.setStatus("current")
_PmmcCfgLabelclientEntry_Object = MibTableRow
pmmcCfgLabelclientEntry = _PmmcCfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 9, 3, 1, 1)
)
pmmcCfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-PmMC-MIB", "pmmcCfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pmmcCfgLabelclientEntry.setStatus("current")


class _PmmcCfgLabelclientIndex_Type(Integer32):
    """Custom type pmmcCfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmmcCfgLabelclientIndex_Type.__name__ = "Integer32"
_PmmcCfgLabelclientIndex_Object = MibTableColumn
pmmcCfgLabelclientIndex = _PmmcCfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 9, 3, 1, 1, 1),
    _PmmcCfgLabelclientIndex_Type()
)
pmmcCfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcCfgLabelclientIndex.setStatus("current")


class _PmmcCfgLabelclientPortn_Type(DisplayString):
    """Custom type pmmcCfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PmmcCfgLabelclientPortn_Type.__name__ = "DisplayString"
_PmmcCfgLabelclientPortn_Object = MibTableColumn
pmmcCfgLabelclientPortn = _PmmcCfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 9, 3, 1, 1, 3),
    _PmmcCfgLabelclientPortn_Type()
)
pmmcCfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmmcCfgLabelclientPortn.setStatus("current")
_PmmcCfgLabellineTable_Object = MibTable
pmmcCfgLabellineTable = _PmmcCfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 9, 3, 2)
)
if mibBuilder.loadTexts:
    pmmcCfgLabellineTable.setStatus("current")
_PmmcCfgLabellineEntry_Object = MibTableRow
pmmcCfgLabellineEntry = _PmmcCfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 9, 3, 2, 1)
)
pmmcCfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-PmMC-MIB", "pmmcCfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pmmcCfgLabellineEntry.setStatus("current")


class _PmmcCfgLabellineIndex_Type(Integer32):
    """Custom type pmmcCfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmmcCfgLabellineIndex_Type.__name__ = "Integer32"
_PmmcCfgLabellineIndex_Object = MibTableColumn
pmmcCfgLabellineIndex = _PmmcCfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 9, 3, 2, 1, 1),
    _PmmcCfgLabellineIndex_Type()
)
pmmcCfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmcCfgLabellineIndex.setStatus("current")


class _PmmcCfgLabellinePortn_Type(DisplayString):
    """Custom type pmmcCfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PmmcCfgLabellinePortn_Type.__name__ = "DisplayString"
_PmmcCfgLabellinePortn_Object = MibTableColumn
pmmcCfgLabellinePortn = _PmmcCfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 9, 3, 2, 1, 3),
    _PmmcCfgLabellinePortn_Type()
)
pmmcCfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmmcCfgLabellinePortn.setStatus("current")
_PmmcCfgWriteConfiguration_Type = EkiOnOff
_PmmcCfgWriteConfiguration_Object = MibScalar
pmmcCfgWriteConfiguration = _PmmcCfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 9, 257),
    _PmmcCfgWriteConfiguration_Type()
)
pmmcCfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmmcCfgWriteConfiguration.setStatus("current")
_Pmmctraps_ObjectIdentity = ObjectIdentity
pmmctraps = _Pmmctraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 21, 10)
)


class _PmmctrapBoardNumber_Type(Integer32):
    """Custom type pmmctrapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_PmmctrapBoardNumber_Type.__name__ = "Integer32"
_PmmctrapBoardNumber_Object = MibScalar
pmmctrapBoardNumber = _PmmctrapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 21, 10, 4),
    _PmmctrapBoardNumber_Type()
)
pmmctrapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmmctrapBoardNumber.setStatus("current")

# Managed Objects groups


# Notification objects

pmmcLine1TrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 21, 10, 30)
)
pmmcLine1TrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-PmMC-MIB", "pmmcAlmLine1TrscvDdmWarning"),
        ("EKINOPS-PmMC-MIB", "pmmctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmmcLine1TrapNotUrgentGoesOn.setStatus(
        "current"
    )

pmmcLine1TrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 21, 10, 31)
)
pmmcLine1TrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-PmMC-MIB", "pmmcAlmLine1TrscvDdmWarning"),
        ("EKINOPS-PmMC-MIB", "pmmctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmmcLine1TrapNotUrgentGoesOff.setStatus(
        "current"
    )

pmmcLine1TrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 21, 10, 32)
)
pmmcLine1TrapUrgentGoesOn.setObjects(
      *(("EKINOPS-PmMC-MIB", "pmmcAlmLine1TrscvDdmAlm"),
        ("EKINOPS-PmMC-MIB", "pmmctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmmcLine1TrapUrgentGoesOn.setStatus(
        "current"
    )

pmmcLine1TrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 21, 10, 33)
)
pmmcLine1TrapUrgentGoesOff.setObjects(
      *(("EKINOPS-PmMC-MIB", "pmmcAlmLine1TrscvDdmAlm"),
        ("EKINOPS-PmMC-MIB", "pmmctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmmcLine1TrapUrgentGoesOff.setStatus(
        "current"
    )

pmmcLine1TrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 21, 10, 34)
)
pmmcLine1TrapCritGoesOn.setObjects(
      *(("EKINOPS-PmMC-MIB", "pmmcAlmLine1Fail"),
        ("EKINOPS-PmMC-MIB", "pmmcAlmLine1HwFail"),
        ("EKINOPS-PmMC-MIB", "pmmctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmmcLine1TrapCritGoesOn.setStatus(
        "current"
    )

pmmcLine1TrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 21, 10, 35)
)
pmmcLine1TrapCritGoesOff.setObjects(
      *(("EKINOPS-PmMC-MIB", "pmmcAlmLine1Fail"),
        ("EKINOPS-PmMC-MIB", "pmmcAlmLine1HwFail"),
        ("EKINOPS-PmMC-MIB", "pmmctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmmcLine1TrapCritGoesOff.setStatus(
        "current"
    )

pmmcLine2NotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 21, 10, 40)
)
pmmcLine2NotUrgentGoesOn.setObjects(
      *(("EKINOPS-PmMC-MIB", "pmmcAlmLine2TrscvDdmWarning"),
        ("EKINOPS-PmMC-MIB", "pmmctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmmcLine2NotUrgentGoesOn.setStatus(
        "current"
    )

pmmcLine2NotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 21, 10, 41)
)
pmmcLine2NotUrgentGoesOff.setObjects(
      *(("EKINOPS-PmMC-MIB", "pmmcAlmLine2TrscvDdmWarning"),
        ("EKINOPS-PmMC-MIB", "pmmctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmmcLine2NotUrgentGoesOff.setStatus(
        "current"
    )

pmmcLine2UrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 21, 10, 42)
)
pmmcLine2UrgentGoesOn.setObjects(
      *(("EKINOPS-PmMC-MIB", "pmmcAlmLine2TrscvDdmAlm"),
        ("EKINOPS-PmMC-MIB", "pmmctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmmcLine2UrgentGoesOn.setStatus(
        "current"
    )

pmmcLine2UrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 21, 10, 43)
)
pmmcLine2UrgentGoesOff.setObjects(
      *(("EKINOPS-PmMC-MIB", "pmmcAlmLine2TrscvDdmAlm"),
        ("EKINOPS-PmMC-MIB", "pmmctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmmcLine2UrgentGoesOff.setStatus(
        "current"
    )

pmmcLine2CritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 21, 10, 44)
)
pmmcLine2CritGoesOn.setObjects(
      *(("EKINOPS-PmMC-MIB", "pmmcAlmLine2Fail"),
        ("EKINOPS-PmMC-MIB", "pmmcAlmLine2HwFail"),
        ("EKINOPS-PmMC-MIB", "pmmctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmmcLine2CritGoesOn.setStatus(
        "current"
    )

pmmcLine2CritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 21, 10, 45)
)
pmmcLine2CritGoesOff.setObjects(
      *(("EKINOPS-PmMC-MIB", "pmmcAlmLine2Fail"),
        ("EKINOPS-PmMC-MIB", "pmmcAlmLine2HwFail"),
        ("EKINOPS-PmMC-MIB", "pmmctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmmcLine2CritGoesOff.setStatus(
        "current"
    )

pmmcPowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 21, 10, 50)
)
pmmcPowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-PmMC-MIB", "pmmcAlmDefFuseB"),
        ("EKINOPS-PmMC-MIB", "pmmcAlmDefFuseA"),
        ("EKINOPS-PmMC-MIB", "pmmctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmmcPowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pmmcPowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 21, 10, 51)
)
pmmcPowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-PmMC-MIB", "pmmcAlmDefFuseB"),
        ("EKINOPS-PmMC-MIB", "pmmcAlmDefFuseA"),
        ("EKINOPS-PmMC-MIB", "pmmctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmmcPowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-PmMC-MIB",
    **{"PmmcBitRate": PmmcBitRate,
       "modulePmMC": modulePmMC,
       "pmmcalarms": pmmcalarms,
       "pmmcAlmOther": pmmcAlmOther,
       "pmmcAlmOtherNurg": pmmcAlmOtherNurg,
       "pmmcAlmOtherUrg": pmmcAlmOtherUrg,
       "pmmcAlmOtherCrit": pmmcAlmOtherCrit,
       "pmmcAlmsynthAlm0": pmmcAlmsynthAlm0,
       "pmmcAlmModuleGlobFailure": pmmcAlmModuleGlobFailure,
       "pmmcAlmSynUnlock": pmmcAlmSynUnlock,
       "pmmcAlmDefFuseA": pmmcAlmDefFuseA,
       "pmmcAlmDefFuseB": pmmcAlmDefFuseB,
       "pmmcAlmClient": pmmcAlmClient,
       "pmmcAlmClientNurg": pmmcAlmClientNurg,
       "pmmcAlmline1TrscvWarnDdm": pmmcAlmline1TrscvWarnDdm,
       "pmmcAlmLine1TxPwLowWng": pmmcAlmLine1TxPwLowWng,
       "pmmcAlmLine1TxPwrHighWng": pmmcAlmLine1TxPwrHighWng,
       "pmmcAlmLine1TxBiasLowWng": pmmcAlmLine1TxBiasLowWng,
       "pmmcAlmLine1TxBiasHighWng": pmmcAlmLine1TxBiasHighWng,
       "pmmcAlmLine1VccLowWng": pmmcAlmLine1VccLowWng,
       "pmmcAlmLine1VccHighWng": pmmcAlmLine1VccHighWng,
       "pmmcAlmLine1TempLowWng": pmmcAlmLine1TempLowWng,
       "pmmcAlmLine1TempHighWng": pmmcAlmLine1TempHighWng,
       "pmmcAlmLine1RxPwrLowWng": pmmcAlmLine1RxPwrLowWng,
       "pmmcAlmLine1RxPwrHighWng": pmmcAlmLine1RxPwrHighWng,
       "pmmcAlmline1CdrAlm": pmmcAlmline1CdrAlm,
       "pmmcAlmLine1CdrLossofsignal": pmmcAlmLine1CdrLossofsignal,
       "pmmcAlmLine1CdrLossoflock": pmmcAlmLine1CdrLossoflock,
       "pmmcAlmLine1CdrRefAbsent": pmmcAlmLine1CdrRefAbsent,
       "pmmcAlmClientUrg": pmmcAlmClientUrg,
       "pmmcAlmline1TrscvAlmDdm": pmmcAlmline1TrscvAlmDdm,
       "pmmcAlmLine1TxPwrLowAla": pmmcAlmLine1TxPwrLowAla,
       "pmmcAlmLine1TxPwrHighAla": pmmcAlmLine1TxPwrHighAla,
       "pmmcAlmLine1TxBiasLowAla": pmmcAlmLine1TxBiasLowAla,
       "pmmcAlmLine1TxBiasHighAla": pmmcAlmLine1TxBiasHighAla,
       "pmmcAlmLine1VccLowAla": pmmcAlmLine1VccLowAla,
       "pmmcAlmLine1VccHighAla": pmmcAlmLine1VccHighAla,
       "pmmcAlmLine1TempLowAla": pmmcAlmLine1TempLowAla,
       "pmmcAlmLine1TempHighAla": pmmcAlmLine1TempHighAla,
       "pmmcAlmLine1RxPwrLowAla": pmmcAlmLine1RxPwrLowAla,
       "pmmcAlmLine1RxPwrHighAla": pmmcAlmLine1RxPwrHighAla,
       "pmmcAlmClientCrit": pmmcAlmClientCrit,
       "pmmcAlmsynthAlm8": pmmcAlmsynthAlm8,
       "pmmcAlmLine1TrscvAbsent": pmmcAlmLine1TrscvAbsent,
       "pmmcAlmLine1TrscvDdmAbsent": pmmcAlmLine1TrscvDdmAbsent,
       "pmmcAlmLine1HwFail": pmmcAlmLine1HwFail,
       "pmmcAlmLine1TrscvLsd": pmmcAlmLine1TrscvLsd,
       "pmmcAlmLine1TrscvDdmWarning": pmmcAlmLine1TrscvDdmWarning,
       "pmmcAlmLine1TrscvDdmAlm": pmmcAlmLine1TrscvDdmAlm,
       "pmmcAlmLine1Fail": pmmcAlmLine1Fail,
       "pmmcAlmline1AccessioAlm": pmmcAlmline1AccessioAlm,
       "pmmcAlmLine1LasFail": pmmcAlmLine1LasFail,
       "pmmcAlmLine1Los": pmmcAlmLine1Los,
       "pmmcAlmLine": pmmcAlmLine,
       "pmmcAlmLineNurg": pmmcAlmLineNurg,
       "pmmcAlmline2TrscvWarnDdm": pmmcAlmline2TrscvWarnDdm,
       "pmmcAlmLine2TxPwLowWng": pmmcAlmLine2TxPwLowWng,
       "pmmcAlmLine2TxPwrHighWng": pmmcAlmLine2TxPwrHighWng,
       "pmmcAlmLine2TxBiasLowWng": pmmcAlmLine2TxBiasLowWng,
       "pmmcAlmLine2TxBiasHighWng": pmmcAlmLine2TxBiasHighWng,
       "pmmcAlmLine2VccLowWng": pmmcAlmLine2VccLowWng,
       "pmmcAlmLine2VccHighWng": pmmcAlmLine2VccHighWng,
       "pmmcAlmLine2TempLowWng": pmmcAlmLine2TempLowWng,
       "pmmcAlmLine2TempHighWng": pmmcAlmLine2TempHighWng,
       "pmmcAlmLine2RxPwrLowWng": pmmcAlmLine2RxPwrLowWng,
       "pmmcAlmLine2RxPwrHighWng": pmmcAlmLine2RxPwrHighWng,
       "pmmcAlmline2CdrAlm": pmmcAlmline2CdrAlm,
       "pmmcAlmLine2CdrLossofsignal": pmmcAlmLine2CdrLossofsignal,
       "pmmcAlmLine2CdrLossoflock": pmmcAlmLine2CdrLossoflock,
       "pmmcAlmLine2CdrRefAbsent": pmmcAlmLine2CdrRefAbsent,
       "pmmcAlmLineUrg": pmmcAlmLineUrg,
       "pmmcAlmline2TrscvAlmDdm": pmmcAlmline2TrscvAlmDdm,
       "pmmcAlmLine2TxPwrLowAla": pmmcAlmLine2TxPwrLowAla,
       "pmmcAlmLine2TxPwrHighAla": pmmcAlmLine2TxPwrHighAla,
       "pmmcAlmLine2TxBiasLowAla": pmmcAlmLine2TxBiasLowAla,
       "pmmcAlmLine2TxBiasHighAla": pmmcAlmLine2TxBiasHighAla,
       "pmmcAlmLine2VccLowAla": pmmcAlmLine2VccLowAla,
       "pmmcAlmLine2VccHighAla": pmmcAlmLine2VccHighAla,
       "pmmcAlmLine2TempLowAla": pmmcAlmLine2TempLowAla,
       "pmmcAlmLine2TempHighAla": pmmcAlmLine2TempHighAla,
       "pmmcAlmLine2RxPwrLowAla": pmmcAlmLine2RxPwrLowAla,
       "pmmcAlmLine2RxPwrHighAla": pmmcAlmLine2RxPwrHighAla,
       "pmmcAlmLineCrit": pmmcAlmLineCrit,
       "pmmcAlmsynthAlm7": pmmcAlmsynthAlm7,
       "pmmcAlmLine2TrscvAbsent": pmmcAlmLine2TrscvAbsent,
       "pmmcAlmLine2TrscvDdmAbsent": pmmcAlmLine2TrscvDdmAbsent,
       "pmmcAlmLine2HwFail": pmmcAlmLine2HwFail,
       "pmmcAlmLine2TrscvLsd": pmmcAlmLine2TrscvLsd,
       "pmmcAlmLine2TrscvDdmWarning": pmmcAlmLine2TrscvDdmWarning,
       "pmmcAlmLine2TrscvDdmAlm": pmmcAlmLine2TrscvDdmAlm,
       "pmmcAlmLine2Fail": pmmcAlmLine2Fail,
       "pmmcAlmline2AccessioAlm": pmmcAlmline2AccessioAlm,
       "pmmcAlmLine2LasFail": pmmcAlmLine2LasFail,
       "pmmcAlmLine2Los": pmmcAlmLine2Los,
       "pmmcmeasures": pmmcmeasures,
       "pmmcMesrOther": pmmcMesrOther,
       "pmmcMesrClient": pmmcMesrClient,
       "pmmcMesrline1Temperature": pmmcMesrline1Temperature,
       "pmmcMesrline1Volt": pmmcMesrline1Volt,
       "pmmcMesrline1TxBias": pmmcMesrline1TxBias,
       "pmmcMesrline1TxPower": pmmcMesrline1TxPower,
       "pmmcMesrline1RxPower": pmmcMesrline1RxPower,
       "pmmcMesrLine": pmmcMesrLine,
       "pmmcMesrline2Temperature": pmmcMesrline2Temperature,
       "pmmcMesrline2Volt": pmmcMesrline2Volt,
       "pmmcMesrline2TxBias": pmmcMesrline2TxBias,
       "pmmcMesrline2TxPower": pmmcMesrline2TxPower,
       "pmmcMesrline2RxPower": pmmcMesrline2RxPower,
       "pmmccontrolsWrite": pmmccontrolsWrite,
       "pmmcCtrlOther": pmmcCtrlOther,
       "pmmcCtrlsynth0": pmmcCtrlsynth0,
       "pmmcCtrlConfLoad": pmmcCtrlConfLoad,
       "pmmcCtrlConfFlash": pmmcCtrlConfFlash,
       "pmmcCtrlConfClear": pmmcCtrlConfClear,
       "pmmcCtrlsynth4": pmmcCtrlsynth4,
       "pmmcCtrlCorrelatOn": pmmcCtrlCorrelatOn,
       "pmmcCtrlCorrelatOff": pmmcCtrlCorrelatOff,
       "pmmcCtrlswMgnt": pmmcCtrlswMgnt,
       "pmmcCtrlColdReset": pmmcCtrlColdReset,
       "pmmcCtrlWarmReset": pmmcCtrlWarmReset,
       "pmmcCtrlledTest": pmmcCtrlledTest,
       "pmmcCtrlGreenLed": pmmcCtrlGreenLed,
       "pmmcCtrlRedLed": pmmcCtrlRedLed,
       "pmmcCtrlLedOff": pmmcCtrlLedOff,
       "pmmcCtrlClient": pmmcCtrlClient,
       "pmmcCtrlline1TrscvOnoff": pmmcCtrlline1TrscvOnoff,
       "pmmcCtrlLine1TrscvOnoff": pmmcCtrlLine1TrscvOnoff,
       "pmmcCtrlLine": pmmcCtrlLine,
       "pmmcCtrlline2TrscvOnoff": pmmcCtrlline2TrscvOnoff,
       "pmmcCtrlLine2TrscvOnoff": pmmcCtrlLine2TrscvOnoff,
       "pmmcri": pmmcri,
       "pmmcRinvReloadInventory": pmmcRinvReloadInventory,
       "pmmcRinvHwPlatform": pmmcRinvHwPlatform,
       "pmmcRinvSwPlatform": pmmcRinvSwPlatform,
       "pmmcRinvLine1SFP": pmmcRinvLine1SFP,
       "pmmcRinvLine2SFP": pmmcRinvLine2SFP,
       "pmmcConfig": pmmcConfig,
       "pmmcCfgLsd": pmmcCfgLsd,
       "pmmctableclientLsd": pmmctableclientLsd,
       "pmmcCfglsdMode": pmmcCfglsdMode,
       "pmmcCfgline1AccessioCtrb": pmmcCfgline1AccessioCtrb,
       "pmmcCfgline1CdrCtrb": pmmcCfgline1CdrCtrb,
       "pmmcCfgline2AccessioCtrb": pmmcCfgline2AccessioCtrb,
       "pmmcCfgline2CdrCtrb": pmmcCfgline2CdrCtrb,
       "pmmcCfgStartUp": pmmcCfgStartUp,
       "pmmctableclientStartup": pmmctableclientStartup,
       "pmmcCfgline1TrscvCtrl": pmmcCfgline1TrscvCtrl,
       "pmmctablelineStartup": pmmctablelineStartup,
       "pmmcCfgline2TrscvCtrl": pmmcCfgline2TrscvCtrl,
       "pmmcCfgbitrateSelect": pmmcCfgbitrateSelect,
       "pmmcCfgLabels": pmmcCfgLabels,
       "pmmcCfgLabelclientTable": pmmcCfgLabelclientTable,
       "pmmcCfgLabelclientEntry": pmmcCfgLabelclientEntry,
       "pmmcCfgLabelclientIndex": pmmcCfgLabelclientIndex,
       "pmmcCfgLabelclientPortn": pmmcCfgLabelclientPortn,
       "pmmcCfgLabellineTable": pmmcCfgLabellineTable,
       "pmmcCfgLabellineEntry": pmmcCfgLabellineEntry,
       "pmmcCfgLabellineIndex": pmmcCfgLabellineIndex,
       "pmmcCfgLabellinePortn": pmmcCfgLabellinePortn,
       "pmmcCfgWriteConfiguration": pmmcCfgWriteConfiguration,
       "pmmctraps": pmmctraps,
       "pmmctrapBoardNumber": pmmctrapBoardNumber,
       "pmmcLine1TrapNotUrgentGoesOn": pmmcLine1TrapNotUrgentGoesOn,
       "pmmcLine1TrapNotUrgentGoesOff": pmmcLine1TrapNotUrgentGoesOff,
       "pmmcLine1TrapUrgentGoesOn": pmmcLine1TrapUrgentGoesOn,
       "pmmcLine1TrapUrgentGoesOff": pmmcLine1TrapUrgentGoesOff,
       "pmmcLine1TrapCritGoesOn": pmmcLine1TrapCritGoesOn,
       "pmmcLine1TrapCritGoesOff": pmmcLine1TrapCritGoesOff,
       "pmmcLine2NotUrgentGoesOn": pmmcLine2NotUrgentGoesOn,
       "pmmcLine2NotUrgentGoesOff": pmmcLine2NotUrgentGoesOff,
       "pmmcLine2UrgentGoesOn": pmmcLine2UrgentGoesOn,
       "pmmcLine2UrgentGoesOff": pmmcLine2UrgentGoesOff,
       "pmmcLine2CritGoesOn": pmmcLine2CritGoesOn,
       "pmmcLine2CritGoesOff": pmmcLine2CritGoesOff,
       "pmmcPowerTrapUrgentGoesOn": pmmcPowerTrapUrgentGoesOn,
       "pmmcPowerTrapUrgentGoesOff": pmmcPowerTrapUrgentGoesOff}
)
