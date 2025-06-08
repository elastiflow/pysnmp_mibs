# SNMP MIB module (EKINOPS-Pmoabphcs-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Pmoabphcs-MIB.mib
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

modulepmoabphcs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61)
)
if mibBuilder.loadTexts:
    modulepmoabphcs.setRevisions(
        ("2014-03-10 00:00",
         "2014-03-10 00:00",
         "2015-01-27 00:00",
         "2016-05-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PmoabphcspreampMode(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("oabphcspreampdefaultmode", 0),
          ("oabphcspreampconstantcurrentmode", 1),
          ("oabphcspreampconstantpowermode", 2),
          ("oabphcspreampconstantgainmode", 3),
          ("oabphcspreamppoutpinmode", 4),
          ("oabphcspreampmanualmode", 5),
          ("oabphcspreampfeedforwardmode", 6),
          ("oabphcspreamptransientsupmode", 7))
    )



class PmoabphcsboosterMode(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("oabphcsboosterdefaultmode", 0),
          ("oabphcsboosterconstantcurrentmode", 1),
          ("oabphcsboosterconstantpowermode", 2),
          ("oabphcsboosterconstantgainmode", 3),
          ("oabphcsboosterpoutpinmode", 4),
          ("oabphcsboostermanualmode", 5),
          ("oabphcsboosterfeedforwardmode", 6),
          ("oabphcsboostertransientsupmode", 7))
    )



class PmoabphcsaprMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("oabphcsaproffmode", 0),
          ("oabphcsaprsemiautomode", 1),
          ("oabphcsaprautomode", 2),
          ("oabphcsaprlossforwardingmode", 3),
          ("oabphcsaprrepeatmode", 4))
    )



class PmoabphcsPreampGainAdjMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oabphcspreampgainadjmanualmode", 0),
          ("oabphcspreampgainadjsemiautomode", 1),
          ("oabphcspreampgainadjautomode", 2))
    )



class PmoabphcsBoosterGainAdjMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oabphcsboostergainadjmanualmode", 0),
          ("oabphcsboostergainadjsemiautomode", 1),
          ("oabphcsboostergainadjautomode", 2))
    )



class PmoabphcsPreampCstGainAdjMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oabphcspreampcstgainadjsemiautomode", 1),
          ("oabphcspreampcstgainadjautomode", 2))
    )



class PmoabphcsBoosterCstGainAdjMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oabphcsboostercstgainadjsemiautomode", 1),
          ("oabphcsboostercstgainadjautomode", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Pmoabphcsalarms_ObjectIdentity = ObjectIdentity
pmoabphcsalarms = _Pmoabphcsalarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2)
)
_PmoabphcsAlmOther_ObjectIdentity = ObjectIdentity
pmoabphcsAlmOther = _PmoabphcsAlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 1)
)
_PmoabphcsAlmOtherNurg_ObjectIdentity = ObjectIdentity
pmoabphcsAlmOtherNurg = _PmoabphcsAlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 1, 1)
)
_PmoabphcsAlmsynthAlm2_ObjectIdentity = ObjectIdentity
pmoabphcsAlmsynthAlm2 = _PmoabphcsAlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 1, 1, 2)
)
_PmoabphcsAlmConfTableSave_Type = EkiOnOff
_PmoabphcsAlmConfTableSave_Object = MibScalar
pmoabphcsAlmConfTableSave = _PmoabphcsAlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 1, 1, 2, 1),
    _PmoabphcsAlmConfTableSave_Type()
)
pmoabphcsAlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmConfTableSave.setStatus("current")
_PmoabphcsAlmInvUpload_Type = EkiOnOff
_PmoabphcsAlmInvUpload_Object = MibScalar
pmoabphcsAlmInvUpload = _PmoabphcsAlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 1, 1, 2, 2),
    _PmoabphcsAlmInvUpload_Type()
)
pmoabphcsAlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmInvUpload.setStatus("current")
_PmoabphcsAlmConfTableLoad_Type = EkiOnOff
_PmoabphcsAlmConfTableLoad_Object = MibScalar
pmoabphcsAlmConfTableLoad = _PmoabphcsAlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 1, 1, 2, 3),
    _PmoabphcsAlmConfTableLoad_Type()
)
pmoabphcsAlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmConfTableLoad.setStatus("current")
_PmoabphcsAlmfoaWarnings_ObjectIdentity = ObjectIdentity
pmoabphcsAlmfoaWarnings = _PmoabphcsAlmfoaWarnings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 1, 1, 75)
)
_PmoabphcsAlmTermpLowWarning_Type = EkiOnOff
_PmoabphcsAlmTermpLowWarning_Object = MibScalar
pmoabphcsAlmTermpLowWarning = _PmoabphcsAlmTermpLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 1, 1, 75, 7),
    _PmoabphcsAlmTermpLowWarning_Type()
)
pmoabphcsAlmTermpLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmTermpLowWarning.setStatus("current")
_PmoabphcsAlmTempHighWarning_Type = EkiOnOff
_PmoabphcsAlmTempHighWarning_Object = MibScalar
pmoabphcsAlmTempHighWarning = _PmoabphcsAlmTempHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 1, 1, 75, 8),
    _PmoabphcsAlmTempHighWarning_Type()
)
pmoabphcsAlmTempHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmTempHighWarning.setStatus("current")
_PmoabphcsAlmOtherUrg_ObjectIdentity = ObjectIdentity
pmoabphcsAlmOtherUrg = _PmoabphcsAlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 1, 2)
)
_PmoabphcsAlmfoaAlarms_ObjectIdentity = ObjectIdentity
pmoabphcsAlmfoaAlarms = _PmoabphcsAlmfoaAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 1, 2, 74)
)
_PmoabphcsAlmTermpLowAlarm_Type = EkiOnOff
_PmoabphcsAlmTermpLowAlarm_Object = MibScalar
pmoabphcsAlmTermpLowAlarm = _PmoabphcsAlmTermpLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 1, 2, 74, 7),
    _PmoabphcsAlmTermpLowAlarm_Type()
)
pmoabphcsAlmTermpLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmTermpLowAlarm.setStatus("current")
_PmoabphcsAlmTempHighAlarm_Type = EkiOnOff
_PmoabphcsAlmTempHighAlarm_Object = MibScalar
pmoabphcsAlmTempHighAlarm = _PmoabphcsAlmTempHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 1, 2, 74, 8),
    _PmoabphcsAlmTempHighAlarm_Type()
)
pmoabphcsAlmTempHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmTempHighAlarm.setStatus("current")
_PmoabphcsAlmOtherCrit_ObjectIdentity = ObjectIdentity
pmoabphcsAlmOtherCrit = _PmoabphcsAlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 1, 3)
)
_PmoabphcsAlmsynthAlm0_ObjectIdentity = ObjectIdentity
pmoabphcsAlmsynthAlm0 = _PmoabphcsAlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 1, 3, 0)
)
_PmoabphcsAlmMaintenanceMode_Type = EkiOnOff
_PmoabphcsAlmMaintenanceMode_Object = MibScalar
pmoabphcsAlmMaintenanceMode = _PmoabphcsAlmMaintenanceMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 1, 3, 0, 1),
    _PmoabphcsAlmMaintenanceMode_Type()
)
pmoabphcsAlmMaintenanceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmMaintenanceMode.setStatus("current")
_PmoabphcsAlmAprOn_Type = EkiOnOff
_PmoabphcsAlmAprOn_Object = MibScalar
pmoabphcsAlmAprOn = _PmoabphcsAlmAprOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 1, 3, 0, 2),
    _PmoabphcsAlmAprOn_Type()
)
pmoabphcsAlmAprOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmAprOn.setStatus("current")
_PmoabphcsAlmModGlobFail_Type = EkiOnOff
_PmoabphcsAlmModGlobFail_Object = MibScalar
pmoabphcsAlmModGlobFail = _PmoabphcsAlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 1, 3, 0, 9),
    _PmoabphcsAlmModGlobFail_Type()
)
pmoabphcsAlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmModGlobFail.setStatus("current")
_PmoabphcsAlmUpEdfaInitNotCompl_Type = EkiOnOff
_PmoabphcsAlmUpEdfaInitNotCompl_Object = MibScalar
pmoabphcsAlmUpEdfaInitNotCompl = _PmoabphcsAlmUpEdfaInitNotCompl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 1, 3, 0, 10),
    _PmoabphcsAlmUpEdfaInitNotCompl_Type()
)
pmoabphcsAlmUpEdfaInitNotCompl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmUpEdfaInitNotCompl.setStatus("current")
_PmoabphcsAlmDwEdfaInitNotCompl_Type = EkiOnOff
_PmoabphcsAlmDwEdfaInitNotCompl_Object = MibScalar
pmoabphcsAlmDwEdfaInitNotCompl = _PmoabphcsAlmDwEdfaInitNotCompl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 1, 3, 0, 11),
    _PmoabphcsAlmDwEdfaInitNotCompl_Type()
)
pmoabphcsAlmDwEdfaInitNotCompl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmDwEdfaInitNotCompl.setStatus("current")
_PmoabphcsAlmExtPump1NotLocked_Type = EkiOnOff
_PmoabphcsAlmExtPump1NotLocked_Object = MibScalar
pmoabphcsAlmExtPump1NotLocked = _PmoabphcsAlmExtPump1NotLocked_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 1, 3, 0, 12),
    _PmoabphcsAlmExtPump1NotLocked_Type()
)
pmoabphcsAlmExtPump1NotLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmExtPump1NotLocked.setStatus("current")
_PmoabphcsAlmDefFuseA_Type = EkiOnOff
_PmoabphcsAlmDefFuseA_Object = MibScalar
pmoabphcsAlmDefFuseA = _PmoabphcsAlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 1, 3, 0, 15),
    _PmoabphcsAlmDefFuseA_Type()
)
pmoabphcsAlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmDefFuseA.setStatus("current")
_PmoabphcsAlmDefFuseB_Type = EkiOnOff
_PmoabphcsAlmDefFuseB_Object = MibScalar
pmoabphcsAlmDefFuseB = _PmoabphcsAlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 1, 3, 0, 16),
    _PmoabphcsAlmDefFuseB_Type()
)
pmoabphcsAlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmDefFuseB.setStatus("current")
_PmoabphcsAlmClient_ObjectIdentity = ObjectIdentity
pmoabphcsAlmClient = _PmoabphcsAlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 2)
)
_PmoabphcsAlmClientNurg_ObjectIdentity = ObjectIdentity
pmoabphcsAlmClientNurg = _PmoabphcsAlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 2, 1)
)
_PmoabphcsAlmclientEdfaWarnings_ObjectIdentity = ObjectIdentity
pmoabphcsAlmclientEdfaWarnings = _PmoabphcsAlmclientEdfaWarnings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 2, 1, 33)
)
_PmoabphcsAlmClientGainLowWarning_Type = EkiOnOff
_PmoabphcsAlmClientGainLowWarning_Object = MibScalar
pmoabphcsAlmClientGainLowWarning = _PmoabphcsAlmClientGainLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 2, 1, 33, 1),
    _PmoabphcsAlmClientGainLowWarning_Type()
)
pmoabphcsAlmClientGainLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmClientGainLowWarning.setStatus("current")
_PmoabphcsAlmClientGainHighWarning_Type = EkiOnOff
_PmoabphcsAlmClientGainHighWarning_Object = MibScalar
pmoabphcsAlmClientGainHighWarning = _PmoabphcsAlmClientGainHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 2, 1, 33, 2),
    _PmoabphcsAlmClientGainHighWarning_Type()
)
pmoabphcsAlmClientGainHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmClientGainHighWarning.setStatus("current")
_PmoabphcsAlmClientInputPwrLowWarning_Type = EkiOnOff
_PmoabphcsAlmClientInputPwrLowWarning_Object = MibScalar
pmoabphcsAlmClientInputPwrLowWarning = _PmoabphcsAlmClientInputPwrLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 2, 1, 33, 3),
    _PmoabphcsAlmClientInputPwrLowWarning_Type()
)
pmoabphcsAlmClientInputPwrLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmClientInputPwrLowWarning.setStatus("current")
_PmoabphcsAlmClientInputPwrHighWarning_Type = EkiOnOff
_PmoabphcsAlmClientInputPwrHighWarning_Object = MibScalar
pmoabphcsAlmClientInputPwrHighWarning = _PmoabphcsAlmClientInputPwrHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 2, 1, 33, 4),
    _PmoabphcsAlmClientInputPwrHighWarning_Type()
)
pmoabphcsAlmClientInputPwrHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmClientInputPwrHighWarning.setStatus("current")
_PmoabphcsAlmClientOutputPwrLowWarning_Type = EkiOnOff
_PmoabphcsAlmClientOutputPwrLowWarning_Object = MibScalar
pmoabphcsAlmClientOutputPwrLowWarning = _PmoabphcsAlmClientOutputPwrLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 2, 1, 33, 5),
    _PmoabphcsAlmClientOutputPwrLowWarning_Type()
)
pmoabphcsAlmClientOutputPwrLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmClientOutputPwrLowWarning.setStatus("current")
_PmoabphcsAlmClientOutputPwrHighWarning_Type = EkiOnOff
_PmoabphcsAlmClientOutputPwrHighWarning_Object = MibScalar
pmoabphcsAlmClientOutputPwrHighWarning = _PmoabphcsAlmClientOutputPwrHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 2, 1, 33, 6),
    _PmoabphcsAlmClientOutputPwrHighWarning_Type()
)
pmoabphcsAlmClientOutputPwrHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmClientOutputPwrHighWarning.setStatus("current")
_PmoabphcsAlmClientBiasLowWarning_Type = EkiOnOff
_PmoabphcsAlmClientBiasLowWarning_Object = MibScalar
pmoabphcsAlmClientBiasLowWarning = _PmoabphcsAlmClientBiasLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 2, 1, 33, 7),
    _PmoabphcsAlmClientBiasLowWarning_Type()
)
pmoabphcsAlmClientBiasLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmClientBiasLowWarning.setStatus("current")
_PmoabphcsAlmClientBiasHighWarning_Type = EkiOnOff
_PmoabphcsAlmClientBiasHighWarning_Object = MibScalar
pmoabphcsAlmClientBiasHighWarning = _PmoabphcsAlmClientBiasHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 2, 1, 33, 8),
    _PmoabphcsAlmClientBiasHighWarning_Type()
)
pmoabphcsAlmClientBiasHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmClientBiasHighWarning.setStatus("current")
_PmoabphcsAlmClientUrg_ObjectIdentity = ObjectIdentity
pmoabphcsAlmClientUrg = _PmoabphcsAlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 2, 2)
)
_PmoabphcsAlmclientEdfaAlarms1_ObjectIdentity = ObjectIdentity
pmoabphcsAlmclientEdfaAlarms1 = _PmoabphcsAlmclientEdfaAlarms1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 2, 2, 32)
)
_PmoabphcsAlmClientGainLowAlarm_Type = EkiOnOff
_PmoabphcsAlmClientGainLowAlarm_Object = MibScalar
pmoabphcsAlmClientGainLowAlarm = _PmoabphcsAlmClientGainLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 2, 2, 32, 1),
    _PmoabphcsAlmClientGainLowAlarm_Type()
)
pmoabphcsAlmClientGainLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmClientGainLowAlarm.setStatus("current")
_PmoabphcsAlmClientGainHighAlarm_Type = EkiOnOff
_PmoabphcsAlmClientGainHighAlarm_Object = MibScalar
pmoabphcsAlmClientGainHighAlarm = _PmoabphcsAlmClientGainHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 2, 2, 32, 2),
    _PmoabphcsAlmClientGainHighAlarm_Type()
)
pmoabphcsAlmClientGainHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmClientGainHighAlarm.setStatus("current")
_PmoabphcsAlmClientInputPwrLowAlarm_Type = EkiOnOff
_PmoabphcsAlmClientInputPwrLowAlarm_Object = MibScalar
pmoabphcsAlmClientInputPwrLowAlarm = _PmoabphcsAlmClientInputPwrLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 2, 2, 32, 3),
    _PmoabphcsAlmClientInputPwrLowAlarm_Type()
)
pmoabphcsAlmClientInputPwrLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmClientInputPwrLowAlarm.setStatus("current")
_PmoabphcsAlmClientInputPwrHighAlarm_Type = EkiOnOff
_PmoabphcsAlmClientInputPwrHighAlarm_Object = MibScalar
pmoabphcsAlmClientInputPwrHighAlarm = _PmoabphcsAlmClientInputPwrHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 2, 2, 32, 4),
    _PmoabphcsAlmClientInputPwrHighAlarm_Type()
)
pmoabphcsAlmClientInputPwrHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmClientInputPwrHighAlarm.setStatus("current")
_PmoabphcsAlmClientOutputPwrLowAlarm_Type = EkiOnOff
_PmoabphcsAlmClientOutputPwrLowAlarm_Object = MibScalar
pmoabphcsAlmClientOutputPwrLowAlarm = _PmoabphcsAlmClientOutputPwrLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 2, 2, 32, 5),
    _PmoabphcsAlmClientOutputPwrLowAlarm_Type()
)
pmoabphcsAlmClientOutputPwrLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmClientOutputPwrLowAlarm.setStatus("current")
_PmoabphcsAlmClientOutputPwrHighAlarm_Type = EkiOnOff
_PmoabphcsAlmClientOutputPwrHighAlarm_Object = MibScalar
pmoabphcsAlmClientOutputPwrHighAlarm = _PmoabphcsAlmClientOutputPwrHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 2, 2, 32, 6),
    _PmoabphcsAlmClientOutputPwrHighAlarm_Type()
)
pmoabphcsAlmClientOutputPwrHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmClientOutputPwrHighAlarm.setStatus("current")
_PmoabphcsAlmClientBiasLowAlarm_Type = EkiOnOff
_PmoabphcsAlmClientBiasLowAlarm_Object = MibScalar
pmoabphcsAlmClientBiasLowAlarm = _PmoabphcsAlmClientBiasLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 2, 2, 32, 7),
    _PmoabphcsAlmClientBiasLowAlarm_Type()
)
pmoabphcsAlmClientBiasLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmClientBiasLowAlarm.setStatus("current")
_PmoabphcsAlmClientBiasHighAlarm_Type = EkiOnOff
_PmoabphcsAlmClientBiasHighAlarm_Object = MibScalar
pmoabphcsAlmClientBiasHighAlarm = _PmoabphcsAlmClientBiasHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 2, 2, 32, 8),
    _PmoabphcsAlmClientBiasHighAlarm_Type()
)
pmoabphcsAlmClientBiasHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmClientBiasHighAlarm.setStatus("current")
_PmoabphcsAlmClientCrit_ObjectIdentity = ObjectIdentity
pmoabphcsAlmClientCrit = _PmoabphcsAlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 2, 3)
)
_PmoabphcsAlmsynthAlm8_ObjectIdentity = ObjectIdentity
pmoabphcsAlmsynthAlm8 = _PmoabphcsAlmsynthAlm8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 2, 3, 8)
)
_PmoabphcsAlmClientHwFail_Type = EkiOnOff
_PmoabphcsAlmClientHwFail_Object = MibScalar
pmoabphcsAlmClientHwFail = _PmoabphcsAlmClientHwFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 2, 3, 8, 4),
    _PmoabphcsAlmClientHwFail_Type()
)
pmoabphcsAlmClientHwFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmClientHwFail.setStatus("current")
_PmoabphcsAlmClientTxOff_Type = EkiOnOff
_PmoabphcsAlmClientTxOff_Object = MibScalar
pmoabphcsAlmClientTxOff = _PmoabphcsAlmClientTxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 2, 3, 8, 5),
    _PmoabphcsAlmClientTxOff_Type()
)
pmoabphcsAlmClientTxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmClientTxOff.setStatus("current")
_PmoabphcsAlmClientFail_Type = EkiOnOff
_PmoabphcsAlmClientFail_Object = MibScalar
pmoabphcsAlmClientFail = _PmoabphcsAlmClientFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 2, 3, 8, 12),
    _PmoabphcsAlmClientFail_Type()
)
pmoabphcsAlmClientFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmClientFail.setStatus("current")
_PmoabphcsAlmClientExtPumpFail_Type = EkiOnOff
_PmoabphcsAlmClientExtPumpFail_Object = MibScalar
pmoabphcsAlmClientExtPumpFail = _PmoabphcsAlmClientExtPumpFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 2, 3, 8, 13),
    _PmoabphcsAlmClientExtPumpFail_Type()
)
pmoabphcsAlmClientExtPumpFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmClientExtPumpFail.setStatus("current")
_PmoabphcsAlmSupvbFail_Type = EkiOnOff
_PmoabphcsAlmSupvbFail_Object = MibScalar
pmoabphcsAlmSupvbFail = _PmoabphcsAlmSupvbFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 2, 3, 8, 14),
    _PmoabphcsAlmSupvbFail_Type()
)
pmoabphcsAlmSupvbFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmSupvbFail.setStatus("current")
_PmoabphcsAlmclientEdfaAlarms2_ObjectIdentity = ObjectIdentity
pmoabphcsAlmclientEdfaAlarms2 = _PmoabphcsAlmclientEdfaAlarms2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 2, 3, 35)
)
_PmoabphcsAlmClientEdfaNr_Type = EkiOnOff
_PmoabphcsAlmClientEdfaNr_Object = MibScalar
pmoabphcsAlmClientEdfaNr = _PmoabphcsAlmClientEdfaNr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 2, 3, 35, 1),
    _PmoabphcsAlmClientEdfaNr_Type()
)
pmoabphcsAlmClientEdfaNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmClientEdfaNr.setStatus("current")
_PmoabphcsAlmClientEdfaTecFail_Type = EkiOnOff
_PmoabphcsAlmClientEdfaTecFail_Object = MibScalar
pmoabphcsAlmClientEdfaTecFail = _PmoabphcsAlmClientEdfaTecFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 2, 3, 35, 2),
    _PmoabphcsAlmClientEdfaTecFail_Type()
)
pmoabphcsAlmClientEdfaTecFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmClientEdfaTecFail.setStatus("current")
_PmoabphcsAlmClientEdfaLaserFail_Type = EkiOnOff
_PmoabphcsAlmClientEdfaLaserFail_Object = MibScalar
pmoabphcsAlmClientEdfaLaserFail = _PmoabphcsAlmClientEdfaLaserFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 2, 3, 35, 3),
    _PmoabphcsAlmClientEdfaLaserFail_Type()
)
pmoabphcsAlmClientEdfaLaserFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmClientEdfaLaserFail.setStatus("current")
_PmoabphcsAlmClientEdfaLos_Type = EkiOnOff
_PmoabphcsAlmClientEdfaLos_Object = MibScalar
pmoabphcsAlmClientEdfaLos = _PmoabphcsAlmClientEdfaLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 2, 3, 35, 4),
    _PmoabphcsAlmClientEdfaLos_Type()
)
pmoabphcsAlmClientEdfaLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmClientEdfaLos.setStatus("current")
_PmoabphcsAlmClientExtPumpEdfaLowCurrent_Type = EkiOnOff
_PmoabphcsAlmClientExtPumpEdfaLowCurrent_Object = MibScalar
pmoabphcsAlmClientExtPumpEdfaLowCurrent = _PmoabphcsAlmClientExtPumpEdfaLowCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 2, 3, 35, 5),
    _PmoabphcsAlmClientExtPumpEdfaLowCurrent_Type()
)
pmoabphcsAlmClientExtPumpEdfaLowCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmClientExtPumpEdfaLowCurrent.setStatus("current")
_PmoabphcsAlmClientGainOutOfRange_Type = EkiOnOff
_PmoabphcsAlmClientGainOutOfRange_Object = MibScalar
pmoabphcsAlmClientGainOutOfRange = _PmoabphcsAlmClientGainOutOfRange_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 2, 3, 35, 6),
    _PmoabphcsAlmClientGainOutOfRange_Type()
)
pmoabphcsAlmClientGainOutOfRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmClientGainOutOfRange.setStatus("current")
_PmoabphcsAlmclientMsaAlarms_ObjectIdentity = ObjectIdentity
pmoabphcsAlmclientMsaAlarms = _PmoabphcsAlmclientMsaAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 2, 3, 37)
)
_PmoabphcsAlmClientMsaLos_Type = EkiOnOff
_PmoabphcsAlmClientMsaLos_Object = MibScalar
pmoabphcsAlmClientMsaLos = _PmoabphcsAlmClientMsaLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 2, 3, 37, 1),
    _PmoabphcsAlmClientMsaLos_Type()
)
pmoabphcsAlmClientMsaLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmClientMsaLos.setStatus("current")
_PmoabphcsAlmClientMsaAttenuation_Type = EkiOnOff
_PmoabphcsAlmClientMsaAttenuation_Object = MibScalar
pmoabphcsAlmClientMsaAttenuation = _PmoabphcsAlmClientMsaAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 2, 3, 37, 2),
    _PmoabphcsAlmClientMsaAttenuation_Type()
)
pmoabphcsAlmClientMsaAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmClientMsaAttenuation.setStatus("current")
_PmoabphcsAlmLine_ObjectIdentity = ObjectIdentity
pmoabphcsAlmLine = _PmoabphcsAlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3)
)
_PmoabphcsAlmLineNurg_ObjectIdentity = ObjectIdentity
pmoabphcsAlmLineNurg = _PmoabphcsAlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 1)
)
_PmoabphcsAlmlineEdfaWarnings_ObjectIdentity = ObjectIdentity
pmoabphcsAlmlineEdfaWarnings = _PmoabphcsAlmlineEdfaWarnings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 1, 41)
)
_PmoabphcsAlmLineGainLowWarning_Type = EkiOnOff
_PmoabphcsAlmLineGainLowWarning_Object = MibScalar
pmoabphcsAlmLineGainLowWarning = _PmoabphcsAlmLineGainLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 1, 41, 1),
    _PmoabphcsAlmLineGainLowWarning_Type()
)
pmoabphcsAlmLineGainLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineGainLowWarning.setStatus("current")
_PmoabphcsAlmLineGainHighWarning_Type = EkiOnOff
_PmoabphcsAlmLineGainHighWarning_Object = MibScalar
pmoabphcsAlmLineGainHighWarning = _PmoabphcsAlmLineGainHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 1, 41, 2),
    _PmoabphcsAlmLineGainHighWarning_Type()
)
pmoabphcsAlmLineGainHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineGainHighWarning.setStatus("current")
_PmoabphcsAlmLineInputPwrLowWarning_Type = EkiOnOff
_PmoabphcsAlmLineInputPwrLowWarning_Object = MibScalar
pmoabphcsAlmLineInputPwrLowWarning = _PmoabphcsAlmLineInputPwrLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 1, 41, 3),
    _PmoabphcsAlmLineInputPwrLowWarning_Type()
)
pmoabphcsAlmLineInputPwrLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineInputPwrLowWarning.setStatus("current")
_PmoabphcsAlmLineInputPwrHighWarning_Type = EkiOnOff
_PmoabphcsAlmLineInputPwrHighWarning_Object = MibScalar
pmoabphcsAlmLineInputPwrHighWarning = _PmoabphcsAlmLineInputPwrHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 1, 41, 4),
    _PmoabphcsAlmLineInputPwrHighWarning_Type()
)
pmoabphcsAlmLineInputPwrHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineInputPwrHighWarning.setStatus("current")
_PmoabphcsAlmLineOutputPwrLowWarning_Type = EkiOnOff
_PmoabphcsAlmLineOutputPwrLowWarning_Object = MibScalar
pmoabphcsAlmLineOutputPwrLowWarning = _PmoabphcsAlmLineOutputPwrLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 1, 41, 5),
    _PmoabphcsAlmLineOutputPwrLowWarning_Type()
)
pmoabphcsAlmLineOutputPwrLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineOutputPwrLowWarning.setStatus("current")
_PmoabphcsAlmLineOutputPwrHighWarning_Type = EkiOnOff
_PmoabphcsAlmLineOutputPwrHighWarning_Object = MibScalar
pmoabphcsAlmLineOutputPwrHighWarning = _PmoabphcsAlmLineOutputPwrHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 1, 41, 6),
    _PmoabphcsAlmLineOutputPwrHighWarning_Type()
)
pmoabphcsAlmLineOutputPwrHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineOutputPwrHighWarning.setStatus("current")
_PmoabphcsAlmLineBiasLowWarning_Type = EkiOnOff
_PmoabphcsAlmLineBiasLowWarning_Object = MibScalar
pmoabphcsAlmLineBiasLowWarning = _PmoabphcsAlmLineBiasLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 1, 41, 7),
    _PmoabphcsAlmLineBiasLowWarning_Type()
)
pmoabphcsAlmLineBiasLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineBiasLowWarning.setStatus("current")
_PmoabphcsAlmLineBiasHighWarning_Type = EkiOnOff
_PmoabphcsAlmLineBiasHighWarning_Object = MibScalar
pmoabphcsAlmLineBiasHighWarning = _PmoabphcsAlmLineBiasHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 1, 41, 8),
    _PmoabphcsAlmLineBiasHighWarning_Type()
)
pmoabphcsAlmLineBiasHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineBiasHighWarning.setStatus("current")
_PmoabphcsAlmLineUrg_ObjectIdentity = ObjectIdentity
pmoabphcsAlmLineUrg = _PmoabphcsAlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 2)
)
_PmoabphcsAlmlineEdfaAlarms1_ObjectIdentity = ObjectIdentity
pmoabphcsAlmlineEdfaAlarms1 = _PmoabphcsAlmlineEdfaAlarms1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 2, 40)
)
_PmoabphcsAlmLineGainLowAlarm_Type = EkiOnOff
_PmoabphcsAlmLineGainLowAlarm_Object = MibScalar
pmoabphcsAlmLineGainLowAlarm = _PmoabphcsAlmLineGainLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 2, 40, 1),
    _PmoabphcsAlmLineGainLowAlarm_Type()
)
pmoabphcsAlmLineGainLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineGainLowAlarm.setStatus("current")
_PmoabphcsAlmLineGainHighAlarm_Type = EkiOnOff
_PmoabphcsAlmLineGainHighAlarm_Object = MibScalar
pmoabphcsAlmLineGainHighAlarm = _PmoabphcsAlmLineGainHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 2, 40, 2),
    _PmoabphcsAlmLineGainHighAlarm_Type()
)
pmoabphcsAlmLineGainHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineGainHighAlarm.setStatus("current")
_PmoabphcsAlmLineInputPwrLowAlarm_Type = EkiOnOff
_PmoabphcsAlmLineInputPwrLowAlarm_Object = MibScalar
pmoabphcsAlmLineInputPwrLowAlarm = _PmoabphcsAlmLineInputPwrLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 2, 40, 3),
    _PmoabphcsAlmLineInputPwrLowAlarm_Type()
)
pmoabphcsAlmLineInputPwrLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineInputPwrLowAlarm.setStatus("current")
_PmoabphcsAlmLineInputPwrHighAlarm_Type = EkiOnOff
_PmoabphcsAlmLineInputPwrHighAlarm_Object = MibScalar
pmoabphcsAlmLineInputPwrHighAlarm = _PmoabphcsAlmLineInputPwrHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 2, 40, 4),
    _PmoabphcsAlmLineInputPwrHighAlarm_Type()
)
pmoabphcsAlmLineInputPwrHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineInputPwrHighAlarm.setStatus("current")
_PmoabphcsAlmLineOutputPwrLowAlarm_Type = EkiOnOff
_PmoabphcsAlmLineOutputPwrLowAlarm_Object = MibScalar
pmoabphcsAlmLineOutputPwrLowAlarm = _PmoabphcsAlmLineOutputPwrLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 2, 40, 5),
    _PmoabphcsAlmLineOutputPwrLowAlarm_Type()
)
pmoabphcsAlmLineOutputPwrLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineOutputPwrLowAlarm.setStatus("current")
_PmoabphcsAlmLineOutputPwrHighAlarm_Type = EkiOnOff
_PmoabphcsAlmLineOutputPwrHighAlarm_Object = MibScalar
pmoabphcsAlmLineOutputPwrHighAlarm = _PmoabphcsAlmLineOutputPwrHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 2, 40, 6),
    _PmoabphcsAlmLineOutputPwrHighAlarm_Type()
)
pmoabphcsAlmLineOutputPwrHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineOutputPwrHighAlarm.setStatus("current")
_PmoabphcsAlmLineBiasLowAlarm_Type = EkiOnOff
_PmoabphcsAlmLineBiasLowAlarm_Object = MibScalar
pmoabphcsAlmLineBiasLowAlarm = _PmoabphcsAlmLineBiasLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 2, 40, 7),
    _PmoabphcsAlmLineBiasLowAlarm_Type()
)
pmoabphcsAlmLineBiasLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineBiasLowAlarm.setStatus("current")
_PmoabphcsAlmLineBiasHighAlarm_Type = EkiOnOff
_PmoabphcsAlmLineBiasHighAlarm_Object = MibScalar
pmoabphcsAlmLineBiasHighAlarm = _PmoabphcsAlmLineBiasHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 2, 40, 8),
    _PmoabphcsAlmLineBiasHighAlarm_Type()
)
pmoabphcsAlmLineBiasHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineBiasHighAlarm.setStatus("current")
_PmoabphcsAlmLineCrit_ObjectIdentity = ObjectIdentity
pmoabphcsAlmLineCrit = _PmoabphcsAlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3)
)
_PmoabphcsAlmsynthAlm7_ObjectIdentity = ObjectIdentity
pmoabphcsAlmsynthAlm7 = _PmoabphcsAlmsynthAlm7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 7)
)
_PmoabphcsAlmLineHwFail_Type = EkiOnOff
_PmoabphcsAlmLineHwFail_Object = MibScalar
pmoabphcsAlmLineHwFail = _PmoabphcsAlmLineHwFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 7, 4),
    _PmoabphcsAlmLineHwFail_Type()
)
pmoabphcsAlmLineHwFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineHwFail.setStatus("current")
_PmoabphcsAlmLineTxOff_Type = EkiOnOff
_PmoabphcsAlmLineTxOff_Object = MibScalar
pmoabphcsAlmLineTxOff = _PmoabphcsAlmLineTxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 7, 5),
    _PmoabphcsAlmLineTxOff_Type()
)
pmoabphcsAlmLineTxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineTxOff.setStatus("current")
_PmoabphcsAlmLineFail_Type = EkiOnOff
_PmoabphcsAlmLineFail_Object = MibScalar
pmoabphcsAlmLineFail = _PmoabphcsAlmLineFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 7, 12),
    _PmoabphcsAlmLineFail_Type()
)
pmoabphcsAlmLineFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineFail.setStatus("current")
_PmoabphcsAlmLineExtPumpFail_Type = EkiOnOff
_PmoabphcsAlmLineExtPumpFail_Object = MibScalar
pmoabphcsAlmLineExtPumpFail = _PmoabphcsAlmLineExtPumpFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 7, 13),
    _PmoabphcsAlmLineExtPumpFail_Type()
)
pmoabphcsAlmLineExtPumpFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineExtPumpFail.setStatus("current")
_PmoabphcsAlmSupvaFail_Type = EkiOnOff
_PmoabphcsAlmSupvaFail_Object = MibScalar
pmoabphcsAlmSupvaFail = _PmoabphcsAlmSupvaFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 7, 14),
    _PmoabphcsAlmSupvaFail_Type()
)
pmoabphcsAlmSupvaFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmSupvaFail.setStatus("current")
_PmoabphcsAlmlineEdfaAlarms2_ObjectIdentity = ObjectIdentity
pmoabphcsAlmlineEdfaAlarms2 = _PmoabphcsAlmlineEdfaAlarms2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 43)
)
_PmoabphcsAlmLineEdfaNr_Type = EkiOnOff
_PmoabphcsAlmLineEdfaNr_Object = MibScalar
pmoabphcsAlmLineEdfaNr = _PmoabphcsAlmLineEdfaNr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 43, 1),
    _PmoabphcsAlmLineEdfaNr_Type()
)
pmoabphcsAlmLineEdfaNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineEdfaNr.setStatus("current")
_PmoabphcsAlmLineEdfaTecFail_Type = EkiOnOff
_PmoabphcsAlmLineEdfaTecFail_Object = MibScalar
pmoabphcsAlmLineEdfaTecFail = _PmoabphcsAlmLineEdfaTecFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 43, 2),
    _PmoabphcsAlmLineEdfaTecFail_Type()
)
pmoabphcsAlmLineEdfaTecFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineEdfaTecFail.setStatus("current")
_PmoabphcsAlmLineEdfaLaserFail_Type = EkiOnOff
_PmoabphcsAlmLineEdfaLaserFail_Object = MibScalar
pmoabphcsAlmLineEdfaLaserFail = _PmoabphcsAlmLineEdfaLaserFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 43, 3),
    _PmoabphcsAlmLineEdfaLaserFail_Type()
)
pmoabphcsAlmLineEdfaLaserFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineEdfaLaserFail.setStatus("current")
_PmoabphcsAlmLineEdfaLos_Type = EkiOnOff
_PmoabphcsAlmLineEdfaLos_Object = MibScalar
pmoabphcsAlmLineEdfaLos = _PmoabphcsAlmLineEdfaLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 43, 4),
    _PmoabphcsAlmLineEdfaLos_Type()
)
pmoabphcsAlmLineEdfaLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineEdfaLos.setStatus("current")
_PmoabphcsAlmLineExtPumpEdfaLowCurrent_Type = EkiOnOff
_PmoabphcsAlmLineExtPumpEdfaLowCurrent_Object = MibScalar
pmoabphcsAlmLineExtPumpEdfaLowCurrent = _PmoabphcsAlmLineExtPumpEdfaLowCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 43, 5),
    _PmoabphcsAlmLineExtPumpEdfaLowCurrent_Type()
)
pmoabphcsAlmLineExtPumpEdfaLowCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineExtPumpEdfaLowCurrent.setStatus("current")
_PmoabphcsAlmLineGainOutOfRange_Type = EkiOnOff
_PmoabphcsAlmLineGainOutOfRange_Object = MibScalar
pmoabphcsAlmLineGainOutOfRange = _PmoabphcsAlmLineGainOutOfRange_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 43, 6),
    _PmoabphcsAlmLineGainOutOfRange_Type()
)
pmoabphcsAlmLineGainOutOfRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineGainOutOfRange.setStatus("current")
_PmoabphcsAlmlineMsaAlarms_ObjectIdentity = ObjectIdentity
pmoabphcsAlmlineMsaAlarms = _PmoabphcsAlmlineMsaAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 45)
)
_PmoabphcsAlmLineMsaLos_Type = EkiOnOff
_PmoabphcsAlmLineMsaLos_Object = MibScalar
pmoabphcsAlmLineMsaLos = _PmoabphcsAlmLineMsaLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 45, 1),
    _PmoabphcsAlmLineMsaLos_Type()
)
pmoabphcsAlmLineMsaLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineMsaLos.setStatus("current")
_PmoabphcsAlmLineMsaAttenuation_Type = EkiOnOff
_PmoabphcsAlmLineMsaAttenuation_Object = MibScalar
pmoabphcsAlmLineMsaAttenuation = _PmoabphcsAlmLineMsaAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 45, 2),
    _PmoabphcsAlmLineMsaAttenuation_Type()
)
pmoabphcsAlmLineMsaAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineMsaAttenuation.setStatus("current")
_PmoabphcsAlmlineOscAlarmsTable_Object = MibTable
pmoabphcsAlmlineOscAlarmsTable = _PmoabphcsAlmlineOscAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 48)
)
if mibBuilder.loadTexts:
    pmoabphcsAlmlineOscAlarmsTable.setStatus("current")
