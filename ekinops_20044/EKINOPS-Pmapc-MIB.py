# SNMP MIB module (EKINOPS-Pmapc-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Pmapc-MIB.mib
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

modulePmapc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42)
)
if mibBuilder.loadTexts:
    modulePmapc.setRevisions(
        ("2009-05-29 00:00",
         "2009-09-29 00:00",
         "2010-02-25 00:00",
         "2010-11-05 00:00",
         "2010-12-14 00:00",
         "2012-07-04 00:00",
         "2014-03-25 00:00",
         "2014-11-21 00:00",
         "2016-05-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Pmapcalarms_ObjectIdentity = ObjectIdentity
pmapcalarms = _Pmapcalarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2)
)
_PmapcAlmOther_ObjectIdentity = ObjectIdentity
pmapcAlmOther = _PmapcAlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1)
)
_PmapcAlmOtherNurg_ObjectIdentity = ObjectIdentity
pmapcAlmOtherNurg = _PmapcAlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 1)
)
_PmapcAlmsynthAlm2_ObjectIdentity = ObjectIdentity
pmapcAlmsynthAlm2 = _PmapcAlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 1, 2)
)
_PmapcAlmConfTableSave_Type = EkiOnOff
_PmapcAlmConfTableSave_Object = MibScalar
pmapcAlmConfTableSave = _PmapcAlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 1, 2, 1),
    _PmapcAlmConfTableSave_Type()
)
pmapcAlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmConfTableSave.setStatus("current")
_PmapcAlmInvUpload_Type = EkiOnOff
_PmapcAlmInvUpload_Object = MibScalar
pmapcAlmInvUpload = _PmapcAlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 1, 2, 2),
    _PmapcAlmInvUpload_Type()
)
pmapcAlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmInvUpload.setStatus("current")
_PmapcAlmConfTableLoad_Type = EkiOnOff
_PmapcAlmConfTableLoad_Object = MibScalar
pmapcAlmConfTableLoad = _PmapcAlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 1, 2, 3),
    _PmapcAlmConfTableLoad_Type()
)
pmapcAlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmConfTableLoad.setStatus("current")
_PmapcAlmCorrelatOff_Type = EkiOnOff
_PmapcAlmCorrelatOff_Object = MibScalar
pmapcAlmCorrelatOff = _PmapcAlmCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 1, 2, 4),
    _PmapcAlmCorrelatOff_Type()
)
pmapcAlmCorrelatOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmCorrelatOff.setStatus("current")
_PmapcAlmmoduleWarning_ObjectIdentity = ObjectIdentity
pmapcAlmmoduleWarning = _PmapcAlmmoduleWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 1, 65)
)
_PmapcAlmPwrInLowWng_Type = EkiOnOff
_PmapcAlmPwrInLowWng_Object = MibScalar
pmapcAlmPwrInLowWng = _PmapcAlmPwrInLowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 1, 65, 1),
    _PmapcAlmPwrInLowWng_Type()
)
pmapcAlmPwrInLowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmPwrInLowWng.setStatus("current")
_PmapcAlmPwrInHighWng_Type = EkiOnOff
_PmapcAlmPwrInHighWng_Object = MibScalar
pmapcAlmPwrInHighWng = _PmapcAlmPwrInHighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 1, 65, 2),
    _PmapcAlmPwrInHighWng_Type()
)
pmapcAlmPwrInHighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmPwrInHighWng.setStatus("current")
_PmapcAlmPwrOutLowWng_Type = EkiOnOff
_PmapcAlmPwrOutLowWng_Object = MibScalar
pmapcAlmPwrOutLowWng = _PmapcAlmPwrOutLowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 1, 65, 3),
    _PmapcAlmPwrOutLowWng_Type()
)
pmapcAlmPwrOutLowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmPwrOutLowWng.setStatus("current")
_PmapcAlmPwrOutHighWng_Type = EkiOnOff
_PmapcAlmPwrOutHighWng_Object = MibScalar
pmapcAlmPwrOutHighWng = _PmapcAlmPwrOutHighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 1, 65, 4),
    _PmapcAlmPwrOutHighWng_Type()
)
pmapcAlmPwrOutHighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmPwrOutHighWng.setStatus("current")
_PmapcAlmEamAttLowWng_Type = EkiOnOff
_PmapcAlmEamAttLowWng_Object = MibScalar
pmapcAlmEamAttLowWng = _PmapcAlmEamAttLowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 1, 65, 5),
    _PmapcAlmEamAttLowWng_Type()
)
pmapcAlmEamAttLowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmEamAttLowWng.setStatus("current")
_PmapcAlmEamAttHighWng_Type = EkiOnOff
_PmapcAlmEamAttHighWng_Object = MibScalar
pmapcAlmEamAttHighWng = _PmapcAlmEamAttHighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 1, 65, 6),
    _PmapcAlmEamAttHighWng_Type()
)
pmapcAlmEamAttHighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmEamAttHighWng.setStatus("current")
_PmapcAlmOtherUrg_ObjectIdentity = ObjectIdentity
pmapcAlmOtherUrg = _PmapcAlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 2)
)
_PmapcAlmmoduleAlarm_ObjectIdentity = ObjectIdentity
pmapcAlmmoduleAlarm = _PmapcAlmmoduleAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 2, 64)
)
_PmapcAlmPwrInLowAla_Type = EkiOnOff
_PmapcAlmPwrInLowAla_Object = MibScalar
pmapcAlmPwrInLowAla = _PmapcAlmPwrInLowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 2, 64, 1),
    _PmapcAlmPwrInLowAla_Type()
)
pmapcAlmPwrInLowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmPwrInLowAla.setStatus("current")
_PmapcAlmPwrInHighAla_Type = EkiOnOff
_PmapcAlmPwrInHighAla_Object = MibScalar
pmapcAlmPwrInHighAla = _PmapcAlmPwrInHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 2, 64, 2),
    _PmapcAlmPwrInHighAla_Type()
)
pmapcAlmPwrInHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmPwrInHighAla.setStatus("current")
_PmapcAlmPwrOutLowAla_Type = EkiOnOff
_PmapcAlmPwrOutLowAla_Object = MibScalar
pmapcAlmPwrOutLowAla = _PmapcAlmPwrOutLowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 2, 64, 3),
    _PmapcAlmPwrOutLowAla_Type()
)
pmapcAlmPwrOutLowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmPwrOutLowAla.setStatus("current")
_PmapcAlmPwrOutHighAla_Type = EkiOnOff
_PmapcAlmPwrOutHighAla_Object = MibScalar
pmapcAlmPwrOutHighAla = _PmapcAlmPwrOutHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 2, 64, 4),
    _PmapcAlmPwrOutHighAla_Type()
)
pmapcAlmPwrOutHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmPwrOutHighAla.setStatus("current")
_PmapcAlmEamAttLowAla_Type = EkiOnOff
_PmapcAlmEamAttLowAla_Object = MibScalar
pmapcAlmEamAttLowAla = _PmapcAlmEamAttLowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 2, 64, 5),
    _PmapcAlmEamAttLowAla_Type()
)
pmapcAlmEamAttLowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmEamAttLowAla.setStatus("current")
_PmapcAlmEamAttHighAla_Type = EkiOnOff
_PmapcAlmEamAttHighAla_Object = MibScalar
pmapcAlmEamAttHighAla = _PmapcAlmEamAttHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 2, 64, 6),
    _PmapcAlmEamAttHighAla_Type()
)
pmapcAlmEamAttHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmEamAttHighAla.setStatus("current")
_PmapcAlmLossInputSignal_Type = EkiOnOff
_PmapcAlmLossInputSignal_Object = MibScalar
pmapcAlmLossInputSignal = _PmapcAlmLossInputSignal_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 2, 64, 16),
    _PmapcAlmLossInputSignal_Type()
)
pmapcAlmLossInputSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmLossInputSignal.setStatus("current")
_PmapcAlmmodInitFailLevel2_ObjectIdentity = ObjectIdentity
pmapcAlmmodInitFailLevel2 = _PmapcAlmmodInitFailLevel2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 2, 70)
)
_PmapcAlmRegReadFail_Type = EkiOnOff
_PmapcAlmRegReadFail_Object = MibScalar
pmapcAlmRegReadFail = _PmapcAlmRegReadFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 2, 70, 1),
    _PmapcAlmRegReadFail_Type()
)
pmapcAlmRegReadFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmRegReadFail.setStatus("current")
_PmapcAlmResetHwInitFail_Type = EkiOnOff
_PmapcAlmResetHwInitFail_Object = MibScalar
pmapcAlmResetHwInitFail = _PmapcAlmResetHwInitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 2, 70, 2),
    _PmapcAlmResetHwInitFail_Type()
)
pmapcAlmResetHwInitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmResetHwInitFail.setStatus("current")
_PmapcAlmConfReadFail_Type = EkiOnOff
_PmapcAlmConfReadFail_Object = MibScalar
pmapcAlmConfReadFail = _PmapcAlmConfReadFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 2, 70, 3),
    _PmapcAlmConfReadFail_Type()
)
pmapcAlmConfReadFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmConfReadFail.setStatus("current")
_PmapcAlmInvReadFail_Type = EkiOnOff
_PmapcAlmInvReadFail_Object = MibScalar
pmapcAlmInvReadFail = _PmapcAlmInvReadFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 2, 70, 4),
    _PmapcAlmInvReadFail_Type()
)
pmapcAlmInvReadFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmInvReadFail.setStatus("current")
_PmapcAlmCalibReadFail_Type = EkiOnOff
_PmapcAlmCalibReadFail_Object = MibScalar
pmapcAlmCalibReadFail = _PmapcAlmCalibReadFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 2, 70, 6),
    _PmapcAlmCalibReadFail_Type()
)
pmapcAlmCalibReadFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmCalibReadFail.setStatus("current")
_PmapcAlmThreshConfFail_Type = EkiOnOff
_PmapcAlmThreshConfFail_Object = MibScalar
pmapcAlmThreshConfFail = _PmapcAlmThreshConfFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 2, 70, 7),
    _PmapcAlmThreshConfFail_Type()
)
pmapcAlmThreshConfFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmThreshConfFail.setStatus("current")
_PmapcAlmmodInitFailLevel3_ObjectIdentity = ObjectIdentity
pmapcAlmmodInitFailLevel3 = _PmapcAlmmodInitFailLevel3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 2, 71)
)
_PmapcAlmOptIdentFail_Type = EkiOnOff
_PmapcAlmOptIdentFail_Object = MibScalar
pmapcAlmOptIdentFail = _PmapcAlmOptIdentFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 2, 71, 1),
    _PmapcAlmOptIdentFail_Type()
)
pmapcAlmOptIdentFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmOptIdentFail.setStatus("current")
_PmapcAlmOtherCrit_ObjectIdentity = ObjectIdentity
pmapcAlmOtherCrit = _PmapcAlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 3)
)
_PmapcAlmsynthAlm0_ObjectIdentity = ObjectIdentity
pmapcAlmsynthAlm0 = _PmapcAlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 3, 0)
)
_PmapcAlmPwrInAla_Type = EkiOnOff
_PmapcAlmPwrInAla_Object = MibScalar
pmapcAlmPwrInAla = _PmapcAlmPwrInAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 3, 0, 5),
    _PmapcAlmPwrInAla_Type()
)
pmapcAlmPwrInAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmPwrInAla.setStatus("current")
_PmapcAlmPwrInWng_Type = EkiOnOff
_PmapcAlmPwrInWng_Object = MibScalar
pmapcAlmPwrInWng = _PmapcAlmPwrInWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 3, 0, 6),
    _PmapcAlmPwrInWng_Type()
)
pmapcAlmPwrInWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmPwrInWng.setStatus("current")
_PmapcAlmPwrOutAla_Type = EkiOnOff
_PmapcAlmPwrOutAla_Object = MibScalar
pmapcAlmPwrOutAla = _PmapcAlmPwrOutAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 3, 0, 7),
    _PmapcAlmPwrOutAla_Type()
)
pmapcAlmPwrOutAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmPwrOutAla.setStatus("current")
_PmapcAlmPwrOutWng_Type = EkiOnOff
_PmapcAlmPwrOutWng_Object = MibScalar
pmapcAlmPwrOutWng = _PmapcAlmPwrOutWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 3, 0, 8),
    _PmapcAlmPwrOutWng_Type()
)
pmapcAlmPwrOutWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmPwrOutWng.setStatus("current")
_PmapcAlmModuleGlobFailure_Type = EkiOnOff
_PmapcAlmModuleGlobFailure_Object = MibScalar
pmapcAlmModuleGlobFailure = _PmapcAlmModuleGlobFailure_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 3, 0, 9),
    _PmapcAlmModuleGlobFailure_Type()
)
pmapcAlmModuleGlobFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmModuleGlobFailure.setStatus("current")
_PmapcAlmDefFuseA_Type = EkiOnOff
_PmapcAlmDefFuseA_Object = MibScalar
pmapcAlmDefFuseA = _PmapcAlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 3, 0, 15),
    _PmapcAlmDefFuseA_Type()
)
pmapcAlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmDefFuseA.setStatus("current")
_PmapcAlmDefFuseB_Type = EkiOnOff
_PmapcAlmDefFuseB_Object = MibScalar
pmapcAlmDefFuseB = _PmapcAlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 1, 3, 0, 16),
    _PmapcAlmDefFuseB_Type()
)
pmapcAlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmDefFuseB.setStatus("current")
_PmapcAlmClient_ObjectIdentity = ObjectIdentity
pmapcAlmClient = _PmapcAlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 2)
)
_PmapcAlmClientNurg_ObjectIdentity = ObjectIdentity
pmapcAlmClientNurg = _PmapcAlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 2, 1)
)
_PmapcAlmlaser1MeasWng_ObjectIdentity = ObjectIdentity
pmapcAlmlaser1MeasWng = _PmapcAlmlaser1MeasWng_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 2, 1, 18)
)
_PmapcAlmPwrLas1LowWng_Type = EkiOnOff
_PmapcAlmPwrLas1LowWng_Object = MibScalar
pmapcAlmPwrLas1LowWng = _PmapcAlmPwrLas1LowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 2, 1, 18, 1),
    _PmapcAlmPwrLas1LowWng_Type()
)
pmapcAlmPwrLas1LowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmPwrLas1LowWng.setStatus("current")
_PmapcAlmPwrLas1HighWng_Type = EkiOnOff
_PmapcAlmPwrLas1HighWng_Object = MibScalar
pmapcAlmPwrLas1HighWng = _PmapcAlmPwrLas1HighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 2, 1, 18, 2),
    _PmapcAlmPwrLas1HighWng_Type()
)
pmapcAlmPwrLas1HighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmPwrLas1HighWng.setStatus("current")
_PmapcAlmVthLas1LowWng_Type = EkiOnOff
_PmapcAlmVthLas1LowWng_Object = MibScalar
pmapcAlmVthLas1LowWng = _PmapcAlmVthLas1LowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 2, 1, 18, 3),
    _PmapcAlmVthLas1LowWng_Type()
)
pmapcAlmVthLas1LowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmVthLas1LowWng.setStatus("current")
_PmapcAlmVthLas1HighWng_Type = EkiOnOff
_PmapcAlmVthLas1HighWng_Object = MibScalar
pmapcAlmVthLas1HighWng = _PmapcAlmVthLas1HighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 2, 1, 18, 4),
    _PmapcAlmVthLas1HighWng_Type()
)
pmapcAlmVthLas1HighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmVthLas1HighWng.setStatus("current")
_PmapcAlmVtecLas1LowWng_Type = EkiOnOff
_PmapcAlmVtecLas1LowWng_Object = MibScalar
pmapcAlmVtecLas1LowWng = _PmapcAlmVtecLas1LowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 2, 1, 18, 5),
    _PmapcAlmVtecLas1LowWng_Type()
)
pmapcAlmVtecLas1LowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmVtecLas1LowWng.setStatus("current")
_PmapcAlmVtecLas1HighWng_Type = EkiOnOff
_PmapcAlmVtecLas1HighWng_Object = MibScalar
pmapcAlmVtecLas1HighWng = _PmapcAlmVtecLas1HighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 2, 1, 18, 6),
    _PmapcAlmVtecLas1HighWng_Type()
)
pmapcAlmVtecLas1HighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmVtecLas1HighWng.setStatus("current")
_PmapcAlmILas1LowWng_Type = EkiOnOff
_PmapcAlmILas1LowWng_Object = MibScalar
pmapcAlmILas1LowWng = _PmapcAlmILas1LowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 2, 1, 18, 7),
    _PmapcAlmILas1LowWng_Type()
)
pmapcAlmILas1LowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmILas1LowWng.setStatus("current")
_PmapcAlmILas1HighWng_Type = EkiOnOff
_PmapcAlmILas1HighWng_Object = MibScalar
pmapcAlmILas1HighWng = _PmapcAlmILas1HighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 2, 1, 18, 8),
    _PmapcAlmILas1HighWng_Type()
)
pmapcAlmILas1HighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmILas1HighWng.setStatus("current")
_PmapcAlmClientUrg_ObjectIdentity = ObjectIdentity
pmapcAlmClientUrg = _PmapcAlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 2, 2)
)
_PmapcAlmlaser1Alm_ObjectIdentity = ObjectIdentity
pmapcAlmlaser1Alm = _PmapcAlmlaser1Alm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 2, 2, 16)
)
_PmapcAlmLas1Fail_Type = EkiOnOff
_PmapcAlmLas1Fail_Object = MibScalar
pmapcAlmLas1Fail = _PmapcAlmLas1Fail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 2, 2, 16, 1),
    _PmapcAlmLas1Fail_Type()
)
pmapcAlmLas1Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmLas1Fail.setStatus("current")
_PmapcAlmLas1Tec1Fail_Type = EkiOnOff
_PmapcAlmLas1Tec1Fail_Object = MibScalar
pmapcAlmLas1Tec1Fail = _PmapcAlmLas1Tec1Fail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 2, 2, 16, 2),
    _PmapcAlmLas1Tec1Fail_Type()
)
pmapcAlmLas1Tec1Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmLas1Tec1Fail.setStatus("current")
_PmapcAlmlaser1MeasAlm_ObjectIdentity = ObjectIdentity
pmapcAlmlaser1MeasAlm = _PmapcAlmlaser1MeasAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 2, 2, 17)
)
_PmapcAlmPwrLas1LowAla_Type = EkiOnOff
_PmapcAlmPwrLas1LowAla_Object = MibScalar
pmapcAlmPwrLas1LowAla = _PmapcAlmPwrLas1LowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 2, 2, 17, 1),
    _PmapcAlmPwrLas1LowAla_Type()
)
pmapcAlmPwrLas1LowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmPwrLas1LowAla.setStatus("current")
_PmapcAlmPwrLas1HighAla_Type = EkiOnOff
_PmapcAlmPwrLas1HighAla_Object = MibScalar
pmapcAlmPwrLas1HighAla = _PmapcAlmPwrLas1HighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 2, 2, 17, 2),
    _PmapcAlmPwrLas1HighAla_Type()
)
pmapcAlmPwrLas1HighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmPwrLas1HighAla.setStatus("current")
_PmapcAlmVthLas1LowAla_Type = EkiOnOff
_PmapcAlmVthLas1LowAla_Object = MibScalar
pmapcAlmVthLas1LowAla = _PmapcAlmVthLas1LowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 2, 2, 17, 3),
    _PmapcAlmVthLas1LowAla_Type()
)
pmapcAlmVthLas1LowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmVthLas1LowAla.setStatus("current")
_PmapcAlmVthLas1HighAla_Type = EkiOnOff
_PmapcAlmVthLas1HighAla_Object = MibScalar
pmapcAlmVthLas1HighAla = _PmapcAlmVthLas1HighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 2, 2, 17, 4),
    _PmapcAlmVthLas1HighAla_Type()
)
pmapcAlmVthLas1HighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmVthLas1HighAla.setStatus("current")
_PmapcAlmVtecLas1LowAla_Type = EkiOnOff
_PmapcAlmVtecLas1LowAla_Object = MibScalar
pmapcAlmVtecLas1LowAla = _PmapcAlmVtecLas1LowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 2, 2, 17, 5),
    _PmapcAlmVtecLas1LowAla_Type()
)
pmapcAlmVtecLas1LowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmVtecLas1LowAla.setStatus("current")
_PmapcAlmVtecLas1HighAla_Type = EkiOnOff
_PmapcAlmVtecLas1HighAla_Object = MibScalar
pmapcAlmVtecLas1HighAla = _PmapcAlmVtecLas1HighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 2, 2, 17, 6),
    _PmapcAlmVtecLas1HighAla_Type()
)
pmapcAlmVtecLas1HighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmVtecLas1HighAla.setStatus("current")
_PmapcAlmILas1LowAla_Type = EkiOnOff
_PmapcAlmILas1LowAla_Object = MibScalar
pmapcAlmILas1LowAla = _PmapcAlmILas1LowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 2, 2, 17, 7),
    _PmapcAlmILas1LowAla_Type()
)
pmapcAlmILas1LowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmILas1LowAla.setStatus("current")
_PmapcAlmILas1HighAla_Type = EkiOnOff
_PmapcAlmILas1HighAla_Object = MibScalar
pmapcAlmILas1HighAla = _PmapcAlmILas1HighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 2, 2, 17, 8),
    _PmapcAlmILas1HighAla_Type()
)
pmapcAlmILas1HighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmILas1HighAla.setStatus("current")
_PmapcAlmClientCrit_ObjectIdentity = ObjectIdentity
pmapcAlmClientCrit = _PmapcAlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 2, 3)
)
_PmapcAlmsynthAlmLaser1_ObjectIdentity = ObjectIdentity
pmapcAlmsynthAlmLaser1 = _PmapcAlmsynthAlmLaser1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 2, 3, 8)
)
_PmapcAlmLas1InitNotCompl_Type = EkiOnOff
_PmapcAlmLas1InitNotCompl_Object = MibScalar
pmapcAlmLas1InitNotCompl = _PmapcAlmLas1InitNotCompl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 2, 3, 8, 2),
    _PmapcAlmLas1InitNotCompl_Type()
)
pmapcAlmLas1InitNotCompl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmLas1InitNotCompl.setStatus("current")
_PmapcAlmLas1HwFailAcc_Type = EkiOnOff
_PmapcAlmLas1HwFailAcc_Object = MibScalar
pmapcAlmLas1HwFailAcc = _PmapcAlmLas1HwFailAcc_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 2, 3, 8, 4),
    _PmapcAlmLas1HwFailAcc_Type()
)
pmapcAlmLas1HwFailAcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmLas1HwFailAcc.setStatus("current")
_PmapcAlmLas1LocalOos_Type = EkiOnOff
_PmapcAlmLas1LocalOos_Object = MibScalar
pmapcAlmLas1LocalOos = _PmapcAlmLas1LocalOos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 2, 3, 8, 6),
    _PmapcAlmLas1LocalOos_Type()
)
pmapcAlmLas1LocalOos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmLas1LocalOos.setStatus("current")
_PmapcAlmLas1MeasWng_Type = EkiOnOff
_PmapcAlmLas1MeasWng_Object = MibScalar
pmapcAlmLas1MeasWng = _PmapcAlmLas1MeasWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 2, 3, 8, 9),
    _PmapcAlmLas1MeasWng_Type()
)
pmapcAlmLas1MeasWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmLas1MeasWng.setStatus("current")
_PmapcAlmLas1MeasAlm_Type = EkiOnOff
_PmapcAlmLas1MeasAlm_Object = MibScalar
pmapcAlmLas1MeasAlm = _PmapcAlmLas1MeasAlm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 2, 3, 8, 10),
    _PmapcAlmLas1MeasAlm_Type()
)
pmapcAlmLas1MeasAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmLas1MeasAlm.setStatus("current")
_PmapcAlmLas1FailAcc_Type = EkiOnOff
_PmapcAlmLas1FailAcc_Object = MibScalar
pmapcAlmLas1FailAcc = _PmapcAlmLas1FailAcc_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 2, 3, 8, 12),
    _PmapcAlmLas1FailAcc_Type()
)
pmapcAlmLas1FailAcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmLas1FailAcc.setStatus("current")
_PmapcAlmsynthAlmLaser2_ObjectIdentity = ObjectIdentity
pmapcAlmsynthAlmLaser2 = _PmapcAlmsynthAlmLaser2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 2, 3, 9)
)
_PmapcAlmLas2InitNotCompl_Type = EkiOnOff
_PmapcAlmLas2InitNotCompl_Object = MibScalar
pmapcAlmLas2InitNotCompl = _PmapcAlmLas2InitNotCompl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 2, 3, 9, 2),
    _PmapcAlmLas2InitNotCompl_Type()
)
pmapcAlmLas2InitNotCompl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmLas2InitNotCompl.setStatus("current")
_PmapcAlmLas2HwFailAcc_Type = EkiOnOff
_PmapcAlmLas2HwFailAcc_Object = MibScalar
pmapcAlmLas2HwFailAcc = _PmapcAlmLas2HwFailAcc_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 2, 3, 9, 4),
    _PmapcAlmLas2HwFailAcc_Type()
)
pmapcAlmLas2HwFailAcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmLas2HwFailAcc.setStatus("current")
_PmapcAlmLas2LocalOos_Type = EkiOnOff
_PmapcAlmLas2LocalOos_Object = MibScalar
pmapcAlmLas2LocalOos = _PmapcAlmLas2LocalOos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 2, 3, 9, 6),
    _PmapcAlmLas2LocalOos_Type()
)
pmapcAlmLas2LocalOos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmLas2LocalOos.setStatus("current")
_PmapcAlmLas2MeasWng_Type = EkiOnOff
_PmapcAlmLas2MeasWng_Object = MibScalar
pmapcAlmLas2MeasWng = _PmapcAlmLas2MeasWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 2, 3, 9, 9),
    _PmapcAlmLas2MeasWng_Type()
)
pmapcAlmLas2MeasWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmLas2MeasWng.setStatus("current")
_PmapcAlmLas2MeasAlm_Type = EkiOnOff
_PmapcAlmLas2MeasAlm_Object = MibScalar
pmapcAlmLas2MeasAlm = _PmapcAlmLas2MeasAlm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 2, 3, 9, 10),
    _PmapcAlmLas2MeasAlm_Type()
)
pmapcAlmLas2MeasAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmLas2MeasAlm.setStatus("current")
_PmapcAlmLas2FailAcc_Type = EkiOnOff
_PmapcAlmLas2FailAcc_Object = MibScalar
pmapcAlmLas2FailAcc = _PmapcAlmLas2FailAcc_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 2, 3, 9, 12),
    _PmapcAlmLas2FailAcc_Type()
)
pmapcAlmLas2FailAcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmLas2FailAcc.setStatus("current")
_PmapcAlmLine_ObjectIdentity = ObjectIdentity
pmapcAlmLine = _PmapcAlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 3)
)
_PmapcAlmLineNurg_ObjectIdentity = ObjectIdentity
pmapcAlmLineNurg = _PmapcAlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 3, 1)
)
_PmapcAlmlaser2MeasWng_ObjectIdentity = ObjectIdentity
pmapcAlmlaser2MeasWng = _PmapcAlmlaser2MeasWng_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 3, 1, 26)
)
_PmapcAlmPwrLas2LowWng_Type = EkiOnOff
_PmapcAlmPwrLas2LowWng_Object = MibScalar
pmapcAlmPwrLas2LowWng = _PmapcAlmPwrLas2LowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 3, 1, 26, 1),
    _PmapcAlmPwrLas2LowWng_Type()
)
pmapcAlmPwrLas2LowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmPwrLas2LowWng.setStatus("current")
_PmapcAlmPwrLas2HighWng_Type = EkiOnOff
_PmapcAlmPwrLas2HighWng_Object = MibScalar
pmapcAlmPwrLas2HighWng = _PmapcAlmPwrLas2HighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 3, 1, 26, 2),
    _PmapcAlmPwrLas2HighWng_Type()
)
pmapcAlmPwrLas2HighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmPwrLas2HighWng.setStatus("current")
_PmapcAlmVthLas2LowWng_Type = EkiOnOff
_PmapcAlmVthLas2LowWng_Object = MibScalar
pmapcAlmVthLas2LowWng = _PmapcAlmVthLas2LowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 3, 1, 26, 3),
    _PmapcAlmVthLas2LowWng_Type()
)
pmapcAlmVthLas2LowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmVthLas2LowWng.setStatus("current")
_PmapcAlmVthLas2HighWng_Type = EkiOnOff
_PmapcAlmVthLas2HighWng_Object = MibScalar
pmapcAlmVthLas2HighWng = _PmapcAlmVthLas2HighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 3, 1, 26, 4),
    _PmapcAlmVthLas2HighWng_Type()
)
pmapcAlmVthLas2HighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmVthLas2HighWng.setStatus("current")
_PmapcAlmVtecLas2LowWng_Type = EkiOnOff
_PmapcAlmVtecLas2LowWng_Object = MibScalar
pmapcAlmVtecLas2LowWng = _PmapcAlmVtecLas2LowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 3, 1, 26, 5),
    _PmapcAlmVtecLas2LowWng_Type()
)
pmapcAlmVtecLas2LowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmVtecLas2LowWng.setStatus("current")
_PmapcAlmVtecLas2HighWng_Type = EkiOnOff
_PmapcAlmVtecLas2HighWng_Object = MibScalar
pmapcAlmVtecLas2HighWng = _PmapcAlmVtecLas2HighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 3, 1, 26, 6),
    _PmapcAlmVtecLas2HighWng_Type()
)
pmapcAlmVtecLas2HighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmVtecLas2HighWng.setStatus("current")
_PmapcAlmILas2LowWng_Type = EkiOnOff
_PmapcAlmILas2LowWng_Object = MibScalar
pmapcAlmILas2LowWng = _PmapcAlmILas2LowWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 3, 1, 26, 7),
    _PmapcAlmILas2LowWng_Type()
)
pmapcAlmILas2LowWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmILas2LowWng.setStatus("current")
_PmapcAlmILas2HighWng_Type = EkiOnOff
_PmapcAlmILas2HighWng_Object = MibScalar
pmapcAlmILas2HighWng = _PmapcAlmILas2HighWng_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 3, 1, 26, 8),
    _PmapcAlmILas2HighWng_Type()
)
pmapcAlmILas2HighWng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmILas2HighWng.setStatus("current")
_PmapcAlmLineUrg_ObjectIdentity = ObjectIdentity
pmapcAlmLineUrg = _PmapcAlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 3, 2)
)
_PmapcAlmlaser2Alm_ObjectIdentity = ObjectIdentity
pmapcAlmlaser2Alm = _PmapcAlmlaser2Alm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 3, 2, 24)
)
_PmapcAlmLas2Fail_Type = EkiOnOff
_PmapcAlmLas2Fail_Object = MibScalar
pmapcAlmLas2Fail = _PmapcAlmLas2Fail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 3, 2, 24, 1),
    _PmapcAlmLas2Fail_Type()
)
pmapcAlmLas2Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmLas2Fail.setStatus("current")
_PmapcAlmLas2TecFail_Type = EkiOnOff
_PmapcAlmLas2TecFail_Object = MibScalar
pmapcAlmLas2TecFail = _PmapcAlmLas2TecFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 3, 2, 24, 2),
    _PmapcAlmLas2TecFail_Type()
)
pmapcAlmLas2TecFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmLas2TecFail.setStatus("current")
_PmapcAlmlaser2MeasAla_ObjectIdentity = ObjectIdentity
pmapcAlmlaser2MeasAla = _PmapcAlmlaser2MeasAla_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 3, 2, 25)
)
_PmapcAlmPwrLas2LowAla_Type = EkiOnOff
_PmapcAlmPwrLas2LowAla_Object = MibScalar
pmapcAlmPwrLas2LowAla = _PmapcAlmPwrLas2LowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 3, 2, 25, 1),
    _PmapcAlmPwrLas2LowAla_Type()
)
pmapcAlmPwrLas2LowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmPwrLas2LowAla.setStatus("current")
_PmapcAlmPwrLas2HighAla_Type = EkiOnOff
_PmapcAlmPwrLas2HighAla_Object = MibScalar
pmapcAlmPwrLas2HighAla = _PmapcAlmPwrLas2HighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 3, 2, 25, 2),
    _PmapcAlmPwrLas2HighAla_Type()
)
pmapcAlmPwrLas2HighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmPwrLas2HighAla.setStatus("current")
_PmapcAlmVthLas2LowAla_Type = EkiOnOff
_PmapcAlmVthLas2LowAla_Object = MibScalar
pmapcAlmVthLas2LowAla = _PmapcAlmVthLas2LowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 3, 2, 25, 3),
    _PmapcAlmVthLas2LowAla_Type()
)
pmapcAlmVthLas2LowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmVthLas2LowAla.setStatus("current")
_PmapcAlmVthLas2HighAla_Type = EkiOnOff
_PmapcAlmVthLas2HighAla_Object = MibScalar
pmapcAlmVthLas2HighAla = _PmapcAlmVthLas2HighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 3, 2, 25, 4),
    _PmapcAlmVthLas2HighAla_Type()
)
pmapcAlmVthLas2HighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmVthLas2HighAla.setStatus("current")
_PmapcAlmVtecLas2LowAla_Type = EkiOnOff
_PmapcAlmVtecLas2LowAla_Object = MibScalar
pmapcAlmVtecLas2LowAla = _PmapcAlmVtecLas2LowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 3, 2, 25, 5),
    _PmapcAlmVtecLas2LowAla_Type()
)
pmapcAlmVtecLas2LowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmVtecLas2LowAla.setStatus("current")
_PmapcAlmVtecLas2HighAla_Type = EkiOnOff
_PmapcAlmVtecLas2HighAla_Object = MibScalar
pmapcAlmVtecLas2HighAla = _PmapcAlmVtecLas2HighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 3, 2, 25, 6),
    _PmapcAlmVtecLas2HighAla_Type()
)
pmapcAlmVtecLas2HighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmVtecLas2HighAla.setStatus("current")
_PmapcAlmILas2LowAla_Type = EkiOnOff
_PmapcAlmILas2LowAla_Object = MibScalar
pmapcAlmILas2LowAla = _PmapcAlmILas2LowAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 3, 2, 25, 7),
    _PmapcAlmILas2LowAla_Type()
)
pmapcAlmILas2LowAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmILas2LowAla.setStatus("current")
_PmapcAlmILas2HighAla_Type = EkiOnOff
_PmapcAlmILas2HighAla_Object = MibScalar
pmapcAlmILas2HighAla = _PmapcAlmILas2HighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 3, 2, 25, 8),
    _PmapcAlmILas2HighAla_Type()
)
pmapcAlmILas2HighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcAlmILas2HighAla.setStatus("current")
_PmapcAlmLineCrit_ObjectIdentity = ObjectIdentity
pmapcAlmLineCrit = _PmapcAlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 2, 3, 3)
)
_Pmapcmeasures_ObjectIdentity = ObjectIdentity
pmapcmeasures = _Pmapcmeasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 3)
)
_PmapcMesrOther_ObjectIdentity = ObjectIdentity
pmapcMesrOther = _PmapcMesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 3, 1)
)


