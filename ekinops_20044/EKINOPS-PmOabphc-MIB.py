# SNMP MIB module (EKINOPS-PmOabphc-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-PmOabphc-MIB.mib
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

modulepmoabphc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51)
)
if mibBuilder.loadTexts:
    modulepmoabphc.setRevisions(
        ("2011-07-06 00:00",
         "2011-07-06 00:00",
         "2013-02-08 00:00",
         "2013-07-01 00:00",
         "2013-09-16 00:00",
         "2013-12-02 00:00",
         "2014-03-26 00:00",
         "2014-12-10 00:00",
         "2016-05-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PmoabphcpreampMode(TextualConvention, Integer32):
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
        *(("oabphcpreampdefaultmode", 0),
          ("oabphcpreampconstantcurrentmode", 1),
          ("oabphcpreampconstantpowermode", 2),
          ("oabphcpreampconstantgainmode", 3),
          ("oabphcpreamppoutpinmode", 4),
          ("oabphcpreampmanualmode", 5),
          ("oabphcpreampfeedforwardmode", 6),
          ("oabphcpreamptransientsupmode", 7))
    )



class PmoabphcboosterMode(TextualConvention, Integer32):
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
        *(("oabphcboosterdefaultmode", 0),
          ("oabphcboosterconstantcurrentmode", 1),
          ("oabphcboosterconstantpowermode", 2),
          ("oabphcboosterconstantgainmode", 3),
          ("oabphcboosterpoutpinmode", 4),
          ("oabphcboostermanualmode", 5),
          ("oabphcboosterfeedforwardmode", 6),
          ("oabphcboostertransientsupmode", 7))
    )



class PmoabphcaprMode(TextualConvention, Integer32):
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
        *(("oabphcaproffmode", 0),
          ("oabphcaprsemiautomode", 1),
          ("oabphcaprautomode", 2),
          ("oabphcaprlossforwardingmode", 3),
          ("oabphcaprrepeatmode", 4))
    )



class PmoabphcPreampGainAdjMode(TextualConvention, Integer32):
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
        *(("oabphcpreampgainadjmanualmode", 0),
          ("oabphcpreampgainadjsemiautomode", 1),
          ("oabphcpreampgainadjautomode", 2))
    )



class PmoabphcBoosterGainAdjMode(TextualConvention, Integer32):
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
        *(("oabphcboostergainadjmanualmode", 0),
          ("oabphcboostergainadjsemiautomode", 1),
          ("oabphcboostergainadjautomode", 2))
    )



class PmoabphcPreampCstGainAdjMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oabphcpreampcstgainadjsemiautomode", 1),
          ("oabphcpreampcstgainadjautomode", 2))
    )



class PmoabphcBoosterCstGainAdjMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oabphcboostercstgainadjsemiautomode", 1),
          ("oabphcboostercstgainadjautomode", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Pmoabphcalarms_ObjectIdentity = ObjectIdentity
pmoabphcalarms = _Pmoabphcalarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2)
)
_PmoabphcAlmOther_ObjectIdentity = ObjectIdentity
pmoabphcAlmOther = _PmoabphcAlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 1)
)
_PmoabphcAlmOtherNurg_ObjectIdentity = ObjectIdentity
pmoabphcAlmOtherNurg = _PmoabphcAlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 1, 1)
)
_PmoabphcAlmsynthAlm2_ObjectIdentity = ObjectIdentity
pmoabphcAlmsynthAlm2 = _PmoabphcAlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 1, 1, 2)
)
_PmoabphcAlmConfTableSave_Type = EkiOnOff
_PmoabphcAlmConfTableSave_Object = MibScalar
pmoabphcAlmConfTableSave = _PmoabphcAlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 1, 1, 2, 1),
    _PmoabphcAlmConfTableSave_Type()
)
pmoabphcAlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmConfTableSave.setStatus("current")
_PmoabphcAlmInvUpload_Type = EkiOnOff
_PmoabphcAlmInvUpload_Object = MibScalar
pmoabphcAlmInvUpload = _PmoabphcAlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 1, 1, 2, 2),
    _PmoabphcAlmInvUpload_Type()
)
pmoabphcAlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmInvUpload.setStatus("current")
_PmoabphcAlmConfTableLoad_Type = EkiOnOff
_PmoabphcAlmConfTableLoad_Object = MibScalar
pmoabphcAlmConfTableLoad = _PmoabphcAlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 1, 1, 2, 3),
    _PmoabphcAlmConfTableLoad_Type()
)
pmoabphcAlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmConfTableLoad.setStatus("current")
_PmoabphcAlmfoaWarnings_ObjectIdentity = ObjectIdentity
pmoabphcAlmfoaWarnings = _PmoabphcAlmfoaWarnings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 1, 1, 75)
)
_PmoabphcAlmTermpLowWarning_Type = EkiOnOff
_PmoabphcAlmTermpLowWarning_Object = MibScalar
pmoabphcAlmTermpLowWarning = _PmoabphcAlmTermpLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 1, 1, 75, 7),
    _PmoabphcAlmTermpLowWarning_Type()
)
pmoabphcAlmTermpLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmTermpLowWarning.setStatus("current")
_PmoabphcAlmTempHighWarning_Type = EkiOnOff
_PmoabphcAlmTempHighWarning_Object = MibScalar
pmoabphcAlmTempHighWarning = _PmoabphcAlmTempHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 1, 1, 75, 8),
    _PmoabphcAlmTempHighWarning_Type()
)
pmoabphcAlmTempHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmTempHighWarning.setStatus("current")
_PmoabphcAlmOtherUrg_ObjectIdentity = ObjectIdentity
pmoabphcAlmOtherUrg = _PmoabphcAlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 1, 2)
)
_PmoabphcAlmfoaAlarms_ObjectIdentity = ObjectIdentity
pmoabphcAlmfoaAlarms = _PmoabphcAlmfoaAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 1, 2, 74)
)
_PmoabphcAlmTermpLowAlarm_Type = EkiOnOff
_PmoabphcAlmTermpLowAlarm_Object = MibScalar
pmoabphcAlmTermpLowAlarm = _PmoabphcAlmTermpLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 1, 2, 74, 7),
    _PmoabphcAlmTermpLowAlarm_Type()
)
pmoabphcAlmTermpLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmTermpLowAlarm.setStatus("current")
_PmoabphcAlmTempHighAlarm_Type = EkiOnOff
_PmoabphcAlmTempHighAlarm_Object = MibScalar
pmoabphcAlmTempHighAlarm = _PmoabphcAlmTempHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 1, 2, 74, 8),
    _PmoabphcAlmTempHighAlarm_Type()
)
pmoabphcAlmTempHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmTempHighAlarm.setStatus("current")
_PmoabphcAlmOtherCrit_ObjectIdentity = ObjectIdentity
pmoabphcAlmOtherCrit = _PmoabphcAlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 1, 3)
)
_PmoabphcAlmsynthAlm0_ObjectIdentity = ObjectIdentity
pmoabphcAlmsynthAlm0 = _PmoabphcAlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 1, 3, 0)
)
_PmoabphcAlmMaintenanceMode_Type = EkiOnOff
_PmoabphcAlmMaintenanceMode_Object = MibScalar
pmoabphcAlmMaintenanceMode = _PmoabphcAlmMaintenanceMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 1, 3, 0, 1),
    _PmoabphcAlmMaintenanceMode_Type()
)
pmoabphcAlmMaintenanceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmMaintenanceMode.setStatus("current")
_PmoabphcAlmAprOn_Type = EkiOnOff
_PmoabphcAlmAprOn_Object = MibScalar
pmoabphcAlmAprOn = _PmoabphcAlmAprOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 1, 3, 0, 2),
    _PmoabphcAlmAprOn_Type()
)
pmoabphcAlmAprOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmAprOn.setStatus("current")
_PmoabphcAlmModGlobFail_Type = EkiOnOff
_PmoabphcAlmModGlobFail_Object = MibScalar
pmoabphcAlmModGlobFail = _PmoabphcAlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 1, 3, 0, 9),
    _PmoabphcAlmModGlobFail_Type()
)
pmoabphcAlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmModGlobFail.setStatus("current")
_PmoabphcAlmUpEdfaInitNotCompl_Type = EkiOnOff
_PmoabphcAlmUpEdfaInitNotCompl_Object = MibScalar
pmoabphcAlmUpEdfaInitNotCompl = _PmoabphcAlmUpEdfaInitNotCompl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 1, 3, 0, 10),
    _PmoabphcAlmUpEdfaInitNotCompl_Type()
)
pmoabphcAlmUpEdfaInitNotCompl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmUpEdfaInitNotCompl.setStatus("current")
_PmoabphcAlmDwEdfaInitNotCompl_Type = EkiOnOff
_PmoabphcAlmDwEdfaInitNotCompl_Object = MibScalar
pmoabphcAlmDwEdfaInitNotCompl = _PmoabphcAlmDwEdfaInitNotCompl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 1, 3, 0, 11),
    _PmoabphcAlmDwEdfaInitNotCompl_Type()
)
pmoabphcAlmDwEdfaInitNotCompl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmDwEdfaInitNotCompl.setStatus("current")
_PmoabphcAlmExtPump1NotLocked_Type = EkiOnOff
_PmoabphcAlmExtPump1NotLocked_Object = MibScalar
pmoabphcAlmExtPump1NotLocked = _PmoabphcAlmExtPump1NotLocked_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 1, 3, 0, 12),
    _PmoabphcAlmExtPump1NotLocked_Type()
)
pmoabphcAlmExtPump1NotLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmExtPump1NotLocked.setStatus("current")
_PmoabphcAlmExtPump2NotLocked_Type = EkiOnOff
_PmoabphcAlmExtPump2NotLocked_Object = MibScalar
pmoabphcAlmExtPump2NotLocked = _PmoabphcAlmExtPump2NotLocked_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 1, 3, 0, 13),
    _PmoabphcAlmExtPump2NotLocked_Type()
)
pmoabphcAlmExtPump2NotLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmExtPump2NotLocked.setStatus("current")
_PmoabphcAlmDefFuseA_Type = EkiOnOff
_PmoabphcAlmDefFuseA_Object = MibScalar
pmoabphcAlmDefFuseA = _PmoabphcAlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 1, 3, 0, 15),
    _PmoabphcAlmDefFuseA_Type()
)
pmoabphcAlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmDefFuseA.setStatus("current")
_PmoabphcAlmDefFuseB_Type = EkiOnOff
_PmoabphcAlmDefFuseB_Object = MibScalar
pmoabphcAlmDefFuseB = _PmoabphcAlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 1, 3, 0, 16),
    _PmoabphcAlmDefFuseB_Type()
)
pmoabphcAlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmDefFuseB.setStatus("current")
_PmoabphcAlmClient_ObjectIdentity = ObjectIdentity
pmoabphcAlmClient = _PmoabphcAlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 2)
)
_PmoabphcAlmClientNurg_ObjectIdentity = ObjectIdentity
pmoabphcAlmClientNurg = _PmoabphcAlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 2, 1)
)
_PmoabphcAlmclientEdfaWarnings_ObjectIdentity = ObjectIdentity
pmoabphcAlmclientEdfaWarnings = _PmoabphcAlmclientEdfaWarnings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 2, 1, 33)
)
_PmoabphcAlmClientGainLowWarning_Type = EkiOnOff
_PmoabphcAlmClientGainLowWarning_Object = MibScalar
pmoabphcAlmClientGainLowWarning = _PmoabphcAlmClientGainLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 2, 1, 33, 1),
    _PmoabphcAlmClientGainLowWarning_Type()
)
pmoabphcAlmClientGainLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmClientGainLowWarning.setStatus("current")
_PmoabphcAlmClientGainHighWarning_Type = EkiOnOff
_PmoabphcAlmClientGainHighWarning_Object = MibScalar
pmoabphcAlmClientGainHighWarning = _PmoabphcAlmClientGainHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 2, 1, 33, 2),
    _PmoabphcAlmClientGainHighWarning_Type()
)
pmoabphcAlmClientGainHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmClientGainHighWarning.setStatus("current")
_PmoabphcAlmClientInputPwrLowWarning_Type = EkiOnOff
_PmoabphcAlmClientInputPwrLowWarning_Object = MibScalar
pmoabphcAlmClientInputPwrLowWarning = _PmoabphcAlmClientInputPwrLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 2, 1, 33, 3),
    _PmoabphcAlmClientInputPwrLowWarning_Type()
)
pmoabphcAlmClientInputPwrLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmClientInputPwrLowWarning.setStatus("current")
_PmoabphcAlmClientInputPwrHighWarning_Type = EkiOnOff
_PmoabphcAlmClientInputPwrHighWarning_Object = MibScalar
pmoabphcAlmClientInputPwrHighWarning = _PmoabphcAlmClientInputPwrHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 2, 1, 33, 4),
    _PmoabphcAlmClientInputPwrHighWarning_Type()
)
pmoabphcAlmClientInputPwrHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmClientInputPwrHighWarning.setStatus("current")
_PmoabphcAlmClientOutputPwrLowWarning_Type = EkiOnOff
_PmoabphcAlmClientOutputPwrLowWarning_Object = MibScalar
pmoabphcAlmClientOutputPwrLowWarning = _PmoabphcAlmClientOutputPwrLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 2, 1, 33, 5),
    _PmoabphcAlmClientOutputPwrLowWarning_Type()
)
pmoabphcAlmClientOutputPwrLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmClientOutputPwrLowWarning.setStatus("current")
_PmoabphcAlmClientOutputPwrHighWarning_Type = EkiOnOff
_PmoabphcAlmClientOutputPwrHighWarning_Object = MibScalar
pmoabphcAlmClientOutputPwrHighWarning = _PmoabphcAlmClientOutputPwrHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 2, 1, 33, 6),
    _PmoabphcAlmClientOutputPwrHighWarning_Type()
)
pmoabphcAlmClientOutputPwrHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmClientOutputPwrHighWarning.setStatus("current")
_PmoabphcAlmClientBiasLowWarning_Type = EkiOnOff
_PmoabphcAlmClientBiasLowWarning_Object = MibScalar
pmoabphcAlmClientBiasLowWarning = _PmoabphcAlmClientBiasLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 2, 1, 33, 7),
    _PmoabphcAlmClientBiasLowWarning_Type()
)
pmoabphcAlmClientBiasLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmClientBiasLowWarning.setStatus("current")
_PmoabphcAlmClientBiasHighWarning_Type = EkiOnOff
_PmoabphcAlmClientBiasHighWarning_Object = MibScalar
pmoabphcAlmClientBiasHighWarning = _PmoabphcAlmClientBiasHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 2, 1, 33, 8),
    _PmoabphcAlmClientBiasHighWarning_Type()
)
pmoabphcAlmClientBiasHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmClientBiasHighWarning.setStatus("current")
_PmoabphcAlmClientUrg_ObjectIdentity = ObjectIdentity
pmoabphcAlmClientUrg = _PmoabphcAlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 2, 2)
)
_PmoabphcAlmclientEdfaAlarms1_ObjectIdentity = ObjectIdentity
pmoabphcAlmclientEdfaAlarms1 = _PmoabphcAlmclientEdfaAlarms1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 2, 2, 32)
)
_PmoabphcAlmClientGainLowAlarm_Type = EkiOnOff
_PmoabphcAlmClientGainLowAlarm_Object = MibScalar
pmoabphcAlmClientGainLowAlarm = _PmoabphcAlmClientGainLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 2, 2, 32, 1),
    _PmoabphcAlmClientGainLowAlarm_Type()
)
pmoabphcAlmClientGainLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmClientGainLowAlarm.setStatus("current")
_PmoabphcAlmClientGainHighAlarm_Type = EkiOnOff
_PmoabphcAlmClientGainHighAlarm_Object = MibScalar
pmoabphcAlmClientGainHighAlarm = _PmoabphcAlmClientGainHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 2, 2, 32, 2),
    _PmoabphcAlmClientGainHighAlarm_Type()
)
pmoabphcAlmClientGainHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmClientGainHighAlarm.setStatus("current")
_PmoabphcAlmClientInputPwrLowAlarm_Type = EkiOnOff
_PmoabphcAlmClientInputPwrLowAlarm_Object = MibScalar
pmoabphcAlmClientInputPwrLowAlarm = _PmoabphcAlmClientInputPwrLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 2, 2, 32, 3),
    _PmoabphcAlmClientInputPwrLowAlarm_Type()
)
pmoabphcAlmClientInputPwrLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmClientInputPwrLowAlarm.setStatus("current")
_PmoabphcAlmClientInputPwrHighAlarm_Type = EkiOnOff
_PmoabphcAlmClientInputPwrHighAlarm_Object = MibScalar
pmoabphcAlmClientInputPwrHighAlarm = _PmoabphcAlmClientInputPwrHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 2, 2, 32, 4),
    _PmoabphcAlmClientInputPwrHighAlarm_Type()
)
pmoabphcAlmClientInputPwrHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmClientInputPwrHighAlarm.setStatus("current")
_PmoabphcAlmClientOutputPwrLowAlarm_Type = EkiOnOff
_PmoabphcAlmClientOutputPwrLowAlarm_Object = MibScalar
pmoabphcAlmClientOutputPwrLowAlarm = _PmoabphcAlmClientOutputPwrLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 2, 2, 32, 5),
    _PmoabphcAlmClientOutputPwrLowAlarm_Type()
)
pmoabphcAlmClientOutputPwrLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmClientOutputPwrLowAlarm.setStatus("current")
_PmoabphcAlmClientOutputPwrHighAlarm_Type = EkiOnOff
_PmoabphcAlmClientOutputPwrHighAlarm_Object = MibScalar
pmoabphcAlmClientOutputPwrHighAlarm = _PmoabphcAlmClientOutputPwrHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 2, 2, 32, 6),
    _PmoabphcAlmClientOutputPwrHighAlarm_Type()
)
pmoabphcAlmClientOutputPwrHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmClientOutputPwrHighAlarm.setStatus("current")
_PmoabphcAlmClientBiasLowAlarm_Type = EkiOnOff
_PmoabphcAlmClientBiasLowAlarm_Object = MibScalar
pmoabphcAlmClientBiasLowAlarm = _PmoabphcAlmClientBiasLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 2, 2, 32, 7),
    _PmoabphcAlmClientBiasLowAlarm_Type()
)
pmoabphcAlmClientBiasLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmClientBiasLowAlarm.setStatus("current")
_PmoabphcAlmClientBiasHighAlarm_Type = EkiOnOff
_PmoabphcAlmClientBiasHighAlarm_Object = MibScalar
pmoabphcAlmClientBiasHighAlarm = _PmoabphcAlmClientBiasHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 2, 2, 32, 8),
    _PmoabphcAlmClientBiasHighAlarm_Type()
)
pmoabphcAlmClientBiasHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmClientBiasHighAlarm.setStatus("current")
_PmoabphcAlmClientCrit_ObjectIdentity = ObjectIdentity
pmoabphcAlmClientCrit = _PmoabphcAlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 2, 3)
)
_PmoabphcAlmsynthAlm8_ObjectIdentity = ObjectIdentity
pmoabphcAlmsynthAlm8 = _PmoabphcAlmsynthAlm8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 2, 3, 8)
)
_PmoabphcAlmClientHwFail_Type = EkiOnOff
_PmoabphcAlmClientHwFail_Object = MibScalar
pmoabphcAlmClientHwFail = _PmoabphcAlmClientHwFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 2, 3, 8, 4),
    _PmoabphcAlmClientHwFail_Type()
)
pmoabphcAlmClientHwFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmClientHwFail.setStatus("current")
_PmoabphcAlmClientTxOff_Type = EkiOnOff
_PmoabphcAlmClientTxOff_Object = MibScalar
pmoabphcAlmClientTxOff = _PmoabphcAlmClientTxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 2, 3, 8, 5),
    _PmoabphcAlmClientTxOff_Type()
)
pmoabphcAlmClientTxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmClientTxOff.setStatus("current")
_PmoabphcAlmClientDdmWarning_Type = EkiOnOff
_PmoabphcAlmClientDdmWarning_Object = MibScalar
pmoabphcAlmClientDdmWarning = _PmoabphcAlmClientDdmWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 2, 3, 8, 9),
    _PmoabphcAlmClientDdmWarning_Type()
)
pmoabphcAlmClientDdmWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmClientDdmWarning.setStatus("current")
_PmoabphcAlmClientDdmAlm_Type = EkiOnOff
_PmoabphcAlmClientDdmAlm_Object = MibScalar
pmoabphcAlmClientDdmAlm = _PmoabphcAlmClientDdmAlm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 2, 3, 8, 10),
    _PmoabphcAlmClientDdmAlm_Type()
)
pmoabphcAlmClientDdmAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmClientDdmAlm.setStatus("current")
_PmoabphcAlmClientFail_Type = EkiOnOff
_PmoabphcAlmClientFail_Object = MibScalar
pmoabphcAlmClientFail = _PmoabphcAlmClientFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 2, 3, 8, 12),
    _PmoabphcAlmClientFail_Type()
)
pmoabphcAlmClientFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmClientFail.setStatus("current")
_PmoabphcAlmClientExtPumpFail_Type = EkiOnOff
_PmoabphcAlmClientExtPumpFail_Object = MibScalar
pmoabphcAlmClientExtPumpFail = _PmoabphcAlmClientExtPumpFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 2, 3, 8, 13),
    _PmoabphcAlmClientExtPumpFail_Type()
)
pmoabphcAlmClientExtPumpFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmClientExtPumpFail.setStatus("current")
_PmoabphcAlmclientEdfaAlarms2_ObjectIdentity = ObjectIdentity
pmoabphcAlmclientEdfaAlarms2 = _PmoabphcAlmclientEdfaAlarms2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 2, 3, 35)
)
_PmoabphcAlmClientEdfaNr_Type = EkiOnOff
_PmoabphcAlmClientEdfaNr_Object = MibScalar
pmoabphcAlmClientEdfaNr = _PmoabphcAlmClientEdfaNr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 2, 3, 35, 1),
    _PmoabphcAlmClientEdfaNr_Type()
)
pmoabphcAlmClientEdfaNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmClientEdfaNr.setStatus("current")
_PmoabphcAlmClientEdfaTecFail_Type = EkiOnOff
_PmoabphcAlmClientEdfaTecFail_Object = MibScalar
pmoabphcAlmClientEdfaTecFail = _PmoabphcAlmClientEdfaTecFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 2, 3, 35, 2),
    _PmoabphcAlmClientEdfaTecFail_Type()
)
pmoabphcAlmClientEdfaTecFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmClientEdfaTecFail.setStatus("current")
_PmoabphcAlmClientEdfaLaserFail_Type = EkiOnOff
_PmoabphcAlmClientEdfaLaserFail_Object = MibScalar
pmoabphcAlmClientEdfaLaserFail = _PmoabphcAlmClientEdfaLaserFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 2, 3, 35, 3),
    _PmoabphcAlmClientEdfaLaserFail_Type()
)
pmoabphcAlmClientEdfaLaserFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmClientEdfaLaserFail.setStatus("current")
_PmoabphcAlmClientEdfaLos_Type = EkiOnOff
_PmoabphcAlmClientEdfaLos_Object = MibScalar
pmoabphcAlmClientEdfaLos = _PmoabphcAlmClientEdfaLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 2, 3, 35, 4),
    _PmoabphcAlmClientEdfaLos_Type()
)
pmoabphcAlmClientEdfaLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmClientEdfaLos.setStatus("current")
_PmoabphcAlmClientExtPumpEdfaLowCurrent_Type = EkiOnOff
_PmoabphcAlmClientExtPumpEdfaLowCurrent_Object = MibScalar
pmoabphcAlmClientExtPumpEdfaLowCurrent = _PmoabphcAlmClientExtPumpEdfaLowCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 2, 3, 35, 5),
    _PmoabphcAlmClientExtPumpEdfaLowCurrent_Type()
)
pmoabphcAlmClientExtPumpEdfaLowCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmClientExtPumpEdfaLowCurrent.setStatus("current")
_PmoabphcAlmLine_ObjectIdentity = ObjectIdentity
pmoabphcAlmLine = _PmoabphcAlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 3)
)
_PmoabphcAlmLineNurg_ObjectIdentity = ObjectIdentity
pmoabphcAlmLineNurg = _PmoabphcAlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 3, 1)
)
_PmoabphcAlmlineEdfaWarnings_ObjectIdentity = ObjectIdentity
pmoabphcAlmlineEdfaWarnings = _PmoabphcAlmlineEdfaWarnings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 3, 1, 41)
)
_PmoabphcAlmLineGainLowWarning_Type = EkiOnOff
_PmoabphcAlmLineGainLowWarning_Object = MibScalar
pmoabphcAlmLineGainLowWarning = _PmoabphcAlmLineGainLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 3, 1, 41, 1),
    _PmoabphcAlmLineGainLowWarning_Type()
)
pmoabphcAlmLineGainLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmLineGainLowWarning.setStatus("current")
_PmoabphcAlmLineGainHighWarning_Type = EkiOnOff
_PmoabphcAlmLineGainHighWarning_Object = MibScalar
pmoabphcAlmLineGainHighWarning = _PmoabphcAlmLineGainHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 3, 1, 41, 2),
    _PmoabphcAlmLineGainHighWarning_Type()
)
pmoabphcAlmLineGainHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmLineGainHighWarning.setStatus("current")
_PmoabphcAlmLineInputPwrLowWarning_Type = EkiOnOff
_PmoabphcAlmLineInputPwrLowWarning_Object = MibScalar
pmoabphcAlmLineInputPwrLowWarning = _PmoabphcAlmLineInputPwrLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 3, 1, 41, 3),
    _PmoabphcAlmLineInputPwrLowWarning_Type()
)
pmoabphcAlmLineInputPwrLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmLineInputPwrLowWarning.setStatus("current")
_PmoabphcAlmLineInputPwrHighWarning_Type = EkiOnOff
_PmoabphcAlmLineInputPwrHighWarning_Object = MibScalar
pmoabphcAlmLineInputPwrHighWarning = _PmoabphcAlmLineInputPwrHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 3, 1, 41, 4),
    _PmoabphcAlmLineInputPwrHighWarning_Type()
)
pmoabphcAlmLineInputPwrHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmLineInputPwrHighWarning.setStatus("current")
_PmoabphcAlmLineOutputPwrLowWarning_Type = EkiOnOff
_PmoabphcAlmLineOutputPwrLowWarning_Object = MibScalar
pmoabphcAlmLineOutputPwrLowWarning = _PmoabphcAlmLineOutputPwrLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 3, 1, 41, 5),
    _PmoabphcAlmLineOutputPwrLowWarning_Type()
)
pmoabphcAlmLineOutputPwrLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmLineOutputPwrLowWarning.setStatus("current")
_PmoabphcAlmLineOutputPwrHighWarning_Type = EkiOnOff
_PmoabphcAlmLineOutputPwrHighWarning_Object = MibScalar
pmoabphcAlmLineOutputPwrHighWarning = _PmoabphcAlmLineOutputPwrHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 3, 1, 41, 6),
    _PmoabphcAlmLineOutputPwrHighWarning_Type()
)
pmoabphcAlmLineOutputPwrHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmLineOutputPwrHighWarning.setStatus("current")
_PmoabphcAlmLineBiasLowWarning_Type = EkiOnOff
_PmoabphcAlmLineBiasLowWarning_Object = MibScalar
pmoabphcAlmLineBiasLowWarning = _PmoabphcAlmLineBiasLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 3, 1, 41, 7),
    _PmoabphcAlmLineBiasLowWarning_Type()
)
pmoabphcAlmLineBiasLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmLineBiasLowWarning.setStatus("current")
_PmoabphcAlmLineBiasHighWarning_Type = EkiOnOff
_PmoabphcAlmLineBiasHighWarning_Object = MibScalar
pmoabphcAlmLineBiasHighWarning = _PmoabphcAlmLineBiasHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 3, 1, 41, 8),
    _PmoabphcAlmLineBiasHighWarning_Type()
)
pmoabphcAlmLineBiasHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmLineBiasHighWarning.setStatus("current")
_PmoabphcAlmLineUrg_ObjectIdentity = ObjectIdentity
pmoabphcAlmLineUrg = _PmoabphcAlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 3, 2)
)
_PmoabphcAlmlineEdfaAlarms1_ObjectIdentity = ObjectIdentity
pmoabphcAlmlineEdfaAlarms1 = _PmoabphcAlmlineEdfaAlarms1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 3, 2, 40)
)
_PmoabphcAlmLineGainLowAlarm_Type = EkiOnOff
_PmoabphcAlmLineGainLowAlarm_Object = MibScalar
pmoabphcAlmLineGainLowAlarm = _PmoabphcAlmLineGainLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 3, 2, 40, 1),
    _PmoabphcAlmLineGainLowAlarm_Type()
)
pmoabphcAlmLineGainLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmLineGainLowAlarm.setStatus("current")
_PmoabphcAlmLineGainHighAlarm_Type = EkiOnOff
_PmoabphcAlmLineGainHighAlarm_Object = MibScalar
pmoabphcAlmLineGainHighAlarm = _PmoabphcAlmLineGainHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 3, 2, 40, 2),
    _PmoabphcAlmLineGainHighAlarm_Type()
)
pmoabphcAlmLineGainHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmLineGainHighAlarm.setStatus("current")
_PmoabphcAlmLineInputPwrLowAlarm_Type = EkiOnOff
_PmoabphcAlmLineInputPwrLowAlarm_Object = MibScalar
pmoabphcAlmLineInputPwrLowAlarm = _PmoabphcAlmLineInputPwrLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 3, 2, 40, 3),
    _PmoabphcAlmLineInputPwrLowAlarm_Type()
)
pmoabphcAlmLineInputPwrLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmLineInputPwrLowAlarm.setStatus("current")
_PmoabphcAlmLineInputPwrHighAlarm_Type = EkiOnOff
_PmoabphcAlmLineInputPwrHighAlarm_Object = MibScalar
pmoabphcAlmLineInputPwrHighAlarm = _PmoabphcAlmLineInputPwrHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 3, 2, 40, 4),
    _PmoabphcAlmLineInputPwrHighAlarm_Type()
)
pmoabphcAlmLineInputPwrHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmLineInputPwrHighAlarm.setStatus("current")
_PmoabphcAlmLineOutputPwrLowAlarm_Type = EkiOnOff
_PmoabphcAlmLineOutputPwrLowAlarm_Object = MibScalar
pmoabphcAlmLineOutputPwrLowAlarm = _PmoabphcAlmLineOutputPwrLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 3, 2, 40, 5),
    _PmoabphcAlmLineOutputPwrLowAlarm_Type()
)
pmoabphcAlmLineOutputPwrLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmLineOutputPwrLowAlarm.setStatus("current")
_PmoabphcAlmLineOutputPwrHighAlarm_Type = EkiOnOff
_PmoabphcAlmLineOutputPwrHighAlarm_Object = MibScalar
pmoabphcAlmLineOutputPwrHighAlarm = _PmoabphcAlmLineOutputPwrHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 3, 2, 40, 6),
    _PmoabphcAlmLineOutputPwrHighAlarm_Type()
)
pmoabphcAlmLineOutputPwrHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmLineOutputPwrHighAlarm.setStatus("current")
_PmoabphcAlmLineBiasLowAlarm_Type = EkiOnOff
_PmoabphcAlmLineBiasLowAlarm_Object = MibScalar
pmoabphcAlmLineBiasLowAlarm = _PmoabphcAlmLineBiasLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 3, 2, 40, 7),
    _PmoabphcAlmLineBiasLowAlarm_Type()
)
pmoabphcAlmLineBiasLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmLineBiasLowAlarm.setStatus("current")
_PmoabphcAlmLineBiasHighAlarm_Type = EkiOnOff
_PmoabphcAlmLineBiasHighAlarm_Object = MibScalar
pmoabphcAlmLineBiasHighAlarm = _PmoabphcAlmLineBiasHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 3, 2, 40, 8),
    _PmoabphcAlmLineBiasHighAlarm_Type()
)
pmoabphcAlmLineBiasHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmLineBiasHighAlarm.setStatus("current")
_PmoabphcAlmLineCrit_ObjectIdentity = ObjectIdentity
pmoabphcAlmLineCrit = _PmoabphcAlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 3, 3)
)
_PmoabphcAlmsynthAlm7_ObjectIdentity = ObjectIdentity
pmoabphcAlmsynthAlm7 = _PmoabphcAlmsynthAlm7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 3, 3, 7)
)
_PmoabphcAlmLineHwFail_Type = EkiOnOff
_PmoabphcAlmLineHwFail_Object = MibScalar
pmoabphcAlmLineHwFail = _PmoabphcAlmLineHwFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 3, 3, 7, 4),
    _PmoabphcAlmLineHwFail_Type()
)
pmoabphcAlmLineHwFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmLineHwFail.setStatus("current")
_PmoabphcAlmLineTxOff_Type = EkiOnOff
_PmoabphcAlmLineTxOff_Object = MibScalar
pmoabphcAlmLineTxOff = _PmoabphcAlmLineTxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 3, 3, 7, 5),
    _PmoabphcAlmLineTxOff_Type()
)
pmoabphcAlmLineTxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmLineTxOff.setStatus("current")
_PmoabphcAlmLineDdmWarning_Type = EkiOnOff
_PmoabphcAlmLineDdmWarning_Object = MibScalar
pmoabphcAlmLineDdmWarning = _PmoabphcAlmLineDdmWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 3, 3, 7, 9),
    _PmoabphcAlmLineDdmWarning_Type()
)
pmoabphcAlmLineDdmWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmLineDdmWarning.setStatus("current")
_PmoabphcAlmLineDdmAlm_Type = EkiOnOff
_PmoabphcAlmLineDdmAlm_Object = MibScalar
pmoabphcAlmLineDdmAlm = _PmoabphcAlmLineDdmAlm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 3, 3, 7, 10),
    _PmoabphcAlmLineDdmAlm_Type()
)
pmoabphcAlmLineDdmAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmLineDdmAlm.setStatus("current")
_PmoabphcAlmLineFail_Type = EkiOnOff
_PmoabphcAlmLineFail_Object = MibScalar
pmoabphcAlmLineFail = _PmoabphcAlmLineFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 3, 3, 7, 12),
    _PmoabphcAlmLineFail_Type()
)
pmoabphcAlmLineFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmLineFail.setStatus("current")
_PmoabphcAlmLineExtPumpFail_Type = EkiOnOff
_PmoabphcAlmLineExtPumpFail_Object = MibScalar
pmoabphcAlmLineExtPumpFail = _PmoabphcAlmLineExtPumpFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 3, 3, 7, 13),
    _PmoabphcAlmLineExtPumpFail_Type()
)
pmoabphcAlmLineExtPumpFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmLineExtPumpFail.setStatus("current")
_PmoabphcAlmlineEdfaAlarms2_ObjectIdentity = ObjectIdentity
pmoabphcAlmlineEdfaAlarms2 = _PmoabphcAlmlineEdfaAlarms2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 3, 3, 43)
)
_PmoabphcAlmLineEdfaNr_Type = EkiOnOff
_PmoabphcAlmLineEdfaNr_Object = MibScalar
pmoabphcAlmLineEdfaNr = _PmoabphcAlmLineEdfaNr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 3, 3, 43, 1),
    _PmoabphcAlmLineEdfaNr_Type()
)
pmoabphcAlmLineEdfaNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmLineEdfaNr.setStatus("current")
_PmoabphcAlmLineEdfaTecFail_Type = EkiOnOff
_PmoabphcAlmLineEdfaTecFail_Object = MibScalar
pmoabphcAlmLineEdfaTecFail = _PmoabphcAlmLineEdfaTecFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 3, 3, 43, 2),
    _PmoabphcAlmLineEdfaTecFail_Type()
)
pmoabphcAlmLineEdfaTecFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmLineEdfaTecFail.setStatus("current")
_PmoabphcAlmLineEdfaLaserFail_Type = EkiOnOff
_PmoabphcAlmLineEdfaLaserFail_Object = MibScalar
pmoabphcAlmLineEdfaLaserFail = _PmoabphcAlmLineEdfaLaserFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 3, 3, 43, 3),
    _PmoabphcAlmLineEdfaLaserFail_Type()
)
pmoabphcAlmLineEdfaLaserFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmLineEdfaLaserFail.setStatus("current")
_PmoabphcAlmLineEdfaLos_Type = EkiOnOff
_PmoabphcAlmLineEdfaLos_Object = MibScalar
pmoabphcAlmLineEdfaLos = _PmoabphcAlmLineEdfaLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 3, 3, 43, 4),
    _PmoabphcAlmLineEdfaLos_Type()
)
pmoabphcAlmLineEdfaLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmLineEdfaLos.setStatus("current")
_PmoabphcAlmLineExtPumpEdfaLowCurrent_Type = EkiOnOff
_PmoabphcAlmLineExtPumpEdfaLowCurrent_Object = MibScalar
pmoabphcAlmLineExtPumpEdfaLowCurrent = _PmoabphcAlmLineExtPumpEdfaLowCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 2, 3, 3, 43, 5),
    _PmoabphcAlmLineExtPumpEdfaLowCurrent_Type()
)
pmoabphcAlmLineExtPumpEdfaLowCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcAlmLineExtPumpEdfaLowCurrent.setStatus("current")
_Pmoabphcmeasures_ObjectIdentity = ObjectIdentity
pmoabphcmeasures = _Pmoabphcmeasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 3)
)
_PmoabphcMesrOther_ObjectIdentity = ObjectIdentity
pmoabphcMesrOther = _PmoabphcMesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 3, 1)
)


