# SNMP MIB module (EKINOPS-PmOailhc-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-PmOailhc-MIB.mib
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

modulepmoailhc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55)
)
if mibBuilder.loadTexts:
    modulepmoailhc.setRevisions(
        ("2012-09-10 00:00",
         "2012-09-10 00:00",
         "2013-02-08 00:00",
         "2013-07-02 00:00",
         "2013-09-16 00:00",
         "2013-12-02 00:00",
         "2014-03-26 00:00",
         "2014-12-10 00:00",
         "2016-05-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PmoailhcpreampMode(TextualConvention, Integer32):
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
        *(("oailhcpreampdefaultmode", 0),
          ("oailhcpreampconstantcurrentmode", 1),
          ("oailhcpreampconstantpowermode", 2),
          ("oailhcpreampconstantgainmode", 3),
          ("oailhcpreamppoutpinmode", 4),
          ("oailhcpreampmanualmode", 5),
          ("oailhcpreampfeedforwardmode", 6),
          ("oailhcpreamptransientsupmode", 7))
    )



class PmoailhcboosterMode(TextualConvention, Integer32):
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
        *(("oailhcboosterdefaultmode", 0),
          ("oailhcboosterconstantcurrentmode", 1),
          ("oailhcboosterconstantpowermode", 2),
          ("oailhcboosterconstantgainmode", 3),
          ("oailhcboosterpoutpinmode", 4),
          ("oailhcboostermanualmode", 5),
          ("oailhcboosterfeedforwardmode", 6),
          ("oailhcboostertransientsupmode", 7))
    )



class PmoailhcaprMode(TextualConvention, Integer32):
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
        *(("oailhcaproffmode", 0),
          ("oailhcaprsemiautomode", 1),
          ("oailhcaprautomode", 2),
          ("oailhcaprlossforwardingmode", 3),
          ("oailhcaprrepeatmode", 4))
    )



class PmoailhcPreampGainAdjMode(TextualConvention, Integer32):
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
        *(("oailhcpreampgainadjmanualmode", 0),
          ("oailhcpreampgainadjsemiautomode", 1),
          ("oailhcpreampgainadjautomode", 2))
    )



class PmoailhcBoosterGainAdjMode(TextualConvention, Integer32):
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
        *(("oailhcboostergainadjmanualmode", 0),
          ("oailhcboostergainadjsemiautomode", 1),
          ("oailhcboostergainadjautomode", 2))
    )



class PmoailhcPreampCstGainAdjMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oailhcpreampcstgainadjsemiautomode", 1),
          ("oailhcpreampcstgainadjautomode", 2))
    )



class PmoailhcBoosterCstGainAdjMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oailhcboostercstgainadjsemiautomode", 1),
          ("oailhcboostercstgainadjautomode", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Pmoailhcalarms_ObjectIdentity = ObjectIdentity
pmoailhcalarms = _Pmoailhcalarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2)
)
_PmoailhcAlmOther_ObjectIdentity = ObjectIdentity
pmoailhcAlmOther = _PmoailhcAlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 1)
)
_PmoailhcAlmOtherNurg_ObjectIdentity = ObjectIdentity
pmoailhcAlmOtherNurg = _PmoailhcAlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 1, 1)
)
_PmoailhcAlmsynthAlm2_ObjectIdentity = ObjectIdentity
pmoailhcAlmsynthAlm2 = _PmoailhcAlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 1, 1, 2)
)
_PmoailhcAlmConfTableSave_Type = EkiOnOff
_PmoailhcAlmConfTableSave_Object = MibScalar
pmoailhcAlmConfTableSave = _PmoailhcAlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 1, 1, 2, 1),
    _PmoailhcAlmConfTableSave_Type()
)
pmoailhcAlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmConfTableSave.setStatus("current")
_PmoailhcAlmInvUpload_Type = EkiOnOff
_PmoailhcAlmInvUpload_Object = MibScalar
pmoailhcAlmInvUpload = _PmoailhcAlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 1, 1, 2, 2),
    _PmoailhcAlmInvUpload_Type()
)
pmoailhcAlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmInvUpload.setStatus("current")
_PmoailhcAlmConfTableLoad_Type = EkiOnOff
_PmoailhcAlmConfTableLoad_Object = MibScalar
pmoailhcAlmConfTableLoad = _PmoailhcAlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 1, 1, 2, 3),
    _PmoailhcAlmConfTableLoad_Type()
)
pmoailhcAlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmConfTableLoad.setStatus("current")
_PmoailhcAlmfoaWarnings_ObjectIdentity = ObjectIdentity
pmoailhcAlmfoaWarnings = _PmoailhcAlmfoaWarnings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 1, 1, 75)
)
_PmoailhcAlmTermpLowWarning_Type = EkiOnOff
_PmoailhcAlmTermpLowWarning_Object = MibScalar
pmoailhcAlmTermpLowWarning = _PmoailhcAlmTermpLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 1, 1, 75, 7),
    _PmoailhcAlmTermpLowWarning_Type()
)
pmoailhcAlmTermpLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmTermpLowWarning.setStatus("current")
_PmoailhcAlmTempHighWarning_Type = EkiOnOff
_PmoailhcAlmTempHighWarning_Object = MibScalar
pmoailhcAlmTempHighWarning = _PmoailhcAlmTempHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 1, 1, 75, 8),
    _PmoailhcAlmTempHighWarning_Type()
)
pmoailhcAlmTempHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmTempHighWarning.setStatus("current")
_PmoailhcAlmOtherUrg_ObjectIdentity = ObjectIdentity
pmoailhcAlmOtherUrg = _PmoailhcAlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 1, 2)
)
_PmoailhcAlmfoaAlarms_ObjectIdentity = ObjectIdentity
pmoailhcAlmfoaAlarms = _PmoailhcAlmfoaAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 1, 2, 74)
)
_PmoailhcAlmTermpLowAlarm_Type = EkiOnOff
_PmoailhcAlmTermpLowAlarm_Object = MibScalar
pmoailhcAlmTermpLowAlarm = _PmoailhcAlmTermpLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 1, 2, 74, 7),
    _PmoailhcAlmTermpLowAlarm_Type()
)
pmoailhcAlmTermpLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmTermpLowAlarm.setStatus("current")
_PmoailhcAlmTempHighAlarm_Type = EkiOnOff
_PmoailhcAlmTempHighAlarm_Object = MibScalar
pmoailhcAlmTempHighAlarm = _PmoailhcAlmTempHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 1, 2, 74, 8),
    _PmoailhcAlmTempHighAlarm_Type()
)
pmoailhcAlmTempHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmTempHighAlarm.setStatus("current")
_PmoailhcAlmOtherCrit_ObjectIdentity = ObjectIdentity
pmoailhcAlmOtherCrit = _PmoailhcAlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 1, 3)
)
_PmoailhcAlmsynthAlm0_ObjectIdentity = ObjectIdentity
pmoailhcAlmsynthAlm0 = _PmoailhcAlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 1, 3, 0)
)
_PmoailhcAlmMaintenanceMode_Type = EkiOnOff
_PmoailhcAlmMaintenanceMode_Object = MibScalar
pmoailhcAlmMaintenanceMode = _PmoailhcAlmMaintenanceMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 1, 3, 0, 1),
    _PmoailhcAlmMaintenanceMode_Type()
)
pmoailhcAlmMaintenanceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmMaintenanceMode.setStatus("current")
_PmoailhcAlmAprOn_Type = EkiOnOff
_PmoailhcAlmAprOn_Object = MibScalar
pmoailhcAlmAprOn = _PmoailhcAlmAprOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 1, 3, 0, 2),
    _PmoailhcAlmAprOn_Type()
)
pmoailhcAlmAprOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmAprOn.setStatus("current")
_PmoailhcAlmModGlobFail_Type = EkiOnOff
_PmoailhcAlmModGlobFail_Object = MibScalar
pmoailhcAlmModGlobFail = _PmoailhcAlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 1, 3, 0, 9),
    _PmoailhcAlmModGlobFail_Type()
)
pmoailhcAlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmModGlobFail.setStatus("current")
_PmoailhcAlmUpEdfaInitNotCompl_Type = EkiOnOff
_PmoailhcAlmUpEdfaInitNotCompl_Object = MibScalar
pmoailhcAlmUpEdfaInitNotCompl = _PmoailhcAlmUpEdfaInitNotCompl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 1, 3, 0, 10),
    _PmoailhcAlmUpEdfaInitNotCompl_Type()
)
pmoailhcAlmUpEdfaInitNotCompl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmUpEdfaInitNotCompl.setStatus("current")
_PmoailhcAlmDwEdfaInitNotCompl_Type = EkiOnOff
_PmoailhcAlmDwEdfaInitNotCompl_Object = MibScalar
pmoailhcAlmDwEdfaInitNotCompl = _PmoailhcAlmDwEdfaInitNotCompl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 1, 3, 0, 11),
    _PmoailhcAlmDwEdfaInitNotCompl_Type()
)
pmoailhcAlmDwEdfaInitNotCompl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmDwEdfaInitNotCompl.setStatus("current")
_PmoailhcAlmExtPump1NotLocked_Type = EkiOnOff
_PmoailhcAlmExtPump1NotLocked_Object = MibScalar
pmoailhcAlmExtPump1NotLocked = _PmoailhcAlmExtPump1NotLocked_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 1, 3, 0, 12),
    _PmoailhcAlmExtPump1NotLocked_Type()
)
pmoailhcAlmExtPump1NotLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmExtPump1NotLocked.setStatus("current")
_PmoailhcAlmExtPump2NotLocked_Type = EkiOnOff
_PmoailhcAlmExtPump2NotLocked_Object = MibScalar
pmoailhcAlmExtPump2NotLocked = _PmoailhcAlmExtPump2NotLocked_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 1, 3, 0, 13),
    _PmoailhcAlmExtPump2NotLocked_Type()
)
pmoailhcAlmExtPump2NotLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmExtPump2NotLocked.setStatus("current")
_PmoailhcAlmDefFuseA_Type = EkiOnOff
_PmoailhcAlmDefFuseA_Object = MibScalar
pmoailhcAlmDefFuseA = _PmoailhcAlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 1, 3, 0, 15),
    _PmoailhcAlmDefFuseA_Type()
)
pmoailhcAlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmDefFuseA.setStatus("current")
_PmoailhcAlmDefFuseB_Type = EkiOnOff
_PmoailhcAlmDefFuseB_Object = MibScalar
pmoailhcAlmDefFuseB = _PmoailhcAlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 1, 3, 0, 16),
    _PmoailhcAlmDefFuseB_Type()
)
pmoailhcAlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmDefFuseB.setStatus("current")
_PmoailhcAlmClient_ObjectIdentity = ObjectIdentity
pmoailhcAlmClient = _PmoailhcAlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 2)
)
_PmoailhcAlmClientNurg_ObjectIdentity = ObjectIdentity
pmoailhcAlmClientNurg = _PmoailhcAlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 2, 1)
)
_PmoailhcAlmclientEdfaWarnings_ObjectIdentity = ObjectIdentity
pmoailhcAlmclientEdfaWarnings = _PmoailhcAlmclientEdfaWarnings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 2, 1, 33)
)
_PmoailhcAlmClientGainLowWarning_Type = EkiOnOff
_PmoailhcAlmClientGainLowWarning_Object = MibScalar
pmoailhcAlmClientGainLowWarning = _PmoailhcAlmClientGainLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 2, 1, 33, 1),
    _PmoailhcAlmClientGainLowWarning_Type()
)
pmoailhcAlmClientGainLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmClientGainLowWarning.setStatus("current")
_PmoailhcAlmClientGainHighWarning_Type = EkiOnOff
_PmoailhcAlmClientGainHighWarning_Object = MibScalar
pmoailhcAlmClientGainHighWarning = _PmoailhcAlmClientGainHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 2, 1, 33, 2),
    _PmoailhcAlmClientGainHighWarning_Type()
)
pmoailhcAlmClientGainHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmClientGainHighWarning.setStatus("current")
_PmoailhcAlmClientInputPwrLowWarning_Type = EkiOnOff
_PmoailhcAlmClientInputPwrLowWarning_Object = MibScalar
pmoailhcAlmClientInputPwrLowWarning = _PmoailhcAlmClientInputPwrLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 2, 1, 33, 3),
    _PmoailhcAlmClientInputPwrLowWarning_Type()
)
pmoailhcAlmClientInputPwrLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmClientInputPwrLowWarning.setStatus("current")
_PmoailhcAlmClientInputPwrHighWarning_Type = EkiOnOff
_PmoailhcAlmClientInputPwrHighWarning_Object = MibScalar
pmoailhcAlmClientInputPwrHighWarning = _PmoailhcAlmClientInputPwrHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 2, 1, 33, 4),
    _PmoailhcAlmClientInputPwrHighWarning_Type()
)
pmoailhcAlmClientInputPwrHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmClientInputPwrHighWarning.setStatus("current")
_PmoailhcAlmClientOutputPwrLowWarning_Type = EkiOnOff
_PmoailhcAlmClientOutputPwrLowWarning_Object = MibScalar
pmoailhcAlmClientOutputPwrLowWarning = _PmoailhcAlmClientOutputPwrLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 2, 1, 33, 5),
    _PmoailhcAlmClientOutputPwrLowWarning_Type()
)
pmoailhcAlmClientOutputPwrLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmClientOutputPwrLowWarning.setStatus("current")
_PmoailhcAlmClientOutputPwrHighWarning_Type = EkiOnOff
_PmoailhcAlmClientOutputPwrHighWarning_Object = MibScalar
pmoailhcAlmClientOutputPwrHighWarning = _PmoailhcAlmClientOutputPwrHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 2, 1, 33, 6),
    _PmoailhcAlmClientOutputPwrHighWarning_Type()
)
pmoailhcAlmClientOutputPwrHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmClientOutputPwrHighWarning.setStatus("current")
_PmoailhcAlmClientBiasLowWarning_Type = EkiOnOff
_PmoailhcAlmClientBiasLowWarning_Object = MibScalar
pmoailhcAlmClientBiasLowWarning = _PmoailhcAlmClientBiasLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 2, 1, 33, 7),
    _PmoailhcAlmClientBiasLowWarning_Type()
)
pmoailhcAlmClientBiasLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmClientBiasLowWarning.setStatus("current")
_PmoailhcAlmClientBiasHighWarning_Type = EkiOnOff
_PmoailhcAlmClientBiasHighWarning_Object = MibScalar
pmoailhcAlmClientBiasHighWarning = _PmoailhcAlmClientBiasHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 2, 1, 33, 8),
    _PmoailhcAlmClientBiasHighWarning_Type()
)
pmoailhcAlmClientBiasHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmClientBiasHighWarning.setStatus("current")
_PmoailhcAlmClientUrg_ObjectIdentity = ObjectIdentity
pmoailhcAlmClientUrg = _PmoailhcAlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 2, 2)
)
_PmoailhcAlmclientEdfaAlarms1_ObjectIdentity = ObjectIdentity
pmoailhcAlmclientEdfaAlarms1 = _PmoailhcAlmclientEdfaAlarms1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 2, 2, 32)
)
_PmoailhcAlmClientGainLowAlarm_Type = EkiOnOff
_PmoailhcAlmClientGainLowAlarm_Object = MibScalar
pmoailhcAlmClientGainLowAlarm = _PmoailhcAlmClientGainLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 2, 2, 32, 1),
    _PmoailhcAlmClientGainLowAlarm_Type()
)
pmoailhcAlmClientGainLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmClientGainLowAlarm.setStatus("current")
_PmoailhcAlmClientGainHighAlarm_Type = EkiOnOff
_PmoailhcAlmClientGainHighAlarm_Object = MibScalar
pmoailhcAlmClientGainHighAlarm = _PmoailhcAlmClientGainHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 2, 2, 32, 2),
    _PmoailhcAlmClientGainHighAlarm_Type()
)
pmoailhcAlmClientGainHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmClientGainHighAlarm.setStatus("current")
_PmoailhcAlmClientInputPwrLowAlarm_Type = EkiOnOff
_PmoailhcAlmClientInputPwrLowAlarm_Object = MibScalar
pmoailhcAlmClientInputPwrLowAlarm = _PmoailhcAlmClientInputPwrLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 2, 2, 32, 3),
    _PmoailhcAlmClientInputPwrLowAlarm_Type()
)
pmoailhcAlmClientInputPwrLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmClientInputPwrLowAlarm.setStatus("current")
_PmoailhcAlmClientInputPwrHighAlarm_Type = EkiOnOff
_PmoailhcAlmClientInputPwrHighAlarm_Object = MibScalar
pmoailhcAlmClientInputPwrHighAlarm = _PmoailhcAlmClientInputPwrHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 2, 2, 32, 4),
    _PmoailhcAlmClientInputPwrHighAlarm_Type()
)
pmoailhcAlmClientInputPwrHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmClientInputPwrHighAlarm.setStatus("current")
_PmoailhcAlmClientOutputPwrLowAlarm_Type = EkiOnOff
_PmoailhcAlmClientOutputPwrLowAlarm_Object = MibScalar
pmoailhcAlmClientOutputPwrLowAlarm = _PmoailhcAlmClientOutputPwrLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 2, 2, 32, 5),
    _PmoailhcAlmClientOutputPwrLowAlarm_Type()
)
pmoailhcAlmClientOutputPwrLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmClientOutputPwrLowAlarm.setStatus("current")
_PmoailhcAlmClientOutputPwrHighAlarm_Type = EkiOnOff
_PmoailhcAlmClientOutputPwrHighAlarm_Object = MibScalar
pmoailhcAlmClientOutputPwrHighAlarm = _PmoailhcAlmClientOutputPwrHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 2, 2, 32, 6),
    _PmoailhcAlmClientOutputPwrHighAlarm_Type()
)
pmoailhcAlmClientOutputPwrHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmClientOutputPwrHighAlarm.setStatus("current")
_PmoailhcAlmClientBiasLowAlarm_Type = EkiOnOff
_PmoailhcAlmClientBiasLowAlarm_Object = MibScalar
pmoailhcAlmClientBiasLowAlarm = _PmoailhcAlmClientBiasLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 2, 2, 32, 7),
    _PmoailhcAlmClientBiasLowAlarm_Type()
)
pmoailhcAlmClientBiasLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmClientBiasLowAlarm.setStatus("current")
_PmoailhcAlmClientBiasHighAlarm_Type = EkiOnOff
_PmoailhcAlmClientBiasHighAlarm_Object = MibScalar
pmoailhcAlmClientBiasHighAlarm = _PmoailhcAlmClientBiasHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 2, 2, 32, 8),
    _PmoailhcAlmClientBiasHighAlarm_Type()
)
pmoailhcAlmClientBiasHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmClientBiasHighAlarm.setStatus("current")
_PmoailhcAlmClientCrit_ObjectIdentity = ObjectIdentity
pmoailhcAlmClientCrit = _PmoailhcAlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 2, 3)
)
_PmoailhcAlmsynthAlm8_ObjectIdentity = ObjectIdentity
pmoailhcAlmsynthAlm8 = _PmoailhcAlmsynthAlm8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 2, 3, 8)
)
_PmoailhcAlmClientHwFail_Type = EkiOnOff
_PmoailhcAlmClientHwFail_Object = MibScalar
pmoailhcAlmClientHwFail = _PmoailhcAlmClientHwFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 2, 3, 8, 4),
    _PmoailhcAlmClientHwFail_Type()
)
pmoailhcAlmClientHwFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmClientHwFail.setStatus("current")
_PmoailhcAlmClientTxOff_Type = EkiOnOff
_PmoailhcAlmClientTxOff_Object = MibScalar
pmoailhcAlmClientTxOff = _PmoailhcAlmClientTxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 2, 3, 8, 5),
    _PmoailhcAlmClientTxOff_Type()
)
pmoailhcAlmClientTxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmClientTxOff.setStatus("current")
_PmoailhcAlmClientDdmWarning_Type = EkiOnOff
_PmoailhcAlmClientDdmWarning_Object = MibScalar
pmoailhcAlmClientDdmWarning = _PmoailhcAlmClientDdmWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 2, 3, 8, 9),
    _PmoailhcAlmClientDdmWarning_Type()
)
pmoailhcAlmClientDdmWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmClientDdmWarning.setStatus("current")
_PmoailhcAlmClientDdmAlm_Type = EkiOnOff
_PmoailhcAlmClientDdmAlm_Object = MibScalar
pmoailhcAlmClientDdmAlm = _PmoailhcAlmClientDdmAlm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 2, 3, 8, 10),
    _PmoailhcAlmClientDdmAlm_Type()
)
pmoailhcAlmClientDdmAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmClientDdmAlm.setStatus("current")
_PmoailhcAlmClientFail_Type = EkiOnOff
_PmoailhcAlmClientFail_Object = MibScalar
pmoailhcAlmClientFail = _PmoailhcAlmClientFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 2, 3, 8, 12),
    _PmoailhcAlmClientFail_Type()
)
pmoailhcAlmClientFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmClientFail.setStatus("current")
_PmoailhcAlmClientExtPumpFail_Type = EkiOnOff
_PmoailhcAlmClientExtPumpFail_Object = MibScalar
pmoailhcAlmClientExtPumpFail = _PmoailhcAlmClientExtPumpFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 2, 3, 8, 13),
    _PmoailhcAlmClientExtPumpFail_Type()
)
pmoailhcAlmClientExtPumpFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmClientExtPumpFail.setStatus("current")
_PmoailhcAlmclientEdfaAlarms2_ObjectIdentity = ObjectIdentity
pmoailhcAlmclientEdfaAlarms2 = _PmoailhcAlmclientEdfaAlarms2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 2, 3, 35)
)
_PmoailhcAlmClientEdfaNr_Type = EkiOnOff
_PmoailhcAlmClientEdfaNr_Object = MibScalar
pmoailhcAlmClientEdfaNr = _PmoailhcAlmClientEdfaNr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 2, 3, 35, 1),
    _PmoailhcAlmClientEdfaNr_Type()
)
pmoailhcAlmClientEdfaNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmClientEdfaNr.setStatus("current")
_PmoailhcAlmClientEdfaTecFail_Type = EkiOnOff
_PmoailhcAlmClientEdfaTecFail_Object = MibScalar
pmoailhcAlmClientEdfaTecFail = _PmoailhcAlmClientEdfaTecFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 2, 3, 35, 2),
    _PmoailhcAlmClientEdfaTecFail_Type()
)
pmoailhcAlmClientEdfaTecFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmClientEdfaTecFail.setStatus("current")
_PmoailhcAlmClientEdfaLaserFail_Type = EkiOnOff
_PmoailhcAlmClientEdfaLaserFail_Object = MibScalar
pmoailhcAlmClientEdfaLaserFail = _PmoailhcAlmClientEdfaLaserFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 2, 3, 35, 3),
    _PmoailhcAlmClientEdfaLaserFail_Type()
)
pmoailhcAlmClientEdfaLaserFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmClientEdfaLaserFail.setStatus("current")
_PmoailhcAlmClientEdfaLos_Type = EkiOnOff
_PmoailhcAlmClientEdfaLos_Object = MibScalar
pmoailhcAlmClientEdfaLos = _PmoailhcAlmClientEdfaLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 2, 3, 35, 4),
    _PmoailhcAlmClientEdfaLos_Type()
)
pmoailhcAlmClientEdfaLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmClientEdfaLos.setStatus("current")
_PmoailhcAlmClientExtPumpEdfaLowCurrent_Type = EkiOnOff
_PmoailhcAlmClientExtPumpEdfaLowCurrent_Object = MibScalar
pmoailhcAlmClientExtPumpEdfaLowCurrent = _PmoailhcAlmClientExtPumpEdfaLowCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 2, 3, 35, 5),
    _PmoailhcAlmClientExtPumpEdfaLowCurrent_Type()
)
pmoailhcAlmClientExtPumpEdfaLowCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmClientExtPumpEdfaLowCurrent.setStatus("current")
_PmoailhcAlmLine_ObjectIdentity = ObjectIdentity
pmoailhcAlmLine = _PmoailhcAlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 3)
)
_PmoailhcAlmLineNurg_ObjectIdentity = ObjectIdentity
pmoailhcAlmLineNurg = _PmoailhcAlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 3, 1)
)
_PmoailhcAlmlineEdfaWarnings_ObjectIdentity = ObjectIdentity
pmoailhcAlmlineEdfaWarnings = _PmoailhcAlmlineEdfaWarnings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 3, 1, 41)
)
_PmoailhcAlmLineGainLowWarning_Type = EkiOnOff
_PmoailhcAlmLineGainLowWarning_Object = MibScalar
pmoailhcAlmLineGainLowWarning = _PmoailhcAlmLineGainLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 3, 1, 41, 1),
    _PmoailhcAlmLineGainLowWarning_Type()
)
pmoailhcAlmLineGainLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmLineGainLowWarning.setStatus("current")
_PmoailhcAlmLineGainHighWarning_Type = EkiOnOff
_PmoailhcAlmLineGainHighWarning_Object = MibScalar
pmoailhcAlmLineGainHighWarning = _PmoailhcAlmLineGainHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 3, 1, 41, 2),
    _PmoailhcAlmLineGainHighWarning_Type()
)
pmoailhcAlmLineGainHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmLineGainHighWarning.setStatus("current")
_PmoailhcAlmLineInputPwrLowWarning_Type = EkiOnOff
_PmoailhcAlmLineInputPwrLowWarning_Object = MibScalar
pmoailhcAlmLineInputPwrLowWarning = _PmoailhcAlmLineInputPwrLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 3, 1, 41, 3),
    _PmoailhcAlmLineInputPwrLowWarning_Type()
)
pmoailhcAlmLineInputPwrLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmLineInputPwrLowWarning.setStatus("current")
_PmoailhcAlmLineInputPwrHighWarning_Type = EkiOnOff
_PmoailhcAlmLineInputPwrHighWarning_Object = MibScalar
pmoailhcAlmLineInputPwrHighWarning = _PmoailhcAlmLineInputPwrHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 3, 1, 41, 4),
    _PmoailhcAlmLineInputPwrHighWarning_Type()
)
pmoailhcAlmLineInputPwrHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmLineInputPwrHighWarning.setStatus("current")
_PmoailhcAlmLineOutputPwrLowWarning_Type = EkiOnOff
_PmoailhcAlmLineOutputPwrLowWarning_Object = MibScalar
pmoailhcAlmLineOutputPwrLowWarning = _PmoailhcAlmLineOutputPwrLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 3, 1, 41, 5),
    _PmoailhcAlmLineOutputPwrLowWarning_Type()
)
pmoailhcAlmLineOutputPwrLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmLineOutputPwrLowWarning.setStatus("current")
_PmoailhcAlmLineOutputPwrHighWarning_Type = EkiOnOff
_PmoailhcAlmLineOutputPwrHighWarning_Object = MibScalar
pmoailhcAlmLineOutputPwrHighWarning = _PmoailhcAlmLineOutputPwrHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 3, 1, 41, 6),
    _PmoailhcAlmLineOutputPwrHighWarning_Type()
)
pmoailhcAlmLineOutputPwrHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmLineOutputPwrHighWarning.setStatus("current")
_PmoailhcAlmLineBiasLowWarning_Type = EkiOnOff
_PmoailhcAlmLineBiasLowWarning_Object = MibScalar
pmoailhcAlmLineBiasLowWarning = _PmoailhcAlmLineBiasLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 3, 1, 41, 7),
    _PmoailhcAlmLineBiasLowWarning_Type()
)
pmoailhcAlmLineBiasLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmLineBiasLowWarning.setStatus("current")
_PmoailhcAlmLineBiasHighWarning_Type = EkiOnOff
_PmoailhcAlmLineBiasHighWarning_Object = MibScalar
pmoailhcAlmLineBiasHighWarning = _PmoailhcAlmLineBiasHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 3, 1, 41, 8),
    _PmoailhcAlmLineBiasHighWarning_Type()
)
pmoailhcAlmLineBiasHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmLineBiasHighWarning.setStatus("current")
_PmoailhcAlmLineUrg_ObjectIdentity = ObjectIdentity
pmoailhcAlmLineUrg = _PmoailhcAlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 3, 2)
)
_PmoailhcAlmlineEdfaAlarms1_ObjectIdentity = ObjectIdentity
pmoailhcAlmlineEdfaAlarms1 = _PmoailhcAlmlineEdfaAlarms1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 3, 2, 40)
)
_PmoailhcAlmLineGainLowAlarm_Type = EkiOnOff
_PmoailhcAlmLineGainLowAlarm_Object = MibScalar
pmoailhcAlmLineGainLowAlarm = _PmoailhcAlmLineGainLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 3, 2, 40, 1),
    _PmoailhcAlmLineGainLowAlarm_Type()
)
pmoailhcAlmLineGainLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmLineGainLowAlarm.setStatus("current")
_PmoailhcAlmLineGainHighAlarm_Type = EkiOnOff
_PmoailhcAlmLineGainHighAlarm_Object = MibScalar
pmoailhcAlmLineGainHighAlarm = _PmoailhcAlmLineGainHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 3, 2, 40, 2),
    _PmoailhcAlmLineGainHighAlarm_Type()
)
pmoailhcAlmLineGainHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmLineGainHighAlarm.setStatus("current")
_PmoailhcAlmLineInputPwrLowAlarm_Type = EkiOnOff
_PmoailhcAlmLineInputPwrLowAlarm_Object = MibScalar
pmoailhcAlmLineInputPwrLowAlarm = _PmoailhcAlmLineInputPwrLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 3, 2, 40, 3),
    _PmoailhcAlmLineInputPwrLowAlarm_Type()
)
pmoailhcAlmLineInputPwrLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmLineInputPwrLowAlarm.setStatus("current")
_PmoailhcAlmLineInputPwrHighAlarm_Type = EkiOnOff
_PmoailhcAlmLineInputPwrHighAlarm_Object = MibScalar
pmoailhcAlmLineInputPwrHighAlarm = _PmoailhcAlmLineInputPwrHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 3, 2, 40, 4),
    _PmoailhcAlmLineInputPwrHighAlarm_Type()
)
pmoailhcAlmLineInputPwrHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmLineInputPwrHighAlarm.setStatus("current")
_PmoailhcAlmLineOutputPwrLowAlarm_Type = EkiOnOff
_PmoailhcAlmLineOutputPwrLowAlarm_Object = MibScalar
pmoailhcAlmLineOutputPwrLowAlarm = _PmoailhcAlmLineOutputPwrLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 3, 2, 40, 5),
    _PmoailhcAlmLineOutputPwrLowAlarm_Type()
)
pmoailhcAlmLineOutputPwrLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmLineOutputPwrLowAlarm.setStatus("current")
_PmoailhcAlmLineOutputPwrHighAlarm_Type = EkiOnOff
_PmoailhcAlmLineOutputPwrHighAlarm_Object = MibScalar
pmoailhcAlmLineOutputPwrHighAlarm = _PmoailhcAlmLineOutputPwrHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 3, 2, 40, 6),
    _PmoailhcAlmLineOutputPwrHighAlarm_Type()
)
pmoailhcAlmLineOutputPwrHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmLineOutputPwrHighAlarm.setStatus("current")
_PmoailhcAlmLineBiasLowAlarm_Type = EkiOnOff
_PmoailhcAlmLineBiasLowAlarm_Object = MibScalar
pmoailhcAlmLineBiasLowAlarm = _PmoailhcAlmLineBiasLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 3, 2, 40, 7),
    _PmoailhcAlmLineBiasLowAlarm_Type()
)
pmoailhcAlmLineBiasLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmLineBiasLowAlarm.setStatus("current")
_PmoailhcAlmLineBiasHighAlarm_Type = EkiOnOff
_PmoailhcAlmLineBiasHighAlarm_Object = MibScalar
pmoailhcAlmLineBiasHighAlarm = _PmoailhcAlmLineBiasHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 3, 2, 40, 8),
    _PmoailhcAlmLineBiasHighAlarm_Type()
)
pmoailhcAlmLineBiasHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmLineBiasHighAlarm.setStatus("current")
_PmoailhcAlmLineCrit_ObjectIdentity = ObjectIdentity
pmoailhcAlmLineCrit = _PmoailhcAlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 3, 3)
)
_PmoailhcAlmsynthAlm7_ObjectIdentity = ObjectIdentity
pmoailhcAlmsynthAlm7 = _PmoailhcAlmsynthAlm7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 3, 3, 7)
)
_PmoailhcAlmLineHwFail_Type = EkiOnOff
_PmoailhcAlmLineHwFail_Object = MibScalar
pmoailhcAlmLineHwFail = _PmoailhcAlmLineHwFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 3, 3, 7, 4),
    _PmoailhcAlmLineHwFail_Type()
)
pmoailhcAlmLineHwFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmLineHwFail.setStatus("current")
_PmoailhcAlmLineTxOff_Type = EkiOnOff
_PmoailhcAlmLineTxOff_Object = MibScalar
pmoailhcAlmLineTxOff = _PmoailhcAlmLineTxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 3, 3, 7, 5),
    _PmoailhcAlmLineTxOff_Type()
)
pmoailhcAlmLineTxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmLineTxOff.setStatus("current")
_PmoailhcAlmLineDdmWarning_Type = EkiOnOff
_PmoailhcAlmLineDdmWarning_Object = MibScalar
pmoailhcAlmLineDdmWarning = _PmoailhcAlmLineDdmWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 3, 3, 7, 9),
    _PmoailhcAlmLineDdmWarning_Type()
)
pmoailhcAlmLineDdmWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmLineDdmWarning.setStatus("current")
_PmoailhcAlmLineDdmAlm_Type = EkiOnOff
_PmoailhcAlmLineDdmAlm_Object = MibScalar
pmoailhcAlmLineDdmAlm = _PmoailhcAlmLineDdmAlm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 3, 3, 7, 10),
    _PmoailhcAlmLineDdmAlm_Type()
)
pmoailhcAlmLineDdmAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmLineDdmAlm.setStatus("current")
_PmoailhcAlmLineFail_Type = EkiOnOff
_PmoailhcAlmLineFail_Object = MibScalar
pmoailhcAlmLineFail = _PmoailhcAlmLineFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 3, 3, 7, 12),
    _PmoailhcAlmLineFail_Type()
)
pmoailhcAlmLineFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmLineFail.setStatus("current")
_PmoailhcAlmLineExtPumpFail_Type = EkiOnOff
_PmoailhcAlmLineExtPumpFail_Object = MibScalar
pmoailhcAlmLineExtPumpFail = _PmoailhcAlmLineExtPumpFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 3, 3, 7, 13),
    _PmoailhcAlmLineExtPumpFail_Type()
)
pmoailhcAlmLineExtPumpFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmLineExtPumpFail.setStatus("current")
_PmoailhcAlmlineEdfaAlarms2_ObjectIdentity = ObjectIdentity
pmoailhcAlmlineEdfaAlarms2 = _PmoailhcAlmlineEdfaAlarms2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 3, 3, 43)
)
_PmoailhcAlmLineEdfaNr_Type = EkiOnOff
_PmoailhcAlmLineEdfaNr_Object = MibScalar
pmoailhcAlmLineEdfaNr = _PmoailhcAlmLineEdfaNr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 3, 3, 43, 1),
    _PmoailhcAlmLineEdfaNr_Type()
)
pmoailhcAlmLineEdfaNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmLineEdfaNr.setStatus("current")
_PmoailhcAlmLineEdfaTecFail_Type = EkiOnOff
_PmoailhcAlmLineEdfaTecFail_Object = MibScalar
pmoailhcAlmLineEdfaTecFail = _PmoailhcAlmLineEdfaTecFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 3, 3, 43, 2),
    _PmoailhcAlmLineEdfaTecFail_Type()
)
pmoailhcAlmLineEdfaTecFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmLineEdfaTecFail.setStatus("current")
_PmoailhcAlmLineEdfaLaserFail_Type = EkiOnOff
_PmoailhcAlmLineEdfaLaserFail_Object = MibScalar
pmoailhcAlmLineEdfaLaserFail = _PmoailhcAlmLineEdfaLaserFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 3, 3, 43, 3),
    _PmoailhcAlmLineEdfaLaserFail_Type()
)
pmoailhcAlmLineEdfaLaserFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmLineEdfaLaserFail.setStatus("current")
_PmoailhcAlmLineEdfaLos_Type = EkiOnOff
_PmoailhcAlmLineEdfaLos_Object = MibScalar
pmoailhcAlmLineEdfaLos = _PmoailhcAlmLineEdfaLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 3, 3, 43, 4),
    _PmoailhcAlmLineEdfaLos_Type()
)
pmoailhcAlmLineEdfaLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmLineEdfaLos.setStatus("current")
_PmoailhcAlmLineExtPumpEdfaLowCurrent_Type = EkiOnOff
_PmoailhcAlmLineExtPumpEdfaLowCurrent_Object = MibScalar
pmoailhcAlmLineExtPumpEdfaLowCurrent = _PmoailhcAlmLineExtPumpEdfaLowCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 2, 3, 3, 43, 5),
    _PmoailhcAlmLineExtPumpEdfaLowCurrent_Type()
)
pmoailhcAlmLineExtPumpEdfaLowCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcAlmLineExtPumpEdfaLowCurrent.setStatus("current")
_Pmoailhcmeasures_ObjectIdentity = ObjectIdentity
pmoailhcmeasures = _Pmoailhcmeasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 3)
)
_PmoailhcMesrOther_ObjectIdentity = ObjectIdentity
pmoailhcMesrOther = _PmoailhcMesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 3, 1)
)


