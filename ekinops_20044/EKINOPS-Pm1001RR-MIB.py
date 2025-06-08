# SNMP MIB module (EKINOPS-Pm1001RR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Pm1001RR-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 12:01:47 2025
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

modulePm1001RR = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8)
)
if mibBuilder.loadTexts:
    modulePm1001RR.setRevisions(
        ("2005-12-13 00:00",
         "2007-07-02 00:00",
         "2007-08-28 00:00",
         "2007-11-21 00:00",
         "2008-02-13 00:00",
         "2008-12-04 00:00",
         "2009-06-11 00:00",
         "2010-01-28 00:00",
         "2010-02-23 00:00",
         "2010-03-09 00:00",
         "2010-11-03 00:00",
         "2012-07-04 00:00",
         "2014-03-25 00:00",
         "2015-01-14 00:00",
         "2015-01-14 00:00",
         "2016-05-23 00:00",
         "2016-06-07 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Pm1001rrBitRate(TextualConvention, Integer32):
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("rateOC192", 0),
          ("rate10GBELAN", 1),
          ("rate10GBEWAN", 2),
          ("rate10GFC", 3),
          ("rate10FECG975", 4),
          ("rate10FECG709", 5),
          ("rate10DYNAFEC", 6))
    )



class Pm1001rrOtxMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("otx80mode", 1),
          ("otx60mode", 2),
          ("otxadjustmode", 4))
    )



class Pm1001rrOtxGrid(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(50,
              100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("otxgrid50", 50),
          ("otxgrid100", 100),
          ("otxgrid200", 200))
    )



class Pm1001rrAdjustValue(TextualConvention, Integer32):
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
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("otxadjustvalue0", 0),
          ("otxadjustvalue1", 1),
          ("otxadjustvalue2", 2),
          ("otxadjustvalue3", 3),
          ("otxadjustvalue4", 4),
          ("otxadjustvalue5", 5),
          ("otxadjustvalue6", 6),
          ("otxadjustvalue7", 7),
          ("otxadjustvalue8", 8),
          ("otxadjustvalue9", 9),
          ("otxadjustvalue10", 10))
    )