_PmoabphcsAlmlineOscAlarmsEntry_Object = MibTableRow
pmoabphcsAlmlineOscAlarmsEntry = _PmoabphcsAlmlineOscAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 48, 1)
)
pmoabphcsAlmlineOscAlarmsEntry.setIndexNames(
    (0, "EKINOPS-Pmoabphcs-MIB", "pmoabphcsAlmlineOscAlarmsIndex"),
)
if mibBuilder.loadTexts:
    pmoabphcsAlmlineOscAlarmsEntry.setStatus("current")


class _PmoabphcsAlmlineOscAlarmsIndex_Type(Integer32):
    """Custom type pmoabphcsAlmlineOscAlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmoabphcsAlmlineOscAlarmsIndex_Type.__name__ = "Integer32"
_PmoabphcsAlmlineOscAlarmsIndex_Object = MibTableColumn
pmoabphcsAlmlineOscAlarmsIndex = _PmoabphcsAlmlineOscAlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 48, 1, 1),
    _PmoabphcsAlmlineOscAlarmsIndex_Type()
)
pmoabphcsAlmlineOscAlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmlineOscAlarmsIndex.setStatus("current")
_PmoabphcsAlmLineLosPortn_Type = EkiOnOff
_PmoabphcsAlmLineLosPortn_Object = MibTableColumn
pmoabphcsAlmLineLosPortn = _PmoabphcsAlmLineLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 48, 1, 2),
    _PmoabphcsAlmLineLosPortn_Type()
)
pmoabphcsAlmLineLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineLosPortn.setStatus("current")
_PmoabphcsAlmLineTxOffPortn_Type = EkiOnOff
_PmoabphcsAlmLineTxOffPortn_Object = MibTableColumn
pmoabphcsAlmLineTxOffPortn = _PmoabphcsAlmLineTxOffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 48, 1, 3),
    _PmoabphcsAlmLineTxOffPortn_Type()
)
pmoabphcsAlmLineTxOffPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineTxOffPortn.setStatus("current")
_PmoabphcsAlmLineTxFailPortn_Type = EkiOnOff
_PmoabphcsAlmLineTxFailPortn_Object = MibTableColumn
pmoabphcsAlmLineTxFailPortn = _PmoabphcsAlmLineTxFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 48, 1, 4),
    _PmoabphcsAlmLineTxFailPortn_Type()
)
pmoabphcsAlmLineTxFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineTxFailPortn.setStatus("current")
_PmoabphcsAlmLineFecFailPortn_Type = EkiOnOff
_PmoabphcsAlmLineFecFailPortn_Object = MibTableColumn
pmoabphcsAlmLineFecFailPortn = _PmoabphcsAlmLineFecFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 48, 1, 5),
    _PmoabphcsAlmLineFecFailPortn_Type()
)
pmoabphcsAlmLineFecFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineFecFailPortn.setStatus("current")
_PmoabphcsAlmLineOosPortn_Type = EkiOnOff
_PmoabphcsAlmLineOosPortn_Object = MibTableColumn
pmoabphcsAlmLineOosPortn = _PmoabphcsAlmLineOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 48, 1, 6),
    _PmoabphcsAlmLineOosPortn_Type()
)
pmoabphcsAlmLineOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineOosPortn.setStatus("current")
_PmoabphcsAlmLineLofPortn_Type = EkiOnOff
_PmoabphcsAlmLineLofPortn_Object = MibTableColumn
pmoabphcsAlmLineLofPortn = _PmoabphcsAlmLineLofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 48, 1, 7),
    _PmoabphcsAlmLineLofPortn_Type()
)
pmoabphcsAlmLineLofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineLofPortn.setStatus("current")
_PmoabphcsAlmLineOofPortn_Type = EkiOnOff
_PmoabphcsAlmLineOofPortn_Object = MibTableColumn
pmoabphcsAlmLineOofPortn = _PmoabphcsAlmLineOofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 48, 1, 8),
    _PmoabphcsAlmLineOofPortn_Type()
)
pmoabphcsAlmLineOofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineOofPortn.setStatus("current")
_PmoabphcsAlmLineRemoteTxFailPortn_Type = EkiOnOff
_PmoabphcsAlmLineRemoteTxFailPortn_Object = MibTableColumn
pmoabphcsAlmLineRemoteTxFailPortn = _PmoabphcsAlmLineRemoteTxFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 48, 1, 9),
    _PmoabphcsAlmLineRemoteTxFailPortn_Type()
)
pmoabphcsAlmLineRemoteTxFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineRemoteTxFailPortn.setStatus("current")
_PmoabphcsAlmLineWarningPortn_Type = EkiOnOff
_PmoabphcsAlmLineWarningPortn_Object = MibTableColumn
pmoabphcsAlmLineWarningPortn = _PmoabphcsAlmLineWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 48, 1, 10),
    _PmoabphcsAlmLineWarningPortn_Type()
)
pmoabphcsAlmLineWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineWarningPortn.setStatus("current")
_PmoabphcsAlmLineAlmPortn_Type = EkiOnOff
_PmoabphcsAlmLineAlmPortn_Object = MibTableColumn
pmoabphcsAlmLineAlmPortn = _PmoabphcsAlmLineAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 48, 1, 11),
    _PmoabphcsAlmLineAlmPortn_Type()
)
pmoabphcsAlmLineAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineAlmPortn.setStatus("current")
_PmoabphcsAlmlineOscThresholdAlarmsTable_Object = MibTable
pmoabphcsAlmlineOscThresholdAlarmsTable = _PmoabphcsAlmlineOscThresholdAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 49)
)
if mibBuilder.loadTexts:
    pmoabphcsAlmlineOscThresholdAlarmsTable.setStatus("current")
_PmoabphcsAlmlineOscThresholdAlarmsEntry_Object = MibTableRow
pmoabphcsAlmlineOscThresholdAlarmsEntry = _PmoabphcsAlmlineOscThresholdAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 49, 1)
)
pmoabphcsAlmlineOscThresholdAlarmsEntry.setIndexNames(
    (0, "EKINOPS-Pmoabphcs-MIB", "pmoabphcsAlmlineOscThresholdAlarmsIndex"),
)
if mibBuilder.loadTexts:
    pmoabphcsAlmlineOscThresholdAlarmsEntry.setStatus("current")


class _PmoabphcsAlmlineOscThresholdAlarmsIndex_Type(Integer32):
    """Custom type pmoabphcsAlmlineOscThresholdAlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmoabphcsAlmlineOscThresholdAlarmsIndex_Type.__name__ = "Integer32"
_PmoabphcsAlmlineOscThresholdAlarmsIndex_Object = MibTableColumn
pmoabphcsAlmlineOscThresholdAlarmsIndex = _PmoabphcsAlmlineOscThresholdAlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 49, 1, 1),
    _PmoabphcsAlmlineOscThresholdAlarmsIndex_Type()
)
pmoabphcsAlmlineOscThresholdAlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmlineOscThresholdAlarmsIndex.setStatus("current")
_PmoabphcsAlmLineTxPwrLowAlarmPortn_Type = EkiOnOff
_PmoabphcsAlmLineTxPwrLowAlarmPortn_Object = MibTableColumn
pmoabphcsAlmLineTxPwrLowAlarmPortn = _PmoabphcsAlmLineTxPwrLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 49, 1, 2),
    _PmoabphcsAlmLineTxPwrLowAlarmPortn_Type()
)
pmoabphcsAlmLineTxPwrLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineTxPwrLowAlarmPortn.setStatus("current")
_PmoabphcsAlmLineTxPwrHighAlarmPortn_Type = EkiOnOff
_PmoabphcsAlmLineTxPwrHighAlarmPortn_Object = MibTableColumn
pmoabphcsAlmLineTxPwrHighAlarmPortn = _PmoabphcsAlmLineTxPwrHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 49, 1, 3),
    _PmoabphcsAlmLineTxPwrHighAlarmPortn_Type()
)
pmoabphcsAlmLineTxPwrHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineTxPwrHighAlarmPortn.setStatus("current")
_PmoabphcsAlmLineRxPwrLowAlarmPortn_Type = EkiOnOff
_PmoabphcsAlmLineRxPwrLowAlarmPortn_Object = MibTableColumn
pmoabphcsAlmLineRxPwrLowAlarmPortn = _PmoabphcsAlmLineRxPwrLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 49, 1, 4),
    _PmoabphcsAlmLineRxPwrLowAlarmPortn_Type()
)
pmoabphcsAlmLineRxPwrLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineRxPwrLowAlarmPortn.setStatus("current")
_PmoabphcsAlmLineRxPwrHighAlarmPortn_Type = EkiOnOff
_PmoabphcsAlmLineRxPwrHighAlarmPortn_Object = MibTableColumn
pmoabphcsAlmLineRxPwrHighAlarmPortn = _PmoabphcsAlmLineRxPwrHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 49, 1, 5),
    _PmoabphcsAlmLineRxPwrHighAlarmPortn_Type()
)
pmoabphcsAlmLineRxPwrHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineRxPwrHighAlarmPortn.setStatus("current")
_PmoabphcsAlmLineSpanlossLowAlarmPortn_Type = EkiOnOff
_PmoabphcsAlmLineSpanlossLowAlarmPortn_Object = MibTableColumn
pmoabphcsAlmLineSpanlossLowAlarmPortn = _PmoabphcsAlmLineSpanlossLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 49, 1, 6),
    _PmoabphcsAlmLineSpanlossLowAlarmPortn_Type()
)
pmoabphcsAlmLineSpanlossLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineSpanlossLowAlarmPortn.setStatus("current")
_PmoabphcsAlmLineSpanlossHighAlarmPortn_Type = EkiOnOff
_PmoabphcsAlmLineSpanlossHighAlarmPortn_Object = MibTableColumn
pmoabphcsAlmLineSpanlossHighAlarmPortn = _PmoabphcsAlmLineSpanlossHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 49, 1, 7),
    _PmoabphcsAlmLineSpanlossHighAlarmPortn_Type()
)
pmoabphcsAlmLineSpanlossHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineSpanlossHighAlarmPortn.setStatus("current")
_PmoabphcsAlmLineOscBiasLowAlarmPortn_Type = EkiOnOff
_PmoabphcsAlmLineOscBiasLowAlarmPortn_Object = MibTableColumn
pmoabphcsAlmLineOscBiasLowAlarmPortn = _PmoabphcsAlmLineOscBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 49, 1, 8),
    _PmoabphcsAlmLineOscBiasLowAlarmPortn_Type()
)
pmoabphcsAlmLineOscBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineOscBiasLowAlarmPortn.setStatus("current")
_PmoabphcsAlmLineOscBiasHighAlarmPortn_Type = EkiOnOff
_PmoabphcsAlmLineOscBiasHighAlarmPortn_Object = MibTableColumn
pmoabphcsAlmLineOscBiasHighAlarmPortn = _PmoabphcsAlmLineOscBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 49, 1, 9),
    _PmoabphcsAlmLineOscBiasHighAlarmPortn_Type()
)
pmoabphcsAlmLineOscBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineOscBiasHighAlarmPortn.setStatus("current")
_PmoabphcsAlmlineOscThresholdsWarningsTable_Object = MibTable
pmoabphcsAlmlineOscThresholdsWarningsTable = _PmoabphcsAlmlineOscThresholdsWarningsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 50)
)
if mibBuilder.loadTexts:
    pmoabphcsAlmlineOscThresholdsWarningsTable.setStatus("current")
_PmoabphcsAlmlineOscThresholdsWarningsEntry_Object = MibTableRow
pmoabphcsAlmlineOscThresholdsWarningsEntry = _PmoabphcsAlmlineOscThresholdsWarningsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 50, 1)
)
pmoabphcsAlmlineOscThresholdsWarningsEntry.setIndexNames(
    (0, "EKINOPS-Pmoabphcs-MIB", "pmoabphcsAlmlineOscThresholdsWarningsIndex"),
)
if mibBuilder.loadTexts:
    pmoabphcsAlmlineOscThresholdsWarningsEntry.setStatus("current")


class _PmoabphcsAlmlineOscThresholdsWarningsIndex_Type(Integer32):
    """Custom type pmoabphcsAlmlineOscThresholdsWarningsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmoabphcsAlmlineOscThresholdsWarningsIndex_Type.__name__ = "Integer32"
_PmoabphcsAlmlineOscThresholdsWarningsIndex_Object = MibTableColumn
pmoabphcsAlmlineOscThresholdsWarningsIndex = _PmoabphcsAlmlineOscThresholdsWarningsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 50, 1, 1),
    _PmoabphcsAlmlineOscThresholdsWarningsIndex_Type()
)
pmoabphcsAlmlineOscThresholdsWarningsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmlineOscThresholdsWarningsIndex.setStatus("current")
_PmoabphcsAlmLineTxPwrLowWarningPortn_Type = EkiOnOff
_PmoabphcsAlmLineTxPwrLowWarningPortn_Object = MibTableColumn
pmoabphcsAlmLineTxPwrLowWarningPortn = _PmoabphcsAlmLineTxPwrLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 50, 1, 2),
    _PmoabphcsAlmLineTxPwrLowWarningPortn_Type()
)
pmoabphcsAlmLineTxPwrLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineTxPwrLowWarningPortn.setStatus("current")
_PmoabphcsAlmLineTxPwrHighWarningPortn_Type = EkiOnOff
_PmoabphcsAlmLineTxPwrHighWarningPortn_Object = MibTableColumn
pmoabphcsAlmLineTxPwrHighWarningPortn = _PmoabphcsAlmLineTxPwrHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 50, 1, 3),
    _PmoabphcsAlmLineTxPwrHighWarningPortn_Type()
)
pmoabphcsAlmLineTxPwrHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineTxPwrHighWarningPortn.setStatus("current")
_PmoabphcsAlmLineRxPwrLowWarningPortn_Type = EkiOnOff
_PmoabphcsAlmLineRxPwrLowWarningPortn_Object = MibTableColumn
pmoabphcsAlmLineRxPwrLowWarningPortn = _PmoabphcsAlmLineRxPwrLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 50, 1, 4),
    _PmoabphcsAlmLineRxPwrLowWarningPortn_Type()
)
pmoabphcsAlmLineRxPwrLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineRxPwrLowWarningPortn.setStatus("current")
_PmoabphcsAlmLineRxPwrHighWarningPortn_Type = EkiOnOff
_PmoabphcsAlmLineRxPwrHighWarningPortn_Object = MibTableColumn
pmoabphcsAlmLineRxPwrHighWarningPortn = _PmoabphcsAlmLineRxPwrHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 50, 1, 5),
    _PmoabphcsAlmLineRxPwrHighWarningPortn_Type()
)
pmoabphcsAlmLineRxPwrHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineRxPwrHighWarningPortn.setStatus("current")
_PmoabphcsAlmLineSpanlossLowWarningPortn_Type = EkiOnOff
_PmoabphcsAlmLineSpanlossLowWarningPortn_Object = MibTableColumn
pmoabphcsAlmLineSpanlossLowWarningPortn = _PmoabphcsAlmLineSpanlossLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 50, 1, 6),
    _PmoabphcsAlmLineSpanlossLowWarningPortn_Type()
)
pmoabphcsAlmLineSpanlossLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineSpanlossLowWarningPortn.setStatus("current")
_PmoabphcsAlmLineSpanlossHighWarningPortn_Type = EkiOnOff
_PmoabphcsAlmLineSpanlossHighWarningPortn_Object = MibTableColumn
pmoabphcsAlmLineSpanlossHighWarningPortn = _PmoabphcsAlmLineSpanlossHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 50, 1, 7),
    _PmoabphcsAlmLineSpanlossHighWarningPortn_Type()
)
pmoabphcsAlmLineSpanlossHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineSpanlossHighWarningPortn.setStatus("current")
_PmoabphcsAlmLineOscBiasLowWarningPortn_Type = EkiOnOff
_PmoabphcsAlmLineOscBiasLowWarningPortn_Object = MibTableColumn
pmoabphcsAlmLineOscBiasLowWarningPortn = _PmoabphcsAlmLineOscBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 50, 1, 8),
    _PmoabphcsAlmLineOscBiasLowWarningPortn_Type()
)
pmoabphcsAlmLineOscBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineOscBiasLowWarningPortn.setStatus("current")
_PmoabphcsAlmLineOscBiasHighWarningPortn_Type = EkiOnOff
_PmoabphcsAlmLineOscBiasHighWarningPortn_Object = MibTableColumn
pmoabphcsAlmLineOscBiasHighWarningPortn = _PmoabphcsAlmLineOscBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 2, 3, 3, 50, 1, 9),
    _PmoabphcsAlmLineOscBiasHighWarningPortn_Type()
)
pmoabphcsAlmLineOscBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsAlmLineOscBiasHighWarningPortn.setStatus("current")
_Pmoabphcsmeasures_ObjectIdentity = ObjectIdentity
pmoabphcsmeasures = _Pmoabphcsmeasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 3)
)
_PmoabphcsMesrOther_ObjectIdentity = ObjectIdentity
pmoabphcsMesrOther = _PmoabphcsMesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 3, 1)
)


class _PmoabphcsMesrtempMeas_Type(Integer32):
    """Custom type pmoabphcsMesrtempMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcsMesrtempMeas_Type.__name__ = "Integer32"