class _PmoailhcMesrtempMeas_Type(Integer32):
    """Custom type pmoailhcMesrtempMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoailhcMesrtempMeas_Type.__name__ = "Integer32"
_PmoailhcMesrtempMeas_Object = MibScalar
pmoailhcMesrtempMeas = _PmoailhcMesrtempMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 3, 1, 72),
    _PmoailhcMesrtempMeas_Type()
)
pmoailhcMesrtempMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcMesrtempMeas.setStatus("current")
_PmoailhcMesrClient_ObjectIdentity = ObjectIdentity
pmoailhcMesrClient = _PmoailhcMesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 3, 2)
)


class _PmoailhcMesrclientEdfaBiasMeas_Type(Integer32):
    """Custom type pmoailhcMesrclientEdfaBiasMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoailhcMesrclientEdfaBiasMeas_Type.__name__ = "Integer32"
_PmoailhcMesrclientEdfaBiasMeas_Object = MibScalar
pmoailhcMesrclientEdfaBiasMeas = _PmoailhcMesrclientEdfaBiasMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 3, 2, 32),
    _PmoailhcMesrclientEdfaBiasMeas_Type()
)
pmoailhcMesrclientEdfaBiasMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcMesrclientEdfaBiasMeas.setStatus("current")


class _PmoailhcMesrclientEdfaTxpwrMeas_Type(Integer32):
    """Custom type pmoailhcMesrclientEdfaTxpwrMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoailhcMesrclientEdfaTxpwrMeas_Type.__name__ = "Integer32"
_PmoailhcMesrclientEdfaTxpwrMeas_Object = MibScalar
pmoailhcMesrclientEdfaTxpwrMeas = _PmoailhcMesrclientEdfaTxpwrMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 3, 2, 33),
    _PmoailhcMesrclientEdfaTxpwrMeas_Type()
)
pmoailhcMesrclientEdfaTxpwrMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcMesrclientEdfaTxpwrMeas.setStatus("current")


class _PmoailhcMesrclientEdfaRxpwrMeas_Type(Integer32):
    """Custom type pmoailhcMesrclientEdfaRxpwrMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoailhcMesrclientEdfaRxpwrMeas_Type.__name__ = "Integer32"
