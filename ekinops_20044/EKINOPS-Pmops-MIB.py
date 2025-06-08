# SNMP MIB module (EKINOPS-Pmops-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Pmops-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 12:01:49 2025
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

modulePmops = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30)
)
if mibBuilder.loadTexts:
    modulePmops.setRevisions(
        ("2007-12-11 00:00",
         "2008-01-23 00:00",
         "2009-09-24 00:00",
         "2010-02-26 00:00",
         "2010-05-27 00:00",
         "2010-11-04 00:00",
         "2010-12-15 00:00",
         "2012-07-04 00:00",
         "2014-03-26 00:00",
         "2014-11-21 00:00",
         "2016-05-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PmopsSwitchMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("switchManual1", 1),
          ("switchManual2", 2),
          ("switchAuto", 4),
          ("switchAutoRevertive", 8))
    )



# MIB Managed Objects in the order of their OIDs

_Pmopsalarms_ObjectIdentity = ObjectIdentity
pmopsalarms = _Pmopsalarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2)
)
_PmopsAlmOther_ObjectIdentity = ObjectIdentity
pmopsAlmOther = _PmopsAlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 1)
)
_PmopsAlmOtherNurg_ObjectIdentity = ObjectIdentity
pmopsAlmOtherNurg = _PmopsAlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 1, 1)
)
_PmopsAlmsynthAlm2_ObjectIdentity = ObjectIdentity
pmopsAlmsynthAlm2 = _PmopsAlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 1, 1, 2)
)
_PmopsAlmConfTableSave_Type = EkiOnOff
_PmopsAlmConfTableSave_Object = MibScalar
pmopsAlmConfTableSave = _PmopsAlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 1, 1, 2, 1),
    _PmopsAlmConfTableSave_Type()
)
pmopsAlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmConfTableSave.setStatus("current")
_PmopsAlmInvUpload_Type = EkiOnOff
_PmopsAlmInvUpload_Object = MibScalar
pmopsAlmInvUpload = _PmopsAlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 1, 1, 2, 2),
    _PmopsAlmInvUpload_Type()
)
pmopsAlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmInvUpload.setStatus("current")
_PmopsAlmConfTableLoad_Type = EkiOnOff
_PmopsAlmConfTableLoad_Object = MibScalar
pmopsAlmConfTableLoad = _PmopsAlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 1, 1, 2, 3),
    _PmopsAlmConfTableLoad_Type()
)
pmopsAlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmConfTableLoad.setStatus("current")
_PmopsAlmCorrelatOff_Type = EkiOnOff
_PmopsAlmCorrelatOff_Object = MibScalar
pmopsAlmCorrelatOff = _PmopsAlmCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 1, 1, 2, 4),
    _PmopsAlmCorrelatOff_Type()
)
pmopsAlmCorrelatOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmCorrelatOff.setStatus("current")
_PmopsAlmOtherUrg_ObjectIdentity = ObjectIdentity
pmopsAlmOtherUrg = _PmopsAlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 1, 2)
)
_PmopsAlmmodInitFailLevel2_ObjectIdentity = ObjectIdentity
pmopsAlmmodInitFailLevel2 = _PmopsAlmmodInitFailLevel2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 1, 2, 70)
)
_PmopsAlmRegReadFail_Type = EkiOnOff
_PmopsAlmRegReadFail_Object = MibScalar
pmopsAlmRegReadFail = _PmopsAlmRegReadFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 1, 2, 70, 1),
    _PmopsAlmRegReadFail_Type()
)
pmopsAlmRegReadFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmRegReadFail.setStatus("current")
_PmopsAlmResetHwInitFail_Type = EkiOnOff
_PmopsAlmResetHwInitFail_Object = MibScalar
pmopsAlmResetHwInitFail = _PmopsAlmResetHwInitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 1, 2, 70, 2),
    _PmopsAlmResetHwInitFail_Type()
)
pmopsAlmResetHwInitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmResetHwInitFail.setStatus("current")
_PmopsAlmConfReadFail_Type = EkiOnOff
_PmopsAlmConfReadFail_Object = MibScalar
pmopsAlmConfReadFail = _PmopsAlmConfReadFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 1, 2, 70, 3),
    _PmopsAlmConfReadFail_Type()
)
pmopsAlmConfReadFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmConfReadFail.setStatus("current")
_PmopsAlmGwIdentFail_Type = EkiOnOff
_PmopsAlmGwIdentFail_Object = MibScalar
pmopsAlmGwIdentFail = _PmopsAlmGwIdentFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 1, 2, 70, 5),
    _PmopsAlmGwIdentFail_Type()
)
pmopsAlmGwIdentFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmGwIdentFail.setStatus("current")
_PmopsAlmCalibReadFail_Type = EkiOnOff
_PmopsAlmCalibReadFail_Object = MibScalar
pmopsAlmCalibReadFail = _PmopsAlmCalibReadFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 1, 2, 70, 6),
    _PmopsAlmCalibReadFail_Type()
)
pmopsAlmCalibReadFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmCalibReadFail.setStatus("current")
_PmopsAlmThreshConfFail_Type = EkiOnOff
_PmopsAlmThreshConfFail_Object = MibScalar
pmopsAlmThreshConfFail = _PmopsAlmThreshConfFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 1, 2, 70, 7),
    _PmopsAlmThreshConfFail_Type()
)
pmopsAlmThreshConfFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmThreshConfFail.setStatus("current")
_PmopsAlmmodInitFailLevel3_ObjectIdentity = ObjectIdentity
pmopsAlmmodInitFailLevel3 = _PmopsAlmmodInitFailLevel3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 1, 2, 71)
)
_PmopsAlmOptIdentFail_Type = EkiOnOff
_PmopsAlmOptIdentFail_Object = MibScalar
pmopsAlmOptIdentFail = _PmopsAlmOptIdentFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 1, 2, 71, 1),
    _PmopsAlmOptIdentFail_Type()
)
pmopsAlmOptIdentFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmOptIdentFail.setStatus("current")
_PmopsAlmGwColdBootForced_Type = EkiOnOff
_PmopsAlmGwColdBootForced_Object = MibScalar
pmopsAlmGwColdBootForced = _PmopsAlmGwColdBootForced_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 1, 2, 71, 5),
    _PmopsAlmGwColdBootForced_Type()
)
pmopsAlmGwColdBootForced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmGwColdBootForced.setStatus("current")
_PmopsAlmOtherCrit_ObjectIdentity = ObjectIdentity
pmopsAlmOtherCrit = _PmopsAlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 1, 3)
)
_PmopsAlmsynthAlm0_ObjectIdentity = ObjectIdentity
pmopsAlmsynthAlm0 = _PmopsAlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 1, 3, 0)
)
_PmopsAlmModuleGlobFailure_Type = EkiOnOff
_PmopsAlmModuleGlobFailure_Object = MibScalar
pmopsAlmModuleGlobFailure = _PmopsAlmModuleGlobFailure_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 1, 3, 0, 9),
    _PmopsAlmModuleGlobFailure_Type()
)
pmopsAlmModuleGlobFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmModuleGlobFailure.setStatus("current")
_PmopsAlmDefFuseA_Type = EkiOnOff
_PmopsAlmDefFuseA_Object = MibScalar
pmopsAlmDefFuseA = _PmopsAlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 1, 3, 0, 15),
    _PmopsAlmDefFuseA_Type()
)
pmopsAlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmDefFuseA.setStatus("current")
_PmopsAlmDefFuseB_Type = EkiOnOff
_PmopsAlmDefFuseB_Object = MibScalar
pmopsAlmDefFuseB = _PmopsAlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 1, 3, 0, 16),
    _PmopsAlmDefFuseB_Type()
)
pmopsAlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmDefFuseB.setStatus("current")
_PmopsAlmComa_ObjectIdentity = ObjectIdentity
pmopsAlmComa = _PmopsAlmComa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 2)
)
_PmopsAlmComaNurg_ObjectIdentity = ObjectIdentity
pmopsAlmComaNurg = _PmopsAlmComaNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 2, 1)
)
_PmopsAlmcomaMeasWng_ObjectIdentity = ObjectIdentity
pmopsAlmcomaMeasWng = _PmopsAlmcomaMeasWng_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 2, 1, 18)
)
_PmopsAlmComaTx1PwrLowWng_Type = EkiOnOff
_PmopsAlmComaTx1PwrLowWng_Object = MibScalar
pmopsAlmComaTx1PwrLowWng = _PmopsAlmComaTx1PwrLowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 2, 1, 18, 1),
    _PmopsAlmComaTx1PwrLowWng_Type()
)
pmopsAlmComaTx1PwrLowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmComaTx1PwrLowWng.setStatus("current")
_PmopsAlmComaTx1PwrHighWng_Type = EkiOnOff
_PmopsAlmComaTx1PwrHighWng_Object = MibScalar
pmopsAlmComaTx1PwrHighWng = _PmopsAlmComaTx1PwrHighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 2, 1, 18, 2),
    _PmopsAlmComaTx1PwrHighWng_Type()
)
pmopsAlmComaTx1PwrHighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmComaTx1PwrHighWng.setStatus("current")
_PmopsAlmComaRx1PwrLowWng_Type = EkiOnOff
_PmopsAlmComaRx1PwrLowWng_Object = MibScalar
pmopsAlmComaRx1PwrLowWng = _PmopsAlmComaRx1PwrLowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 2, 1, 18, 3),
    _PmopsAlmComaRx1PwrLowWng_Type()
)
pmopsAlmComaRx1PwrLowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmComaRx1PwrLowWng.setStatus("current")
_PmopsAlmComaRx1PwrHighWng_Type = EkiOnOff
_PmopsAlmComaRx1PwrHighWng_Object = MibScalar
pmopsAlmComaRx1PwrHighWng = _PmopsAlmComaRx1PwrHighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 2, 1, 18, 4),
    _PmopsAlmComaRx1PwrHighWng_Type()
)
pmopsAlmComaRx1PwrHighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmComaRx1PwrHighWng.setStatus("current")
_PmopsAlmComaTx2PwrLowWng_Type = EkiOnOff
_PmopsAlmComaTx2PwrLowWng_Object = MibScalar
pmopsAlmComaTx2PwrLowWng = _PmopsAlmComaTx2PwrLowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 2, 1, 18, 5),
    _PmopsAlmComaTx2PwrLowWng_Type()
)
pmopsAlmComaTx2PwrLowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmComaTx2PwrLowWng.setStatus("current")
_PmopsAlmComaTx2PwrHighWng_Type = EkiOnOff
_PmopsAlmComaTx2PwrHighWng_Object = MibScalar
pmopsAlmComaTx2PwrHighWng = _PmopsAlmComaTx2PwrHighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 2, 1, 18, 6),
    _PmopsAlmComaTx2PwrHighWng_Type()
)
pmopsAlmComaTx2PwrHighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmComaTx2PwrHighWng.setStatus("current")
_PmopsAlmComaRx2PwrLowWng_Type = EkiOnOff
_PmopsAlmComaRx2PwrLowWng_Object = MibScalar
pmopsAlmComaRx2PwrLowWng = _PmopsAlmComaRx2PwrLowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 2, 1, 18, 7),
    _PmopsAlmComaRx2PwrLowWng_Type()
)
pmopsAlmComaRx2PwrLowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmComaRx2PwrLowWng.setStatus("current")
_PmopsAlmComaRx2PwrHighWng_Type = EkiOnOff
_PmopsAlmComaRx2PwrHighWng_Object = MibScalar
pmopsAlmComaRx2PwrHighWng = _PmopsAlmComaRx2PwrHighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 2, 1, 18, 8),
    _PmopsAlmComaRx2PwrHighWng_Type()
)
pmopsAlmComaRx2PwrHighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmComaRx2PwrHighWng.setStatus("current")
_PmopsAlmComaUrg_ObjectIdentity = ObjectIdentity
pmopsAlmComaUrg = _PmopsAlmComaUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 2, 2)
)
_PmopsAlmcomaAccessioAlm_ObjectIdentity = ObjectIdentity
pmopsAlmcomaAccessioAlm = _PmopsAlmcomaAccessioAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 2, 2, 16)
)
_PmopsAlmComaLosRx1_Type = EkiOnOff
_PmopsAlmComaLosRx1_Object = MibScalar
pmopsAlmComaLosRx1 = _PmopsAlmComaLosRx1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 2, 2, 16, 1),
    _PmopsAlmComaLosRx1_Type()
)
pmopsAlmComaLosRx1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmComaLosRx1.setStatus("current")
_PmopsAlmComaLosRx2_Type = EkiOnOff
_PmopsAlmComaLosRx2_Object = MibScalar
pmopsAlmComaLosRx2 = _PmopsAlmComaLosRx2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 2, 2, 16, 2),
    _PmopsAlmComaLosRx2_Type()
)
pmopsAlmComaLosRx2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmComaLosRx2.setStatus("current")
_PmopsAlmComaLosTx1_Type = EkiOnOff
_PmopsAlmComaLosTx1_Object = MibScalar
pmopsAlmComaLosTx1 = _PmopsAlmComaLosTx1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 2, 2, 16, 3),
    _PmopsAlmComaLosTx1_Type()
)
pmopsAlmComaLosTx1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmComaLosTx1.setStatus("current")
_PmopsAlmComaLosTx2_Type = EkiOnOff
_PmopsAlmComaLosTx2_Object = MibScalar
pmopsAlmComaLosTx2 = _PmopsAlmComaLosTx2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 2, 2, 16, 4),
    _PmopsAlmComaLosTx2_Type()
)
pmopsAlmComaLosTx2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmComaLosTx2.setStatus("current")
_PmopsAlmComaSwitchPosition1_Type = EkiOnOff
_PmopsAlmComaSwitchPosition1_Object = MibScalar
pmopsAlmComaSwitchPosition1 = _PmopsAlmComaSwitchPosition1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 2, 2, 16, 5),
    _PmopsAlmComaSwitchPosition1_Type()
)
pmopsAlmComaSwitchPosition1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmComaSwitchPosition1.setStatus("current")
_PmopsAlmComaSwitchPosition2_Type = EkiOnOff
_PmopsAlmComaSwitchPosition2_Object = MibScalar
pmopsAlmComaSwitchPosition2 = _PmopsAlmComaSwitchPosition2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 2, 2, 16, 6),
    _PmopsAlmComaSwitchPosition2_Type()
)
pmopsAlmComaSwitchPosition2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmComaSwitchPosition2.setStatus("current")
_PmopsAlmComaSwitchFail_Type = EkiOnOff
_PmopsAlmComaSwitchFail_Object = MibScalar
pmopsAlmComaSwitchFail = _PmopsAlmComaSwitchFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 2, 2, 16, 8),
    _PmopsAlmComaSwitchFail_Type()
)
pmopsAlmComaSwitchFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmComaSwitchFail.setStatus("current")
_PmopsAlmcomaMeasAlm_ObjectIdentity = ObjectIdentity
pmopsAlmcomaMeasAlm = _PmopsAlmcomaMeasAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 2, 2, 17)
)
_PmopsAlmComaTx1PwrLowAla_Type = EkiOnOff
_PmopsAlmComaTx1PwrLowAla_Object = MibScalar
pmopsAlmComaTx1PwrLowAla = _PmopsAlmComaTx1PwrLowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 2, 2, 17, 1),
    _PmopsAlmComaTx1PwrLowAla_Type()
)
pmopsAlmComaTx1PwrLowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmComaTx1PwrLowAla.setStatus("current")
_PmopsAlmComaTx1PwrHighAla_Type = EkiOnOff
_PmopsAlmComaTx1PwrHighAla_Object = MibScalar
pmopsAlmComaTx1PwrHighAla = _PmopsAlmComaTx1PwrHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 2, 2, 17, 2),
    _PmopsAlmComaTx1PwrHighAla_Type()
)
pmopsAlmComaTx1PwrHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmComaTx1PwrHighAla.setStatus("current")
_PmopsAlmComaRx1PwrLowAla_Type = EkiOnOff
_PmopsAlmComaRx1PwrLowAla_Object = MibScalar
pmopsAlmComaRx1PwrLowAla = _PmopsAlmComaRx1PwrLowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 2, 2, 17, 3),
    _PmopsAlmComaRx1PwrLowAla_Type()
)
pmopsAlmComaRx1PwrLowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmComaRx1PwrLowAla.setStatus("current")
_PmopsAlmComaRx1PwrHighAla_Type = EkiOnOff
_PmopsAlmComaRx1PwrHighAla_Object = MibScalar
pmopsAlmComaRx1PwrHighAla = _PmopsAlmComaRx1PwrHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 2, 2, 17, 4),
    _PmopsAlmComaRx1PwrHighAla_Type()
)
pmopsAlmComaRx1PwrHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmComaRx1PwrHighAla.setStatus("current")
_PmopsAlmComaTx2PwrLowAla_Type = EkiOnOff
_PmopsAlmComaTx2PwrLowAla_Object = MibScalar
pmopsAlmComaTx2PwrLowAla = _PmopsAlmComaTx2PwrLowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 2, 2, 17, 5),
    _PmopsAlmComaTx2PwrLowAla_Type()
)
pmopsAlmComaTx2PwrLowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmComaTx2PwrLowAla.setStatus("current")
_PmopsAlmComaTx2PwrHighAla_Type = EkiOnOff
_PmopsAlmComaTx2PwrHighAla_Object = MibScalar
pmopsAlmComaTx2PwrHighAla = _PmopsAlmComaTx2PwrHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 2, 2, 17, 6),
    _PmopsAlmComaTx2PwrHighAla_Type()
)
pmopsAlmComaTx2PwrHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmComaTx2PwrHighAla.setStatus("current")
_PmopsAlmComaRx2PwrLowAla_Type = EkiOnOff
_PmopsAlmComaRx2PwrLowAla_Object = MibScalar
pmopsAlmComaRx2PwrLowAla = _PmopsAlmComaRx2PwrLowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 2, 2, 17, 7),
    _PmopsAlmComaRx2PwrLowAla_Type()
)
pmopsAlmComaRx2PwrLowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmComaRx2PwrLowAla.setStatus("current")
_PmopsAlmComaRx2PwrHighAla_Type = EkiOnOff
_PmopsAlmComaRx2PwrHighAla_Object = MibScalar
pmopsAlmComaRx2PwrHighAla = _PmopsAlmComaRx2PwrHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 2, 2, 17, 8),
    _PmopsAlmComaRx2PwrHighAla_Type()
)
pmopsAlmComaRx2PwrHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmComaRx2PwrHighAla.setStatus("current")
_PmopsAlmComaCrit_ObjectIdentity = ObjectIdentity
pmopsAlmComaCrit = _PmopsAlmComaCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 2, 3)
)
_PmopsAlmsynthAlmComa_ObjectIdentity = ObjectIdentity
pmopsAlmsynthAlmComa = _PmopsAlmsynthAlmComa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 2, 3, 8)
)
_PmopsAlmComaHwFailAcc_Type = EkiOnOff
_PmopsAlmComaHwFailAcc_Object = MibScalar
pmopsAlmComaHwFailAcc = _PmopsAlmComaHwFailAcc_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 2, 3, 8, 4),
    _PmopsAlmComaHwFailAcc_Type()
)
pmopsAlmComaHwFailAcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmComaHwFailAcc.setStatus("current")
_PmopsAlmComaLocalOos_Type = EkiOnOff
_PmopsAlmComaLocalOos_Object = MibScalar
pmopsAlmComaLocalOos = _PmopsAlmComaLocalOos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 2, 3, 8, 6),
    _PmopsAlmComaLocalOos_Type()
)
pmopsAlmComaLocalOos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmComaLocalOos.setStatus("current")
_PmopsAlmComaMeasWng_Type = EkiOnOff
_PmopsAlmComaMeasWng_Object = MibScalar
pmopsAlmComaMeasWng = _PmopsAlmComaMeasWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 2, 3, 8, 9),
    _PmopsAlmComaMeasWng_Type()
)
pmopsAlmComaMeasWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmComaMeasWng.setStatus("current")
_PmopsAlmComaMeasAlm_Type = EkiOnOff
_PmopsAlmComaMeasAlm_Object = MibScalar
pmopsAlmComaMeasAlm = _PmopsAlmComaMeasAlm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 2, 3, 8, 10),
    _PmopsAlmComaMeasAlm_Type()
)
pmopsAlmComaMeasAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmComaMeasAlm.setStatus("current")
_PmopsAlmComaFailAcc_Type = EkiOnOff
_PmopsAlmComaFailAcc_Object = MibScalar
pmopsAlmComaFailAcc = _PmopsAlmComaFailAcc_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 2, 3, 8, 12),
    _PmopsAlmComaFailAcc_Type()
)
pmopsAlmComaFailAcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmComaFailAcc.setStatus("current")
_PmopsAlmComb_ObjectIdentity = ObjectIdentity
pmopsAlmComb = _PmopsAlmComb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 3)
)
_PmopsAlmCombNurg_ObjectIdentity = ObjectIdentity
pmopsAlmCombNurg = _PmopsAlmCombNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 3, 1)
)
_PmopsAlmcombMeasWng_ObjectIdentity = ObjectIdentity
pmopsAlmcombMeasWng = _PmopsAlmcombMeasWng_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 3, 1, 26)
)
_PmopsAlmCombTx1PwrLowWng_Type = EkiOnOff
_PmopsAlmCombTx1PwrLowWng_Object = MibScalar
pmopsAlmCombTx1PwrLowWng = _PmopsAlmCombTx1PwrLowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 3, 1, 26, 1),
    _PmopsAlmCombTx1PwrLowWng_Type()
)
pmopsAlmCombTx1PwrLowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmCombTx1PwrLowWng.setStatus("current")
_PmopsAlmCombTx1PwrHighWng_Type = EkiOnOff
_PmopsAlmCombTx1PwrHighWng_Object = MibScalar
pmopsAlmCombTx1PwrHighWng = _PmopsAlmCombTx1PwrHighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 3, 1, 26, 2),
    _PmopsAlmCombTx1PwrHighWng_Type()
)
pmopsAlmCombTx1PwrHighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmCombTx1PwrHighWng.setStatus("current")
_PmopsAlmCombRx1PwrLowWng_Type = EkiOnOff
_PmopsAlmCombRx1PwrLowWng_Object = MibScalar
pmopsAlmCombRx1PwrLowWng = _PmopsAlmCombRx1PwrLowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 3, 1, 26, 3),
    _PmopsAlmCombRx1PwrLowWng_Type()
)
pmopsAlmCombRx1PwrLowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmCombRx1PwrLowWng.setStatus("current")
_PmopsAlmCombRx1PwrHighWng_Type = EkiOnOff
_PmopsAlmCombRx1PwrHighWng_Object = MibScalar
pmopsAlmCombRx1PwrHighWng = _PmopsAlmCombRx1PwrHighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 3, 1, 26, 4),
    _PmopsAlmCombRx1PwrHighWng_Type()
)
pmopsAlmCombRx1PwrHighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmCombRx1PwrHighWng.setStatus("current")
_PmopsAlmCombTx2PwrLowWng_Type = EkiOnOff
_PmopsAlmCombTx2PwrLowWng_Object = MibScalar
pmopsAlmCombTx2PwrLowWng = _PmopsAlmCombTx2PwrLowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 3, 1, 26, 5),
    _PmopsAlmCombTx2PwrLowWng_Type()
)
pmopsAlmCombTx2PwrLowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmCombTx2PwrLowWng.setStatus("current")
_PmopsAlmCombTx2PwrHighWng_Type = EkiOnOff
_PmopsAlmCombTx2PwrHighWng_Object = MibScalar
pmopsAlmCombTx2PwrHighWng = _PmopsAlmCombTx2PwrHighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 3, 1, 26, 6),
    _PmopsAlmCombTx2PwrHighWng_Type()
)
pmopsAlmCombTx2PwrHighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmCombTx2PwrHighWng.setStatus("current")
_PmopsAlmCombRx2PwrLowWng_Type = EkiOnOff
_PmopsAlmCombRx2PwrLowWng_Object = MibScalar
pmopsAlmCombRx2PwrLowWng = _PmopsAlmCombRx2PwrLowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 3, 1, 26, 7),
    _PmopsAlmCombRx2PwrLowWng_Type()
)
pmopsAlmCombRx2PwrLowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmCombRx2PwrLowWng.setStatus("current")
_PmopsAlmCombRx2PwrHighWng_Type = EkiOnOff
_PmopsAlmCombRx2PwrHighWng_Object = MibScalar
pmopsAlmCombRx2PwrHighWng = _PmopsAlmCombRx2PwrHighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 3, 1, 26, 8),
    _PmopsAlmCombRx2PwrHighWng_Type()
)
pmopsAlmCombRx2PwrHighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmCombRx2PwrHighWng.setStatus("current")
_PmopsAlmCombUrg_ObjectIdentity = ObjectIdentity
pmopsAlmCombUrg = _PmopsAlmCombUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 3, 2)
)
_PmopsAlmcombAccessioAlm_ObjectIdentity = ObjectIdentity
pmopsAlmcombAccessioAlm = _PmopsAlmcombAccessioAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 3, 2, 24)
)
_PmopsAlmCombLosRx1_Type = EkiOnOff
_PmopsAlmCombLosRx1_Object = MibScalar
pmopsAlmCombLosRx1 = _PmopsAlmCombLosRx1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 3, 2, 24, 1),
    _PmopsAlmCombLosRx1_Type()
)
pmopsAlmCombLosRx1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmCombLosRx1.setStatus("current")
_PmopsAlmCombLosRx2_Type = EkiOnOff
_PmopsAlmCombLosRx2_Object = MibScalar
pmopsAlmCombLosRx2 = _PmopsAlmCombLosRx2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 3, 2, 24, 2),
    _PmopsAlmCombLosRx2_Type()
)
pmopsAlmCombLosRx2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmCombLosRx2.setStatus("current")
_PmopsAlmCombLosTx1_Type = EkiOnOff
_PmopsAlmCombLosTx1_Object = MibScalar
pmopsAlmCombLosTx1 = _PmopsAlmCombLosTx1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 3, 2, 24, 3),
    _PmopsAlmCombLosTx1_Type()
)
pmopsAlmCombLosTx1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmCombLosTx1.setStatus("current")
_PmopsAlmCombLosTx2_Type = EkiOnOff
_PmopsAlmCombLosTx2_Object = MibScalar
pmopsAlmCombLosTx2 = _PmopsAlmCombLosTx2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 3, 2, 24, 4),
    _PmopsAlmCombLosTx2_Type()
)
pmopsAlmCombLosTx2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmCombLosTx2.setStatus("current")
_PmopsAlmCombSwitchPosition1_Type = EkiOnOff
_PmopsAlmCombSwitchPosition1_Object = MibScalar
pmopsAlmCombSwitchPosition1 = _PmopsAlmCombSwitchPosition1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 3, 2, 24, 5),
    _PmopsAlmCombSwitchPosition1_Type()
)
pmopsAlmCombSwitchPosition1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmCombSwitchPosition1.setStatus("current")
_PmopsAlmCombSwitchPosition2_Type = EkiOnOff
_PmopsAlmCombSwitchPosition2_Object = MibScalar
pmopsAlmCombSwitchPosition2 = _PmopsAlmCombSwitchPosition2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 3, 2, 24, 6),
    _PmopsAlmCombSwitchPosition2_Type()
)
pmopsAlmCombSwitchPosition2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmCombSwitchPosition2.setStatus("current")
_PmopsAlmCombSwitchFail_Type = EkiOnOff
_PmopsAlmCombSwitchFail_Object = MibScalar
pmopsAlmCombSwitchFail = _PmopsAlmCombSwitchFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 3, 2, 24, 8),
    _PmopsAlmCombSwitchFail_Type()
)
pmopsAlmCombSwitchFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmCombSwitchFail.setStatus("current")
_PmopsAlmcombMeasAla_ObjectIdentity = ObjectIdentity
pmopsAlmcombMeasAla = _PmopsAlmcombMeasAla_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 3, 2, 25)
)
_PmopsAlmCombTx1PwrLowAla_Type = EkiOnOff
_PmopsAlmCombTx1PwrLowAla_Object = MibScalar
pmopsAlmCombTx1PwrLowAla = _PmopsAlmCombTx1PwrLowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 3, 2, 25, 1),
    _PmopsAlmCombTx1PwrLowAla_Type()
)
pmopsAlmCombTx1PwrLowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmCombTx1PwrLowAla.setStatus("current")
_PmopsAlmCombTx1PwrHighAla_Type = EkiOnOff
_PmopsAlmCombTx1PwrHighAla_Object = MibScalar
pmopsAlmCombTx1PwrHighAla = _PmopsAlmCombTx1PwrHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 3, 2, 25, 2),
    _PmopsAlmCombTx1PwrHighAla_Type()
)
pmopsAlmCombTx1PwrHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmCombTx1PwrHighAla.setStatus("current")
_PmopsAlmCombRx1PwrLowAla_Type = EkiOnOff
_PmopsAlmCombRx1PwrLowAla_Object = MibScalar
pmopsAlmCombRx1PwrLowAla = _PmopsAlmCombRx1PwrLowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 3, 2, 25, 3),
    _PmopsAlmCombRx1PwrLowAla_Type()
)
pmopsAlmCombRx1PwrLowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmCombRx1PwrLowAla.setStatus("current")
_PmopsAlmCombRx1PwrHighAla_Type = EkiOnOff
_PmopsAlmCombRx1PwrHighAla_Object = MibScalar
pmopsAlmCombRx1PwrHighAla = _PmopsAlmCombRx1PwrHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 3, 2, 25, 4),
    _PmopsAlmCombRx1PwrHighAla_Type()
)
pmopsAlmCombRx1PwrHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmCombRx1PwrHighAla.setStatus("current")
_PmopsAlmCombTx2PwrLowAla_Type = EkiOnOff
_PmopsAlmCombTx2PwrLowAla_Object = MibScalar
pmopsAlmCombTx2PwrLowAla = _PmopsAlmCombTx2PwrLowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 3, 2, 25, 5),
    _PmopsAlmCombTx2PwrLowAla_Type()
)
pmopsAlmCombTx2PwrLowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmCombTx2PwrLowAla.setStatus("current")
_PmopsAlmCombTx2PwrHighAla_Type = EkiOnOff
_PmopsAlmCombTx2PwrHighAla_Object = MibScalar
pmopsAlmCombTx2PwrHighAla = _PmopsAlmCombTx2PwrHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 3, 2, 25, 6),
    _PmopsAlmCombTx2PwrHighAla_Type()
)
pmopsAlmCombTx2PwrHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmCombTx2PwrHighAla.setStatus("current")
_PmopsAlmCombRx2PwrLowAla_Type = EkiOnOff
_PmopsAlmCombRx2PwrLowAla_Object = MibScalar
pmopsAlmCombRx2PwrLowAla = _PmopsAlmCombRx2PwrLowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 3, 2, 25, 7),
    _PmopsAlmCombRx2PwrLowAla_Type()
)
pmopsAlmCombRx2PwrLowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmCombRx2PwrLowAla.setStatus("current")
_PmopsAlmCombRx2PwrHighAla_Type = EkiOnOff
_PmopsAlmCombRx2PwrHighAla_Object = MibScalar
pmopsAlmCombRx2PwrHighAla = _PmopsAlmCombRx2PwrHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 3, 2, 25, 8),
    _PmopsAlmCombRx2PwrHighAla_Type()
)
pmopsAlmCombRx2PwrHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmCombRx2PwrHighAla.setStatus("current")
_PmopsAlmCombCrit_ObjectIdentity = ObjectIdentity
pmopsAlmCombCrit = _PmopsAlmCombCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 3, 3)
)
_PmopsAlmsynthAlmComb_ObjectIdentity = ObjectIdentity
pmopsAlmsynthAlmComb = _PmopsAlmsynthAlmComb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 3, 3, 9)
)
_PmopsAlmCombHwFailAcc_Type = EkiOnOff
_PmopsAlmCombHwFailAcc_Object = MibScalar
pmopsAlmCombHwFailAcc = _PmopsAlmCombHwFailAcc_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 3, 3, 9, 4),
    _PmopsAlmCombHwFailAcc_Type()
)
pmopsAlmCombHwFailAcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmCombHwFailAcc.setStatus("current")
_PmopsAlmCombLocalOos_Type = EkiOnOff
_PmopsAlmCombLocalOos_Object = MibScalar
pmopsAlmCombLocalOos = _PmopsAlmCombLocalOos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 3, 3, 9, 6),
    _PmopsAlmCombLocalOos_Type()
)
pmopsAlmCombLocalOos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmCombLocalOos.setStatus("current")
_PmopsAlmCombMeasWng_Type = EkiOnOff
_PmopsAlmCombMeasWng_Object = MibScalar
pmopsAlmCombMeasWng = _PmopsAlmCombMeasWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 3, 3, 9, 9),
    _PmopsAlmCombMeasWng_Type()
)
pmopsAlmCombMeasWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmCombMeasWng.setStatus("current")
_PmopsAlmCombMeasAlm_Type = EkiOnOff
_PmopsAlmCombMeasAlm_Object = MibScalar
pmopsAlmCombMeasAlm = _PmopsAlmCombMeasAlm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 3, 3, 9, 10),
    _PmopsAlmCombMeasAlm_Type()
)
pmopsAlmCombMeasAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmCombMeasAlm.setStatus("current")
_PmopsAlmCombFailAcc_Type = EkiOnOff
_PmopsAlmCombFailAcc_Object = MibScalar
pmopsAlmCombFailAcc = _PmopsAlmCombFailAcc_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 2, 3, 3, 9, 12),
    _PmopsAlmCombFailAcc_Type()
)
pmopsAlmCombFailAcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsAlmCombFailAcc.setStatus("current")
_Pmopsmeasures_ObjectIdentity = ObjectIdentity
pmopsmeasures = _Pmopsmeasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 3)
)
_PmopsMesrOther_ObjectIdentity = ObjectIdentity
pmopsMesrOther = _PmopsMesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 3, 1)
)
_PmopsMesrComa_ObjectIdentity = ObjectIdentity
pmopsMesrComa = _PmopsMesrComa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 3, 2)
)