_PmoabphcsMesrtempMeas_Object = MibScalar
pmoabphcsMesrtempMeas = _PmoabphcsMesrtempMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 3, 1, 80),
    _PmoabphcsMesrtempMeas_Type()
)
pmoabphcsMesrtempMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsMesrtempMeas.setStatus("current")
_PmoabphcsMesrClient_ObjectIdentity = ObjectIdentity
pmoabphcsMesrClient = _PmoabphcsMesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 3, 2)
)


class _PmoabphcsMesrclientEdfaBiasMeas_Type(Integer32):
    """Custom type pmoabphcsMesrclientEdfaBiasMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcsMesrclientEdfaBiasMeas_Type.__name__ = "Integer32"
_PmoabphcsMesrclientEdfaBiasMeas_Object = MibScalar
pmoabphcsMesrclientEdfaBiasMeas = _PmoabphcsMesrclientEdfaBiasMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 3, 2, 32),
    _PmoabphcsMesrclientEdfaBiasMeas_Type()
)
pmoabphcsMesrclientEdfaBiasMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsMesrclientEdfaBiasMeas.setStatus("current")


class _PmoabphcsMesrclientEdfaTxpwrMeas_Type(Integer32):
    """Custom type pmoabphcsMesrclientEdfaTxpwrMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcsMesrclientEdfaTxpwrMeas_Type.__name__ = "Integer32"
_PmoabphcsMesrclientEdfaTxpwrMeas_Object = MibScalar
pmoabphcsMesrclientEdfaTxpwrMeas = _PmoabphcsMesrclientEdfaTxpwrMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 3, 2, 33),
    _PmoabphcsMesrclientEdfaTxpwrMeas_Type()
)
pmoabphcsMesrclientEdfaTxpwrMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsMesrclientEdfaTxpwrMeas.setStatus("current")


class _PmoabphcsMesrclientEdfaRxpwrMeas_Type(Integer32):
    """Custom type pmoabphcsMesrclientEdfaRxpwrMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcsMesrclientEdfaRxpwrMeas_Type.__name__ = "Integer32"
_PmoabphcsMesrclientEdfaRxpwrMeas_Object = MibScalar
pmoabphcsMesrclientEdfaRxpwrMeas = _PmoabphcsMesrclientEdfaRxpwrMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 3, 2, 34),
    _PmoabphcsMesrclientEdfaRxpwrMeas_Type()
)
pmoabphcsMesrclientEdfaRxpwrMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsMesrclientEdfaRxpwrMeas.setStatus("current")


class _PmoabphcsMesrclientEdfaGainMeas_Type(Integer32):
    """Custom type pmoabphcsMesrclientEdfaGainMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcsMesrclientEdfaGainMeas_Type.__name__ = "Integer32"
_PmoabphcsMesrclientEdfaGainMeas_Object = MibScalar
pmoabphcsMesrclientEdfaGainMeas = _PmoabphcsMesrclientEdfaGainMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 3, 2, 35),
    _PmoabphcsMesrclientEdfaGainMeas_Type()
)
pmoabphcsMesrclientEdfaGainMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsMesrclientEdfaGainMeas.setStatus("current")


class _PmoabphcsMesrclientOscSpanLoss_Type(Integer32):
    """Custom type pmoabphcsMesrclientOscSpanLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcsMesrclientOscSpanLoss_Type.__name__ = "Integer32"
_PmoabphcsMesrclientOscSpanLoss_Object = MibScalar
pmoabphcsMesrclientOscSpanLoss = _PmoabphcsMesrclientOscSpanLoss_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 3, 2, 36),
    _PmoabphcsMesrclientOscSpanLoss_Type()
)
pmoabphcsMesrclientOscSpanLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsMesrclientOscSpanLoss.setStatus("current")


class _PmoabphcsMesrclientOscSpanLossRef_Type(Integer32):
    """Custom type pmoabphcsMesrclientOscSpanLossRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcsMesrclientOscSpanLossRef_Type.__name__ = "Integer32"
_PmoabphcsMesrclientOscSpanLossRef_Object = MibScalar
pmoabphcsMesrclientOscSpanLossRef = _PmoabphcsMesrclientOscSpanLossRef_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 3, 2, 37),
    _PmoabphcsMesrclientOscSpanLossRef_Type()
)
pmoabphcsMesrclientOscSpanLossRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsMesrclientOscSpanLossRef.setStatus("current")


class _PmoabphcsMesrclientCorrectedGain_Type(Integer32):
    """Custom type pmoabphcsMesrclientCorrectedGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcsMesrclientCorrectedGain_Type.__name__ = "Integer32"
_PmoabphcsMesrclientCorrectedGain_Object = MibScalar
pmoabphcsMesrclientCorrectedGain = _PmoabphcsMesrclientCorrectedGain_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 3, 2, 38),
    _PmoabphcsMesrclientCorrectedGain_Type()
)
pmoabphcsMesrclientCorrectedGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsMesrclientCorrectedGain.setStatus("current")


class _PmoabphcsMesrclientMsaInputPower_Type(Integer32):
    """Custom type pmoabphcsMesrclientMsaInputPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcsMesrclientMsaInputPower_Type.__name__ = "Integer32"
_PmoabphcsMesrclientMsaInputPower_Object = MibScalar
pmoabphcsMesrclientMsaInputPower = _PmoabphcsMesrclientMsaInputPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 3, 2, 39),
    _PmoabphcsMesrclientMsaInputPower_Type()
)
pmoabphcsMesrclientMsaInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsMesrclientMsaInputPower.setStatus("current")


class _PmoabphcsMesrclientMsaOutputPower_Type(Integer32):
    """Custom type pmoabphcsMesrclientMsaOutputPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcsMesrclientMsaOutputPower_Type.__name__ = "Integer32"
_PmoabphcsMesrclientMsaOutputPower_Object = MibScalar
pmoabphcsMesrclientMsaOutputPower = _PmoabphcsMesrclientMsaOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 3, 2, 40),
    _PmoabphcsMesrclientMsaOutputPower_Type()
)
pmoabphcsMesrclientMsaOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsMesrclientMsaOutputPower.setStatus("current")


class _PmoabphcsMesrclientMsaAttenuation_Type(Integer32):
    """Custom type pmoabphcsMesrclientMsaAttenuation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcsMesrclientMsaAttenuation_Type.__name__ = "Integer32"
_PmoabphcsMesrclientMsaAttenuation_Object = MibScalar
pmoabphcsMesrclientMsaAttenuation = _PmoabphcsMesrclientMsaAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 3, 2, 41),
    _PmoabphcsMesrclientMsaAttenuation_Type()
)
pmoabphcsMesrclientMsaAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsMesrclientMsaAttenuation.setStatus("current")


class _PmoabphcsMesrclientMsaAttenuationRef_Type(Integer32):
    """Custom type pmoabphcsMesrclientMsaAttenuationRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcsMesrclientMsaAttenuationRef_Type.__name__ = "Integer32"
_PmoabphcsMesrclientMsaAttenuationRef_Object = MibScalar
pmoabphcsMesrclientMsaAttenuationRef = _PmoabphcsMesrclientMsaAttenuationRef_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 3, 2, 42),
    _PmoabphcsMesrclientMsaAttenuationRef_Type()
)
pmoabphcsMesrclientMsaAttenuationRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsMesrclientMsaAttenuationRef.setStatus("current")
_PmoabphcsMesrLine_ObjectIdentity = ObjectIdentity
pmoabphcsMesrLine = _PmoabphcsMesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 3, 3)
)


class _PmoabphcsMesrlineEdfaBiasMeas_Type(Integer32):
    """Custom type pmoabphcsMesrlineEdfaBiasMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcsMesrlineEdfaBiasMeas_Type.__name__ = "Integer32"
_PmoabphcsMesrlineEdfaBiasMeas_Object = MibScalar
pmoabphcsMesrlineEdfaBiasMeas = _PmoabphcsMesrlineEdfaBiasMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 3, 3, 48),
    _PmoabphcsMesrlineEdfaBiasMeas_Type()
)
pmoabphcsMesrlineEdfaBiasMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsMesrlineEdfaBiasMeas.setStatus("current")


class _PmoabphcsMesrlineEdfaTxpwrMeas_Type(Integer32):
    """Custom type pmoabphcsMesrlineEdfaTxpwrMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcsMesrlineEdfaTxpwrMeas_Type.__name__ = "Integer32"
_PmoabphcsMesrlineEdfaTxpwrMeas_Object = MibScalar
pmoabphcsMesrlineEdfaTxpwrMeas = _PmoabphcsMesrlineEdfaTxpwrMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 3, 3, 49),
    _PmoabphcsMesrlineEdfaTxpwrMeas_Type()
)
pmoabphcsMesrlineEdfaTxpwrMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsMesrlineEdfaTxpwrMeas.setStatus("current")


class _PmoabphcsMesrlineEdfaRxpwrMeas_Type(Integer32):
    """Custom type pmoabphcsMesrlineEdfaRxpwrMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcsMesrlineEdfaRxpwrMeas_Type.__name__ = "Integer32"
_PmoabphcsMesrlineEdfaRxpwrMeas_Object = MibScalar
pmoabphcsMesrlineEdfaRxpwrMeas = _PmoabphcsMesrlineEdfaRxpwrMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 3, 3, 50),
    _PmoabphcsMesrlineEdfaRxpwrMeas_Type()
)
pmoabphcsMesrlineEdfaRxpwrMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsMesrlineEdfaRxpwrMeas.setStatus("current")


class _PmoabphcsMesrlineEdfaGainMeas_Type(Integer32):
    """Custom type pmoabphcsMesrlineEdfaGainMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcsMesrlineEdfaGainMeas_Type.__name__ = "Integer32"
_PmoabphcsMesrlineEdfaGainMeas_Object = MibScalar
pmoabphcsMesrlineEdfaGainMeas = _PmoabphcsMesrlineEdfaGainMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 3, 3, 51),
    _PmoabphcsMesrlineEdfaGainMeas_Type()
)
pmoabphcsMesrlineEdfaGainMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsMesrlineEdfaGainMeas.setStatus("current")


class _PmoabphcsMesrlineOscSpanLoss_Type(Integer32):
    """Custom type pmoabphcsMesrlineOscSpanLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcsMesrlineOscSpanLoss_Type.__name__ = "Integer32"
_PmoabphcsMesrlineOscSpanLoss_Object = MibScalar
pmoabphcsMesrlineOscSpanLoss = _PmoabphcsMesrlineOscSpanLoss_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 3, 3, 52),
    _PmoabphcsMesrlineOscSpanLoss_Type()
)
pmoabphcsMesrlineOscSpanLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsMesrlineOscSpanLoss.setStatus("current")


class _PmoabphcsMesrlineOscSpanLossRef_Type(Integer32):
    """Custom type pmoabphcsMesrlineOscSpanLossRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcsMesrlineOscSpanLossRef_Type.__name__ = "Integer32"
_PmoabphcsMesrlineOscSpanLossRef_Object = MibScalar
pmoabphcsMesrlineOscSpanLossRef = _PmoabphcsMesrlineOscSpanLossRef_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 3, 3, 53),
    _PmoabphcsMesrlineOscSpanLossRef_Type()
)
pmoabphcsMesrlineOscSpanLossRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsMesrlineOscSpanLossRef.setStatus("current")


class _PmoabphcsMesrlineCorrectedGain_Type(Integer32):
    """Custom type pmoabphcsMesrlineCorrectedGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcsMesrlineCorrectedGain_Type.__name__ = "Integer32"
_PmoabphcsMesrlineCorrectedGain_Object = MibScalar
pmoabphcsMesrlineCorrectedGain = _PmoabphcsMesrlineCorrectedGain_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 3, 3, 54),
    _PmoabphcsMesrlineCorrectedGain_Type()
)
pmoabphcsMesrlineCorrectedGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsMesrlineCorrectedGain.setStatus("current")


class _PmoabphcsMesrlineMsaInputPower_Type(Integer32):
    """Custom type pmoabphcsMesrlineMsaInputPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcsMesrlineMsaInputPower_Type.__name__ = "Integer32"
_PmoabphcsMesrlineMsaInputPower_Object = MibScalar
pmoabphcsMesrlineMsaInputPower = _PmoabphcsMesrlineMsaInputPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 3, 3, 55),
    _PmoabphcsMesrlineMsaInputPower_Type()
)
pmoabphcsMesrlineMsaInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsMesrlineMsaInputPower.setStatus("current")


class _PmoabphcsMesrlineMsaOutputPower_Type(Integer32):
    """Custom type pmoabphcsMesrlineMsaOutputPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcsMesrlineMsaOutputPower_Type.__name__ = "Integer32"
_PmoabphcsMesrlineMsaOutputPower_Object = MibScalar
pmoabphcsMesrlineMsaOutputPower = _PmoabphcsMesrlineMsaOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 3, 3, 56),
    _PmoabphcsMesrlineMsaOutputPower_Type()
)
pmoabphcsMesrlineMsaOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsMesrlineMsaOutputPower.setStatus("current")


class _PmoabphcsMesrlineMsaAttenuation_Type(Integer32):
    """Custom type pmoabphcsMesrlineMsaAttenuation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcsMesrlineMsaAttenuation_Type.__name__ = "Integer32"
_PmoabphcsMesrlineMsaAttenuation_Object = MibScalar
pmoabphcsMesrlineMsaAttenuation = _PmoabphcsMesrlineMsaAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 3, 3, 57),
    _PmoabphcsMesrlineMsaAttenuation_Type()
)
pmoabphcsMesrlineMsaAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsMesrlineMsaAttenuation.setStatus("current")


class _PmoabphcsMesrlineMsaAttenuationRef_Type(Integer32):
    """Custom type pmoabphcsMesrlineMsaAttenuationRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcsMesrlineMsaAttenuationRef_Type.__name__ = "Integer32"
_PmoabphcsMesrlineMsaAttenuationRef_Object = MibScalar
pmoabphcsMesrlineMsaAttenuationRef = _PmoabphcsMesrlineMsaAttenuationRef_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 3, 3, 58),
    _PmoabphcsMesrlineMsaAttenuationRef_Type()
)
pmoabphcsMesrlineMsaAttenuationRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsMesrlineMsaAttenuationRef.setStatus("current")
_PmoabphcsMesrlineOscTxPowerTable_Object = MibTable
pmoabphcsMesrlineOscTxPowerTable = _PmoabphcsMesrlineOscTxPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 3, 3, 64)
)
if mibBuilder.loadTexts:
    pmoabphcsMesrlineOscTxPowerTable.setStatus("current")
_PmoabphcsMesrlineOscTxPowerEntry_Object = MibTableRow
pmoabphcsMesrlineOscTxPowerEntry = _PmoabphcsMesrlineOscTxPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 3, 3, 64, 1)
)
pmoabphcsMesrlineOscTxPowerEntry.setIndexNames(
    (0, "EKINOPS-Pmoabphcs-MIB", "pmoabphcsMesrlineOscTxPowerIndex"),
)
if mibBuilder.loadTexts:
    pmoabphcsMesrlineOscTxPowerEntry.setStatus("current")


class _PmoabphcsMesrlineOscTxPowerIndex_Type(Integer32):
    """Custom type pmoabphcsMesrlineOscTxPowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmoabphcsMesrlineOscTxPowerIndex_Type.__name__ = "Integer32"
_PmoabphcsMesrlineOscTxPowerIndex_Object = MibTableColumn
pmoabphcsMesrlineOscTxPowerIndex = _PmoabphcsMesrlineOscTxPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 3, 3, 64, 1, 1),
    _PmoabphcsMesrlineOscTxPowerIndex_Type()
)
pmoabphcsMesrlineOscTxPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsMesrlineOscTxPowerIndex.setStatus("current")


class _PmoabphcsMesrlineOscTxPowerPortn_Type(Integer32):
    """Custom type pmoabphcsMesrlineOscTxPowerPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcsMesrlineOscTxPowerPortn_Type.__name__ = "Integer32"
_PmoabphcsMesrlineOscTxPowerPortn_Object = MibTableColumn
pmoabphcsMesrlineOscTxPowerPortn = _PmoabphcsMesrlineOscTxPowerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 3, 3, 64, 1, 2),
    _PmoabphcsMesrlineOscTxPowerPortn_Type()
)
pmoabphcsMesrlineOscTxPowerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsMesrlineOscTxPowerPortn.setStatus("current")
_PmoabphcsMesrlineOscRxPowerTable_Object = MibTable
pmoabphcsMesrlineOscRxPowerTable = _PmoabphcsMesrlineOscRxPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 3, 3, 65)
)
if mibBuilder.loadTexts:
    pmoabphcsMesrlineOscRxPowerTable.setStatus("current")
_PmoabphcsMesrlineOscRxPowerEntry_Object = MibTableRow
pmoabphcsMesrlineOscRxPowerEntry = _PmoabphcsMesrlineOscRxPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 3, 3, 65, 1)
)
pmoabphcsMesrlineOscRxPowerEntry.setIndexNames(
    (0, "EKINOPS-Pmoabphcs-MIB", "pmoabphcsMesrlineOscRxPowerIndex"),
)
if mibBuilder.loadTexts:
    pmoabphcsMesrlineOscRxPowerEntry.setStatus("current")