class _PmapcMesrmodulePowerIn_Type(Unsigned32):
    """Custom type pmapcMesrmodulePowerIn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmapcMesrmodulePowerIn_Type.__name__ = "Unsigned32"
_PmapcMesrmodulePowerIn_Object = MibScalar
pmapcMesrmodulePowerIn = _PmapcMesrmodulePowerIn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 3, 1, 64),
    _PmapcMesrmodulePowerIn_Type()
)
pmapcMesrmodulePowerIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcMesrmodulePowerIn.setStatus("current")


class _PmapcMesrmoduleVPowerOut_Type(Unsigned32):
    """Custom type pmapcMesrmoduleVPowerOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmapcMesrmoduleVPowerOut_Type.__name__ = "Unsigned32"
_PmapcMesrmoduleVPowerOut_Object = MibScalar
pmapcMesrmoduleVPowerOut = _PmapcMesrmoduleVPowerOut_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 3, 1, 65),
    _PmapcMesrmoduleVPowerOut_Type()
)
pmapcMesrmoduleVPowerOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcMesrmoduleVPowerOut.setStatus("current")


class _PmapcMesrmoduleEamAtt_Type(Unsigned32):
    """Custom type pmapcMesrmoduleEamAtt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmapcMesrmoduleEamAtt_Type.__name__ = "Unsigned32"
_PmapcMesrmoduleEamAtt_Object = MibScalar
pmapcMesrmoduleEamAtt = _PmapcMesrmoduleEamAtt_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 3, 1, 66),
    _PmapcMesrmoduleEamAtt_Type()
)
pmapcMesrmoduleEamAtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcMesrmoduleEamAtt.setStatus("current")


class _PmapcMesrmoduleTemp_Type(Unsigned32):
    """Custom type pmapcMesrmoduleTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmapcMesrmoduleTemp_Type.__name__ = "Unsigned32"