class Pm1001rrOtxChannel(TextualConvention, Integer32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Pm1001rralarms_ObjectIdentity = ObjectIdentity
pm1001rralarms = _Pm1001rralarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2)
)
_Pm1001rrAlmOther_ObjectIdentity = ObjectIdentity
pm1001rrAlmOther = _Pm1001rrAlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 1)
)
_Pm1001rrAlmOtherNurg_ObjectIdentity = ObjectIdentity
pm1001rrAlmOtherNurg = _Pm1001rrAlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 1, 1)
)
_Pm1001rrAlmOtherUrg_ObjectIdentity = ObjectIdentity
pm1001rrAlmOtherUrg = _Pm1001rrAlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 1, 2)
)
_Pm1001rrAlmOtherCrit_ObjectIdentity = ObjectIdentity
pm1001rrAlmOtherCrit = _Pm1001rrAlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 1, 3)
)
_Pm1001rrAlmsynthAlm0_ObjectIdentity = ObjectIdentity
pm1001rrAlmsynthAlm0 = _Pm1001rrAlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 1, 3, 0)
)
_Pm1001rrAlmModuleGlobFailure_Type = EkiOnOff
_Pm1001rrAlmModuleGlobFailure_Object = MibScalar
pm1001rrAlmModuleGlobFailure = _Pm1001rrAlmModuleGlobFailure_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 1, 3, 0, 9),
    _Pm1001rrAlmModuleGlobFailure_Type()
)
pm1001rrAlmModuleGlobFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmModuleGlobFailure.setStatus("current")
_Pm1001rrAlmDefFuseA_Type = EkiOnOff
_Pm1001rrAlmDefFuseA_Object = MibScalar
pm1001rrAlmDefFuseA = _Pm1001rrAlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 1, 3, 0, 15),
    _Pm1001rrAlmDefFuseA_Type()
)
pm1001rrAlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmDefFuseA.setStatus("current")
_Pm1001rrAlmDefFuseB_Type = EkiOnOff
_Pm1001rrAlmDefFuseB_Object = MibScalar
pm1001rrAlmDefFuseB = _Pm1001rrAlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 1, 3, 0, 16),
    _Pm1001rrAlmDefFuseB_Type()
)
pm1001rrAlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmDefFuseB.setStatus("current")
_Pm1001rrAlmClient_ObjectIdentity = ObjectIdentity
pm1001rrAlmClient = _Pm1001rrAlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2)
)
_Pm1001rrAlmClientNurg_ObjectIdentity = ObjectIdentity
pm1001rrAlmClientNurg = _Pm1001rrAlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 1)
)
_Pm1001rrAlmclientXfpWarnings_ObjectIdentity = ObjectIdentity
pm1001rrAlmclientXfpWarnings = _Pm1001rrAlmclientXfpWarnings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 1, 17)
)
_Pm1001rrAlmClientTxPwrLowWng_Type = EkiOnOff
_Pm1001rrAlmClientTxPwrLowWng_Object = MibScalar
pm1001rrAlmClientTxPwrLowWng = _Pm1001rrAlmClientTxPwrLowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 1, 17, 1),
    _Pm1001rrAlmClientTxPwrLowWng_Type()
)
pm1001rrAlmClientTxPwrLowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientTxPwrLowWng.setStatus("current")
_Pm1001rrAlmClientTxPwrHighWng_Type = EkiOnOff
_Pm1001rrAlmClientTxPwrHighWng_Object = MibScalar
pm1001rrAlmClientTxPwrHighWng = _Pm1001rrAlmClientTxPwrHighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 1, 17, 2),
    _Pm1001rrAlmClientTxPwrHighWng_Type()
)
pm1001rrAlmClientTxPwrHighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientTxPwrHighWng.setStatus("current")
_Pm1001rrAlmClientTxBiasLowWng_Type = EkiOnOff
_Pm1001rrAlmClientTxBiasLowWng_Object = MibScalar
pm1001rrAlmClientTxBiasLowWng = _Pm1001rrAlmClientTxBiasLowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 1, 17, 3),
    _Pm1001rrAlmClientTxBiasLowWng_Type()
)
pm1001rrAlmClientTxBiasLowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientTxBiasLowWng.setStatus("current")
_Pm1001rrAlmClientTxBiasHighWng_Type = EkiOnOff
_Pm1001rrAlmClientTxBiasHighWng_Object = MibScalar
pm1001rrAlmClientTxBiasHighWng = _Pm1001rrAlmClientTxBiasHighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 1, 17, 4),
    _Pm1001rrAlmClientTxBiasHighWng_Type()
)
pm1001rrAlmClientTxBiasHighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientTxBiasHighWng.setStatus("current")
_Pm1001rrAlmClientTempLowWng_Type = EkiOnOff
_Pm1001rrAlmClientTempLowWng_Object = MibScalar
pm1001rrAlmClientTempLowWng = _Pm1001rrAlmClientTempLowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 1, 17, 7),
    _Pm1001rrAlmClientTempLowWng_Type()
)
pm1001rrAlmClientTempLowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientTempLowWng.setStatus("current")
_Pm1001rrAlmClientTempHighWng_Type = EkiOnOff
_Pm1001rrAlmClientTempHighWng_Object = MibScalar
pm1001rrAlmClientTempHighWng = _Pm1001rrAlmClientTempHighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 1, 17, 8),
    _Pm1001rrAlmClientTempHighWng_Type()
)
pm1001rrAlmClientTempHighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientTempHighWng.setStatus("current")
_Pm1001rrAlmClientRxPwrLowWng_Type = EkiOnOff
_Pm1001rrAlmClientRxPwrLowWng_Object = MibScalar
pm1001rrAlmClientRxPwrLowWng = _Pm1001rrAlmClientRxPwrLowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 1, 17, 15),
    _Pm1001rrAlmClientRxPwrLowWng_Type()
)
pm1001rrAlmClientRxPwrLowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientRxPwrLowWng.setStatus("current")
_Pm1001rrAlmClientRxPwrHighWng_Type = EkiOnOff
_Pm1001rrAlmClientRxPwrHighWng_Object = MibScalar
pm1001rrAlmClientRxPwrHighWng = _Pm1001rrAlmClientRxPwrHighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 1, 17, 16),
    _Pm1001rrAlmClientRxPwrHighWng_Type()
)
pm1001rrAlmClientRxPwrHighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientRxPwrHighWng.setStatus("current")
_Pm1001rrAlmclientOtxTlhWarnings_ObjectIdentity = ObjectIdentity
pm1001rrAlmclientOtxTlhWarnings = _Pm1001rrAlmclientOtxTlhWarnings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 1, 23)
)
_Pm1001rrAlmClientModulatorAgingHighWarning_Type = EkiOnOff
_Pm1001rrAlmClientModulatorAgingHighWarning_Object = MibScalar
pm1001rrAlmClientModulatorAgingHighWarning = _Pm1001rrAlmClientModulatorAgingHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 1, 23, 5),
    _Pm1001rrAlmClientModulatorAgingHighWarning_Type()
)
pm1001rrAlmClientModulatorAgingHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientModulatorAgingHighWarning.setStatus("current")
_Pm1001rrAlmClientAgingHighWarning_Type = EkiOnOff
_Pm1001rrAlmClientAgingHighWarning_Object = MibScalar
pm1001rrAlmClientAgingHighWarning = _Pm1001rrAlmClientAgingHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 1, 23, 6),
    _Pm1001rrAlmClientAgingHighWarning_Type()
)
pm1001rrAlmClientAgingHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientAgingHighWarning.setStatus("current")
_Pm1001rrAlmClientFreqDevHighWarning_Type = EkiOnOff
_Pm1001rrAlmClientFreqDevHighWarning_Object = MibScalar
pm1001rrAlmClientFreqDevHighWarning = _Pm1001rrAlmClientFreqDevHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 1, 23, 12),
    _Pm1001rrAlmClientFreqDevHighWarning_Type()
)
pm1001rrAlmClientFreqDevHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientFreqDevHighWarning.setStatus("current")
_Pm1001rrAlmClientLaserTempHighWarning_Type = EkiOnOff
_Pm1001rrAlmClientLaserTempHighWarning_Object = MibScalar
pm1001rrAlmClientLaserTempHighWarning = _Pm1001rrAlmClientLaserTempHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 1, 23, 14),
    _Pm1001rrAlmClientLaserTempHighWarning_Type()
)
pm1001rrAlmClientLaserTempHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientLaserTempHighWarning.setStatus("current")
_Pm1001rrAlmClientUrg_ObjectIdentity = ObjectIdentity
pm1001rrAlmClientUrg = _Pm1001rrAlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 2)
)
_Pm1001rrAlmclientXfpAlarm1_ObjectIdentity = ObjectIdentity
pm1001rrAlmclientXfpAlarm1 = _Pm1001rrAlmclientXfpAlarm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 2, 16)
)
_Pm1001rrAlmClientTxPwrLowAla_Type = EkiOnOff
_Pm1001rrAlmClientTxPwrLowAla_Object = MibScalar
pm1001rrAlmClientTxPwrLowAla = _Pm1001rrAlmClientTxPwrLowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 2, 16, 1),
    _Pm1001rrAlmClientTxPwrLowAla_Type()
)
pm1001rrAlmClientTxPwrLowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientTxPwrLowAla.setStatus("current")
_Pm1001rrAlmClientTxPwrHighAla_Type = EkiOnOff
_Pm1001rrAlmClientTxPwrHighAla_Object = MibScalar
pm1001rrAlmClientTxPwrHighAla = _Pm1001rrAlmClientTxPwrHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 2, 16, 2),
    _Pm1001rrAlmClientTxPwrHighAla_Type()
)
pm1001rrAlmClientTxPwrHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientTxPwrHighAla.setStatus("current")
_Pm1001rrAlmClientTxBiasLowAla_Type = EkiOnOff
_Pm1001rrAlmClientTxBiasLowAla_Object = MibScalar
pm1001rrAlmClientTxBiasLowAla = _Pm1001rrAlmClientTxBiasLowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 2, 16, 3),
    _Pm1001rrAlmClientTxBiasLowAla_Type()
)
pm1001rrAlmClientTxBiasLowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientTxBiasLowAla.setStatus("current")
_Pm1001rrAlmClientTxBiasHighAla_Type = EkiOnOff
_Pm1001rrAlmClientTxBiasHighAla_Object = MibScalar
pm1001rrAlmClientTxBiasHighAla = _Pm1001rrAlmClientTxBiasHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 2, 16, 4),
    _Pm1001rrAlmClientTxBiasHighAla_Type()
)
pm1001rrAlmClientTxBiasHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientTxBiasHighAla.setStatus("current")
_Pm1001rrAlmClientTempLowAla_Type = EkiOnOff
_Pm1001rrAlmClientTempLowAla_Object = MibScalar
pm1001rrAlmClientTempLowAla = _Pm1001rrAlmClientTempLowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 2, 16, 7),
    _Pm1001rrAlmClientTempLowAla_Type()
)
pm1001rrAlmClientTempLowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientTempLowAla.setStatus("current")
_Pm1001rrAlmClientTempHighAla_Type = EkiOnOff
_Pm1001rrAlmClientTempHighAla_Object = MibScalar
pm1001rrAlmClientTempHighAla = _Pm1001rrAlmClientTempHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 2, 16, 8),
    _Pm1001rrAlmClientTempHighAla_Type()
)
pm1001rrAlmClientTempHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientTempHighAla.setStatus("current")
_Pm1001rrAlmClientRxPwrLowAla_Type = EkiOnOff
_Pm1001rrAlmClientRxPwrLowAla_Object = MibScalar
pm1001rrAlmClientRxPwrLowAla = _Pm1001rrAlmClientRxPwrLowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 2, 16, 15),
    _Pm1001rrAlmClientRxPwrLowAla_Type()
)
pm1001rrAlmClientRxPwrLowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientRxPwrLowAla.setStatus("current")
_Pm1001rrAlmClientRxPwrHighAla_Type = EkiOnOff
_Pm1001rrAlmClientRxPwrHighAla_Object = MibScalar
pm1001rrAlmClientRxPwrHighAla = _Pm1001rrAlmClientRxPwrHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 2, 16, 16),
    _Pm1001rrAlmClientRxPwrHighAla_Type()
)
pm1001rrAlmClientRxPwrHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientRxPwrHighAla.setStatus("current")
_Pm1001rrAlmclientOtxTlhAlarms3_ObjectIdentity = ObjectIdentity
pm1001rrAlmclientOtxTlhAlarms3 = _Pm1001rrAlmclientOtxTlhAlarms3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 2, 22)
)
_Pm1001rrAlmClientModulatorAgingHighAla_Type = EkiOnOff
_Pm1001rrAlmClientModulatorAgingHighAla_Object = MibScalar
pm1001rrAlmClientModulatorAgingHighAla = _Pm1001rrAlmClientModulatorAgingHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 2, 22, 5),
    _Pm1001rrAlmClientModulatorAgingHighAla_Type()
)
pm1001rrAlmClientModulatorAgingHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientModulatorAgingHighAla.setStatus("current")
_Pm1001rrAlmClientAgingHighAla_Type = EkiOnOff
_Pm1001rrAlmClientAgingHighAla_Object = MibScalar
pm1001rrAlmClientAgingHighAla = _Pm1001rrAlmClientAgingHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 2, 22, 6),
    _Pm1001rrAlmClientAgingHighAla_Type()
)
pm1001rrAlmClientAgingHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientAgingHighAla.setStatus("current")
_Pm1001rrAlmClientCdrNotReady_Type = EkiOnOff
_Pm1001rrAlmClientCdrNotReady_Object = MibScalar
pm1001rrAlmClientCdrNotReady = _Pm1001rrAlmClientCdrNotReady_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 2, 22, 9),
    _Pm1001rrAlmClientCdrNotReady_Type()
)
pm1001rrAlmClientCdrNotReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientCdrNotReady.setStatus("current")
_Pm1001rrAlmClientFreqDevHighAla_Type = EkiOnOff
_Pm1001rrAlmClientFreqDevHighAla_Object = MibScalar
pm1001rrAlmClientFreqDevHighAla = _Pm1001rrAlmClientFreqDevHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 2, 22, 12),
    _Pm1001rrAlmClientFreqDevHighAla_Type()
)
pm1001rrAlmClientFreqDevHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientFreqDevHighAla.setStatus("current")
_Pm1001rrAlmClientLaserTempHighAla_Type = EkiOnOff
_Pm1001rrAlmClientLaserTempHighAla_Object = MibScalar
pm1001rrAlmClientLaserTempHighAla = _Pm1001rrAlmClientLaserTempHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 2, 22, 14),
    _Pm1001rrAlmClientLaserTempHighAla_Type()
)
pm1001rrAlmClientLaserTempHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientLaserTempHighAla.setStatus("current")
_Pm1001rrAlmClientCrit_ObjectIdentity = ObjectIdentity
pm1001rrAlmClientCrit = _Pm1001rrAlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 3)
)
_Pm1001rrAlmsynthAlm8_ObjectIdentity = ObjectIdentity
pm1001rrAlmsynthAlm8 = _Pm1001rrAlmsynthAlm8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 3, 8)
)
_Pm1001rrAlmClientXfpAbsent_Type = EkiOnOff
_Pm1001rrAlmClientXfpAbsent_Object = MibScalar
pm1001rrAlmClientXfpAbsent = _Pm1001rrAlmClientXfpAbsent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 3, 8, 1),
    _Pm1001rrAlmClientXfpAbsent_Type()
)
pm1001rrAlmClientXfpAbsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientXfpAbsent.setStatus("current")
_Pm1001rrAlmClientInitNotCompl_Type = EkiOnOff
_Pm1001rrAlmClientInitNotCompl_Object = MibScalar
pm1001rrAlmClientInitNotCompl = _Pm1001rrAlmClientInitNotCompl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 3, 8, 2),
    _Pm1001rrAlmClientInitNotCompl_Type()
)
pm1001rrAlmClientInitNotCompl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientInitNotCompl.setStatus("current")
_Pm1001rrAlmClientHwFail_Type = EkiOnOff
_Pm1001rrAlmClientHwFail_Object = MibScalar
pm1001rrAlmClientHwFail = _Pm1001rrAlmClientHwFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 3, 8, 4),
    _Pm1001rrAlmClientHwFail_Type()
)
pm1001rrAlmClientHwFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientHwFail.setStatus("current")
_Pm1001rrAlmClientXfpTxOff_Type = EkiOnOff
_Pm1001rrAlmClientXfpTxOff_Object = MibScalar
pm1001rrAlmClientXfpTxOff = _Pm1001rrAlmClientXfpTxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 3, 8, 5),
    _Pm1001rrAlmClientXfpTxOff_Type()
)
pm1001rrAlmClientXfpTxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientXfpTxOff.setStatus("current")
_Pm1001rrAlmClientDdmWarning_Type = EkiOnOff
_Pm1001rrAlmClientDdmWarning_Object = MibScalar
pm1001rrAlmClientDdmWarning = _Pm1001rrAlmClientDdmWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 3, 8, 9),
    _Pm1001rrAlmClientDdmWarning_Type()
)
pm1001rrAlmClientDdmWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientDdmWarning.setStatus("current")
_Pm1001rrAlmClientDdmAlm_Type = EkiOnOff
_Pm1001rrAlmClientDdmAlm_Object = MibScalar
pm1001rrAlmClientDdmAlm = _Pm1001rrAlmClientDdmAlm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 3, 8, 10),
    _Pm1001rrAlmClientDdmAlm_Type()
)
pm1001rrAlmClientDdmAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientDdmAlm.setStatus("current")
_Pm1001rrAlmClientFail_Type = EkiOnOff
_Pm1001rrAlmClientFail_Object = MibScalar
pm1001rrAlmClientFail = _Pm1001rrAlmClientFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 3, 8, 12),
    _Pm1001rrAlmClientFail_Type()
)
pm1001rrAlmClientFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientFail.setStatus("current")
_Pm1001rrAlmClientVccWarning_Type = EkiOnOff
_Pm1001rrAlmClientVccWarning_Object = MibScalar
pm1001rrAlmClientVccWarning = _Pm1001rrAlmClientVccWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 3, 8, 14),
    _Pm1001rrAlmClientVccWarning_Type()
)
pm1001rrAlmClientVccWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientVccWarning.setStatus("current")
_Pm1001rrAlmClientVccAlarm_Type = EkiOnOff
_Pm1001rrAlmClientVccAlarm_Object = MibScalar
pm1001rrAlmClientVccAlarm = _Pm1001rrAlmClientVccAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 3, 8, 15),
    _Pm1001rrAlmClientVccAlarm_Type()
)
pm1001rrAlmClientVccAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientVccAlarm.setStatus("current")
_Pm1001rrAlmclientXfpAlarms2_ObjectIdentity = ObjectIdentity
pm1001rrAlmclientXfpAlarms2 = _Pm1001rrAlmclientXfpAlarms2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 3, 19)
)
_Pm1001rrAlmClientResetComplete_Type = EkiOnOff
_Pm1001rrAlmClientResetComplete_Object = MibScalar
pm1001rrAlmClientResetComplete = _Pm1001rrAlmClientResetComplete_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 3, 19, 1),
    _Pm1001rrAlmClientResetComplete_Type()
)
pm1001rrAlmClientResetComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientResetComplete.setStatus("current")
_Pm1001rrAlmClientRxCdrNotLocked_Type = EkiOnOff
_Pm1001rrAlmClientRxCdrNotLocked_Object = MibScalar
pm1001rrAlmClientRxCdrNotLocked = _Pm1001rrAlmClientRxCdrNotLocked_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 3, 19, 3),
    _Pm1001rrAlmClientRxCdrNotLocked_Type()
)
pm1001rrAlmClientRxCdrNotLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientRxCdrNotLocked.setStatus("current")
_Pm1001rrAlmClientRxLos_Type = EkiOnOff
_Pm1001rrAlmClientRxLos_Object = MibScalar
pm1001rrAlmClientRxLos = _Pm1001rrAlmClientRxLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 3, 19, 4),
    _Pm1001rrAlmClientRxLos_Type()
)
pm1001rrAlmClientRxLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientRxLos.setStatus("current")
_Pm1001rrAlmClientRxNr_Type = EkiOnOff
_Pm1001rrAlmClientRxNr_Object = MibScalar
pm1001rrAlmClientRxNr = _Pm1001rrAlmClientRxNr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 3, 19, 5),
    _Pm1001rrAlmClientRxNr_Type()
)
pm1001rrAlmClientRxNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientRxNr.setStatus("current")
_Pm1001rrAlmClientTxCdrNotLocked_Type = EkiOnOff
_Pm1001rrAlmClientTxCdrNotLocked_Object = MibScalar
pm1001rrAlmClientTxCdrNotLocked = _Pm1001rrAlmClientTxCdrNotLocked_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 3, 19, 6),
    _Pm1001rrAlmClientTxCdrNotLocked_Type()
)
pm1001rrAlmClientTxCdrNotLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientTxCdrNotLocked.setStatus("current")
_Pm1001rrAlmClientTxFault_Type = EkiOnOff
_Pm1001rrAlmClientTxFault_Object = MibScalar
pm1001rrAlmClientTxFault = _Pm1001rrAlmClientTxFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 3, 19, 7),
    _Pm1001rrAlmClientTxFault_Type()
)
pm1001rrAlmClientTxFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientTxFault.setStatus("current")
_Pm1001rrAlmClientTxNr_Type = EkiOnOff
_Pm1001rrAlmClientTxNr_Object = MibScalar
pm1001rrAlmClientTxNr = _Pm1001rrAlmClientTxNr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 3, 19, 8),
    _Pm1001rrAlmClientTxNr_Type()
)
pm1001rrAlmClientTxNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientTxNr.setStatus("current")
_Pm1001rrAlmClientChannelNotAcquired_Type = EkiOnOff
_Pm1001rrAlmClientChannelNotAcquired_Object = MibScalar
pm1001rrAlmClientChannelNotAcquired = _Pm1001rrAlmClientChannelNotAcquired_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 3, 19, 10),
    _Pm1001rrAlmClientChannelNotAcquired_Type()
)
pm1001rrAlmClientChannelNotAcquired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientChannelNotAcquired.setStatus("current")
_Pm1001rrAlmClientWavelengthUnlocked_Type = EkiOnOff
_Pm1001rrAlmClientWavelengthUnlocked_Object = MibScalar
pm1001rrAlmClientWavelengthUnlocked = _Pm1001rrAlmClientWavelengthUnlocked_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 3, 19, 14),
    _Pm1001rrAlmClientWavelengthUnlocked_Type()
)
pm1001rrAlmClientWavelengthUnlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientWavelengthUnlocked.setStatus("current")
_Pm1001rrAlmClientTecFault_Type = EkiOnOff
_Pm1001rrAlmClientTecFault_Object = MibScalar
pm1001rrAlmClientTecFault = _Pm1001rrAlmClientTecFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 3, 19, 15),
    _Pm1001rrAlmClientTecFault_Type()
)
pm1001rrAlmClientTecFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientTecFault.setStatus("current")
_Pm1001rrAlmClientApdSupplyFault_Type = EkiOnOff
_Pm1001rrAlmClientApdSupplyFault_Object = MibScalar
pm1001rrAlmClientApdSupplyFault = _Pm1001rrAlmClientApdSupplyFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 2, 3, 19, 16),
    _Pm1001rrAlmClientApdSupplyFault_Type()
)
pm1001rrAlmClientApdSupplyFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmClientApdSupplyFault.setStatus("current")
_Pm1001rrAlmLine_ObjectIdentity = ObjectIdentity
pm1001rrAlmLine = _Pm1001rrAlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3)
)
_Pm1001rrAlmLineNurg_ObjectIdentity = ObjectIdentity
pm1001rrAlmLineNurg = _Pm1001rrAlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 1)
)
_Pm1001rrAlmlineXfpWarnings_ObjectIdentity = ObjectIdentity
pm1001rrAlmlineXfpWarnings = _Pm1001rrAlmlineXfpWarnings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 1, 25)
)
_Pm1001rrAlmLineTxPwrLowWng_Type = EkiOnOff
_Pm1001rrAlmLineTxPwrLowWng_Object = MibScalar
pm1001rrAlmLineTxPwrLowWng = _Pm1001rrAlmLineTxPwrLowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 1, 25, 1),
    _Pm1001rrAlmLineTxPwrLowWng_Type()
)
pm1001rrAlmLineTxPwrLowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineTxPwrLowWng.setStatus("current")
_Pm1001rrAlmLineTxPwrHighWng_Type = EkiOnOff
_Pm1001rrAlmLineTxPwrHighWng_Object = MibScalar
pm1001rrAlmLineTxPwrHighWng = _Pm1001rrAlmLineTxPwrHighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 1, 25, 2),
    _Pm1001rrAlmLineTxPwrHighWng_Type()
)
pm1001rrAlmLineTxPwrHighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineTxPwrHighWng.setStatus("current")
_Pm1001rrAlmLineTxBiasLowWng_Type = EkiOnOff
_Pm1001rrAlmLineTxBiasLowWng_Object = MibScalar
pm1001rrAlmLineTxBiasLowWng = _Pm1001rrAlmLineTxBiasLowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 1, 25, 3),
    _Pm1001rrAlmLineTxBiasLowWng_Type()
)
pm1001rrAlmLineTxBiasLowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineTxBiasLowWng.setStatus("current")
_Pm1001rrAlmLineTxBiasHighWng_Type = EkiOnOff
_Pm1001rrAlmLineTxBiasHighWng_Object = MibScalar
pm1001rrAlmLineTxBiasHighWng = _Pm1001rrAlmLineTxBiasHighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 1, 25, 4),
    _Pm1001rrAlmLineTxBiasHighWng_Type()
)
pm1001rrAlmLineTxBiasHighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineTxBiasHighWng.setStatus("current")
_Pm1001rrAlmLineTempLowWng_Type = EkiOnOff
_Pm1001rrAlmLineTempLowWng_Object = MibScalar
pm1001rrAlmLineTempLowWng = _Pm1001rrAlmLineTempLowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 1, 25, 7),
    _Pm1001rrAlmLineTempLowWng_Type()
)
pm1001rrAlmLineTempLowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineTempLowWng.setStatus("current")
_Pm1001rrAlmLineTempHighWng_Type = EkiOnOff
_Pm1001rrAlmLineTempHighWng_Object = MibScalar
pm1001rrAlmLineTempHighWng = _Pm1001rrAlmLineTempHighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 1, 25, 8),
    _Pm1001rrAlmLineTempHighWng_Type()
)
pm1001rrAlmLineTempHighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineTempHighWng.setStatus("current")
_Pm1001rrAlmLineRxPwrLowWng_Type = EkiOnOff
_Pm1001rrAlmLineRxPwrLowWng_Object = MibScalar
pm1001rrAlmLineRxPwrLowWng = _Pm1001rrAlmLineRxPwrLowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 1, 25, 15),
    _Pm1001rrAlmLineRxPwrLowWng_Type()
)
pm1001rrAlmLineRxPwrLowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineRxPwrLowWng.setStatus("current")
_Pm1001rrAlmLineRxPwrHighWng_Type = EkiOnOff
_Pm1001rrAlmLineRxPwrHighWng_Object = MibScalar
pm1001rrAlmLineRxPwrHighWng = _Pm1001rrAlmLineRxPwrHighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 1, 25, 16),
    _Pm1001rrAlmLineRxPwrHighWng_Type()
)
pm1001rrAlmLineRxPwrHighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineRxPwrHighWng.setStatus("current")
_Pm1001rrAlmrrLineOtxTlhWarnings_ObjectIdentity = ObjectIdentity
pm1001rrAlmrrLineOtxTlhWarnings = _Pm1001rrAlmrrLineOtxTlhWarnings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 1, 31)
)
_Pm1001rrAlmLineModulatorAgingHighWarning_Type = EkiOnOff
_Pm1001rrAlmLineModulatorAgingHighWarning_Object = MibScalar
pm1001rrAlmLineModulatorAgingHighWarning = _Pm1001rrAlmLineModulatorAgingHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 1, 31, 5),
    _Pm1001rrAlmLineModulatorAgingHighWarning_Type()
)
pm1001rrAlmLineModulatorAgingHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineModulatorAgingHighWarning.setStatus("current")
_Pm1001rrAlmLineAgingHighWarning_Type = EkiOnOff
_Pm1001rrAlmLineAgingHighWarning_Object = MibScalar
pm1001rrAlmLineAgingHighWarning = _Pm1001rrAlmLineAgingHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 1, 31, 6),
    _Pm1001rrAlmLineAgingHighWarning_Type()
)
pm1001rrAlmLineAgingHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineAgingHighWarning.setStatus("current")
_Pm1001rrAlmLineFreqDevHighWarning_Type = EkiOnOff
_Pm1001rrAlmLineFreqDevHighWarning_Object = MibScalar
pm1001rrAlmLineFreqDevHighWarning = _Pm1001rrAlmLineFreqDevHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 1, 31, 12),
    _Pm1001rrAlmLineFreqDevHighWarning_Type()
)
pm1001rrAlmLineFreqDevHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineFreqDevHighWarning.setStatus("current")
_Pm1001rrAlmLineLaserTempHighWarning_Type = EkiOnOff
_Pm1001rrAlmLineLaserTempHighWarning_Object = MibScalar
pm1001rrAlmLineLaserTempHighWarning = _Pm1001rrAlmLineLaserTempHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 1, 31, 14),
    _Pm1001rrAlmLineLaserTempHighWarning_Type()
)
pm1001rrAlmLineLaserTempHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineLaserTempHighWarning.setStatus("current")
_Pm1001rrAlmLineUrg_ObjectIdentity = ObjectIdentity
pm1001rrAlmLineUrg = _Pm1001rrAlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 2)
)
_Pm1001rrAlmlineXfpAlarm1_ObjectIdentity = ObjectIdentity
pm1001rrAlmlineXfpAlarm1 = _Pm1001rrAlmlineXfpAlarm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 2, 24)
)
_Pm1001rrAlmLineTxPwrLowAla_Type = EkiOnOff
_Pm1001rrAlmLineTxPwrLowAla_Object = MibScalar
pm1001rrAlmLineTxPwrLowAla = _Pm1001rrAlmLineTxPwrLowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 2, 24, 1),
    _Pm1001rrAlmLineTxPwrLowAla_Type()
)
pm1001rrAlmLineTxPwrLowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineTxPwrLowAla.setStatus("current")
_Pm1001rrAlmLineTxPwrHighAla_Type = EkiOnOff
_Pm1001rrAlmLineTxPwrHighAla_Object = MibScalar
pm1001rrAlmLineTxPwrHighAla = _Pm1001rrAlmLineTxPwrHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 2, 24, 2),
    _Pm1001rrAlmLineTxPwrHighAla_Type()
)
pm1001rrAlmLineTxPwrHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineTxPwrHighAla.setStatus("current")
_Pm1001rrAlmLineTxBiasLowAla_Type = EkiOnOff
_Pm1001rrAlmLineTxBiasLowAla_Object = MibScalar
pm1001rrAlmLineTxBiasLowAla = _Pm1001rrAlmLineTxBiasLowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 2, 24, 3),
    _Pm1001rrAlmLineTxBiasLowAla_Type()
)
pm1001rrAlmLineTxBiasLowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineTxBiasLowAla.setStatus("current")
_Pm1001rrAlmLineTxBiasHighAla_Type = EkiOnOff
_Pm1001rrAlmLineTxBiasHighAla_Object = MibScalar
pm1001rrAlmLineTxBiasHighAla = _Pm1001rrAlmLineTxBiasHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 2, 24, 4),
    _Pm1001rrAlmLineTxBiasHighAla_Type()
)
pm1001rrAlmLineTxBiasHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineTxBiasHighAla.setStatus("current")
_Pm1001rrAlmLineTempLowAla_Type = EkiOnOff
_Pm1001rrAlmLineTempLowAla_Object = MibScalar
pm1001rrAlmLineTempLowAla = _Pm1001rrAlmLineTempLowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 2, 24, 7),
    _Pm1001rrAlmLineTempLowAla_Type()
)
pm1001rrAlmLineTempLowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineTempLowAla.setStatus("current")
_Pm1001rrAlmLineTempHighAla_Type = EkiOnOff
_Pm1001rrAlmLineTempHighAla_Object = MibScalar
pm1001rrAlmLineTempHighAla = _Pm1001rrAlmLineTempHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 2, 24, 8),
    _Pm1001rrAlmLineTempHighAla_Type()
)
pm1001rrAlmLineTempHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineTempHighAla.setStatus("current")
_Pm1001rrAlmLineRxPwrLowAla_Type = EkiOnOff
_Pm1001rrAlmLineRxPwrLowAla_Object = MibScalar
pm1001rrAlmLineRxPwrLowAla = _Pm1001rrAlmLineRxPwrLowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 2, 24, 15),
    _Pm1001rrAlmLineRxPwrLowAla_Type()
)
pm1001rrAlmLineRxPwrLowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineRxPwrLowAla.setStatus("current")
_Pm1001rrAlmLineRxPwrHighAla_Type = EkiOnOff
_Pm1001rrAlmLineRxPwrHighAla_Object = MibScalar
pm1001rrAlmLineRxPwrHighAla = _Pm1001rrAlmLineRxPwrHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 2, 24, 16),
    _Pm1001rrAlmLineRxPwrHighAla_Type()
)
pm1001rrAlmLineRxPwrHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineRxPwrHighAla.setStatus("current")
_Pm1001rrAlmrrLineOtxTlhAlarms3_ObjectIdentity = ObjectIdentity
pm1001rrAlmrrLineOtxTlhAlarms3 = _Pm1001rrAlmrrLineOtxTlhAlarms3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 2, 30)
)
_Pm1001rrAlmLineModulatorAgingHighAla_Type = EkiOnOff
_Pm1001rrAlmLineModulatorAgingHighAla_Object = MibScalar
pm1001rrAlmLineModulatorAgingHighAla = _Pm1001rrAlmLineModulatorAgingHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 2, 30, 5),
    _Pm1001rrAlmLineModulatorAgingHighAla_Type()
)
pm1001rrAlmLineModulatorAgingHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineModulatorAgingHighAla.setStatus("current")
_Pm1001rrAlmLineAgingHighAla_Type = EkiOnOff
_Pm1001rrAlmLineAgingHighAla_Object = MibScalar
pm1001rrAlmLineAgingHighAla = _Pm1001rrAlmLineAgingHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 2, 30, 6),
    _Pm1001rrAlmLineAgingHighAla_Type()
)
pm1001rrAlmLineAgingHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineAgingHighAla.setStatus("current")
_Pm1001rrAlmLineCdrNotReady_Type = EkiOnOff
_Pm1001rrAlmLineCdrNotReady_Object = MibScalar
pm1001rrAlmLineCdrNotReady = _Pm1001rrAlmLineCdrNotReady_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 2, 30, 9),
    _Pm1001rrAlmLineCdrNotReady_Type()
)
pm1001rrAlmLineCdrNotReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineCdrNotReady.setStatus("current")
_Pm1001rrAlmLineFreqDevHighAla_Type = EkiOnOff
_Pm1001rrAlmLineFreqDevHighAla_Object = MibScalar
pm1001rrAlmLineFreqDevHighAla = _Pm1001rrAlmLineFreqDevHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 2, 30, 12),
    _Pm1001rrAlmLineFreqDevHighAla_Type()
)
pm1001rrAlmLineFreqDevHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineFreqDevHighAla.setStatus("current")
_Pm1001rrAlmLineLaserTempHighAla_Type = EkiOnOff
_Pm1001rrAlmLineLaserTempHighAla_Object = MibScalar
pm1001rrAlmLineLaserTempHighAla = _Pm1001rrAlmLineLaserTempHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 2, 30, 14),
    _Pm1001rrAlmLineLaserTempHighAla_Type()
)
pm1001rrAlmLineLaserTempHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineLaserTempHighAla.setStatus("current")
_Pm1001rrAlmLineCrit_ObjectIdentity = ObjectIdentity
pm1001rrAlmLineCrit = _Pm1001rrAlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 3)
)
_Pm1001rrAlmsynthAlm7_ObjectIdentity = ObjectIdentity
pm1001rrAlmsynthAlm7 = _Pm1001rrAlmsynthAlm7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 3, 7)
)
_Pm1001rrAlmLineXfpAbsent_Type = EkiOnOff
_Pm1001rrAlmLineXfpAbsent_Object = MibScalar
pm1001rrAlmLineXfpAbsent = _Pm1001rrAlmLineXfpAbsent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 3, 7, 1),
    _Pm1001rrAlmLineXfpAbsent_Type()
)
pm1001rrAlmLineXfpAbsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineXfpAbsent.setStatus("current")
_Pm1001rrAlmLineInitNotCompl_Type = EkiOnOff
_Pm1001rrAlmLineInitNotCompl_Object = MibScalar
pm1001rrAlmLineInitNotCompl = _Pm1001rrAlmLineInitNotCompl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 3, 7, 2),
    _Pm1001rrAlmLineInitNotCompl_Type()
)
pm1001rrAlmLineInitNotCompl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineInitNotCompl.setStatus("current")
_Pm1001rrAlmLineHwFail_Type = EkiOnOff
_Pm1001rrAlmLineHwFail_Object = MibScalar
pm1001rrAlmLineHwFail = _Pm1001rrAlmLineHwFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 3, 7, 4),
    _Pm1001rrAlmLineHwFail_Type()
)
pm1001rrAlmLineHwFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineHwFail.setStatus("current")
_Pm1001rrAlmLineXfpTxOff_Type = EkiOnOff
_Pm1001rrAlmLineXfpTxOff_Object = MibScalar
pm1001rrAlmLineXfpTxOff = _Pm1001rrAlmLineXfpTxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 3, 7, 5),
    _Pm1001rrAlmLineXfpTxOff_Type()
)
pm1001rrAlmLineXfpTxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineXfpTxOff.setStatus("current")
_Pm1001rrAlmLineDdmWarning_Type = EkiOnOff
_Pm1001rrAlmLineDdmWarning_Object = MibScalar
pm1001rrAlmLineDdmWarning = _Pm1001rrAlmLineDdmWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 3, 7, 9),
    _Pm1001rrAlmLineDdmWarning_Type()
)
pm1001rrAlmLineDdmWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineDdmWarning.setStatus("current")
_Pm1001rrAlmLineDdmAlm_Type = EkiOnOff
_Pm1001rrAlmLineDdmAlm_Object = MibScalar
pm1001rrAlmLineDdmAlm = _Pm1001rrAlmLineDdmAlm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 3, 7, 10),
    _Pm1001rrAlmLineDdmAlm_Type()
)
pm1001rrAlmLineDdmAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineDdmAlm.setStatus("current")
_Pm1001rrAlmLineFail_Type = EkiOnOff
_Pm1001rrAlmLineFail_Object = MibScalar
pm1001rrAlmLineFail = _Pm1001rrAlmLineFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 3, 7, 12),
    _Pm1001rrAlmLineFail_Type()
)
pm1001rrAlmLineFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineFail.setStatus("current")
_Pm1001rrAlmLineVccWarning_Type = EkiOnOff
_Pm1001rrAlmLineVccWarning_Object = MibScalar
pm1001rrAlmLineVccWarning = _Pm1001rrAlmLineVccWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 3, 7, 14),
    _Pm1001rrAlmLineVccWarning_Type()
)
pm1001rrAlmLineVccWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineVccWarning.setStatus("current")
_Pm1001rrAlmLineVccAlarm_Type = EkiOnOff
_Pm1001rrAlmLineVccAlarm_Object = MibScalar
pm1001rrAlmLineVccAlarm = _Pm1001rrAlmLineVccAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 3, 7, 15),
    _Pm1001rrAlmLineVccAlarm_Type()
)
pm1001rrAlmLineVccAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineVccAlarm.setStatus("current")
_Pm1001rrAlmlineXfpAlarms2_ObjectIdentity = ObjectIdentity
pm1001rrAlmlineXfpAlarms2 = _Pm1001rrAlmlineXfpAlarms2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 3, 27)
)
_Pm1001rrAlmLineResetComplete_Type = EkiOnOff
_Pm1001rrAlmLineResetComplete_Object = MibScalar
pm1001rrAlmLineResetComplete = _Pm1001rrAlmLineResetComplete_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 3, 27, 1),
    _Pm1001rrAlmLineResetComplete_Type()
)
pm1001rrAlmLineResetComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineResetComplete.setStatus("current")
_Pm1001rrAlmLineRxCdrNotLocked_Type = EkiOnOff
_Pm1001rrAlmLineRxCdrNotLocked_Object = MibScalar
pm1001rrAlmLineRxCdrNotLocked = _Pm1001rrAlmLineRxCdrNotLocked_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 3, 27, 3),
    _Pm1001rrAlmLineRxCdrNotLocked_Type()
)
pm1001rrAlmLineRxCdrNotLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineRxCdrNotLocked.setStatus("current")
_Pm1001rrAlmLineRxLos_Type = EkiOnOff
_Pm1001rrAlmLineRxLos_Object = MibScalar
pm1001rrAlmLineRxLos = _Pm1001rrAlmLineRxLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 3, 27, 4),
    _Pm1001rrAlmLineRxLos_Type()
)
pm1001rrAlmLineRxLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineRxLos.setStatus("current")
_Pm1001rrAlmLineRxNr_Type = EkiOnOff
_Pm1001rrAlmLineRxNr_Object = MibScalar
pm1001rrAlmLineRxNr = _Pm1001rrAlmLineRxNr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 3, 27, 5),
    _Pm1001rrAlmLineRxNr_Type()
)
pm1001rrAlmLineRxNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineRxNr.setStatus("current")
_Pm1001rrAlmLineTxCdrNotLocked_Type = EkiOnOff
_Pm1001rrAlmLineTxCdrNotLocked_Object = MibScalar
pm1001rrAlmLineTxCdrNotLocked = _Pm1001rrAlmLineTxCdrNotLocked_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 3, 27, 6),
    _Pm1001rrAlmLineTxCdrNotLocked_Type()
)
pm1001rrAlmLineTxCdrNotLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineTxCdrNotLocked.setStatus("current")
_Pm1001rrAlmLineTxFault_Type = EkiOnOff
_Pm1001rrAlmLineTxFault_Object = MibScalar
pm1001rrAlmLineTxFault = _Pm1001rrAlmLineTxFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 3, 27, 7),
    _Pm1001rrAlmLineTxFault_Type()
)
pm1001rrAlmLineTxFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineTxFault.setStatus("current")
_Pm1001rrAlmLineTxNr_Type = EkiOnOff
_Pm1001rrAlmLineTxNr_Object = MibScalar
pm1001rrAlmLineTxNr = _Pm1001rrAlmLineTxNr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 3, 27, 8),
    _Pm1001rrAlmLineTxNr_Type()
)
pm1001rrAlmLineTxNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineTxNr.setStatus("current")
_Pm1001rrAlmLineChannelNotAcquired_Type = EkiOnOff
_Pm1001rrAlmLineChannelNotAcquired_Object = MibScalar
pm1001rrAlmLineChannelNotAcquired = _Pm1001rrAlmLineChannelNotAcquired_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 3, 27, 10),
    _Pm1001rrAlmLineChannelNotAcquired_Type()
)
pm1001rrAlmLineChannelNotAcquired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineChannelNotAcquired.setStatus("current")
_Pm1001rrAlmLineWavelengthUnlocked_Type = EkiOnOff
_Pm1001rrAlmLineWavelengthUnlocked_Object = MibScalar
pm1001rrAlmLineWavelengthUnlocked = _Pm1001rrAlmLineWavelengthUnlocked_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 3, 27, 14),
    _Pm1001rrAlmLineWavelengthUnlocked_Type()
)
pm1001rrAlmLineWavelengthUnlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineWavelengthUnlocked.setStatus("current")
_Pm1001rrAlmLineTecFault_Type = EkiOnOff
_Pm1001rrAlmLineTecFault_Object = MibScalar
pm1001rrAlmLineTecFault = _Pm1001rrAlmLineTecFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 3, 27, 15),
    _Pm1001rrAlmLineTecFault_Type()
)
pm1001rrAlmLineTecFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineTecFault.setStatus("current")
_Pm1001rrAlmLineApdSupplyFault_Type = EkiOnOff
_Pm1001rrAlmLineApdSupplyFault_Object = MibScalar
pm1001rrAlmLineApdSupplyFault = _Pm1001rrAlmLineApdSupplyFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 2, 3, 3, 27, 16),
    _Pm1001rrAlmLineApdSupplyFault_Type()
)
pm1001rrAlmLineApdSupplyFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrAlmLineApdSupplyFault.setStatus("current")
_Pm1001rrmeasures_ObjectIdentity = ObjectIdentity
pm1001rrmeasures = _Pm1001rrmeasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 3)
)
_Pm1001rrMesrOther_ObjectIdentity = ObjectIdentity
pm1001rrMesrOther = _Pm1001rrMesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 3, 1)
)
_Pm1001rrMesrClient_ObjectIdentity = ObjectIdentity
pm1001rrMesrClient = _Pm1001rrMesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 3, 2)
)