class _PmoabphcsMesrlineOscRxPowerIndex_Type(Integer32):
    """Custom type pmoabphcsMesrlineOscRxPowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmoabphcsMesrlineOscRxPowerIndex_Type.__name__ = "Integer32"
_PmoabphcsMesrlineOscRxPowerIndex_Object = MibTableColumn
pmoabphcsMesrlineOscRxPowerIndex = _PmoabphcsMesrlineOscRxPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 3, 3, 65, 1, 1),
    _PmoabphcsMesrlineOscRxPowerIndex_Type()
)
pmoabphcsMesrlineOscRxPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsMesrlineOscRxPowerIndex.setStatus("current")


class _PmoabphcsMesrlineOscRxPowerPortn_Type(Integer32):
    """Custom type pmoabphcsMesrlineOscRxPowerPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcsMesrlineOscRxPowerPortn_Type.__name__ = "Integer32"
_PmoabphcsMesrlineOscRxPowerPortn_Object = MibTableColumn
pmoabphcsMesrlineOscRxPowerPortn = _PmoabphcsMesrlineOscRxPowerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 3, 3, 65, 1, 2),
    _PmoabphcsMesrlineOscRxPowerPortn_Type()
)
pmoabphcsMesrlineOscRxPowerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsMesrlineOscRxPowerPortn.setStatus("current")
_Pmoabphcscounters_ObjectIdentity = ObjectIdentity
pmoabphcscounters = _Pmoabphcscounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 4)
)
_PmoabphcsCntOther_ObjectIdentity = ObjectIdentity
pmoabphcsCntOther = _PmoabphcsCntOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 4, 1)
)
_PmoabphcsCntClient_ObjectIdentity = ObjectIdentity
pmoabphcsCntClient = _PmoabphcsCntClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 4, 2)
)
_PmoabphcsCntLine_ObjectIdentity = ObjectIdentity
pmoabphcsCntLine = _PmoabphcsCntLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 4, 3)
)
_PmoabphcsCntlineOscErrTable_Object = MibTable
pmoabphcsCntlineOscErrTable = _PmoabphcsCntlineOscErrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 4, 3, 16)
)
if mibBuilder.loadTexts:
    pmoabphcsCntlineOscErrTable.setStatus("current")
_PmoabphcsCntlineOscErrEntry_Object = MibTableRow
pmoabphcsCntlineOscErrEntry = _PmoabphcsCntlineOscErrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 4, 3, 16, 1)
)
pmoabphcsCntlineOscErrEntry.setIndexNames(
    (0, "EKINOPS-Pmoabphcs-MIB", "pmoabphcsCntlineOscErrIndex"),
)
if mibBuilder.loadTexts:
    pmoabphcsCntlineOscErrEntry.setStatus("current")


class _PmoabphcsCntlineOscErrIndex_Type(Integer32):
    """Custom type pmoabphcsCntlineOscErrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmoabphcsCntlineOscErrIndex_Type.__name__ = "Integer32"
_PmoabphcsCntlineOscErrIndex_Object = MibTableColumn
pmoabphcsCntlineOscErrIndex = _PmoabphcsCntlineOscErrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 4, 3, 16, 1, 1),
    _PmoabphcsCntlineOscErrIndex_Type()
)
pmoabphcsCntlineOscErrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsCntlineOscErrIndex.setStatus("current")
_PmoabphcsCntlineOscErrValuePortn_Type = Counter32
_PmoabphcsCntlineOscErrValuePortn_Object = MibTableColumn
pmoabphcsCntlineOscErrValuePortn = _PmoabphcsCntlineOscErrValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 4, 3, 16, 1, 2),
    _PmoabphcsCntlineOscErrValuePortn_Type()
)
pmoabphcsCntlineOscErrValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsCntlineOscErrValuePortn.setStatus("current")
_PmoabphcsCntlineOscErrErrorPortn_Type = EkiOnOff
_PmoabphcsCntlineOscErrErrorPortn_Object = MibTableColumn
pmoabphcsCntlineOscErrErrorPortn = _PmoabphcsCntlineOscErrErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 4, 3, 16, 1, 3),
    _PmoabphcsCntlineOscErrErrorPortn_Type()
)
pmoabphcsCntlineOscErrErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsCntlineOscErrErrorPortn.setStatus("current")
_PmoabphcsCntlineOscErrOverloadPortn_Type = EkiOnOff
_PmoabphcsCntlineOscErrOverloadPortn_Object = MibTableColumn
pmoabphcsCntlineOscErrOverloadPortn = _PmoabphcsCntlineOscErrOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 4, 3, 16, 1, 4),
    _PmoabphcsCntlineOscErrOverloadPortn_Type()
)
pmoabphcsCntlineOscErrOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsCntlineOscErrOverloadPortn.setStatus("current")
_PmoabphcsCntCountersReset_Type = EkiOnOff
_PmoabphcsCntCountersReset_Object = MibScalar
pmoabphcsCntCountersReset = _PmoabphcsCntCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 4, 259),
    _PmoabphcsCntCountersReset_Type()
)
pmoabphcsCntCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCntCountersReset.setStatus("current")
_PmoabphcsCntCountersStop_Type = EkiOnOff
_PmoabphcsCntCountersStop_Object = MibScalar
pmoabphcsCntCountersStop = _PmoabphcsCntCountersStop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 4, 260),
    _PmoabphcsCntCountersStop_Type()
)
pmoabphcsCntCountersStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCntCountersStop.setStatus("current")
_PmoabphcscontrolsWrite_ObjectIdentity = ObjectIdentity
pmoabphcscontrolsWrite = _PmoabphcscontrolsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 6)
)
_PmoabphcsCtrlOther_ObjectIdentity = ObjectIdentity
pmoabphcsCtrlOther = _PmoabphcsCtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 6, 1)
)
_PmoabphcsCtrlsynth0_ObjectIdentity = ObjectIdentity
pmoabphcsCtrlsynth0 = _PmoabphcsCtrlsynth0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 6, 1, 0)
)
_PmoabphcsCtrlConfLoad_Type = EkiOnOff
_PmoabphcsCtrlConfLoad_Object = MibScalar
pmoabphcsCtrlConfLoad = _PmoabphcsCtrlConfLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 6, 1, 0, 1),
    _PmoabphcsCtrlConfLoad_Type()
)
pmoabphcsCtrlConfLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCtrlConfLoad.setStatus("current")
_PmoabphcsCtrlConfFlash_Type = EkiOnOff
_PmoabphcsCtrlConfFlash_Object = MibScalar
pmoabphcsCtrlConfFlash = _PmoabphcsCtrlConfFlash_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 6, 1, 0, 9),
    _PmoabphcsCtrlConfFlash_Type()
)
pmoabphcsCtrlConfFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCtrlConfFlash.setStatus("current")
_PmoabphcsCtrlConfClear_Type = EkiOnOff
_PmoabphcsCtrlConfClear_Object = MibScalar
pmoabphcsCtrlConfClear = _PmoabphcsCtrlConfClear_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 6, 1, 0, 13),
    _PmoabphcsCtrlConfClear_Type()
)
pmoabphcsCtrlConfClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCtrlConfClear.setStatus("current")
_PmoabphcsCtrlswMgnt_ObjectIdentity = ObjectIdentity
pmoabphcsCtrlswMgnt = _PmoabphcsCtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 6, 1, 5)
)
_PmoabphcsCtrlColdReset_Type = EkiOnOff
_PmoabphcsCtrlColdReset_Object = MibScalar
pmoabphcsCtrlColdReset = _PmoabphcsCtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 6, 1, 5, 2),
    _PmoabphcsCtrlColdReset_Type()
)
pmoabphcsCtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCtrlColdReset.setStatus("current")
_PmoabphcsCtrlWarmReset_Type = EkiOnOff
_PmoabphcsCtrlWarmReset_Object = MibScalar
pmoabphcsCtrlWarmReset = _PmoabphcsCtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 6, 1, 5, 3),
    _PmoabphcsCtrlWarmReset_Type()
)
pmoabphcsCtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCtrlWarmReset.setStatus("current")
_PmoabphcsCtrlledTest_ObjectIdentity = ObjectIdentity
pmoabphcsCtrlledTest = _PmoabphcsCtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 6, 1, 73)
)
_PmoabphcsCtrlGreenLed_Type = EkiOnOff
_PmoabphcsCtrlGreenLed_Object = MibScalar
pmoabphcsCtrlGreenLed = _PmoabphcsCtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 6, 1, 73, 1),
    _PmoabphcsCtrlGreenLed_Type()
)
pmoabphcsCtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCtrlGreenLed.setStatus("current")
_PmoabphcsCtrlRedLed_Type = EkiOnOff
_PmoabphcsCtrlRedLed_Object = MibScalar
pmoabphcsCtrlRedLed = _PmoabphcsCtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 6, 1, 73, 2),
    _PmoabphcsCtrlRedLed_Type()
)
pmoabphcsCtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCtrlRedLed.setStatus("current")
_PmoabphcsCtrlLedOff_Type = EkiOnOff
_PmoabphcsCtrlLedOff_Object = MibScalar
pmoabphcsCtrlLedOff = _PmoabphcsCtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 6, 1, 73, 3),
    _PmoabphcsCtrlLedOff_Type()
)
pmoabphcsCtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCtrlLedOff.setStatus("current")
_PmoabphcsCtrlmaintMode_ObjectIdentity = ObjectIdentity
pmoabphcsCtrlmaintMode = _PmoabphcsCtrlmaintMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 6, 1, 75)
)
_PmoabphcsCtrlMaintenance_Type = EkiOnOff
_PmoabphcsCtrlMaintenance_Object = MibScalar
pmoabphcsCtrlMaintenance = _PmoabphcsCtrlMaintenance_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 6, 1, 75, 1),
    _PmoabphcsCtrlMaintenance_Type()
)
pmoabphcsCtrlMaintenance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCtrlMaintenance.setStatus("current")
_PmoabphcsCtrlaprRestart_ObjectIdentity = ObjectIdentity
pmoabphcsCtrlaprRestart = _PmoabphcsCtrlaprRestart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 6, 1, 76)
)
_PmoabphcsCtrlAprManualRestart_Type = EkiOnOff
_PmoabphcsCtrlAprManualRestart_Object = MibScalar
pmoabphcsCtrlAprManualRestart = _PmoabphcsCtrlAprManualRestart_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 6, 1, 76, 1),
    _PmoabphcsCtrlAprManualRestart_Type()
)
pmoabphcsCtrlAprManualRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCtrlAprManualRestart.setStatus("current")
_PmoabphcsCtrlClient_ObjectIdentity = ObjectIdentity
pmoabphcsCtrlClient = _PmoabphcsCtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 6, 2)
)
_PmoabphcsCtrlclientOscInputSpanLoss_ObjectIdentity = ObjectIdentity
pmoabphcsCtrlclientOscInputSpanLoss = _PmoabphcsCtrlclientOscInputSpanLoss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 6, 2, 33)
)
_PmoabphcsCtrlClientSpanLoss_Type = EkiOnOff
_PmoabphcsCtrlClientSpanLoss_Object = MibScalar
pmoabphcsCtrlClientSpanLoss = _PmoabphcsCtrlClientSpanLoss_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 6, 2, 33, 1),
    _PmoabphcsCtrlClientSpanLoss_Type()
)
pmoabphcsCtrlClientSpanLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCtrlClientSpanLoss.setStatus("current")


class _PmoabphcsCtrlclientGainCstMonitorValue_Type(Integer32):
    """Custom type pmoabphcsCtrlclientGainCstMonitorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcsCtrlclientGainCstMonitorValue_Type.__name__ = "Integer32"
_PmoabphcsCtrlclientGainCstMonitorValue_Object = MibScalar
pmoabphcsCtrlclientGainCstMonitorValue = _PmoabphcsCtrlclientGainCstMonitorValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 6, 2, 34),
    _PmoabphcsCtrlclientGainCstMonitorValue_Type()
)
pmoabphcsCtrlclientGainCstMonitorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCtrlclientGainCstMonitorValue.setStatus("current")


class _PmoabphcsCtrlclientGainSettingValue_Type(Integer32):
    """Custom type pmoabphcsCtrlclientGainSettingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcsCtrlclientGainSettingValue_Type.__name__ = "Integer32"
_PmoabphcsCtrlclientGainSettingValue_Object = MibScalar
pmoabphcsCtrlclientGainSettingValue = _PmoabphcsCtrlclientGainSettingValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 6, 2, 36),
    _PmoabphcsCtrlclientGainSettingValue_Type()
)
pmoabphcsCtrlclientGainSettingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCtrlclientGainSettingValue.setStatus("current")
_PmoabphcsCtrlclientGainProcessing_ObjectIdentity = ObjectIdentity
pmoabphcsCtrlclientGainProcessing = _PmoabphcsCtrlclientGainProcessing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 6, 2, 37)
)
_PmoabphcsCtrlClientGainProc_Type = EkiOnOff
_PmoabphcsCtrlClientGainProc_Object = MibScalar
pmoabphcsCtrlClientGainProc = _PmoabphcsCtrlClientGainProc_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 6, 2, 37, 1),
    _PmoabphcsCtrlClientGainProc_Type()
)
pmoabphcsCtrlClientGainProc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCtrlClientGainProc.setStatus("current")


class _PmoabphcsCtrlclientGainCstFiberAgingMarginValue_Type(Integer32):
    """Custom type pmoabphcsCtrlclientGainCstFiberAgingMarginValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcsCtrlclientGainCstFiberAgingMarginValue_Type.__name__ = "Integer32"
_PmoabphcsCtrlclientGainCstFiberAgingMarginValue_Object = MibScalar
pmoabphcsCtrlclientGainCstFiberAgingMarginValue = _PmoabphcsCtrlclientGainCstFiberAgingMarginValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 6, 2, 38),
    _PmoabphcsCtrlclientGainCstFiberAgingMarginValue_Type()
)
pmoabphcsCtrlclientGainCstFiberAgingMarginValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCtrlclientGainCstFiberAgingMarginValue.setStatus("current")
_PmoabphcsCtrlclientMsaAttenuationValue_ObjectIdentity = ObjectIdentity
pmoabphcsCtrlclientMsaAttenuationValue = _PmoabphcsCtrlclientMsaAttenuationValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 6, 2, 40)
)
_PmoabphcsCtrlClientAttenuation_Type = EkiOnOff
_PmoabphcsCtrlClientAttenuation_Object = MibScalar
pmoabphcsCtrlClientAttenuation = _PmoabphcsCtrlClientAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 6, 2, 40, 1),
    _PmoabphcsCtrlClientAttenuation_Type()
)
pmoabphcsCtrlClientAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCtrlClientAttenuation.setStatus("current")
_PmoabphcsCtrlLine_ObjectIdentity = ObjectIdentity
pmoabphcsCtrlLine = _PmoabphcsCtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 6, 3)
)
_PmoabphcsCtrllineOscInputSpanLoss_ObjectIdentity = ObjectIdentity
pmoabphcsCtrllineOscInputSpanLoss = _PmoabphcsCtrllineOscInputSpanLoss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 6, 3, 49)
)
_PmoabphcsCtrlLineSpanLoss_Type = EkiOnOff
_PmoabphcsCtrlLineSpanLoss_Object = MibScalar
pmoabphcsCtrlLineSpanLoss = _PmoabphcsCtrlLineSpanLoss_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 6, 3, 49, 1),
    _PmoabphcsCtrlLineSpanLoss_Type()
)
pmoabphcsCtrlLineSpanLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCtrlLineSpanLoss.setStatus("current")


class _PmoabphcsCtrllineGainCstMonitorValue_Type(Integer32):
    """Custom type pmoabphcsCtrllineGainCstMonitorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcsCtrllineGainCstMonitorValue_Type.__name__ = "Integer32"
_PmoabphcsCtrllineGainCstMonitorValue_Object = MibScalar
pmoabphcsCtrllineGainCstMonitorValue = _PmoabphcsCtrllineGainCstMonitorValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 6, 3, 50),
    _PmoabphcsCtrllineGainCstMonitorValue_Type()
)
pmoabphcsCtrllineGainCstMonitorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCtrllineGainCstMonitorValue.setStatus("current")


class _PmoabphcsCtrllineGainSettingValue_Type(Integer32):
    """Custom type pmoabphcsCtrllineGainSettingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcsCtrllineGainSettingValue_Type.__name__ = "Integer32"
_PmoabphcsCtrllineGainSettingValue_Object = MibScalar
pmoabphcsCtrllineGainSettingValue = _PmoabphcsCtrllineGainSettingValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 6, 3, 52),
    _PmoabphcsCtrllineGainSettingValue_Type()
)
pmoabphcsCtrllineGainSettingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCtrllineGainSettingValue.setStatus("current")
_PmoabphcsCtrllineGainProcessing_ObjectIdentity = ObjectIdentity
pmoabphcsCtrllineGainProcessing = _PmoabphcsCtrllineGainProcessing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 6, 3, 53)
)
_PmoabphcsCtrlLineGainProc_Type = EkiOnOff
_PmoabphcsCtrlLineGainProc_Object = MibScalar
pmoabphcsCtrlLineGainProc = _PmoabphcsCtrlLineGainProc_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 6, 3, 53, 1),
    _PmoabphcsCtrlLineGainProc_Type()
)
pmoabphcsCtrlLineGainProc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCtrlLineGainProc.setStatus("current")