_PmapcMesrmoduleTemp_Object = MibScalar
pmapcMesrmoduleTemp = _PmapcMesrmoduleTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 3, 1, 67),
    _PmapcMesrmoduleTemp_Type()
)
pmapcMesrmoduleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcMesrmoduleTemp.setStatus("current")


class _PmapcMesrmodule33v_Type(Unsigned32):
    """Custom type pmapcMesrmodule33v based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmapcMesrmodule33v_Type.__name__ = "Unsigned32"
_PmapcMesrmodule33v_Object = MibScalar
pmapcMesrmodule33v = _PmapcMesrmodule33v_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 3, 1, 68),
    _PmapcMesrmodule33v_Type()
)
pmapcMesrmodule33v.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcMesrmodule33v.setStatus("current")
_PmapcMesrClient_ObjectIdentity = ObjectIdentity
pmapcMesrClient = _PmapcMesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 3, 2)
)


class _PmapcMesrpowerLas1_Type(Unsigned32):
    """Custom type pmapcMesrpowerLas1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmapcMesrpowerLas1_Type.__name__ = "Unsigned32"
_PmapcMesrpowerLas1_Object = MibScalar
pmapcMesrpowerLas1 = _PmapcMesrpowerLas1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 3, 2, 16),
    _PmapcMesrpowerLas1_Type()
)
pmapcMesrpowerLas1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcMesrpowerLas1.setStatus("current")