_PmoailhcMesrclientEdfaRxpwrMeas_Object = MibScalar
pmoailhcMesrclientEdfaRxpwrMeas = _PmoailhcMesrclientEdfaRxpwrMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 3, 2, 34),
    _PmoailhcMesrclientEdfaRxpwrMeas_Type()
)
pmoailhcMesrclientEdfaRxpwrMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcMesrclientEdfaRxpwrMeas.setStatus("current")


class _PmoailhcMesrclientEdfaGainMeas_Type(Integer32):
    """Custom type pmoailhcMesrclientEdfaGainMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoailhcMesrclientEdfaGainMeas_Type.__name__ = "Integer32"
_PmoailhcMesrclientEdfaGainMeas_Object = MibScalar
pmoailhcMesrclientEdfaGainMeas = _PmoailhcMesrclientEdfaGainMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 3, 2, 35),
    _PmoailhcMesrclientEdfaGainMeas_Type()
)
pmoailhcMesrclientEdfaGainMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcMesrclientEdfaGainMeas.setStatus("current")


class _PmoailhcMesrclientCorrectedGain_Type(Integer32):
    """Custom type pmoailhcMesrclientCorrectedGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoailhcMesrclientCorrectedGain_Type.__name__ = "Integer32"
_PmoailhcMesrclientCorrectedGain_Object = MibScalar
pmoailhcMesrclientCorrectedGain = _PmoailhcMesrclientCorrectedGain_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 3, 2, 38),
    _PmoailhcMesrclientCorrectedGain_Type()
)
pmoailhcMesrclientCorrectedGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcMesrclientCorrectedGain.setStatus("current")
_PmoailhcMesrLine_ObjectIdentity = ObjectIdentity
pmoailhcMesrLine = _PmoailhcMesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 3, 3)
)


class _PmoailhcMesrlineEdfaBiasMeas_Type(Integer32):
    """Custom type pmoailhcMesrlineEdfaBiasMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoailhcMesrlineEdfaBiasMeas_Type.__name__ = "Integer32"
_PmoailhcMesrlineEdfaBiasMeas_Object = MibScalar
pmoailhcMesrlineEdfaBiasMeas = _PmoailhcMesrlineEdfaBiasMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 3, 3, 40),
    _PmoailhcMesrlineEdfaBiasMeas_Type()
)
pmoailhcMesrlineEdfaBiasMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcMesrlineEdfaBiasMeas.setStatus("current")


class _PmoailhcMesrlineEdfaTxpwrMeas_Type(Integer32):
    """Custom type pmoailhcMesrlineEdfaTxpwrMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoailhcMesrlineEdfaTxpwrMeas_Type.__name__ = "Integer32"
_PmoailhcMesrlineEdfaTxpwrMeas_Object = MibScalar
pmoailhcMesrlineEdfaTxpwrMeas = _PmoailhcMesrlineEdfaTxpwrMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 3, 3, 41),
    _PmoailhcMesrlineEdfaTxpwrMeas_Type()
)
pmoailhcMesrlineEdfaTxpwrMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcMesrlineEdfaTxpwrMeas.setStatus("current")


class _PmoailhcMesrlineEdfaRxpwrMeas_Type(Integer32):
    """Custom type pmoailhcMesrlineEdfaRxpwrMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoailhcMesrlineEdfaRxpwrMeas_Type.__name__ = "Integer32"
_PmoailhcMesrlineEdfaRxpwrMeas_Object = MibScalar
pmoailhcMesrlineEdfaRxpwrMeas = _PmoailhcMesrlineEdfaRxpwrMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 3, 3, 42),
    _PmoailhcMesrlineEdfaRxpwrMeas_Type()
)
pmoailhcMesrlineEdfaRxpwrMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcMesrlineEdfaRxpwrMeas.setStatus("current")


class _PmoailhcMesrlineEdfaGainMeas_Type(Integer32):
    """Custom type pmoailhcMesrlineEdfaGainMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoailhcMesrlineEdfaGainMeas_Type.__name__ = "Integer32"
_PmoailhcMesrlineEdfaGainMeas_Object = MibScalar
pmoailhcMesrlineEdfaGainMeas = _PmoailhcMesrlineEdfaGainMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 3, 3, 43),
    _PmoailhcMesrlineEdfaGainMeas_Type()
)
pmoailhcMesrlineEdfaGainMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcMesrlineEdfaGainMeas.setStatus("current")


class _PmoailhcMesrlineCorrectedGain_Type(Integer32):
    """Custom type pmoailhcMesrlineCorrectedGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoailhcMesrlineCorrectedGain_Type.__name__ = "Integer32"
_PmoailhcMesrlineCorrectedGain_Object = MibScalar
pmoailhcMesrlineCorrectedGain = _PmoailhcMesrlineCorrectedGain_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 3, 3, 46),
    _PmoailhcMesrlineCorrectedGain_Type()
)
pmoailhcMesrlineCorrectedGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcMesrlineCorrectedGain.setStatus("current")
_PmoailhccontrolsWrite_ObjectIdentity = ObjectIdentity
pmoailhccontrolsWrite = _PmoailhccontrolsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 6)
)
_PmoailhcCtrlOther_ObjectIdentity = ObjectIdentity
pmoailhcCtrlOther = _PmoailhcCtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 6, 1)
)
_PmoailhcCtrlsynth0_ObjectIdentity = ObjectIdentity
pmoailhcCtrlsynth0 = _PmoailhcCtrlsynth0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 6, 1, 0)
)
_PmoailhcCtrlConfLoad_Type = EkiOnOff
_PmoailhcCtrlConfLoad_Object = MibScalar
pmoailhcCtrlConfLoad = _PmoailhcCtrlConfLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 6, 1, 0, 1),
    _PmoailhcCtrlConfLoad_Type()
)
pmoailhcCtrlConfLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCtrlConfLoad.setStatus("current")
_PmoailhcCtrlConfFlash_Type = EkiOnOff
_PmoailhcCtrlConfFlash_Object = MibScalar
pmoailhcCtrlConfFlash = _PmoailhcCtrlConfFlash_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 6, 1, 0, 9),
    _PmoailhcCtrlConfFlash_Type()
)
pmoailhcCtrlConfFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCtrlConfFlash.setStatus("current")
_PmoailhcCtrlConfClear_Type = EkiOnOff
_PmoailhcCtrlConfClear_Object = MibScalar
pmoailhcCtrlConfClear = _PmoailhcCtrlConfClear_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 6, 1, 0, 13),
    _PmoailhcCtrlConfClear_Type()
)
pmoailhcCtrlConfClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCtrlConfClear.setStatus("current")
_PmoailhcCtrlswMgnt_ObjectIdentity = ObjectIdentity
pmoailhcCtrlswMgnt = _PmoailhcCtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 6, 1, 5)
)
_PmoailhcCtrlColdReset_Type = EkiOnOff
_PmoailhcCtrlColdReset_Object = MibScalar
pmoailhcCtrlColdReset = _PmoailhcCtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 6, 1, 5, 2),
    _PmoailhcCtrlColdReset_Type()
)
pmoailhcCtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCtrlColdReset.setStatus("current")
_PmoailhcCtrlWarmReset_Type = EkiOnOff
_PmoailhcCtrlWarmReset_Object = MibScalar
pmoailhcCtrlWarmReset = _PmoailhcCtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 6, 1, 5, 3),
    _PmoailhcCtrlWarmReset_Type()
)
pmoailhcCtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCtrlWarmReset.setStatus("current")
_PmoailhcCtrlledTest_ObjectIdentity = ObjectIdentity
pmoailhcCtrlledTest = _PmoailhcCtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 6, 1, 73)
)
_PmoailhcCtrlGreenLed_Type = EkiOnOff
_PmoailhcCtrlGreenLed_Object = MibScalar
pmoailhcCtrlGreenLed = _PmoailhcCtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 6, 1, 73, 1),
    _PmoailhcCtrlGreenLed_Type()
)
pmoailhcCtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCtrlGreenLed.setStatus("current")
_PmoailhcCtrlRedLed_Type = EkiOnOff
_PmoailhcCtrlRedLed_Object = MibScalar
pmoailhcCtrlRedLed = _PmoailhcCtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 6, 1, 73, 2),
    _PmoailhcCtrlRedLed_Type()
)
pmoailhcCtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCtrlRedLed.setStatus("current")
_PmoailhcCtrlLedOff_Type = EkiOnOff
_PmoailhcCtrlLedOff_Object = MibScalar
pmoailhcCtrlLedOff = _PmoailhcCtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 6, 1, 73, 3),
    _PmoailhcCtrlLedOff_Type()
)
pmoailhcCtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCtrlLedOff.setStatus("current")
_PmoailhcCtrlmaintMode_ObjectIdentity = ObjectIdentity
pmoailhcCtrlmaintMode = _PmoailhcCtrlmaintMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 6, 1, 75)
)
_PmoailhcCtrlMaintenance_Type = EkiOnOff
_PmoailhcCtrlMaintenance_Object = MibScalar
pmoailhcCtrlMaintenance = _PmoailhcCtrlMaintenance_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 6, 1, 75, 1),
    _PmoailhcCtrlMaintenance_Type()
)
pmoailhcCtrlMaintenance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCtrlMaintenance.setStatus("current")
_PmoailhcCtrlaprRestart_ObjectIdentity = ObjectIdentity
pmoailhcCtrlaprRestart = _PmoailhcCtrlaprRestart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 6, 1, 76)
)
_PmoailhcCtrlAprManualRestart_Type = EkiOnOff
_PmoailhcCtrlAprManualRestart_Object = MibScalar
pmoailhcCtrlAprManualRestart = _PmoailhcCtrlAprManualRestart_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 6, 1, 76, 1),
    _PmoailhcCtrlAprManualRestart_Type()
)
pmoailhcCtrlAprManualRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCtrlAprManualRestart.setStatus("current")
_PmoailhcCtrlClient_ObjectIdentity = ObjectIdentity
pmoailhcCtrlClient = _PmoailhcCtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 6, 2)
)
_PmoailhcCtrlclientEdfaLaserOff_ObjectIdentity = ObjectIdentity
pmoailhcCtrlclientEdfaLaserOff = _PmoailhcCtrlclientEdfaLaserOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 6, 2, 32)
)
_PmoailhcCtrlClientEdfaLaserOff_Type = EkiOnOff
_PmoailhcCtrlClientEdfaLaserOff_Object = MibScalar
pmoailhcCtrlClientEdfaLaserOff = _PmoailhcCtrlClientEdfaLaserOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 6, 2, 32, 1),
    _PmoailhcCtrlClientEdfaLaserOff_Type()
)
pmoailhcCtrlClientEdfaLaserOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCtrlClientEdfaLaserOff.setStatus("current")


class _PmoailhcCtrlclientGainCstMonitorValue_Type(Integer32):
    """Custom type pmoailhcCtrlclientGainCstMonitorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoailhcCtrlclientGainCstMonitorValue_Type.__name__ = "Integer32"
_PmoailhcCtrlclientGainCstMonitorValue_Object = MibScalar
pmoailhcCtrlclientGainCstMonitorValue = _PmoailhcCtrlclientGainCstMonitorValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 6, 2, 34),
    _PmoailhcCtrlclientGainCstMonitorValue_Type()
)
pmoailhcCtrlclientGainCstMonitorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCtrlclientGainCstMonitorValue.setStatus("current")