class _Pm1001rrMesrclientTemperature_Type(Unsigned32):
    """Custom type pm1001rrMesrclientTemperature based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001rrMesrclientTemperature_Type.__name__ = "Unsigned32"
_Pm1001rrMesrclientTemperature_Object = MibScalar
pm1001rrMesrclientTemperature = _Pm1001rrMesrclientTemperature_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 3, 2, 16),
    _Pm1001rrMesrclientTemperature_Type()
)
pm1001rrMesrclientTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrMesrclientTemperature.setStatus("current")


class _Pm1001rrMesrclientTxBias_Type(Unsigned32):
    """Custom type pm1001rrMesrclientTxBias based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001rrMesrclientTxBias_Type.__name__ = "Unsigned32"
_Pm1001rrMesrclientTxBias_Object = MibScalar
pm1001rrMesrclientTxBias = _Pm1001rrMesrclientTxBias_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 3, 2, 18),
    _Pm1001rrMesrclientTxBias_Type()
)
pm1001rrMesrclientTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrMesrclientTxBias.setStatus("current")


class _Pm1001rrMesrclientTxPower_Type(Unsigned32):
    """Custom type pm1001rrMesrclientTxPower based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001rrMesrclientTxPower_Type.__name__ = "Unsigned32"
_Pm1001rrMesrclientTxPower_Object = MibScalar
pm1001rrMesrclientTxPower = _Pm1001rrMesrclientTxPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 3, 2, 19),
    _Pm1001rrMesrclientTxPower_Type()
)
pm1001rrMesrclientTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrMesrclientTxPower.setStatus("current")


class _Pm1001rrMesrclientRxPower_Type(Unsigned32):
    """Custom type pm1001rrMesrclientRxPower based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001rrMesrclientRxPower_Type.__name__ = "Unsigned32"