class _PmapcMesrvthLas1_Type(Unsigned32):
    """Custom type pmapcMesrvthLas1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmapcMesrvthLas1_Type.__name__ = "Unsigned32"
_PmapcMesrvthLas1_Object = MibScalar
pmapcMesrvthLas1 = _PmapcMesrvthLas1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 3, 2, 17),
    _PmapcMesrvthLas1_Type()
)
pmapcMesrvthLas1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcMesrvthLas1.setStatus("current")


class _PmapcMesrvtecLas1_Type(Unsigned32):
    """Custom type pmapcMesrvtecLas1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmapcMesrvtecLas1_Type.__name__ = "Unsigned32"
_PmapcMesrvtecLas1_Object = MibScalar
pmapcMesrvtecLas1 = _PmapcMesrvtecLas1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 3, 2, 18),
    _PmapcMesrvtecLas1_Type()
)
pmapcMesrvtecLas1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcMesrvtecLas1.setStatus("current")


class _PmapcMesriLas1_Type(Unsigned32):
    """Custom type pmapcMesriLas1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmapcMesriLas1_Type.__name__ = "Unsigned32"
_PmapcMesriLas1_Object = MibScalar
pmapcMesriLas1 = _PmapcMesriLas1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 3, 2, 19),
    _PmapcMesriLas1_Type()
)
pmapcMesriLas1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcMesriLas1.setStatus("current")
_PmapcMesrLine_ObjectIdentity = ObjectIdentity
pmapcMesrLine = _PmapcMesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 3, 3)
)


class _PmapcMesrpowerLas2_Type(Unsigned32):
    """Custom type pmapcMesrpowerLas2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmapcMesrpowerLas2_Type.__name__ = "Unsigned32"
_PmapcMesrpowerLas2_Object = MibScalar
pmapcMesrpowerLas2 = _PmapcMesrpowerLas2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 3, 3, 24),
    _PmapcMesrpowerLas2_Type()
)
pmapcMesrpowerLas2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcMesrpowerLas2.setStatus("current")


class _PmapcMesrvthLas2_Type(Unsigned32):
    """Custom type pmapcMesrvthLas2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmapcMesrvthLas2_Type.__name__ = "Unsigned32"
_PmapcMesrvthLas2_Object = MibScalar
pmapcMesrvthLas2 = _PmapcMesrvthLas2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 3, 3, 25),
    _PmapcMesrvthLas2_Type()
)
pmapcMesrvthLas2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcMesrvthLas2.setStatus("current")


class _PmapcMesrvtecLas2_Type(Unsigned32):
    """Custom type pmapcMesrvtecLas2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmapcMesrvtecLas2_Type.__name__ = "Unsigned32"
_PmapcMesrvtecLas2_Object = MibScalar
pmapcMesrvtecLas2 = _PmapcMesrvtecLas2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 3, 3, 26),
    _PmapcMesrvtecLas2_Type()
)
pmapcMesrvtecLas2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcMesrvtecLas2.setStatus("current")