class _PmopsMesrcomaTxPower1_Type(Unsigned32):
    """Custom type pmopsMesrcomaTxPower1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmopsMesrcomaTxPower1_Type.__name__ = "Unsigned32"
_PmopsMesrcomaTxPower1_Object = MibScalar
pmopsMesrcomaTxPower1 = _PmopsMesrcomaTxPower1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 3, 2, 16),
    _PmopsMesrcomaTxPower1_Type()
)
pmopsMesrcomaTxPower1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsMesrcomaTxPower1.setStatus("current")


class _PmopsMesrcomaTxPower2_Type(Unsigned32):
    """Custom type pmopsMesrcomaTxPower2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmopsMesrcomaTxPower2_Type.__name__ = "Unsigned32"
_PmopsMesrcomaTxPower2_Object = MibScalar
pmopsMesrcomaTxPower2 = _PmopsMesrcomaTxPower2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 3, 2, 17),
    _PmopsMesrcomaTxPower2_Type()
)
pmopsMesrcomaTxPower2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsMesrcomaTxPower2.setStatus("current")


class _PmopsMesrcomaRxPower1_Type(Unsigned32):
    """Custom type pmopsMesrcomaRxPower1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmopsMesrcomaRxPower1_Type.__name__ = "Unsigned32"
_PmopsMesrcomaRxPower1_Object = MibScalar
pmopsMesrcomaRxPower1 = _PmopsMesrcomaRxPower1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 3, 2, 18),
    _PmopsMesrcomaRxPower1_Type()
)
pmopsMesrcomaRxPower1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsMesrcomaRxPower1.setStatus("current")


class _PmopsMesrcomaRxPower2_Type(Unsigned32):
    """Custom type pmopsMesrcomaRxPower2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmopsMesrcomaRxPower2_Type.__name__ = "Unsigned32"