_Pm1001rrMesrclientRxPower_Object = MibScalar
pm1001rrMesrclientRxPower = _Pm1001rrMesrclientRxPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 3, 2, 20),
    _Pm1001rrMesrclientRxPower_Type()
)
pm1001rrMesrclientRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrMesrclientRxPower.setStatus("current")


class _Pm1001rrMesrclientAging_Type(Unsigned32):
    """Custom type pm1001rrMesrclientAging based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001rrMesrclientAging_Type.__name__ = "Unsigned32"
_Pm1001rrMesrclientAging_Object = MibScalar
pm1001rrMesrclientAging = _Pm1001rrMesrclientAging_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 3, 2, 32),
    _Pm1001rrMesrclientAging_Type()
)
pm1001rrMesrclientAging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrMesrclientAging.setStatus("current")


class _Pm1001rrMesrclientLaserTemperature_Type(Unsigned32):
    """Custom type pm1001rrMesrclientLaserTemperature based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001rrMesrclientLaserTemperature_Type.__name__ = "Unsigned32"
_Pm1001rrMesrclientLaserTemperature_Object = MibScalar
pm1001rrMesrclientLaserTemperature = _Pm1001rrMesrclientLaserTemperature_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 3, 2, 33),
    _Pm1001rrMesrclientLaserTemperature_Type()
)
pm1001rrMesrclientLaserTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrMesrclientLaserTemperature.setStatus("current")


class _Pm1001rrMesrclientFreqDeviation_Type(Unsigned32):
    """Custom type pm1001rrMesrclientFreqDeviation based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001rrMesrclientFreqDeviation_Type.__name__ = "Unsigned32"
_Pm1001rrMesrclientFreqDeviation_Object = MibScalar
pm1001rrMesrclientFreqDeviation = _Pm1001rrMesrclientFreqDeviation_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 3, 2, 34),
    _Pm1001rrMesrclientFreqDeviation_Type()
)
pm1001rrMesrclientFreqDeviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrMesrclientFreqDeviation.setStatus("current")


class _Pm1001rrMesrclientLaserWvlength_Type(Unsigned32):
    """Custom type pm1001rrMesrclientLaserWvlength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001rrMesrclientLaserWvlength_Type.__name__ = "Unsigned32"
_Pm1001rrMesrclientLaserWvlength_Object = MibScalar
pm1001rrMesrclientLaserWvlength = _Pm1001rrMesrclientLaserWvlength_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 3, 2, 35),
    _Pm1001rrMesrclientLaserWvlength_Type()
)
pm1001rrMesrclientLaserWvlength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrMesrclientLaserWvlength.setStatus("current")
_Pm1001rrMesrLine_ObjectIdentity = ObjectIdentity
pm1001rrMesrLine = _Pm1001rrMesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 3, 3)
)


class _Pm1001rrMesrlineTemperature_Type(Unsigned32):
    """Custom type pm1001rrMesrlineTemperature based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001rrMesrlineTemperature_Type.__name__ = "Unsigned32"
_Pm1001rrMesrlineTemperature_Object = MibScalar
pm1001rrMesrlineTemperature = _Pm1001rrMesrlineTemperature_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 3, 3, 24),
    _Pm1001rrMesrlineTemperature_Type()
)
pm1001rrMesrlineTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrMesrlineTemperature.setStatus("current")


class _Pm1001rrMesrlineTxBias_Type(Unsigned32):
    """Custom type pm1001rrMesrlineTxBias based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001rrMesrlineTxBias_Type.__name__ = "Unsigned32"
_Pm1001rrMesrlineTxBias_Object = MibScalar
pm1001rrMesrlineTxBias = _Pm1001rrMesrlineTxBias_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 3, 3, 26),
    _Pm1001rrMesrlineTxBias_Type()
)
pm1001rrMesrlineTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrMesrlineTxBias.setStatus("current")


class _Pm1001rrMesrlineTxPower_Type(Unsigned32):
    """Custom type pm1001rrMesrlineTxPower based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001rrMesrlineTxPower_Type.__name__ = "Unsigned32"
_Pm1001rrMesrlineTxPower_Object = MibScalar
pm1001rrMesrlineTxPower = _Pm1001rrMesrlineTxPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 3, 3, 27),
    _Pm1001rrMesrlineTxPower_Type()
)
pm1001rrMesrlineTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrMesrlineTxPower.setStatus("current")


class _Pm1001rrMesrlineRxPower_Type(Unsigned32):
    """Custom type pm1001rrMesrlineRxPower based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001rrMesrlineRxPower_Type.__name__ = "Unsigned32"
_Pm1001rrMesrlineRxPower_Object = MibScalar
pm1001rrMesrlineRxPower = _Pm1001rrMesrlineRxPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 3, 3, 28),
    _Pm1001rrMesrlineRxPower_Type()
)
pm1001rrMesrlineRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrMesrlineRxPower.setStatus("current")


class _Pm1001rrMesrlineAging_Type(Unsigned32):
    """Custom type pm1001rrMesrlineAging based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001rrMesrlineAging_Type.__name__ = "Unsigned32"
_Pm1001rrMesrlineAging_Object = MibScalar
pm1001rrMesrlineAging = _Pm1001rrMesrlineAging_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 3, 3, 40),
    _Pm1001rrMesrlineAging_Type()
)
pm1001rrMesrlineAging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrMesrlineAging.setStatus("current")


class _Pm1001rrMesrlineLaserTemperature_Type(Unsigned32):
    """Custom type pm1001rrMesrlineLaserTemperature based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001rrMesrlineLaserTemperature_Type.__name__ = "Unsigned32"
_Pm1001rrMesrlineLaserTemperature_Object = MibScalar
pm1001rrMesrlineLaserTemperature = _Pm1001rrMesrlineLaserTemperature_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 3, 3, 41),
    _Pm1001rrMesrlineLaserTemperature_Type()
)
pm1001rrMesrlineLaserTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrMesrlineLaserTemperature.setStatus("current")


class _Pm1001rrMesrlineFreqDeviation_Type(Unsigned32):
    """Custom type pm1001rrMesrlineFreqDeviation based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001rrMesrlineFreqDeviation_Type.__name__ = "Unsigned32"
_Pm1001rrMesrlineFreqDeviation_Object = MibScalar
pm1001rrMesrlineFreqDeviation = _Pm1001rrMesrlineFreqDeviation_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 3, 3, 42),
    _Pm1001rrMesrlineFreqDeviation_Type()
)
pm1001rrMesrlineFreqDeviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrMesrlineFreqDeviation.setStatus("current")


class _Pm1001rrMesrlineLaserWvlength_Type(Unsigned32):
    """Custom type pm1001rrMesrlineLaserWvlength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001rrMesrlineLaserWvlength_Type.__name__ = "Unsigned32"
_Pm1001rrMesrlineLaserWvlength_Object = MibScalar
pm1001rrMesrlineLaserWvlength = _Pm1001rrMesrlineLaserWvlength_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 3, 3, 43),
    _Pm1001rrMesrlineLaserWvlength_Type()
)
pm1001rrMesrlineLaserWvlength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrMesrlineLaserWvlength.setStatus("current")
_Pm1001rrcontrolsWrite_ObjectIdentity = ObjectIdentity
pm1001rrcontrolsWrite = _Pm1001rrcontrolsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6)
)
_Pm1001rrCtrlOther_ObjectIdentity = ObjectIdentity
pm1001rrCtrlOther = _Pm1001rrCtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 1)
)
_Pm1001rrCtrlsynth0_ObjectIdentity = ObjectIdentity
pm1001rrCtrlsynth0 = _Pm1001rrCtrlsynth0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 1, 0)
)
_Pm1001rrCtrlConfLoad_Type = EkiOnOff
_Pm1001rrCtrlConfLoad_Object = MibScalar
pm1001rrCtrlConfLoad = _Pm1001rrCtrlConfLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 1, 0, 1),
    _Pm1001rrCtrlConfLoad_Type()
)
pm1001rrCtrlConfLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCtrlConfLoad.setStatus("current")
_Pm1001rrCtrlConfFlash_Type = EkiOnOff
_Pm1001rrCtrlConfFlash_Object = MibScalar
pm1001rrCtrlConfFlash = _Pm1001rrCtrlConfFlash_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 1, 0, 9),
    _Pm1001rrCtrlConfFlash_Type()
)
pm1001rrCtrlConfFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCtrlConfFlash.setStatus("current")
_Pm1001rrCtrlConfClear_Type = EkiOnOff
_Pm1001rrCtrlConfClear_Object = MibScalar
pm1001rrCtrlConfClear = _Pm1001rrCtrlConfClear_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 1, 0, 13),
    _Pm1001rrCtrlConfClear_Type()
)
pm1001rrCtrlConfClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCtrlConfClear.setStatus("current")
_Pm1001rrCtrlsynth4_ObjectIdentity = ObjectIdentity
pm1001rrCtrlsynth4 = _Pm1001rrCtrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 1, 4)
)
_Pm1001rrCtrlCorrelatOn_Type = EkiOnOff
_Pm1001rrCtrlCorrelatOn_Object = MibScalar
pm1001rrCtrlCorrelatOn = _Pm1001rrCtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 1, 4, 1),
    _Pm1001rrCtrlCorrelatOn_Type()
)
pm1001rrCtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCtrlCorrelatOn.setStatus("current")
_Pm1001rrCtrlCorrelatOff_Type = EkiOnOff
_Pm1001rrCtrlCorrelatOff_Object = MibScalar
pm1001rrCtrlCorrelatOff = _Pm1001rrCtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 1, 4, 2),
    _Pm1001rrCtrlCorrelatOff_Type()
)
pm1001rrCtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCtrlCorrelatOff.setStatus("current")
_Pm1001rrCtrlswMgnt_ObjectIdentity = ObjectIdentity
pm1001rrCtrlswMgnt = _Pm1001rrCtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 1, 5)
)
_Pm1001rrCtrlColdReset_Type = EkiOnOff
_Pm1001rrCtrlColdReset_Object = MibScalar
pm1001rrCtrlColdReset = _Pm1001rrCtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 1, 5, 2),
    _Pm1001rrCtrlColdReset_Type()
)
pm1001rrCtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCtrlColdReset.setStatus("current")
_Pm1001rrCtrlWarmReset_Type = EkiOnOff
_Pm1001rrCtrlWarmReset_Object = MibScalar
pm1001rrCtrlWarmReset = _Pm1001rrCtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 1, 5, 3),
    _Pm1001rrCtrlWarmReset_Type()
)
pm1001rrCtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCtrlWarmReset.setStatus("current")
_Pm1001rrCtrlledTest_ObjectIdentity = ObjectIdentity
pm1001rrCtrlledTest = _Pm1001rrCtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 1, 64)
)
_Pm1001rrCtrlGreenLed_Type = EkiOnOff
_Pm1001rrCtrlGreenLed_Object = MibScalar
pm1001rrCtrlGreenLed = _Pm1001rrCtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 1, 64, 1),
    _Pm1001rrCtrlGreenLed_Type()
)
pm1001rrCtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCtrlGreenLed.setStatus("current")
_Pm1001rrCtrlRedLed_Type = EkiOnOff
_Pm1001rrCtrlRedLed_Object = MibScalar
pm1001rrCtrlRedLed = _Pm1001rrCtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 1, 64, 2),
    _Pm1001rrCtrlRedLed_Type()
)
pm1001rrCtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCtrlRedLed.setStatus("current")
_Pm1001rrCtrlLedOff_Type = EkiOnOff
_Pm1001rrCtrlLedOff_Object = MibScalar
pm1001rrCtrlLedOff = _Pm1001rrCtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 1, 64, 3),
    _Pm1001rrCtrlLedOff_Type()
)
pm1001rrCtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCtrlLedOff.setStatus("current")
_Pm1001rrCtrlClient_ObjectIdentity = ObjectIdentity
pm1001rrCtrlClient = _Pm1001rrCtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 2)
)
_Pm1001rrCtrlclientXfpOnoff_ObjectIdentity = ObjectIdentity
pm1001rrCtrlclientXfpOnoff = _Pm1001rrCtrlclientXfpOnoff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 2, 16)
)
_Pm1001rrCtrlClientXfpOnoff_Type = EkiOnOff
_Pm1001rrCtrlClientXfpOnoff_Object = MibScalar
pm1001rrCtrlClientXfpOnoff = _Pm1001rrCtrlClientXfpOnoff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 2, 16, 1),
    _Pm1001rrCtrlClientXfpOnoff_Type()
)
pm1001rrCtrlClientXfpOnoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCtrlClientXfpOnoff.setStatus("current")
_Pm1001rrCtrlclientXfpLineLoop_ObjectIdentity = ObjectIdentity
pm1001rrCtrlclientXfpLineLoop = _Pm1001rrCtrlclientXfpLineLoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 2, 17)
)
_Pm1001rrCtrlClientXfpLineLoop_Type = EkiOnOff
_Pm1001rrCtrlClientXfpLineLoop_Object = MibScalar
pm1001rrCtrlClientXfpLineLoop = _Pm1001rrCtrlClientXfpLineLoop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 2, 17, 1),
    _Pm1001rrCtrlClientXfpLineLoop_Type()
)
pm1001rrCtrlClientXfpLineLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCtrlClientXfpLineLoop.setStatus("current")
_Pm1001rrCtrlclientXfiLoop_ObjectIdentity = ObjectIdentity
pm1001rrCtrlclientXfiLoop = _Pm1001rrCtrlclientXfiLoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 2, 18)
)
_Pm1001rrCtrlClientXfiLoop_Type = EkiOnOff
_Pm1001rrCtrlClientXfiLoop_Object = MibScalar
pm1001rrCtrlClientXfiLoop = _Pm1001rrCtrlClientXfiLoop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 2, 18, 1),
    _Pm1001rrCtrlClientXfiLoop_Type()
)
pm1001rrCtrlClientXfiLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCtrlClientXfiLoop.setStatus("current")
_Pm1001rrCtrlclientTunableChannel_Type = Pm1001rrOtxChannel
_Pm1001rrCtrlclientTunableChannel_Object = MibScalar
pm1001rrCtrlclientTunableChannel = _Pm1001rrCtrlclientTunableChannel_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 2, 19),
    _Pm1001rrCtrlclientTunableChannel_Type()
)
pm1001rrCtrlclientTunableChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCtrlclientTunableChannel.setStatus("current")
_Pm1001rrCtrlclientPhotodiodeMode_Type = Pm1001rrOtxMode
_Pm1001rrCtrlclientPhotodiodeMode_Object = MibScalar
pm1001rrCtrlclientPhotodiodeMode = _Pm1001rrCtrlclientPhotodiodeMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 2, 20),
    _Pm1001rrCtrlclientPhotodiodeMode_Type()
)
pm1001rrCtrlclientPhotodiodeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCtrlclientPhotodiodeMode.setStatus("current")
_Pm1001rrCtrlclientPhotodiodeValue_Type = Pm1001rrAdjustValue
_Pm1001rrCtrlclientPhotodiodeValue_Object = MibScalar
pm1001rrCtrlclientPhotodiodeValue = _Pm1001rrCtrlclientPhotodiodeValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 2, 21),
    _Pm1001rrCtrlclientPhotodiodeValue_Type()
)
pm1001rrCtrlclientPhotodiodeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCtrlclientPhotodiodeValue.setStatus("current")