class _PmapcMesriLas2_Type(Unsigned32):
    """Custom type pmapcMesriLas2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmapcMesriLas2_Type.__name__ = "Unsigned32"
_PmapcMesriLas2_Object = MibScalar
pmapcMesriLas2 = _PmapcMesriLas2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 3, 3, 27),
    _PmapcMesriLas2_Type()
)
pmapcMesriLas2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcMesriLas2.setStatus("current")
_PmapccontrolsWrite_ObjectIdentity = ObjectIdentity
pmapccontrolsWrite = _PmapccontrolsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 6)
)
_PmapcCtrlOther_ObjectIdentity = ObjectIdentity
pmapcCtrlOther = _PmapcCtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 6, 1)
)
_PmapcCtrlsynth0_ObjectIdentity = ObjectIdentity
pmapcCtrlsynth0 = _PmapcCtrlsynth0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 6, 1, 0)
)
_PmapcCtrlConfLoad_Type = EkiOnOff
_PmapcCtrlConfLoad_Object = MibScalar
pmapcCtrlConfLoad = _PmapcCtrlConfLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 6, 1, 0, 1),
    _PmapcCtrlConfLoad_Type()
)
pmapcCtrlConfLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmapcCtrlConfLoad.setStatus("current")
_PmapcCtrlConfFlash_Type = EkiOnOff
_PmapcCtrlConfFlash_Object = MibScalar
pmapcCtrlConfFlash = _PmapcCtrlConfFlash_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 6, 1, 0, 9),
    _PmapcCtrlConfFlash_Type()
)
pmapcCtrlConfFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmapcCtrlConfFlash.setStatus("current")
_PmapcCtrlConfClear_Type = EkiOnOff
_PmapcCtrlConfClear_Object = MibScalar
pmapcCtrlConfClear = _PmapcCtrlConfClear_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 6, 1, 0, 13),
    _PmapcCtrlConfClear_Type()
)
pmapcCtrlConfClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmapcCtrlConfClear.setStatus("current")
_PmapcCtrlsynth4_ObjectIdentity = ObjectIdentity
pmapcCtrlsynth4 = _PmapcCtrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 6, 1, 4)
)
_PmapcCtrlCorrelatOn_Type = EkiOnOff
_PmapcCtrlCorrelatOn_Object = MibScalar
pmapcCtrlCorrelatOn = _PmapcCtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 6, 1, 4, 1),
    _PmapcCtrlCorrelatOn_Type()
)
pmapcCtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmapcCtrlCorrelatOn.setStatus("current")
_PmapcCtrlCorrelatOff_Type = EkiOnOff
_PmapcCtrlCorrelatOff_Object = MibScalar
pmapcCtrlCorrelatOff = _PmapcCtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 6, 1, 4, 2),
    _PmapcCtrlCorrelatOff_Type()
)
pmapcCtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmapcCtrlCorrelatOff.setStatus("current")
_PmapcCtrlswMgnt_ObjectIdentity = ObjectIdentity
pmapcCtrlswMgnt = _PmapcCtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 6, 1, 5)
)
_PmapcCtrlColdReset_Type = EkiOnOff
_PmapcCtrlColdReset_Object = MibScalar
pmapcCtrlColdReset = _PmapcCtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 6, 1, 5, 2),
    _PmapcCtrlColdReset_Type()
)
pmapcCtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmapcCtrlColdReset.setStatus("current")
_PmapcCtrlWarmReset_Type = EkiOnOff
_PmapcCtrlWarmReset_Object = MibScalar
pmapcCtrlWarmReset = _PmapcCtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 6, 1, 5, 3),
    _PmapcCtrlWarmReset_Type()
)
pmapcCtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmapcCtrlWarmReset.setStatus("current")
_PmapcCtrlledTest_ObjectIdentity = ObjectIdentity
pmapcCtrlledTest = _PmapcCtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 6, 1, 64)
)
_PmapcCtrlGreenLed_Type = EkiOnOff
_PmapcCtrlGreenLed_Object = MibScalar
pmapcCtrlGreenLed = _PmapcCtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 6, 1, 64, 1),
    _PmapcCtrlGreenLed_Type()
)
pmapcCtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmapcCtrlGreenLed.setStatus("current")
_PmapcCtrlRedLed_Type = EkiOnOff
_PmapcCtrlRedLed_Object = MibScalar
pmapcCtrlRedLed = _PmapcCtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 6, 1, 64, 2),
    _PmapcCtrlRedLed_Type()
)
pmapcCtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmapcCtrlRedLed.setStatus("current")
_PmapcCtrlLedOff_Type = EkiOnOff
_PmapcCtrlLedOff_Object = MibScalar
pmapcCtrlLedOff = _PmapcCtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 6, 1, 64, 3),
    _PmapcCtrlLedOff_Type()
)
pmapcCtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmapcCtrlLedOff.setStatus("current")
_PmapcCtrlClient_ObjectIdentity = ObjectIdentity
pmapcCtrlClient = _PmapcCtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 6, 2)
)
_PmapcCtrllaser1Shutdown_ObjectIdentity = ObjectIdentity
pmapcCtrllaser1Shutdown = _PmapcCtrllaser1Shutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 6, 2, 16)
)
_PmapcCtrlLaser1Shutdown_Type = EkiOnOff
_PmapcCtrlLaser1Shutdown_Object = MibScalar
pmapcCtrlLaser1Shutdown = _PmapcCtrlLaser1Shutdown_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 6, 2, 16, 1),
    _PmapcCtrlLaser1Shutdown_Type()
)
pmapcCtrlLaser1Shutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmapcCtrlLaser1Shutdown.setStatus("current")
_PmapcCtrllaser1Oos_ObjectIdentity = ObjectIdentity
pmapcCtrllaser1Oos = _PmapcCtrllaser1Oos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 6, 2, 18)
)
_PmapcCtrlLaser1OosMode_Type = EkiOnOff
_PmapcCtrlLaser1OosMode_Object = MibScalar
pmapcCtrlLaser1OosMode = _PmapcCtrlLaser1OosMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 6, 2, 18, 1),
    _PmapcCtrlLaser1OosMode_Type()
)
pmapcCtrlLaser1OosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmapcCtrlLaser1OosMode.setStatus("current")
_PmapcCtrlLine_ObjectIdentity = ObjectIdentity
pmapcCtrlLine = _PmapcCtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 6, 3)
)
_PmapcCtrllaser2Shutdown_ObjectIdentity = ObjectIdentity
pmapcCtrllaser2Shutdown = _PmapcCtrllaser2Shutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 6, 3, 17)
)
_PmapcCtrlLaser2Shutdown_Type = EkiOnOff
_PmapcCtrlLaser2Shutdown_Object = MibScalar
pmapcCtrlLaser2Shutdown = _PmapcCtrlLaser2Shutdown_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 6, 3, 17, 1),
    _PmapcCtrlLaser2Shutdown_Type()
)
pmapcCtrlLaser2Shutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmapcCtrlLaser2Shutdown.setStatus("current")
_PmapcCtrllaser2Oos_ObjectIdentity = ObjectIdentity
pmapcCtrllaser2Oos = _PmapcCtrllaser2Oos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 6, 3, 19)
)
_PmapcCtrlLaser2OosMode_Type = EkiOnOff
_PmapcCtrlLaser2OosMode_Object = MibScalar
pmapcCtrlLaser2OosMode = _PmapcCtrlLaser2OosMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 6, 3, 19, 1),
    _PmapcCtrlLaser2OosMode_Type()
)
pmapcCtrlLaser2OosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmapcCtrlLaser2OosMode.setStatus("current")


class _PmapcCtrlmoduleOutputPwrSetting_Type(Unsigned32):
    """Custom type pmapcCtrlmoduleOutputPwrSetting based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmapcCtrlmoduleOutputPwrSetting_Type.__name__ = "Unsigned32"
_PmapcCtrlmoduleOutputPwrSetting_Object = MibScalar
pmapcCtrlmoduleOutputPwrSetting = _PmapcCtrlmoduleOutputPwrSetting_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 6, 3, 65),
    _PmapcCtrlmoduleOutputPwrSetting_Type()
)
pmapcCtrlmoduleOutputPwrSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmapcCtrlmoduleOutputPwrSetting.setStatus("current")


class _PmapcCtrlmoduleInputPwrSetting_Type(Unsigned32):
    """Custom type pmapcCtrlmoduleInputPwrSetting based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmapcCtrlmoduleInputPwrSetting_Type.__name__ = "Unsigned32"
_PmapcCtrlmoduleInputPwrSetting_Object = MibScalar
pmapcCtrlmoduleInputPwrSetting = _PmapcCtrlmoduleInputPwrSetting_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 6, 3, 66),
    _PmapcCtrlmoduleInputPwrSetting_Type()
)
pmapcCtrlmoduleInputPwrSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmapcCtrlmoduleInputPwrSetting.setStatus("current")
_Pmapcri_ObjectIdentity = ObjectIdentity
pmapcri = _Pmapcri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 7)
)
_PmapcriTable_ObjectIdentity = ObjectIdentity
pmapcriTable = _PmapcriTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 7, 1)
)
_PmapcRinvLaser1Table_Object = MibTable
pmapcRinvLaser1Table = _PmapcRinvLaser1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 7, 1, 1)
)
if mibBuilder.loadTexts:
    pmapcRinvLaser1Table.setStatus("current")
_PmapcRinvLaser1Entry_Object = MibTableRow
pmapcRinvLaser1Entry = _PmapcRinvLaser1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 7, 1, 1, 1)
)
pmapcRinvLaser1Entry.setIndexNames(
    (0, "EKINOPS-Pmapc-MIB", "pmapcRinvLaser1Index"),
)
if mibBuilder.loadTexts:
    pmapcRinvLaser1Entry.setStatus("current")


class _PmapcRinvLaser1Index_Type(Integer32):
    """Custom type pmapcRinvLaser1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PmapcRinvLaser1Index_Type.__name__ = "Integer32"
_PmapcRinvLaser1Index_Object = MibTableColumn
pmapcRinvLaser1Index = _PmapcRinvLaser1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 7, 1, 1, 1, 1),
    _PmapcRinvLaser1Index_Type()
)
pmapcRinvLaser1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcRinvLaser1Index.setStatus("current")
_PmapcRinvLaser1_Type = DisplayString
_PmapcRinvLaser1_Object = MibTableColumn
pmapcRinvLaser1 = _PmapcRinvLaser1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 7, 1, 1, 1, 2),
    _PmapcRinvLaser1_Type()
)
pmapcRinvLaser1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcRinvLaser1.setStatus("current")
_PmapcRinvLaser2Table_Object = MibTable
pmapcRinvLaser2Table = _PmapcRinvLaser2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pmapcRinvLaser2Table.setStatus("current")
_PmapcRinvLaser2Entry_Object = MibTableRow
pmapcRinvLaser2Entry = _PmapcRinvLaser2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 7, 1, 2, 1)
)
pmapcRinvLaser2Entry.setIndexNames(
    (0, "EKINOPS-Pmapc-MIB", "pmapcRinvLaser2Index"),
)
if mibBuilder.loadTexts:
    pmapcRinvLaser2Entry.setStatus("current")