_PmopsMesrcomaRxPower2_Object = MibScalar
pmopsMesrcomaRxPower2 = _PmopsMesrcomaRxPower2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 3, 2, 19),
    _PmopsMesrcomaRxPower2_Type()
)
pmopsMesrcomaRxPower2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsMesrcomaRxPower2.setStatus("current")
_PmopsMesrComb_ObjectIdentity = ObjectIdentity
pmopsMesrComb = _PmopsMesrComb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 3, 3)
)


class _PmopsMesrcombTxPower1_Type(Unsigned32):
    """Custom type pmopsMesrcombTxPower1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmopsMesrcombTxPower1_Type.__name__ = "Unsigned32"
_PmopsMesrcombTxPower1_Object = MibScalar
pmopsMesrcombTxPower1 = _PmopsMesrcombTxPower1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 3, 3, 24),
    _PmopsMesrcombTxPower1_Type()
)
pmopsMesrcombTxPower1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsMesrcombTxPower1.setStatus("current")


class _PmopsMesrcombTxPower2_Type(Unsigned32):
    """Custom type pmopsMesrcombTxPower2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmopsMesrcombTxPower2_Type.__name__ = "Unsigned32"
_PmopsMesrcombTxPower2_Object = MibScalar
pmopsMesrcombTxPower2 = _PmopsMesrcombTxPower2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 3, 3, 25),
    _PmopsMesrcombTxPower2_Type()
)
pmopsMesrcombTxPower2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsMesrcombTxPower2.setStatus("current")