class _PmoailhcCtrlclientGainCstPoutValue_Type(Integer32):
    """Custom type pmoailhcCtrlclientGainCstPoutValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoailhcCtrlclientGainCstPoutValue_Type.__name__ = "Integer32"
_PmoailhcCtrlclientGainCstPoutValue_Object = MibScalar
pmoailhcCtrlclientGainCstPoutValue = _PmoailhcCtrlclientGainCstPoutValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 6, 2, 35),
    _PmoailhcCtrlclientGainCstPoutValue_Type()
)
pmoailhcCtrlclientGainCstPoutValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCtrlclientGainCstPoutValue.setStatus("current")


class _PmoailhcCtrlclientGainSettingValue_Type(Integer32):
    """Custom type pmoailhcCtrlclientGainSettingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoailhcCtrlclientGainSettingValue_Type.__name__ = "Integer32"
_PmoailhcCtrlclientGainSettingValue_Object = MibScalar
pmoailhcCtrlclientGainSettingValue = _PmoailhcCtrlclientGainSettingValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 6, 2, 36),
    _PmoailhcCtrlclientGainSettingValue_Type()
)
pmoailhcCtrlclientGainSettingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCtrlclientGainSettingValue.setStatus("current")
_PmoailhcCtrlclientGainProcessing_ObjectIdentity = ObjectIdentity
pmoailhcCtrlclientGainProcessing = _PmoailhcCtrlclientGainProcessing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 6, 2, 37)
)
_PmoailhcCtrlClientGainProc_Type = EkiOnOff
_PmoailhcCtrlClientGainProc_Object = MibScalar
pmoailhcCtrlClientGainProc = _PmoailhcCtrlClientGainProc_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 6, 2, 37, 1),
    _PmoailhcCtrlClientGainProc_Type()
)
pmoailhcCtrlClientGainProc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCtrlClientGainProc.setStatus("current")


class _PmoailhcCtrlclientGainCstFiberAgingMarginValue_Type(Integer32):
    """Custom type pmoailhcCtrlclientGainCstFiberAgingMarginValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoailhcCtrlclientGainCstFiberAgingMarginValue_Type.__name__ = "Integer32"
_PmoailhcCtrlclientGainCstFiberAgingMarginValue_Object = MibScalar
pmoailhcCtrlclientGainCstFiberAgingMarginValue = _PmoailhcCtrlclientGainCstFiberAgingMarginValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 6, 2, 38),
    _PmoailhcCtrlclientGainCstFiberAgingMarginValue_Type()
)
pmoailhcCtrlclientGainCstFiberAgingMarginValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCtrlclientGainCstFiberAgingMarginValue.setStatus("current")


class _PmoailhcCtrlclientGainCstAdddropMarginValue_Type(Integer32):
    """Custom type pmoailhcCtrlclientGainCstAdddropMarginValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoailhcCtrlclientGainCstAdddropMarginValue_Type.__name__ = "Integer32"
_PmoailhcCtrlclientGainCstAdddropMarginValue_Object = MibScalar
pmoailhcCtrlclientGainCstAdddropMarginValue = _PmoailhcCtrlclientGainCstAdddropMarginValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 6, 2, 39),
    _PmoailhcCtrlclientGainCstAdddropMarginValue_Type()
)
pmoailhcCtrlclientGainCstAdddropMarginValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCtrlclientGainCstAdddropMarginValue.setStatus("current")
_PmoailhcCtrlLine_ObjectIdentity = ObjectIdentity
pmoailhcCtrlLine = _PmoailhcCtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 6, 3)
)
_PmoailhcCtrllineEdfaLaserOff_ObjectIdentity = ObjectIdentity
pmoailhcCtrllineEdfaLaserOff = _PmoailhcCtrllineEdfaLaserOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 6, 3, 40)
)
_PmoailhcCtrlLineEdfaLaserOff_Type = EkiOnOff
_PmoailhcCtrlLineEdfaLaserOff_Object = MibScalar
pmoailhcCtrlLineEdfaLaserOff = _PmoailhcCtrlLineEdfaLaserOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 6, 3, 40, 1),
    _PmoailhcCtrlLineEdfaLaserOff_Type()
)
pmoailhcCtrlLineEdfaLaserOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCtrlLineEdfaLaserOff.setStatus("current")


class _PmoailhcCtrllineGainCstMonitorValue_Type(Integer32):
    """Custom type pmoailhcCtrllineGainCstMonitorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoailhcCtrllineGainCstMonitorValue_Type.__name__ = "Integer32"
_PmoailhcCtrllineGainCstMonitorValue_Object = MibScalar
pmoailhcCtrllineGainCstMonitorValue = _PmoailhcCtrllineGainCstMonitorValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 6, 3, 42),
    _PmoailhcCtrllineGainCstMonitorValue_Type()
)
pmoailhcCtrllineGainCstMonitorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCtrllineGainCstMonitorValue.setStatus("current")


class _PmoailhcCtrllineGainCstPoutValue_Type(Integer32):
    """Custom type pmoailhcCtrllineGainCstPoutValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoailhcCtrllineGainCstPoutValue_Type.__name__ = "Integer32"
_PmoailhcCtrllineGainCstPoutValue_Object = MibScalar
pmoailhcCtrllineGainCstPoutValue = _PmoailhcCtrllineGainCstPoutValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 6, 3, 43),
    _PmoailhcCtrllineGainCstPoutValue_Type()
)
pmoailhcCtrllineGainCstPoutValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCtrllineGainCstPoutValue.setStatus("current")


class _PmoailhcCtrllineGainSettingValue_Type(Integer32):
    """Custom type pmoailhcCtrllineGainSettingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoailhcCtrllineGainSettingValue_Type.__name__ = "Integer32"
_PmoailhcCtrllineGainSettingValue_Object = MibScalar
pmoailhcCtrllineGainSettingValue = _PmoailhcCtrllineGainSettingValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 6, 3, 44),
    _PmoailhcCtrllineGainSettingValue_Type()
)
pmoailhcCtrllineGainSettingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCtrllineGainSettingValue.setStatus("current")
_PmoailhcCtrllineGainProcessing_ObjectIdentity = ObjectIdentity
pmoailhcCtrllineGainProcessing = _PmoailhcCtrllineGainProcessing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 6, 3, 45)
)
_PmoailhcCtrlLineGainProc_Type = EkiOnOff
_PmoailhcCtrlLineGainProc_Object = MibScalar
pmoailhcCtrlLineGainProc = _PmoailhcCtrlLineGainProc_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 6, 3, 45, 1),
    _PmoailhcCtrlLineGainProc_Type()
)
pmoailhcCtrlLineGainProc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCtrlLineGainProc.setStatus("current")


class _PmoailhcCtrllineGainCstFiberAgingMarginValue_Type(Integer32):
    """Custom type pmoailhcCtrllineGainCstFiberAgingMarginValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoailhcCtrllineGainCstFiberAgingMarginValue_Type.__name__ = "Integer32"
_PmoailhcCtrllineGainCstFiberAgingMarginValue_Object = MibScalar
pmoailhcCtrllineGainCstFiberAgingMarginValue = _PmoailhcCtrllineGainCstFiberAgingMarginValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 6, 3, 46),
    _PmoailhcCtrllineGainCstFiberAgingMarginValue_Type()
)
pmoailhcCtrllineGainCstFiberAgingMarginValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCtrllineGainCstFiberAgingMarginValue.setStatus("current")


class _PmoailhcCtrllineGainCstAdddropMarginValue_Type(Integer32):
    """Custom type pmoailhcCtrllineGainCstAdddropMarginValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmoailhcCtrllineGainCstAdddropMarginValue_Type.__name__ = "Integer32"
_PmoailhcCtrllineGainCstAdddropMarginValue_Object = MibScalar
pmoailhcCtrllineGainCstAdddropMarginValue = _PmoailhcCtrllineGainCstAdddropMarginValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 6, 3, 47),
    _PmoailhcCtrllineGainCstAdddropMarginValue_Type()
)
pmoailhcCtrllineGainCstAdddropMarginValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCtrllineGainCstAdddropMarginValue.setStatus("current")
_Pmoailhcri_ObjectIdentity = ObjectIdentity
pmoailhcri = _Pmoailhcri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 7)
)
_PmoailhcRinvReloadInventory_Type = EkiOnOff
_PmoailhcRinvReloadInventory_Object = MibScalar
pmoailhcRinvReloadInventory = _PmoailhcRinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 7, 2),
    _PmoailhcRinvReloadInventory_Type()
)
pmoailhcRinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcRinvReloadInventory.setStatus("current")
_PmoailhcRinvModulePlatform_Type = DisplayString
_PmoailhcRinvModulePlatform_Object = MibScalar
pmoailhcRinvModulePlatform = _PmoailhcRinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 7, 3),
    _PmoailhcRinvModulePlatform_Type()
)
pmoailhcRinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcRinvModulePlatform.setStatus("current")
_PmoailhcRinvSwPlatform_Type = DisplayString
_PmoailhcRinvSwPlatform_Object = MibScalar
pmoailhcRinvSwPlatform = _PmoailhcRinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 7, 4),
    _PmoailhcRinvSwPlatform_Type()
)
pmoailhcRinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcRinvSwPlatform.setStatus("current")
_PmoailhcRinvSwFoa_Type = DisplayString
_PmoailhcRinvSwFoa_Object = MibScalar
pmoailhcRinvSwFoa = _PmoailhcRinvSwFoa_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 7, 5),
    _PmoailhcRinvSwFoa_Type()
)
pmoailhcRinvSwFoa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcRinvSwFoa.setStatus("current")
_PmoailhcRinvInLine1Table_Object = MibTable
pmoailhcRinvInLine1Table = _PmoailhcRinvInLine1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 7, 6)
)
if mibBuilder.loadTexts:
    pmoailhcRinvInLine1Table.setStatus("current")
_PmoailhcRinvInLine1Entry_Object = MibTableRow
pmoailhcRinvInLine1Entry = _PmoailhcRinvInLine1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 7, 6, 1)
)
pmoailhcRinvInLine1Entry.setIndexNames(
    (0, "EKINOPS-PmOailhc-MIB", "pmoailhcRinvInLine1Index"),
)
if mibBuilder.loadTexts:
    pmoailhcRinvInLine1Entry.setStatus("current")


class _PmoailhcRinvInLine1Index_Type(Integer32):
    """Custom type pmoailhcRinvInLine1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PmoailhcRinvInLine1Index_Type.__name__ = "Integer32"
_PmoailhcRinvInLine1Index_Object = MibTableColumn
pmoailhcRinvInLine1Index = _PmoailhcRinvInLine1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 7, 6, 1, 1),
    _PmoailhcRinvInLine1Index_Type()
)
pmoailhcRinvInLine1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcRinvInLine1Index.setStatus("current")
_PmoailhcRinvInLine1_Type = DisplayString
_PmoailhcRinvInLine1_Object = MibTableColumn
pmoailhcRinvInLine1 = _PmoailhcRinvInLine1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 7, 6, 1, 2),
    _PmoailhcRinvInLine1_Type()
)
pmoailhcRinvInLine1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcRinvInLine1.setStatus("current")
_PmoailhcRinvInLine2Table_Object = MibTable
pmoailhcRinvInLine2Table = _PmoailhcRinvInLine2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 7, 7)
)
if mibBuilder.loadTexts:
    pmoailhcRinvInLine2Table.setStatus("current")
_PmoailhcRinvInLine2Entry_Object = MibTableRow
pmoailhcRinvInLine2Entry = _PmoailhcRinvInLine2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 7, 7, 1)
)
pmoailhcRinvInLine2Entry.setIndexNames(
    (0, "EKINOPS-PmOailhc-MIB", "pmoailhcRinvInLine2Index"),
)
if mibBuilder.loadTexts:
    pmoailhcRinvInLine2Entry.setStatus("current")


class _PmoailhcRinvInLine2Index_Type(Integer32):
    """Custom type pmoailhcRinvInLine2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PmoailhcRinvInLine2Index_Type.__name__ = "Integer32"
_PmoailhcRinvInLine2Index_Object = MibTableColumn
pmoailhcRinvInLine2Index = _PmoailhcRinvInLine2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 7, 7, 1, 1),
    _PmoailhcRinvInLine2Index_Type()
)
pmoailhcRinvInLine2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcRinvInLine2Index.setStatus("current")
_PmoailhcRinvInLine2_Type = DisplayString
_PmoailhcRinvInLine2_Object = MibTableColumn
pmoailhcRinvInLine2 = _PmoailhcRinvInLine2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 7, 7, 1, 2),
    _PmoailhcRinvInLine2_Type()
)
pmoailhcRinvInLine2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcRinvInLine2.setStatus("current")
_PmoailhcConfig_ObjectIdentity = ObjectIdentity
pmoailhcConfig = _PmoailhcConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 9)
)
_PmoailhcCfgNoValue_ObjectIdentity = ObjectIdentity
pmoailhcCfgNoValue = _PmoailhcCfgNoValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 9, 1)
)
_PmoailhctableclientStartup_ObjectIdentity = ObjectIdentity
pmoailhctableclientStartup = _PmoailhctableclientStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 9, 1, 1)
)


class _PmoailhcCfgclientEdfaLaserCtrl_Type(Unsigned32):
    """Custom type pmoailhcCfgclientEdfaLaserCtrl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoailhcCfgclientEdfaLaserCtrl_Type.__name__ = "Unsigned32"