class _PmapcRinvLaser2Index_Type(Integer32):
    """Custom type pmapcRinvLaser2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PmapcRinvLaser2Index_Type.__name__ = "Integer32"
_PmapcRinvLaser2Index_Object = MibTableColumn
pmapcRinvLaser2Index = _PmapcRinvLaser2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 7, 1, 2, 1, 1),
    _PmapcRinvLaser2Index_Type()
)
pmapcRinvLaser2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcRinvLaser2Index.setStatus("current")
_PmapcRinvLaser2_Type = DisplayString
_PmapcRinvLaser2_Object = MibTableColumn
pmapcRinvLaser2 = _PmapcRinvLaser2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 7, 1, 2, 1, 2),
    _PmapcRinvLaser2_Type()
)
pmapcRinvLaser2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcRinvLaser2.setStatus("current")
_PmapcRinvReloadInventory_Type = EkiOnOff
_PmapcRinvReloadInventory_Object = MibScalar
pmapcRinvReloadInventory = _PmapcRinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 7, 2),
    _PmapcRinvReloadInventory_Type()
)
pmapcRinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmapcRinvReloadInventory.setStatus("current")
_PmapcRinvHwPlatform_Type = DisplayString
_PmapcRinvHwPlatform_Object = MibScalar
pmapcRinvHwPlatform = _PmapcRinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 7, 3),
    _PmapcRinvHwPlatform_Type()
)
pmapcRinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcRinvHwPlatform.setStatus("current")
_PmapcRinvModulePlatform_Type = DisplayString
_PmapcRinvModulePlatform_Object = MibScalar
pmapcRinvModulePlatform = _PmapcRinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 7, 4),
    _PmapcRinvModulePlatform_Type()
)
pmapcRinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcRinvModulePlatform.setStatus("current")
_PmapcRinvSwPlatform_Type = DisplayString
_PmapcRinvSwPlatform_Object = MibScalar
pmapcRinvSwPlatform = _PmapcRinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 7, 5),
    _PmapcRinvSwPlatform_Type()
)
pmapcRinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcRinvSwPlatform.setStatus("current")
_PmapcConfig_ObjectIdentity = ObjectIdentity
pmapcConfig = _PmapcConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 9)
)
_PmapcCfgLsd_ObjectIdentity = ObjectIdentity
pmapcCfgLsd = _PmapcCfgLsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 9, 1)
)
_PmapctablecomaLsd_ObjectIdentity = ObjectIdentity
pmapctablecomaLsd = _PmapctablecomaLsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 9, 1, 1)
)
_PmapcCfgStartUp_ObjectIdentity = ObjectIdentity
pmapcCfgStartUp = _PmapcCfgStartUp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 9, 2)
)
_PmapctablecomaStartup_ObjectIdentity = ObjectIdentity
pmapctablecomaStartup = _PmapctablecomaStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 9, 2, 1)
)


class _PmapcCfglaser1Oos_Type(Unsigned32):
    """Custom type pmapcCfglaser1Oos based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmapcCfglaser1Oos_Type.__name__ = "Unsigned32"
_PmapcCfglaser1Oos_Object = MibScalar
pmapcCfglaser1Oos = _PmapcCfglaser1Oos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 9, 2, 1, 2),
    _PmapcCfglaser1Oos_Type()
)
pmapcCfglaser1Oos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmapcCfglaser1Oos.setStatus("current")
_PmapctablecombStartup_ObjectIdentity = ObjectIdentity
pmapctablecombStartup = _PmapctablecombStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 9, 2, 2)
)


class _PmapcCfglaser2Oos_Type(Unsigned32):
    """Custom type pmapcCfglaser2Oos based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmapcCfglaser2Oos_Type.__name__ = "Unsigned32"
_PmapcCfglaser2Oos_Object = MibScalar
pmapcCfglaser2Oos = _PmapcCfglaser2Oos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 9, 2, 2, 2),
    _PmapcCfglaser2Oos_Type()
)
pmapcCfglaser2Oos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmapcCfglaser2Oos.setStatus("current")


class _PmapcCfgmoduleOutputPwrSetting_Type(Unsigned32):
    """Custom type pmapcCfgmoduleOutputPwrSetting based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmapcCfgmoduleOutputPwrSetting_Type.__name__ = "Unsigned32"
_PmapcCfgmoduleOutputPwrSetting_Object = MibScalar
pmapcCfgmoduleOutputPwrSetting = _PmapcCfgmoduleOutputPwrSetting_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 9, 2, 2, 10),
    _PmapcCfgmoduleOutputPwrSetting_Type()
)
pmapcCfgmoduleOutputPwrSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmapcCfgmoduleOutputPwrSetting.setStatus("current")


class _PmapcCfgmoduleInputPwrSetting_Type(Unsigned32):
    """Custom type pmapcCfgmoduleInputPwrSetting based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmapcCfgmoduleInputPwrSetting_Type.__name__ = "Unsigned32"
_PmapcCfgmoduleInputPwrSetting_Object = MibScalar
pmapcCfgmoduleInputPwrSetting = _PmapcCfgmoduleInputPwrSetting_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 9, 2, 2, 11),
    _PmapcCfgmoduleInputPwrSetting_Type()
)
pmapcCfgmoduleInputPwrSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmapcCfgmoduleInputPwrSetting.setStatus("current")
_PmapcCfgLabels_ObjectIdentity = ObjectIdentity
pmapcCfgLabels = _PmapcCfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 9, 3)
)
_PmapcCfgLabelclientTable_Object = MibTable
pmapcCfgLabelclientTable = _PmapcCfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 9, 3, 1)
)
if mibBuilder.loadTexts:
    pmapcCfgLabelclientTable.setStatus("current")
_PmapcCfgLabelclientEntry_Object = MibTableRow
pmapcCfgLabelclientEntry = _PmapcCfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 9, 3, 1, 1)
)
pmapcCfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-Pmapc-MIB", "pmapcCfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pmapcCfgLabelclientEntry.setStatus("current")


class _PmapcCfgLabelclientIndex_Type(Integer32):
    """Custom type pmapcCfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmapcCfgLabelclientIndex_Type.__name__ = "Integer32"
_PmapcCfgLabelclientIndex_Object = MibTableColumn
pmapcCfgLabelclientIndex = _PmapcCfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 9, 3, 1, 1, 1),
    _PmapcCfgLabelclientIndex_Type()
)
pmapcCfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcCfgLabelclientIndex.setStatus("current")


class _PmapcCfgLabelclientPortn_Type(DisplayString):
    """Custom type pmapcCfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PmapcCfgLabelclientPortn_Type.__name__ = "DisplayString"
_PmapcCfgLabelclientPortn_Object = MibTableColumn
pmapcCfgLabelclientPortn = _PmapcCfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 9, 3, 1, 1, 3),
    _PmapcCfgLabelclientPortn_Type()
)
pmapcCfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmapcCfgLabelclientPortn.setStatus("current")
_PmapcCfgLabellineTable_Object = MibTable
pmapcCfgLabellineTable = _PmapcCfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 9, 3, 2)
)
if mibBuilder.loadTexts:
    pmapcCfgLabellineTable.setStatus("current")
_PmapcCfgLabellineEntry_Object = MibTableRow
pmapcCfgLabellineEntry = _PmapcCfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 9, 3, 2, 1)
)
pmapcCfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-Pmapc-MIB", "pmapcCfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pmapcCfgLabellineEntry.setStatus("current")


class _PmapcCfgLabellineIndex_Type(Integer32):
    """Custom type pmapcCfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmapcCfgLabellineIndex_Type.__name__ = "Integer32"
_PmapcCfgLabellineIndex_Object = MibTableColumn
pmapcCfgLabellineIndex = _PmapcCfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 9, 3, 2, 1, 1),
    _PmapcCfgLabellineIndex_Type()
)
pmapcCfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapcCfgLabellineIndex.setStatus("current")


class _PmapcCfgLabellinePortn_Type(DisplayString):
    """Custom type pmapcCfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PmapcCfgLabellinePortn_Type.__name__ = "DisplayString"
_PmapcCfgLabellinePortn_Object = MibTableColumn
pmapcCfgLabellinePortn = _PmapcCfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 9, 3, 2, 1, 3),
    _PmapcCfgLabellinePortn_Type()
)
pmapcCfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmapcCfgLabellinePortn.setStatus("current")
_PmapcCfgWriteConfiguration_Type = EkiOnOff
_PmapcCfgWriteConfiguration_Object = MibScalar
pmapcCfgWriteConfiguration = _PmapcCfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 9, 257),
    _PmapcCfgWriteConfiguration_Type()
)
pmapcCfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmapcCfgWriteConfiguration.setStatus("current")
_Pmapctraps_ObjectIdentity = ObjectIdentity
pmapctraps = _Pmapctraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 42, 10)
)


class _PmapctrapPortNumber_Type(Integer32):
    """Custom type pmapctrapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_PmapctrapPortNumber_Type.__name__ = "Integer32"
_PmapctrapPortNumber_Object = MibScalar
pmapctrapPortNumber = _PmapctrapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 10, 2),
    _PmapctrapPortNumber_Type()
)
pmapctrapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapctrapPortNumber.setStatus("current")


class _PmapctrapLineNumber_Type(Integer32):
    """Custom type pmapctrapLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_PmapctrapLineNumber_Type.__name__ = "Integer32"
_PmapctrapLineNumber_Object = MibScalar
pmapctrapLineNumber = _PmapctrapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 10, 3),
    _PmapctrapLineNumber_Type()
)
pmapctrapLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapctrapLineNumber.setStatus("current")


class _PmapctrapBoardNumber_Type(Integer32):
    """Custom type pmapctrapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_PmapctrapBoardNumber_Type.__name__ = "Integer32"
_PmapctrapBoardNumber_Object = MibScalar
pmapctrapBoardNumber = _PmapctrapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 42, 10, 4),
    _PmapctrapBoardNumber_Type()
)
pmapctrapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmapctrapBoardNumber.setStatus("current")

# Managed Objects groups


# Notification objects

pmapcLas2TrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 42, 10, 30)
)
pmapcLas2TrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pmapc-MIB", "pmapcAlmLas2MeasWng"),
        ("EKINOPS-Pmapc-MIB", "pmapctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmapcLas2TrapNotUrgentGoesOn.setStatus(
        "current"
    )

pmapcLas2TrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 42, 10, 31)
)
pmapcLas2TrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pmapc-MIB", "pmapcAlmLas2MeasWng"),
        ("EKINOPS-Pmapc-MIB", "pmapctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmapcLas2TrapNotUrgentGoesOff.setStatus(
        "current"
    )