class _PmopsMesrcombRxPower1_Type(Unsigned32):
    """Custom type pmopsMesrcombRxPower1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmopsMesrcombRxPower1_Type.__name__ = "Unsigned32"
_PmopsMesrcombRxPower1_Object = MibScalar
pmopsMesrcombRxPower1 = _PmopsMesrcombRxPower1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 3, 3, 26),
    _PmopsMesrcombRxPower1_Type()
)
pmopsMesrcombRxPower1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsMesrcombRxPower1.setStatus("current")


class _PmopsMesrcombRxPower2_Type(Unsigned32):
    """Custom type pmopsMesrcombRxPower2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmopsMesrcombRxPower2_Type.__name__ = "Unsigned32"
_PmopsMesrcombRxPower2_Object = MibScalar
pmopsMesrcombRxPower2 = _PmopsMesrcombRxPower2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 3, 3, 27),
    _PmopsMesrcombRxPower2_Type()
)
pmopsMesrcombRxPower2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsMesrcombRxPower2.setStatus("current")
_PmopscontrolsWrite_ObjectIdentity = ObjectIdentity
pmopscontrolsWrite = _PmopscontrolsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 6)
)
_PmopsCtrlOther_ObjectIdentity = ObjectIdentity
pmopsCtrlOther = _PmopsCtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 6, 1)
)
_PmopsCtrlsynth0_ObjectIdentity = ObjectIdentity
pmopsCtrlsynth0 = _PmopsCtrlsynth0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 6, 1, 0)
)
_PmopsCtrlConfLoad_Type = EkiOnOff
_PmopsCtrlConfLoad_Object = MibScalar
pmopsCtrlConfLoad = _PmopsCtrlConfLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 6, 1, 0, 1),
    _PmopsCtrlConfLoad_Type()
)
pmopsCtrlConfLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopsCtrlConfLoad.setStatus("current")
_PmopsCtrlConfFlash_Type = EkiOnOff
_PmopsCtrlConfFlash_Object = MibScalar
pmopsCtrlConfFlash = _PmopsCtrlConfFlash_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 6, 1, 0, 9),
    _PmopsCtrlConfFlash_Type()
)
pmopsCtrlConfFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopsCtrlConfFlash.setStatus("current")
_PmopsCtrlConfClear_Type = EkiOnOff
_PmopsCtrlConfClear_Object = MibScalar
pmopsCtrlConfClear = _PmopsCtrlConfClear_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 6, 1, 0, 13),
    _PmopsCtrlConfClear_Type()
)
pmopsCtrlConfClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopsCtrlConfClear.setStatus("current")
_PmopsCtrlsynth4_ObjectIdentity = ObjectIdentity
pmopsCtrlsynth4 = _PmopsCtrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 6, 1, 4)
)
_PmopsCtrlCorrelatOn_Type = EkiOnOff
_PmopsCtrlCorrelatOn_Object = MibScalar
pmopsCtrlCorrelatOn = _PmopsCtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 6, 1, 4, 1),
    _PmopsCtrlCorrelatOn_Type()
)
pmopsCtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopsCtrlCorrelatOn.setStatus("current")
_PmopsCtrlCorrelatOff_Type = EkiOnOff
_PmopsCtrlCorrelatOff_Object = MibScalar
pmopsCtrlCorrelatOff = _PmopsCtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 6, 1, 4, 2),
    _PmopsCtrlCorrelatOff_Type()
)
pmopsCtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopsCtrlCorrelatOff.setStatus("current")
_PmopsCtrlswMgnt_ObjectIdentity = ObjectIdentity
pmopsCtrlswMgnt = _PmopsCtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 6, 1, 5)
)
_PmopsCtrlColdReset_Type = EkiOnOff
_PmopsCtrlColdReset_Object = MibScalar
pmopsCtrlColdReset = _PmopsCtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 6, 1, 5, 2),
    _PmopsCtrlColdReset_Type()
)
pmopsCtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopsCtrlColdReset.setStatus("current")
_PmopsCtrlWarmReset_Type = EkiOnOff
_PmopsCtrlWarmReset_Object = MibScalar
pmopsCtrlWarmReset = _PmopsCtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 6, 1, 5, 3),
    _PmopsCtrlWarmReset_Type()
)
pmopsCtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopsCtrlWarmReset.setStatus("current")
_PmopsCtrlledTest_ObjectIdentity = ObjectIdentity
pmopsCtrlledTest = _PmopsCtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 6, 1, 64)
)
_PmopsCtrlGreenLed_Type = EkiOnOff
_PmopsCtrlGreenLed_Object = MibScalar
pmopsCtrlGreenLed = _PmopsCtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 6, 1, 64, 1),
    _PmopsCtrlGreenLed_Type()
)
pmopsCtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopsCtrlGreenLed.setStatus("current")
_PmopsCtrlRedLed_Type = EkiOnOff
_PmopsCtrlRedLed_Object = MibScalar
pmopsCtrlRedLed = _PmopsCtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 6, 1, 64, 2),
    _PmopsCtrlRedLed_Type()
)
pmopsCtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopsCtrlRedLed.setStatus("current")
_PmopsCtrlLedOff_Type = EkiOnOff
_PmopsCtrlLedOff_Object = MibScalar
pmopsCtrlLedOff = _PmopsCtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 6, 1, 64, 3),
    _PmopsCtrlLedOff_Type()
)
pmopsCtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopsCtrlLedOff.setStatus("current")
_PmopsCtrlComa_ObjectIdentity = ObjectIdentity
pmopsCtrlComa = _PmopsCtrlComa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 6, 2)
)
_PmopsCtrlcomaSwitchMode_Type = PmopsSwitchMode
_PmopsCtrlcomaSwitchMode_Object = MibScalar
pmopsCtrlcomaSwitchMode = _PmopsCtrlcomaSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 6, 2, 16),
    _PmopsCtrlcomaSwitchMode_Type()
)
pmopsCtrlcomaSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopsCtrlcomaSwitchMode.setStatus("current")
_PmopsCtrlcomaOosMode_ObjectIdentity = ObjectIdentity
pmopsCtrlcomaOosMode = _PmopsCtrlcomaOosMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 6, 2, 18)
)
_PmopsCtrlComaOosMode_Type = EkiOnOff
_PmopsCtrlComaOosMode_Object = MibScalar
pmopsCtrlComaOosMode = _PmopsCtrlComaOosMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 6, 2, 18, 1),
    _PmopsCtrlComaOosMode_Type()
)
pmopsCtrlComaOosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopsCtrlComaOosMode.setStatus("current")