class _PmoabphcMesrtempMeas_Type(Integer32):
    """Custom type pmoabphcMesrtempMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcMesrtempMeas_Type.__name__ = "Integer32"
_PmoabphcMesrtempMeas_Object = MibScalar
pmoabphcMesrtempMeas = _PmoabphcMesrtempMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 3, 1, 72),
    _PmoabphcMesrtempMeas_Type()
)
pmoabphcMesrtempMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcMesrtempMeas.setStatus("current")
_PmoabphcMesrClient_ObjectIdentity = ObjectIdentity
pmoabphcMesrClient = _PmoabphcMesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 3, 2)
)


class _PmoabphcMesrclientEdfaBiasMeas_Type(Integer32):
    """Custom type pmoabphcMesrclientEdfaBiasMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcMesrclientEdfaBiasMeas_Type.__name__ = "Integer32"
_PmoabphcMesrclientEdfaBiasMeas_Object = MibScalar
pmoabphcMesrclientEdfaBiasMeas = _PmoabphcMesrclientEdfaBiasMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 3, 2, 32),
    _PmoabphcMesrclientEdfaBiasMeas_Type()
)
pmoabphcMesrclientEdfaBiasMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcMesrclientEdfaBiasMeas.setStatus("current")


class _PmoabphcMesrclientEdfaTxpwrMeas_Type(Integer32):
    """Custom type pmoabphcMesrclientEdfaTxpwrMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcMesrclientEdfaTxpwrMeas_Type.__name__ = "Integer32"
_PmoabphcMesrclientEdfaTxpwrMeas_Object = MibScalar
pmoabphcMesrclientEdfaTxpwrMeas = _PmoabphcMesrclientEdfaTxpwrMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 3, 2, 33),
    _PmoabphcMesrclientEdfaTxpwrMeas_Type()
)
pmoabphcMesrclientEdfaTxpwrMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcMesrclientEdfaTxpwrMeas.setStatus("current")


class _PmoabphcMesrclientEdfaRxpwrMeas_Type(Integer32):
    """Custom type pmoabphcMesrclientEdfaRxpwrMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcMesrclientEdfaRxpwrMeas_Type.__name__ = "Integer32"