class _Pm1001rrCtrlclientPowerLaser_Type(Unsigned32):
    """Custom type pm1001rrCtrlclientPowerLaser based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001rrCtrlclientPowerLaser_Type.__name__ = "Unsigned32"
_Pm1001rrCtrlclientPowerLaser_Object = MibScalar
pm1001rrCtrlclientPowerLaser = _Pm1001rrCtrlclientPowerLaser_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 2, 22),
    _Pm1001rrCtrlclientPowerLaser_Type()
)
pm1001rrCtrlclientPowerLaser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCtrlclientPowerLaser.setStatus("current")
_Pm1001rrCtrlLine_ObjectIdentity = ObjectIdentity
pm1001rrCtrlLine = _Pm1001rrCtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 3)
)
_Pm1001rrCtrlclientOtxVlhReset_ObjectIdentity = ObjectIdentity
pm1001rrCtrlclientOtxVlhReset = _Pm1001rrCtrlclientOtxVlhReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 3, 23)
)
_Pm1001rrCtrlClientOtxVlhReset_Type = EkiOnOff
_Pm1001rrCtrlClientOtxVlhReset_Object = MibScalar
pm1001rrCtrlClientOtxVlhReset = _Pm1001rrCtrlClientOtxVlhReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 3, 23, 1),
    _Pm1001rrCtrlClientOtxVlhReset_Type()
)
pm1001rrCtrlClientOtxVlhReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCtrlClientOtxVlhReset.setStatus("current")
_Pm1001rrCtrllineXfpOnoff_ObjectIdentity = ObjectIdentity
pm1001rrCtrllineXfpOnoff = _Pm1001rrCtrllineXfpOnoff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 3, 24)
)
_Pm1001rrCtrlLineXfpOnoff_Type = EkiOnOff
_Pm1001rrCtrlLineXfpOnoff_Object = MibScalar
pm1001rrCtrlLineXfpOnoff = _Pm1001rrCtrlLineXfpOnoff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 3, 24, 1),
    _Pm1001rrCtrlLineXfpOnoff_Type()
)
pm1001rrCtrlLineXfpOnoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCtrlLineXfpOnoff.setStatus("current")
_Pm1001rrCtrllineXfpLineLoop_ObjectIdentity = ObjectIdentity
pm1001rrCtrllineXfpLineLoop = _Pm1001rrCtrllineXfpLineLoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 3, 25)
)
_Pm1001rrCtrlLineXfpLineLoop_Type = EkiOnOff
_Pm1001rrCtrlLineXfpLineLoop_Object = MibScalar
pm1001rrCtrlLineXfpLineLoop = _Pm1001rrCtrlLineXfpLineLoop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 3, 25, 1),
    _Pm1001rrCtrlLineXfpLineLoop_Type()
)
pm1001rrCtrlLineXfpLineLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCtrlLineXfpLineLoop.setStatus("current")
_Pm1001rrCtrllineXfiLoop_ObjectIdentity = ObjectIdentity
pm1001rrCtrllineXfiLoop = _Pm1001rrCtrllineXfiLoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 3, 26)
)
_Pm1001rrCtrlLineXfiLoop_Type = EkiOnOff
_Pm1001rrCtrlLineXfiLoop_Object = MibScalar
pm1001rrCtrlLineXfiLoop = _Pm1001rrCtrlLineXfiLoop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 3, 26, 1),
    _Pm1001rrCtrlLineXfiLoop_Type()
)
pm1001rrCtrlLineXfiLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCtrlLineXfiLoop.setStatus("current")
_Pm1001rrCtrllineTunableChannel_Type = Pm1001rrOtxChannel
_Pm1001rrCtrllineTunableChannel_Object = MibScalar
pm1001rrCtrllineTunableChannel = _Pm1001rrCtrllineTunableChannel_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 3, 27),
    _Pm1001rrCtrllineTunableChannel_Type()
)
pm1001rrCtrllineTunableChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCtrllineTunableChannel.setStatus("current")
_Pm1001rrCtrllinePhotodiodeMode_Type = Pm1001rrOtxMode
_Pm1001rrCtrllinePhotodiodeMode_Object = MibScalar
pm1001rrCtrllinePhotodiodeMode = _Pm1001rrCtrllinePhotodiodeMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 3, 28),
    _Pm1001rrCtrllinePhotodiodeMode_Type()
)
pm1001rrCtrllinePhotodiodeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCtrllinePhotodiodeMode.setStatus("current")
_Pm1001rrCtrllinePhotodiodeValue_Type = Pm1001rrAdjustValue
_Pm1001rrCtrllinePhotodiodeValue_Object = MibScalar
pm1001rrCtrllinePhotodiodeValue = _Pm1001rrCtrllinePhotodiodeValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 3, 29),
    _Pm1001rrCtrllinePhotodiodeValue_Type()
)
pm1001rrCtrllinePhotodiodeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCtrllinePhotodiodeValue.setStatus("current")


class _Pm1001rrCtrllinePowerLaser_Type(Unsigned32):
    """Custom type pm1001rrCtrllinePowerLaser based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001rrCtrllinePowerLaser_Type.__name__ = "Unsigned32"
_Pm1001rrCtrllinePowerLaser_Object = MibScalar
pm1001rrCtrllinePowerLaser = _Pm1001rrCtrllinePowerLaser_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 3, 30),
    _Pm1001rrCtrllinePowerLaser_Type()
)
pm1001rrCtrllinePowerLaser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCtrllinePowerLaser.setStatus("current")
_Pm1001rrCtrllineOtxVlhReset_ObjectIdentity = ObjectIdentity
pm1001rrCtrllineOtxVlhReset = _Pm1001rrCtrllineOtxVlhReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 3, 31)
)
_Pm1001rrCtrlLineOtxVlhReset_Type = EkiOnOff
_Pm1001rrCtrlLineOtxVlhReset_Object = MibScalar
pm1001rrCtrlLineOtxVlhReset = _Pm1001rrCtrlLineOtxVlhReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 6, 3, 31, 1),
    _Pm1001rrCtrlLineOtxVlhReset_Type()
)
pm1001rrCtrlLineOtxVlhReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCtrlLineOtxVlhReset.setStatus("current")
_Pm1001rrri_ObjectIdentity = ObjectIdentity
pm1001rrri = _Pm1001rrri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 7)
)
_Pm1001rrRinvReloadInventory_Type = EkiOnOff
_Pm1001rrRinvReloadInventory_Object = MibScalar
pm1001rrRinvReloadInventory = _Pm1001rrRinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 7, 2),
    _Pm1001rrRinvReloadInventory_Type()
)
pm1001rrRinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrRinvReloadInventory.setStatus("current")
_Pm1001rrRinvHwPlatform_Type = DisplayString
_Pm1001rrRinvHwPlatform_Object = MibScalar
pm1001rrRinvHwPlatform = _Pm1001rrRinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 7, 4),
    _Pm1001rrRinvHwPlatform_Type()
)
pm1001rrRinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrRinvHwPlatform.setStatus("current")
_Pm1001rrRinvSwPlatform_Type = DisplayString
_Pm1001rrRinvSwPlatform_Object = MibScalar
pm1001rrRinvSwPlatform = _Pm1001rrRinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 7, 5),
    _Pm1001rrRinvSwPlatform_Type()
)
pm1001rrRinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrRinvSwPlatform.setStatus("current")
_Pm1001rrRinvClientXFP_Type = DisplayString
_Pm1001rrRinvClientXFP_Object = MibScalar
pm1001rrRinvClientXFP = _Pm1001rrRinvClientXFP_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 7, 6),
    _Pm1001rrRinvClientXFP_Type()
)
pm1001rrRinvClientXFP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrRinvClientXFP.setStatus("current")
_Pm1001rrRinvLineXFP_Type = DisplayString
_Pm1001rrRinvLineXFP_Object = MibScalar
pm1001rrRinvLineXFP = _Pm1001rrRinvLineXFP_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 7, 7),
    _Pm1001rrRinvLineXFP_Type()
)
pm1001rrRinvLineXFP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrRinvLineXFP.setStatus("current")
_Pm1001rrConfig_ObjectIdentity = ObjectIdentity
pm1001rrConfig = _Pm1001rrConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9)
)
_Pm1001rrCfgLsd_ObjectIdentity = ObjectIdentity
pm1001rrCfgLsd = _Pm1001rrCfgLsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 1)
)
_Pm1001rrtableclientLsd_ObjectIdentity = ObjectIdentity
pm1001rrtableclientLsd = _Pm1001rrtableclientLsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 1, 1)
)


class _Pm1001rrCfglsdMode_Type(Unsigned32):
    """Custom type pm1001rrCfglsdMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001rrCfglsdMode_Type.__name__ = "Unsigned32"
_Pm1001rrCfglsdMode_Object = MibScalar
pm1001rrCfglsdMode = _Pm1001rrCfglsdMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 1, 1, 2),
    _Pm1001rrCfglsdMode_Type()
)
pm1001rrCfglsdMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCfglsdMode.setStatus("current")


class _Pm1001rrCfgclientXfpAlarms_Type(Unsigned32):
    """Custom type pm1001rrCfgclientXfpAlarms based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001rrCfgclientXfpAlarms_Type.__name__ = "Unsigned32"
_Pm1001rrCfgclientXfpAlarms_Object = MibScalar
pm1001rrCfgclientXfpAlarms = _Pm1001rrCfgclientXfpAlarms_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 1, 1, 3),
    _Pm1001rrCfgclientXfpAlarms_Type()
)
pm1001rrCfgclientXfpAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCfgclientXfpAlarms.setStatus("current")


class _Pm1001rrCfgclientXfpAbsence_Type(Unsigned32):
    """Custom type pm1001rrCfgclientXfpAbsence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001rrCfgclientXfpAbsence_Type.__name__ = "Unsigned32"
_Pm1001rrCfgclientXfpAbsence_Object = MibScalar
pm1001rrCfgclientXfpAbsence = _Pm1001rrCfgclientXfpAbsence_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 1, 1, 4),
    _Pm1001rrCfgclientXfpAbsence_Type()
)
pm1001rrCfgclientXfpAbsence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCfgclientXfpAbsence.setStatus("current")


class _Pm1001rrCfglineXfpAlarms_Type(Unsigned32):
    """Custom type pm1001rrCfglineXfpAlarms based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001rrCfglineXfpAlarms_Type.__name__ = "Unsigned32"
_Pm1001rrCfglineXfpAlarms_Object = MibScalar
pm1001rrCfglineXfpAlarms = _Pm1001rrCfglineXfpAlarms_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 1, 1, 5),
    _Pm1001rrCfglineXfpAlarms_Type()
)
pm1001rrCfglineXfpAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCfglineXfpAlarms.setStatus("current")


class _Pm1001rrCfglineXfpAbsence_Type(Unsigned32):
    """Custom type pm1001rrCfglineXfpAbsence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001rrCfglineXfpAbsence_Type.__name__ = "Unsigned32"
_Pm1001rrCfglineXfpAbsence_Object = MibScalar
pm1001rrCfglineXfpAbsence = _Pm1001rrCfglineXfpAbsence_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 1, 1, 6),
    _Pm1001rrCfglineXfpAbsence_Type()
)
pm1001rrCfglineXfpAbsence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCfglineXfpAbsence.setStatus("current")
_Pm1001rrCfgStartUp_ObjectIdentity = ObjectIdentity
pm1001rrCfgStartUp = _Pm1001rrCfgStartUp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 2)
)
_Pm1001rrtableclientStartup_ObjectIdentity = ObjectIdentity
pm1001rrtableclientStartup = _Pm1001rrtableclientStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 2, 1)
)


class _Pm1001rrCfgclientXfpCtrl_Type(Unsigned32):
    """Custom type pm1001rrCfgclientXfpCtrl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001rrCfgclientXfpCtrl_Type.__name__ = "Unsigned32"
_Pm1001rrCfgclientXfpCtrl_Object = MibScalar
pm1001rrCfgclientXfpCtrl = _Pm1001rrCfgclientXfpCtrl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 2, 1, 2),
    _Pm1001rrCfgclientXfpCtrl_Type()
)
pm1001rrCfgclientXfpCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCfgclientXfpCtrl.setStatus("current")
_Pm1001rrtablelineStartup_ObjectIdentity = ObjectIdentity
pm1001rrtablelineStartup = _Pm1001rrtablelineStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 2, 2)
)


class _Pm1001rrCfglineXfpCtrl_Type(Unsigned32):
    """Custom type pm1001rrCfglineXfpCtrl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001rrCfglineXfpCtrl_Type.__name__ = "Unsigned32"
_Pm1001rrCfglineXfpCtrl_Object = MibScalar
pm1001rrCfglineXfpCtrl = _Pm1001rrCfglineXfpCtrl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 2, 2, 2),
    _Pm1001rrCfglineXfpCtrl_Type()
)
pm1001rrCfglineXfpCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCfglineXfpCtrl.setStatus("current")


class _Pm1001rrCfgprotocolSelect_Type(Unsigned32):
    """Custom type pm1001rrCfgprotocolSelect based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001rrCfgprotocolSelect_Type.__name__ = "Unsigned32"
_Pm1001rrCfgprotocolSelect_Object = MibScalar
pm1001rrCfgprotocolSelect = _Pm1001rrCfgprotocolSelect_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 2, 2, 18),
    _Pm1001rrCfgprotocolSelect_Type()
)
pm1001rrCfgprotocolSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCfgprotocolSelect.setStatus("current")
_Pm1001rrtableclientOtxtlh_ObjectIdentity = ObjectIdentity
pm1001rrtableclientOtxtlh = _Pm1001rrtableclientOtxtlh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 2, 3)
)


class _Pm1001rrCfgclientDitherControl_Type(Unsigned32):
    """Custom type pm1001rrCfgclientDitherControl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001rrCfgclientDitherControl_Type.__name__ = "Unsigned32"
_Pm1001rrCfgclientDitherControl_Object = MibScalar
pm1001rrCfgclientDitherControl = _Pm1001rrCfgclientDitherControl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 2, 3, 2),
    _Pm1001rrCfgclientDitherControl_Type()
)
pm1001rrCfgclientDitherControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCfgclientDitherControl.setStatus("current")


class _Pm1001rrCfgclientDitherRate_Type(Unsigned32):
    """Custom type pm1001rrCfgclientDitherRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001rrCfgclientDitherRate_Type.__name__ = "Unsigned32"