class _PmopsCtrlcomaRxPwrSetting1_Type(Unsigned32):
    """Custom type pmopsCtrlcomaRxPwrSetting1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmopsCtrlcomaRxPwrSetting1_Type.__name__ = "Unsigned32"
_PmopsCtrlcomaRxPwrSetting1_Object = MibScalar
pmopsCtrlcomaRxPwrSetting1 = _PmopsCtrlcomaRxPwrSetting1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 6, 2, 24),
    _PmopsCtrlcomaRxPwrSetting1_Type()
)
pmopsCtrlcomaRxPwrSetting1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopsCtrlcomaRxPwrSetting1.setStatus("current")


class _PmopsCtrlcomaRxPwrSetting2_Type(Unsigned32):
    """Custom type pmopsCtrlcomaRxPwrSetting2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmopsCtrlcomaRxPwrSetting2_Type.__name__ = "Unsigned32"
_PmopsCtrlcomaRxPwrSetting2_Object = MibScalar
pmopsCtrlcomaRxPwrSetting2 = _PmopsCtrlcomaRxPwrSetting2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 6, 2, 25),
    _PmopsCtrlcomaRxPwrSetting2_Type()
)
pmopsCtrlcomaRxPwrSetting2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopsCtrlcomaRxPwrSetting2.setStatus("current")
_PmopsCtrlComb_ObjectIdentity = ObjectIdentity
pmopsCtrlComb = _PmopsCtrlComb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 6, 3)
)
_PmopsCtrlcombSwitchMode_Type = PmopsSwitchMode
_PmopsCtrlcombSwitchMode_Object = MibScalar
pmopsCtrlcombSwitchMode = _PmopsCtrlcombSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 6, 3, 17),
    _PmopsCtrlcombSwitchMode_Type()
)
pmopsCtrlcombSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopsCtrlcombSwitchMode.setStatus("current")
_PmopsCtrlcombOosMode_ObjectIdentity = ObjectIdentity
pmopsCtrlcombOosMode = _PmopsCtrlcombOosMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 6, 3, 19)
)
_PmopsCtrlCombOosMode_Type = EkiOnOff
_PmopsCtrlCombOosMode_Object = MibScalar
pmopsCtrlCombOosMode = _PmopsCtrlCombOosMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 6, 3, 19, 1),
    _PmopsCtrlCombOosMode_Type()
)
pmopsCtrlCombOosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopsCtrlCombOosMode.setStatus("current")


class _PmopsCtrlcombRxPwrSetting1_Type(Unsigned32):
    """Custom type pmopsCtrlcombRxPwrSetting1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmopsCtrlcombRxPwrSetting1_Type.__name__ = "Unsigned32"
_PmopsCtrlcombRxPwrSetting1_Object = MibScalar
pmopsCtrlcombRxPwrSetting1 = _PmopsCtrlcombRxPwrSetting1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 6, 3, 26),
    _PmopsCtrlcombRxPwrSetting1_Type()
)
pmopsCtrlcombRxPwrSetting1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopsCtrlcombRxPwrSetting1.setStatus("current")


class _PmopsCtrlcombRxPwrSetting2_Type(Unsigned32):
    """Custom type pmopsCtrlcombRxPwrSetting2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmopsCtrlcombRxPwrSetting2_Type.__name__ = "Unsigned32"
_PmopsCtrlcombRxPwrSetting2_Object = MibScalar
pmopsCtrlcombRxPwrSetting2 = _PmopsCtrlcombRxPwrSetting2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 6, 3, 27),
    _PmopsCtrlcombRxPwrSetting2_Type()
)
pmopsCtrlcombRxPwrSetting2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopsCtrlcombRxPwrSetting2.setStatus("current")
_Pmopsri_ObjectIdentity = ObjectIdentity
pmopsri = _Pmopsri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 7)
)
_PmopsriTable_ObjectIdentity = ObjectIdentity
pmopsriTable = _PmopsriTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 7, 1)
)
_PmopsRinvReloadInventory_Type = EkiOnOff
_PmopsRinvReloadInventory_Object = MibScalar
pmopsRinvReloadInventory = _PmopsRinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 7, 2),
    _PmopsRinvReloadInventory_Type()
)
pmopsRinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopsRinvReloadInventory.setStatus("current")
_PmopsRinvHwPlatform_Type = DisplayString
_PmopsRinvHwPlatform_Object = MibScalar
pmopsRinvHwPlatform = _PmopsRinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 7, 3),
    _PmopsRinvHwPlatform_Type()
)
pmopsRinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsRinvHwPlatform.setStatus("current")
_PmopsRinvModulePlatform_Type = DisplayString
_PmopsRinvModulePlatform_Object = MibScalar
pmopsRinvModulePlatform = _PmopsRinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 7, 4),
    _PmopsRinvModulePlatform_Type()
)
pmopsRinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsRinvModulePlatform.setStatus("current")
_PmopsRinvSwPlatform_Type = DisplayString
_PmopsRinvSwPlatform_Object = MibScalar
pmopsRinvSwPlatform = _PmopsRinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 7, 5),
    _PmopsRinvSwPlatform_Type()
)
pmopsRinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsRinvSwPlatform.setStatus("current")
_PmopsRinvLine1SFP_Type = DisplayString
_PmopsRinvLine1SFP_Object = MibScalar
pmopsRinvLine1SFP = _PmopsRinvLine1SFP_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 7, 6),
    _PmopsRinvLine1SFP_Type()
)
pmopsRinvLine1SFP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsRinvLine1SFP.setStatus("current")
_PmopsRinvLine2SFP_Type = DisplayString
_PmopsRinvLine2SFP_Object = MibScalar
pmopsRinvLine2SFP = _PmopsRinvLine2SFP_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 7, 7),
    _PmopsRinvLine2SFP_Type()
)
pmopsRinvLine2SFP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsRinvLine2SFP.setStatus("current")
_PmopsConfig_ObjectIdentity = ObjectIdentity
pmopsConfig = _PmopsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 9)
)
_PmopsCfgLsd_ObjectIdentity = ObjectIdentity
pmopsCfgLsd = _PmopsCfgLsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 9, 1)
)
_PmopstablecomaLsd_ObjectIdentity = ObjectIdentity
pmopstablecomaLsd = _PmopstablecomaLsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 9, 1, 1)
)
_PmopsCfgStartUp_ObjectIdentity = ObjectIdentity
pmopsCfgStartUp = _PmopsCfgStartUp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 9, 2)
)
_PmopstablecomaStartup_ObjectIdentity = ObjectIdentity
pmopstablecomaStartup = _PmopstablecomaStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 9, 2, 1)
)