_PmoabphcMesrclientEdfaRxpwrMeas_Object = MibScalar
pmoabphcMesrclientEdfaRxpwrMeas = _PmoabphcMesrclientEdfaRxpwrMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 3, 2, 34),
    _PmoabphcMesrclientEdfaRxpwrMeas_Type()
)
pmoabphcMesrclientEdfaRxpwrMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcMesrclientEdfaRxpwrMeas.setStatus("current")


class _PmoabphcMesrclientEdfaGainMeas_Type(Integer32):
    """Custom type pmoabphcMesrclientEdfaGainMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcMesrclientEdfaGainMeas_Type.__name__ = "Integer32"
_PmoabphcMesrclientEdfaGainMeas_Object = MibScalar
pmoabphcMesrclientEdfaGainMeas = _PmoabphcMesrclientEdfaGainMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 3, 2, 35),
    _PmoabphcMesrclientEdfaGainMeas_Type()
)
pmoabphcMesrclientEdfaGainMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcMesrclientEdfaGainMeas.setStatus("current")


class _PmoabphcMesrclientCorrectedGain_Type(Integer32):
    """Custom type pmoabphcMesrclientCorrectedGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcMesrclientCorrectedGain_Type.__name__ = "Integer32"
_PmoabphcMesrclientCorrectedGain_Object = MibScalar
pmoabphcMesrclientCorrectedGain = _PmoabphcMesrclientCorrectedGain_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 3, 2, 38),
    _PmoabphcMesrclientCorrectedGain_Type()
)
pmoabphcMesrclientCorrectedGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcMesrclientCorrectedGain.setStatus("current")
_PmoabphcMesrLine_ObjectIdentity = ObjectIdentity
pmoabphcMesrLine = _PmoabphcMesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 3, 3)
)


class _PmoabphcMesrlineEdfaBiasMeas_Type(Integer32):
    """Custom type pmoabphcMesrlineEdfaBiasMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcMesrlineEdfaBiasMeas_Type.__name__ = "Integer32"
_PmoabphcMesrlineEdfaBiasMeas_Object = MibScalar
pmoabphcMesrlineEdfaBiasMeas = _PmoabphcMesrlineEdfaBiasMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 3, 3, 40),
    _PmoabphcMesrlineEdfaBiasMeas_Type()
)
pmoabphcMesrlineEdfaBiasMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcMesrlineEdfaBiasMeas.setStatus("current")


class _PmoabphcMesrlineEdfaTxpwrMeas_Type(Integer32):
    """Custom type pmoabphcMesrlineEdfaTxpwrMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcMesrlineEdfaTxpwrMeas_Type.__name__ = "Integer32"
_PmoabphcMesrlineEdfaTxpwrMeas_Object = MibScalar
pmoabphcMesrlineEdfaTxpwrMeas = _PmoabphcMesrlineEdfaTxpwrMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 3, 3, 41),
    _PmoabphcMesrlineEdfaTxpwrMeas_Type()
)
pmoabphcMesrlineEdfaTxpwrMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcMesrlineEdfaTxpwrMeas.setStatus("current")


class _PmoabphcMesrlineEdfaRxpwrMeas_Type(Integer32):
    """Custom type pmoabphcMesrlineEdfaRxpwrMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcMesrlineEdfaRxpwrMeas_Type.__name__ = "Integer32"
_PmoabphcMesrlineEdfaRxpwrMeas_Object = MibScalar
pmoabphcMesrlineEdfaRxpwrMeas = _PmoabphcMesrlineEdfaRxpwrMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 3, 3, 42),
    _PmoabphcMesrlineEdfaRxpwrMeas_Type()
)
pmoabphcMesrlineEdfaRxpwrMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcMesrlineEdfaRxpwrMeas.setStatus("current")


class _PmoabphcMesrlineEdfaGainMeas_Type(Integer32):
    """Custom type pmoabphcMesrlineEdfaGainMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcMesrlineEdfaGainMeas_Type.__name__ = "Integer32"
_PmoabphcMesrlineEdfaGainMeas_Object = MibScalar
pmoabphcMesrlineEdfaGainMeas = _PmoabphcMesrlineEdfaGainMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 3, 3, 43),
    _PmoabphcMesrlineEdfaGainMeas_Type()
)
pmoabphcMesrlineEdfaGainMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcMesrlineEdfaGainMeas.setStatus("current")


class _PmoabphcMesrlineCorrectedGain_Type(Integer32):
    """Custom type pmoabphcMesrlineCorrectedGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcMesrlineCorrectedGain_Type.__name__ = "Integer32"
_PmoabphcMesrlineCorrectedGain_Object = MibScalar
pmoabphcMesrlineCorrectedGain = _PmoabphcMesrlineCorrectedGain_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 3, 3, 46),
    _PmoabphcMesrlineCorrectedGain_Type()
)
pmoabphcMesrlineCorrectedGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcMesrlineCorrectedGain.setStatus("current")
_PmoabphccontrolsWrite_ObjectIdentity = ObjectIdentity
pmoabphccontrolsWrite = _PmoabphccontrolsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 6)
)
_PmoabphcCtrlOther_ObjectIdentity = ObjectIdentity
pmoabphcCtrlOther = _PmoabphcCtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 6, 1)
)
_PmoabphcCtrlsynth0_ObjectIdentity = ObjectIdentity
pmoabphcCtrlsynth0 = _PmoabphcCtrlsynth0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 6, 1, 0)
)
_PmoabphcCtrlConfLoad_Type = EkiOnOff
_PmoabphcCtrlConfLoad_Object = MibScalar
pmoabphcCtrlConfLoad = _PmoabphcCtrlConfLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 6, 1, 0, 1),
    _PmoabphcCtrlConfLoad_Type()
)
pmoabphcCtrlConfLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCtrlConfLoad.setStatus("current")
_PmoabphcCtrlConfFlash_Type = EkiOnOff
_PmoabphcCtrlConfFlash_Object = MibScalar
pmoabphcCtrlConfFlash = _PmoabphcCtrlConfFlash_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 6, 1, 0, 9),
    _PmoabphcCtrlConfFlash_Type()
)
pmoabphcCtrlConfFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCtrlConfFlash.setStatus("current")
_PmoabphcCtrlConfClear_Type = EkiOnOff
_PmoabphcCtrlConfClear_Object = MibScalar
pmoabphcCtrlConfClear = _PmoabphcCtrlConfClear_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 6, 1, 0, 13),
    _PmoabphcCtrlConfClear_Type()
)
pmoabphcCtrlConfClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCtrlConfClear.setStatus("current")
_PmoabphcCtrlswMgnt_ObjectIdentity = ObjectIdentity
pmoabphcCtrlswMgnt = _PmoabphcCtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 6, 1, 5)
)
_PmoabphcCtrlColdReset_Type = EkiOnOff
_PmoabphcCtrlColdReset_Object = MibScalar
pmoabphcCtrlColdReset = _PmoabphcCtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 6, 1, 5, 2),
    _PmoabphcCtrlColdReset_Type()
)
pmoabphcCtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCtrlColdReset.setStatus("current")
_PmoabphcCtrlWarmReset_Type = EkiOnOff
_PmoabphcCtrlWarmReset_Object = MibScalar
pmoabphcCtrlWarmReset = _PmoabphcCtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 6, 1, 5, 3),
    _PmoabphcCtrlWarmReset_Type()
)
pmoabphcCtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCtrlWarmReset.setStatus("current")
_PmoabphcCtrlledTest_ObjectIdentity = ObjectIdentity
pmoabphcCtrlledTest = _PmoabphcCtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 6, 1, 73)
)
_PmoabphcCtrlGreenLed_Type = EkiOnOff
_PmoabphcCtrlGreenLed_Object = MibScalar
pmoabphcCtrlGreenLed = _PmoabphcCtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 6, 1, 73, 1),
    _PmoabphcCtrlGreenLed_Type()
)
pmoabphcCtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCtrlGreenLed.setStatus("current")
_PmoabphcCtrlRedLed_Type = EkiOnOff
_PmoabphcCtrlRedLed_Object = MibScalar
pmoabphcCtrlRedLed = _PmoabphcCtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 6, 1, 73, 2),
    _PmoabphcCtrlRedLed_Type()
)
pmoabphcCtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCtrlRedLed.setStatus("current")
_PmoabphcCtrlLedOff_Type = EkiOnOff
_PmoabphcCtrlLedOff_Object = MibScalar
pmoabphcCtrlLedOff = _PmoabphcCtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 6, 1, 73, 3),
    _PmoabphcCtrlLedOff_Type()
)
pmoabphcCtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCtrlLedOff.setStatus("current")
_PmoabphcCtrlmaintMode_ObjectIdentity = ObjectIdentity
pmoabphcCtrlmaintMode = _PmoabphcCtrlmaintMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 6, 1, 75)
)
_PmoabphcCtrlMaintenance_Type = EkiOnOff
_PmoabphcCtrlMaintenance_Object = MibScalar
pmoabphcCtrlMaintenance = _PmoabphcCtrlMaintenance_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 6, 1, 75, 1),
    _PmoabphcCtrlMaintenance_Type()
)
pmoabphcCtrlMaintenance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCtrlMaintenance.setStatus("current")
_PmoabphcCtrlaprRestart_ObjectIdentity = ObjectIdentity
pmoabphcCtrlaprRestart = _PmoabphcCtrlaprRestart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 6, 1, 76)
)
_PmoabphcCtrlAprManualRestart_Type = EkiOnOff
_PmoabphcCtrlAprManualRestart_Object = MibScalar
pmoabphcCtrlAprManualRestart = _PmoabphcCtrlAprManualRestart_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 6, 1, 76, 1),
    _PmoabphcCtrlAprManualRestart_Type()
)
pmoabphcCtrlAprManualRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCtrlAprManualRestart.setStatus("current")
_PmoabphcCtrlClient_ObjectIdentity = ObjectIdentity
pmoabphcCtrlClient = _PmoabphcCtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 6, 2)
)
_PmoabphcCtrlclientEdfaLaserOff_ObjectIdentity = ObjectIdentity
pmoabphcCtrlclientEdfaLaserOff = _PmoabphcCtrlclientEdfaLaserOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 6, 2, 32)
)
_PmoabphcCtrlClientEdfaLaserOff_Type = EkiOnOff
_PmoabphcCtrlClientEdfaLaserOff_Object = MibScalar
pmoabphcCtrlClientEdfaLaserOff = _PmoabphcCtrlClientEdfaLaserOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 6, 2, 32, 1),
    _PmoabphcCtrlClientEdfaLaserOff_Type()
)
pmoabphcCtrlClientEdfaLaserOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCtrlClientEdfaLaserOff.setStatus("current")


class _PmoabphcCtrlclientGainCstMonitorValue_Type(Integer32):
    """Custom type pmoabphcCtrlclientGainCstMonitorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcCtrlclientGainCstMonitorValue_Type.__name__ = "Integer32"
_PmoabphcCtrlclientGainCstMonitorValue_Object = MibScalar
pmoabphcCtrlclientGainCstMonitorValue = _PmoabphcCtrlclientGainCstMonitorValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 6, 2, 34),
    _PmoabphcCtrlclientGainCstMonitorValue_Type()
)
pmoabphcCtrlclientGainCstMonitorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCtrlclientGainCstMonitorValue.setStatus("current")