_PmoailhcCfgclientEdfaLaserCtrl_Object = MibScalar
pmoailhcCfgclientEdfaLaserCtrl = _PmoailhcCfgclientEdfaLaserCtrl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 9, 1, 1, 2),
    _PmoailhcCfgclientEdfaLaserCtrl_Type()
)
pmoailhcCfgclientEdfaLaserCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCfgclientEdfaLaserCtrl.setStatus("current")


class _PmoailhcCfgclientEdfaLaserMode_Type(Unsigned32):
    """Custom type pmoailhcCfgclientEdfaLaserMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoailhcCfgclientEdfaLaserMode_Type.__name__ = "Unsigned32"
_PmoailhcCfgclientEdfaLaserMode_Object = MibScalar
pmoailhcCfgclientEdfaLaserMode = _PmoailhcCfgclientEdfaLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 9, 1, 1, 3),
    _PmoailhcCfgclientEdfaLaserMode_Type()
)
pmoailhcCfgclientEdfaLaserMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCfgclientEdfaLaserMode.setStatus("current")


class _PmoailhcCfgclientGainValue_Type(Unsigned32):
    """Custom type pmoailhcCfgclientGainValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoailhcCfgclientGainValue_Type.__name__ = "Unsigned32"
_PmoailhcCfgclientGainValue_Object = MibScalar
pmoailhcCfgclientGainValue = _PmoailhcCfgclientGainValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 9, 1, 1, 4),
    _PmoailhcCfgclientGainValue_Type()
)
pmoailhcCfgclientGainValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCfgclientGainValue.setStatus("current")


class _PmoailhcCfgclientTiltValue_Type(Unsigned32):
    """Custom type pmoailhcCfgclientTiltValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoailhcCfgclientTiltValue_Type.__name__ = "Unsigned32"
_PmoailhcCfgclientTiltValue_Object = MibScalar
pmoailhcCfgclientTiltValue = _PmoailhcCfgclientTiltValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 9, 1, 1, 5),
    _PmoailhcCfgclientTiltValue_Type()
)
pmoailhcCfgclientTiltValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCfgclientTiltValue.setStatus("current")


class _PmoailhcCfgclientMsaLoss_Type(Unsigned32):
    """Custom type pmoailhcCfgclientMsaLoss based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoailhcCfgclientMsaLoss_Type.__name__ = "Unsigned32"
_PmoailhcCfgclientMsaLoss_Object = MibScalar
pmoailhcCfgclientMsaLoss = _PmoailhcCfgclientMsaLoss_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 9, 1, 1, 6),
    _PmoailhcCfgclientMsaLoss_Type()
)
pmoailhcCfgclientMsaLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCfgclientMsaLoss.setStatus("current")


class _PmoailhcCfgclientOutputPowerValue_Type(Unsigned32):
    """Custom type pmoailhcCfgclientOutputPowerValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoailhcCfgclientOutputPowerValue_Type.__name__ = "Unsigned32"
_PmoailhcCfgclientOutputPowerValue_Object = MibScalar
pmoailhcCfgclientOutputPowerValue = _PmoailhcCfgclientOutputPowerValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 9, 1, 1, 7),
    _PmoailhcCfgclientOutputPowerValue_Type()
)
pmoailhcCfgclientOutputPowerValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCfgclientOutputPowerValue.setStatus("current")


class _PmoailhcCfgclientAseCompensation_Type(Unsigned32):
    """Custom type pmoailhcCfgclientAseCompensation based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoailhcCfgclientAseCompensation_Type.__name__ = "Unsigned32"
_PmoailhcCfgclientAseCompensation_Object = MibScalar
pmoailhcCfgclientAseCompensation = _PmoailhcCfgclientAseCompensation_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 9, 1, 1, 8),
    _PmoailhcCfgclientAseCompensation_Type()
)
pmoailhcCfgclientAseCompensation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCfgclientAseCompensation.setStatus("current")
_PmoailhcCfgLineStartUp_ObjectIdentity = ObjectIdentity
pmoailhcCfgLineStartUp = _PmoailhcCfgLineStartUp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 9, 2)
)
_PmoailhctablelineStartup_ObjectIdentity = ObjectIdentity
pmoailhctablelineStartup = _PmoailhctablelineStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 9, 2, 1)
)


class _PmoailhcCfglineEdfaLaserCtrl_Type(Unsigned32):
    """Custom type pmoailhcCfglineEdfaLaserCtrl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoailhcCfglineEdfaLaserCtrl_Type.__name__ = "Unsigned32"
_PmoailhcCfglineEdfaLaserCtrl_Object = MibScalar
pmoailhcCfglineEdfaLaserCtrl = _PmoailhcCfglineEdfaLaserCtrl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 9, 2, 1, 2),
    _PmoailhcCfglineEdfaLaserCtrl_Type()
)
pmoailhcCfglineEdfaLaserCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCfglineEdfaLaserCtrl.setStatus("current")


class _PmoailhcCfglineEdfaLaserMode_Type(Unsigned32):
    """Custom type pmoailhcCfglineEdfaLaserMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoailhcCfglineEdfaLaserMode_Type.__name__ = "Unsigned32"
_PmoailhcCfglineEdfaLaserMode_Object = MibScalar
pmoailhcCfglineEdfaLaserMode = _PmoailhcCfglineEdfaLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 9, 2, 1, 3),
    _PmoailhcCfglineEdfaLaserMode_Type()
)
pmoailhcCfglineEdfaLaserMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCfglineEdfaLaserMode.setStatus("current")


class _PmoailhcCfglineGainValue_Type(Unsigned32):
    """Custom type pmoailhcCfglineGainValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoailhcCfglineGainValue_Type.__name__ = "Unsigned32"
_PmoailhcCfglineGainValue_Object = MibScalar
pmoailhcCfglineGainValue = _PmoailhcCfglineGainValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 9, 2, 1, 4),
    _PmoailhcCfglineGainValue_Type()
)
pmoailhcCfglineGainValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCfglineGainValue.setStatus("current")


class _PmoailhcCfglineTiltValue_Type(Unsigned32):
    """Custom type pmoailhcCfglineTiltValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoailhcCfglineTiltValue_Type.__name__ = "Unsigned32"
_PmoailhcCfglineTiltValue_Object = MibScalar
pmoailhcCfglineTiltValue = _PmoailhcCfglineTiltValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 9, 2, 1, 5),
    _PmoailhcCfglineTiltValue_Type()
)
pmoailhcCfglineTiltValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCfglineTiltValue.setStatus("current")


class _PmoailhcCfglineMsaLoss_Type(Unsigned32):
    """Custom type pmoailhcCfglineMsaLoss based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoailhcCfglineMsaLoss_Type.__name__ = "Unsigned32"
_PmoailhcCfglineMsaLoss_Object = MibScalar
pmoailhcCfglineMsaLoss = _PmoailhcCfglineMsaLoss_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 9, 2, 1, 6),
    _PmoailhcCfglineMsaLoss_Type()
)
pmoailhcCfglineMsaLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCfglineMsaLoss.setStatus("current")


class _PmoailhcCfglineOutputPowerValue_Type(Unsigned32):
    """Custom type pmoailhcCfglineOutputPowerValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoailhcCfglineOutputPowerValue_Type.__name__ = "Unsigned32"
_PmoailhcCfglineOutputPowerValue_Object = MibScalar
pmoailhcCfglineOutputPowerValue = _PmoailhcCfglineOutputPowerValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 9, 2, 1, 7),
    _PmoailhcCfglineOutputPowerValue_Type()
)
pmoailhcCfglineOutputPowerValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCfglineOutputPowerValue.setStatus("current")


class _PmoailhcCfglineAseCompensation_Type(Unsigned32):
    """Custom type pmoailhcCfglineAseCompensation based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoailhcCfglineAseCompensation_Type.__name__ = "Unsigned32"
_PmoailhcCfglineAseCompensation_Object = MibScalar
pmoailhcCfglineAseCompensation = _PmoailhcCfglineAseCompensation_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 9, 2, 1, 8),
    _PmoailhcCfglineAseCompensation_Type()
)
pmoailhcCfglineAseCompensation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCfglineAseCompensation.setStatus("current")


class _PmoailhcCfgaprMode_Type(Unsigned32):
    """Custom type pmoailhcCfgaprMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmoailhcCfgaprMode_Type.__name__ = "Unsigned32"
_PmoailhcCfgaprMode_Object = MibScalar
pmoailhcCfgaprMode = _PmoailhcCfgaprMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 9, 2, 1, 11),
    _PmoailhcCfgaprMode_Type()
)
pmoailhcCfgaprMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCfgaprMode.setStatus("current")
_PmoailhcCfgLabels_ObjectIdentity = ObjectIdentity
pmoailhcCfgLabels = _PmoailhcCfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 9, 3)
)
_PmoailhcCfgLabelclientTable_Object = MibTable
pmoailhcCfgLabelclientTable = _PmoailhcCfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 9, 3, 1)
)
if mibBuilder.loadTexts:
    pmoailhcCfgLabelclientTable.setStatus("current")
_PmoailhcCfgLabelclientEntry_Object = MibTableRow
pmoailhcCfgLabelclientEntry = _PmoailhcCfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 9, 3, 1, 1)
)
pmoailhcCfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-PmOailhc-MIB", "pmoailhcCfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pmoailhcCfgLabelclientEntry.setStatus("current")


class _PmoailhcCfgLabelclientIndex_Type(Integer32):
    """Custom type pmoailhcCfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmoailhcCfgLabelclientIndex_Type.__name__ = "Integer32"
_PmoailhcCfgLabelclientIndex_Object = MibTableColumn
pmoailhcCfgLabelclientIndex = _PmoailhcCfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 9, 3, 1, 1, 1),
    _PmoailhcCfgLabelclientIndex_Type()
)
pmoailhcCfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcCfgLabelclientIndex.setStatus("current")


class _PmoailhcCfgLabelclientPortn_Type(DisplayString):
    """Custom type pmoailhcCfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PmoailhcCfgLabelclientPortn_Type.__name__ = "DisplayString"
_PmoailhcCfgLabelclientPortn_Object = MibTableColumn
pmoailhcCfgLabelclientPortn = _PmoailhcCfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 9, 3, 1, 1, 3),
    _PmoailhcCfgLabelclientPortn_Type()
)
pmoailhcCfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCfgLabelclientPortn.setStatus("current")
_PmoailhcCfgLabellineTable_Object = MibTable
pmoailhcCfgLabellineTable = _PmoailhcCfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 9, 3, 2)
)
if mibBuilder.loadTexts:
    pmoailhcCfgLabellineTable.setStatus("current")
_PmoailhcCfgLabellineEntry_Object = MibTableRow
pmoailhcCfgLabellineEntry = _PmoailhcCfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 9, 3, 2, 1)
)
pmoailhcCfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-PmOailhc-MIB", "pmoailhcCfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pmoailhcCfgLabellineEntry.setStatus("current")


class _PmoailhcCfgLabellineIndex_Type(Integer32):
    """Custom type pmoailhcCfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmoailhcCfgLabellineIndex_Type.__name__ = "Integer32"
_PmoailhcCfgLabellineIndex_Object = MibTableColumn
pmoailhcCfgLabellineIndex = _PmoailhcCfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 9, 3, 2, 1, 1),
    _PmoailhcCfgLabellineIndex_Type()
)
pmoailhcCfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhcCfgLabellineIndex.setStatus("current")


class _PmoailhcCfgLabellinePortn_Type(DisplayString):
    """Custom type pmoailhcCfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PmoailhcCfgLabellinePortn_Type.__name__ = "DisplayString"
_PmoailhcCfgLabellinePortn_Object = MibTableColumn
pmoailhcCfgLabellinePortn = _PmoailhcCfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 9, 3, 2, 1, 3),
    _PmoailhcCfgLabellinePortn_Type()
)
pmoailhcCfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCfgLabellinePortn.setStatus("current")
_PmoailhcCfgWriteConfiguration_Type = EkiOnOff
_PmoailhcCfgWriteConfiguration_Object = MibScalar
pmoailhcCfgWriteConfiguration = _PmoailhcCfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 9, 257),
    _PmoailhcCfgWriteConfiguration_Type()
)
pmoailhcCfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmoailhcCfgWriteConfiguration.setStatus("current")
_Pmoailhctraps_ObjectIdentity = ObjectIdentity
pmoailhctraps = _Pmoailhctraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 55, 10)
)