class _PmopsCfgcomaSwitchMode_Type(Unsigned32):
    """Custom type pmopsCfgcomaSwitchMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmopsCfgcomaSwitchMode_Type.__name__ = "Unsigned32"
_PmopsCfgcomaSwitchMode_Object = MibScalar
pmopsCfgcomaSwitchMode = _PmopsCfgcomaSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 9, 2, 1, 2),
    _PmopsCfgcomaSwitchMode_Type()
)
pmopsCfgcomaSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopsCfgcomaSwitchMode.setStatus("current")


class _PmopsCfgcomaRxPwrSetting1_Type(Unsigned32):
    """Custom type pmopsCfgcomaRxPwrSetting1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmopsCfgcomaRxPwrSetting1_Type.__name__ = "Unsigned32"
_PmopsCfgcomaRxPwrSetting1_Object = MibScalar
pmopsCfgcomaRxPwrSetting1 = _PmopsCfgcomaRxPwrSetting1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 9, 2, 1, 3),
    _PmopsCfgcomaRxPwrSetting1_Type()
)
pmopsCfgcomaRxPwrSetting1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopsCfgcomaRxPwrSetting1.setStatus("current")


class _PmopsCfgcomaRxPwrSetting2_Type(Unsigned32):
    """Custom type pmopsCfgcomaRxPwrSetting2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmopsCfgcomaRxPwrSetting2_Type.__name__ = "Unsigned32"
_PmopsCfgcomaRxPwrSetting2_Object = MibScalar
pmopsCfgcomaRxPwrSetting2 = _PmopsCfgcomaRxPwrSetting2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 9, 2, 1, 4),
    _PmopsCfgcomaRxPwrSetting2_Type()
)
pmopsCfgcomaRxPwrSetting2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopsCfgcomaRxPwrSetting2.setStatus("current")


class _PmopsCfgcomaOosMode_Type(Unsigned32):
    """Custom type pmopsCfgcomaOosMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmopsCfgcomaOosMode_Type.__name__ = "Unsigned32"
_PmopsCfgcomaOosMode_Object = MibScalar
pmopsCfgcomaOosMode = _PmopsCfgcomaOosMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 9, 2, 1, 5),
    _PmopsCfgcomaOosMode_Type()
)
pmopsCfgcomaOosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopsCfgcomaOosMode.setStatus("current")
_PmopstablecombStartup_ObjectIdentity = ObjectIdentity
pmopstablecombStartup = _PmopstablecombStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 9, 2, 2)
)


class _PmopsCfgcombSwitchMode_Type(Unsigned32):
    """Custom type pmopsCfgcombSwitchMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmopsCfgcombSwitchMode_Type.__name__ = "Unsigned32"
_PmopsCfgcombSwitchMode_Object = MibScalar
pmopsCfgcombSwitchMode = _PmopsCfgcombSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 9, 2, 2, 2),
    _PmopsCfgcombSwitchMode_Type()
)
pmopsCfgcombSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopsCfgcombSwitchMode.setStatus("current")


class _PmopsCfgcombRxPwrSetting1_Type(Unsigned32):
    """Custom type pmopsCfgcombRxPwrSetting1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmopsCfgcombRxPwrSetting1_Type.__name__ = "Unsigned32"
_PmopsCfgcombRxPwrSetting1_Object = MibScalar
pmopsCfgcombRxPwrSetting1 = _PmopsCfgcombRxPwrSetting1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 9, 2, 2, 3),
    _PmopsCfgcombRxPwrSetting1_Type()
)
pmopsCfgcombRxPwrSetting1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopsCfgcombRxPwrSetting1.setStatus("current")


class _PmopsCfgcombRxPwrSetting2_Type(Unsigned32):
    """Custom type pmopsCfgcombRxPwrSetting2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmopsCfgcombRxPwrSetting2_Type.__name__ = "Unsigned32"
_PmopsCfgcombRxPwrSetting2_Object = MibScalar
pmopsCfgcombRxPwrSetting2 = _PmopsCfgcombRxPwrSetting2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 9, 2, 2, 4),
    _PmopsCfgcombRxPwrSetting2_Type()
)
pmopsCfgcombRxPwrSetting2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopsCfgcombRxPwrSetting2.setStatus("current")


class _PmopsCfgcombOosMode_Type(Unsigned32):
    """Custom type pmopsCfgcombOosMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmopsCfgcombOosMode_Type.__name__ = "Unsigned32"
_PmopsCfgcombOosMode_Object = MibScalar
pmopsCfgcombOosMode = _PmopsCfgcombOosMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 9, 2, 2, 5),
    _PmopsCfgcombOosMode_Type()
)
pmopsCfgcombOosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopsCfgcombOosMode.setStatus("current")
_PmopsCfgLabels_ObjectIdentity = ObjectIdentity
pmopsCfgLabels = _PmopsCfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 9, 3)
)
_PmopsCfgLabelclientTable_Object = MibTable
pmopsCfgLabelclientTable = _PmopsCfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 9, 3, 1)
)
if mibBuilder.loadTexts:
    pmopsCfgLabelclientTable.setStatus("current")
_PmopsCfgLabelclientEntry_Object = MibTableRow
pmopsCfgLabelclientEntry = _PmopsCfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 9, 3, 1, 1)
)
pmopsCfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-Pmops-MIB", "pmopsCfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pmopsCfgLabelclientEntry.setStatus("current")


class _PmopsCfgLabelclientIndex_Type(Integer32):
    """Custom type pmopsCfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmopsCfgLabelclientIndex_Type.__name__ = "Integer32"
_PmopsCfgLabelclientIndex_Object = MibTableColumn
pmopsCfgLabelclientIndex = _PmopsCfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 9, 3, 1, 1, 1),
    _PmopsCfgLabelclientIndex_Type()
)
pmopsCfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsCfgLabelclientIndex.setStatus("current")


class _PmopsCfgLabelclientPortn_Type(DisplayString):
    """Custom type pmopsCfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PmopsCfgLabelclientPortn_Type.__name__ = "DisplayString"
_PmopsCfgLabelclientPortn_Object = MibTableColumn
pmopsCfgLabelclientPortn = _PmopsCfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 9, 3, 1, 1, 3),
    _PmopsCfgLabelclientPortn_Type()
)
pmopsCfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopsCfgLabelclientPortn.setStatus("current")
_PmopsCfgLabellineTable_Object = MibTable
pmopsCfgLabellineTable = _PmopsCfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 9, 3, 2)
)
if mibBuilder.loadTexts:
    pmopsCfgLabellineTable.setStatus("current")
_PmopsCfgLabellineEntry_Object = MibTableRow
pmopsCfgLabellineEntry = _PmopsCfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 9, 3, 2, 1)
)
pmopsCfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-Pmops-MIB", "pmopsCfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pmopsCfgLabellineEntry.setStatus("current")


class _PmopsCfgLabellineIndex_Type(Integer32):
    """Custom type pmopsCfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmopsCfgLabellineIndex_Type.__name__ = "Integer32"
_PmopsCfgLabellineIndex_Object = MibTableColumn
pmopsCfgLabellineIndex = _PmopsCfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 9, 3, 2, 1, 1),
    _PmopsCfgLabellineIndex_Type()
)
pmopsCfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopsCfgLabellineIndex.setStatus("current")


class _PmopsCfgLabellinePortn_Type(DisplayString):
    """Custom type pmopsCfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PmopsCfgLabellinePortn_Type.__name__ = "DisplayString"
_PmopsCfgLabellinePortn_Object = MibTableColumn
pmopsCfgLabellinePortn = _PmopsCfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 9, 3, 2, 1, 3),
    _PmopsCfgLabellinePortn_Type()
)
pmopsCfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopsCfgLabellinePortn.setStatus("current")
_PmopsCfgWriteConfiguration_Type = EkiOnOff
_PmopsCfgWriteConfiguration_Object = MibScalar
pmopsCfgWriteConfiguration = _PmopsCfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 9, 257),
    _PmopsCfgWriteConfiguration_Type()
)
pmopsCfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmopsCfgWriteConfiguration.setStatus("current")
_Pmopstraps_ObjectIdentity = ObjectIdentity
pmopstraps = _Pmopstraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 30, 10)
)


class _PmopstrapPortNumber_Type(Integer32):
    """Custom type pmopstrapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_PmopstrapPortNumber_Type.__name__ = "Integer32"
_PmopstrapPortNumber_Object = MibScalar
pmopstrapPortNumber = _PmopstrapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 10, 2),
    _PmopstrapPortNumber_Type()
)
pmopstrapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopstrapPortNumber.setStatus("current")


class _PmopstrapLineNumber_Type(Integer32):
    """Custom type pmopstrapLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_PmopstrapLineNumber_Type.__name__ = "Integer32"
_PmopstrapLineNumber_Object = MibScalar
pmopstrapLineNumber = _PmopstrapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 10, 3),
    _PmopstrapLineNumber_Type()
)
pmopstrapLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopstrapLineNumber.setStatus("current")