class _PmoabphcCtrlclientGainCstPoutValue_Type(Integer32):
    """Custom type pmoabphcCtrlclientGainCstPoutValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcCtrlclientGainCstPoutValue_Type.__name__ = "Integer32"
_PmoabphcCtrlclientGainCstPoutValue_Object = MibScalar
pmoabphcCtrlclientGainCstPoutValue = _PmoabphcCtrlclientGainCstPoutValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 6, 2, 35),
    _PmoabphcCtrlclientGainCstPoutValue_Type()
)
pmoabphcCtrlclientGainCstPoutValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCtrlclientGainCstPoutValue.setStatus("current")


class _PmoabphcCtrlclientGainSettingValue_Type(Integer32):
    """Custom type pmoabphcCtrlclientGainSettingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcCtrlclientGainSettingValue_Type.__name__ = "Integer32"
_PmoabphcCtrlclientGainSettingValue_Object = MibScalar
pmoabphcCtrlclientGainSettingValue = _PmoabphcCtrlclientGainSettingValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 6, 2, 36),
    _PmoabphcCtrlclientGainSettingValue_Type()
)
pmoabphcCtrlclientGainSettingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCtrlclientGainSettingValue.setStatus("current")
_PmoabphcCtrlclientGainProcessing_ObjectIdentity = ObjectIdentity
pmoabphcCtrlclientGainProcessing = _PmoabphcCtrlclientGainProcessing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 6, 2, 37)
)
_PmoabphcCtrlClientGainProc_Type = EkiOnOff
_PmoabphcCtrlClientGainProc_Object = MibScalar
pmoabphcCtrlClientGainProc = _PmoabphcCtrlClientGainProc_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 6, 2, 37, 1),
    _PmoabphcCtrlClientGainProc_Type()
)
pmoabphcCtrlClientGainProc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCtrlClientGainProc.setStatus("current")


class _PmoabphcCtrlclientGainCstFiberAgingMarginValue_Type(Integer32):
    """Custom type pmoabphcCtrlclientGainCstFiberAgingMarginValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcCtrlclientGainCstFiberAgingMarginValue_Type.__name__ = "Integer32"
_PmoabphcCtrlclientGainCstFiberAgingMarginValue_Object = MibScalar
pmoabphcCtrlclientGainCstFiberAgingMarginValue = _PmoabphcCtrlclientGainCstFiberAgingMarginValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 6, 2, 38),
    _PmoabphcCtrlclientGainCstFiberAgingMarginValue_Type()
)
pmoabphcCtrlclientGainCstFiberAgingMarginValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCtrlclientGainCstFiberAgingMarginValue.setStatus("current")


class _PmoabphcCtrlclientGainCstAdddropMarginValue_Type(Integer32):
    """Custom type pmoabphcCtrlclientGainCstAdddropMarginValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcCtrlclientGainCstAdddropMarginValue_Type.__name__ = "Integer32"
_PmoabphcCtrlclientGainCstAdddropMarginValue_Object = MibScalar
pmoabphcCtrlclientGainCstAdddropMarginValue = _PmoabphcCtrlclientGainCstAdddropMarginValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 6, 2, 39),
    _PmoabphcCtrlclientGainCstAdddropMarginValue_Type()
)
pmoabphcCtrlclientGainCstAdddropMarginValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCtrlclientGainCstAdddropMarginValue.setStatus("current")
_PmoabphcCtrlLine_ObjectIdentity = ObjectIdentity
pmoabphcCtrlLine = _PmoabphcCtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 6, 3)
)
_PmoabphcCtrllineEdfaLaserOff_ObjectIdentity = ObjectIdentity
pmoabphcCtrllineEdfaLaserOff = _PmoabphcCtrllineEdfaLaserOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 6, 3, 40)
)
_PmoabphcCtrlLineEdfaLaserOff_Type = EkiOnOff
_PmoabphcCtrlLineEdfaLaserOff_Object = MibScalar
pmoabphcCtrlLineEdfaLaserOff = _PmoabphcCtrlLineEdfaLaserOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 6, 3, 40, 1),
    _PmoabphcCtrlLineEdfaLaserOff_Type()
)
pmoabphcCtrlLineEdfaLaserOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCtrlLineEdfaLaserOff.setStatus("current")


class _PmoabphcCtrllineGainCstMonitorValue_Type(Integer32):
    """Custom type pmoabphcCtrllineGainCstMonitorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcCtrllineGainCstMonitorValue_Type.__name__ = "Integer32"
_PmoabphcCtrllineGainCstMonitorValue_Object = MibScalar
pmoabphcCtrllineGainCstMonitorValue = _PmoabphcCtrllineGainCstMonitorValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 6, 3, 42),
    _PmoabphcCtrllineGainCstMonitorValue_Type()
)
pmoabphcCtrllineGainCstMonitorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCtrllineGainCstMonitorValue.setStatus("current")


class _PmoabphcCtrllineGainCstPoutValue_Type(Integer32):
    """Custom type pmoabphcCtrllineGainCstPoutValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcCtrllineGainCstPoutValue_Type.__name__ = "Integer32"
_PmoabphcCtrllineGainCstPoutValue_Object = MibScalar
pmoabphcCtrllineGainCstPoutValue = _PmoabphcCtrllineGainCstPoutValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 6, 3, 43),
    _PmoabphcCtrllineGainCstPoutValue_Type()
)
pmoabphcCtrllineGainCstPoutValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCtrllineGainCstPoutValue.setStatus("current")


class _PmoabphcCtrllineGainSettingValue_Type(Integer32):
    """Custom type pmoabphcCtrllineGainSettingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcCtrllineGainSettingValue_Type.__name__ = "Integer32"
_PmoabphcCtrllineGainSettingValue_Object = MibScalar
pmoabphcCtrllineGainSettingValue = _PmoabphcCtrllineGainSettingValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 6, 3, 44),
    _PmoabphcCtrllineGainSettingValue_Type()
)
pmoabphcCtrllineGainSettingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCtrllineGainSettingValue.setStatus("current")
_PmoabphcCtrllineGainProcessing_ObjectIdentity = ObjectIdentity
pmoabphcCtrllineGainProcessing = _PmoabphcCtrllineGainProcessing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 6, 3, 45)
)
_PmoabphcCtrlLineGainProc_Type = EkiOnOff
_PmoabphcCtrlLineGainProc_Object = MibScalar
pmoabphcCtrlLineGainProc = _PmoabphcCtrlLineGainProc_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 6, 3, 45, 1),
    _PmoabphcCtrlLineGainProc_Type()
)
pmoabphcCtrlLineGainProc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCtrlLineGainProc.setStatus("current")


class _PmoabphcCtrllineGainCstFiberAgingMarginValue_Type(Integer32):
    """Custom type pmoabphcCtrllineGainCstFiberAgingMarginValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcCtrllineGainCstFiberAgingMarginValue_Type.__name__ = "Integer32"
_PmoabphcCtrllineGainCstFiberAgingMarginValue_Object = MibScalar
pmoabphcCtrllineGainCstFiberAgingMarginValue = _PmoabphcCtrllineGainCstFiberAgingMarginValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 6, 3, 46),
    _PmoabphcCtrllineGainCstFiberAgingMarginValue_Type()
)
pmoabphcCtrllineGainCstFiberAgingMarginValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCtrllineGainCstFiberAgingMarginValue.setStatus("current")


class _PmoabphcCtrllineGainCstAdddropMarginValue_Type(Integer32):
    """Custom type pmoabphcCtrllineGainCstAdddropMarginValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoabphcCtrllineGainCstAdddropMarginValue_Type.__name__ = "Integer32"
_PmoabphcCtrllineGainCstAdddropMarginValue_Object = MibScalar
pmoabphcCtrllineGainCstAdddropMarginValue = _PmoabphcCtrllineGainCstAdddropMarginValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 6, 3, 47),
    _PmoabphcCtrllineGainCstAdddropMarginValue_Type()
)
pmoabphcCtrllineGainCstAdddropMarginValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCtrllineGainCstAdddropMarginValue.setStatus("current")
_Pmoabphcri_ObjectIdentity = ObjectIdentity
pmoabphcri = _Pmoabphcri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 7)
)
_PmoabphcRinvReloadInventory_Type = EkiOnOff
_PmoabphcRinvReloadInventory_Object = MibScalar
pmoabphcRinvReloadInventory = _PmoabphcRinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 7, 2),
    _PmoabphcRinvReloadInventory_Type()
)
pmoabphcRinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcRinvReloadInventory.setStatus("current")
_PmoabphcRinvModulePlatform_Type = DisplayString
_PmoabphcRinvModulePlatform_Object = MibScalar
pmoabphcRinvModulePlatform = _PmoabphcRinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 7, 3),
    _PmoabphcRinvModulePlatform_Type()
)
pmoabphcRinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcRinvModulePlatform.setStatus("current")
_PmoabphcRinvSwPlatform_Type = DisplayString
_PmoabphcRinvSwPlatform_Object = MibScalar
pmoabphcRinvSwPlatform = _PmoabphcRinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 7, 4),
    _PmoabphcRinvSwPlatform_Type()
)
pmoabphcRinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcRinvSwPlatform.setStatus("current")
_PmoabphcRinvSwFoa_Type = DisplayString
_PmoabphcRinvSwFoa_Object = MibScalar
pmoabphcRinvSwFoa = _PmoabphcRinvSwFoa_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 7, 5),
    _PmoabphcRinvSwFoa_Type()
)
pmoabphcRinvSwFoa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcRinvSwFoa.setStatus("current")
_PmoabphcRinvBoosterTable_Object = MibTable
pmoabphcRinvBoosterTable = _PmoabphcRinvBoosterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 7, 6)
)
if mibBuilder.loadTexts:
    pmoabphcRinvBoosterTable.setStatus("current")
_PmoabphcRinvBoosterEntry_Object = MibTableRow
pmoabphcRinvBoosterEntry = _PmoabphcRinvBoosterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 7, 6, 1)
)
pmoabphcRinvBoosterEntry.setIndexNames(
    (0, "EKINOPS-PmOabphc-MIB", "pmoabphcRinvBoosterIndex"),
)
if mibBuilder.loadTexts:
    pmoabphcRinvBoosterEntry.setStatus("current")


class _PmoabphcRinvBoosterIndex_Type(Integer32):
    """Custom type pmoabphcRinvBoosterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PmoabphcRinvBoosterIndex_Type.__name__ = "Integer32"
_PmoabphcRinvBoosterIndex_Object = MibTableColumn
pmoabphcRinvBoosterIndex = _PmoabphcRinvBoosterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 7, 6, 1, 1),
    _PmoabphcRinvBoosterIndex_Type()
)
pmoabphcRinvBoosterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcRinvBoosterIndex.setStatus("current")
_PmoabphcRinvBooster_Type = DisplayString
_PmoabphcRinvBooster_Object = MibTableColumn
pmoabphcRinvBooster = _PmoabphcRinvBooster_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 7, 6, 1, 2),
    _PmoabphcRinvBooster_Type()
)
pmoabphcRinvBooster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcRinvBooster.setStatus("current")
_PmoabphcRinvPreAmpTable_Object = MibTable
pmoabphcRinvPreAmpTable = _PmoabphcRinvPreAmpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 7, 7)
)
if mibBuilder.loadTexts:
    pmoabphcRinvPreAmpTable.setStatus("current")
_PmoabphcRinvPreAmpEntry_Object = MibTableRow
pmoabphcRinvPreAmpEntry = _PmoabphcRinvPreAmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 7, 7, 1)
)
pmoabphcRinvPreAmpEntry.setIndexNames(
    (0, "EKINOPS-PmOabphc-MIB", "pmoabphcRinvPreAmpIndex"),
)
if mibBuilder.loadTexts:
    pmoabphcRinvPreAmpEntry.setStatus("current")


class _PmoabphcRinvPreAmpIndex_Type(Integer32):
    """Custom type pmoabphcRinvPreAmpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PmoabphcRinvPreAmpIndex_Type.__name__ = "Integer32"
_PmoabphcRinvPreAmpIndex_Object = MibTableColumn
pmoabphcRinvPreAmpIndex = _PmoabphcRinvPreAmpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 7, 7, 1, 1),
    _PmoabphcRinvPreAmpIndex_Type()
)
pmoabphcRinvPreAmpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcRinvPreAmpIndex.setStatus("current")
_PmoabphcRinvPreAmp_Type = DisplayString
_PmoabphcRinvPreAmp_Object = MibTableColumn
pmoabphcRinvPreAmp = _PmoabphcRinvPreAmp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 7, 7, 1, 2),
    _PmoabphcRinvPreAmp_Type()
)
pmoabphcRinvPreAmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcRinvPreAmp.setStatus("current")
_PmoabphcConfig_ObjectIdentity = ObjectIdentity
pmoabphcConfig = _PmoabphcConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 9)
)
_PmoabphcCfgNoValue_ObjectIdentity = ObjectIdentity
pmoabphcCfgNoValue = _PmoabphcCfgNoValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 9, 1)
)
_PmoabphctableclientStartup_ObjectIdentity = ObjectIdentity
pmoabphctableclientStartup = _PmoabphctableclientStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 9, 1, 1)
)


class _PmoabphcCfgclientEdfaLaserCtrl_Type(Unsigned32):
    """Custom type pmoabphcCfgclientEdfaLaserCtrl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoabphcCfgclientEdfaLaserCtrl_Type.__name__ = "Unsigned32"