_Pm1001rrCfgclientDitherRate_Object = MibScalar
pm1001rrCfgclientDitherRate = _Pm1001rrCfgclientDitherRate_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 2, 3, 3),
    _Pm1001rrCfgclientDitherRate_Type()
)
pm1001rrCfgclientDitherRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCfgclientDitherRate.setStatus("current")


class _Pm1001rrCfgclientDitherFhz_Type(Unsigned32):
    """Custom type pm1001rrCfgclientDitherFhz based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001rrCfgclientDitherFhz_Type.__name__ = "Unsigned32"
_Pm1001rrCfgclientDitherFhz_Object = MibScalar
pm1001rrCfgclientDitherFhz = _Pm1001rrCfgclientDitherFhz_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 2, 3, 4),
    _Pm1001rrCfgclientDitherFhz_Type()
)
pm1001rrCfgclientDitherFhz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCfgclientDitherFhz.setStatus("current")


class _Pm1001rrCfgclientPwrLaser_Type(Unsigned32):
    """Custom type pm1001rrCfgclientPwrLaser based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001rrCfgclientPwrLaser_Type.__name__ = "Unsigned32"
_Pm1001rrCfgclientPwrLaser_Object = MibScalar
pm1001rrCfgclientPwrLaser = _Pm1001rrCfgclientPwrLaser_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 2, 3, 5),
    _Pm1001rrCfgclientPwrLaser_Type()
)
pm1001rrCfgclientPwrLaser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCfgclientPwrLaser.setStatus("current")


class _Pm1001rrCfgclientFCurrent_Type(Unsigned32):
    """Custom type pm1001rrCfgclientFCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001rrCfgclientFCurrent_Type.__name__ = "Unsigned32"
_Pm1001rrCfgclientFCurrent_Object = MibScalar
pm1001rrCfgclientFCurrent = _Pm1001rrCfgclientFCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 2, 3, 6),
    _Pm1001rrCfgclientFCurrent_Type()
)
pm1001rrCfgclientFCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCfgclientFCurrent.setStatus("current")


class _Pm1001rrCfgclientGridCurrent_Type(Unsigned32):
    """Custom type pm1001rrCfgclientGridCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001rrCfgclientGridCurrent_Type.__name__ = "Unsigned32"
_Pm1001rrCfgclientGridCurrent_Object = MibScalar
pm1001rrCfgclientGridCurrent = _Pm1001rrCfgclientGridCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 2, 3, 7),
    _Pm1001rrCfgclientGridCurrent_Type()
)
pm1001rrCfgclientGridCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCfgclientGridCurrent.setStatus("current")


class _Pm1001rrCfgclientF0_Type(Unsigned32):
    """Custom type pm1001rrCfgclientF0 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001rrCfgclientF0_Type.__name__ = "Unsigned32"
_Pm1001rrCfgclientF0_Object = MibScalar
pm1001rrCfgclientF0 = _Pm1001rrCfgclientF0_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 2, 3, 8),
    _Pm1001rrCfgclientF0_Type()
)
pm1001rrCfgclientF0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCfgclientF0.setStatus("current")


class _Pm1001rrCfgclientPhotodiodeMode_Type(Unsigned32):
    """Custom type pm1001rrCfgclientPhotodiodeMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001rrCfgclientPhotodiodeMode_Type.__name__ = "Unsigned32"
_Pm1001rrCfgclientPhotodiodeMode_Object = MibScalar
pm1001rrCfgclientPhotodiodeMode = _Pm1001rrCfgclientPhotodiodeMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 2, 3, 10),
    _Pm1001rrCfgclientPhotodiodeMode_Type()
)
pm1001rrCfgclientPhotodiodeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCfgclientPhotodiodeMode.setStatus("current")


class _Pm1001rrCfgclientPhotodiodeValue_Type(Unsigned32):
    """Custom type pm1001rrCfgclientPhotodiodeValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001rrCfgclientPhotodiodeValue_Type.__name__ = "Unsigned32"
_Pm1001rrCfgclientPhotodiodeValue_Object = MibScalar
pm1001rrCfgclientPhotodiodeValue = _Pm1001rrCfgclientPhotodiodeValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 2, 3, 11),
    _Pm1001rrCfgclientPhotodiodeValue_Type()
)
pm1001rrCfgclientPhotodiodeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCfgclientPhotodiodeValue.setStatus("current")
_Pm1001rrtablelineOtxtlh_ObjectIdentity = ObjectIdentity
pm1001rrtablelineOtxtlh = _Pm1001rrtablelineOtxtlh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 2, 4)
)


class _Pm1001rrCfglineDitherControl_Type(Unsigned32):
    """Custom type pm1001rrCfglineDitherControl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001rrCfglineDitherControl_Type.__name__ = "Unsigned32"
_Pm1001rrCfglineDitherControl_Object = MibScalar
pm1001rrCfglineDitherControl = _Pm1001rrCfglineDitherControl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 2, 4, 2),
    _Pm1001rrCfglineDitherControl_Type()
)
pm1001rrCfglineDitherControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCfglineDitherControl.setStatus("current")


class _Pm1001rrCfglineDitherRate_Type(Unsigned32):
    """Custom type pm1001rrCfglineDitherRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001rrCfglineDitherRate_Type.__name__ = "Unsigned32"
_Pm1001rrCfglineDitherRate_Object = MibScalar
pm1001rrCfglineDitherRate = _Pm1001rrCfglineDitherRate_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 2, 4, 3),
    _Pm1001rrCfglineDitherRate_Type()
)
pm1001rrCfglineDitherRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCfglineDitherRate.setStatus("current")


class _Pm1001rrCfglineDitherFhz_Type(Unsigned32):
    """Custom type pm1001rrCfglineDitherFhz based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001rrCfglineDitherFhz_Type.__name__ = "Unsigned32"
_Pm1001rrCfglineDitherFhz_Object = MibScalar
pm1001rrCfglineDitherFhz = _Pm1001rrCfglineDitherFhz_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 2, 4, 4),
    _Pm1001rrCfglineDitherFhz_Type()
)
pm1001rrCfglineDitherFhz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCfglineDitherFhz.setStatus("current")


class _Pm1001rrCfglinePwrLaser_Type(Unsigned32):
    """Custom type pm1001rrCfglinePwrLaser based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001rrCfglinePwrLaser_Type.__name__ = "Unsigned32"
_Pm1001rrCfglinePwrLaser_Object = MibScalar
pm1001rrCfglinePwrLaser = _Pm1001rrCfglinePwrLaser_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 2, 4, 5),
    _Pm1001rrCfglinePwrLaser_Type()
)
pm1001rrCfglinePwrLaser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCfglinePwrLaser.setStatus("current")


class _Pm1001rrCfglineFCurrent_Type(Unsigned32):
    """Custom type pm1001rrCfglineFCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001rrCfglineFCurrent_Type.__name__ = "Unsigned32"
_Pm1001rrCfglineFCurrent_Object = MibScalar
pm1001rrCfglineFCurrent = _Pm1001rrCfglineFCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 2, 4, 6),
    _Pm1001rrCfglineFCurrent_Type()
)
pm1001rrCfglineFCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCfglineFCurrent.setStatus("current")


class _Pm1001rrCfglineGridCurrent_Type(Unsigned32):
    """Custom type pm1001rrCfglineGridCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001rrCfglineGridCurrent_Type.__name__ = "Unsigned32"
_Pm1001rrCfglineGridCurrent_Object = MibScalar
pm1001rrCfglineGridCurrent = _Pm1001rrCfglineGridCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 2, 4, 7),
    _Pm1001rrCfglineGridCurrent_Type()
)
pm1001rrCfglineGridCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCfglineGridCurrent.setStatus("current")


class _Pm1001rrCfglineF0_Type(Unsigned32):
    """Custom type pm1001rrCfglineF0 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001rrCfglineF0_Type.__name__ = "Unsigned32"
_Pm1001rrCfglineF0_Object = MibScalar
pm1001rrCfglineF0 = _Pm1001rrCfglineF0_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 2, 4, 8),
    _Pm1001rrCfglineF0_Type()
)
pm1001rrCfglineF0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCfglineF0.setStatus("current")


class _Pm1001rrCfglinePhotodiodeMode_Type(Unsigned32):
    """Custom type pm1001rrCfglinePhotodiodeMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001rrCfglinePhotodiodeMode_Type.__name__ = "Unsigned32"
_Pm1001rrCfglinePhotodiodeMode_Object = MibScalar
pm1001rrCfglinePhotodiodeMode = _Pm1001rrCfglinePhotodiodeMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 2, 4, 10),
    _Pm1001rrCfglinePhotodiodeMode_Type()
)
pm1001rrCfglinePhotodiodeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCfglinePhotodiodeMode.setStatus("current")


class _Pm1001rrCfglinePhotodiodeValue_Type(Unsigned32):
    """Custom type pm1001rrCfglinePhotodiodeValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001rrCfglinePhotodiodeValue_Type.__name__ = "Unsigned32"
_Pm1001rrCfglinePhotodiodeValue_Object = MibScalar
pm1001rrCfglinePhotodiodeValue = _Pm1001rrCfglinePhotodiodeValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 2, 4, 11),
    _Pm1001rrCfglinePhotodiodeValue_Type()
)
pm1001rrCfglinePhotodiodeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCfglinePhotodiodeValue.setStatus("current")
_Pm1001rrCfgLabels_ObjectIdentity = ObjectIdentity
pm1001rrCfgLabels = _Pm1001rrCfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 3)
)
_Pm1001rrCfgLabelclientTable_Object = MibTable
pm1001rrCfgLabelclientTable = _Pm1001rrCfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 3, 1)
)
if mibBuilder.loadTexts:
    pm1001rrCfgLabelclientTable.setStatus("current")
_Pm1001rrCfgLabelclientEntry_Object = MibTableRow
pm1001rrCfgLabelclientEntry = _Pm1001rrCfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 3, 1, 1)
)
pm1001rrCfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-Pm1001RR-MIB", "pm1001rrCfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pm1001rrCfgLabelclientEntry.setStatus("current")


class _Pm1001rrCfgLabelclientIndex_Type(Integer32):
    """Custom type pm1001rrCfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001rrCfgLabelclientIndex_Type.__name__ = "Integer32"
_Pm1001rrCfgLabelclientIndex_Object = MibTableColumn
pm1001rrCfgLabelclientIndex = _Pm1001rrCfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 3, 1, 1, 1),
    _Pm1001rrCfgLabelclientIndex_Type()
)
pm1001rrCfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrCfgLabelclientIndex.setStatus("current")


class _Pm1001rrCfgLabelclientPortn_Type(DisplayString):
    """Custom type pm1001rrCfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm1001rrCfgLabelclientPortn_Type.__name__ = "DisplayString"
_Pm1001rrCfgLabelclientPortn_Object = MibTableColumn
pm1001rrCfgLabelclientPortn = _Pm1001rrCfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 3, 1, 1, 3),
    _Pm1001rrCfgLabelclientPortn_Type()
)
pm1001rrCfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCfgLabelclientPortn.setStatus("current")
_Pm1001rrCfgLabellineTable_Object = MibTable
pm1001rrCfgLabellineTable = _Pm1001rrCfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 3, 2)
)
if mibBuilder.loadTexts:
    pm1001rrCfgLabellineTable.setStatus("current")
_Pm1001rrCfgLabellineEntry_Object = MibTableRow
pm1001rrCfgLabellineEntry = _Pm1001rrCfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 3, 2, 1)
)
pm1001rrCfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-Pm1001RR-MIB", "pm1001rrCfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pm1001rrCfgLabellineEntry.setStatus("current")


class _Pm1001rrCfgLabellineIndex_Type(Integer32):
    """Custom type pm1001rrCfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001rrCfgLabellineIndex_Type.__name__ = "Integer32"
_Pm1001rrCfgLabellineIndex_Object = MibTableColumn
pm1001rrCfgLabellineIndex = _Pm1001rrCfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 3, 2, 1, 1),
    _Pm1001rrCfgLabellineIndex_Type()
)
pm1001rrCfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrCfgLabellineIndex.setStatus("current")


class _Pm1001rrCfgLabellinePortn_Type(DisplayString):
    """Custom type pm1001rrCfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm1001rrCfgLabellinePortn_Type.__name__ = "DisplayString"
_Pm1001rrCfgLabellinePortn_Object = MibTableColumn
pm1001rrCfgLabellinePortn = _Pm1001rrCfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 3, 2, 1, 3),
    _Pm1001rrCfgLabellinePortn_Type()
)
pm1001rrCfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCfgLabellinePortn.setStatus("current")
_Pm1001rrCfgStartuptablefive_ObjectIdentity = ObjectIdentity
pm1001rrCfgStartuptablefive = _Pm1001rrCfgStartuptablefive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 4)
)
_Pm1001rrCfgOtxtlhcapabilitiesTable_Object = MibTable
pm1001rrCfgOtxtlhcapabilitiesTable = _Pm1001rrCfgOtxtlhcapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 4, 1)
)
if mibBuilder.loadTexts:
    pm1001rrCfgOtxtlhcapabilitiesTable.setStatus("current")
_Pm1001rrCfgOtxtlhcapabilitiesEntry_Object = MibTableRow
pm1001rrCfgOtxtlhcapabilitiesEntry = _Pm1001rrCfgOtxtlhcapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 4, 1, 1)
)
pm1001rrCfgOtxtlhcapabilitiesEntry.setIndexNames(
    (0, "EKINOPS-Pm1001RR-MIB", "pm1001rrCfgOtxtlhcapabilitiesIndex"),
)
if mibBuilder.loadTexts:
    pm1001rrCfgOtxtlhcapabilitiesEntry.setStatus("current")


class _Pm1001rrCfgOtxtlhcapabilitiesIndex_Type(Integer32):
    """Custom type pm1001rrCfgOtxtlhcapabilitiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001rrCfgOtxtlhcapabilitiesIndex_Type.__name__ = "Integer32"
_Pm1001rrCfgOtxtlhcapabilitiesIndex_Object = MibTableColumn
pm1001rrCfgOtxtlhcapabilitiesIndex = _Pm1001rrCfgOtxtlhcapabilitiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 4, 1, 1, 1),
    _Pm1001rrCfgOtxtlhcapabilitiesIndex_Type()
)
pm1001rrCfgOtxtlhcapabilitiesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrCfgOtxtlhcapabilitiesIndex.setStatus("current")


class _Pm1001rrCfgComponentTypePortn_Type(Unsigned32):
    """Custom type pm1001rrCfgComponentTypePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001rrCfgComponentTypePortn_Type.__name__ = "Unsigned32"
_Pm1001rrCfgComponentTypePortn_Object = MibTableColumn
pm1001rrCfgComponentTypePortn = _Pm1001rrCfgComponentTypePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 4, 1, 1, 3),
    _Pm1001rrCfgComponentTypePortn_Type()
)
pm1001rrCfgComponentTypePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrCfgComponentTypePortn.setStatus("current")


class _Pm1001rrCfgMiscellaneousPortn_Type(Unsigned32):
    """Custom type pm1001rrCfgMiscellaneousPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001rrCfgMiscellaneousPortn_Type.__name__ = "Unsigned32"
_Pm1001rrCfgMiscellaneousPortn_Object = MibTableColumn
pm1001rrCfgMiscellaneousPortn = _Pm1001rrCfgMiscellaneousPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 4, 1, 1, 4),
    _Pm1001rrCfgMiscellaneousPortn_Type()
)
pm1001rrCfgMiscellaneousPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrCfgMiscellaneousPortn.setStatus("current")


class _Pm1001rrCfgFirstChannelPortn_Type(Unsigned32):
    """Custom type pm1001rrCfgFirstChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001rrCfgFirstChannelPortn_Type.__name__ = "Unsigned32"
_Pm1001rrCfgFirstChannelPortn_Object = MibTableColumn
pm1001rrCfgFirstChannelPortn = _Pm1001rrCfgFirstChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 4, 1, 1, 5),
    _Pm1001rrCfgFirstChannelPortn_Type()
)
pm1001rrCfgFirstChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrCfgFirstChannelPortn.setStatus("current")