class _PmoabphcsCtrllineGainCstFiberAgingMarginValue_Type(Integer32):
    """Custom type pmoabphcsCtrllineGainCstFiberAgingMarginValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcsCtrllineGainCstFiberAgingMarginValue_Type.__name__ = "Integer32"
_PmoabphcsCtrllineGainCstFiberAgingMarginValue_Object = MibScalar
pmoabphcsCtrllineGainCstFiberAgingMarginValue = _PmoabphcsCtrllineGainCstFiberAgingMarginValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 6, 3, 54),
    _PmoabphcsCtrllineGainCstFiberAgingMarginValue_Type()
)
pmoabphcsCtrllineGainCstFiberAgingMarginValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCtrllineGainCstFiberAgingMarginValue.setStatus("current")
_PmoabphcsCtrllineMsaAttenuationValue_ObjectIdentity = ObjectIdentity
pmoabphcsCtrllineMsaAttenuationValue = _PmoabphcsCtrllineMsaAttenuationValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 6, 3, 56)
)
_PmoabphcsCtrlLineAttenuation_Type = EkiOnOff
_PmoabphcsCtrlLineAttenuation_Object = MibScalar
pmoabphcsCtrlLineAttenuation = _PmoabphcsCtrlLineAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 6, 3, 56, 1),
    _PmoabphcsCtrlLineAttenuation_Type()
)
pmoabphcsCtrlLineAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCtrlLineAttenuation.setStatus("current")
_Pmoabphcsri_ObjectIdentity = ObjectIdentity
pmoabphcsri = _Pmoabphcsri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 7)
)
_PmoabphcsRinvReloadInventory_Type = EkiOnOff
_PmoabphcsRinvReloadInventory_Object = MibScalar
pmoabphcsRinvReloadInventory = _PmoabphcsRinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 7, 2),
    _PmoabphcsRinvReloadInventory_Type()
)
pmoabphcsRinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsRinvReloadInventory.setStatus("current")
_PmoabphcsRinvHwPlatform_Type = DisplayString
_PmoabphcsRinvHwPlatform_Object = MibScalar
pmoabphcsRinvHwPlatform = _PmoabphcsRinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 7, 3),
    _PmoabphcsRinvHwPlatform_Type()
)
pmoabphcsRinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsRinvHwPlatform.setStatus("current")
_PmoabphcsRinvModulePlatform_Type = DisplayString
_PmoabphcsRinvModulePlatform_Object = MibScalar
pmoabphcsRinvModulePlatform = _PmoabphcsRinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 7, 4),
    _PmoabphcsRinvModulePlatform_Type()
)
pmoabphcsRinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsRinvModulePlatform.setStatus("current")
_PmoabphcsRinvSwPlatform_Type = DisplayString
_PmoabphcsRinvSwPlatform_Object = MibScalar
pmoabphcsRinvSwPlatform = _PmoabphcsRinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 7, 5),
    _PmoabphcsRinvSwPlatform_Type()
)
pmoabphcsRinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsRinvSwPlatform.setStatus("current")
_PmoabphcsRinvGwPlatform_Type = DisplayString
_PmoabphcsRinvGwPlatform_Object = MibScalar
pmoabphcsRinvGwPlatform = _PmoabphcsRinvGwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 7, 6),
    _PmoabphcsRinvGwPlatform_Type()
)
pmoabphcsRinvGwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsRinvGwPlatform.setStatus("current")
_PmoabphcsRinvBoosterTable_Object = MibTable
pmoabphcsRinvBoosterTable = _PmoabphcsRinvBoosterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 7, 7)
)
if mibBuilder.loadTexts:
    pmoabphcsRinvBoosterTable.setStatus("current")
_PmoabphcsRinvBoosterEntry_Object = MibTableRow
pmoabphcsRinvBoosterEntry = _PmoabphcsRinvBoosterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 7, 7, 1)
)
pmoabphcsRinvBoosterEntry.setIndexNames(
    (0, "EKINOPS-Pmoabphcs-MIB", "pmoabphcsRinvBoosterIndex"),
)
if mibBuilder.loadTexts:
    pmoabphcsRinvBoosterEntry.setStatus("current")


class _PmoabphcsRinvBoosterIndex_Type(Integer32):
    """Custom type pmoabphcsRinvBoosterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PmoabphcsRinvBoosterIndex_Type.__name__ = "Integer32"
_PmoabphcsRinvBoosterIndex_Object = MibTableColumn
pmoabphcsRinvBoosterIndex = _PmoabphcsRinvBoosterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 7, 7, 1, 1),
    _PmoabphcsRinvBoosterIndex_Type()
)
pmoabphcsRinvBoosterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsRinvBoosterIndex.setStatus("current")
_PmoabphcsRinvBooster_Type = DisplayString
_PmoabphcsRinvBooster_Object = MibTableColumn
pmoabphcsRinvBooster = _PmoabphcsRinvBooster_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 7, 7, 1, 2),
    _PmoabphcsRinvBooster_Type()
)
pmoabphcsRinvBooster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsRinvBooster.setStatus("current")
_PmoabphcsRinvPreAmpTable_Object = MibTable
pmoabphcsRinvPreAmpTable = _PmoabphcsRinvPreAmpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 7, 8)
)
if mibBuilder.loadTexts:
    pmoabphcsRinvPreAmpTable.setStatus("current")
_PmoabphcsRinvPreAmpEntry_Object = MibTableRow
pmoabphcsRinvPreAmpEntry = _PmoabphcsRinvPreAmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 7, 8, 1)
)
pmoabphcsRinvPreAmpEntry.setIndexNames(
    (0, "EKINOPS-Pmoabphcs-MIB", "pmoabphcsRinvPreAmpIndex"),
)
if mibBuilder.loadTexts:
    pmoabphcsRinvPreAmpEntry.setStatus("current")


class _PmoabphcsRinvPreAmpIndex_Type(Integer32):
    """Custom type pmoabphcsRinvPreAmpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PmoabphcsRinvPreAmpIndex_Type.__name__ = "Integer32"
_PmoabphcsRinvPreAmpIndex_Object = MibTableColumn
pmoabphcsRinvPreAmpIndex = _PmoabphcsRinvPreAmpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 7, 8, 1, 1),
    _PmoabphcsRinvPreAmpIndex_Type()
)
pmoabphcsRinvPreAmpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsRinvPreAmpIndex.setStatus("current")
_PmoabphcsRinvPreAmp_Type = DisplayString
_PmoabphcsRinvPreAmp_Object = MibTableColumn
pmoabphcsRinvPreAmp = _PmoabphcsRinvPreAmp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 7, 8, 1, 2),
    _PmoabphcsRinvPreAmp_Type()
)
pmoabphcsRinvPreAmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsRinvPreAmp.setStatus("current")
_PmoabphcsConfig_ObjectIdentity = ObjectIdentity
pmoabphcsConfig = _PmoabphcsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 9)
)
_PmoabphcsCfgNoValue_ObjectIdentity = ObjectIdentity
pmoabphcsCfgNoValue = _PmoabphcsCfgNoValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 9, 1)
)
_PmoabphcstableclientStartup_ObjectIdentity = ObjectIdentity
pmoabphcstableclientStartup = _PmoabphcstableclientStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 9, 1, 1)
)


class _PmoabphcsCfgclientEdfaLaserCtrl_Type(Unsigned32):
    """Custom type pmoabphcsCfgclientEdfaLaserCtrl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoabphcsCfgclientEdfaLaserCtrl_Type.__name__ = "Unsigned32"
_PmoabphcsCfgclientEdfaLaserCtrl_Object = MibScalar
pmoabphcsCfgclientEdfaLaserCtrl = _PmoabphcsCfgclientEdfaLaserCtrl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 9, 1, 1, 2),
    _PmoabphcsCfgclientEdfaLaserCtrl_Type()
)
pmoabphcsCfgclientEdfaLaserCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCfgclientEdfaLaserCtrl.setStatus("current")


class _PmoabphcsCfgclientEdfaLaserMode_Type(Unsigned32):
    """Custom type pmoabphcsCfgclientEdfaLaserMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoabphcsCfgclientEdfaLaserMode_Type.__name__ = "Unsigned32"
_PmoabphcsCfgclientEdfaLaserMode_Object = MibScalar
pmoabphcsCfgclientEdfaLaserMode = _PmoabphcsCfgclientEdfaLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 9, 1, 1, 3),
    _PmoabphcsCfgclientEdfaLaserMode_Type()
)
pmoabphcsCfgclientEdfaLaserMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCfgclientEdfaLaserMode.setStatus("current")


class _PmoabphcsCfgclientGainValue_Type(Unsigned32):
    """Custom type pmoabphcsCfgclientGainValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoabphcsCfgclientGainValue_Type.__name__ = "Unsigned32"
_PmoabphcsCfgclientGainValue_Object = MibScalar
pmoabphcsCfgclientGainValue = _PmoabphcsCfgclientGainValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 9, 1, 1, 4),
    _PmoabphcsCfgclientGainValue_Type()
)
pmoabphcsCfgclientGainValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCfgclientGainValue.setStatus("current")


class _PmoabphcsCfgclientTiltValue_Type(Unsigned32):
    """Custom type pmoabphcsCfgclientTiltValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoabphcsCfgclientTiltValue_Type.__name__ = "Unsigned32"
_PmoabphcsCfgclientTiltValue_Object = MibScalar
pmoabphcsCfgclientTiltValue = _PmoabphcsCfgclientTiltValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 9, 1, 1, 5),
    _PmoabphcsCfgclientTiltValue_Type()
)
pmoabphcsCfgclientTiltValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCfgclientTiltValue.setStatus("current")


class _PmoabphcsCfgclientMsaLoss_Type(Unsigned32):
    """Custom type pmoabphcsCfgclientMsaLoss based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoabphcsCfgclientMsaLoss_Type.__name__ = "Unsigned32"
_PmoabphcsCfgclientMsaLoss_Object = MibScalar
pmoabphcsCfgclientMsaLoss = _PmoabphcsCfgclientMsaLoss_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 9, 1, 1, 6),
    _PmoabphcsCfgclientMsaLoss_Type()
)
pmoabphcsCfgclientMsaLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCfgclientMsaLoss.setStatus("current")


class _PmoabphcsCfgclientOutputPowerValue_Type(Unsigned32):
    """Custom type pmoabphcsCfgclientOutputPowerValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoabphcsCfgclientOutputPowerValue_Type.__name__ = "Unsigned32"
_PmoabphcsCfgclientOutputPowerValue_Object = MibScalar
pmoabphcsCfgclientOutputPowerValue = _PmoabphcsCfgclientOutputPowerValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 9, 1, 1, 7),
    _PmoabphcsCfgclientOutputPowerValue_Type()
)
pmoabphcsCfgclientOutputPowerValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCfgclientOutputPowerValue.setStatus("current")


class _PmoabphcsCfgclientAseCompensation_Type(Unsigned32):
    """Custom type pmoabphcsCfgclientAseCompensation based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoabphcsCfgclientAseCompensation_Type.__name__ = "Unsigned32"
_PmoabphcsCfgclientAseCompensation_Object = MibScalar
pmoabphcsCfgclientAseCompensation = _PmoabphcsCfgclientAseCompensation_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 9, 1, 1, 8),
    _PmoabphcsCfgclientAseCompensation_Type()
)
pmoabphcsCfgclientAseCompensation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCfgclientAseCompensation.setStatus("current")
_PmoabphcsCfgLineStartUp_ObjectIdentity = ObjectIdentity
pmoabphcsCfgLineStartUp = _PmoabphcsCfgLineStartUp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 9, 2)
)
_PmoabphcstablelineStartup_ObjectIdentity = ObjectIdentity
pmoabphcstablelineStartup = _PmoabphcstablelineStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 9, 2, 1)
)


class _PmoabphcsCfglineEdfaLaserCtrl_Type(Unsigned32):
    """Custom type pmoabphcsCfglineEdfaLaserCtrl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoabphcsCfglineEdfaLaserCtrl_Type.__name__ = "Unsigned32"
_PmoabphcsCfglineEdfaLaserCtrl_Object = MibScalar
pmoabphcsCfglineEdfaLaserCtrl = _PmoabphcsCfglineEdfaLaserCtrl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 9, 2, 1, 2),
    _PmoabphcsCfglineEdfaLaserCtrl_Type()
)
pmoabphcsCfglineEdfaLaserCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCfglineEdfaLaserCtrl.setStatus("current")


class _PmoabphcsCfglineEdfaLaserMode_Type(Unsigned32):
    """Custom type pmoabphcsCfglineEdfaLaserMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoabphcsCfglineEdfaLaserMode_Type.__name__ = "Unsigned32"
_PmoabphcsCfglineEdfaLaserMode_Object = MibScalar
pmoabphcsCfglineEdfaLaserMode = _PmoabphcsCfglineEdfaLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 9, 2, 1, 3),
    _PmoabphcsCfglineEdfaLaserMode_Type()
)
pmoabphcsCfglineEdfaLaserMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCfglineEdfaLaserMode.setStatus("current")


class _PmoabphcsCfglineGainValue_Type(Unsigned32):
    """Custom type pmoabphcsCfglineGainValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoabphcsCfglineGainValue_Type.__name__ = "Unsigned32"
_PmoabphcsCfglineGainValue_Object = MibScalar
pmoabphcsCfglineGainValue = _PmoabphcsCfglineGainValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 9, 2, 1, 4),
    _PmoabphcsCfglineGainValue_Type()
)
pmoabphcsCfglineGainValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCfglineGainValue.setStatus("current")


class _PmoabphcsCfglineTiltValue_Type(Unsigned32):
    """Custom type pmoabphcsCfglineTiltValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoabphcsCfglineTiltValue_Type.__name__ = "Unsigned32"
_PmoabphcsCfglineTiltValue_Object = MibScalar
pmoabphcsCfglineTiltValue = _PmoabphcsCfglineTiltValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 9, 2, 1, 5),
    _PmoabphcsCfglineTiltValue_Type()
)
pmoabphcsCfglineTiltValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCfglineTiltValue.setStatus("current")


class _PmoabphcsCfglineMsaLoss_Type(Unsigned32):
    """Custom type pmoabphcsCfglineMsaLoss based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoabphcsCfglineMsaLoss_Type.__name__ = "Unsigned32"
_PmoabphcsCfglineMsaLoss_Object = MibScalar
pmoabphcsCfglineMsaLoss = _PmoabphcsCfglineMsaLoss_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 9, 2, 1, 6),
    _PmoabphcsCfglineMsaLoss_Type()
)
pmoabphcsCfglineMsaLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCfglineMsaLoss.setStatus("current")


class _PmoabphcsCfglineOutputPowerValue_Type(Unsigned32):
    """Custom type pmoabphcsCfglineOutputPowerValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoabphcsCfglineOutputPowerValue_Type.__name__ = "Unsigned32"
_PmoabphcsCfglineOutputPowerValue_Object = MibScalar
pmoabphcsCfglineOutputPowerValue = _PmoabphcsCfglineOutputPowerValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 9, 2, 1, 7),
    _PmoabphcsCfglineOutputPowerValue_Type()
)
pmoabphcsCfglineOutputPowerValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCfglineOutputPowerValue.setStatus("current")


class _PmoabphcsCfglineAseCompensation_Type(Unsigned32):
    """Custom type pmoabphcsCfglineAseCompensation based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoabphcsCfglineAseCompensation_Type.__name__ = "Unsigned32"
_PmoabphcsCfglineAseCompensation_Object = MibScalar
pmoabphcsCfglineAseCompensation = _PmoabphcsCfglineAseCompensation_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 9, 2, 1, 8),
    _PmoabphcsCfglineAseCompensation_Type()
)
pmoabphcsCfglineAseCompensation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCfglineAseCompensation.setStatus("current")


class _PmoabphcsCfgaprMode_Type(Unsigned32):
    """Custom type pmoabphcsCfgaprMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoabphcsCfgaprMode_Type.__name__ = "Unsigned32"
_PmoabphcsCfgaprMode_Object = MibScalar
pmoabphcsCfgaprMode = _PmoabphcsCfgaprMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 9, 2, 1, 11),
    _PmoabphcsCfgaprMode_Type()
)
pmoabphcsCfgaprMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCfgaprMode.setStatus("current")
_PmoabphcsCfgClientSupvStartUp_ObjectIdentity = ObjectIdentity
pmoabphcsCfgClientSupvStartUp = _PmoabphcsCfgClientSupvStartUp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 9, 3)
)
_PmoabphcsCfgLineStartupTable_Object = MibTable
pmoabphcsCfgLineStartupTable = _PmoabphcsCfgLineStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 9, 3, 1)
)
if mibBuilder.loadTexts:
    pmoabphcsCfgLineStartupTable.setStatus("current")
_PmoabphcsCfgLineStartupEntry_Object = MibTableRow
pmoabphcsCfgLineStartupEntry = _PmoabphcsCfgLineStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 9, 3, 1, 1)
)
pmoabphcsCfgLineStartupEntry.setIndexNames(
    (0, "EKINOPS-Pmoabphcs-MIB", "pmoabphcsCfgLineStartupIndex"),
)
if mibBuilder.loadTexts:
    pmoabphcsCfgLineStartupEntry.setStatus("current")


class _PmoabphcsCfgLineStartupIndex_Type(Integer32):
    """Custom type pmoabphcsCfgLineStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmoabphcsCfgLineStartupIndex_Type.__name__ = "Integer32"
_PmoabphcsCfgLineStartupIndex_Object = MibTableColumn
pmoabphcsCfgLineStartupIndex = _PmoabphcsCfgLineStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 9, 3, 1, 1, 1),
    _PmoabphcsCfgLineStartupIndex_Type()
)
pmoabphcsCfgLineStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsCfgLineStartupIndex.setStatus("current")


class _PmoabphcsCfgLineOscLaserCtrlPortn_Type(Unsigned32):
    """Custom type pmoabphcsCfgLineOscLaserCtrlPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoabphcsCfgLineOscLaserCtrlPortn_Type.__name__ = "Unsigned32"
_PmoabphcsCfgLineOscLaserCtrlPortn_Object = MibTableColumn
pmoabphcsCfgLineOscLaserCtrlPortn = _PmoabphcsCfgLineOscLaserCtrlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 9, 3, 1, 1, 3),
    _PmoabphcsCfgLineOscLaserCtrlPortn_Type()
)
pmoabphcsCfgLineOscLaserCtrlPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCfgLineOscLaserCtrlPortn.setStatus("current")


class _PmoabphcsCfgLineOscOosPortn_Type(Unsigned32):
    """Custom type pmoabphcsCfgLineOscOosPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoabphcsCfgLineOscOosPortn_Type.__name__ = "Unsigned32"
_PmoabphcsCfgLineOscOosPortn_Object = MibTableColumn
pmoabphcsCfgLineOscOosPortn = _PmoabphcsCfgLineOscOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 9, 3, 1, 1, 4),
    _PmoabphcsCfgLineOscOosPortn_Type()
)
pmoabphcsCfgLineOscOosPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCfgLineOscOosPortn.setStatus("current")


class _PmoabphcsCfgLineOscSpanLengthPortn_Type(Unsigned32):
    """Custom type pmoabphcsCfgLineOscSpanLengthPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoabphcsCfgLineOscSpanLengthPortn_Type.__name__ = "Unsigned32"
_PmoabphcsCfgLineOscSpanLengthPortn_Object = MibTableColumn
pmoabphcsCfgLineOscSpanLengthPortn = _PmoabphcsCfgLineOscSpanLengthPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 9, 3, 1, 1, 5),
    _PmoabphcsCfgLineOscSpanLengthPortn_Type()
)
pmoabphcsCfgLineOscSpanLengthPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCfgLineOscSpanLengthPortn.setStatus("current")