_PmoabphcCfgclientEdfaLaserCtrl_Object = MibScalar
pmoabphcCfgclientEdfaLaserCtrl = _PmoabphcCfgclientEdfaLaserCtrl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 9, 1, 1, 2),
    _PmoabphcCfgclientEdfaLaserCtrl_Type()
)
pmoabphcCfgclientEdfaLaserCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCfgclientEdfaLaserCtrl.setStatus("current")


class _PmoabphcCfgclientEdfaLaserMode_Type(Unsigned32):
    """Custom type pmoabphcCfgclientEdfaLaserMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoabphcCfgclientEdfaLaserMode_Type.__name__ = "Unsigned32"
_PmoabphcCfgclientEdfaLaserMode_Object = MibScalar
pmoabphcCfgclientEdfaLaserMode = _PmoabphcCfgclientEdfaLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 9, 1, 1, 3),
    _PmoabphcCfgclientEdfaLaserMode_Type()
)
pmoabphcCfgclientEdfaLaserMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCfgclientEdfaLaserMode.setStatus("current")


class _PmoabphcCfgclientGainValue_Type(Unsigned32):
    """Custom type pmoabphcCfgclientGainValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoabphcCfgclientGainValue_Type.__name__ = "Unsigned32"
_PmoabphcCfgclientGainValue_Object = MibScalar
pmoabphcCfgclientGainValue = _PmoabphcCfgclientGainValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 9, 1, 1, 4),
    _PmoabphcCfgclientGainValue_Type()
)
pmoabphcCfgclientGainValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCfgclientGainValue.setStatus("current")


class _PmoabphcCfgclientTiltValue_Type(Unsigned32):
    """Custom type pmoabphcCfgclientTiltValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoabphcCfgclientTiltValue_Type.__name__ = "Unsigned32"
_PmoabphcCfgclientTiltValue_Object = MibScalar
pmoabphcCfgclientTiltValue = _PmoabphcCfgclientTiltValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 9, 1, 1, 5),
    _PmoabphcCfgclientTiltValue_Type()
)
pmoabphcCfgclientTiltValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCfgclientTiltValue.setStatus("current")


class _PmoabphcCfgclientMsaLoss_Type(Unsigned32):
    """Custom type pmoabphcCfgclientMsaLoss based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoabphcCfgclientMsaLoss_Type.__name__ = "Unsigned32"
_PmoabphcCfgclientMsaLoss_Object = MibScalar
pmoabphcCfgclientMsaLoss = _PmoabphcCfgclientMsaLoss_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 9, 1, 1, 6),
    _PmoabphcCfgclientMsaLoss_Type()
)
pmoabphcCfgclientMsaLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCfgclientMsaLoss.setStatus("current")


class _PmoabphcCfgclientOutputPowerValue_Type(Unsigned32):
    """Custom type pmoabphcCfgclientOutputPowerValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoabphcCfgclientOutputPowerValue_Type.__name__ = "Unsigned32"
_PmoabphcCfgclientOutputPowerValue_Object = MibScalar
pmoabphcCfgclientOutputPowerValue = _PmoabphcCfgclientOutputPowerValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 9, 1, 1, 7),
    _PmoabphcCfgclientOutputPowerValue_Type()
)
pmoabphcCfgclientOutputPowerValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCfgclientOutputPowerValue.setStatus("current")


class _PmoabphcCfgclientAseCompensation_Type(Unsigned32):
    """Custom type pmoabphcCfgclientAseCompensation based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoabphcCfgclientAseCompensation_Type.__name__ = "Unsigned32"
_PmoabphcCfgclientAseCompensation_Object = MibScalar
pmoabphcCfgclientAseCompensation = _PmoabphcCfgclientAseCompensation_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 9, 1, 1, 8),
    _PmoabphcCfgclientAseCompensation_Type()
)
pmoabphcCfgclientAseCompensation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCfgclientAseCompensation.setStatus("current")
_PmoabphcCfgLineStartUp_ObjectIdentity = ObjectIdentity
pmoabphcCfgLineStartUp = _PmoabphcCfgLineStartUp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 9, 2)
)
_PmoabphctablelineStartup_ObjectIdentity = ObjectIdentity
pmoabphctablelineStartup = _PmoabphctablelineStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 9, 2, 1)
)


class _PmoabphcCfglineEdfaLaserCtrl_Type(Unsigned32):
    """Custom type pmoabphcCfglineEdfaLaserCtrl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoabphcCfglineEdfaLaserCtrl_Type.__name__ = "Unsigned32"
_PmoabphcCfglineEdfaLaserCtrl_Object = MibScalar
pmoabphcCfglineEdfaLaserCtrl = _PmoabphcCfglineEdfaLaserCtrl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 9, 2, 1, 2),
    _PmoabphcCfglineEdfaLaserCtrl_Type()
)
pmoabphcCfglineEdfaLaserCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCfglineEdfaLaserCtrl.setStatus("current")


class _PmoabphcCfglineEdfaLaserMode_Type(Unsigned32):
    """Custom type pmoabphcCfglineEdfaLaserMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoabphcCfglineEdfaLaserMode_Type.__name__ = "Unsigned32"
_PmoabphcCfglineEdfaLaserMode_Object = MibScalar
pmoabphcCfglineEdfaLaserMode = _PmoabphcCfglineEdfaLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 9, 2, 1, 3),
    _PmoabphcCfglineEdfaLaserMode_Type()
)
pmoabphcCfglineEdfaLaserMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCfglineEdfaLaserMode.setStatus("current")


class _PmoabphcCfglineGainValue_Type(Unsigned32):
    """Custom type pmoabphcCfglineGainValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoabphcCfglineGainValue_Type.__name__ = "Unsigned32"
_PmoabphcCfglineGainValue_Object = MibScalar
pmoabphcCfglineGainValue = _PmoabphcCfglineGainValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 9, 2, 1, 4),
    _PmoabphcCfglineGainValue_Type()
)
pmoabphcCfglineGainValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCfglineGainValue.setStatus("current")


class _PmoabphcCfglineTiltValue_Type(Unsigned32):
    """Custom type pmoabphcCfglineTiltValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoabphcCfglineTiltValue_Type.__name__ = "Unsigned32"
_PmoabphcCfglineTiltValue_Object = MibScalar
pmoabphcCfglineTiltValue = _PmoabphcCfglineTiltValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 9, 2, 1, 5),
    _PmoabphcCfglineTiltValue_Type()
)
pmoabphcCfglineTiltValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCfglineTiltValue.setStatus("current")


class _PmoabphcCfglineMsaLoss_Type(Unsigned32):
    """Custom type pmoabphcCfglineMsaLoss based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoabphcCfglineMsaLoss_Type.__name__ = "Unsigned32"
_PmoabphcCfglineMsaLoss_Object = MibScalar
pmoabphcCfglineMsaLoss = _PmoabphcCfglineMsaLoss_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 9, 2, 1, 6),
    _PmoabphcCfglineMsaLoss_Type()
)
pmoabphcCfglineMsaLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCfglineMsaLoss.setStatus("current")


class _PmoabphcCfglineOutputPowerValue_Type(Unsigned32):
    """Custom type pmoabphcCfglineOutputPowerValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoabphcCfglineOutputPowerValue_Type.__name__ = "Unsigned32"
_PmoabphcCfglineOutputPowerValue_Object = MibScalar
pmoabphcCfglineOutputPowerValue = _PmoabphcCfglineOutputPowerValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 9, 2, 1, 7),
    _PmoabphcCfglineOutputPowerValue_Type()
)
pmoabphcCfglineOutputPowerValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCfglineOutputPowerValue.setStatus("current")


class _PmoabphcCfglineAseCompensation_Type(Unsigned32):
    """Custom type pmoabphcCfglineAseCompensation based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoabphcCfglineAseCompensation_Type.__name__ = "Unsigned32"
_PmoabphcCfglineAseCompensation_Object = MibScalar
pmoabphcCfglineAseCompensation = _PmoabphcCfglineAseCompensation_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 9, 2, 1, 8),
    _PmoabphcCfglineAseCompensation_Type()
)
pmoabphcCfglineAseCompensation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCfglineAseCompensation.setStatus("current")


class _PmoabphcCfgaprMode_Type(Unsigned32):
    """Custom type pmoabphcCfgaprMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoabphcCfgaprMode_Type.__name__ = "Unsigned32"
_PmoabphcCfgaprMode_Object = MibScalar
pmoabphcCfgaprMode = _PmoabphcCfgaprMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 9, 2, 1, 11),
    _PmoabphcCfgaprMode_Type()
)
pmoabphcCfgaprMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCfgaprMode.setStatus("current")
_PmoabphcCfgLabels_ObjectIdentity = ObjectIdentity
pmoabphcCfgLabels = _PmoabphcCfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 9, 3)
)
_PmoabphcCfgLabelclientTable_Object = MibTable
pmoabphcCfgLabelclientTable = _PmoabphcCfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 9, 3, 1)
)
if mibBuilder.loadTexts:
    pmoabphcCfgLabelclientTable.setStatus("current")
_PmoabphcCfgLabelclientEntry_Object = MibTableRow
pmoabphcCfgLabelclientEntry = _PmoabphcCfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 9, 3, 1, 1)
)
pmoabphcCfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-PmOabphc-MIB", "pmoabphcCfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pmoabphcCfgLabelclientEntry.setStatus("current")


class _PmoabphcCfgLabelclientIndex_Type(Integer32):
    """Custom type pmoabphcCfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmoabphcCfgLabelclientIndex_Type.__name__ = "Integer32"
_PmoabphcCfgLabelclientIndex_Object = MibTableColumn
pmoabphcCfgLabelclientIndex = _PmoabphcCfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 9, 3, 1, 1, 1),
    _PmoabphcCfgLabelclientIndex_Type()
)
pmoabphcCfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcCfgLabelclientIndex.setStatus("current")


class _PmoabphcCfgLabelclientPortn_Type(DisplayString):
    """Custom type pmoabphcCfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PmoabphcCfgLabelclientPortn_Type.__name__ = "DisplayString"
_PmoabphcCfgLabelclientPortn_Object = MibTableColumn
pmoabphcCfgLabelclientPortn = _PmoabphcCfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 9, 3, 1, 1, 3),
    _PmoabphcCfgLabelclientPortn_Type()
)
pmoabphcCfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCfgLabelclientPortn.setStatus("current")
_PmoabphcCfgLabellineTable_Object = MibTable
pmoabphcCfgLabellineTable = _PmoabphcCfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 9, 3, 2)
)
if mibBuilder.loadTexts:
    pmoabphcCfgLabellineTable.setStatus("current")
_PmoabphcCfgLabellineEntry_Object = MibTableRow
pmoabphcCfgLabellineEntry = _PmoabphcCfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 9, 3, 2, 1)
)
pmoabphcCfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-PmOabphc-MIB", "pmoabphcCfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pmoabphcCfgLabellineEntry.setStatus("current")


class _PmoabphcCfgLabellineIndex_Type(Integer32):
    """Custom type pmoabphcCfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmoabphcCfgLabellineIndex_Type.__name__ = "Integer32"
_PmoabphcCfgLabellineIndex_Object = MibTableColumn
pmoabphcCfgLabellineIndex = _PmoabphcCfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 9, 3, 2, 1, 1),
    _PmoabphcCfgLabellineIndex_Type()
)
pmoabphcCfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphcCfgLabellineIndex.setStatus("current")


class _PmoabphcCfgLabellinePortn_Type(DisplayString):
    """Custom type pmoabphcCfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PmoabphcCfgLabellinePortn_Type.__name__ = "DisplayString"
_PmoabphcCfgLabellinePortn_Object = MibTableColumn
pmoabphcCfgLabellinePortn = _PmoabphcCfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 9, 3, 2, 1, 3),
    _PmoabphcCfgLabellinePortn_Type()
)
pmoabphcCfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCfgLabellinePortn.setStatus("current")
_PmoabphcCfgWriteConfiguration_Type = EkiOnOff
_PmoabphcCfgWriteConfiguration_Object = MibScalar
pmoabphcCfgWriteConfiguration = _PmoabphcCfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 9, 257),
    _PmoabphcCfgWriteConfiguration_Type()
)
pmoabphcCfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoabphcCfgWriteConfiguration.setStatus("current")
_Pmoabphctraps_ObjectIdentity = ObjectIdentity
pmoabphctraps = _Pmoabphctraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 51, 10)
)