class _Pm1001rrCfgLastChannelPortn_Type(Unsigned32):
    """Custom type pm1001rrCfgLastChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001rrCfgLastChannelPortn_Type.__name__ = "Unsigned32"
_Pm1001rrCfgLastChannelPortn_Object = MibTableColumn
pm1001rrCfgLastChannelPortn = _Pm1001rrCfgLastChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 4, 1, 1, 6),
    _Pm1001rrCfgLastChannelPortn_Type()
)
pm1001rrCfgLastChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrCfgLastChannelPortn.setStatus("current")


class _Pm1001rrCfgGridPortn_Type(Unsigned32):
    """Custom type pm1001rrCfgGridPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001rrCfgGridPortn_Type.__name__ = "Unsigned32"
_Pm1001rrCfgGridPortn_Object = MibTableColumn
pm1001rrCfgGridPortn = _Pm1001rrCfgGridPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 4, 1, 1, 7),
    _Pm1001rrCfgGridPortn_Type()
)
pm1001rrCfgGridPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrCfgGridPortn.setStatus("current")
_Pm1001rrCfgWriteConfiguration_Type = EkiOnOff
_Pm1001rrCfgWriteConfiguration_Object = MibScalar
pm1001rrCfgWriteConfiguration = _Pm1001rrCfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 9, 257),
    _Pm1001rrCfgWriteConfiguration_Type()
)
pm1001rrCfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001rrCfgWriteConfiguration.setStatus("current")
_Pm1001rrtraps_ObjectIdentity = ObjectIdentity
pm1001rrtraps = _Pm1001rrtraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 8, 10)
)