class _PmopstrapBoardNumber_Type(Integer32):
    """Custom type pmopstrapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_PmopstrapBoardNumber_Type.__name__ = "Integer32"
_PmopstrapBoardNumber_Object = MibScalar
pmopstrapBoardNumber = _PmopstrapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 30, 10, 4),
    _PmopstrapBoardNumber_Type()
)
pmopstrapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmopstrapBoardNumber.setStatus("current")

# Managed Objects groups


# Notification objects

pmopsComBTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 30, 10, 30)
)
pmopsComBTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pmops-MIB", "pmopsAlmCombMeasWng"),
        ("EKINOPS-Pmops-MIB", "pmopstrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmopsComBTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pmopsComBTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 30, 10, 31)
)
pmopsComBTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pmops-MIB", "pmopsAlmCombMeasWng"),
        ("EKINOPS-Pmops-MIB", "pmopstrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmopsComBTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pmopsComBTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 30, 10, 32)
)
pmopsComBTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pmops-MIB", "pmopsAlmCombMeasAlm"),
        ("EKINOPS-Pmops-MIB", "pmopstrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmopsComBTrapUrgentGoesOn.setStatus(
        "current"
    )

pmopsComBTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 30, 10, 33)
)
pmopsComBTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pmops-MIB", "pmopsAlmCombMeasAlm"),
        ("EKINOPS-Pmops-MIB", "pmopstrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmopsComBTrapUrgentGoesOff.setStatus(
        "current"
    )

pmopsComBTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 30, 10, 34)
)
pmopsComBTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pmops-MIB", "pmopsAlmCombFailAcc"),
        ("EKINOPS-Pmops-MIB", "pmopsAlmCombHwFailAcc"),
        ("EKINOPS-Pmops-MIB", "pmopstrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmopsComBTrapCritGoesOn.setStatus(
        "current"
    )

pmopsComBTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 30, 10, 35)
)
pmopsComBTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pmops-MIB", "pmopsAlmCombFailAcc"),
        ("EKINOPS-Pmops-MIB", "pmopsAlmCombHwFailAcc"),
        ("EKINOPS-Pmops-MIB", "pmopstrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmopsComBTrapCritGoesOff.setStatus(
        "current"
    )

pmopsComATrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 30, 10, 40)
)
pmopsComATrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pmops-MIB", "pmopsAlmComaMeasWng"),
        ("EKINOPS-Pmops-MIB", "pmopstrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmopsComATrapNotUrgentGoesOn.setStatus(
        "current"
    )

pmopsComATrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 30, 10, 41)
)
pmopsComATrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pmops-MIB", "pmopsAlmComaMeasWng"),
        ("EKINOPS-Pmops-MIB", "pmopstrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmopsComATrapNotUrgentGoesOff.setStatus(
        "current"
    )

pmopsComATrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 30, 10, 42)
)
pmopsComATrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pmops-MIB", "pmopsAlmComaMeasAlm"),
        ("EKINOPS-Pmops-MIB", "pmopstrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmopsComATrapUrgentGoesOn.setStatus(
        "current"
    )

pmopsComATrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 30, 10, 43)
)
pmopsComATrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pmops-MIB", "pmopsAlmComaMeasAlm"),
        ("EKINOPS-Pmops-MIB", "pmopstrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmopsComATrapUrgentGoesOff.setStatus(
        "current"
    )

pmopsComATrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 30, 10, 44)
)
pmopsComATrapCritGoesOn.setObjects(
      *(("EKINOPS-Pmops-MIB", "pmopsAlmComaFailAcc"),
        ("EKINOPS-Pmops-MIB", "pmopsAlmComaHwFailAcc"),
        ("EKINOPS-Pmops-MIB", "pmopstrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmopsComATrapCritGoesOn.setStatus(
        "current"
    )

pmopsComATrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 30, 10, 45)
)
pmopsComATrapCritGoesOff.setObjects(
      *(("EKINOPS-Pmops-MIB", "pmopsAlmComaFailAcc"),
        ("EKINOPS-Pmops-MIB", "pmopsAlmComaHwFailAcc"),
        ("EKINOPS-Pmops-MIB", "pmopstrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmopsComATrapCritGoesOff.setStatus(
        "current"
    )

pmopsPowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 30, 10, 50)
)
pmopsPowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pmops-MIB", "pmopsAlmDefFuseB"),
        ("EKINOPS-Pmops-MIB", "pmopsAlmDefFuseA"),
        ("EKINOPS-Pmops-MIB", "pmopstrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmopsPowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pmopsPowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 30, 10, 51)
)
pmopsPowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pmops-MIB", "pmopsAlmDefFuseB"),
        ("EKINOPS-Pmops-MIB", "pmopsAlmDefFuseA"),
        ("EKINOPS-Pmops-MIB", "pmopstrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmopsPowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Pmops-MIB",
    **{"PmopsSwitchMode": PmopsSwitchMode,
       "modulePmops": modulePmops,
       "pmopsalarms": pmopsalarms,
       "pmopsAlmOther": pmopsAlmOther,
       "pmopsAlmOtherNurg": pmopsAlmOtherNurg,
       "pmopsAlmsynthAlm2": pmopsAlmsynthAlm2,
       "pmopsAlmConfTableSave": pmopsAlmConfTableSave,
       "pmopsAlmInvUpload": pmopsAlmInvUpload,
       "pmopsAlmConfTableLoad": pmopsAlmConfTableLoad,
       "pmopsAlmCorrelatOff": pmopsAlmCorrelatOff,
       "pmopsAlmOtherUrg": pmopsAlmOtherUrg,
       "pmopsAlmmodInitFailLevel2": pmopsAlmmodInitFailLevel2,
       "pmopsAlmRegReadFail": pmopsAlmRegReadFail,
       "pmopsAlmResetHwInitFail": pmopsAlmResetHwInitFail,
       "pmopsAlmConfReadFail": pmopsAlmConfReadFail,
       "pmopsAlmGwIdentFail": pmopsAlmGwIdentFail,
       "pmopsAlmCalibReadFail": pmopsAlmCalibReadFail,
       "pmopsAlmThreshConfFail": pmopsAlmThreshConfFail,
       "pmopsAlmmodInitFailLevel3": pmopsAlmmodInitFailLevel3,
       "pmopsAlmOptIdentFail": pmopsAlmOptIdentFail,
       "pmopsAlmGwColdBootForced": pmopsAlmGwColdBootForced,
       "pmopsAlmOtherCrit": pmopsAlmOtherCrit,
       "pmopsAlmsynthAlm0": pmopsAlmsynthAlm0,
       "pmopsAlmModuleGlobFailure": pmopsAlmModuleGlobFailure,
       "pmopsAlmDefFuseA": pmopsAlmDefFuseA,
       "pmopsAlmDefFuseB": pmopsAlmDefFuseB,
       "pmopsAlmComa": pmopsAlmComa,
       "pmopsAlmComaNurg": pmopsAlmComaNurg,
       "pmopsAlmcomaMeasWng": pmopsAlmcomaMeasWng,
       "pmopsAlmComaTx1PwrLowWng": pmopsAlmComaTx1PwrLowWng,
       "pmopsAlmComaTx1PwrHighWng": pmopsAlmComaTx1PwrHighWng,
       "pmopsAlmComaRx1PwrLowWng": pmopsAlmComaRx1PwrLowWng,
       "pmopsAlmComaRx1PwrHighWng": pmopsAlmComaRx1PwrHighWng,
       "pmopsAlmComaTx2PwrLowWng": pmopsAlmComaTx2PwrLowWng,
       "pmopsAlmComaTx2PwrHighWng": pmopsAlmComaTx2PwrHighWng,
       "pmopsAlmComaRx2PwrLowWng": pmopsAlmComaRx2PwrLowWng,
       "pmopsAlmComaRx2PwrHighWng": pmopsAlmComaRx2PwrHighWng,
       "pmopsAlmComaUrg": pmopsAlmComaUrg,
       "pmopsAlmcomaAccessioAlm": pmopsAlmcomaAccessioAlm,
       "pmopsAlmComaLosRx1": pmopsAlmComaLosRx1,
       "pmopsAlmComaLosRx2": pmopsAlmComaLosRx2,
       "pmopsAlmComaLosTx1": pmopsAlmComaLosTx1,
       "pmopsAlmComaLosTx2": pmopsAlmComaLosTx2,
       "pmopsAlmComaSwitchPosition1": pmopsAlmComaSwitchPosition1,
       "pmopsAlmComaSwitchPosition2": pmopsAlmComaSwitchPosition2,
       "pmopsAlmComaSwitchFail": pmopsAlmComaSwitchFail,
       "pmopsAlmcomaMeasAlm": pmopsAlmcomaMeasAlm,
       "pmopsAlmComaTx1PwrLowAla": pmopsAlmComaTx1PwrLowAla,
       "pmopsAlmComaTx1PwrHighAla": pmopsAlmComaTx1PwrHighAla,
       "pmopsAlmComaRx1PwrLowAla": pmopsAlmComaRx1PwrLowAla,
       "pmopsAlmComaRx1PwrHighAla": pmopsAlmComaRx1PwrHighAla,
       "pmopsAlmComaTx2PwrLowAla": pmopsAlmComaTx2PwrLowAla,
       "pmopsAlmComaTx2PwrHighAla": pmopsAlmComaTx2PwrHighAla,
       "pmopsAlmComaRx2PwrLowAla": pmopsAlmComaRx2PwrLowAla,
       "pmopsAlmComaRx2PwrHighAla": pmopsAlmComaRx2PwrHighAla,
       "pmopsAlmComaCrit": pmopsAlmComaCrit,
       "pmopsAlmsynthAlmComa": pmopsAlmsynthAlmComa,
       "pmopsAlmComaHwFailAcc": pmopsAlmComaHwFailAcc,
       "pmopsAlmComaLocalOos": pmopsAlmComaLocalOos,
       "pmopsAlmComaMeasWng": pmopsAlmComaMeasWng,
       "pmopsAlmComaMeasAlm": pmopsAlmComaMeasAlm,
       "pmopsAlmComaFailAcc": pmopsAlmComaFailAcc,
       "pmopsAlmComb": pmopsAlmComb,
       "pmopsAlmCombNurg": pmopsAlmCombNurg,
       "pmopsAlmcombMeasWng": pmopsAlmcombMeasWng,
       "pmopsAlmCombTx1PwrLowWng": pmopsAlmCombTx1PwrLowWng,
       "pmopsAlmCombTx1PwrHighWng": pmopsAlmCombTx1PwrHighWng,
       "pmopsAlmCombRx1PwrLowWng": pmopsAlmCombRx1PwrLowWng,
       "pmopsAlmCombRx1PwrHighWng": pmopsAlmCombRx1PwrHighWng,
       "pmopsAlmCombTx2PwrLowWng": pmopsAlmCombTx2PwrLowWng,
       "pmopsAlmCombTx2PwrHighWng": pmopsAlmCombTx2PwrHighWng,
       "pmopsAlmCombRx2PwrLowWng": pmopsAlmCombRx2PwrLowWng,
       "pmopsAlmCombRx2PwrHighWng": pmopsAlmCombRx2PwrHighWng,
       "pmopsAlmCombUrg": pmopsAlmCombUrg,
       "pmopsAlmcombAccessioAlm": pmopsAlmcombAccessioAlm,
       "pmopsAlmCombLosRx1": pmopsAlmCombLosRx1,
       "pmopsAlmCombLosRx2": pmopsAlmCombLosRx2,
       "pmopsAlmCombLosTx1": pmopsAlmCombLosTx1,
       "pmopsAlmCombLosTx2": pmopsAlmCombLosTx2,
       "pmopsAlmCombSwitchPosition1": pmopsAlmCombSwitchPosition1,
       "pmopsAlmCombSwitchPosition2": pmopsAlmCombSwitchPosition2,
       "pmopsAlmCombSwitchFail": pmopsAlmCombSwitchFail,
       "pmopsAlmcombMeasAla": pmopsAlmcombMeasAla,
       "pmopsAlmCombTx1PwrLowAla": pmopsAlmCombTx1PwrLowAla,
       "pmopsAlmCombTx1PwrHighAla": pmopsAlmCombTx1PwrHighAla,
       "pmopsAlmCombRx1PwrLowAla": pmopsAlmCombRx1PwrLowAla,
       "pmopsAlmCombRx1PwrHighAla": pmopsAlmCombRx1PwrHighAla,
       "pmopsAlmCombTx2PwrLowAla": pmopsAlmCombTx2PwrLowAla,
       "pmopsAlmCombTx2PwrHighAla": pmopsAlmCombTx2PwrHighAla,
       "pmopsAlmCombRx2PwrLowAla": pmopsAlmCombRx2PwrLowAla,
       "pmopsAlmCombRx2PwrHighAla": pmopsAlmCombRx2PwrHighAla,
       "pmopsAlmCombCrit": pmopsAlmCombCrit,
       "pmopsAlmsynthAlmComb": pmopsAlmsynthAlmComb,
       "pmopsAlmCombHwFailAcc": pmopsAlmCombHwFailAcc,
       "pmopsAlmCombLocalOos": pmopsAlmCombLocalOos,
       "pmopsAlmCombMeasWng": pmopsAlmCombMeasWng,
       "pmopsAlmCombMeasAlm": pmopsAlmCombMeasAlm,
       "pmopsAlmCombFailAcc": pmopsAlmCombFailAcc,
       "pmopsmeasures": pmopsmeasures,
       "pmopsMesrOther": pmopsMesrOther,
       "pmopsMesrComa": pmopsMesrComa,
       "pmopsMesrcomaTxPower1": pmopsMesrcomaTxPower1,
       "pmopsMesrcomaTxPower2": pmopsMesrcomaTxPower2,
       "pmopsMesrcomaRxPower1": pmopsMesrcomaRxPower1,
       "pmopsMesrcomaRxPower2": pmopsMesrcomaRxPower2,
       "pmopsMesrComb": pmopsMesrComb,
       "pmopsMesrcombTxPower1": pmopsMesrcombTxPower1,
       "pmopsMesrcombTxPower2": pmopsMesrcombTxPower2,
       "pmopsMesrcombRxPower1": pmopsMesrcombRxPower1,
       "pmopsMesrcombRxPower2": pmopsMesrcombRxPower2,
       "pmopscontrolsWrite": pmopscontrolsWrite,
       "pmopsCtrlOther": pmopsCtrlOther,
       "pmopsCtrlsynth0": pmopsCtrlsynth0,
       "pmopsCtrlConfLoad": pmopsCtrlConfLoad,
       "pmopsCtrlConfFlash": pmopsCtrlConfFlash,
       "pmopsCtrlConfClear": pmopsCtrlConfClear,
       "pmopsCtrlsynth4": pmopsCtrlsynth4,
       "pmopsCtrlCorrelatOn": pmopsCtrlCorrelatOn,
       "pmopsCtrlCorrelatOff": pmopsCtrlCorrelatOff,
       "pmopsCtrlswMgnt": pmopsCtrlswMgnt,
       "pmopsCtrlColdReset": pmopsCtrlColdReset,
       "pmopsCtrlWarmReset": pmopsCtrlWarmReset,
       "pmopsCtrlledTest": pmopsCtrlledTest,
       "pmopsCtrlGreenLed": pmopsCtrlGreenLed,
       "pmopsCtrlRedLed": pmopsCtrlRedLed,
       "pmopsCtrlLedOff": pmopsCtrlLedOff,
       "pmopsCtrlComa": pmopsCtrlComa,
       "pmopsCtrlcomaSwitchMode": pmopsCtrlcomaSwitchMode,
       "pmopsCtrlcomaOosMode": pmopsCtrlcomaOosMode,
       "pmopsCtrlComaOosMode": pmopsCtrlComaOosMode,
       "pmopsCtrlcomaRxPwrSetting1": pmopsCtrlcomaRxPwrSetting1,
       "pmopsCtrlcomaRxPwrSetting2": pmopsCtrlcomaRxPwrSetting2,
       "pmopsCtrlComb": pmopsCtrlComb,
       "pmopsCtrlcombSwitchMode": pmopsCtrlcombSwitchMode,
       "pmopsCtrlcombOosMode": pmopsCtrlcombOosMode,
       "pmopsCtrlCombOosMode": pmopsCtrlCombOosMode,
       "pmopsCtrlcombRxPwrSetting1": pmopsCtrlcombRxPwrSetting1,
       "pmopsCtrlcombRxPwrSetting2": pmopsCtrlcombRxPwrSetting2,
       "pmopsri": pmopsri,
       "pmopsriTable": pmopsriTable,
       "pmopsRinvReloadInventory": pmopsRinvReloadInventory,
       "pmopsRinvHwPlatform": pmopsRinvHwPlatform,
       "pmopsRinvModulePlatform": pmopsRinvModulePlatform,
       "pmopsRinvSwPlatform": pmopsRinvSwPlatform,
       "pmopsRinvLine1SFP": pmopsRinvLine1SFP,
       "pmopsRinvLine2SFP": pmopsRinvLine2SFP,
       "pmopsConfig": pmopsConfig,
       "pmopsCfgLsd": pmopsCfgLsd,
       "pmopstablecomaLsd": pmopstablecomaLsd,
       "pmopsCfgStartUp": pmopsCfgStartUp,
       "pmopstablecomaStartup": pmopstablecomaStartup,
       "pmopsCfgcomaSwitchMode": pmopsCfgcomaSwitchMode,
       "pmopsCfgcomaRxPwrSetting1": pmopsCfgcomaRxPwrSetting1,
       "pmopsCfgcomaRxPwrSetting2": pmopsCfgcomaRxPwrSetting2,
       "pmopsCfgcomaOosMode": pmopsCfgcomaOosMode,
       "pmopstablecombStartup": pmopstablecombStartup,
       "pmopsCfgcombSwitchMode": pmopsCfgcombSwitchMode,
       "pmopsCfgcombRxPwrSetting1": pmopsCfgcombRxPwrSetting1,
       "pmopsCfgcombRxPwrSetting2": pmopsCfgcombRxPwrSetting2,
       "pmopsCfgcombOosMode": pmopsCfgcombOosMode,
       "pmopsCfgLabels": pmopsCfgLabels,
       "pmopsCfgLabelclientTable": pmopsCfgLabelclientTable,
       "pmopsCfgLabelclientEntry": pmopsCfgLabelclientEntry,
       "pmopsCfgLabelclientIndex": pmopsCfgLabelclientIndex,
       "pmopsCfgLabelclientPortn": pmopsCfgLabelclientPortn,
       "pmopsCfgLabellineTable": pmopsCfgLabellineTable,
       "pmopsCfgLabellineEntry": pmopsCfgLabellineEntry,
       "pmopsCfgLabellineIndex": pmopsCfgLabellineIndex,
       "pmopsCfgLabellinePortn": pmopsCfgLabellinePortn,
       "pmopsCfgWriteConfiguration": pmopsCfgWriteConfiguration,
       "pmopstraps": pmopstraps,
       "pmopstrapPortNumber": pmopstrapPortNumber,
       "pmopstrapLineNumber": pmopstrapLineNumber,
       "pmopstrapBoardNumber": pmopstrapBoardNumber,
       "pmopsComBTrapNotUrgentGoesOn": pmopsComBTrapNotUrgentGoesOn,
       "pmopsComBTrapNotUrgentGoesOff": pmopsComBTrapNotUrgentGoesOff,
       "pmopsComBTrapUrgentGoesOn": pmopsComBTrapUrgentGoesOn,
       "pmopsComBTrapUrgentGoesOff": pmopsComBTrapUrgentGoesOff,
       "pmopsComBTrapCritGoesOn": pmopsComBTrapCritGoesOn,
       "pmopsComBTrapCritGoesOff": pmopsComBTrapCritGoesOff,
       "pmopsComATrapNotUrgentGoesOn": pmopsComATrapNotUrgentGoesOn,
       "pmopsComATrapNotUrgentGoesOff": pmopsComATrapNotUrgentGoesOff,
       "pmopsComATrapUrgentGoesOn": pmopsComATrapUrgentGoesOn,
       "pmopsComATrapUrgentGoesOff": pmopsComATrapUrgentGoesOff,
       "pmopsComATrapCritGoesOn": pmopsComATrapCritGoesOn,
       "pmopsComATrapCritGoesOff": pmopsComATrapCritGoesOff,
       "pmopsPowerTrapUrgentGoesOn": pmopsPowerTrapUrgentGoesOn,
       "pmopsPowerTrapUrgentGoesOff": pmopsPowerTrapUrgentGoesOff}
)