pmapcLas2TrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 42, 10, 32)
)
pmapcLas2TrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pmapc-MIB", "pmapcAlmLas2MeasAlm"),
        ("EKINOPS-Pmapc-MIB", "pmapctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmapcLas2TrapUrgentGoesOn.setStatus(
        "current"
    )

pmapcLas2TrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 42, 10, 33)
)
pmapcLas2TrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pmapc-MIB", "pmapcAlmLas2MeasAlm"),
        ("EKINOPS-Pmapc-MIB", "pmapctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmapcLas2TrapUrgentGoesOff.setStatus(
        "current"
    )

pmapcLas2TrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 42, 10, 34)
)
pmapcLas2TrapCritGoesOn.setObjects(
      *(("EKINOPS-Pmapc-MIB", "pmapcAlmLas2FailAcc"),
        ("EKINOPS-Pmapc-MIB", "pmapcAlmLas2HwFailAcc"),
        ("EKINOPS-Pmapc-MIB", "pmapctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmapcLas2TrapCritGoesOn.setStatus(
        "current"
    )

pmapcLas2TrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 42, 10, 35)
)
pmapcLas2TrapCritGoesOff.setObjects(
      *(("EKINOPS-Pmapc-MIB", "pmapcAlmLas2FailAcc"),
        ("EKINOPS-Pmapc-MIB", "pmapcAlmLas2HwFailAcc"),
        ("EKINOPS-Pmapc-MIB", "pmapctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmapcLas2TrapCritGoesOff.setStatus(
        "current"
    )

pmapcLas1TrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 42, 10, 40)
)
pmapcLas1TrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pmapc-MIB", "pmapcAlmLas1MeasWng"),
        ("EKINOPS-Pmapc-MIB", "pmapctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmapcLas1TrapNotUrgentGoesOn.setStatus(
        "current"
    )

pmapcLas1TrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 42, 10, 41)
)
pmapcLas1TrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pmapc-MIB", "pmapcAlmLas1MeasWng"),
        ("EKINOPS-Pmapc-MIB", "pmapctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmapcLas1TrapNotUrgentGoesOff.setStatus(
        "current"
    )

pmapcLas1TrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 42, 10, 42)
)
pmapcLas1TrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pmapc-MIB", "pmapcAlmLas1MeasAlm"),
        ("EKINOPS-Pmapc-MIB", "pmapctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmapcLas1TrapUrgentGoesOn.setStatus(
        "current"
    )

pmapcLas1TrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 42, 10, 43)
)
pmapcLas1TrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pmapc-MIB", "pmapcAlmLas1MeasAlm"),
        ("EKINOPS-Pmapc-MIB", "pmapctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmapcLas1TrapUrgentGoesOff.setStatus(
        "current"
    )