class _Pm1001rrtrapBoardNumber_Type(Integer32):
    """Custom type pm1001rrtrapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm1001rrtrapBoardNumber_Type.__name__ = "Integer32"
_Pm1001rrtrapBoardNumber_Object = MibScalar
pm1001rrtrapBoardNumber = _Pm1001rrtrapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 8, 10, 4),
    _Pm1001rrtrapBoardNumber_Type()
)
pm1001rrtrapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001rrtrapBoardNumber.setStatus("current")

# Managed Objects groups


# Notification objects

pm1001rrLineTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 8, 10, 30)
)
pm1001rrLineTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1001RR-MIB", "pm1001rrAlmLineDdmWarning"),
        ("EKINOPS-Pm1001RR-MIB", "pm1001rrtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1001rrLineTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm1001rrLineTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 8, 10, 31)
)
pm1001rrLineTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1001RR-MIB", "pm1001rrAlmLineDdmWarning"),
        ("EKINOPS-Pm1001RR-MIB", "pm1001rrtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1001rrLineTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm1001rrLineTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 8, 10, 32)
)
pm1001rrLineTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1001RR-MIB", "pm1001rrAlmLineDdmAlm"),
        ("EKINOPS-Pm1001RR-MIB", "pm1001rrtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1001rrLineTrapUrgentGoesOn.setStatus(
        "current"
    )

pm1001rrLineTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 8, 10, 33)
)
pm1001rrLineTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1001RR-MIB", "pm1001rrAlmLineDdmAlm"),
        ("EKINOPS-Pm1001RR-MIB", "pm1001rrtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1001rrLineTrapUrgentGoesOff.setStatus(
        "current"
    )

pm1001rrLineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 8, 10, 34)
)
pm1001rrLineTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm1001RR-MIB", "pm1001rrAlmLineFail"),
        ("EKINOPS-Pm1001RR-MIB", "pm1001rrAlmLineHwFail"),
        ("EKINOPS-Pm1001RR-MIB", "pm1001rrtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1001rrLineTrapCritGoesOn.setStatus(
        "current"
    )

pm1001rrLineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 8, 10, 35)
)
pm1001rrLineTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm1001RR-MIB", "pm1001rrAlmLineFail"),
        ("EKINOPS-Pm1001RR-MIB", "pm1001rrAlmLineHwFail"),
        ("EKINOPS-Pm1001RR-MIB", "pm1001rrtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1001rrLineTrapCritGoesOff.setStatus(
        "current"
    )

pm1001rrClientTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 8, 10, 40)
)
pm1001rrClientTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1001RR-MIB", "pm1001rrAlmClientDdmWarning"),
        ("EKINOPS-Pm1001RR-MIB", "pm1001rrtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1001rrClientTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm1001rrClientTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 8, 10, 41)
)
pm1001rrClientTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1001RR-MIB", "pm1001rrAlmClientDdmWarning"),
        ("EKINOPS-Pm1001RR-MIB", "pm1001rrtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1001rrClientTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm1001rrClientTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 8, 10, 42)
)
pm1001rrClientTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1001RR-MIB", "pm1001rrAlmClientDdmAlm"),
        ("EKINOPS-Pm1001RR-MIB", "pm1001rrtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1001rrClientTrapUrgentGoesOn.setStatus(
        "current"
    )

pm1001rrClientTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 8, 10, 43)
)
pm1001rrClientTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1001RR-MIB", "pm1001rrAlmClientDdmAlm"),
        ("EKINOPS-Pm1001RR-MIB", "pm1001rrtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1001rrClientTrapUrgentGoesOff.setStatus(
        "current"
    )

pm1001rrClientTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 8, 10, 44)
)
pm1001rrClientTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm1001RR-MIB", "pm1001rrAlmClientFail"),
        ("EKINOPS-Pm1001RR-MIB", "pm1001rrAlmClientHwFail"),
        ("EKINOPS-Pm1001RR-MIB", "pm1001rrtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1001rrClientTrapCritGoesOn.setStatus(
        "current"
    )

pm1001rrClientTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 8, 10, 45)
)
pm1001rrClientTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm1001RR-MIB", "pm1001rrAlmClientFail"),
        ("EKINOPS-Pm1001RR-MIB", "pm1001rrAlmClientHwFail"),
        ("EKINOPS-Pm1001RR-MIB", "pm1001rrtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1001rrClientTrapCritGoesOff.setStatus(
        "current"
    )

pm1001rrPowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 8, 10, 50)
)
pm1001rrPowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1001RR-MIB", "pm1001rrAlmDefFuseB"),
        ("EKINOPS-Pm1001RR-MIB", "pm1001rrAlmDefFuseA"),
        ("EKINOPS-Pm1001RR-MIB", "pm1001rrtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1001rrPowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pm1001rrPowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 8, 10, 51)
)
pm1001rrPowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1001RR-MIB", "pm1001rrAlmDefFuseB"),
        ("EKINOPS-Pm1001RR-MIB", "pm1001rrAlmDefFuseA"),
        ("EKINOPS-Pm1001RR-MIB", "pm1001rrtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1001rrPowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Pm1001RR-MIB",
    **{"Pm1001rrBitRate": Pm1001rrBitRate,
       "Pm1001rrOtxMode": Pm1001rrOtxMode,
       "Pm1001rrOtxGrid": Pm1001rrOtxGrid,
       "Pm1001rrAdjustValue": Pm1001rrAdjustValue,
       "Pm1001rrOtxChannel": Pm1001rrOtxChannel,
       "modulePm1001RR": modulePm1001RR,
       "pm1001rralarms": pm1001rralarms,
       "pm1001rrAlmOther": pm1001rrAlmOther,
       "pm1001rrAlmOtherNurg": pm1001rrAlmOtherNurg,
       "pm1001rrAlmOtherUrg": pm1001rrAlmOtherUrg,
       "pm1001rrAlmOtherCrit": pm1001rrAlmOtherCrit,
       "pm1001rrAlmsynthAlm0": pm1001rrAlmsynthAlm0,
       "pm1001rrAlmModuleGlobFailure": pm1001rrAlmModuleGlobFailure,
       "pm1001rrAlmDefFuseA": pm1001rrAlmDefFuseA,
       "pm1001rrAlmDefFuseB": pm1001rrAlmDefFuseB,
       "pm1001rrAlmClient": pm1001rrAlmClient,
       "pm1001rrAlmClientNurg": pm1001rrAlmClientNurg,
       "pm1001rrAlmclientXfpWarnings": pm1001rrAlmclientXfpWarnings,
       "pm1001rrAlmClientTxPwrLowWng": pm1001rrAlmClientTxPwrLowWng,
       "pm1001rrAlmClientTxPwrHighWng": pm1001rrAlmClientTxPwrHighWng,
       "pm1001rrAlmClientTxBiasLowWng": pm1001rrAlmClientTxBiasLowWng,
       "pm1001rrAlmClientTxBiasHighWng": pm1001rrAlmClientTxBiasHighWng,
       "pm1001rrAlmClientTempLowWng": pm1001rrAlmClientTempLowWng,
       "pm1001rrAlmClientTempHighWng": pm1001rrAlmClientTempHighWng,
       "pm1001rrAlmClientRxPwrLowWng": pm1001rrAlmClientRxPwrLowWng,
       "pm1001rrAlmClientRxPwrHighWng": pm1001rrAlmClientRxPwrHighWng,
       "pm1001rrAlmclientOtxTlhWarnings": pm1001rrAlmclientOtxTlhWarnings,
       "pm1001rrAlmClientModulatorAgingHighWarning": pm1001rrAlmClientModulatorAgingHighWarning,
       "pm1001rrAlmClientAgingHighWarning": pm1001rrAlmClientAgingHighWarning,
       "pm1001rrAlmClientFreqDevHighWarning": pm1001rrAlmClientFreqDevHighWarning,
       "pm1001rrAlmClientLaserTempHighWarning": pm1001rrAlmClientLaserTempHighWarning,
       "pm1001rrAlmClientUrg": pm1001rrAlmClientUrg,
       "pm1001rrAlmclientXfpAlarm1": pm1001rrAlmclientXfpAlarm1,
       "pm1001rrAlmClientTxPwrLowAla": pm1001rrAlmClientTxPwrLowAla,
       "pm1001rrAlmClientTxPwrHighAla": pm1001rrAlmClientTxPwrHighAla,
       "pm1001rrAlmClientTxBiasLowAla": pm1001rrAlmClientTxBiasLowAla,
       "pm1001rrAlmClientTxBiasHighAla": pm1001rrAlmClientTxBiasHighAla,
       "pm1001rrAlmClientTempLowAla": pm1001rrAlmClientTempLowAla,
       "pm1001rrAlmClientTempHighAla": pm1001rrAlmClientTempHighAla,
       "pm1001rrAlmClientRxPwrLowAla": pm1001rrAlmClientRxPwrLowAla,
       "pm1001rrAlmClientRxPwrHighAla": pm1001rrAlmClientRxPwrHighAla,
       "pm1001rrAlmclientOtxTlhAlarms3": pm1001rrAlmclientOtxTlhAlarms3,
       "pm1001rrAlmClientModulatorAgingHighAla": pm1001rrAlmClientModulatorAgingHighAla,
       "pm1001rrAlmClientAgingHighAla": pm1001rrAlmClientAgingHighAla,
       "pm1001rrAlmClientCdrNotReady": pm1001rrAlmClientCdrNotReady,
       "pm1001rrAlmClientFreqDevHighAla": pm1001rrAlmClientFreqDevHighAla,
       "pm1001rrAlmClientLaserTempHighAla": pm1001rrAlmClientLaserTempHighAla,
       "pm1001rrAlmClientCrit": pm1001rrAlmClientCrit,
       "pm1001rrAlmsynthAlm8": pm1001rrAlmsynthAlm8,
       "pm1001rrAlmClientXfpAbsent": pm1001rrAlmClientXfpAbsent,
       "pm1001rrAlmClientInitNotCompl": pm1001rrAlmClientInitNotCompl,
       "pm1001rrAlmClientHwFail": pm1001rrAlmClientHwFail,
       "pm1001rrAlmClientXfpTxOff": pm1001rrAlmClientXfpTxOff,
       "pm1001rrAlmClientDdmWarning": pm1001rrAlmClientDdmWarning,
       "pm1001rrAlmClientDdmAlm": pm1001rrAlmClientDdmAlm,
       "pm1001rrAlmClientFail": pm1001rrAlmClientFail,
       "pm1001rrAlmClientVccWarning": pm1001rrAlmClientVccWarning,
       "pm1001rrAlmClientVccAlarm": pm1001rrAlmClientVccAlarm,
       "pm1001rrAlmclientXfpAlarms2": pm1001rrAlmclientXfpAlarms2,
       "pm1001rrAlmClientResetComplete": pm1001rrAlmClientResetComplete,
       "pm1001rrAlmClientRxCdrNotLocked": pm1001rrAlmClientRxCdrNotLocked,
       "pm1001rrAlmClientRxLos": pm1001rrAlmClientRxLos,
       "pm1001rrAlmClientRxNr": pm1001rrAlmClientRxNr,
       "pm1001rrAlmClientTxCdrNotLocked": pm1001rrAlmClientTxCdrNotLocked,
       "pm1001rrAlmClientTxFault": pm1001rrAlmClientTxFault,
       "pm1001rrAlmClientTxNr": pm1001rrAlmClientTxNr,
       "pm1001rrAlmClientChannelNotAcquired": pm1001rrAlmClientChannelNotAcquired,
       "pm1001rrAlmClientWavelengthUnlocked": pm1001rrAlmClientWavelengthUnlocked,
       "pm1001rrAlmClientTecFault": pm1001rrAlmClientTecFault,
       "pm1001rrAlmClientApdSupplyFault": pm1001rrAlmClientApdSupplyFault,
       "pm1001rrAlmLine": pm1001rrAlmLine,
       "pm1001rrAlmLineNurg": pm1001rrAlmLineNurg,
       "pm1001rrAlmlineXfpWarnings": pm1001rrAlmlineXfpWarnings,
       "pm1001rrAlmLineTxPwrLowWng": pm1001rrAlmLineTxPwrLowWng,
       "pm1001rrAlmLineTxPwrHighWng": pm1001rrAlmLineTxPwrHighWng,
       "pm1001rrAlmLineTxBiasLowWng": pm1001rrAlmLineTxBiasLowWng,
       "pm1001rrAlmLineTxBiasHighWng": pm1001rrAlmLineTxBiasHighWng,
       "pm1001rrAlmLineTempLowWng": pm1001rrAlmLineTempLowWng,
       "pm1001rrAlmLineTempHighWng": pm1001rrAlmLineTempHighWng,
       "pm1001rrAlmLineRxPwrLowWng": pm1001rrAlmLineRxPwrLowWng,
       "pm1001rrAlmLineRxPwrHighWng": pm1001rrAlmLineRxPwrHighWng,
       "pm1001rrAlmrrLineOtxTlhWarnings": pm1001rrAlmrrLineOtxTlhWarnings,
       "pm1001rrAlmLineModulatorAgingHighWarning": pm1001rrAlmLineModulatorAgingHighWarning,
       "pm1001rrAlmLineAgingHighWarning": pm1001rrAlmLineAgingHighWarning,
       "pm1001rrAlmLineFreqDevHighWarning": pm1001rrAlmLineFreqDevHighWarning,
       "pm1001rrAlmLineLaserTempHighWarning": pm1001rrAlmLineLaserTempHighWarning,
       "pm1001rrAlmLineUrg": pm1001rrAlmLineUrg,
       "pm1001rrAlmlineXfpAlarm1": pm1001rrAlmlineXfpAlarm1,
       "pm1001rrAlmLineTxPwrLowAla": pm1001rrAlmLineTxPwrLowAla,
       "pm1001rrAlmLineTxPwrHighAla": pm1001rrAlmLineTxPwrHighAla,
       "pm1001rrAlmLineTxBiasLowAla": pm1001rrAlmLineTxBiasLowAla,
       "pm1001rrAlmLineTxBiasHighAla": pm1001rrAlmLineTxBiasHighAla,
       "pm1001rrAlmLineTempLowAla": pm1001rrAlmLineTempLowAla,
       "pm1001rrAlmLineTempHighAla": pm1001rrAlmLineTempHighAla,
       "pm1001rrAlmLineRxPwrLowAla": pm1001rrAlmLineRxPwrLowAla,
       "pm1001rrAlmLineRxPwrHighAla": pm1001rrAlmLineRxPwrHighAla,
       "pm1001rrAlmrrLineOtxTlhAlarms3": pm1001rrAlmrrLineOtxTlhAlarms3,
       "pm1001rrAlmLineModulatorAgingHighAla": pm1001rrAlmLineModulatorAgingHighAla,
       "pm1001rrAlmLineAgingHighAla": pm1001rrAlmLineAgingHighAla,
       "pm1001rrAlmLineCdrNotReady": pm1001rrAlmLineCdrNotReady,
       "pm1001rrAlmLineFreqDevHighAla": pm1001rrAlmLineFreqDevHighAla,
       "pm1001rrAlmLineLaserTempHighAla": pm1001rrAlmLineLaserTempHighAla,
       "pm1001rrAlmLineCrit": pm1001rrAlmLineCrit,
       "pm1001rrAlmsynthAlm7": pm1001rrAlmsynthAlm7,
       "pm1001rrAlmLineXfpAbsent": pm1001rrAlmLineXfpAbsent,
       "pm1001rrAlmLineInitNotCompl": pm1001rrAlmLineInitNotCompl,
       "pm1001rrAlmLineHwFail": pm1001rrAlmLineHwFail,
       "pm1001rrAlmLineXfpTxOff": pm1001rrAlmLineXfpTxOff,
       "pm1001rrAlmLineDdmWarning": pm1001rrAlmLineDdmWarning,
       "pm1001rrAlmLineDdmAlm": pm1001rrAlmLineDdmAlm,
       "pm1001rrAlmLineFail": pm1001rrAlmLineFail,
       "pm1001rrAlmLineVccWarning": pm1001rrAlmLineVccWarning,
       "pm1001rrAlmLineVccAlarm": pm1001rrAlmLineVccAlarm,
       "pm1001rrAlmlineXfpAlarms2": pm1001rrAlmlineXfpAlarms2,
       "pm1001rrAlmLineResetComplete": pm1001rrAlmLineResetComplete,
       "pm1001rrAlmLineRxCdrNotLocked": pm1001rrAlmLineRxCdrNotLocked,
       "pm1001rrAlmLineRxLos": pm1001rrAlmLineRxLos,
       "pm1001rrAlmLineRxNr": pm1001rrAlmLineRxNr,
       "pm1001rrAlmLineTxCdrNotLocked": pm1001rrAlmLineTxCdrNotLocked,
       "pm1001rrAlmLineTxFault": pm1001rrAlmLineTxFault,
       "pm1001rrAlmLineTxNr": pm1001rrAlmLineTxNr,
       "pm1001rrAlmLineChannelNotAcquired": pm1001rrAlmLineChannelNotAcquired,
       "pm1001rrAlmLineWavelengthUnlocked": pm1001rrAlmLineWavelengthUnlocked,
       "pm1001rrAlmLineTecFault": pm1001rrAlmLineTecFault,
       "pm1001rrAlmLineApdSupplyFault": pm1001rrAlmLineApdSupplyFault,
       "pm1001rrmeasures": pm1001rrmeasures,
       "pm1001rrMesrOther": pm1001rrMesrOther,
       "pm1001rrMesrClient": pm1001rrMesrClient,
       "pm1001rrMesrclientTemperature": pm1001rrMesrclientTemperature,
       "pm1001rrMesrclientTxBias": pm1001rrMesrclientTxBias,
       "pm1001rrMesrclientTxPower": pm1001rrMesrclientTxPower,
       "pm1001rrMesrclientRxPower": pm1001rrMesrclientRxPower,
       "pm1001rrMesrclientAging": pm1001rrMesrclientAging,
       "pm1001rrMesrclientLaserTemperature": pm1001rrMesrclientLaserTemperature,
       "pm1001rrMesrclientFreqDeviation": pm1001rrMesrclientFreqDeviation,
       "pm1001rrMesrclientLaserWvlength": pm1001rrMesrclientLaserWvlength,
       "pm1001rrMesrLine": pm1001rrMesrLine,
       "pm1001rrMesrlineTemperature": pm1001rrMesrlineTemperature,
       "pm1001rrMesrlineTxBias": pm1001rrMesrlineTxBias,
       "pm1001rrMesrlineTxPower": pm1001rrMesrlineTxPower,
       "pm1001rrMesrlineRxPower": pm1001rrMesrlineRxPower,
       "pm1001rrMesrlineAging": pm1001rrMesrlineAging,
       "pm1001rrMesrlineLaserTemperature": pm1001rrMesrlineLaserTemperature,
       "pm1001rrMesrlineFreqDeviation": pm1001rrMesrlineFreqDeviation,
       "pm1001rrMesrlineLaserWvlength": pm1001rrMesrlineLaserWvlength,
       "pm1001rrcontrolsWrite": pm1001rrcontrolsWrite,
       "pm1001rrCtrlOther": pm1001rrCtrlOther,
       "pm1001rrCtrlsynth0": pm1001rrCtrlsynth0,
       "pm1001rrCtrlConfLoad": pm1001rrCtrlConfLoad,
       "pm1001rrCtrlConfFlash": pm1001rrCtrlConfFlash,
       "pm1001rrCtrlConfClear": pm1001rrCtrlConfClear,
       "pm1001rrCtrlsynth4": pm1001rrCtrlsynth4,
       "pm1001rrCtrlCorrelatOn": pm1001rrCtrlCorrelatOn,
       "pm1001rrCtrlCorrelatOff": pm1001rrCtrlCorrelatOff,
       "pm1001rrCtrlswMgnt": pm1001rrCtrlswMgnt,
       "pm1001rrCtrlColdReset": pm1001rrCtrlColdReset,
       "pm1001rrCtrlWarmReset": pm1001rrCtrlWarmReset,
       "pm1001rrCtrlledTest": pm1001rrCtrlledTest,
       "pm1001rrCtrlGreenLed": pm1001rrCtrlGreenLed,
       "pm1001rrCtrlRedLed": pm1001rrCtrlRedLed,
       "pm1001rrCtrlLedOff": pm1001rrCtrlLedOff,
       "pm1001rrCtrlClient": pm1001rrCtrlClient,
       "pm1001rrCtrlclientXfpOnoff": pm1001rrCtrlclientXfpOnoff,
       "pm1001rrCtrlClientXfpOnoff": pm1001rrCtrlClientXfpOnoff,
       "pm1001rrCtrlclientXfpLineLoop": pm1001rrCtrlclientXfpLineLoop,
       "pm1001rrCtrlClientXfpLineLoop": pm1001rrCtrlClientXfpLineLoop,
       "pm1001rrCtrlclientXfiLoop": pm1001rrCtrlclientXfiLoop,
       "pm1001rrCtrlClientXfiLoop": pm1001rrCtrlClientXfiLoop,
       "pm1001rrCtrlclientTunableChannel": pm1001rrCtrlclientTunableChannel,
       "pm1001rrCtrlclientPhotodiodeMode": pm1001rrCtrlclientPhotodiodeMode,
       "pm1001rrCtrlclientPhotodiodeValue": pm1001rrCtrlclientPhotodiodeValue,
       "pm1001rrCtrlclientPowerLaser": pm1001rrCtrlclientPowerLaser,
       "pm1001rrCtrlLine": pm1001rrCtrlLine,
       "pm1001rrCtrlclientOtxVlhReset": pm1001rrCtrlclientOtxVlhReset,
       "pm1001rrCtrlClientOtxVlhReset": pm1001rrCtrlClientOtxVlhReset,
       "pm1001rrCtrllineXfpOnoff": pm1001rrCtrllineXfpOnoff,
       "pm1001rrCtrlLineXfpOnoff": pm1001rrCtrlLineXfpOnoff,
       "pm1001rrCtrllineXfpLineLoop": pm1001rrCtrllineXfpLineLoop,
       "pm1001rrCtrlLineXfpLineLoop": pm1001rrCtrlLineXfpLineLoop,
       "pm1001rrCtrllineXfiLoop": pm1001rrCtrllineXfiLoop,
       "pm1001rrCtrlLineXfiLoop": pm1001rrCtrlLineXfiLoop,
       "pm1001rrCtrllineTunableChannel": pm1001rrCtrllineTunableChannel,
       "pm1001rrCtrllinePhotodiodeMode": pm1001rrCtrllinePhotodiodeMode,
       "pm1001rrCtrllinePhotodiodeValue": pm1001rrCtrllinePhotodiodeValue,
       "pm1001rrCtrllinePowerLaser": pm1001rrCtrllinePowerLaser,
       "pm1001rrCtrllineOtxVlhReset": pm1001rrCtrllineOtxVlhReset,
       "pm1001rrCtrlLineOtxVlhReset": pm1001rrCtrlLineOtxVlhReset,
       "pm1001rrri": pm1001rrri,
       "pm1001rrRinvReloadInventory": pm1001rrRinvReloadInventory,
       "pm1001rrRinvHwPlatform": pm1001rrRinvHwPlatform,
       "pm1001rrRinvSwPlatform": pm1001rrRinvSwPlatform,
       "pm1001rrRinvClientXFP": pm1001rrRinvClientXFP,
       "pm1001rrRinvLineXFP": pm1001rrRinvLineXFP,
       "pm1001rrConfig": pm1001rrConfig,
       "pm1001rrCfgLsd": pm1001rrCfgLsd,
       "pm1001rrtableclientLsd": pm1001rrtableclientLsd,
       "pm1001rrCfglsdMode": pm1001rrCfglsdMode,
       "pm1001rrCfgclientXfpAlarms": pm1001rrCfgclientXfpAlarms,
       "pm1001rrCfgclientXfpAbsence": pm1001rrCfgclientXfpAbsence,
       "pm1001rrCfglineXfpAlarms": pm1001rrCfglineXfpAlarms,
       "pm1001rrCfglineXfpAbsence": pm1001rrCfglineXfpAbsence,
       "pm1001rrCfgStartUp": pm1001rrCfgStartUp,
       "pm1001rrtableclientStartup": pm1001rrtableclientStartup,
       "pm1001rrCfgclientXfpCtrl": pm1001rrCfgclientXfpCtrl,
       "pm1001rrtablelineStartup": pm1001rrtablelineStartup,
       "pm1001rrCfglineXfpCtrl": pm1001rrCfglineXfpCtrl,
       "pm1001rrCfgprotocolSelect": pm1001rrCfgprotocolSelect,
       "pm1001rrtableclientOtxtlh": pm1001rrtableclientOtxtlh,
       "pm1001rrCfgclientDitherControl": pm1001rrCfgclientDitherControl,
       "pm1001rrCfgclientDitherRate": pm1001rrCfgclientDitherRate,
       "pm1001rrCfgclientDitherFhz": pm1001rrCfgclientDitherFhz,
       "pm1001rrCfgclientPwrLaser": pm1001rrCfgclientPwrLaser,
       "pm1001rrCfgclientFCurrent": pm1001rrCfgclientFCurrent,
       "pm1001rrCfgclientGridCurrent": pm1001rrCfgclientGridCurrent,
       "pm1001rrCfgclientF0": pm1001rrCfgclientF0,
       "pm1001rrCfgclientPhotodiodeMode": pm1001rrCfgclientPhotodiodeMode,
       "pm1001rrCfgclientPhotodiodeValue": pm1001rrCfgclientPhotodiodeValue,
       "pm1001rrtablelineOtxtlh": pm1001rrtablelineOtxtlh,
       "pm1001rrCfglineDitherControl": pm1001rrCfglineDitherControl,
       "pm1001rrCfglineDitherRate": pm1001rrCfglineDitherRate,
       "pm1001rrCfglineDitherFhz": pm1001rrCfglineDitherFhz,
       "pm1001rrCfglinePwrLaser": pm1001rrCfglinePwrLaser,
       "pm1001rrCfglineFCurrent": pm1001rrCfglineFCurrent,
       "pm1001rrCfglineGridCurrent": pm1001rrCfglineGridCurrent,
       "pm1001rrCfglineF0": pm1001rrCfglineF0,
       "pm1001rrCfglinePhotodiodeMode": pm1001rrCfglinePhotodiodeMode,
       "pm1001rrCfglinePhotodiodeValue": pm1001rrCfglinePhotodiodeValue,
       "pm1001rrCfgLabels": pm1001rrCfgLabels,
       "pm1001rrCfgLabelclientTable": pm1001rrCfgLabelclientTable,
       "pm1001rrCfgLabelclientEntry": pm1001rrCfgLabelclientEntry,
       "pm1001rrCfgLabelclientIndex": pm1001rrCfgLabelclientIndex,
       "pm1001rrCfgLabelclientPortn": pm1001rrCfgLabelclientPortn,
       "pm1001rrCfgLabellineTable": pm1001rrCfgLabellineTable,
       "pm1001rrCfgLabellineEntry": pm1001rrCfgLabellineEntry,
       "pm1001rrCfgLabellineIndex": pm1001rrCfgLabellineIndex,
       "pm1001rrCfgLabellinePortn": pm1001rrCfgLabellinePortn,
       "pm1001rrCfgStartuptablefive": pm1001rrCfgStartuptablefive,
       "pm1001rrCfgOtxtlhcapabilitiesTable": pm1001rrCfgOtxtlhcapabilitiesTable,
       "pm1001rrCfgOtxtlhcapabilitiesEntry": pm1001rrCfgOtxtlhcapabilitiesEntry,
       "pm1001rrCfgOtxtlhcapabilitiesIndex": pm1001rrCfgOtxtlhcapabilitiesIndex,
       "pm1001rrCfgComponentTypePortn": pm1001rrCfgComponentTypePortn,
       "pm1001rrCfgMiscellaneousPortn": pm1001rrCfgMiscellaneousPortn,
       "pm1001rrCfgFirstChannelPortn": pm1001rrCfgFirstChannelPortn,
       "pm1001rrCfgLastChannelPortn": pm1001rrCfgLastChannelPortn,
       "pm1001rrCfgGridPortn": pm1001rrCfgGridPortn,
       "pm1001rrCfgWriteConfiguration": pm1001rrCfgWriteConfiguration,
       "pm1001rrtraps": pm1001rrtraps,
       "pm1001rrtrapBoardNumber": pm1001rrtrapBoardNumber,
       "pm1001rrLineTrapNotUrgentGoesOn": pm1001rrLineTrapNotUrgentGoesOn,
       "pm1001rrLineTrapNotUrgentGoesOff": pm1001rrLineTrapNotUrgentGoesOff,
       "pm1001rrLineTrapUrgentGoesOn": pm1001rrLineTrapUrgentGoesOn,
       "pm1001rrLineTrapUrgentGoesOff": pm1001rrLineTrapUrgentGoesOff,
       "pm1001rrLineTrapCritGoesOn": pm1001rrLineTrapCritGoesOn,
       "pm1001rrLineTrapCritGoesOff": pm1001rrLineTrapCritGoesOff,
       "pm1001rrClientTrapNotUrgentGoesOn": pm1001rrClientTrapNotUrgentGoesOn,
       "pm1001rrClientTrapNotUrgentGoesOff": pm1001rrClientTrapNotUrgentGoesOff,
       "pm1001rrClientTrapUrgentGoesOn": pm1001rrClientTrapUrgentGoesOn,
       "pm1001rrClientTrapUrgentGoesOff": pm1001rrClientTrapUrgentGoesOff,
       "pm1001rrClientTrapCritGoesOn": pm1001rrClientTrapCritGoesOn,
       "pm1001rrClientTrapCritGoesOff": pm1001rrClientTrapCritGoesOff,
       "pm1001rrPowerTrapUrgentGoesOn": pm1001rrPowerTrapUrgentGoesOn,
       "pm1001rrPowerTrapUrgentGoesOff": pm1001rrPowerTrapUrgentGoesOff}
)