class _PmoabphctrapBoardNumber_Type(Integer32):
    """Custom type pmoabphctrapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_PmoabphctrapBoardNumber_Type.__name__ = "Integer32"
_PmoabphctrapBoardNumber_Object = MibScalar
pmoabphctrapBoardNumber = _PmoabphctrapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 51, 10, 4),
    _PmoabphctrapBoardNumber_Type()
)
pmoabphctrapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoabphctrapBoardNumber.setStatus("current")

# Managed Objects groups


# Notification objects

pmoabphcLineTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 51, 10, 30)
)
pmoabphcLineTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-PmOabphc-MIB", "pmoabphcAlmLineDdmWarning"),
        ("EKINOPS-PmOabphc-MIB", "pmoabphctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoabphcLineTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pmoabphcLineTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 51, 10, 31)
)
pmoabphcLineTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-PmOabphc-MIB", "pmoabphcAlmLineDdmWarning"),
        ("EKINOPS-PmOabphc-MIB", "pmoabphctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoabphcLineTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pmoabphcLineTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 51, 10, 32)
)
pmoabphcLineTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-PmOabphc-MIB", "pmoabphcAlmLineDdmAlm"),
        ("EKINOPS-PmOabphc-MIB", "pmoabphctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoabphcLineTrapUrgentGoesOn.setStatus(
        "current"
    )

pmoabphcLineTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 51, 10, 33)
)
pmoabphcLineTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-PmOabphc-MIB", "pmoabphcAlmLineDdmAlm"),
        ("EKINOPS-PmOabphc-MIB", "pmoabphctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoabphcLineTrapUrgentGoesOff.setStatus(
        "current"
    )

pmoabphcLineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 51, 10, 34)
)
pmoabphcLineTrapCritGoesOn.setObjects(
      *(("EKINOPS-PmOabphc-MIB", "pmoabphcAlmLineFail"),
        ("EKINOPS-PmOabphc-MIB", "pmoabphcAlmLineHwFail"),
        ("EKINOPS-PmOabphc-MIB", "pmoabphctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoabphcLineTrapCritGoesOn.setStatus(
        "current"
    )

pmoabphcLineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 51, 10, 35)
)
pmoabphcLineTrapCritGoesOff.setObjects(
      *(("EKINOPS-PmOabphc-MIB", "pmoabphcAlmLineFail"),
        ("EKINOPS-PmOabphc-MIB", "pmoabphcAlmLineHwFail"),
        ("EKINOPS-PmOabphc-MIB", "pmoabphctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoabphcLineTrapCritGoesOff.setStatus(
        "current"
    )

pmoabphcClientTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 51, 10, 40)
)
pmoabphcClientTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-PmOabphc-MIB", "pmoabphcAlmClientDdmWarning"),
        ("EKINOPS-PmOabphc-MIB", "pmoabphctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoabphcClientTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pmoabphcClientTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 51, 10, 41)
)
pmoabphcClientTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-PmOabphc-MIB", "pmoabphcAlmClientDdmWarning"),
        ("EKINOPS-PmOabphc-MIB", "pmoabphctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoabphcClientTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pmoabphcClientTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 51, 10, 42)
)
pmoabphcClientTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-PmOabphc-MIB", "pmoabphcAlmClientDdmAlm"),
        ("EKINOPS-PmOabphc-MIB", "pmoabphctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoabphcClientTrapUrgentGoesOn.setStatus(
        "current"
    )

pmoabphcClientTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 51, 10, 43)
)
pmoabphcClientTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-PmOabphc-MIB", "pmoabphcAlmClientDdmAlm"),
        ("EKINOPS-PmOabphc-MIB", "pmoabphctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoabphcClientTrapUrgentGoesOff.setStatus(
        "current"
    )

pmoabphcClientTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 51, 10, 44)
)
pmoabphcClientTrapCritGoesOn.setObjects(
      *(("EKINOPS-PmOabphc-MIB", "pmoabphcAlmClientFail"),
        ("EKINOPS-PmOabphc-MIB", "pmoabphcAlmClientHwFail"),
        ("EKINOPS-PmOabphc-MIB", "pmoabphctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoabphcClientTrapCritGoesOn.setStatus(
        "current"
    )

pmoabphcClientTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 51, 10, 45)
)
pmoabphcClientTrapCritGoesOff.setObjects(
      *(("EKINOPS-PmOabphc-MIB", "pmoabphcAlmClientFail"),
        ("EKINOPS-PmOabphc-MIB", "pmoabphcAlmClientHwFail"),
        ("EKINOPS-PmOabphc-MIB", "pmoabphctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoabphcClientTrapCritGoesOff.setStatus(
        "current"
    )

pmoabphcPowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 51, 10, 50)
)
pmoabphcPowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-PmOabphc-MIB", "pmoabphcAlmDefFuseB"),
        ("EKINOPS-PmOabphc-MIB", "pmoabphcAlmDefFuseA"),
        ("EKINOPS-PmOabphc-MIB", "pmoabphctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoabphcPowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pmoabphcPowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 51, 10, 51)
)
pmoabphcPowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-PmOabphc-MIB", "pmoabphcAlmDefFuseB"),
        ("EKINOPS-PmOabphc-MIB", "pmoabphcAlmDefFuseA"),
        ("EKINOPS-PmOabphc-MIB", "pmoabphctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoabphcPowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-PmOabphc-MIB",
    **{"PmoabphcpreampMode": PmoabphcpreampMode,
       "PmoabphcboosterMode": PmoabphcboosterMode,
       "PmoabphcaprMode": PmoabphcaprMode,
       "PmoabphcPreampGainAdjMode": PmoabphcPreampGainAdjMode,
       "PmoabphcBoosterGainAdjMode": PmoabphcBoosterGainAdjMode,
       "PmoabphcPreampCstGainAdjMode": PmoabphcPreampCstGainAdjMode,
       "PmoabphcBoosterCstGainAdjMode": PmoabphcBoosterCstGainAdjMode,
       "modulepmoabphc": modulepmoabphc,
       "pmoabphcalarms": pmoabphcalarms,
       "pmoabphcAlmOther": pmoabphcAlmOther,
       "pmoabphcAlmOtherNurg": pmoabphcAlmOtherNurg,
       "pmoabphcAlmsynthAlm2": pmoabphcAlmsynthAlm2,
       "pmoabphcAlmConfTableSave": pmoabphcAlmConfTableSave,
       "pmoabphcAlmInvUpload": pmoabphcAlmInvUpload,
       "pmoabphcAlmConfTableLoad": pmoabphcAlmConfTableLoad,
       "pmoabphcAlmfoaWarnings": pmoabphcAlmfoaWarnings,
       "pmoabphcAlmTermpLowWarning": pmoabphcAlmTermpLowWarning,
       "pmoabphcAlmTempHighWarning": pmoabphcAlmTempHighWarning,
       "pmoabphcAlmOtherUrg": pmoabphcAlmOtherUrg,
       "pmoabphcAlmfoaAlarms": pmoabphcAlmfoaAlarms,
       "pmoabphcAlmTermpLowAlarm": pmoabphcAlmTermpLowAlarm,
       "pmoabphcAlmTempHighAlarm": pmoabphcAlmTempHighAlarm,
       "pmoabphcAlmOtherCrit": pmoabphcAlmOtherCrit,
       "pmoabphcAlmsynthAlm0": pmoabphcAlmsynthAlm0,
       "pmoabphcAlmMaintenanceMode": pmoabphcAlmMaintenanceMode,
       "pmoabphcAlmAprOn": pmoabphcAlmAprOn,
       "pmoabphcAlmModGlobFail": pmoabphcAlmModGlobFail,
       "pmoabphcAlmUpEdfaInitNotCompl": pmoabphcAlmUpEdfaInitNotCompl,
       "pmoabphcAlmDwEdfaInitNotCompl": pmoabphcAlmDwEdfaInitNotCompl,
       "pmoabphcAlmExtPump1NotLocked": pmoabphcAlmExtPump1NotLocked,
       "pmoabphcAlmExtPump2NotLocked": pmoabphcAlmExtPump2NotLocked,
       "pmoabphcAlmDefFuseA": pmoabphcAlmDefFuseA,
       "pmoabphcAlmDefFuseB": pmoabphcAlmDefFuseB,
       "pmoabphcAlmClient": pmoabphcAlmClient,
       "pmoabphcAlmClientNurg": pmoabphcAlmClientNurg,
       "pmoabphcAlmclientEdfaWarnings": pmoabphcAlmclientEdfaWarnings,
       "pmoabphcAlmClientGainLowWarning": pmoabphcAlmClientGainLowWarning,
       "pmoabphcAlmClientGainHighWarning": pmoabphcAlmClientGainHighWarning,
       "pmoabphcAlmClientInputPwrLowWarning": pmoabphcAlmClientInputPwrLowWarning,
       "pmoabphcAlmClientInputPwrHighWarning": pmoabphcAlmClientInputPwrHighWarning,
       "pmoabphcAlmClientOutputPwrLowWarning": pmoabphcAlmClientOutputPwrLowWarning,
       "pmoabphcAlmClientOutputPwrHighWarning": pmoabphcAlmClientOutputPwrHighWarning,
       "pmoabphcAlmClientBiasLowWarning": pmoabphcAlmClientBiasLowWarning,
       "pmoabphcAlmClientBiasHighWarning": pmoabphcAlmClientBiasHighWarning,
       "pmoabphcAlmClientUrg": pmoabphcAlmClientUrg,
       "pmoabphcAlmclientEdfaAlarms1": pmoabphcAlmclientEdfaAlarms1,
       "pmoabphcAlmClientGainLowAlarm": pmoabphcAlmClientGainLowAlarm,
       "pmoabphcAlmClientGainHighAlarm": pmoabphcAlmClientGainHighAlarm,
       "pmoabphcAlmClientInputPwrLowAlarm": pmoabphcAlmClientInputPwrLowAlarm,
       "pmoabphcAlmClientInputPwrHighAlarm": pmoabphcAlmClientInputPwrHighAlarm,
       "pmoabphcAlmClientOutputPwrLowAlarm": pmoabphcAlmClientOutputPwrLowAlarm,
       "pmoabphcAlmClientOutputPwrHighAlarm": pmoabphcAlmClientOutputPwrHighAlarm,
       "pmoabphcAlmClientBiasLowAlarm": pmoabphcAlmClientBiasLowAlarm,
       "pmoabphcAlmClientBiasHighAlarm": pmoabphcAlmClientBiasHighAlarm,
       "pmoabphcAlmClientCrit": pmoabphcAlmClientCrit,
       "pmoabphcAlmsynthAlm8": pmoabphcAlmsynthAlm8,
       "pmoabphcAlmClientHwFail": pmoabphcAlmClientHwFail,
       "pmoabphcAlmClientTxOff": pmoabphcAlmClientTxOff,
       "pmoabphcAlmClientDdmWarning": pmoabphcAlmClientDdmWarning,
       "pmoabphcAlmClientDdmAlm": pmoabphcAlmClientDdmAlm,
       "pmoabphcAlmClientFail": pmoabphcAlmClientFail,
       "pmoabphcAlmClientExtPumpFail": pmoabphcAlmClientExtPumpFail,
       "pmoabphcAlmclientEdfaAlarms2": pmoabphcAlmclientEdfaAlarms2,
       "pmoabphcAlmClientEdfaNr": pmoabphcAlmClientEdfaNr,
       "pmoabphcAlmClientEdfaTecFail": pmoabphcAlmClientEdfaTecFail,
       "pmoabphcAlmClientEdfaLaserFail": pmoabphcAlmClientEdfaLaserFail,
       "pmoabphcAlmClientEdfaLos": pmoabphcAlmClientEdfaLos,
       "pmoabphcAlmClientExtPumpEdfaLowCurrent": pmoabphcAlmClientExtPumpEdfaLowCurrent,
       "pmoabphcAlmLine": pmoabphcAlmLine,
       "pmoabphcAlmLineNurg": pmoabphcAlmLineNurg,
       "pmoabphcAlmlineEdfaWarnings": pmoabphcAlmlineEdfaWarnings,
       "pmoabphcAlmLineGainLowWarning": pmoabphcAlmLineGainLowWarning,
       "pmoabphcAlmLineGainHighWarning": pmoabphcAlmLineGainHighWarning,
       "pmoabphcAlmLineInputPwrLowWarning": pmoabphcAlmLineInputPwrLowWarning,
       "pmoabphcAlmLineInputPwrHighWarning": pmoabphcAlmLineInputPwrHighWarning,
       "pmoabphcAlmLineOutputPwrLowWarning": pmoabphcAlmLineOutputPwrLowWarning,
       "pmoabphcAlmLineOutputPwrHighWarning": pmoabphcAlmLineOutputPwrHighWarning,
       "pmoabphcAlmLineBiasLowWarning": pmoabphcAlmLineBiasLowWarning,
       "pmoabphcAlmLineBiasHighWarning": pmoabphcAlmLineBiasHighWarning,
       "pmoabphcAlmLineUrg": pmoabphcAlmLineUrg,
       "pmoabphcAlmlineEdfaAlarms1": pmoabphcAlmlineEdfaAlarms1,
       "pmoabphcAlmLineGainLowAlarm": pmoabphcAlmLineGainLowAlarm,
       "pmoabphcAlmLineGainHighAlarm": pmoabphcAlmLineGainHighAlarm,
       "pmoabphcAlmLineInputPwrLowAlarm": pmoabphcAlmLineInputPwrLowAlarm,
       "pmoabphcAlmLineInputPwrHighAlarm": pmoabphcAlmLineInputPwrHighAlarm,
       "pmoabphcAlmLineOutputPwrLowAlarm": pmoabphcAlmLineOutputPwrLowAlarm,
       "pmoabphcAlmLineOutputPwrHighAlarm": pmoabphcAlmLineOutputPwrHighAlarm,
       "pmoabphcAlmLineBiasLowAlarm": pmoabphcAlmLineBiasLowAlarm,
       "pmoabphcAlmLineBiasHighAlarm": pmoabphcAlmLineBiasHighAlarm,
       "pmoabphcAlmLineCrit": pmoabphcAlmLineCrit,
       "pmoabphcAlmsynthAlm7": pmoabphcAlmsynthAlm7,
       "pmoabphcAlmLineHwFail": pmoabphcAlmLineHwFail,
       "pmoabphcAlmLineTxOff": pmoabphcAlmLineTxOff,
       "pmoabphcAlmLineDdmWarning": pmoabphcAlmLineDdmWarning,
       "pmoabphcAlmLineDdmAlm": pmoabphcAlmLineDdmAlm,
       "pmoabphcAlmLineFail": pmoabphcAlmLineFail,
       "pmoabphcAlmLineExtPumpFail": pmoabphcAlmLineExtPumpFail,
       "pmoabphcAlmlineEdfaAlarms2": pmoabphcAlmlineEdfaAlarms2,
       "pmoabphcAlmLineEdfaNr": pmoabphcAlmLineEdfaNr,
       "pmoabphcAlmLineEdfaTecFail": pmoabphcAlmLineEdfaTecFail,
       "pmoabphcAlmLineEdfaLaserFail": pmoabphcAlmLineEdfaLaserFail,
       "pmoabphcAlmLineEdfaLos": pmoabphcAlmLineEdfaLos,
       "pmoabphcAlmLineExtPumpEdfaLowCurrent": pmoabphcAlmLineExtPumpEdfaLowCurrent,
       "pmoabphcmeasures": pmoabphcmeasures,
       "pmoabphcMesrOther": pmoabphcMesrOther,
       "pmoabphcMesrtempMeas": pmoabphcMesrtempMeas,
       "pmoabphcMesrClient": pmoabphcMesrClient,
       "pmoabphcMesrclientEdfaBiasMeas": pmoabphcMesrclientEdfaBiasMeas,
       "pmoabphcMesrclientEdfaTxpwrMeas": pmoabphcMesrclientEdfaTxpwrMeas,
       "pmoabphcMesrclientEdfaRxpwrMeas": pmoabphcMesrclientEdfaRxpwrMeas,
       "pmoabphcMesrclientEdfaGainMeas": pmoabphcMesrclientEdfaGainMeas,
       "pmoabphcMesrclientCorrectedGain": pmoabphcMesrclientCorrectedGain,
       "pmoabphcMesrLine": pmoabphcMesrLine,
       "pmoabphcMesrlineEdfaBiasMeas": pmoabphcMesrlineEdfaBiasMeas,
       "pmoabphcMesrlineEdfaTxpwrMeas": pmoabphcMesrlineEdfaTxpwrMeas,
       "pmoabphcMesrlineEdfaRxpwrMeas": pmoabphcMesrlineEdfaRxpwrMeas,
       "pmoabphcMesrlineEdfaGainMeas": pmoabphcMesrlineEdfaGainMeas,
       "pmoabphcMesrlineCorrectedGain": pmoabphcMesrlineCorrectedGain,
       "pmoabphccontrolsWrite": pmoabphccontrolsWrite,
       "pmoabphcCtrlOther": pmoabphcCtrlOther,
       "pmoabphcCtrlsynth0": pmoabphcCtrlsynth0,
       "pmoabphcCtrlConfLoad": pmoabphcCtrlConfLoad,
       "pmoabphcCtrlConfFlash": pmoabphcCtrlConfFlash,
       "pmoabphcCtrlConfClear": pmoabphcCtrlConfClear,
       "pmoabphcCtrlswMgnt": pmoabphcCtrlswMgnt,
       "pmoabphcCtrlColdReset": pmoabphcCtrlColdReset,
       "pmoabphcCtrlWarmReset": pmoabphcCtrlWarmReset,
       "pmoabphcCtrlledTest": pmoabphcCtrlledTest,
       "pmoabphcCtrlGreenLed": pmoabphcCtrlGreenLed,
       "pmoabphcCtrlRedLed": pmoabphcCtrlRedLed,
       "pmoabphcCtrlLedOff": pmoabphcCtrlLedOff,
       "pmoabphcCtrlmaintMode": pmoabphcCtrlmaintMode,
       "pmoabphcCtrlMaintenance": pmoabphcCtrlMaintenance,
       "pmoabphcCtrlaprRestart": pmoabphcCtrlaprRestart,
       "pmoabphcCtrlAprManualRestart": pmoabphcCtrlAprManualRestart,
       "pmoabphcCtrlClient": pmoabphcCtrlClient,
       "pmoabphcCtrlclientEdfaLaserOff": pmoabphcCtrlclientEdfaLaserOff,
       "pmoabphcCtrlClientEdfaLaserOff": pmoabphcCtrlClientEdfaLaserOff,
       "pmoabphcCtrlclientGainCstMonitorValue": pmoabphcCtrlclientGainCstMonitorValue,
       "pmoabphcCtrlclientGainCstPoutValue": pmoabphcCtrlclientGainCstPoutValue,
       "pmoabphcCtrlclientGainSettingValue": pmoabphcCtrlclientGainSettingValue,
       "pmoabphcCtrlclientGainProcessing": pmoabphcCtrlclientGainProcessing,
       "pmoabphcCtrlClientGainProc": pmoabphcCtrlClientGainProc,
       "pmoabphcCtrlclientGainCstFiberAgingMarginValue": pmoabphcCtrlclientGainCstFiberAgingMarginValue,
       "pmoabphcCtrlclientGainCstAdddropMarginValue": pmoabphcCtrlclientGainCstAdddropMarginValue,
       "pmoabphcCtrlLine": pmoabphcCtrlLine,
       "pmoabphcCtrllineEdfaLaserOff": pmoabphcCtrllineEdfaLaserOff,
       "pmoabphcCtrlLineEdfaLaserOff": pmoabphcCtrlLineEdfaLaserOff,
       "pmoabphcCtrllineGainCstMonitorValue": pmoabphcCtrllineGainCstMonitorValue,
       "pmoabphcCtrllineGainCstPoutValue": pmoabphcCtrllineGainCstPoutValue,
       "pmoabphcCtrllineGainSettingValue": pmoabphcCtrllineGainSettingValue,
       "pmoabphcCtrllineGainProcessing": pmoabphcCtrllineGainProcessing,
       "pmoabphcCtrlLineGainProc": pmoabphcCtrlLineGainProc,
       "pmoabphcCtrllineGainCstFiberAgingMarginValue": pmoabphcCtrllineGainCstFiberAgingMarginValue,
       "pmoabphcCtrllineGainCstAdddropMarginValue": pmoabphcCtrllineGainCstAdddropMarginValue,
       "pmoabphcri": pmoabphcri,
       "pmoabphcRinvReloadInventory": pmoabphcRinvReloadInventory,
       "pmoabphcRinvModulePlatform": pmoabphcRinvModulePlatform,
       "pmoabphcRinvSwPlatform": pmoabphcRinvSwPlatform,
       "pmoabphcRinvSwFoa": pmoabphcRinvSwFoa,
       "pmoabphcRinvBoosterTable": pmoabphcRinvBoosterTable,
       "pmoabphcRinvBoosterEntry": pmoabphcRinvBoosterEntry,
       "pmoabphcRinvBoosterIndex": pmoabphcRinvBoosterIndex,
       "pmoabphcRinvBooster": pmoabphcRinvBooster,
       "pmoabphcRinvPreAmpTable": pmoabphcRinvPreAmpTable,
       "pmoabphcRinvPreAmpEntry": pmoabphcRinvPreAmpEntry,
       "pmoabphcRinvPreAmpIndex": pmoabphcRinvPreAmpIndex,
       "pmoabphcRinvPreAmp": pmoabphcRinvPreAmp,
       "pmoabphcConfig": pmoabphcConfig,
       "pmoabphcCfgNoValue": pmoabphcCfgNoValue,
       "pmoabphctableclientStartup": pmoabphctableclientStartup,
       "pmoabphcCfgclientEdfaLaserCtrl": pmoabphcCfgclientEdfaLaserCtrl,
       "pmoabphcCfgclientEdfaLaserMode": pmoabphcCfgclientEdfaLaserMode,
       "pmoabphcCfgclientGainValue": pmoabphcCfgclientGainValue,
       "pmoabphcCfgclientTiltValue": pmoabphcCfgclientTiltValue,
       "pmoabphcCfgclientMsaLoss": pmoabphcCfgclientMsaLoss,
       "pmoabphcCfgclientOutputPowerValue": pmoabphcCfgclientOutputPowerValue,
       "pmoabphcCfgclientAseCompensation": pmoabphcCfgclientAseCompensation,
       "pmoabphcCfgLineStartUp": pmoabphcCfgLineStartUp,
       "pmoabphctablelineStartup": pmoabphctablelineStartup,
       "pmoabphcCfglineEdfaLaserCtrl": pmoabphcCfglineEdfaLaserCtrl,
       "pmoabphcCfglineEdfaLaserMode": pmoabphcCfglineEdfaLaserMode,
       "pmoabphcCfglineGainValue": pmoabphcCfglineGainValue,
       "pmoabphcCfglineTiltValue": pmoabphcCfglineTiltValue,
       "pmoabphcCfglineMsaLoss": pmoabphcCfglineMsaLoss,
       "pmoabphcCfglineOutputPowerValue": pmoabphcCfglineOutputPowerValue,
       "pmoabphcCfglineAseCompensation": pmoabphcCfglineAseCompensation,
       "pmoabphcCfgaprMode": pmoabphcCfgaprMode,
       "pmoabphcCfgLabels": pmoabphcCfgLabels,
       "pmoabphcCfgLabelclientTable": pmoabphcCfgLabelclientTable,
       "pmoabphcCfgLabelclientEntry": pmoabphcCfgLabelclientEntry,
       "pmoabphcCfgLabelclientIndex": pmoabphcCfgLabelclientIndex,
       "pmoabphcCfgLabelclientPortn": pmoabphcCfgLabelclientPortn,
       "pmoabphcCfgLabellineTable": pmoabphcCfgLabellineTable,
       "pmoabphcCfgLabellineEntry": pmoabphcCfgLabellineEntry,
       "pmoabphcCfgLabellineIndex": pmoabphcCfgLabellineIndex,
       "pmoabphcCfgLabellinePortn": pmoabphcCfgLabellinePortn,
       "pmoabphcCfgWriteConfiguration": pmoabphcCfgWriteConfiguration,
       "pmoabphctraps": pmoabphctraps,
       "pmoabphctrapBoardNumber": pmoabphctrapBoardNumber,
       "pmoabphcLineTrapNotUrgentGoesOn": pmoabphcLineTrapNotUrgentGoesOn,
       "pmoabphcLineTrapNotUrgentGoesOff": pmoabphcLineTrapNotUrgentGoesOff,
       "pmoabphcLineTrapUrgentGoesOn": pmoabphcLineTrapUrgentGoesOn,
       "pmoabphcLineTrapUrgentGoesOff": pmoabphcLineTrapUrgentGoesOff,
       "pmoabphcLineTrapCritGoesOn": pmoabphcLineTrapCritGoesOn,
       "pmoabphcLineTrapCritGoesOff": pmoabphcLineTrapCritGoesOff,
       "pmoabphcClientTrapNotUrgentGoesOn": pmoabphcClientTrapNotUrgentGoesOn,
       "pmoabphcClientTrapNotUrgentGoesOff": pmoabphcClientTrapNotUrgentGoesOff,
       "pmoabphcClientTrapUrgentGoesOn": pmoabphcClientTrapUrgentGoesOn,
       "pmoabphcClientTrapUrgentGoesOff": pmoabphcClientTrapUrgentGoesOff,
       "pmoabphcClientTrapCritGoesOn": pmoabphcClientTrapCritGoesOn,
       "pmoabphcClientTrapCritGoesOff": pmoabphcClientTrapCritGoesOff,
       "pmoabphcPowerTrapUrgentGoesOn": pmoabphcPowerTrapUrgentGoesOn,
       "pmoabphcPowerTrapUrgentGoesOff": pmoabphcPowerTrapUrgentGoesOff}
)