class _PmoailhctrapBoardNumber_Type(Integer32):
    """Custom type pmoailhctrapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_PmoailhctrapBoardNumber_Type.__name__ = "Integer32"
_PmoailhctrapBoardNumber_Object = MibScalar
pmoailhctrapBoardNumber = _PmoailhctrapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 55, 10, 4),
    _PmoailhctrapBoardNumber_Type()
)
pmoailhctrapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmoailhctrapBoardNumber.setStatus("current")

# Managed Objects groups


# Notification objects

pmoailhcLineTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 55, 10, 30)
)
pmoailhcLineTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-PmOailhc-MIB", "pmoailhcAlmLineDdmWarning"),
        ("EKINOPS-PmOailhc-MIB", "pmoailhctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoailhcLineTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pmoailhcLineTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 55, 10, 31)
)
pmoailhcLineTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-PmOailhc-MIB", "pmoailhcAlmLineDdmWarning"),
        ("EKINOPS-PmOailhc-MIB", "pmoailhctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoailhcLineTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pmoailhcLineTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 55, 10, 32)
)
pmoailhcLineTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-PmOailhc-MIB", "pmoailhcAlmLineDdmAlm"),
        ("EKINOPS-PmOailhc-MIB", "pmoailhctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoailhcLineTrapUrgentGoesOn.setStatus(
        "current"
    )

pmoailhcLineTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 55, 10, 33)
)
pmoailhcLineTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-PmOailhc-MIB", "pmoailhcAlmLineDdmAlm"),
        ("EKINOPS-PmOailhc-MIB", "pmoailhctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoailhcLineTrapUrgentGoesOff.setStatus(
        "current"
    )

pmoailhcLineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 55, 10, 34)
)
pmoailhcLineTrapCritGoesOn.setObjects(
      *(("EKINOPS-PmOailhc-MIB", "pmoailhcAlmLineFail"),
        ("EKINOPS-PmOailhc-MIB", "pmoailhcAlmLineHwFail"),
        ("EKINOPS-PmOailhc-MIB", "pmoailhctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoailhcLineTrapCritGoesOn.setStatus(
        "current"
    )

pmoailhcLineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 55, 10, 35)
)
pmoailhcLineTrapCritGoesOff.setObjects(
      *(("EKINOPS-PmOailhc-MIB", "pmoailhcAlmLineFail"),
        ("EKINOPS-PmOailhc-MIB", "pmoailhcAlmLineHwFail"),
        ("EKINOPS-PmOailhc-MIB", "pmoailhctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoailhcLineTrapCritGoesOff.setStatus(
        "current"
    )

pmoailhcClientTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 55, 10, 40)
)
pmoailhcClientTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-PmOailhc-MIB", "pmoailhcAlmClientDdmWarning"),
        ("EKINOPS-PmOailhc-MIB", "pmoailhctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoailhcClientTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pmoailhcClientTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 55, 10, 41)
)
pmoailhcClientTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-PmOailhc-MIB", "pmoailhcAlmClientDdmWarning"),
        ("EKINOPS-PmOailhc-MIB", "pmoailhctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoailhcClientTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pmoailhcClientTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 55, 10, 42)
)
pmoailhcClientTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-PmOailhc-MIB", "pmoailhcAlmClientDdmAlm"),
        ("EKINOPS-PmOailhc-MIB", "pmoailhctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoailhcClientTrapUrgentGoesOn.setStatus(
        "current"
    )

pmoailhcClientTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 55, 10, 43)
)
pmoailhcClientTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-PmOailhc-MIB", "pmoailhcAlmClientDdmAlm"),
        ("EKINOPS-PmOailhc-MIB", "pmoailhctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoailhcClientTrapUrgentGoesOff.setStatus(
        "current"
    )

pmoailhcClientTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 55, 10, 44)
)
pmoailhcClientTrapCritGoesOn.setObjects(
      *(("EKINOPS-PmOailhc-MIB", "pmoailhcAlmClientFail"),
        ("EKINOPS-PmOailhc-MIB", "pmoailhcAlmClientHwFail"),
        ("EKINOPS-PmOailhc-MIB", "pmoailhctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoailhcClientTrapCritGoesOn.setStatus(
        "current"
    )

pmoailhcClientTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 55, 10, 45)
)
pmoailhcClientTrapCritGoesOff.setObjects(
      *(("EKINOPS-PmOailhc-MIB", "pmoailhcAlmClientFail"),
        ("EKINOPS-PmOailhc-MIB", "pmoailhcAlmClientHwFail"),
        ("EKINOPS-PmOailhc-MIB", "pmoailhctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoailhcClientTrapCritGoesOff.setStatus(
        "current"
    )

pmoailhcPowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 55, 10, 50)
)
pmoailhcPowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-PmOailhc-MIB", "pmoailhcAlmDefFuseB"),
        ("EKINOPS-PmOailhc-MIB", "pmoailhcAlmDefFuseA"),
        ("EKINOPS-PmOailhc-MIB", "pmoailhctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoailhcPowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pmoailhcPowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 55, 10, 51)
)
pmoailhcPowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-PmOailhc-MIB", "pmoailhcAlmDefFuseB"),
        ("EKINOPS-PmOailhc-MIB", "pmoailhcAlmDefFuseA"),
        ("EKINOPS-PmOailhc-MIB", "pmoailhctrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmoailhcPowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-PmOailhc-MIB",
    **{"PmoailhcpreampMode": PmoailhcpreampMode,
       "PmoailhcboosterMode": PmoailhcboosterMode,
       "PmoailhcaprMode": PmoailhcaprMode,
       "PmoailhcPreampGainAdjMode": PmoailhcPreampGainAdjMode,
       "PmoailhcBoosterGainAdjMode": PmoailhcBoosterGainAdjMode,
       "PmoailhcPreampCstGainAdjMode": PmoailhcPreampCstGainAdjMode,
       "PmoailhcBoosterCstGainAdjMode": PmoailhcBoosterCstGainAdjMode,
       "modulepmoailhc": modulepmoailhc,
       "pmoailhcalarms": pmoailhcalarms,
       "pmoailhcAlmOther": pmoailhcAlmOther,
       "pmoailhcAlmOtherNurg": pmoailhcAlmOtherNurg,
       "pmoailhcAlmsynthAlm2": pmoailhcAlmsynthAlm2,
       "pmoailhcAlmConfTableSave": pmoailhcAlmConfTableSave,
       "pmoailhcAlmInvUpload": pmoailhcAlmInvUpload,
       "pmoailhcAlmConfTableLoad": pmoailhcAlmConfTableLoad,
       "pmoailhcAlmfoaWarnings": pmoailhcAlmfoaWarnings,
       "pmoailhcAlmTermpLowWarning": pmoailhcAlmTermpLowWarning,
       "pmoailhcAlmTempHighWarning": pmoailhcAlmTempHighWarning,
       "pmoailhcAlmOtherUrg": pmoailhcAlmOtherUrg,
       "pmoailhcAlmfoaAlarms": pmoailhcAlmfoaAlarms,
       "pmoailhcAlmTermpLowAlarm": pmoailhcAlmTermpLowAlarm,
       "pmoailhcAlmTempHighAlarm": pmoailhcAlmTempHighAlarm,
       "pmoailhcAlmOtherCrit": pmoailhcAlmOtherCrit,
       "pmoailhcAlmsynthAlm0": pmoailhcAlmsynthAlm0,
       "pmoailhcAlmMaintenanceMode": pmoailhcAlmMaintenanceMode,
       "pmoailhcAlmAprOn": pmoailhcAlmAprOn,
       "pmoailhcAlmModGlobFail": pmoailhcAlmModGlobFail,
       "pmoailhcAlmUpEdfaInitNotCompl": pmoailhcAlmUpEdfaInitNotCompl,
       "pmoailhcAlmDwEdfaInitNotCompl": pmoailhcAlmDwEdfaInitNotCompl,
       "pmoailhcAlmExtPump1NotLocked": pmoailhcAlmExtPump1NotLocked,
       "pmoailhcAlmExtPump2NotLocked": pmoailhcAlmExtPump2NotLocked,
       "pmoailhcAlmDefFuseA": pmoailhcAlmDefFuseA,
       "pmoailhcAlmDefFuseB": pmoailhcAlmDefFuseB,
       "pmoailhcAlmClient": pmoailhcAlmClient,
       "pmoailhcAlmClientNurg": pmoailhcAlmClientNurg,
       "pmoailhcAlmclientEdfaWarnings": pmoailhcAlmclientEdfaWarnings,
       "pmoailhcAlmClientGainLowWarning": pmoailhcAlmClientGainLowWarning,
       "pmoailhcAlmClientGainHighWarning": pmoailhcAlmClientGainHighWarning,
       "pmoailhcAlmClientInputPwrLowWarning": pmoailhcAlmClientInputPwrLowWarning,
       "pmoailhcAlmClientInputPwrHighWarning": pmoailhcAlmClientInputPwrHighWarning,
       "pmoailhcAlmClientOutputPwrLowWarning": pmoailhcAlmClientOutputPwrLowWarning,
       "pmoailhcAlmClientOutputPwrHighWarning": pmoailhcAlmClientOutputPwrHighWarning,
       "pmoailhcAlmClientBiasLowWarning": pmoailhcAlmClientBiasLowWarning,
       "pmoailhcAlmClientBiasHighWarning": pmoailhcAlmClientBiasHighWarning,
       "pmoailhcAlmClientUrg": pmoailhcAlmClientUrg,
       "pmoailhcAlmclientEdfaAlarms1": pmoailhcAlmclientEdfaAlarms1,
       "pmoailhcAlmClientGainLowAlarm": pmoailhcAlmClientGainLowAlarm,
       "pmoailhcAlmClientGainHighAlarm": pmoailhcAlmClientGainHighAlarm,
       "pmoailhcAlmClientInputPwrLowAlarm": pmoailhcAlmClientInputPwrLowAlarm,
       "pmoailhcAlmClientInputPwrHighAlarm": pmoailhcAlmClientInputPwrHighAlarm,
       "pmoailhcAlmClientOutputPwrLowAlarm": pmoailhcAlmClientOutputPwrLowAlarm,
       "pmoailhcAlmClientOutputPwrHighAlarm": pmoailhcAlmClientOutputPwrHighAlarm,
       "pmoailhcAlmClientBiasLowAlarm": pmoailhcAlmClientBiasLowAlarm,
       "pmoailhcAlmClientBiasHighAlarm": pmoailhcAlmClientBiasHighAlarm,
       "pmoailhcAlmClientCrit": pmoailhcAlmClientCrit,
       "pmoailhcAlmsynthAlm8": pmoailhcAlmsynthAlm8,
       "pmoailhcAlmClientHwFail": pmoailhcAlmClientHwFail,
       "pmoailhcAlmClientTxOff": pmoailhcAlmClientTxOff,
       "pmoailhcAlmClientDdmWarning": pmoailhcAlmClientDdmWarning,
       "pmoailhcAlmClientDdmAlm": pmoailhcAlmClientDdmAlm,
       "pmoailhcAlmClientFail": pmoailhcAlmClientFail,
       "pmoailhcAlmClientExtPumpFail": pmoailhcAlmClientExtPumpFail,
       "pmoailhcAlmclientEdfaAlarms2": pmoailhcAlmclientEdfaAlarms2,
       "pmoailhcAlmClientEdfaNr": pmoailhcAlmClientEdfaNr,
       "pmoailhcAlmClientEdfaTecFail": pmoailhcAlmClientEdfaTecFail,
       "pmoailhcAlmClientEdfaLaserFail": pmoailhcAlmClientEdfaLaserFail,
       "pmoailhcAlmClientEdfaLos": pmoailhcAlmClientEdfaLos,
       "pmoailhcAlmClientExtPumpEdfaLowCurrent": pmoailhcAlmClientExtPumpEdfaLowCurrent,
       "pmoailhcAlmLine": pmoailhcAlmLine,
       "pmoailhcAlmLineNurg": pmoailhcAlmLineNurg,
       "pmoailhcAlmlineEdfaWarnings": pmoailhcAlmlineEdfaWarnings,
       "pmoailhcAlmLineGainLowWarning": pmoailhcAlmLineGainLowWarning,
       "pmoailhcAlmLineGainHighWarning": pmoailhcAlmLineGainHighWarning,
       "pmoailhcAlmLineInputPwrLowWarning": pmoailhcAlmLineInputPwrLowWarning,
       "pmoailhcAlmLineInputPwrHighWarning": pmoailhcAlmLineInputPwrHighWarning,
       "pmoailhcAlmLineOutputPwrLowWarning": pmoailhcAlmLineOutputPwrLowWarning,
       "pmoailhcAlmLineOutputPwrHighWarning": pmoailhcAlmLineOutputPwrHighWarning,
       "pmoailhcAlmLineBiasLowWarning": pmoailhcAlmLineBiasLowWarning,
       "pmoailhcAlmLineBiasHighWarning": pmoailhcAlmLineBiasHighWarning,
       "pmoailhcAlmLineUrg": pmoailhcAlmLineUrg,
       "pmoailhcAlmlineEdfaAlarms1": pmoailhcAlmlineEdfaAlarms1,
       "pmoailhcAlmLineGainLowAlarm": pmoailhcAlmLineGainLowAlarm,
       "pmoailhcAlmLineGainHighAlarm": pmoailhcAlmLineGainHighAlarm,
       "pmoailhcAlmLineInputPwrLowAlarm": pmoailhcAlmLineInputPwrLowAlarm,
       "pmoailhcAlmLineInputPwrHighAlarm": pmoailhcAlmLineInputPwrHighAlarm,
       "pmoailhcAlmLineOutputPwrLowAlarm": pmoailhcAlmLineOutputPwrLowAlarm,
       "pmoailhcAlmLineOutputPwrHighAlarm": pmoailhcAlmLineOutputPwrHighAlarm,
       "pmoailhcAlmLineBiasLowAlarm": pmoailhcAlmLineBiasLowAlarm,
       "pmoailhcAlmLineBiasHighAlarm": pmoailhcAlmLineBiasHighAlarm,
       "pmoailhcAlmLineCrit": pmoailhcAlmLineCrit,
       "pmoailhcAlmsynthAlm7": pmoailhcAlmsynthAlm7,
       "pmoailhcAlmLineHwFail": pmoailhcAlmLineHwFail,
       "pmoailhcAlmLineTxOff": pmoailhcAlmLineTxOff,
       "pmoailhcAlmLineDdmWarning": pmoailhcAlmLineDdmWarning,
       "pmoailhcAlmLineDdmAlm": pmoailhcAlmLineDdmAlm,
       "pmoailhcAlmLineFail": pmoailhcAlmLineFail,
       "pmoailhcAlmLineExtPumpFail": pmoailhcAlmLineExtPumpFail,
       "pmoailhcAlmlineEdfaAlarms2": pmoailhcAlmlineEdfaAlarms2,
       "pmoailhcAlmLineEdfaNr": pmoailhcAlmLineEdfaNr,
       "pmoailhcAlmLineEdfaTecFail": pmoailhcAlmLineEdfaTecFail,
       "pmoailhcAlmLineEdfaLaserFail": pmoailhcAlmLineEdfaLaserFail,
       "pmoailhcAlmLineEdfaLos": pmoailhcAlmLineEdfaLos,
       "pmoailhcAlmLineExtPumpEdfaLowCurrent": pmoailhcAlmLineExtPumpEdfaLowCurrent,
       "pmoailhcmeasures": pmoailhcmeasures,
       "pmoailhcMesrOther": pmoailhcMesrOther,
       "pmoailhcMesrtempMeas": pmoailhcMesrtempMeas,
       "pmoailhcMesrClient": pmoailhcMesrClient,
       "pmoailhcMesrclientEdfaBiasMeas": pmoailhcMesrclientEdfaBiasMeas,
       "pmoailhcMesrclientEdfaTxpwrMeas": pmoailhcMesrclientEdfaTxpwrMeas,
       "pmoailhcMesrclientEdfaRxpwrMeas": pmoailhcMesrclientEdfaRxpwrMeas,
       "pmoailhcMesrclientEdfaGainMeas": pmoailhcMesrclientEdfaGainMeas,
       "pmoailhcMesrclientCorrectedGain": pmoailhcMesrclientCorrectedGain,
       "pmoailhcMesrLine": pmoailhcMesrLine,
       "pmoailhcMesrlineEdfaBiasMeas": pmoailhcMesrlineEdfaBiasMeas,
       "pmoailhcMesrlineEdfaTxpwrMeas": pmoailhcMesrlineEdfaTxpwrMeas,
       "pmoailhcMesrlineEdfaRxpwrMeas": pmoailhcMesrlineEdfaRxpwrMeas,
       "pmoailhcMesrlineEdfaGainMeas": pmoailhcMesrlineEdfaGainMeas,
       "pmoailhcMesrlineCorrectedGain": pmoailhcMesrlineCorrectedGain,
       "pmoailhccontrolsWrite": pmoailhccontrolsWrite,
       "pmoailhcCtrlOther": pmoailhcCtrlOther,
       "pmoailhcCtrlsynth0": pmoailhcCtrlsynth0,
       "pmoailhcCtrlConfLoad": pmoailhcCtrlConfLoad,
       "pmoailhcCtrlConfFlash": pmoailhcCtrlConfFlash,
       "pmoailhcCtrlConfClear": pmoailhcCtrlConfClear,
       "pmoailhcCtrlswMgnt": pmoailhcCtrlswMgnt,
       "pmoailhcCtrlColdReset": pmoailhcCtrlColdReset,
       "pmoailhcCtrlWarmReset": pmoailhcCtrlWarmReset,
       "pmoailhcCtrlledTest": pmoailhcCtrlledTest,
       "pmoailhcCtrlGreenLed": pmoailhcCtrlGreenLed,
       "pmoailhcCtrlRedLed": pmoailhcCtrlRedLed,
       "pmoailhcCtrlLedOff": pmoailhcCtrlLedOff,
       "pmoailhcCtrlmaintMode": pmoailhcCtrlmaintMode,
       "pmoailhcCtrlMaintenance": pmoailhcCtrlMaintenance,
       "pmoailhcCtrlaprRestart": pmoailhcCtrlaprRestart,
       "pmoailhcCtrlAprManualRestart": pmoailhcCtrlAprManualRestart,
       "pmoailhcCtrlClient": pmoailhcCtrlClient,
       "pmoailhcCtrlclientEdfaLaserOff": pmoailhcCtrlclientEdfaLaserOff,
       "pmoailhcCtrlClientEdfaLaserOff": pmoailhcCtrlClientEdfaLaserOff,
       "pmoailhcCtrlclientGainCstMonitorValue": pmoailhcCtrlclientGainCstMonitorValue,
       "pmoailhcCtrlclientGainCstPoutValue": pmoailhcCtrlclientGainCstPoutValue,
       "pmoailhcCtrlclientGainSettingValue": pmoailhcCtrlclientGainSettingValue,
       "pmoailhcCtrlclientGainProcessing": pmoailhcCtrlclientGainProcessing,
       "pmoailhcCtrlClientGainProc": pmoailhcCtrlClientGainProc,
       "pmoailhcCtrlclientGainCstFiberAgingMarginValue": pmoailhcCtrlclientGainCstFiberAgingMarginValue,
       "pmoailhcCtrlclientGainCstAdddropMarginValue": pmoailhcCtrlclientGainCstAdddropMarginValue,
       "pmoailhcCtrlLine": pmoailhcCtrlLine,
       "pmoailhcCtrllineEdfaLaserOff": pmoailhcCtrllineEdfaLaserOff,
       "pmoailhcCtrlLineEdfaLaserOff": pmoailhcCtrlLineEdfaLaserOff,
       "pmoailhcCtrllineGainCstMonitorValue": pmoailhcCtrllineGainCstMonitorValue,
       "pmoailhcCtrllineGainCstPoutValue": pmoailhcCtrllineGainCstPoutValue,
       "pmoailhcCtrllineGainSettingValue": pmoailhcCtrllineGainSettingValue,
       "pmoailhcCtrllineGainProcessing": pmoailhcCtrllineGainProcessing,
       "pmoailhcCtrlLineGainProc": pmoailhcCtrlLineGainProc,
       "pmoailhcCtrllineGainCstFiberAgingMarginValue": pmoailhcCtrllineGainCstFiberAgingMarginValue,
       "pmoailhcCtrllineGainCstAdddropMarginValue": pmoailhcCtrllineGainCstAdddropMarginValue,
       "pmoailhcri": pmoailhcri,
       "pmoailhcRinvReloadInventory": pmoailhcRinvReloadInventory,
       "pmoailhcRinvModulePlatform": pmoailhcRinvModulePlatform,
       "pmoailhcRinvSwPlatform": pmoailhcRinvSwPlatform,
       "pmoailhcRinvSwFoa": pmoailhcRinvSwFoa,
       "pmoailhcRinvInLine1Table": pmoailhcRinvInLine1Table,
       "pmoailhcRinvInLine1Entry": pmoailhcRinvInLine1Entry,
       "pmoailhcRinvInLine1Index": pmoailhcRinvInLine1Index,
       "pmoailhcRinvInLine1": pmoailhcRinvInLine1,
       "pmoailhcRinvInLine2Table": pmoailhcRinvInLine2Table,
       "pmoailhcRinvInLine2Entry": pmoailhcRinvInLine2Entry,
       "pmoailhcRinvInLine2Index": pmoailhcRinvInLine2Index,
       "pmoailhcRinvInLine2": pmoailhcRinvInLine2,
       "pmoailhcConfig": pmoailhcConfig,
       "pmoailhcCfgNoValue": pmoailhcCfgNoValue,
       "pmoailhctableclientStartup": pmoailhctableclientStartup,
       "pmoailhcCfgclientEdfaLaserCtrl": pmoailhcCfgclientEdfaLaserCtrl,
       "pmoailhcCfgclientEdfaLaserMode": pmoailhcCfgclientEdfaLaserMode,
       "pmoailhcCfgclientGainValue": pmoailhcCfgclientGainValue,
       "pmoailhcCfgclientTiltValue": pmoailhcCfgclientTiltValue,
       "pmoailhcCfgclientMsaLoss": pmoailhcCfgclientMsaLoss,
       "pmoailhcCfgclientOutputPowerValue": pmoailhcCfgclientOutputPowerValue,
       "pmoailhcCfgclientAseCompensation": pmoailhcCfgclientAseCompensation,
       "pmoailhcCfgLineStartUp": pmoailhcCfgLineStartUp,
       "pmoailhctablelineStartup": pmoailhctablelineStartup,
       "pmoailhcCfglineEdfaLaserCtrl": pmoailhcCfglineEdfaLaserCtrl,
       "pmoailhcCfglineEdfaLaserMode": pmoailhcCfglineEdfaLaserMode,
       "pmoailhcCfglineGainValue": pmoailhcCfglineGainValue,
       "pmoailhcCfglineTiltValue": pmoailhcCfglineTiltValue,
       "pmoailhcCfglineMsaLoss": pmoailhcCfglineMsaLoss,
       "pmoailhcCfglineOutputPowerValue": pmoailhcCfglineOutputPowerValue,
       "pmoailhcCfglineAseCompensation": pmoailhcCfglineAseCompensation,
       "pmoailhcCfgaprMode": pmoailhcCfgaprMode,
       "pmoailhcCfgLabels": pmoailhcCfgLabels,
       "pmoailhcCfgLabelclientTable": pmoailhcCfgLabelclientTable,
       "pmoailhcCfgLabelclientEntry": pmoailhcCfgLabelclientEntry,
       "pmoailhcCfgLabelclientIndex": pmoailhcCfgLabelclientIndex,
       "pmoailhcCfgLabelclientPortn": pmoailhcCfgLabelclientPortn,
       "pmoailhcCfgLabellineTable": pmoailhcCfgLabellineTable,
       "pmoailhcCfgLabellineEntry": pmoailhcCfgLabellineEntry,
       "pmoailhcCfgLabellineIndex": pmoailhcCfgLabellineIndex,
       "pmoailhcCfgLabellinePortn": pmoailhcCfgLabellinePortn,
       "pmoailhcCfgWriteConfiguration": pmoailhcCfgWriteConfiguration,
       "pmoailhctraps": pmoailhctraps,
       "pmoailhctrapBoardNumber": pmoailhctrapBoardNumber,
       "pmoailhcLineTrapNotUrgentGoesOn": pmoailhcLineTrapNotUrgentGoesOn,
       "pmoailhcLineTrapNotUrgentGoesOff": pmoailhcLineTrapNotUrgentGoesOff,
       "pmoailhcLineTrapUrgentGoesOn": pmoailhcLineTrapUrgentGoesOn,
       "pmoailhcLineTrapUrgentGoesOff": pmoailhcLineTrapUrgentGoesOff,
       "pmoailhcLineTrapCritGoesOn": pmoailhcLineTrapCritGoesOn,
       "pmoailhcLineTrapCritGoesOff": pmoailhcLineTrapCritGoesOff,
       "pmoailhcClientTrapNotUrgentGoesOn": pmoailhcClientTrapNotUrgentGoesOn,
       "pmoailhcClientTrapNotUrgentGoesOff": pmoailhcClientTrapNotUrgentGoesOff,
       "pmoailhcClientTrapUrgentGoesOn": pmoailhcClientTrapUrgentGoesOn,
       "pmoailhcClientTrapUrgentGoesOff": pmoailhcClientTrapUrgentGoesOff,
       "pmoailhcClientTrapCritGoesOn": pmoailhcClientTrapCritGoesOn,
       "pmoailhcClientTrapCritGoesOff": pmoailhcClientTrapCritGoesOff,
       "pmoailhcPowerTrapUrgentGoesOn": pmoailhcPowerTrapUrgentGoesOn,
       "pmoailhcPowerTrapUrgentGoesOff": pmoailhcPowerTrapUrgentGoesOff}
)