class _PmoabphcsCfgLineOscCorrectionFactorPortn_Type(Unsigned32):
    """Custom type pmoabphcsCfgLineOscCorrectionFactorPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoabphcsCfgLineOscCorrectionFactorPortn_Type.__name__ = "Unsigned32"
_PmoabphcsCfgLineOscCorrectionFactorPortn_Object = MibTableColumn
pmoabphcsCfgLineOscCorrectionFactorPortn = _PmoabphcsCfgLineOscCorrectionFactorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 9, 3, 1, 1, 6),
    _PmoabphcsCfgLineOscCorrectionFactorPortn_Type()
)
pmoabphcsCfgLineOscCorrectionFactorPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCfgLineOscCorrectionFactorPortn.setStatus("current")
_PmoabphcsCfgLabels_ObjectIdentity = ObjectIdentity
pmoabphcsCfgLabels = _PmoabphcsCfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 9, 4)
)
_PmoabphcsCfgLabelclientTable_Object = MibTable
pmoabphcsCfgLabelclientTable = _PmoabphcsCfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 9, 4, 1)
)
if mibBuilder.loadTexts:
    pmoabphcsCfgLabelclientTable.setStatus("current")
_PmoabphcsCfgLabelclientEntry_Object = MibTableRow
pmoabphcsCfgLabelclientEntry = _PmoabphcsCfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 9, 4, 1, 1)
)
pmoabphcsCfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-Pmoabphcs-MIB", "pmoabphcsCfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pmoabphcsCfgLabelclientEntry.setStatus("current")


class _PmoabphcsCfgLabelclientIndex_Type(Integer32):
    """Custom type pmoabphcsCfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmoabphcsCfgLabelclientIndex_Type.__name__ = "Integer32"
_PmoabphcsCfgLabelclientIndex_Object = MibTableColumn
pmoabphcsCfgLabelclientIndex = _PmoabphcsCfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 9, 4, 1, 1, 1),
    _PmoabphcsCfgLabelclientIndex_Type()
)
pmoabphcsCfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsCfgLabelclientIndex.setStatus("current")


class _PmoabphcsCfgLabelclientPortn_Type(DisplayString):
    """Custom type pmoabphcsCfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PmoabphcsCfgLabelclientPortn_Type.__name__ = "DisplayString"
_PmoabphcsCfgLabelclientPortn_Object = MibTableColumn
pmoabphcsCfgLabelclientPortn = _PmoabphcsCfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 9, 4, 1, 1, 3),
    _PmoabphcsCfgLabelclientPortn_Type()
)
pmoabphcsCfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCfgLabelclientPortn.setStatus("current")
_PmoabphcsCfgLabellineTable_Object = MibTable
pmoabphcsCfgLabellineTable = _PmoabphcsCfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 9, 4, 2)
)
if mibBuilder.loadTexts:
    pmoabphcsCfgLabellineTable.setStatus("current")
_PmoabphcsCfgLabellineEntry_Object = MibTableRow
pmoabphcsCfgLabellineEntry = _PmoabphcsCfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 9, 4, 2, 1)
)
pmoabphcsCfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-Pmoabphcs-MIB", "pmoabphcsCfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pmoabphcsCfgLabellineEntry.setStatus("current")


class _PmoabphcsCfgLabellineIndex_Type(Integer32):
    """Custom type pmoabphcsCfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmoabphcsCfgLabellineIndex_Type.__name__ = "Integer32"
_PmoabphcsCfgLabellineIndex_Object = MibTableColumn
pmoabphcsCfgLabellineIndex = _PmoabphcsCfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 9, 4, 2, 1, 1),
    _PmoabphcsCfgLabellineIndex_Type()
)
pmoabphcsCfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcsCfgLabellineIndex.setStatus("current")


class _PmoabphcsCfgLabellinePortn_Type(DisplayString):
    """Custom type pmoabphcsCfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PmoabphcsCfgLabellinePortn_Type.__name__ = "DisplayString"
_PmoabphcsCfgLabellinePortn_Object = MibTableColumn
pmoabphcsCfgLabellinePortn = _PmoabphcsCfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 9, 4, 2, 1, 3),
    _PmoabphcsCfgLabellinePortn_Type()
)
pmoabphcsCfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCfgLabellinePortn.setStatus("current")
_PmoabphcsCfgWriteConfiguration_Type = EkiOnOff
_PmoabphcsCfgWriteConfiguration_Object = MibScalar
pmoabphcsCfgWriteConfiguration = _PmoabphcsCfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 9, 257),
    _PmoabphcsCfgWriteConfiguration_Type()
)
pmoabphcsCfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcsCfgWriteConfiguration.setStatus("current")
_Pmoabphcstraps_ObjectIdentity = ObjectIdentity
pmoabphcstraps = _Pmoabphcstraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 61, 10)
)


class _PmoabphcstrapBoardNumber_Type(Integer32):
    """Custom type pmoabphcstrapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_PmoabphcstrapBoardNumber_Type.__name__ = "Integer32"
_PmoabphcstrapBoardNumber_Object = MibScalar
pmoabphcstrapBoardNumber = _PmoabphcstrapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 61, 10, 4),
    _PmoabphcstrapBoardNumber_Type()
)
pmoabphcstrapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcstrapBoardNumber.setStatus("current")

# Managed Objects groups


# Notification objects

pmoabphcsLineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 61, 10, 34)
)
pmoabphcsLineTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pmoabphcs-MIB", "pmoabphcsAlmLineFail"),
        ("EKINOPS-Pmoabphcs-MIB", "pmoabphcsAlmLineHwFail"),
        ("EKINOPS-Pmoabphcs-MIB", "pmoabphcstrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoabphcsLineTrapCritGoesOn.setStatus(
        "current"
    )

pmoabphcsLineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 61, 10, 35)
)
pmoabphcsLineTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pmoabphcs-MIB", "pmoabphcsAlmLineFail"),
        ("EKINOPS-Pmoabphcs-MIB", "pmoabphcsAlmLineHwFail"),
        ("EKINOPS-Pmoabphcs-MIB", "pmoabphcstrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoabphcsLineTrapCritGoesOff.setStatus(
        "current"
    )

pmoabphcsClientTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 61, 10, 44)
)
pmoabphcsClientTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pmoabphcs-MIB", "pmoabphcsAlmClientFail"),
        ("EKINOPS-Pmoabphcs-MIB", "pmoabphcsAlmClientHwFail"),
        ("EKINOPS-Pmoabphcs-MIB", "pmoabphcstrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoabphcsClientTrapCritGoesOn.setStatus(
        "current"
    )

pmoabphcsClientTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 61, 10, 45)
)
pmoabphcsClientTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pmoabphcs-MIB", "pmoabphcsAlmClientFail"),
        ("EKINOPS-Pmoabphcs-MIB", "pmoabphcsAlmClientHwFail"),
        ("EKINOPS-Pmoabphcs-MIB", "pmoabphcstrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoabphcsClientTrapCritGoesOff.setStatus(
        "current"
    )

pmoabphcsPowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 61, 10, 50)
)
pmoabphcsPowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pmoabphcs-MIB", "pmoabphcsAlmDefFuseB"),
        ("EKINOPS-Pmoabphcs-MIB", "pmoabphcsAlmDefFuseA"),
        ("EKINOPS-Pmoabphcs-MIB", "pmoabphcstrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoabphcsPowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pmoabphcsPowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 61, 10, 51)
)
pmoabphcsPowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pmoabphcs-MIB", "pmoabphcsAlmDefFuseB"),
        ("EKINOPS-Pmoabphcs-MIB", "pmoabphcsAlmDefFuseA"),
        ("EKINOPS-Pmoabphcs-MIB", "pmoabphcstrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoabphcsPowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Pmoabphcs-MIB",
    **{"PmoabphcspreampMode": PmoabphcspreampMode,
       "PmoabphcsboosterMode": PmoabphcsboosterMode,
       "PmoabphcsaprMode": PmoabphcsaprMode,
       "PmoabphcsPreampGainAdjMode": PmoabphcsPreampGainAdjMode,
       "PmoabphcsBoosterGainAdjMode": PmoabphcsBoosterGainAdjMode,
       "PmoabphcsPreampCstGainAdjMode": PmoabphcsPreampCstGainAdjMode,
       "PmoabphcsBoosterCstGainAdjMode": PmoabphcsBoosterCstGainAdjMode,
       "modulepmoabphcs": modulepmoabphcs,
       "pmoabphcsalarms": pmoabphcsalarms,
       "pmoabphcsAlmOther": pmoabphcsAlmOther,
       "pmoabphcsAlmOtherNurg": pmoabphcsAlmOtherNurg,
       "pmoabphcsAlmsynthAlm2": pmoabphcsAlmsynthAlm2,
       "pmoabphcsAlmConfTableSave": pmoabphcsAlmConfTableSave,
       "pmoabphcsAlmInvUpload": pmoabphcsAlmInvUpload,
       "pmoabphcsAlmConfTableLoad": pmoabphcsAlmConfTableLoad,
       "pmoabphcsAlmfoaWarnings": pmoabphcsAlmfoaWarnings,
       "pmoabphcsAlmTermpLowWarning": pmoabphcsAlmTermpLowWarning,
       "pmoabphcsAlmTempHighWarning": pmoabphcsAlmTempHighWarning,
       "pmoabphcsAlmOtherUrg": pmoabphcsAlmOtherUrg,
       "pmoabphcsAlmfoaAlarms": pmoabphcsAlmfoaAlarms,
       "pmoabphcsAlmTermpLowAlarm": pmoabphcsAlmTermpLowAlarm,
       "pmoabphcsAlmTempHighAlarm": pmoabphcsAlmTempHighAlarm,
       "pmoabphcsAlmOtherCrit": pmoabphcsAlmOtherCrit,
       "pmoabphcsAlmsynthAlm0": pmoabphcsAlmsynthAlm0,
       "pmoabphcsAlmMaintenanceMode": pmoabphcsAlmMaintenanceMode,
       "pmoabphcsAlmAprOn": pmoabphcsAlmAprOn,
       "pmoabphcsAlmModGlobFail": pmoabphcsAlmModGlobFail,
       "pmoabphcsAlmUpEdfaInitNotCompl": pmoabphcsAlmUpEdfaInitNotCompl,
       "pmoabphcsAlmDwEdfaInitNotCompl": pmoabphcsAlmDwEdfaInitNotCompl,
       "pmoabphcsAlmExtPump1NotLocked": pmoabphcsAlmExtPump1NotLocked,
       "pmoabphcsAlmDefFuseA": pmoabphcsAlmDefFuseA,
       "pmoabphcsAlmDefFuseB": pmoabphcsAlmDefFuseB,
       "pmoabphcsAlmClient": pmoabphcsAlmClient,
       "pmoabphcsAlmClientNurg": pmoabphcsAlmClientNurg,
       "pmoabphcsAlmclientEdfaWarnings": pmoabphcsAlmclientEdfaWarnings,
       "pmoabphcsAlmClientGainLowWarning": pmoabphcsAlmClientGainLowWarning,
       "pmoabphcsAlmClientGainHighWarning": pmoabphcsAlmClientGainHighWarning,
       "pmoabphcsAlmClientInputPwrLowWarning": pmoabphcsAlmClientInputPwrLowWarning,
       "pmoabphcsAlmClientInputPwrHighWarning": pmoabphcsAlmClientInputPwrHighWarning,
       "pmoabphcsAlmClientOutputPwrLowWarning": pmoabphcsAlmClientOutputPwrLowWarning,
       "pmoabphcsAlmClientOutputPwrHighWarning": pmoabphcsAlmClientOutputPwrHighWarning,
       "pmoabphcsAlmClientBiasLowWarning": pmoabphcsAlmClientBiasLowWarning,
       "pmoabphcsAlmClientBiasHighWarning": pmoabphcsAlmClientBiasHighWarning,
       "pmoabphcsAlmClientUrg": pmoabphcsAlmClientUrg,
       "pmoabphcsAlmclientEdfaAlarms1": pmoabphcsAlmclientEdfaAlarms1,
       "pmoabphcsAlmClientGainLowAlarm": pmoabphcsAlmClientGainLowAlarm,
       "pmoabphcsAlmClientGainHighAlarm": pmoabphcsAlmClientGainHighAlarm,
       "pmoabphcsAlmClientInputPwrLowAlarm": pmoabphcsAlmClientInputPwrLowAlarm,
       "pmoabphcsAlmClientInputPwrHighAlarm": pmoabphcsAlmClientInputPwrHighAlarm,
       "pmoabphcsAlmClientOutputPwrLowAlarm": pmoabphcsAlmClientOutputPwrLowAlarm,
       "pmoabphcsAlmClientOutputPwrHighAlarm": pmoabphcsAlmClientOutputPwrHighAlarm,
       "pmoabphcsAlmClientBiasLowAlarm": pmoabphcsAlmClientBiasLowAlarm,
       "pmoabphcsAlmClientBiasHighAlarm": pmoabphcsAlmClientBiasHighAlarm,
       "pmoabphcsAlmClientCrit": pmoabphcsAlmClientCrit,
       "pmoabphcsAlmsynthAlm8": pmoabphcsAlmsynthAlm8,
       "pmoabphcsAlmClientHwFail": pmoabphcsAlmClientHwFail,
       "pmoabphcsAlmClientTxOff": pmoabphcsAlmClientTxOff,
       "pmoabphcsAlmClientFail": pmoabphcsAlmClientFail,
       "pmoabphcsAlmClientExtPumpFail": pmoabphcsAlmClientExtPumpFail,
       "pmoabphcsAlmSupvbFail": pmoabphcsAlmSupvbFail,
       "pmoabphcsAlmclientEdfaAlarms2": pmoabphcsAlmclientEdfaAlarms2,
       "pmoabphcsAlmClientEdfaNr": pmoabphcsAlmClientEdfaNr,
       "pmoabphcsAlmClientEdfaTecFail": pmoabphcsAlmClientEdfaTecFail,
       "pmoabphcsAlmClientEdfaLaserFail": pmoabphcsAlmClientEdfaLaserFail,
       "pmoabphcsAlmClientEdfaLos": pmoabphcsAlmClientEdfaLos,
       "pmoabphcsAlmClientExtPumpEdfaLowCurrent": pmoabphcsAlmClientExtPumpEdfaLowCurrent,
       "pmoabphcsAlmClientGainOutOfRange": pmoabphcsAlmClientGainOutOfRange,
       "pmoabphcsAlmclientMsaAlarms": pmoabphcsAlmclientMsaAlarms,
       "pmoabphcsAlmClientMsaLos": pmoabphcsAlmClientMsaLos,
       "pmoabphcsAlmClientMsaAttenuation": pmoabphcsAlmClientMsaAttenuation,
       "pmoabphcsAlmLine": pmoabphcsAlmLine,
       "pmoabphcsAlmLineNurg": pmoabphcsAlmLineNurg,
       "pmoabphcsAlmlineEdfaWarnings": pmoabphcsAlmlineEdfaWarnings,
       "pmoabphcsAlmLineGainLowWarning": pmoabphcsAlmLineGainLowWarning,
       "pmoabphcsAlmLineGainHighWarning": pmoabphcsAlmLineGainHighWarning,
       "pmoabphcsAlmLineInputPwrLowWarning": pmoabphcsAlmLineInputPwrLowWarning,
       "pmoabphcsAlmLineInputPwrHighWarning": pmoabphcsAlmLineInputPwrHighWarning,
       "pmoabphcsAlmLineOutputPwrLowWarning": pmoabphcsAlmLineOutputPwrLowWarning,
       "pmoabphcsAlmLineOutputPwrHighWarning": pmoabphcsAlmLineOutputPwrHighWarning,
       "pmoabphcsAlmLineBiasLowWarning": pmoabphcsAlmLineBiasLowWarning,
       "pmoabphcsAlmLineBiasHighWarning": pmoabphcsAlmLineBiasHighWarning,
       "pmoabphcsAlmLineUrg": pmoabphcsAlmLineUrg,
       "pmoabphcsAlmlineEdfaAlarms1": pmoabphcsAlmlineEdfaAlarms1,
       "pmoabphcsAlmLineGainLowAlarm": pmoabphcsAlmLineGainLowAlarm,
       "pmoabphcsAlmLineGainHighAlarm": pmoabphcsAlmLineGainHighAlarm,
       "pmoabphcsAlmLineInputPwrLowAlarm": pmoabphcsAlmLineInputPwrLowAlarm,
       "pmoabphcsAlmLineInputPwrHighAlarm": pmoabphcsAlmLineInputPwrHighAlarm,
       "pmoabphcsAlmLineOutputPwrLowAlarm": pmoabphcsAlmLineOutputPwrLowAlarm,
       "pmoabphcsAlmLineOutputPwrHighAlarm": pmoabphcsAlmLineOutputPwrHighAlarm,
       "pmoabphcsAlmLineBiasLowAlarm": pmoabphcsAlmLineBiasLowAlarm,
       "pmoabphcsAlmLineBiasHighAlarm": pmoabphcsAlmLineBiasHighAlarm,
       "pmoabphcsAlmLineCrit": pmoabphcsAlmLineCrit,
       "pmoabphcsAlmsynthAlm7": pmoabphcsAlmsynthAlm7,
       "pmoabphcsAlmLineHwFail": pmoabphcsAlmLineHwFail,
       "pmoabphcsAlmLineTxOff": pmoabphcsAlmLineTxOff,
       "pmoabphcsAlmLineFail": pmoabphcsAlmLineFail,
       "pmoabphcsAlmLineExtPumpFail": pmoabphcsAlmLineExtPumpFail,
       "pmoabphcsAlmSupvaFail": pmoabphcsAlmSupvaFail,
       "pmoabphcsAlmlineEdfaAlarms2": pmoabphcsAlmlineEdfaAlarms2,
       "pmoabphcsAlmLineEdfaNr": pmoabphcsAlmLineEdfaNr,
       "pmoabphcsAlmLineEdfaTecFail": pmoabphcsAlmLineEdfaTecFail,
       "pmoabphcsAlmLineEdfaLaserFail": pmoabphcsAlmLineEdfaLaserFail,
       "pmoabphcsAlmLineEdfaLos": pmoabphcsAlmLineEdfaLos,
       "pmoabphcsAlmLineExtPumpEdfaLowCurrent": pmoabphcsAlmLineExtPumpEdfaLowCurrent,
       "pmoabphcsAlmLineGainOutOfRange": pmoabphcsAlmLineGainOutOfRange,
       "pmoabphcsAlmlineMsaAlarms": pmoabphcsAlmlineMsaAlarms,
       "pmoabphcsAlmLineMsaLos": pmoabphcsAlmLineMsaLos,
       "pmoabphcsAlmLineMsaAttenuation": pmoabphcsAlmLineMsaAttenuation,
       "pmoabphcsAlmlineOscAlarmsTable": pmoabphcsAlmlineOscAlarmsTable,
       "pmoabphcsAlmlineOscAlarmsEntry": pmoabphcsAlmlineOscAlarmsEntry,
       "pmoabphcsAlmlineOscAlarmsIndex": pmoabphcsAlmlineOscAlarmsIndex,
       "pmoabphcsAlmLineLosPortn": pmoabphcsAlmLineLosPortn,
       "pmoabphcsAlmLineTxOffPortn": pmoabphcsAlmLineTxOffPortn,
       "pmoabphcsAlmLineTxFailPortn": pmoabphcsAlmLineTxFailPortn,
       "pmoabphcsAlmLineFecFailPortn": pmoabphcsAlmLineFecFailPortn,
       "pmoabphcsAlmLineOosPortn": pmoabphcsAlmLineOosPortn,
       "pmoabphcsAlmLineLofPortn": pmoabphcsAlmLineLofPortn,
       "pmoabphcsAlmLineOofPortn": pmoabphcsAlmLineOofPortn,
       "pmoabphcsAlmLineRemoteTxFailPortn": pmoabphcsAlmLineRemoteTxFailPortn,
       "pmoabphcsAlmLineWarningPortn": pmoabphcsAlmLineWarningPortn,
       "pmoabphcsAlmLineAlmPortn": pmoabphcsAlmLineAlmPortn,
       "pmoabphcsAlmlineOscThresholdAlarmsTable": pmoabphcsAlmlineOscThresholdAlarmsTable,
       "pmoabphcsAlmlineOscThresholdAlarmsEntry": pmoabphcsAlmlineOscThresholdAlarmsEntry,
       "pmoabphcsAlmlineOscThresholdAlarmsIndex": pmoabphcsAlmlineOscThresholdAlarmsIndex,
       "pmoabphcsAlmLineTxPwrLowAlarmPortn": pmoabphcsAlmLineTxPwrLowAlarmPortn,
       "pmoabphcsAlmLineTxPwrHighAlarmPortn": pmoabphcsAlmLineTxPwrHighAlarmPortn,
       "pmoabphcsAlmLineRxPwrLowAlarmPortn": pmoabphcsAlmLineRxPwrLowAlarmPortn,
       "pmoabphcsAlmLineRxPwrHighAlarmPortn": pmoabphcsAlmLineRxPwrHighAlarmPortn,
       "pmoabphcsAlmLineSpanlossLowAlarmPortn": pmoabphcsAlmLineSpanlossLowAlarmPortn,
       "pmoabphcsAlmLineSpanlossHighAlarmPortn": pmoabphcsAlmLineSpanlossHighAlarmPortn,
       "pmoabphcsAlmLineOscBiasLowAlarmPortn": pmoabphcsAlmLineOscBiasLowAlarmPortn,
       "pmoabphcsAlmLineOscBiasHighAlarmPortn": pmoabphcsAlmLineOscBiasHighAlarmPortn,
       "pmoabphcsAlmlineOscThresholdsWarningsTable": pmoabphcsAlmlineOscThresholdsWarningsTable,
       "pmoabphcsAlmlineOscThresholdsWarningsEntry": pmoabphcsAlmlineOscThresholdsWarningsEntry,
       "pmoabphcsAlmlineOscThresholdsWarningsIndex": pmoabphcsAlmlineOscThresholdsWarningsIndex,
       "pmoabphcsAlmLineTxPwrLowWarningPortn": pmoabphcsAlmLineTxPwrLowWarningPortn,
       "pmoabphcsAlmLineTxPwrHighWarningPortn": pmoabphcsAlmLineTxPwrHighWarningPortn,
       "pmoabphcsAlmLineRxPwrLowWarningPortn": pmoabphcsAlmLineRxPwrLowWarningPortn,
       "pmoabphcsAlmLineRxPwrHighWarningPortn": pmoabphcsAlmLineRxPwrHighWarningPortn,
       "pmoabphcsAlmLineSpanlossLowWarningPortn": pmoabphcsAlmLineSpanlossLowWarningPortn,
       "pmoabphcsAlmLineSpanlossHighWarningPortn": pmoabphcsAlmLineSpanlossHighWarningPortn,
       "pmoabphcsAlmLineOscBiasLowWarningPortn": pmoabphcsAlmLineOscBiasLowWarningPortn,
       "pmoabphcsAlmLineOscBiasHighWarningPortn": pmoabphcsAlmLineOscBiasHighWarningPortn,
       "pmoabphcsmeasures": pmoabphcsmeasures,
       "pmoabphcsMesrOther": pmoabphcsMesrOther,
       "pmoabphcsMesrtempMeas": pmoabphcsMesrtempMeas,
       "pmoabphcsMesrClient": pmoabphcsMesrClient,
       "pmoabphcsMesrclientEdfaBiasMeas": pmoabphcsMesrclientEdfaBiasMeas,
       "pmoabphcsMesrclientEdfaTxpwrMeas": pmoabphcsMesrclientEdfaTxpwrMeas,
       "pmoabphcsMesrclientEdfaRxpwrMeas": pmoabphcsMesrclientEdfaRxpwrMeas,
       "pmoabphcsMesrclientEdfaGainMeas": pmoabphcsMesrclientEdfaGainMeas,
       "pmoabphcsMesrclientOscSpanLoss": pmoabphcsMesrclientOscSpanLoss,
       "pmoabphcsMesrclientOscSpanLossRef": pmoabphcsMesrclientOscSpanLossRef,
       "pmoabphcsMesrclientCorrectedGain": pmoabphcsMesrclientCorrectedGain,
       "pmoabphcsMesrclientMsaInputPower": pmoabphcsMesrclientMsaInputPower,
       "pmoabphcsMesrclientMsaOutputPower": pmoabphcsMesrclientMsaOutputPower,
       "pmoabphcsMesrclientMsaAttenuation": pmoabphcsMesrclientMsaAttenuation,
       "pmoabphcsMesrclientMsaAttenuationRef": pmoabphcsMesrclientMsaAttenuationRef,
       "pmoabphcsMesrLine": pmoabphcsMesrLine,
       "pmoabphcsMesrlineEdfaBiasMeas": pmoabphcsMesrlineEdfaBiasMeas,
       "pmoabphcsMesrlineEdfaTxpwrMeas": pmoabphcsMesrlineEdfaTxpwrMeas,
       "pmoabphcsMesrlineEdfaRxpwrMeas": pmoabphcsMesrlineEdfaRxpwrMeas,
       "pmoabphcsMesrlineEdfaGainMeas": pmoabphcsMesrlineEdfaGainMeas,
       "pmoabphcsMesrlineOscSpanLoss": pmoabphcsMesrlineOscSpanLoss,
       "pmoabphcsMesrlineOscSpanLossRef": pmoabphcsMesrlineOscSpanLossRef,
       "pmoabphcsMesrlineCorrectedGain": pmoabphcsMesrlineCorrectedGain,
       "pmoabphcsMesrlineMsaInputPower": pmoabphcsMesrlineMsaInputPower,
       "pmoabphcsMesrlineMsaOutputPower": pmoabphcsMesrlineMsaOutputPower,
       "pmoabphcsMesrlineMsaAttenuation": pmoabphcsMesrlineMsaAttenuation,
       "pmoabphcsMesrlineMsaAttenuationRef": pmoabphcsMesrlineMsaAttenuationRef,
       "pmoabphcsMesrlineOscTxPowerTable": pmoabphcsMesrlineOscTxPowerTable,
       "pmoabphcsMesrlineOscTxPowerEntry": pmoabphcsMesrlineOscTxPowerEntry,
       "pmoabphcsMesrlineOscTxPowerIndex": pmoabphcsMesrlineOscTxPowerIndex,
       "pmoabphcsMesrlineOscTxPowerPortn": pmoabphcsMesrlineOscTxPowerPortn,
       "pmoabphcsMesrlineOscRxPowerTable": pmoabphcsMesrlineOscRxPowerTable,
       "pmoabphcsMesrlineOscRxPowerEntry": pmoabphcsMesrlineOscRxPowerEntry,
       "pmoabphcsMesrlineOscRxPowerIndex": pmoabphcsMesrlineOscRxPowerIndex,
       "pmoabphcsMesrlineOscRxPowerPortn": pmoabphcsMesrlineOscRxPowerPortn,
       "pmoabphcscounters": pmoabphcscounters,
       "pmoabphcsCntOther": pmoabphcsCntOther,
       "pmoabphcsCntClient": pmoabphcsCntClient,
       "pmoabphcsCntLine": pmoabphcsCntLine,
       "pmoabphcsCntlineOscErrTable": pmoabphcsCntlineOscErrTable,
       "pmoabphcsCntlineOscErrEntry": pmoabphcsCntlineOscErrEntry,
       "pmoabphcsCntlineOscErrIndex": pmoabphcsCntlineOscErrIndex,
       "pmoabphcsCntlineOscErrValuePortn": pmoabphcsCntlineOscErrValuePortn,
       "pmoabphcsCntlineOscErrErrorPortn": pmoabphcsCntlineOscErrErrorPortn,
       "pmoabphcsCntlineOscErrOverloadPortn": pmoabphcsCntlineOscErrOverloadPortn,
       "pmoabphcsCntCountersReset": pmoabphcsCntCountersReset,
       "pmoabphcsCntCountersStop": pmoabphcsCntCountersStop,
       "pmoabphcscontrolsWrite": pmoabphcscontrolsWrite,
       "pmoabphcsCtrlOther": pmoabphcsCtrlOther,
       "pmoabphcsCtrlsynth0": pmoabphcsCtrlsynth0,
       "pmoabphcsCtrlConfLoad": pmoabphcsCtrlConfLoad,
       "pmoabphcsCtrlConfFlash": pmoabphcsCtrlConfFlash,
       "pmoabphcsCtrlConfClear": pmoabphcsCtrlConfClear,
       "pmoabphcsCtrlswMgnt": pmoabphcsCtrlswMgnt,
       "pmoabphcsCtrlColdReset": pmoabphcsCtrlColdReset,
       "pmoabphcsCtrlWarmReset": pmoabphcsCtrlWarmReset,
       "pmoabphcsCtrlledTest": pmoabphcsCtrlledTest,
       "pmoabphcsCtrlGreenLed": pmoabphcsCtrlGreenLed,
       "pmoabphcsCtrlRedLed": pmoabphcsCtrlRedLed,
       "pmoabphcsCtrlLedOff": pmoabphcsCtrlLedOff,
       "pmoabphcsCtrlmaintMode": pmoabphcsCtrlmaintMode,
       "pmoabphcsCtrlMaintenance": pmoabphcsCtrlMaintenance,
       "pmoabphcsCtrlaprRestart": pmoabphcsCtrlaprRestart,
       "pmoabphcsCtrlAprManualRestart": pmoabphcsCtrlAprManualRestart,
       "pmoabphcsCtrlClient": pmoabphcsCtrlClient,
       "pmoabphcsCtrlclientOscInputSpanLoss": pmoabphcsCtrlclientOscInputSpanLoss,
       "pmoabphcsCtrlClientSpanLoss": pmoabphcsCtrlClientSpanLoss,
       "pmoabphcsCtrlclientGainCstMonitorValue": pmoabphcsCtrlclientGainCstMonitorValue,
       "pmoabphcsCtrlclientGainSettingValue": pmoabphcsCtrlclientGainSettingValue,
       "pmoabphcsCtrlclientGainProcessing": pmoabphcsCtrlclientGainProcessing,
       "pmoabphcsCtrlClientGainProc": pmoabphcsCtrlClientGainProc,
       "pmoabphcsCtrlclientGainCstFiberAgingMarginValue": pmoabphcsCtrlclientGainCstFiberAgingMarginValue,
       "pmoabphcsCtrlclientMsaAttenuationValue": pmoabphcsCtrlclientMsaAttenuationValue,
       "pmoabphcsCtrlClientAttenuation": pmoabphcsCtrlClientAttenuation,
       "pmoabphcsCtrlLine": pmoabphcsCtrlLine,
       "pmoabphcsCtrllineOscInputSpanLoss": pmoabphcsCtrllineOscInputSpanLoss,
       "pmoabphcsCtrlLineSpanLoss": pmoabphcsCtrlLineSpanLoss,
       "pmoabphcsCtrllineGainCstMonitorValue": pmoabphcsCtrllineGainCstMonitorValue,
       "pmoabphcsCtrllineGainSettingValue": pmoabphcsCtrllineGainSettingValue,
       "pmoabphcsCtrllineGainProcessing": pmoabphcsCtrllineGainProcessing,
       "pmoabphcsCtrlLineGainProc": pmoabphcsCtrlLineGainProc,
       "pmoabphcsCtrllineGainCstFiberAgingMarginValue": pmoabphcsCtrllineGainCstFiberAgingMarginValue,
       "pmoabphcsCtrllineMsaAttenuationValue": pmoabphcsCtrllineMsaAttenuationValue,
       "pmoabphcsCtrlLineAttenuation": pmoabphcsCtrlLineAttenuation,
       "pmoabphcsri": pmoabphcsri,
       "pmoabphcsRinvReloadInventory": pmoabphcsRinvReloadInventory,
       "pmoabphcsRinvHwPlatform": pmoabphcsRinvHwPlatform,
       "pmoabphcsRinvModulePlatform": pmoabphcsRinvModulePlatform,
       "pmoabphcsRinvSwPlatform": pmoabphcsRinvSwPlatform,
       "pmoabphcsRinvGwPlatform": pmoabphcsRinvGwPlatform,
       "pmoabphcsRinvBoosterTable": pmoabphcsRinvBoosterTable,
       "pmoabphcsRinvBoosterEntry": pmoabphcsRinvBoosterEntry,
       "pmoabphcsRinvBoosterIndex": pmoabphcsRinvBoosterIndex,
       "pmoabphcsRinvBooster": pmoabphcsRinvBooster,
       "pmoabphcsRinvPreAmpTable": pmoabphcsRinvPreAmpTable,
       "pmoabphcsRinvPreAmpEntry": pmoabphcsRinvPreAmpEntry,
       "pmoabphcsRinvPreAmpIndex": pmoabphcsRinvPreAmpIndex,
       "pmoabphcsRinvPreAmp": pmoabphcsRinvPreAmp,
       "pmoabphcsConfig": pmoabphcsConfig,
       "pmoabphcsCfgNoValue": pmoabphcsCfgNoValue,
       "pmoabphcstableclientStartup": pmoabphcstableclientStartup,
       "pmoabphcsCfgclientEdfaLaserCtrl": pmoabphcsCfgclientEdfaLaserCtrl,
       "pmoabphcsCfgclientEdfaLaserMode": pmoabphcsCfgclientEdfaLaserMode,
       "pmoabphcsCfgclientGainValue": pmoabphcsCfgclientGainValue,
       "pmoabphcsCfgclientTiltValue": pmoabphcsCfgclientTiltValue,
       "pmoabphcsCfgclientMsaLoss": pmoabphcsCfgclientMsaLoss,
       "pmoabphcsCfgclientOutputPowerValue": pmoabphcsCfgclientOutputPowerValue,
       "pmoabphcsCfgclientAseCompensation": pmoabphcsCfgclientAseCompensation,
       "pmoabphcsCfgLineStartUp": pmoabphcsCfgLineStartUp,
       "pmoabphcstablelineStartup": pmoabphcstablelineStartup,
       "pmoabphcsCfglineEdfaLaserCtrl": pmoabphcsCfglineEdfaLaserCtrl,
       "pmoabphcsCfglineEdfaLaserMode": pmoabphcsCfglineEdfaLaserMode,
       "pmoabphcsCfglineGainValue": pmoabphcsCfglineGainValue,
       "pmoabphcsCfglineTiltValue": pmoabphcsCfglineTiltValue,
       "pmoabphcsCfglineMsaLoss": pmoabphcsCfglineMsaLoss,
       "pmoabphcsCfglineOutputPowerValue": pmoabphcsCfglineOutputPowerValue,
       "pmoabphcsCfglineAseCompensation": pmoabphcsCfglineAseCompensation,
       "pmoabphcsCfgaprMode": pmoabphcsCfgaprMode,
       "pmoabphcsCfgClientSupvStartUp": pmoabphcsCfgClientSupvStartUp,
       "pmoabphcsCfgLineStartupTable": pmoabphcsCfgLineStartupTable,
       "pmoabphcsCfgLineStartupEntry": pmoabphcsCfgLineStartupEntry,
       "pmoabphcsCfgLineStartupIndex": pmoabphcsCfgLineStartupIndex,
       "pmoabphcsCfgLineOscLaserCtrlPortn": pmoabphcsCfgLineOscLaserCtrlPortn,
       "pmoabphcsCfgLineOscOosPortn": pmoabphcsCfgLineOscOosPortn,
       "pmoabphcsCfgLineOscSpanLengthPortn": pmoabphcsCfgLineOscSpanLengthPortn,
       "pmoabphcsCfgLineOscCorrectionFactorPortn": pmoabphcsCfgLineOscCorrectionFactorPortn,
       "pmoabphcsCfgLabels": pmoabphcsCfgLabels,
       "pmoabphcsCfgLabelclientTable": pmoabphcsCfgLabelclientTable,
       "pmoabphcsCfgLabelclientEntry": pmoabphcsCfgLabelclientEntry,
       "pmoabphcsCfgLabelclientIndex": pmoabphcsCfgLabelclientIndex,
       "pmoabphcsCfgLabelclientPortn": pmoabphcsCfgLabelclientPortn,
       "pmoabphcsCfgLabellineTable": pmoabphcsCfgLabellineTable,
       "pmoabphcsCfgLabellineEntry": pmoabphcsCfgLabellineEntry,
       "pmoabphcsCfgLabellineIndex": pmoabphcsCfgLabellineIndex,
       "pmoabphcsCfgLabellinePortn": pmoabphcsCfgLabellinePortn,
       "pmoabphcsCfgWriteConfiguration": pmoabphcsCfgWriteConfiguration,
       "pmoabphcstraps": pmoabphcstraps,
       "pmoabphcstrapBoardNumber": pmoabphcstrapBoardNumber,
       "pmoabphcsLineTrapCritGoesOn": pmoabphcsLineTrapCritGoesOn,
       "pmoabphcsLineTrapCritGoesOff": pmoabphcsLineTrapCritGoesOff,
       "pmoabphcsClientTrapCritGoesOn": pmoabphcsClientTrapCritGoesOn,
       "pmoabphcsClientTrapCritGoesOff": pmoabphcsClientTrapCritGoesOff,
       "pmoabphcsPowerTrapUrgentGoesOn": pmoabphcsPowerTrapUrgentGoesOn,
       "pmoabphcsPowerTrapUrgentGoesOff": pmoabphcsPowerTrapUrgentGoesOff}
)