pmapcLas1TrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 42, 10, 44)
)
pmapcLas1TrapCritGoesOn.setObjects(
      *(("EKINOPS-Pmapc-MIB", "pmapcAlmLas1FailAcc"),
        ("EKINOPS-Pmapc-MIB", "pmapcAlmLas1HwFailAcc"),
        ("EKINOPS-Pmapc-MIB", "pmapctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmapcLas1TrapCritGoesOn.setStatus(
        "current"
    )

pmapcLas1TrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 42, 10, 45)
)
pmapcLas1TrapCritGoesOff.setObjects(
      *(("EKINOPS-Pmapc-MIB", "pmapcAlmLas1FailAcc"),
        ("EKINOPS-Pmapc-MIB", "pmapcAlmLas1HwFailAcc"),
        ("EKINOPS-Pmapc-MIB", "pmapctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmapcLas1TrapCritGoesOff.setStatus(
        "current"
    )

pmapcPowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 42, 10, 50)
)
pmapcPowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pmapc-MIB", "pmapcAlmDefFuseB"),
        ("EKINOPS-Pmapc-MIB", "pmapcAlmDefFuseA"),
        ("EKINOPS-Pmapc-MIB", "pmapctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmapcPowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pmapcPowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 42, 10, 51)
)
pmapcPowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pmapc-MIB", "pmapcAlmDefFuseB"),
        ("EKINOPS-Pmapc-MIB", "pmapcAlmDefFuseA"),
        ("EKINOPS-Pmapc-MIB", "pmapctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmapcPowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Pmapc-MIB",
    **{"modulePmapc": modulePmapc,
       "pmapcalarms": pmapcalarms,
       "pmapcAlmOther": pmapcAlmOther,
       "pmapcAlmOtherNurg": pmapcAlmOtherNurg,
       "pmapcAlmsynthAlm2": pmapcAlmsynthAlm2,
       "pmapcAlmConfTableSave": pmapcAlmConfTableSave,
       "pmapcAlmInvUpload": pmapcAlmInvUpload,
       "pmapcAlmConfTableLoad": pmapcAlmConfTableLoad,
       "pmapcAlmCorrelatOff": pmapcAlmCorrelatOff,
       "pmapcAlmmoduleWarning": pmapcAlmmoduleWarning,
       "pmapcAlmPwrInLowWng": pmapcAlmPwrInLowWng,
       "pmapcAlmPwrInHighWng": pmapcAlmPwrInHighWng,
       "pmapcAlmPwrOutLowWng": pmapcAlmPwrOutLowWng,
       "pmapcAlmPwrOutHighWng": pmapcAlmPwrOutHighWng,
       "pmapcAlmEamAttLowWng": pmapcAlmEamAttLowWng,
       "pmapcAlmEamAttHighWng": pmapcAlmEamAttHighWng,
       "pmapcAlmOtherUrg": pmapcAlmOtherUrg,
       "pmapcAlmmoduleAlarm": pmapcAlmmoduleAlarm,
       "pmapcAlmPwrInLowAla": pmapcAlmPwrInLowAla,
       "pmapcAlmPwrInHighAla": pmapcAlmPwrInHighAla,
       "pmapcAlmPwrOutLowAla": pmapcAlmPwrOutLowAla,
       "pmapcAlmPwrOutHighAla": pmapcAlmPwrOutHighAla,
       "pmapcAlmEamAttLowAla": pmapcAlmEamAttLowAla,
       "pmapcAlmEamAttHighAla": pmapcAlmEamAttHighAla,
       "pmapcAlmLossInputSignal": pmapcAlmLossInputSignal,
       "pmapcAlmmodInitFailLevel2": pmapcAlmmodInitFailLevel2,
       "pmapcAlmRegReadFail": pmapcAlmRegReadFail,
       "pmapcAlmResetHwInitFail": pmapcAlmResetHwInitFail,
       "pmapcAlmConfReadFail": pmapcAlmConfReadFail,
       "pmapcAlmInvReadFail": pmapcAlmInvReadFail,
       "pmapcAlmCalibReadFail": pmapcAlmCalibReadFail,
       "pmapcAlmThreshConfFail": pmapcAlmThreshConfFail,
       "pmapcAlmmodInitFailLevel3": pmapcAlmmodInitFailLevel3,
       "pmapcAlmOptIdentFail": pmapcAlmOptIdentFail,
       "pmapcAlmOtherCrit": pmapcAlmOtherCrit,
       "pmapcAlmsynthAlm0": pmapcAlmsynthAlm0,
       "pmapcAlmPwrInAla": pmapcAlmPwrInAla,
       "pmapcAlmPwrInWng": pmapcAlmPwrInWng,
       "pmapcAlmPwrOutAla": pmapcAlmPwrOutAla,
       "pmapcAlmPwrOutWng": pmapcAlmPwrOutWng,
       "pmapcAlmModuleGlobFailure": pmapcAlmModuleGlobFailure,
       "pmapcAlmDefFuseA": pmapcAlmDefFuseA,
       "pmapcAlmDefFuseB": pmapcAlmDefFuseB,
       "pmapcAlmClient": pmapcAlmClient,
       "pmapcAlmClientNurg": pmapcAlmClientNurg,
       "pmapcAlmlaser1MeasWng": pmapcAlmlaser1MeasWng,
       "pmapcAlmPwrLas1LowWng": pmapcAlmPwrLas1LowWng,
       "pmapcAlmPwrLas1HighWng": pmapcAlmPwrLas1HighWng,
       "pmapcAlmVthLas1LowWng": pmapcAlmVthLas1LowWng,
       "pmapcAlmVthLas1HighWng": pmapcAlmVthLas1HighWng,
       "pmapcAlmVtecLas1LowWng": pmapcAlmVtecLas1LowWng,
       "pmapcAlmVtecLas1HighWng": pmapcAlmVtecLas1HighWng,
       "pmapcAlmILas1LowWng": pmapcAlmILas1LowWng,
       "pmapcAlmILas1HighWng": pmapcAlmILas1HighWng,
       "pmapcAlmClientUrg": pmapcAlmClientUrg,
       "pmapcAlmlaser1Alm": pmapcAlmlaser1Alm,
       "pmapcAlmLas1Fail": pmapcAlmLas1Fail,
       "pmapcAlmLas1Tec1Fail": pmapcAlmLas1Tec1Fail,
       "pmapcAlmlaser1MeasAlm": pmapcAlmlaser1MeasAlm,
       "pmapcAlmPwrLas1LowAla": pmapcAlmPwrLas1LowAla,
       "pmapcAlmPwrLas1HighAla": pmapcAlmPwrLas1HighAla,
       "pmapcAlmVthLas1LowAla": pmapcAlmVthLas1LowAla,
       "pmapcAlmVthLas1HighAla": pmapcAlmVthLas1HighAla,
       "pmapcAlmVtecLas1LowAla": pmapcAlmVtecLas1LowAla,
       "pmapcAlmVtecLas1HighAla": pmapcAlmVtecLas1HighAla,
       "pmapcAlmILas1LowAla": pmapcAlmILas1LowAla,
       "pmapcAlmILas1HighAla": pmapcAlmILas1HighAla,
       "pmapcAlmClientCrit": pmapcAlmClientCrit,
       "pmapcAlmsynthAlmLaser1": pmapcAlmsynthAlmLaser1,
       "pmapcAlmLas1InitNotCompl": pmapcAlmLas1InitNotCompl,
       "pmapcAlmLas1HwFailAcc": pmapcAlmLas1HwFailAcc,
       "pmapcAlmLas1LocalOos": pmapcAlmLas1LocalOos,
       "pmapcAlmLas1MeasWng": pmapcAlmLas1MeasWng,
       "pmapcAlmLas1MeasAlm": pmapcAlmLas1MeasAlm,
       "pmapcAlmLas1FailAcc": pmapcAlmLas1FailAcc,
       "pmapcAlmsynthAlmLaser2": pmapcAlmsynthAlmLaser2,
       "pmapcAlmLas2InitNotCompl": pmapcAlmLas2InitNotCompl,
       "pmapcAlmLas2HwFailAcc": pmapcAlmLas2HwFailAcc,
       "pmapcAlmLas2LocalOos": pmapcAlmLas2LocalOos,
       "pmapcAlmLas2MeasWng": pmapcAlmLas2MeasWng,
       "pmapcAlmLas2MeasAlm": pmapcAlmLas2MeasAlm,
       "pmapcAlmLas2FailAcc": pmapcAlmLas2FailAcc,
       "pmapcAlmLine": pmapcAlmLine,
       "pmapcAlmLineNurg": pmapcAlmLineNurg,
       "pmapcAlmlaser2MeasWng": pmapcAlmlaser2MeasWng,
       "pmapcAlmPwrLas2LowWng": pmapcAlmPwrLas2LowWng,
       "pmapcAlmPwrLas2HighWng": pmapcAlmPwrLas2HighWng,
       "pmapcAlmVthLas2LowWng": pmapcAlmVthLas2LowWng,
       "pmapcAlmVthLas2HighWng": pmapcAlmVthLas2HighWng,
       "pmapcAlmVtecLas2LowWng": pmapcAlmVtecLas2LowWng,
       "pmapcAlmVtecLas2HighWng": pmapcAlmVtecLas2HighWng,
       "pmapcAlmILas2LowWng": pmapcAlmILas2LowWng,
       "pmapcAlmILas2HighWng": pmapcAlmILas2HighWng,
       "pmapcAlmLineUrg": pmapcAlmLineUrg,
       "pmapcAlmlaser2Alm": pmapcAlmlaser2Alm,
       "pmapcAlmLas2Fail": pmapcAlmLas2Fail,
       "pmapcAlmLas2TecFail": pmapcAlmLas2TecFail,
       "pmapcAlmlaser2MeasAla": pmapcAlmlaser2MeasAla,
       "pmapcAlmPwrLas2LowAla": pmapcAlmPwrLas2LowAla,
       "pmapcAlmPwrLas2HighAla": pmapcAlmPwrLas2HighAla,
       "pmapcAlmVthLas2LowAla": pmapcAlmVthLas2LowAla,
       "pmapcAlmVthLas2HighAla": pmapcAlmVthLas2HighAla,
       "pmapcAlmVtecLas2LowAla": pmapcAlmVtecLas2LowAla,
       "pmapcAlmVtecLas2HighAla": pmapcAlmVtecLas2HighAla,
       "pmapcAlmILas2LowAla": pmapcAlmILas2LowAla,
       "pmapcAlmILas2HighAla": pmapcAlmILas2HighAla,
       "pmapcAlmLineCrit": pmapcAlmLineCrit,
       "pmapcmeasures": pmapcmeasures,
       "pmapcMesrOther": pmapcMesrOther,
       "pmapcMesrmodulePowerIn": pmapcMesrmodulePowerIn,
       "pmapcMesrmoduleVPowerOut": pmapcMesrmoduleVPowerOut,
       "pmapcMesrmoduleEamAtt": pmapcMesrmoduleEamAtt,
       "pmapcMesrmoduleTemp": pmapcMesrmoduleTemp,
       "pmapcMesrmodule33v": pmapcMesrmodule33v,
       "pmapcMesrClient": pmapcMesrClient,
       "pmapcMesrpowerLas1": pmapcMesrpowerLas1,
       "pmapcMesrvthLas1": pmapcMesrvthLas1,
       "pmapcMesrvtecLas1": pmapcMesrvtecLas1,
       "pmapcMesriLas1": pmapcMesriLas1,
       "pmapcMesrLine": pmapcMesrLine,
       "pmapcMesrpowerLas2": pmapcMesrpowerLas2,
       "pmapcMesrvthLas2": pmapcMesrvthLas2,
       "pmapcMesrvtecLas2": pmapcMesrvtecLas2,
       "pmapcMesriLas2": pmapcMesriLas2,
       "pmapccontrolsWrite": pmapccontrolsWrite,
       "pmapcCtrlOther": pmapcCtrlOther,
       "pmapcCtrlsynth0": pmapcCtrlsynth0,
       "pmapcCtrlConfLoad": pmapcCtrlConfLoad,
       "pmapcCtrlConfFlash": pmapcCtrlConfFlash,
       "pmapcCtrlConfClear": pmapcCtrlConfClear,
       "pmapcCtrlsynth4": pmapcCtrlsynth4,
       "pmapcCtrlCorrelatOn": pmapcCtrlCorrelatOn,
       "pmapcCtrlCorrelatOff": pmapcCtrlCorrelatOff,
       "pmapcCtrlswMgnt": pmapcCtrlswMgnt,
       "pmapcCtrlColdReset": pmapcCtrlColdReset,
       "pmapcCtrlWarmReset": pmapcCtrlWarmReset,
       "pmapcCtrlledTest": pmapcCtrlledTest,
       "pmapcCtrlGreenLed": pmapcCtrlGreenLed,
       "pmapcCtrlRedLed": pmapcCtrlRedLed,
       "pmapcCtrlLedOff": pmapcCtrlLedOff,
       "pmapcCtrlClient": pmapcCtrlClient,
       "pmapcCtrllaser1Shutdown": pmapcCtrllaser1Shutdown,
       "pmapcCtrlLaser1Shutdown": pmapcCtrlLaser1Shutdown,
       "pmapcCtrllaser1Oos": pmapcCtrllaser1Oos,
       "pmapcCtrlLaser1OosMode": pmapcCtrlLaser1OosMode,
       "pmapcCtrlLine": pmapcCtrlLine,
       "pmapcCtrllaser2Shutdown": pmapcCtrllaser2Shutdown,
       "pmapcCtrlLaser2Shutdown": pmapcCtrlLaser2Shutdown,
       "pmapcCtrllaser2Oos": pmapcCtrllaser2Oos,
       "pmapcCtrlLaser2OosMode": pmapcCtrlLaser2OosMode,
       "pmapcCtrlmoduleOutputPwrSetting": pmapcCtrlmoduleOutputPwrSetting,
       "pmapcCtrlmoduleInputPwrSetting": pmapcCtrlmoduleInputPwrSetting,
       "pmapcri": pmapcri,
       "pmapcriTable": pmapcriTable,
       "pmapcRinvLaser1Table": pmapcRinvLaser1Table,
       "pmapcRinvLaser1Entry": pmapcRinvLaser1Entry,
       "pmapcRinvLaser1Index": pmapcRinvLaser1Index,
       "pmapcRinvLaser1": pmapcRinvLaser1,
       "pmapcRinvLaser2Table": pmapcRinvLaser2Table,
       "pmapcRinvLaser2Entry": pmapcRinvLaser2Entry,
       "pmapcRinvLaser2Index": pmapcRinvLaser2Index,
       "pmapcRinvLaser2": pmapcRinvLaser2,
       "pmapcRinvReloadInventory": pmapcRinvReloadInventory,
       "pmapcRinvHwPlatform": pmapcRinvHwPlatform,
       "pmapcRinvModulePlatform": pmapcRinvModulePlatform,
       "pmapcRinvSwPlatform": pmapcRinvSwPlatform,
       "pmapcConfig": pmapcConfig,
       "pmapcCfgLsd": pmapcCfgLsd,
       "pmapctablecomaLsd": pmapctablecomaLsd,
       "pmapcCfgStartUp": pmapcCfgStartUp,
       "pmapctablecomaStartup": pmapctablecomaStartup,
       "pmapcCfglaser1Oos": pmapcCfglaser1Oos,
       "pmapctablecombStartup": pmapctablecombStartup,
       "pmapcCfglaser2Oos": pmapcCfglaser2Oos,
       "pmapcCfgmoduleOutputPwrSetting": pmapcCfgmoduleOutputPwrSetting,
       "pmapcCfgmoduleInputPwrSetting": pmapcCfgmoduleInputPwrSetting,
       "pmapcCfgLabels": pmapcCfgLabels,
       "pmapcCfgLabelclientTable": pmapcCfgLabelclientTable,
       "pmapcCfgLabelclientEntry": pmapcCfgLabelclientEntry,
       "pmapcCfgLabelclientIndex": pmapcCfgLabelclientIndex,
       "pmapcCfgLabelclientPortn": pmapcCfgLabelclientPortn,
       "pmapcCfgLabellineTable": pmapcCfgLabellineTable,
       "pmapcCfgLabellineEntry": pmapcCfgLabellineEntry,
       "pmapcCfgLabellineIndex": pmapcCfgLabellineIndex,
       "pmapcCfgLabellinePortn": pmapcCfgLabellinePortn,
       "pmapcCfgWriteConfiguration": pmapcCfgWriteConfiguration,
       "pmapctraps": pmapctraps,
       "pmapctrapPortNumber": pmapctrapPortNumber,
       "pmapctrapLineNumber": pmapctrapLineNumber,
       "pmapctrapBoardNumber": pmapctrapBoardNumber,
       "pmapcLas2TrapNotUrgentGoesOn": pmapcLas2TrapNotUrgentGoesOn,
       "pmapcLas2TrapNotUrgentGoesOff": pmapcLas2TrapNotUrgentGoesOff,
       "pmapcLas2TrapUrgentGoesOn": pmapcLas2TrapUrgentGoesOn,
       "pmapcLas2TrapUrgentGoesOff": pmapcLas2TrapUrgentGoesOff,
       "pmapcLas2TrapCritGoesOn": pmapcLas2TrapCritGoesOn,
       "pmapcLas2TrapCritGoesOff": pmapcLas2TrapCritGoesOff,
       "pmapcLas1TrapNotUrgentGoesOn": pmapcLas1TrapNotUrgentGoesOn,
       "pmapcLas1TrapNotUrgentGoesOff": pmapcLas1TrapNotUrgentGoesOff,
       "pmapcLas1TrapUrgentGoesOn": pmapcLas1TrapUrgentGoesOn,
       "pmapcLas1TrapUrgentGoesOff": pmapcLas1TrapUrgentGoesOff,
       "pmapcLas1TrapCritGoesOn": pmapcLas1TrapCritGoesOn,
       "pmapcLas1TrapCritGoesOff": pmapcLas1TrapCritGoesOff,
       "pmapcPowerTrapUrgentGoesOn": pmapcPowerTrapUrgentGoesOn,
       "pmapcPowerTrapUrgentGoesOff": pmapcPowerTrapUrgentGoesOff}
)
