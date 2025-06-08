# SNMP MIB module (EKINOPS-Pm200fr20-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Pm200fr20-MIB.mib
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

modulePm200fr20 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87)
)
if mibBuilder.loadTexts:
    modulePm200fr20.setRevisions(
        ("2017-05-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Pm200fr20OtxGrid(TextualConvention, Integer32):
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



class Pm200fr20ClientProtocolA(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("protocolclientvalue0A", 1),
          ("protocolclientvalue1A", 2),
          ("protocolclientvalue2A", 3))
    )



class Pm200fr20ClientProtocolB(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("protocolclientvalue0B", 1),
          ("protocolclientvalue1B", 2),
          ("protocolclientvalue2B", 3),
          ("protocolclientvalue3B", 4),
          ("protocolclientvalue4B", 5))
    )



class Pm200fr20ClientProtocolC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("protocolclientvalue0C", 1)
    )



class Pm200fr20ProtocolMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("protocolmodevalue0", 1),
          ("protocolmodevalue1", 2),
          ("protocolmodevalue2", 3))
    )



class Pm200fr20OtxChannel(TextualConvention, Integer32):
    status = "current"


class Pm200fr20OrxChannel(TextualConvention, Integer32):
    status = "current"


class Pm200fr20DccMode(TextualConvention, Integer32):
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
        *(("dccNo", 0),
          ("dccLine1", 1),
          ("dccLine2", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Pm200fr20alarms_ObjectIdentity = ObjectIdentity
pm200fr20alarms = _Pm200fr20alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2)
)
_Pm200fr20AlmOther_ObjectIdentity = ObjectIdentity
pm200fr20AlmOther = _Pm200fr20AlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 1)
)
_Pm200fr20AlmOtherNurg_ObjectIdentity = ObjectIdentity
pm200fr20AlmOtherNurg = _Pm200fr20AlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 1, 1)
)
_Pm200fr20AlmsynthAlm2_ObjectIdentity = ObjectIdentity
pm200fr20AlmsynthAlm2 = _Pm200fr20AlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 1, 1, 2)
)
_Pm200fr20AlmConfTableSave_Type = EkiOnOff
_Pm200fr20AlmConfTableSave_Object = MibScalar
pm200fr20AlmConfTableSave = _Pm200fr20AlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 1, 1, 2, 1),
    _Pm200fr20AlmConfTableSave_Type()
)
pm200fr20AlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmConfTableSave.setStatus("current")
_Pm200fr20AlmInvUpload_Type = EkiOnOff
_Pm200fr20AlmInvUpload_Object = MibScalar
pm200fr20AlmInvUpload = _Pm200fr20AlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 1, 1, 2, 2),
    _Pm200fr20AlmInvUpload_Type()
)
pm200fr20AlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmInvUpload.setStatus("current")
_Pm200fr20AlmConfTableLoad_Type = EkiOnOff
_Pm200fr20AlmConfTableLoad_Object = MibScalar
pm200fr20AlmConfTableLoad = _Pm200fr20AlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 1, 1, 2, 3),
    _Pm200fr20AlmConfTableLoad_Type()
)
pm200fr20AlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmConfTableLoad.setStatus("current")
_Pm200fr20AlmCorrelatOff_Type = EkiOnOff
_Pm200fr20AlmCorrelatOff_Object = MibScalar
pm200fr20AlmCorrelatOff = _Pm200fr20AlmCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 1, 1, 2, 4),
    _Pm200fr20AlmCorrelatOff_Type()
)
pm200fr20AlmCorrelatOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmCorrelatOff.setStatus("current")
_Pm200fr20AlmMaintenanceOn_Type = EkiOnOff
_Pm200fr20AlmMaintenanceOn_Object = MibScalar
pm200fr20AlmMaintenanceOn = _Pm200fr20AlmMaintenanceOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 1, 1, 2, 5),
    _Pm200fr20AlmMaintenanceOn_Type()
)
pm200fr20AlmMaintenanceOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmMaintenanceOn.setStatus("current")
_Pm200fr20AlmOtherUrg_ObjectIdentity = ObjectIdentity
pm200fr20AlmOtherUrg = _Pm200fr20AlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 1, 2)
)
_Pm200fr20AlmmodFanFail_ObjectIdentity = ObjectIdentity
pm200fr20AlmmodFanFail = _Pm200fr20AlmmodFanFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 1, 2, 336)
)
_Pm200fr20AlmFanFail_Type = EkiOnOff
_Pm200fr20AlmFanFail_Object = MibScalar
pm200fr20AlmFanFail = _Pm200fr20AlmFanFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 1, 2, 336, 1),
    _Pm200fr20AlmFanFail_Type()
)
pm200fr20AlmFanFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmFanFail.setStatus("current")
_Pm200fr20AlmFanHighSpeed_Type = EkiOnOff
_Pm200fr20AlmFanHighSpeed_Object = MibScalar
pm200fr20AlmFanHighSpeed = _Pm200fr20AlmFanHighSpeed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 1, 2, 336, 2),
    _Pm200fr20AlmFanHighSpeed_Type()
)
pm200fr20AlmFanHighSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmFanHighSpeed.setStatus("current")
_Pm200fr20AlmOtherCrit_ObjectIdentity = ObjectIdentity
pm200fr20AlmOtherCrit = _Pm200fr20AlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 1, 3)
)
_Pm200fr20AlmsynthAlm0_ObjectIdentity = ObjectIdentity
pm200fr20AlmsynthAlm0 = _Pm200fr20AlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 1, 3, 0)
)
_Pm200fr20AlmFailFan_Type = EkiOnOff
_Pm200fr20AlmFailFan_Object = MibScalar
pm200fr20AlmFailFan = _Pm200fr20AlmFailFan_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 1, 3, 0, 2),
    _Pm200fr20AlmFailFan_Type()
)
pm200fr20AlmFailFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmFailFan.setStatus("current")
_Pm200fr20AlmModGlobFail_Type = EkiOnOff
_Pm200fr20AlmModGlobFail_Object = MibScalar
pm200fr20AlmModGlobFail = _Pm200fr20AlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 1, 3, 0, 9),
    _Pm200fr20AlmModGlobFail_Type()
)
pm200fr20AlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmModGlobFail.setStatus("current")
_Pm200fr20AlmDefFuseA_Type = EkiOnOff
_Pm200fr20AlmDefFuseA_Object = MibScalar
pm200fr20AlmDefFuseA = _Pm200fr20AlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 1, 3, 0, 15),
    _Pm200fr20AlmDefFuseA_Type()
)
pm200fr20AlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmDefFuseA.setStatus("current")
_Pm200fr20AlmDefFuseB_Type = EkiOnOff
_Pm200fr20AlmDefFuseB_Object = MibScalar
pm200fr20AlmDefFuseB = _Pm200fr20AlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 1, 3, 0, 16),
    _Pm200fr20AlmDefFuseB_Type()
)
pm200fr20AlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmDefFuseB.setStatus("current")
_Pm200fr20AlmmsaModuleState_ObjectIdentity = ObjectIdentity
pm200fr20AlmmsaModuleState = _Pm200fr20AlmmsaModuleState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 1, 3, 78)
)
_Pm200fr20AlmMsaReady_Type = EkiOnOff
_Pm200fr20AlmMsaReady_Object = MibScalar
pm200fr20AlmMsaReady = _Pm200fr20AlmMsaReady_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 1, 3, 78, 6),
    _Pm200fr20AlmMsaReady_Type()
)
pm200fr20AlmMsaReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmMsaReady.setStatus("current")
_Pm200fr20AlmMsaFault_Type = EkiOnOff
_Pm200fr20AlmMsaFault_Object = MibScalar
pm200fr20AlmMsaFault = _Pm200fr20AlmMsaFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 1, 3, 78, 7),
    _Pm200fr20AlmMsaFault_Type()
)
pm200fr20AlmMsaFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmMsaFault.setStatus("current")
_Pm200fr20AlmClient_ObjectIdentity = ObjectIdentity
pm200fr20AlmClient = _Pm200fr20AlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2)
)
_Pm200fr20AlmClientNurg_ObjectIdentity = ObjectIdentity
pm200fr20AlmClientNurg = _Pm200fr20AlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 1)
)
_Pm200fr20AlmclientSfpWarnDdmTable_Object = MibTable
pm200fr20AlmclientSfpWarnDdmTable = _Pm200fr20AlmclientSfpWarnDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 1, 272)
)
if mibBuilder.loadTexts:
    pm200fr20AlmclientSfpWarnDdmTable.setStatus("current")
_Pm200fr20AlmclientSfpWarnDdmEntry_Object = MibTableRow
pm200fr20AlmclientSfpWarnDdmEntry = _Pm200fr20AlmclientSfpWarnDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 1, 272, 1)
)
pm200fr20AlmclientSfpWarnDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20AlmclientSfpWarnDdmIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20AlmclientSfpWarnDdmEntry.setStatus("current")


class _Pm200fr20AlmclientSfpWarnDdmIndex_Type(Integer32):
    """Custom type pm200fr20AlmclientSfpWarnDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20AlmclientSfpWarnDdmIndex_Type.__name__ = "Integer32"
_Pm200fr20AlmclientSfpWarnDdmIndex_Object = MibTableColumn
pm200fr20AlmclientSfpWarnDdmIndex = _Pm200fr20AlmclientSfpWarnDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 1, 272, 1, 1),
    _Pm200fr20AlmclientSfpWarnDdmIndex_Type()
)
pm200fr20AlmclientSfpWarnDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmclientSfpWarnDdmIndex.setStatus("current")
_Pm200fr20AlmTxPwLowWngPortn_Type = EkiOnOff
_Pm200fr20AlmTxPwLowWngPortn_Object = MibTableColumn
pm200fr20AlmTxPwLowWngPortn = _Pm200fr20AlmTxPwLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 1, 272, 1, 2),
    _Pm200fr20AlmTxPwLowWngPortn_Type()
)
pm200fr20AlmTxPwLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmTxPwLowWngPortn.setStatus("current")
_Pm200fr20AlmTxPwrHighWngPortn_Type = EkiOnOff
_Pm200fr20AlmTxPwrHighWngPortn_Object = MibTableColumn
pm200fr20AlmTxPwrHighWngPortn = _Pm200fr20AlmTxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 1, 272, 1, 3),
    _Pm200fr20AlmTxPwrHighWngPortn_Type()
)
pm200fr20AlmTxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmTxPwrHighWngPortn.setStatus("current")
_Pm200fr20AlmTxBiasLowWngPortn_Type = EkiOnOff
_Pm200fr20AlmTxBiasLowWngPortn_Object = MibTableColumn
pm200fr20AlmTxBiasLowWngPortn = _Pm200fr20AlmTxBiasLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 1, 272, 1, 4),
    _Pm200fr20AlmTxBiasLowWngPortn_Type()
)
pm200fr20AlmTxBiasLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmTxBiasLowWngPortn.setStatus("current")
_Pm200fr20AlmTxBiasHighWngPortn_Type = EkiOnOff
_Pm200fr20AlmTxBiasHighWngPortn_Object = MibTableColumn
pm200fr20AlmTxBiasHighWngPortn = _Pm200fr20AlmTxBiasHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 1, 272, 1, 5),
    _Pm200fr20AlmTxBiasHighWngPortn_Type()
)
pm200fr20AlmTxBiasHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmTxBiasHighWngPortn.setStatus("current")
_Pm200fr20AlmVccLowWngPortn_Type = EkiOnOff
_Pm200fr20AlmVccLowWngPortn_Object = MibTableColumn
pm200fr20AlmVccLowWngPortn = _Pm200fr20AlmVccLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 1, 272, 1, 6),
    _Pm200fr20AlmVccLowWngPortn_Type()
)
pm200fr20AlmVccLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmVccLowWngPortn.setStatus("current")
_Pm200fr20AlmVccHighWngPortn_Type = EkiOnOff
_Pm200fr20AlmVccHighWngPortn_Object = MibTableColumn
pm200fr20AlmVccHighWngPortn = _Pm200fr20AlmVccHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 1, 272, 1, 7),
    _Pm200fr20AlmVccHighWngPortn_Type()
)
pm200fr20AlmVccHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmVccHighWngPortn.setStatus("current")
_Pm200fr20AlmTempLowWngPortn_Type = EkiOnOff
_Pm200fr20AlmTempLowWngPortn_Object = MibTableColumn
pm200fr20AlmTempLowWngPortn = _Pm200fr20AlmTempLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 1, 272, 1, 8),
    _Pm200fr20AlmTempLowWngPortn_Type()
)
pm200fr20AlmTempLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmTempLowWngPortn.setStatus("current")
_Pm200fr20AlmTempHighWngPortn_Type = EkiOnOff
_Pm200fr20AlmTempHighWngPortn_Object = MibTableColumn
pm200fr20AlmTempHighWngPortn = _Pm200fr20AlmTempHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 1, 272, 1, 9),
    _Pm200fr20AlmTempHighWngPortn_Type()
)
pm200fr20AlmTempHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmTempHighWngPortn.setStatus("current")
_Pm200fr20AlmRxPwrLowWngPortn_Type = EkiOnOff
_Pm200fr20AlmRxPwrLowWngPortn_Object = MibTableColumn
pm200fr20AlmRxPwrLowWngPortn = _Pm200fr20AlmRxPwrLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 1, 272, 1, 16),
    _Pm200fr20AlmRxPwrLowWngPortn_Type()
)
pm200fr20AlmRxPwrLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmRxPwrLowWngPortn.setStatus("current")
_Pm200fr20AlmRxPwrHighWngPortn_Type = EkiOnOff
_Pm200fr20AlmRxPwrHighWngPortn_Object = MibTableColumn
pm200fr20AlmRxPwrHighWngPortn = _Pm200fr20AlmRxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 1, 272, 1, 17),
    _Pm200fr20AlmRxPwrHighWngPortn_Type()
)
pm200fr20AlmRxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmRxPwrHighWngPortn.setStatus("current")
_Pm200fr20AlmClientUrg_ObjectIdentity = ObjectIdentity
pm200fr20AlmClientUrg = _Pm200fr20AlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 2)
)
_Pm200fr20AlmclientHostLaneFaultTable_Object = MibTable
pm200fr20AlmclientHostLaneFaultTable = _Pm200fr20AlmclientHostLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 2, 152)
)
if mibBuilder.loadTexts:
    pm200fr20AlmclientHostLaneFaultTable.setStatus("current")
_Pm200fr20AlmclientHostLaneFaultEntry_Object = MibTableRow
pm200fr20AlmclientHostLaneFaultEntry = _Pm200fr20AlmclientHostLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 2, 152, 1)
)
pm200fr20AlmclientHostLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20AlmclientHostLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20AlmclientHostLaneFaultEntry.setStatus("current")


class _Pm200fr20AlmclientHostLaneFaultIndex_Type(Integer32):
    """Custom type pm200fr20AlmclientHostLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20AlmclientHostLaneFaultIndex_Type.__name__ = "Integer32"
_Pm200fr20AlmclientHostLaneFaultIndex_Object = MibTableColumn
pm200fr20AlmclientHostLaneFaultIndex = _Pm200fr20AlmclientHostLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 2, 152, 1, 1),
    _Pm200fr20AlmclientHostLaneFaultIndex_Type()
)
pm200fr20AlmclientHostLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmclientHostLaneFaultIndex.setStatus("current")
_Pm200fr20AlmClientLossOfSyncPortn_Type = EkiOnOff
_Pm200fr20AlmClientLossOfSyncPortn_Object = MibTableColumn
pm200fr20AlmClientLossOfSyncPortn = _Pm200fr20AlmClientLossOfSyncPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 2, 152, 1, 2),
    _Pm200fr20AlmClientLossOfSyncPortn_Type()
)
pm200fr20AlmClientLossOfSyncPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmClientLossOfSyncPortn.setStatus("current")
_Pm200fr20AlmClientInputLossOfSigPortn_Type = EkiOnOff
_Pm200fr20AlmClientInputLossOfSigPortn_Object = MibTableColumn
pm200fr20AlmClientInputLossOfSigPortn = _Pm200fr20AlmClientInputLossOfSigPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 2, 152, 1, 3),
    _Pm200fr20AlmClientInputLossOfSigPortn_Type()
)
pm200fr20AlmClientInputLossOfSigPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmClientInputLossOfSigPortn.setStatus("current")
_Pm200fr20AlmClientLanesMarkerUnlockPortn_Type = EkiOnOff
_Pm200fr20AlmClientLanesMarkerUnlockPortn_Object = MibTableColumn
pm200fr20AlmClientLanesMarkerUnlockPortn = _Pm200fr20AlmClientLanesMarkerUnlockPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 2, 152, 1, 4),
    _Pm200fr20AlmClientLanesMarkerUnlockPortn_Type()
)
pm200fr20AlmClientLanesMarkerUnlockPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmClientLanesMarkerUnlockPortn.setStatus("current")
_Pm200fr20AlmClientLanes6466UnlockPortn_Type = EkiOnOff
_Pm200fr20AlmClientLanes6466UnlockPortn_Object = MibTableColumn
pm200fr20AlmClientLanes6466UnlockPortn = _Pm200fr20AlmClientLanes6466UnlockPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 2, 152, 1, 5),
    _Pm200fr20AlmClientLanes6466UnlockPortn_Type()
)
pm200fr20AlmClientLanes6466UnlockPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmClientLanes6466UnlockPortn.setStatus("current")
_Pm200fr20AlmClientLanesNotAlignedPortn_Type = EkiOnOff
_Pm200fr20AlmClientLanesNotAlignedPortn_Object = MibTableColumn
pm200fr20AlmClientLanesNotAlignedPortn = _Pm200fr20AlmClientLanesNotAlignedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 2, 152, 1, 6),
    _Pm200fr20AlmClientLanesNotAlignedPortn_Type()
)
pm200fr20AlmClientLanesNotAlignedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmClientLanesNotAlignedPortn.setStatus("current")
_Pm200fr20AlmClientCsfDetectedPortn_Type = EkiOnOff
_Pm200fr20AlmClientCsfDetectedPortn_Object = MibTableColumn
pm200fr20AlmClientCsfDetectedPortn = _Pm200fr20AlmClientCsfDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 2, 152, 1, 7),
    _Pm200fr20AlmClientCsfDetectedPortn_Type()
)
pm200fr20AlmClientCsfDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmClientCsfDetectedPortn.setStatus("current")
_Pm200fr20AlmClientTxHostLolPortn_Type = EkiOnOff
_Pm200fr20AlmClientTxHostLolPortn_Object = MibTableColumn
pm200fr20AlmClientTxHostLolPortn = _Pm200fr20AlmClientTxHostLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 2, 152, 1, 10),
    _Pm200fr20AlmClientTxHostLolPortn_Type()
)
pm200fr20AlmClientTxHostLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmClientTxHostLolPortn.setStatus("current")
_Pm200fr20AlmClientLaneTxFifoErrorPortn_Type = EkiOnOff
_Pm200fr20AlmClientLaneTxFifoErrorPortn_Object = MibTableColumn
pm200fr20AlmClientLaneTxFifoErrorPortn = _Pm200fr20AlmClientLaneTxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 2, 152, 1, 11),
    _Pm200fr20AlmClientLaneTxFifoErrorPortn_Type()
)
pm200fr20AlmClientLaneTxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmClientLaneTxFifoErrorPortn.setStatus("current")
_Pm200fr20AlmLfDetectedPortn_Type = EkiOnOff
_Pm200fr20AlmLfDetectedPortn_Object = MibTableColumn
pm200fr20AlmLfDetectedPortn = _Pm200fr20AlmLfDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 2, 152, 1, 12),
    _Pm200fr20AlmLfDetectedPortn_Type()
)
pm200fr20AlmLfDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmLfDetectedPortn.setStatus("current")
_Pm200fr20AlmRfDetectedPortn_Type = EkiOnOff
_Pm200fr20AlmRfDetectedPortn_Object = MibTableColumn
pm200fr20AlmRfDetectedPortn = _Pm200fr20AlmRfDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 2, 152, 1, 13),
    _Pm200fr20AlmRfDetectedPortn_Type()
)
pm200fr20AlmRfDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmRfDetectedPortn.setStatus("current")
_Pm200fr20AlmStm64ProtocDetectedPortn_Type = EkiOnOff
_Pm200fr20AlmStm64ProtocDetectedPortn_Object = MibTableColumn
pm200fr20AlmStm64ProtocDetectedPortn = _Pm200fr20AlmStm64ProtocDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 2, 152, 1, 14),
    _Pm200fr20AlmStm64ProtocDetectedPortn_Type()
)
pm200fr20AlmStm64ProtocDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmStm64ProtocDetectedPortn.setStatus("current")
_Pm200fr20Alm10gbeProtocDetectedPortn_Type = EkiOnOff
_Pm200fr20Alm10gbeProtocDetectedPortn_Object = MibTableColumn
pm200fr20Alm10gbeProtocDetectedPortn = _Pm200fr20Alm10gbeProtocDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 2, 152, 1, 15),
    _Pm200fr20Alm10gbeProtocDetectedPortn_Type()
)
pm200fr20Alm10gbeProtocDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20Alm10gbeProtocDetectedPortn.setStatus("current")
_Pm200fr20AlmOtu2ProtocDetectedPortn_Type = EkiOnOff
_Pm200fr20AlmOtu2ProtocDetectedPortn_Object = MibTableColumn
pm200fr20AlmOtu2ProtocDetectedPortn = _Pm200fr20AlmOtu2ProtocDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 2, 152, 1, 16),
    _Pm200fr20AlmOtu2ProtocDetectedPortn_Type()
)
pm200fr20AlmOtu2ProtocDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmOtu2ProtocDetectedPortn.setStatus("current")
_Pm200fr20AlmOtu2eProtocDetectedPortn_Type = EkiOnOff
_Pm200fr20AlmOtu2eProtocDetectedPortn_Object = MibTableColumn
pm200fr20AlmOtu2eProtocDetectedPortn = _Pm200fr20AlmOtu2eProtocDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 2, 152, 1, 17),
    _Pm200fr20AlmOtu2eProtocDetectedPortn_Type()
)
pm200fr20AlmOtu2eProtocDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmOtu2eProtocDetectedPortn.setStatus("current")
_Pm200fr20AlmclientSfpAlmDdmTable_Object = MibTable
pm200fr20AlmclientSfpAlmDdmTable = _Pm200fr20AlmclientSfpAlmDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 2, 240)
)
if mibBuilder.loadTexts:
    pm200fr20AlmclientSfpAlmDdmTable.setStatus("current")
_Pm200fr20AlmclientSfpAlmDdmEntry_Object = MibTableRow
pm200fr20AlmclientSfpAlmDdmEntry = _Pm200fr20AlmclientSfpAlmDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 2, 240, 1)
)
pm200fr20AlmclientSfpAlmDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20AlmclientSfpAlmDdmIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20AlmclientSfpAlmDdmEntry.setStatus("current")


class _Pm200fr20AlmclientSfpAlmDdmIndex_Type(Integer32):
    """Custom type pm200fr20AlmclientSfpAlmDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20AlmclientSfpAlmDdmIndex_Type.__name__ = "Integer32"
_Pm200fr20AlmclientSfpAlmDdmIndex_Object = MibTableColumn
pm200fr20AlmclientSfpAlmDdmIndex = _Pm200fr20AlmclientSfpAlmDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 2, 240, 1, 1),
    _Pm200fr20AlmclientSfpAlmDdmIndex_Type()
)
pm200fr20AlmclientSfpAlmDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmclientSfpAlmDdmIndex.setStatus("current")
_Pm200fr20AlmTxPwrLowAlaPortn_Type = EkiOnOff
_Pm200fr20AlmTxPwrLowAlaPortn_Object = MibTableColumn
pm200fr20AlmTxPwrLowAlaPortn = _Pm200fr20AlmTxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 2, 240, 1, 2),
    _Pm200fr20AlmTxPwrLowAlaPortn_Type()
)
pm200fr20AlmTxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmTxPwrLowAlaPortn.setStatus("current")
_Pm200fr20AlmTxPwrHighAlaPortn_Type = EkiOnOff
_Pm200fr20AlmTxPwrHighAlaPortn_Object = MibTableColumn
pm200fr20AlmTxPwrHighAlaPortn = _Pm200fr20AlmTxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 2, 240, 1, 3),
    _Pm200fr20AlmTxPwrHighAlaPortn_Type()
)
pm200fr20AlmTxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmTxPwrHighAlaPortn.setStatus("current")
_Pm200fr20AlmTxBiasLowAlaPortn_Type = EkiOnOff
_Pm200fr20AlmTxBiasLowAlaPortn_Object = MibTableColumn
pm200fr20AlmTxBiasLowAlaPortn = _Pm200fr20AlmTxBiasLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 2, 240, 1, 4),
    _Pm200fr20AlmTxBiasLowAlaPortn_Type()
)
pm200fr20AlmTxBiasLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmTxBiasLowAlaPortn.setStatus("current")
_Pm200fr20AlmTxBiasHighAlaPortn_Type = EkiOnOff
_Pm200fr20AlmTxBiasHighAlaPortn_Object = MibTableColumn
pm200fr20AlmTxBiasHighAlaPortn = _Pm200fr20AlmTxBiasHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 2, 240, 1, 5),
    _Pm200fr20AlmTxBiasHighAlaPortn_Type()
)
pm200fr20AlmTxBiasHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmTxBiasHighAlaPortn.setStatus("current")
_Pm200fr20AlmVccLowAlaPortn_Type = EkiOnOff
_Pm200fr20AlmVccLowAlaPortn_Object = MibTableColumn
pm200fr20AlmVccLowAlaPortn = _Pm200fr20AlmVccLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 2, 240, 1, 6),
    _Pm200fr20AlmVccLowAlaPortn_Type()
)
pm200fr20AlmVccLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmVccLowAlaPortn.setStatus("current")
_Pm200fr20AlmVccHighAlaPortn_Type = EkiOnOff
_Pm200fr20AlmVccHighAlaPortn_Object = MibTableColumn
pm200fr20AlmVccHighAlaPortn = _Pm200fr20AlmVccHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 2, 240, 1, 7),
    _Pm200fr20AlmVccHighAlaPortn_Type()
)
pm200fr20AlmVccHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmVccHighAlaPortn.setStatus("current")
_Pm200fr20AlmTempLowAlaPortn_Type = EkiOnOff
_Pm200fr20AlmTempLowAlaPortn_Object = MibTableColumn
pm200fr20AlmTempLowAlaPortn = _Pm200fr20AlmTempLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 2, 240, 1, 8),
    _Pm200fr20AlmTempLowAlaPortn_Type()
)
pm200fr20AlmTempLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmTempLowAlaPortn.setStatus("current")
_Pm200fr20AlmTempHighAlaPortn_Type = EkiOnOff
_Pm200fr20AlmTempHighAlaPortn_Object = MibTableColumn
pm200fr20AlmTempHighAlaPortn = _Pm200fr20AlmTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 2, 240, 1, 9),
    _Pm200fr20AlmTempHighAlaPortn_Type()
)
pm200fr20AlmTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmTempHighAlaPortn.setStatus("current")
_Pm200fr20AlmRxPwrLowAlaPortn_Type = EkiOnOff
_Pm200fr20AlmRxPwrLowAlaPortn_Object = MibTableColumn
pm200fr20AlmRxPwrLowAlaPortn = _Pm200fr20AlmRxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 2, 240, 1, 16),
    _Pm200fr20AlmRxPwrLowAlaPortn_Type()
)
pm200fr20AlmRxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmRxPwrLowAlaPortn.setStatus("current")
_Pm200fr20AlmRxPwrHighAlaPortn_Type = EkiOnOff
_Pm200fr20AlmRxPwrHighAlaPortn_Object = MibTableColumn
pm200fr20AlmRxPwrHighAlaPortn = _Pm200fr20AlmRxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 2, 240, 1, 17),
    _Pm200fr20AlmRxPwrHighAlaPortn_Type()
)
pm200fr20AlmRxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmRxPwrHighAlaPortn.setStatus("current")
_Pm200fr20AlmclientOtnAlmTable_Object = MibTable
pm200fr20AlmclientOtnAlmTable = _Pm200fr20AlmclientOtnAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 2, 304)
)
if mibBuilder.loadTexts:
    pm200fr20AlmclientOtnAlmTable.setStatus("current")
_Pm200fr20AlmclientOtnAlmEntry_Object = MibTableRow
pm200fr20AlmclientOtnAlmEntry = _Pm200fr20AlmclientOtnAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 2, 304, 1)
)
pm200fr20AlmclientOtnAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20AlmclientOtnAlmIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20AlmclientOtnAlmEntry.setStatus("current")


class _Pm200fr20AlmclientOtnAlmIndex_Type(Integer32):
    """Custom type pm200fr20AlmclientOtnAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20AlmclientOtnAlmIndex_Type.__name__ = "Integer32"
_Pm200fr20AlmclientOtnAlmIndex_Object = MibTableColumn
pm200fr20AlmclientOtnAlmIndex = _Pm200fr20AlmclientOtnAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 2, 304, 1, 1),
    _Pm200fr20AlmclientOtnAlmIndex_Type()
)
pm200fr20AlmclientOtnAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmclientOtnAlmIndex.setStatus("current")
_Pm200fr20AlmClientOtu2eDlomPortn_Type = EkiOnOff
_Pm200fr20AlmClientOtu2eDlomPortn_Object = MibTableColumn
pm200fr20AlmClientOtu2eDlomPortn = _Pm200fr20AlmClientOtu2eDlomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 2, 304, 1, 2),
    _Pm200fr20AlmClientOtu2eDlomPortn_Type()
)
pm200fr20AlmClientOtu2eDlomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmClientOtu2eDlomPortn.setStatus("current")
_Pm200fr20AlmClientCrit_ObjectIdentity = ObjectIdentity
pm200fr20AlmClientCrit = _Pm200fr20AlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 3)
)
_Pm200fr20AlmsynthAlmPortTable_Object = MibTable
pm200fr20AlmsynthAlmPortTable = _Pm200fr20AlmsynthAlmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    pm200fr20AlmsynthAlmPortTable.setStatus("current")
_Pm200fr20AlmsynthAlmPortEntry_Object = MibTableRow
pm200fr20AlmsynthAlmPortEntry = _Pm200fr20AlmsynthAlmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 3, 8, 1)
)
pm200fr20AlmsynthAlmPortEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20AlmsynthAlmPortIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20AlmsynthAlmPortEntry.setStatus("current")


class _Pm200fr20AlmsynthAlmPortIndex_Type(Integer32):
    """Custom type pm200fr20AlmsynthAlmPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20AlmsynthAlmPortIndex_Type.__name__ = "Integer32"
_Pm200fr20AlmsynthAlmPortIndex_Object = MibTableColumn
pm200fr20AlmsynthAlmPortIndex = _Pm200fr20AlmsynthAlmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 3, 8, 1, 1),
    _Pm200fr20AlmsynthAlmPortIndex_Type()
)
pm200fr20AlmsynthAlmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmsynthAlmPortIndex.setStatus("current")
_Pm200fr20AlmSfpAbsentPortn_Type = EkiOnOff
_Pm200fr20AlmSfpAbsentPortn_Object = MibTableColumn
pm200fr20AlmSfpAbsentPortn = _Pm200fr20AlmSfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 3, 8, 1, 2),
    _Pm200fr20AlmSfpAbsentPortn_Type()
)
pm200fr20AlmSfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmSfpAbsentPortn.setStatus("current")
_Pm200fr20AlmDdmAbsentPortn_Type = EkiOnOff
_Pm200fr20AlmDdmAbsentPortn_Object = MibTableColumn
pm200fr20AlmDdmAbsentPortn = _Pm200fr20AlmDdmAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 3, 8, 1, 3),
    _Pm200fr20AlmDdmAbsentPortn_Type()
)
pm200fr20AlmDdmAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmDdmAbsentPortn.setStatus("current")
_Pm200fr20AlmHwFailAccPortn_Type = EkiOnOff
_Pm200fr20AlmHwFailAccPortn_Object = MibTableColumn
pm200fr20AlmHwFailAccPortn = _Pm200fr20AlmHwFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 3, 8, 1, 5),
    _Pm200fr20AlmHwFailAccPortn_Type()
)
pm200fr20AlmHwFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmHwFailAccPortn.setStatus("current")
_Pm200fr20AlmDwLsdPortn_Type = EkiOnOff
_Pm200fr20AlmDwLsdPortn_Object = MibTableColumn
pm200fr20AlmDwLsdPortn = _Pm200fr20AlmDwLsdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 3, 8, 1, 6),
    _Pm200fr20AlmDwLsdPortn_Type()
)
pm200fr20AlmDwLsdPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmDwLsdPortn.setStatus("current")
_Pm200fr20AlmClientLocalOosPortn_Type = EkiOnOff
_Pm200fr20AlmClientLocalOosPortn_Object = MibTableColumn
pm200fr20AlmClientLocalOosPortn = _Pm200fr20AlmClientLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 3, 8, 1, 7),
    _Pm200fr20AlmClientLocalOosPortn_Type()
)
pm200fr20AlmClientLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmClientLocalOosPortn.setStatus("current")
_Pm200fr20AlmClientRemoteOosPortn_Type = EkiOnOff
_Pm200fr20AlmClientRemoteOosPortn_Object = MibTableColumn
pm200fr20AlmClientRemoteOosPortn = _Pm200fr20AlmClientRemoteOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 3, 8, 1, 8),
    _Pm200fr20AlmClientRemoteOosPortn_Type()
)
pm200fr20AlmClientRemoteOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmClientRemoteOosPortn.setStatus("current")
_Pm200fr20AlmDwCaisPortn_Type = EkiOnOff
_Pm200fr20AlmDwCaisPortn_Object = MibTableColumn
pm200fr20AlmDwCaisPortn = _Pm200fr20AlmDwCaisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 3, 8, 1, 9),
    _Pm200fr20AlmDwCaisPortn_Type()
)
pm200fr20AlmDwCaisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmDwCaisPortn.setStatus("current")
_Pm200fr20AlmSfpDdmWarningPortn_Type = EkiOnOff
_Pm200fr20AlmSfpDdmWarningPortn_Object = MibTableColumn
pm200fr20AlmSfpDdmWarningPortn = _Pm200fr20AlmSfpDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 3, 8, 1, 10),
    _Pm200fr20AlmSfpDdmWarningPortn_Type()
)
pm200fr20AlmSfpDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmSfpDdmWarningPortn.setStatus("current")
_Pm200fr20AlmSfpDdmAlmPortn_Type = EkiOnOff
_Pm200fr20AlmSfpDdmAlmPortn_Object = MibTableColumn
pm200fr20AlmSfpDdmAlmPortn = _Pm200fr20AlmSfpDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 3, 8, 1, 11),
    _Pm200fr20AlmSfpDdmAlmPortn_Type()
)
pm200fr20AlmSfpDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmSfpDdmAlmPortn.setStatus("current")
_Pm200fr20AlmFailAccPortn_Type = EkiOnOff
_Pm200fr20AlmFailAccPortn_Object = MibTableColumn
pm200fr20AlmFailAccPortn = _Pm200fr20AlmFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 3, 8, 1, 13),
    _Pm200fr20AlmFailAccPortn_Type()
)
pm200fr20AlmFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmFailAccPortn.setStatus("current")
_Pm200fr20AlmUpCsfPortn_Type = EkiOnOff
_Pm200fr20AlmUpCsfPortn_Object = MibTableColumn
pm200fr20AlmUpCsfPortn = _Pm200fr20AlmUpCsfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 2, 3, 8, 1, 17),
    _Pm200fr20AlmUpCsfPortn_Type()
)
pm200fr20AlmUpCsfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmUpCsfPortn.setStatus("current")
_Pm200fr20AlmLine_ObjectIdentity = ObjectIdentity
pm200fr20AlmLine = _Pm200fr20AlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3)
)
_Pm200fr20AlmLineNurg_ObjectIdentity = ObjectIdentity
pm200fr20AlmLineNurg = _Pm200fr20AlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 1)
)
_Pm200fr20AlmlineQsfpWarnDdmTable_Object = MibTable
pm200fr20AlmlineQsfpWarnDdmTable = _Pm200fr20AlmlineQsfpWarnDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 1, 104)
)
if mibBuilder.loadTexts:
    pm200fr20AlmlineQsfpWarnDdmTable.setStatus("current")
_Pm200fr20AlmlineQsfpWarnDdmEntry_Object = MibTableRow
pm200fr20AlmlineQsfpWarnDdmEntry = _Pm200fr20AlmlineQsfpWarnDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 1, 104, 1)
)
pm200fr20AlmlineQsfpWarnDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20AlmlineQsfpWarnDdmIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20AlmlineQsfpWarnDdmEntry.setStatus("current")


class _Pm200fr20AlmlineQsfpWarnDdmIndex_Type(Integer32):
    """Custom type pm200fr20AlmlineQsfpWarnDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20AlmlineQsfpWarnDdmIndex_Type.__name__ = "Integer32"
_Pm200fr20AlmlineQsfpWarnDdmIndex_Object = MibTableColumn
pm200fr20AlmlineQsfpWarnDdmIndex = _Pm200fr20AlmlineQsfpWarnDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 1, 104, 1, 1),
    _Pm200fr20AlmlineQsfpWarnDdmIndex_Type()
)
pm200fr20AlmlineQsfpWarnDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmlineQsfpWarnDdmIndex.setStatus("current")
_Pm200fr20AlmLineTxPwLowWngPortn_Type = EkiOnOff
_Pm200fr20AlmLineTxPwLowWngPortn_Object = MibTableColumn
pm200fr20AlmLineTxPwLowWngPortn = _Pm200fr20AlmLineTxPwLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 1, 104, 1, 2),
    _Pm200fr20AlmLineTxPwLowWngPortn_Type()
)
pm200fr20AlmLineTxPwLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmLineTxPwLowWngPortn.setStatus("current")
_Pm200fr20AlmLineTxPwrHighWngPortn_Type = EkiOnOff
_Pm200fr20AlmLineTxPwrHighWngPortn_Object = MibTableColumn
pm200fr20AlmLineTxPwrHighWngPortn = _Pm200fr20AlmLineTxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 1, 104, 1, 3),
    _Pm200fr20AlmLineTxPwrHighWngPortn_Type()
)
pm200fr20AlmLineTxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmLineTxPwrHighWngPortn.setStatus("current")
_Pm200fr20AlmLineTxBiasLowWngPortn_Type = EkiOnOff
_Pm200fr20AlmLineTxBiasLowWngPortn_Object = MibTableColumn
pm200fr20AlmLineTxBiasLowWngPortn = _Pm200fr20AlmLineTxBiasLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 1, 104, 1, 4),
    _Pm200fr20AlmLineTxBiasLowWngPortn_Type()
)
pm200fr20AlmLineTxBiasLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmLineTxBiasLowWngPortn.setStatus("current")
_Pm200fr20AlmLineTxBiasHighWngPortn_Type = EkiOnOff
_Pm200fr20AlmLineTxBiasHighWngPortn_Object = MibTableColumn
pm200fr20AlmLineTxBiasHighWngPortn = _Pm200fr20AlmLineTxBiasHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 1, 104, 1, 5),
    _Pm200fr20AlmLineTxBiasHighWngPortn_Type()
)
pm200fr20AlmLineTxBiasHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmLineTxBiasHighWngPortn.setStatus("current")
_Pm200fr20AlmLineVccLowWngPortn_Type = EkiOnOff
_Pm200fr20AlmLineVccLowWngPortn_Object = MibTableColumn
pm200fr20AlmLineVccLowWngPortn = _Pm200fr20AlmLineVccLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 1, 104, 1, 6),
    _Pm200fr20AlmLineVccLowWngPortn_Type()
)
pm200fr20AlmLineVccLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmLineVccLowWngPortn.setStatus("current")
_Pm200fr20AlmLineVccHighWngPortn_Type = EkiOnOff
_Pm200fr20AlmLineVccHighWngPortn_Object = MibTableColumn
pm200fr20AlmLineVccHighWngPortn = _Pm200fr20AlmLineVccHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 1, 104, 1, 7),
    _Pm200fr20AlmLineVccHighWngPortn_Type()
)
pm200fr20AlmLineVccHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmLineVccHighWngPortn.setStatus("current")
_Pm200fr20AlmLineTempLowWngPortn_Type = EkiOnOff
_Pm200fr20AlmLineTempLowWngPortn_Object = MibTableColumn
pm200fr20AlmLineTempLowWngPortn = _Pm200fr20AlmLineTempLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 1, 104, 1, 8),
    _Pm200fr20AlmLineTempLowWngPortn_Type()
)
pm200fr20AlmLineTempLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmLineTempLowWngPortn.setStatus("current")
_Pm200fr20AlmLineTempHighWngPortn_Type = EkiOnOff
_Pm200fr20AlmLineTempHighWngPortn_Object = MibTableColumn
pm200fr20AlmLineTempHighWngPortn = _Pm200fr20AlmLineTempHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 1, 104, 1, 9),
    _Pm200fr20AlmLineTempHighWngPortn_Type()
)
pm200fr20AlmLineTempHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmLineTempHighWngPortn.setStatus("current")
_Pm200fr20AlmLineRxPwrLowWngPortn_Type = EkiOnOff
_Pm200fr20AlmLineRxPwrLowWngPortn_Object = MibTableColumn
pm200fr20AlmLineRxPwrLowWngPortn = _Pm200fr20AlmLineRxPwrLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 1, 104, 1, 16),
    _Pm200fr20AlmLineRxPwrLowWngPortn_Type()
)
pm200fr20AlmLineRxPwrLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmLineRxPwrLowWngPortn.setStatus("current")
_Pm200fr20AlmLineRxPwrHighWngPortn_Type = EkiOnOff
_Pm200fr20AlmLineRxPwrHighWngPortn_Object = MibTableColumn
pm200fr20AlmLineRxPwrHighWngPortn = _Pm200fr20AlmLineRxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 1, 104, 1, 17),
    _Pm200fr20AlmLineRxPwrHighWngPortn_Type()
)
pm200fr20AlmLineRxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmLineRxPwrHighWngPortn.setStatus("current")
_Pm200fr20AlmLineUrg_ObjectIdentity = ObjectIdentity
pm200fr20AlmLineUrg = _Pm200fr20AlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 2)
)
_Pm200fr20AlmlineHostLaneFaultTable_Object = MibTable
pm200fr20AlmlineHostLaneFaultTable = _Pm200fr20AlmlineHostLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 2, 196)
)
if mibBuilder.loadTexts:
    pm200fr20AlmlineHostLaneFaultTable.setStatus("current")
_Pm200fr20AlmlineHostLaneFaultEntry_Object = MibTableRow
pm200fr20AlmlineHostLaneFaultEntry = _Pm200fr20AlmlineHostLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 2, 196, 1)
)
pm200fr20AlmlineHostLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20AlmlineHostLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20AlmlineHostLaneFaultEntry.setStatus("current")


class _Pm200fr20AlmlineHostLaneFaultIndex_Type(Integer32):
    """Custom type pm200fr20AlmlineHostLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20AlmlineHostLaneFaultIndex_Type.__name__ = "Integer32"
_Pm200fr20AlmlineHostLaneFaultIndex_Object = MibTableColumn
pm200fr20AlmlineHostLaneFaultIndex = _Pm200fr20AlmlineHostLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 2, 196, 1, 1),
    _Pm200fr20AlmlineHostLaneFaultIndex_Type()
)
pm200fr20AlmlineHostLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmlineHostLaneFaultIndex.setStatus("current")
_Pm200fr20AlmLineInputLossOfSignalPortn_Type = EkiOnOff
_Pm200fr20AlmLineInputLossOfSignalPortn_Object = MibTableColumn
pm200fr20AlmLineInputLossOfSignalPortn = _Pm200fr20AlmLineInputLossOfSignalPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 2, 196, 1, 2),
    _Pm200fr20AlmLineInputLossOfSignalPortn_Type()
)
pm200fr20AlmLineInputLossOfSignalPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmLineInputLossOfSignalPortn.setStatus("current")
_Pm200fr20AlmLineLossOfFramePortn_Type = EkiOnOff
_Pm200fr20AlmLineLossOfFramePortn_Object = MibTableColumn
pm200fr20AlmLineLossOfFramePortn = _Pm200fr20AlmLineLossOfFramePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 2, 196, 1, 3),
    _Pm200fr20AlmLineLossOfFramePortn_Type()
)
pm200fr20AlmLineLossOfFramePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmLineLossOfFramePortn.setStatus("current")
_Pm200fr20AlmLineSmBdiInsertedPortn_Type = EkiOnOff
_Pm200fr20AlmLineSmBdiInsertedPortn_Object = MibTableColumn
pm200fr20AlmLineSmBdiInsertedPortn = _Pm200fr20AlmLineSmBdiInsertedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 2, 196, 1, 4),
    _Pm200fr20AlmLineSmBdiInsertedPortn_Type()
)
pm200fr20AlmLineSmBdiInsertedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmLineSmBdiInsertedPortn.setStatus("current")
_Pm200fr20AlmLineSmBdiDetectedPortn_Type = EkiOnOff
_Pm200fr20AlmLineSmBdiDetectedPortn_Object = MibTableColumn
pm200fr20AlmLineSmBdiDetectedPortn = _Pm200fr20AlmLineSmBdiDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 2, 196, 1, 5),
    _Pm200fr20AlmLineSmBdiDetectedPortn_Type()
)
pm200fr20AlmLineSmBdiDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmLineSmBdiDetectedPortn.setStatus("current")
_Pm200fr20AlmLineSmIaeInsertedPortn_Type = EkiOnOff
_Pm200fr20AlmLineSmIaeInsertedPortn_Object = MibTableColumn
pm200fr20AlmLineSmIaeInsertedPortn = _Pm200fr20AlmLineSmIaeInsertedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 2, 196, 1, 6),
    _Pm200fr20AlmLineSmIaeInsertedPortn_Type()
)
pm200fr20AlmLineSmIaeInsertedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmLineSmIaeInsertedPortn.setStatus("current")
_Pm200fr20AlmLineSmIaeDetectedPortn_Type = EkiOnOff
_Pm200fr20AlmLineSmIaeDetectedPortn_Object = MibTableColumn
pm200fr20AlmLineSmIaeDetectedPortn = _Pm200fr20AlmLineSmIaeDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 2, 196, 1, 7),
    _Pm200fr20AlmLineSmIaeDetectedPortn_Type()
)
pm200fr20AlmLineSmIaeDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmLineSmIaeDetectedPortn.setStatus("current")
_Pm200fr20AlmOtu4DdegPortn_Type = EkiOnOff
_Pm200fr20AlmOtu4DdegPortn_Object = MibTableColumn
pm200fr20AlmOtu4DdegPortn = _Pm200fr20AlmOtu4DdegPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 2, 196, 1, 8),
    _Pm200fr20AlmOtu4DdegPortn_Type()
)
pm200fr20AlmOtu4DdegPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmOtu4DdegPortn.setStatus("current")
_Pm200fr20AlmClientOtu4DtimPortn_Type = EkiOnOff
_Pm200fr20AlmClientOtu4DtimPortn_Object = MibTableColumn
pm200fr20AlmClientOtu4DtimPortn = _Pm200fr20AlmClientOtu4DtimPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 2, 196, 1, 9),
    _Pm200fr20AlmClientOtu4DtimPortn_Type()
)
pm200fr20AlmClientOtu4DtimPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmClientOtu4DtimPortn.setStatus("current")
_Pm200fr20AlmLineOchr4DlosPPortn_Type = EkiOnOff
_Pm200fr20AlmLineOchr4DlosPPortn_Object = MibTableColumn
pm200fr20AlmLineOchr4DlosPPortn = _Pm200fr20AlmLineOchr4DlosPPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 2, 196, 1, 12),
    _Pm200fr20AlmLineOchr4DlosPPortn_Type()
)
pm200fr20AlmLineOchr4DlosPPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmLineOchr4DlosPPortn.setStatus("current")
_Pm200fr20AlmLineOtu4DlomPortn_Type = EkiOnOff
_Pm200fr20AlmLineOtu4DlomPortn_Object = MibTableColumn
pm200fr20AlmLineOtu4DlomPortn = _Pm200fr20AlmLineOtu4DlomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 2, 196, 1, 17),
    _Pm200fr20AlmLineOtu4DlomPortn_Type()
)
pm200fr20AlmLineOtu4DlomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmLineOtu4DlomPortn.setStatus("current")
_Pm200fr20AlmlineOdu4AlmTable_Object = MibTable
pm200fr20AlmlineOdu4AlmTable = _Pm200fr20AlmlineOdu4AlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 2, 208)
)
if mibBuilder.loadTexts:
    pm200fr20AlmlineOdu4AlmTable.setStatus("current")
_Pm200fr20AlmlineOdu4AlmEntry_Object = MibTableRow
pm200fr20AlmlineOdu4AlmEntry = _Pm200fr20AlmlineOdu4AlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 2, 208, 1)
)
pm200fr20AlmlineOdu4AlmEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20AlmlineOdu4AlmIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20AlmlineOdu4AlmEntry.setStatus("current")


class _Pm200fr20AlmlineOdu4AlmIndex_Type(Integer32):
    """Custom type pm200fr20AlmlineOdu4AlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20AlmlineOdu4AlmIndex_Type.__name__ = "Integer32"
_Pm200fr20AlmlineOdu4AlmIndex_Object = MibTableColumn
pm200fr20AlmlineOdu4AlmIndex = _Pm200fr20AlmlineOdu4AlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 2, 208, 1, 1),
    _Pm200fr20AlmlineOdu4AlmIndex_Type()
)
pm200fr20AlmlineOdu4AlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmlineOdu4AlmIndex.setStatus("current")
_Pm200fr20AlmLineOdu4DplmPortn_Type = EkiOnOff
_Pm200fr20AlmLineOdu4DplmPortn_Object = MibTableColumn
pm200fr20AlmLineOdu4DplmPortn = _Pm200fr20AlmLineOdu4DplmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 2, 208, 1, 4),
    _Pm200fr20AlmLineOdu4DplmPortn_Type()
)
pm200fr20AlmLineOdu4DplmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmLineOdu4DplmPortn.setStatus("current")
_Pm200fr20AlmLineOdu4DdegPortn_Type = EkiOnOff
_Pm200fr20AlmLineOdu4DdegPortn_Object = MibTableColumn
pm200fr20AlmLineOdu4DdegPortn = _Pm200fr20AlmLineOdu4DdegPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 2, 208, 1, 6),
    _Pm200fr20AlmLineOdu4DdegPortn_Type()
)
pm200fr20AlmLineOdu4DdegPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmLineOdu4DdegPortn.setStatus("current")
_Pm200fr20AlmLineOdu4IaisPortn_Type = EkiOnOff
_Pm200fr20AlmLineOdu4IaisPortn_Object = MibTableColumn
pm200fr20AlmLineOdu4IaisPortn = _Pm200fr20AlmLineOdu4IaisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 2, 208, 1, 8),
    _Pm200fr20AlmLineOdu4IaisPortn_Type()
)
pm200fr20AlmLineOdu4IaisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmLineOdu4IaisPortn.setStatus("current")
_Pm200fr20AlmLineOdu4DtimPortn_Type = EkiOnOff
_Pm200fr20AlmLineOdu4DtimPortn_Object = MibTableColumn
pm200fr20AlmLineOdu4DtimPortn = _Pm200fr20AlmLineOdu4DtimPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 2, 208, 1, 9),
    _Pm200fr20AlmLineOdu4DtimPortn_Type()
)
pm200fr20AlmLineOdu4DtimPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmLineOdu4DtimPortn.setStatus("current")
_Pm200fr20AlmLineOdu4DaisPortn_Type = EkiOnOff
_Pm200fr20AlmLineOdu4DaisPortn_Object = MibTableColumn
pm200fr20AlmLineOdu4DaisPortn = _Pm200fr20AlmLineOdu4DaisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 2, 208, 1, 10),
    _Pm200fr20AlmLineOdu4DaisPortn_Type()
)
pm200fr20AlmLineOdu4DaisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmLineOdu4DaisPortn.setStatus("current")
_Pm200fr20AlmLineOdu4IociPortn_Type = EkiOnOff
_Pm200fr20AlmLineOdu4IociPortn_Object = MibTableColumn
pm200fr20AlmLineOdu4IociPortn = _Pm200fr20AlmLineOdu4IociPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 2, 208, 1, 12),
    _Pm200fr20AlmLineOdu4IociPortn_Type()
)
pm200fr20AlmLineOdu4IociPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmLineOdu4IociPortn.setStatus("current")
_Pm200fr20AlmLineOdu4DociPortn_Type = EkiOnOff
_Pm200fr20AlmLineOdu4DociPortn_Object = MibTableColumn
pm200fr20AlmLineOdu4DociPortn = _Pm200fr20AlmLineOdu4DociPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 2, 208, 1, 13),
    _Pm200fr20AlmLineOdu4DociPortn_Type()
)
pm200fr20AlmLineOdu4DociPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmLineOdu4DociPortn.setStatus("current")
_Pm200fr20AlmLineOdu4IbdiPortn_Type = EkiOnOff
_Pm200fr20AlmLineOdu4IbdiPortn_Object = MibTableColumn
pm200fr20AlmLineOdu4IbdiPortn = _Pm200fr20AlmLineOdu4IbdiPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 2, 208, 1, 14),
    _Pm200fr20AlmLineOdu4IbdiPortn_Type()
)
pm200fr20AlmLineOdu4IbdiPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmLineOdu4IbdiPortn.setStatus("current")
_Pm200fr20AlmLineOdu4DbdiPortn_Type = EkiOnOff
_Pm200fr20AlmLineOdu4DbdiPortn_Object = MibTableColumn
pm200fr20AlmLineOdu4DbdiPortn = _Pm200fr20AlmLineOdu4DbdiPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 2, 208, 1, 15),
    _Pm200fr20AlmLineOdu4DbdiPortn_Type()
)
pm200fr20AlmLineOdu4DbdiPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmLineOdu4DbdiPortn.setStatus("current")
_Pm200fr20AlmLineOdu4IlckPortn_Type = EkiOnOff
_Pm200fr20AlmLineOdu4IlckPortn_Object = MibTableColumn
pm200fr20AlmLineOdu4IlckPortn = _Pm200fr20AlmLineOdu4IlckPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 2, 208, 1, 16),
    _Pm200fr20AlmLineOdu4IlckPortn_Type()
)
pm200fr20AlmLineOdu4IlckPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmLineOdu4IlckPortn.setStatus("current")
_Pm200fr20AlmLineOdu4DlckPortn_Type = EkiOnOff
_Pm200fr20AlmLineOdu4DlckPortn_Object = MibTableColumn
pm200fr20AlmLineOdu4DlckPortn = _Pm200fr20AlmLineOdu4DlckPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 2, 208, 1, 17),
    _Pm200fr20AlmLineOdu4DlckPortn_Type()
)
pm200fr20AlmLineOdu4DlckPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmLineOdu4DlckPortn.setStatus("current")
_Pm200fr20AlmLineCrit_ObjectIdentity = ObjectIdentity
pm200fr20AlmLineCrit = _Pm200fr20AlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 3)
)
_Pm200fr20AlmsynthAlmLineTable_Object = MibTable
pm200fr20AlmsynthAlmLineTable = _Pm200fr20AlmsynthAlmLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 3, 40)
)
if mibBuilder.loadTexts:
    pm200fr20AlmsynthAlmLineTable.setStatus("current")
_Pm200fr20AlmsynthAlmLineEntry_Object = MibTableRow
pm200fr20AlmsynthAlmLineEntry = _Pm200fr20AlmsynthAlmLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 3, 40, 1)
)
pm200fr20AlmsynthAlmLineEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20AlmsynthAlmLineIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20AlmsynthAlmLineEntry.setStatus("current")


class _Pm200fr20AlmsynthAlmLineIndex_Type(Integer32):
    """Custom type pm200fr20AlmsynthAlmLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20AlmsynthAlmLineIndex_Type.__name__ = "Integer32"
_Pm200fr20AlmsynthAlmLineIndex_Object = MibTableColumn
pm200fr20AlmsynthAlmLineIndex = _Pm200fr20AlmsynthAlmLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 3, 40, 1, 1),
    _Pm200fr20AlmsynthAlmLineIndex_Type()
)
pm200fr20AlmsynthAlmLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmsynthAlmLineIndex.setStatus("current")
_Pm200fr20AlmXfpAbsentPortn_Type = EkiOnOff
_Pm200fr20AlmXfpAbsentPortn_Object = MibTableColumn
pm200fr20AlmXfpAbsentPortn = _Pm200fr20AlmXfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 3, 40, 1, 2),
    _Pm200fr20AlmXfpAbsentPortn_Type()
)
pm200fr20AlmXfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmXfpAbsentPortn.setStatus("current")
_Pm200fr20AlmXfpInitNotComplPortn_Type = EkiOnOff
_Pm200fr20AlmXfpInitNotComplPortn_Object = MibTableColumn
pm200fr20AlmXfpInitNotComplPortn = _Pm200fr20AlmXfpInitNotComplPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 3, 40, 1, 3),
    _Pm200fr20AlmXfpInitNotComplPortn_Type()
)
pm200fr20AlmXfpInitNotComplPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmXfpInitNotComplPortn.setStatus("current")
_Pm200fr20AlmLineHwFailPortn_Type = EkiOnOff
_Pm200fr20AlmLineHwFailPortn_Object = MibTableColumn
pm200fr20AlmLineHwFailPortn = _Pm200fr20AlmLineHwFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 3, 40, 1, 5),
    _Pm200fr20AlmLineHwFailPortn_Type()
)
pm200fr20AlmLineHwFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmLineHwFailPortn.setStatus("current")
_Pm200fr20AlmXfpTxOffPortn_Type = EkiOnOff
_Pm200fr20AlmXfpTxOffPortn_Object = MibTableColumn
pm200fr20AlmXfpTxOffPortn = _Pm200fr20AlmXfpTxOffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 3, 40, 1, 6),
    _Pm200fr20AlmXfpTxOffPortn_Type()
)
pm200fr20AlmXfpTxOffPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmXfpTxOffPortn.setStatus("current")
_Pm200fr20AlmLineLocalOosPortn_Type = EkiOnOff
_Pm200fr20AlmLineLocalOosPortn_Object = MibTableColumn
pm200fr20AlmLineLocalOosPortn = _Pm200fr20AlmLineLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 3, 40, 1, 7),
    _Pm200fr20AlmLineLocalOosPortn_Type()
)
pm200fr20AlmLineLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmLineLocalOosPortn.setStatus("current")
_Pm200fr20AlmUpRdiInsPortn_Type = EkiOnOff
_Pm200fr20AlmUpRdiInsPortn_Object = MibTableColumn
pm200fr20AlmUpRdiInsPortn = _Pm200fr20AlmUpRdiInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 3, 40, 1, 9),
    _Pm200fr20AlmUpRdiInsPortn_Type()
)
pm200fr20AlmUpRdiInsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmUpRdiInsPortn.setStatus("current")
_Pm200fr20AlmLineDdmWarningPortn_Type = EkiOnOff
_Pm200fr20AlmLineDdmWarningPortn_Object = MibTableColumn
pm200fr20AlmLineDdmWarningPortn = _Pm200fr20AlmLineDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 3, 40, 1, 10),
    _Pm200fr20AlmLineDdmWarningPortn_Type()
)
pm200fr20AlmLineDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmLineDdmWarningPortn.setStatus("current")
_Pm200fr20AlmLineDdmAlmPortn_Type = EkiOnOff
_Pm200fr20AlmLineDdmAlmPortn_Object = MibTableColumn
pm200fr20AlmLineDdmAlmPortn = _Pm200fr20AlmLineDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 3, 40, 1, 11),
    _Pm200fr20AlmLineDdmAlmPortn_Type()
)
pm200fr20AlmLineDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmLineDdmAlmPortn.setStatus("current")
_Pm200fr20AlmLineFailPortn_Type = EkiOnOff
_Pm200fr20AlmLineFailPortn_Object = MibTableColumn
pm200fr20AlmLineFailPortn = _Pm200fr20AlmLineFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 2, 3, 3, 40, 1, 13),
    _Pm200fr20AlmLineFailPortn_Type()
)
pm200fr20AlmLineFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20AlmLineFailPortn.setStatus("current")
_Pm200fr20measures_ObjectIdentity = ObjectIdentity
pm200fr20measures = _Pm200fr20measures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3)
)
_Pm200fr20MesrOther_ObjectIdentity = ObjectIdentity
pm200fr20MesrOther = _Pm200fr20MesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1)
)
_Pm200fr20Mesrsynth0_Type = EkiMeasureType
_Pm200fr20Mesrsynth0_Object = MibScalar
pm200fr20Mesrsynth0 = _Pm200fr20Mesrsynth0_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 0),
    _Pm200fr20Mesrsynth0_Type()
)
pm200fr20Mesrsynth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20Mesrsynth0.setStatus("deprecated")
_Pm200fr20Mesrsynth1_Type = EkiMeasureType
_Pm200fr20Mesrsynth1_Object = MibScalar
pm200fr20Mesrsynth1 = _Pm200fr20Mesrsynth1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 1),
    _Pm200fr20Mesrsynth1_Type()
)
pm200fr20Mesrsynth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20Mesrsynth1.setStatus("deprecated")


class _Pm200fr20MesrpmIntervalNumber_Type(Unsigned32):
    """Custom type pm200fr20MesrpmIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrpmIntervalNumber_Type.__name__ = "Unsigned32"
_Pm200fr20MesrpmIntervalNumber_Object = MibScalar
pm200fr20MesrpmIntervalNumber = _Pm200fr20MesrpmIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 7),
    _Pm200fr20MesrpmIntervalNumber_Type()
)
pm200fr20MesrpmIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrpmIntervalNumber.setStatus("current")


class _Pm200fr20MesrlineNetTxLaserOutputPwrAverage_Type(Unsigned32):
    """Custom type pm200fr20MesrlineNetTxLaserOutputPwrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrlineNetTxLaserOutputPwrAverage_Type.__name__ = "Unsigned32"
_Pm200fr20MesrlineNetTxLaserOutputPwrAverage_Object = MibScalar
pm200fr20MesrlineNetTxLaserOutputPwrAverage = _Pm200fr20MesrlineNetTxLaserOutputPwrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 196),
    _Pm200fr20MesrlineNetTxLaserOutputPwrAverage_Type()
)
pm200fr20MesrlineNetTxLaserOutputPwrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineNetTxLaserOutputPwrAverage.setStatus("current")


class _Pm200fr20MesrlineNetTxLaserTempAverage_Type(Unsigned32):
    """Custom type pm200fr20MesrlineNetTxLaserTempAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrlineNetTxLaserTempAverage_Type.__name__ = "Unsigned32"
_Pm200fr20MesrlineNetTxLaserTempAverage_Object = MibScalar
pm200fr20MesrlineNetTxLaserTempAverage = _Pm200fr20MesrlineNetTxLaserTempAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 197),
    _Pm200fr20MesrlineNetTxLaserTempAverage_Type()
)
pm200fr20MesrlineNetTxLaserTempAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineNetTxLaserTempAverage.setStatus("current")


class _Pm200fr20MesrlineNetTxBiasCurrentAverage_Type(Unsigned32):
    """Custom type pm200fr20MesrlineNetTxBiasCurrentAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrlineNetTxBiasCurrentAverage_Type.__name__ = "Unsigned32"
_Pm200fr20MesrlineNetTxBiasCurrentAverage_Object = MibScalar
pm200fr20MesrlineNetTxBiasCurrentAverage = _Pm200fr20MesrlineNetTxBiasCurrentAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 198),
    _Pm200fr20MesrlineNetTxBiasCurrentAverage_Type()
)
pm200fr20MesrlineNetTxBiasCurrentAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineNetTxBiasCurrentAverage.setStatus("current")


class _Pm200fr20MesrlineNetRxInputPwrAverage_Type(Unsigned32):
    """Custom type pm200fr20MesrlineNetRxInputPwrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrlineNetRxInputPwrAverage_Type.__name__ = "Unsigned32"
_Pm200fr20MesrlineNetRxInputPwrAverage_Object = MibScalar
pm200fr20MesrlineNetRxInputPwrAverage = _Pm200fr20MesrlineNetRxInputPwrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 199),
    _Pm200fr20MesrlineNetRxInputPwrAverage_Type()
)
pm200fr20MesrlineNetRxInputPwrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineNetRxInputPwrAverage.setStatus("current")


class _Pm200fr20MesrlineResidualChromaticDispAverage_Type(Unsigned32):
    """Custom type pm200fr20MesrlineResidualChromaticDispAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrlineResidualChromaticDispAverage_Type.__name__ = "Unsigned32"
_Pm200fr20MesrlineResidualChromaticDispAverage_Object = MibScalar
pm200fr20MesrlineResidualChromaticDispAverage = _Pm200fr20MesrlineResidualChromaticDispAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 200),
    _Pm200fr20MesrlineResidualChromaticDispAverage_Type()
)
pm200fr20MesrlineResidualChromaticDispAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineResidualChromaticDispAverage.setStatus("current")


class _Pm200fr20MesrlineDiffGroupDelayAverage_Type(Unsigned32):
    """Custom type pm200fr20MesrlineDiffGroupDelayAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrlineDiffGroupDelayAverage_Type.__name__ = "Unsigned32"
_Pm200fr20MesrlineDiffGroupDelayAverage_Object = MibScalar
pm200fr20MesrlineDiffGroupDelayAverage = _Pm200fr20MesrlineDiffGroupDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 201),
    _Pm200fr20MesrlineDiffGroupDelayAverage_Type()
)
pm200fr20MesrlineDiffGroupDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineDiffGroupDelayAverage.setStatus("current")


class _Pm200fr20MesrlineQFactorAverage_Type(Unsigned32):
    """Custom type pm200fr20MesrlineQFactorAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrlineQFactorAverage_Type.__name__ = "Unsigned32"
_Pm200fr20MesrlineQFactorAverage_Object = MibScalar
pm200fr20MesrlineQFactorAverage = _Pm200fr20MesrlineQFactorAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 202),
    _Pm200fr20MesrlineQFactorAverage_Type()
)
pm200fr20MesrlineQFactorAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineQFactorAverage.setStatus("current")


class _Pm200fr20MesrlineCarrierFreqOffsetAverage_Type(Unsigned32):
    """Custom type pm200fr20MesrlineCarrierFreqOffsetAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrlineCarrierFreqOffsetAverage_Type.__name__ = "Unsigned32"
_Pm200fr20MesrlineCarrierFreqOffsetAverage_Object = MibScalar
pm200fr20MesrlineCarrierFreqOffsetAverage = _Pm200fr20MesrlineCarrierFreqOffsetAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 203),
    _Pm200fr20MesrlineCarrierFreqOffsetAverage_Type()
)
pm200fr20MesrlineCarrierFreqOffsetAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineCarrierFreqOffsetAverage.setStatus("current")


class _Pm200fr20MesrlineOsnrAverage_Type(Unsigned32):
    """Custom type pm200fr20MesrlineOsnrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrlineOsnrAverage_Type.__name__ = "Unsigned32"
_Pm200fr20MesrlineOsnrAverage_Object = MibScalar
pm200fr20MesrlineOsnrAverage = _Pm200fr20MesrlineOsnrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 204),
    _Pm200fr20MesrlineOsnrAverage_Type()
)
pm200fr20MesrlineOsnrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineOsnrAverage.setStatus("current")


class _Pm200fr20MesrclientNetTxTempMin_Type(Unsigned32):
    """Custom type pm200fr20MesrclientNetTxTempMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrclientNetTxTempMin_Type.__name__ = "Unsigned32"
_Pm200fr20MesrclientNetTxTempMin_Object = MibScalar
pm200fr20MesrclientNetTxTempMin = _Pm200fr20MesrclientNetTxTempMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 208),
    _Pm200fr20MesrclientNetTxTempMin_Type()
)
pm200fr20MesrclientNetTxTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrclientNetTxTempMin.setStatus("current")


class _Pm200fr20MesrclientNetTxBiasMin_Type(Unsigned32):
    """Custom type pm200fr20MesrclientNetTxBiasMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrclientNetTxBiasMin_Type.__name__ = "Unsigned32"
_Pm200fr20MesrclientNetTxBiasMin_Object = MibScalar
pm200fr20MesrclientNetTxBiasMin = _Pm200fr20MesrclientNetTxBiasMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 209),
    _Pm200fr20MesrclientNetTxBiasMin_Type()
)
pm200fr20MesrclientNetTxBiasMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrclientNetTxBiasMin.setStatus("current")


class _Pm200fr20MesrclientNetTxPwrMin_Type(Unsigned32):
    """Custom type pm200fr20MesrclientNetTxPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrclientNetTxPwrMin_Type.__name__ = "Unsigned32"
_Pm200fr20MesrclientNetTxPwrMin_Object = MibScalar
pm200fr20MesrclientNetTxPwrMin = _Pm200fr20MesrclientNetTxPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 210),
    _Pm200fr20MesrclientNetTxPwrMin_Type()
)
pm200fr20MesrclientNetTxPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrclientNetTxPwrMin.setStatus("current")


class _Pm200fr20MesrclientNetRxPwrMin_Type(Unsigned32):
    """Custom type pm200fr20MesrclientNetRxPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrclientNetRxPwrMin_Type.__name__ = "Unsigned32"
_Pm200fr20MesrclientNetRxPwrMin_Object = MibScalar
pm200fr20MesrclientNetRxPwrMin = _Pm200fr20MesrclientNetRxPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 211),
    _Pm200fr20MesrclientNetRxPwrMin_Type()
)
pm200fr20MesrclientNetRxPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrclientNetRxPwrMin.setStatus("current")


class _Pm200fr20MesrlineNetTxLaserOutputPwrMin_Type(Unsigned32):
    """Custom type pm200fr20MesrlineNetTxLaserOutputPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrlineNetTxLaserOutputPwrMin_Type.__name__ = "Unsigned32"
_Pm200fr20MesrlineNetTxLaserOutputPwrMin_Object = MibScalar
pm200fr20MesrlineNetTxLaserOutputPwrMin = _Pm200fr20MesrlineNetTxLaserOutputPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 212),
    _Pm200fr20MesrlineNetTxLaserOutputPwrMin_Type()
)
pm200fr20MesrlineNetTxLaserOutputPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineNetTxLaserOutputPwrMin.setStatus("current")


class _Pm200fr20MesrlineNetTxLaserTempMin_Type(Unsigned32):
    """Custom type pm200fr20MesrlineNetTxLaserTempMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrlineNetTxLaserTempMin_Type.__name__ = "Unsigned32"
_Pm200fr20MesrlineNetTxLaserTempMin_Object = MibScalar
pm200fr20MesrlineNetTxLaserTempMin = _Pm200fr20MesrlineNetTxLaserTempMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 213),
    _Pm200fr20MesrlineNetTxLaserTempMin_Type()
)
pm200fr20MesrlineNetTxLaserTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineNetTxLaserTempMin.setStatus("current")


class _Pm200fr20MesrlineNetTxBiasCurrentMin_Type(Unsigned32):
    """Custom type pm200fr20MesrlineNetTxBiasCurrentMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrlineNetTxBiasCurrentMin_Type.__name__ = "Unsigned32"
_Pm200fr20MesrlineNetTxBiasCurrentMin_Object = MibScalar
pm200fr20MesrlineNetTxBiasCurrentMin = _Pm200fr20MesrlineNetTxBiasCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 214),
    _Pm200fr20MesrlineNetTxBiasCurrentMin_Type()
)
pm200fr20MesrlineNetTxBiasCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineNetTxBiasCurrentMin.setStatus("current")


class _Pm200fr20MesrlineNetRxInputPwrMin_Type(Unsigned32):
    """Custom type pm200fr20MesrlineNetRxInputPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrlineNetRxInputPwrMin_Type.__name__ = "Unsigned32"
_Pm200fr20MesrlineNetRxInputPwrMin_Object = MibScalar
pm200fr20MesrlineNetRxInputPwrMin = _Pm200fr20MesrlineNetRxInputPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 215),
    _Pm200fr20MesrlineNetRxInputPwrMin_Type()
)
pm200fr20MesrlineNetRxInputPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineNetRxInputPwrMin.setStatus("current")


class _Pm200fr20MesrlineResidualChromaticDispMin_Type(Unsigned32):
    """Custom type pm200fr20MesrlineResidualChromaticDispMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrlineResidualChromaticDispMin_Type.__name__ = "Unsigned32"
_Pm200fr20MesrlineResidualChromaticDispMin_Object = MibScalar
pm200fr20MesrlineResidualChromaticDispMin = _Pm200fr20MesrlineResidualChromaticDispMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 216),
    _Pm200fr20MesrlineResidualChromaticDispMin_Type()
)
pm200fr20MesrlineResidualChromaticDispMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineResidualChromaticDispMin.setStatus("current")


class _Pm200fr20MesrlineDiffGroupDelayMin_Type(Unsigned32):
    """Custom type pm200fr20MesrlineDiffGroupDelayMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrlineDiffGroupDelayMin_Type.__name__ = "Unsigned32"
_Pm200fr20MesrlineDiffGroupDelayMin_Object = MibScalar
pm200fr20MesrlineDiffGroupDelayMin = _Pm200fr20MesrlineDiffGroupDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 217),
    _Pm200fr20MesrlineDiffGroupDelayMin_Type()
)
pm200fr20MesrlineDiffGroupDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineDiffGroupDelayMin.setStatus("current")


class _Pm200fr20MesrlineQFactorMin_Type(Unsigned32):
    """Custom type pm200fr20MesrlineQFactorMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrlineQFactorMin_Type.__name__ = "Unsigned32"
_Pm200fr20MesrlineQFactorMin_Object = MibScalar
pm200fr20MesrlineQFactorMin = _Pm200fr20MesrlineQFactorMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 218),
    _Pm200fr20MesrlineQFactorMin_Type()
)
pm200fr20MesrlineQFactorMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineQFactorMin.setStatus("current")


class _Pm200fr20MesrlineCarrierFreqOffsetMin_Type(Unsigned32):
    """Custom type pm200fr20MesrlineCarrierFreqOffsetMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrlineCarrierFreqOffsetMin_Type.__name__ = "Unsigned32"
_Pm200fr20MesrlineCarrierFreqOffsetMin_Object = MibScalar
pm200fr20MesrlineCarrierFreqOffsetMin = _Pm200fr20MesrlineCarrierFreqOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 219),
    _Pm200fr20MesrlineCarrierFreqOffsetMin_Type()
)
pm200fr20MesrlineCarrierFreqOffsetMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineCarrierFreqOffsetMin.setStatus("current")


class _Pm200fr20MesrlineOsnrMin_Type(Unsigned32):
    """Custom type pm200fr20MesrlineOsnrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrlineOsnrMin_Type.__name__ = "Unsigned32"
_Pm200fr20MesrlineOsnrMin_Object = MibScalar
pm200fr20MesrlineOsnrMin = _Pm200fr20MesrlineOsnrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 220),
    _Pm200fr20MesrlineOsnrMin_Type()
)
pm200fr20MesrlineOsnrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineOsnrMin.setStatus("current")


class _Pm200fr20MesrclientNetTxTempMax_Type(Unsigned32):
    """Custom type pm200fr20MesrclientNetTxTempMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrclientNetTxTempMax_Type.__name__ = "Unsigned32"
_Pm200fr20MesrclientNetTxTempMax_Object = MibScalar
pm200fr20MesrclientNetTxTempMax = _Pm200fr20MesrclientNetTxTempMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 224),
    _Pm200fr20MesrclientNetTxTempMax_Type()
)
pm200fr20MesrclientNetTxTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrclientNetTxTempMax.setStatus("current")


class _Pm200fr20MesrclientNetTxBiasMax_Type(Unsigned32):
    """Custom type pm200fr20MesrclientNetTxBiasMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrclientNetTxBiasMax_Type.__name__ = "Unsigned32"
_Pm200fr20MesrclientNetTxBiasMax_Object = MibScalar
pm200fr20MesrclientNetTxBiasMax = _Pm200fr20MesrclientNetTxBiasMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 225),
    _Pm200fr20MesrclientNetTxBiasMax_Type()
)
pm200fr20MesrclientNetTxBiasMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrclientNetTxBiasMax.setStatus("current")


class _Pm200fr20MesrclientNetTxPwrMax_Type(Unsigned32):
    """Custom type pm200fr20MesrclientNetTxPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrclientNetTxPwrMax_Type.__name__ = "Unsigned32"
_Pm200fr20MesrclientNetTxPwrMax_Object = MibScalar
pm200fr20MesrclientNetTxPwrMax = _Pm200fr20MesrclientNetTxPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 226),
    _Pm200fr20MesrclientNetTxPwrMax_Type()
)
pm200fr20MesrclientNetTxPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrclientNetTxPwrMax.setStatus("current")


class _Pm200fr20MesrclientNetRxPwrMax_Type(Unsigned32):
    """Custom type pm200fr20MesrclientNetRxPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrclientNetRxPwrMax_Type.__name__ = "Unsigned32"
_Pm200fr20MesrclientNetRxPwrMax_Object = MibScalar
pm200fr20MesrclientNetRxPwrMax = _Pm200fr20MesrclientNetRxPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 227),
    _Pm200fr20MesrclientNetRxPwrMax_Type()
)
pm200fr20MesrclientNetRxPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrclientNetRxPwrMax.setStatus("current")


class _Pm200fr20MesrlineNetTxLaserOutputPwrMax_Type(Unsigned32):
    """Custom type pm200fr20MesrlineNetTxLaserOutputPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrlineNetTxLaserOutputPwrMax_Type.__name__ = "Unsigned32"
_Pm200fr20MesrlineNetTxLaserOutputPwrMax_Object = MibScalar
pm200fr20MesrlineNetTxLaserOutputPwrMax = _Pm200fr20MesrlineNetTxLaserOutputPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 228),
    _Pm200fr20MesrlineNetTxLaserOutputPwrMax_Type()
)
pm200fr20MesrlineNetTxLaserOutputPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineNetTxLaserOutputPwrMax.setStatus("current")


class _Pm200fr20MesrlineNetTxLaserTempMax_Type(Unsigned32):
    """Custom type pm200fr20MesrlineNetTxLaserTempMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrlineNetTxLaserTempMax_Type.__name__ = "Unsigned32"
_Pm200fr20MesrlineNetTxLaserTempMax_Object = MibScalar
pm200fr20MesrlineNetTxLaserTempMax = _Pm200fr20MesrlineNetTxLaserTempMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 229),
    _Pm200fr20MesrlineNetTxLaserTempMax_Type()
)
pm200fr20MesrlineNetTxLaserTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineNetTxLaserTempMax.setStatus("current")


class _Pm200fr20MesrlineNetTxBiasCurrentMax_Type(Unsigned32):
    """Custom type pm200fr20MesrlineNetTxBiasCurrentMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrlineNetTxBiasCurrentMax_Type.__name__ = "Unsigned32"
_Pm200fr20MesrlineNetTxBiasCurrentMax_Object = MibScalar
pm200fr20MesrlineNetTxBiasCurrentMax = _Pm200fr20MesrlineNetTxBiasCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 230),
    _Pm200fr20MesrlineNetTxBiasCurrentMax_Type()
)
pm200fr20MesrlineNetTxBiasCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineNetTxBiasCurrentMax.setStatus("current")


class _Pm200fr20MesrlineNetRxInputPwrMax_Type(Unsigned32):
    """Custom type pm200fr20MesrlineNetRxInputPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrlineNetRxInputPwrMax_Type.__name__ = "Unsigned32"
_Pm200fr20MesrlineNetRxInputPwrMax_Object = MibScalar
pm200fr20MesrlineNetRxInputPwrMax = _Pm200fr20MesrlineNetRxInputPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 231),
    _Pm200fr20MesrlineNetRxInputPwrMax_Type()
)
pm200fr20MesrlineNetRxInputPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineNetRxInputPwrMax.setStatus("current")


class _Pm200fr20MesrlineResidualChromaticDispMax_Type(Unsigned32):
    """Custom type pm200fr20MesrlineResidualChromaticDispMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrlineResidualChromaticDispMax_Type.__name__ = "Unsigned32"
_Pm200fr20MesrlineResidualChromaticDispMax_Object = MibScalar
pm200fr20MesrlineResidualChromaticDispMax = _Pm200fr20MesrlineResidualChromaticDispMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 232),
    _Pm200fr20MesrlineResidualChromaticDispMax_Type()
)
pm200fr20MesrlineResidualChromaticDispMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineResidualChromaticDispMax.setStatus("current")


class _Pm200fr20MesrlineDiffGroupDelayMax_Type(Unsigned32):
    """Custom type pm200fr20MesrlineDiffGroupDelayMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrlineDiffGroupDelayMax_Type.__name__ = "Unsigned32"
_Pm200fr20MesrlineDiffGroupDelayMax_Object = MibScalar
pm200fr20MesrlineDiffGroupDelayMax = _Pm200fr20MesrlineDiffGroupDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 233),
    _Pm200fr20MesrlineDiffGroupDelayMax_Type()
)
pm200fr20MesrlineDiffGroupDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineDiffGroupDelayMax.setStatus("current")


class _Pm200fr20MesrlineQFactorMax_Type(Unsigned32):
    """Custom type pm200fr20MesrlineQFactorMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrlineQFactorMax_Type.__name__ = "Unsigned32"
_Pm200fr20MesrlineQFactorMax_Object = MibScalar
pm200fr20MesrlineQFactorMax = _Pm200fr20MesrlineQFactorMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 234),
    _Pm200fr20MesrlineQFactorMax_Type()
)
pm200fr20MesrlineQFactorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineQFactorMax.setStatus("current")


class _Pm200fr20MesrlineCarrierFreqOffsetMax_Type(Unsigned32):
    """Custom type pm200fr20MesrlineCarrierFreqOffsetMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrlineCarrierFreqOffsetMax_Type.__name__ = "Unsigned32"
_Pm200fr20MesrlineCarrierFreqOffsetMax_Object = MibScalar
pm200fr20MesrlineCarrierFreqOffsetMax = _Pm200fr20MesrlineCarrierFreqOffsetMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 235),
    _Pm200fr20MesrlineCarrierFreqOffsetMax_Type()
)
pm200fr20MesrlineCarrierFreqOffsetMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineCarrierFreqOffsetMax.setStatus("current")


class _Pm200fr20MesrlineOsnrMax_Type(Unsigned32):
    """Custom type pm200fr20MesrlineOsnrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrlineOsnrMax_Type.__name__ = "Unsigned32"
_Pm200fr20MesrlineOsnrMax_Object = MibScalar
pm200fr20MesrlineOsnrMax = _Pm200fr20MesrlineOsnrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 236),
    _Pm200fr20MesrlineOsnrMax_Type()
)
pm200fr20MesrlineOsnrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineOsnrMax.setStatus("current")


class _Pm200fr20MesrlineTrscvTemp_Type(Unsigned32):
    """Custom type pm200fr20MesrlineTrscvTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrlineTrscvTemp_Type.__name__ = "Unsigned32"
_Pm200fr20MesrlineTrscvTemp_Object = MibScalar
pm200fr20MesrlineTrscvTemp = _Pm200fr20MesrlineTrscvTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 400),
    _Pm200fr20MesrlineTrscvTemp_Type()
)
pm200fr20MesrlineTrscvTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineTrscvTemp.setStatus("current")


class _Pm200fr20MesrlineTrscvVoltage_Type(Unsigned32):
    """Custom type pm200fr20MesrlineTrscvVoltage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrlineTrscvVoltage_Type.__name__ = "Unsigned32"
_Pm200fr20MesrlineTrscvVoltage_Object = MibScalar
pm200fr20MesrlineTrscvVoltage = _Pm200fr20MesrlineTrscvVoltage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 1, 408),
    _Pm200fr20MesrlineTrscvVoltage_Type()
)
pm200fr20MesrlineTrscvVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineTrscvVoltage.setStatus("current")
_Pm200fr20MesrClient_ObjectIdentity = ObjectIdentity
pm200fr20MesrClient = _Pm200fr20MesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 2)
)
_Pm200fr20MesrclientTxTempTable_Object = MibTable
pm200fr20MesrclientTxTempTable = _Pm200fr20MesrclientTxTempTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 2, 16)
)
if mibBuilder.loadTexts:
    pm200fr20MesrclientTxTempTable.setStatus("current")
_Pm200fr20MesrclientTxTempEntry_Object = MibTableRow
pm200fr20MesrclientTxTempEntry = _Pm200fr20MesrclientTxTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 2, 16, 1)
)
pm200fr20MesrclientTxTempEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20MesrclientTxTempIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20MesrclientTxTempEntry.setStatus("current")


class _Pm200fr20MesrclientTxTempIndex_Type(Integer32):
    """Custom type pm200fr20MesrclientTxTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20MesrclientTxTempIndex_Type.__name__ = "Integer32"
_Pm200fr20MesrclientTxTempIndex_Object = MibTableColumn
pm200fr20MesrclientTxTempIndex = _Pm200fr20MesrclientTxTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 2, 16, 1, 1),
    _Pm200fr20MesrclientTxTempIndex_Type()
)
pm200fr20MesrclientTxTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrclientTxTempIndex.setStatus("current")


class _Pm200fr20MesrclientTxTempPortn_Type(Integer32):
    """Custom type pm200fr20MesrclientTxTempPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrclientTxTempPortn_Type.__name__ = "Integer32"
_Pm200fr20MesrclientTxTempPortn_Object = MibTableColumn
pm200fr20MesrclientTxTempPortn = _Pm200fr20MesrclientTxTempPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 2, 16, 1, 2),
    _Pm200fr20MesrclientTxTempPortn_Type()
)
pm200fr20MesrclientTxTempPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrclientTxTempPortn.setStatus("current")
_Pm200fr20MesrclientTxBiasTable_Object = MibTable
pm200fr20MesrclientTxBiasTable = _Pm200fr20MesrclientTxBiasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 2, 48)
)
if mibBuilder.loadTexts:
    pm200fr20MesrclientTxBiasTable.setStatus("current")
_Pm200fr20MesrclientTxBiasEntry_Object = MibTableRow
pm200fr20MesrclientTxBiasEntry = _Pm200fr20MesrclientTxBiasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 2, 48, 1)
)
pm200fr20MesrclientTxBiasEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20MesrclientTxBiasIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20MesrclientTxBiasEntry.setStatus("current")


class _Pm200fr20MesrclientTxBiasIndex_Type(Integer32):
    """Custom type pm200fr20MesrclientTxBiasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20MesrclientTxBiasIndex_Type.__name__ = "Integer32"
_Pm200fr20MesrclientTxBiasIndex_Object = MibTableColumn
pm200fr20MesrclientTxBiasIndex = _Pm200fr20MesrclientTxBiasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 2, 48, 1, 1),
    _Pm200fr20MesrclientTxBiasIndex_Type()
)
pm200fr20MesrclientTxBiasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrclientTxBiasIndex.setStatus("current")


class _Pm200fr20MesrclientTxBiasPortn_Type(Integer32):
    """Custom type pm200fr20MesrclientTxBiasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrclientTxBiasPortn_Type.__name__ = "Integer32"
_Pm200fr20MesrclientTxBiasPortn_Object = MibTableColumn
pm200fr20MesrclientTxBiasPortn = _Pm200fr20MesrclientTxBiasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 2, 48, 1, 2),
    _Pm200fr20MesrclientTxBiasPortn_Type()
)
pm200fr20MesrclientTxBiasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrclientTxBiasPortn.setStatus("current")
_Pm200fr20MesrclientTxPwrTable_Object = MibTable
pm200fr20MesrclientTxPwrTable = _Pm200fr20MesrclientTxPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 2, 80)
)
if mibBuilder.loadTexts:
    pm200fr20MesrclientTxPwrTable.setStatus("current")
_Pm200fr20MesrclientTxPwrEntry_Object = MibTableRow
pm200fr20MesrclientTxPwrEntry = _Pm200fr20MesrclientTxPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 2, 80, 1)
)
pm200fr20MesrclientTxPwrEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20MesrclientTxPwrIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20MesrclientTxPwrEntry.setStatus("current")


class _Pm200fr20MesrclientTxPwrIndex_Type(Integer32):
    """Custom type pm200fr20MesrclientTxPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20MesrclientTxPwrIndex_Type.__name__ = "Integer32"
_Pm200fr20MesrclientTxPwrIndex_Object = MibTableColumn
pm200fr20MesrclientTxPwrIndex = _Pm200fr20MesrclientTxPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 2, 80, 1, 1),
    _Pm200fr20MesrclientTxPwrIndex_Type()
)
pm200fr20MesrclientTxPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrclientTxPwrIndex.setStatus("current")


class _Pm200fr20MesrclientTxPwrPortn_Type(Integer32):
    """Custom type pm200fr20MesrclientTxPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrclientTxPwrPortn_Type.__name__ = "Integer32"
_Pm200fr20MesrclientTxPwrPortn_Object = MibTableColumn
pm200fr20MesrclientTxPwrPortn = _Pm200fr20MesrclientTxPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 2, 80, 1, 2),
    _Pm200fr20MesrclientTxPwrPortn_Type()
)
pm200fr20MesrclientTxPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrclientTxPwrPortn.setStatus("current")
_Pm200fr20MesrclientRxPwrTable_Object = MibTable
pm200fr20MesrclientRxPwrTable = _Pm200fr20MesrclientRxPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 2, 112)
)
if mibBuilder.loadTexts:
    pm200fr20MesrclientRxPwrTable.setStatus("current")
_Pm200fr20MesrclientRxPwrEntry_Object = MibTableRow
pm200fr20MesrclientRxPwrEntry = _Pm200fr20MesrclientRxPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 2, 112, 1)
)
pm200fr20MesrclientRxPwrEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20MesrclientRxPwrIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20MesrclientRxPwrEntry.setStatus("current")


class _Pm200fr20MesrclientRxPwrIndex_Type(Integer32):
    """Custom type pm200fr20MesrclientRxPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20MesrclientRxPwrIndex_Type.__name__ = "Integer32"
_Pm200fr20MesrclientRxPwrIndex_Object = MibTableColumn
pm200fr20MesrclientRxPwrIndex = _Pm200fr20MesrclientRxPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 2, 112, 1, 1),
    _Pm200fr20MesrclientRxPwrIndex_Type()
)
pm200fr20MesrclientRxPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrclientRxPwrIndex.setStatus("current")


class _Pm200fr20MesrclientRxPwrPortn_Type(Integer32):
    """Custom type pm200fr20MesrclientRxPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrclientRxPwrPortn_Type.__name__ = "Integer32"
_Pm200fr20MesrclientRxPwrPortn_Object = MibTableColumn
pm200fr20MesrclientRxPwrPortn = _Pm200fr20MesrclientRxPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 2, 112, 1, 2),
    _Pm200fr20MesrclientRxPwrPortn_Type()
)
pm200fr20MesrclientRxPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrclientRxPwrPortn.setStatus("current")
_Pm200fr20MesrLine_ObjectIdentity = ObjectIdentity
pm200fr20MesrLine = _Pm200fr20MesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 3)
)
_Pm200fr20MesrlineNetTxLaserOutputPwrTable_Object = MibTable
pm200fr20MesrlineNetTxLaserOutputPwrTable = _Pm200fr20MesrlineNetTxLaserOutputPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 3, 144)
)
if mibBuilder.loadTexts:
    pm200fr20MesrlineNetTxLaserOutputPwrTable.setStatus("current")
_Pm200fr20MesrlineNetTxLaserOutputPwrEntry_Object = MibTableRow
pm200fr20MesrlineNetTxLaserOutputPwrEntry = _Pm200fr20MesrlineNetTxLaserOutputPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 3, 144, 1)
)
pm200fr20MesrlineNetTxLaserOutputPwrEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20MesrlineNetTxLaserOutputPwrIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20MesrlineNetTxLaserOutputPwrEntry.setStatus("current")


class _Pm200fr20MesrlineNetTxLaserOutputPwrIndex_Type(Integer32):
    """Custom type pm200fr20MesrlineNetTxLaserOutputPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20MesrlineNetTxLaserOutputPwrIndex_Type.__name__ = "Integer32"
_Pm200fr20MesrlineNetTxLaserOutputPwrIndex_Object = MibTableColumn
pm200fr20MesrlineNetTxLaserOutputPwrIndex = _Pm200fr20MesrlineNetTxLaserOutputPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 3, 144, 1, 1),
    _Pm200fr20MesrlineNetTxLaserOutputPwrIndex_Type()
)
pm200fr20MesrlineNetTxLaserOutputPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineNetTxLaserOutputPwrIndex.setStatus("current")


class _Pm200fr20MesrlineNetTxLaserOutputPwrPortn_Type(Integer32):
    """Custom type pm200fr20MesrlineNetTxLaserOutputPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrlineNetTxLaserOutputPwrPortn_Type.__name__ = "Integer32"
_Pm200fr20MesrlineNetTxLaserOutputPwrPortn_Object = MibTableColumn
pm200fr20MesrlineNetTxLaserOutputPwrPortn = _Pm200fr20MesrlineNetTxLaserOutputPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 3, 144, 1, 2),
    _Pm200fr20MesrlineNetTxLaserOutputPwrPortn_Type()
)
pm200fr20MesrlineNetTxLaserOutputPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineNetTxLaserOutputPwrPortn.setStatus("current")
_Pm200fr20MesrlineNetTxLaserTempTable_Object = MibTable
pm200fr20MesrlineNetTxLaserTempTable = _Pm200fr20MesrlineNetTxLaserTempTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 3, 148)
)
if mibBuilder.loadTexts:
    pm200fr20MesrlineNetTxLaserTempTable.setStatus("current")
_Pm200fr20MesrlineNetTxLaserTempEntry_Object = MibTableRow
pm200fr20MesrlineNetTxLaserTempEntry = _Pm200fr20MesrlineNetTxLaserTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 3, 148, 1)
)
pm200fr20MesrlineNetTxLaserTempEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20MesrlineNetTxLaserTempIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20MesrlineNetTxLaserTempEntry.setStatus("current")


class _Pm200fr20MesrlineNetTxLaserTempIndex_Type(Integer32):
    """Custom type pm200fr20MesrlineNetTxLaserTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20MesrlineNetTxLaserTempIndex_Type.__name__ = "Integer32"
_Pm200fr20MesrlineNetTxLaserTempIndex_Object = MibTableColumn
pm200fr20MesrlineNetTxLaserTempIndex = _Pm200fr20MesrlineNetTxLaserTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 3, 148, 1, 1),
    _Pm200fr20MesrlineNetTxLaserTempIndex_Type()
)
pm200fr20MesrlineNetTxLaserTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineNetTxLaserTempIndex.setStatus("current")


class _Pm200fr20MesrlineNetTxLaserTempPortn_Type(Integer32):
    """Custom type pm200fr20MesrlineNetTxLaserTempPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrlineNetTxLaserTempPortn_Type.__name__ = "Integer32"
_Pm200fr20MesrlineNetTxLaserTempPortn_Object = MibTableColumn
pm200fr20MesrlineNetTxLaserTempPortn = _Pm200fr20MesrlineNetTxLaserTempPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 3, 148, 1, 2),
    _Pm200fr20MesrlineNetTxLaserTempPortn_Type()
)
pm200fr20MesrlineNetTxLaserTempPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineNetTxLaserTempPortn.setStatus("current")
_Pm200fr20MesrlineNetTxBiasCurrentTable_Object = MibTable
pm200fr20MesrlineNetTxBiasCurrentTable = _Pm200fr20MesrlineNetTxBiasCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 3, 152)
)
if mibBuilder.loadTexts:
    pm200fr20MesrlineNetTxBiasCurrentTable.setStatus("current")
_Pm200fr20MesrlineNetTxBiasCurrentEntry_Object = MibTableRow
pm200fr20MesrlineNetTxBiasCurrentEntry = _Pm200fr20MesrlineNetTxBiasCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 3, 152, 1)
)
pm200fr20MesrlineNetTxBiasCurrentEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20MesrlineNetTxBiasCurrentIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20MesrlineNetTxBiasCurrentEntry.setStatus("current")


class _Pm200fr20MesrlineNetTxBiasCurrentIndex_Type(Integer32):
    """Custom type pm200fr20MesrlineNetTxBiasCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20MesrlineNetTxBiasCurrentIndex_Type.__name__ = "Integer32"
_Pm200fr20MesrlineNetTxBiasCurrentIndex_Object = MibTableColumn
pm200fr20MesrlineNetTxBiasCurrentIndex = _Pm200fr20MesrlineNetTxBiasCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 3, 152, 1, 1),
    _Pm200fr20MesrlineNetTxBiasCurrentIndex_Type()
)
pm200fr20MesrlineNetTxBiasCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineNetTxBiasCurrentIndex.setStatus("current")


class _Pm200fr20MesrlineNetTxBiasCurrentPortn_Type(Integer32):
    """Custom type pm200fr20MesrlineNetTxBiasCurrentPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrlineNetTxBiasCurrentPortn_Type.__name__ = "Integer32"
_Pm200fr20MesrlineNetTxBiasCurrentPortn_Object = MibTableColumn
pm200fr20MesrlineNetTxBiasCurrentPortn = _Pm200fr20MesrlineNetTxBiasCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 3, 152, 1, 2),
    _Pm200fr20MesrlineNetTxBiasCurrentPortn_Type()
)
pm200fr20MesrlineNetTxBiasCurrentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineNetTxBiasCurrentPortn.setStatus("current")
_Pm200fr20MesrlineNetRxInputPwrTable_Object = MibTable
pm200fr20MesrlineNetRxInputPwrTable = _Pm200fr20MesrlineNetRxInputPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 3, 156)
)
if mibBuilder.loadTexts:
    pm200fr20MesrlineNetRxInputPwrTable.setStatus("current")
_Pm200fr20MesrlineNetRxInputPwrEntry_Object = MibTableRow
pm200fr20MesrlineNetRxInputPwrEntry = _Pm200fr20MesrlineNetRxInputPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 3, 156, 1)
)
pm200fr20MesrlineNetRxInputPwrEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20MesrlineNetRxInputPwrIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20MesrlineNetRxInputPwrEntry.setStatus("current")


class _Pm200fr20MesrlineNetRxInputPwrIndex_Type(Integer32):
    """Custom type pm200fr20MesrlineNetRxInputPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20MesrlineNetRxInputPwrIndex_Type.__name__ = "Integer32"
_Pm200fr20MesrlineNetRxInputPwrIndex_Object = MibTableColumn
pm200fr20MesrlineNetRxInputPwrIndex = _Pm200fr20MesrlineNetRxInputPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 3, 156, 1, 1),
    _Pm200fr20MesrlineNetRxInputPwrIndex_Type()
)
pm200fr20MesrlineNetRxInputPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineNetRxInputPwrIndex.setStatus("current")


class _Pm200fr20MesrlineNetRxInputPwrPortn_Type(Integer32):
    """Custom type pm200fr20MesrlineNetRxInputPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrlineNetRxInputPwrPortn_Type.__name__ = "Integer32"
_Pm200fr20MesrlineNetRxInputPwrPortn_Object = MibTableColumn
pm200fr20MesrlineNetRxInputPwrPortn = _Pm200fr20MesrlineNetRxInputPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 3, 156, 1, 2),
    _Pm200fr20MesrlineNetRxInputPwrPortn_Type()
)
pm200fr20MesrlineNetRxInputPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineNetRxInputPwrPortn.setStatus("current")
_Pm200fr20MesrlineResidualChromaticDispTable_Object = MibTable
pm200fr20MesrlineResidualChromaticDispTable = _Pm200fr20MesrlineResidualChromaticDispTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 3, 160)
)
if mibBuilder.loadTexts:
    pm200fr20MesrlineResidualChromaticDispTable.setStatus("current")
_Pm200fr20MesrlineResidualChromaticDispEntry_Object = MibTableRow
pm200fr20MesrlineResidualChromaticDispEntry = _Pm200fr20MesrlineResidualChromaticDispEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 3, 160, 1)
)
pm200fr20MesrlineResidualChromaticDispEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20MesrlineResidualChromaticDispIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20MesrlineResidualChromaticDispEntry.setStatus("current")


class _Pm200fr20MesrlineResidualChromaticDispIndex_Type(Integer32):
    """Custom type pm200fr20MesrlineResidualChromaticDispIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20MesrlineResidualChromaticDispIndex_Type.__name__ = "Integer32"
_Pm200fr20MesrlineResidualChromaticDispIndex_Object = MibTableColumn
pm200fr20MesrlineResidualChromaticDispIndex = _Pm200fr20MesrlineResidualChromaticDispIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 3, 160, 1, 1),
    _Pm200fr20MesrlineResidualChromaticDispIndex_Type()
)
pm200fr20MesrlineResidualChromaticDispIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineResidualChromaticDispIndex.setStatus("current")


class _Pm200fr20MesrlineResidualChromaticDispPortn_Type(Integer32):
    """Custom type pm200fr20MesrlineResidualChromaticDispPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrlineResidualChromaticDispPortn_Type.__name__ = "Integer32"
_Pm200fr20MesrlineResidualChromaticDispPortn_Object = MibTableColumn
pm200fr20MesrlineResidualChromaticDispPortn = _Pm200fr20MesrlineResidualChromaticDispPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 3, 160, 1, 2),
    _Pm200fr20MesrlineResidualChromaticDispPortn_Type()
)
pm200fr20MesrlineResidualChromaticDispPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineResidualChromaticDispPortn.setStatus("current")
_Pm200fr20MesrlineDiffGroupDelayTable_Object = MibTable
pm200fr20MesrlineDiffGroupDelayTable = _Pm200fr20MesrlineDiffGroupDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 3, 164)
)
if mibBuilder.loadTexts:
    pm200fr20MesrlineDiffGroupDelayTable.setStatus("current")
_Pm200fr20MesrlineDiffGroupDelayEntry_Object = MibTableRow
pm200fr20MesrlineDiffGroupDelayEntry = _Pm200fr20MesrlineDiffGroupDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 3, 164, 1)
)
pm200fr20MesrlineDiffGroupDelayEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20MesrlineDiffGroupDelayIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20MesrlineDiffGroupDelayEntry.setStatus("current")


class _Pm200fr20MesrlineDiffGroupDelayIndex_Type(Integer32):
    """Custom type pm200fr20MesrlineDiffGroupDelayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20MesrlineDiffGroupDelayIndex_Type.__name__ = "Integer32"
_Pm200fr20MesrlineDiffGroupDelayIndex_Object = MibTableColumn
pm200fr20MesrlineDiffGroupDelayIndex = _Pm200fr20MesrlineDiffGroupDelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 3, 164, 1, 1),
    _Pm200fr20MesrlineDiffGroupDelayIndex_Type()
)
pm200fr20MesrlineDiffGroupDelayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineDiffGroupDelayIndex.setStatus("current")


class _Pm200fr20MesrlineDiffGroupDelayPortn_Type(Integer32):
    """Custom type pm200fr20MesrlineDiffGroupDelayPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrlineDiffGroupDelayPortn_Type.__name__ = "Integer32"
_Pm200fr20MesrlineDiffGroupDelayPortn_Object = MibTableColumn
pm200fr20MesrlineDiffGroupDelayPortn = _Pm200fr20MesrlineDiffGroupDelayPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 3, 164, 1, 2),
    _Pm200fr20MesrlineDiffGroupDelayPortn_Type()
)
pm200fr20MesrlineDiffGroupDelayPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineDiffGroupDelayPortn.setStatus("current")
_Pm200fr20MesrlineQFactorTable_Object = MibTable
pm200fr20MesrlineQFactorTable = _Pm200fr20MesrlineQFactorTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 3, 168)
)
if mibBuilder.loadTexts:
    pm200fr20MesrlineQFactorTable.setStatus("current")
_Pm200fr20MesrlineQFactorEntry_Object = MibTableRow
pm200fr20MesrlineQFactorEntry = _Pm200fr20MesrlineQFactorEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 3, 168, 1)
)
pm200fr20MesrlineQFactorEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20MesrlineQFactorIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20MesrlineQFactorEntry.setStatus("current")


class _Pm200fr20MesrlineQFactorIndex_Type(Integer32):
    """Custom type pm200fr20MesrlineQFactorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20MesrlineQFactorIndex_Type.__name__ = "Integer32"
_Pm200fr20MesrlineQFactorIndex_Object = MibTableColumn
pm200fr20MesrlineQFactorIndex = _Pm200fr20MesrlineQFactorIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 3, 168, 1, 1),
    _Pm200fr20MesrlineQFactorIndex_Type()
)
pm200fr20MesrlineQFactorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineQFactorIndex.setStatus("current")


class _Pm200fr20MesrlineQFactorPortn_Type(Integer32):
    """Custom type pm200fr20MesrlineQFactorPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrlineQFactorPortn_Type.__name__ = "Integer32"
_Pm200fr20MesrlineQFactorPortn_Object = MibTableColumn
pm200fr20MesrlineQFactorPortn = _Pm200fr20MesrlineQFactorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 3, 168, 1, 2),
    _Pm200fr20MesrlineQFactorPortn_Type()
)
pm200fr20MesrlineQFactorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineQFactorPortn.setStatus("current")
_Pm200fr20MesrlineCarrierFreqOffsetTable_Object = MibTable
pm200fr20MesrlineCarrierFreqOffsetTable = _Pm200fr20MesrlineCarrierFreqOffsetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 3, 172)
)
if mibBuilder.loadTexts:
    pm200fr20MesrlineCarrierFreqOffsetTable.setStatus("current")
_Pm200fr20MesrlineCarrierFreqOffsetEntry_Object = MibTableRow
pm200fr20MesrlineCarrierFreqOffsetEntry = _Pm200fr20MesrlineCarrierFreqOffsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 3, 172, 1)
)
pm200fr20MesrlineCarrierFreqOffsetEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20MesrlineCarrierFreqOffsetIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20MesrlineCarrierFreqOffsetEntry.setStatus("current")


class _Pm200fr20MesrlineCarrierFreqOffsetIndex_Type(Integer32):
    """Custom type pm200fr20MesrlineCarrierFreqOffsetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20MesrlineCarrierFreqOffsetIndex_Type.__name__ = "Integer32"
_Pm200fr20MesrlineCarrierFreqOffsetIndex_Object = MibTableColumn
pm200fr20MesrlineCarrierFreqOffsetIndex = _Pm200fr20MesrlineCarrierFreqOffsetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 3, 172, 1, 1),
    _Pm200fr20MesrlineCarrierFreqOffsetIndex_Type()
)
pm200fr20MesrlineCarrierFreqOffsetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineCarrierFreqOffsetIndex.setStatus("current")


class _Pm200fr20MesrlineCarrierFreqOffsetPortn_Type(Integer32):
    """Custom type pm200fr20MesrlineCarrierFreqOffsetPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrlineCarrierFreqOffsetPortn_Type.__name__ = "Integer32"
_Pm200fr20MesrlineCarrierFreqOffsetPortn_Object = MibTableColumn
pm200fr20MesrlineCarrierFreqOffsetPortn = _Pm200fr20MesrlineCarrierFreqOffsetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 3, 172, 1, 2),
    _Pm200fr20MesrlineCarrierFreqOffsetPortn_Type()
)
pm200fr20MesrlineCarrierFreqOffsetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineCarrierFreqOffsetPortn.setStatus("current")
_Pm200fr20MesrlineOsnrTable_Object = MibTable
pm200fr20MesrlineOsnrTable = _Pm200fr20MesrlineOsnrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 3, 176)
)
if mibBuilder.loadTexts:
    pm200fr20MesrlineOsnrTable.setStatus("current")
_Pm200fr20MesrlineOsnrEntry_Object = MibTableRow
pm200fr20MesrlineOsnrEntry = _Pm200fr20MesrlineOsnrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 3, 176, 1)
)
pm200fr20MesrlineOsnrEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20MesrlineOsnrIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20MesrlineOsnrEntry.setStatus("current")


class _Pm200fr20MesrlineOsnrIndex_Type(Integer32):
    """Custom type pm200fr20MesrlineOsnrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20MesrlineOsnrIndex_Type.__name__ = "Integer32"
_Pm200fr20MesrlineOsnrIndex_Object = MibTableColumn
pm200fr20MesrlineOsnrIndex = _Pm200fr20MesrlineOsnrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 3, 176, 1, 1),
    _Pm200fr20MesrlineOsnrIndex_Type()
)
pm200fr20MesrlineOsnrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineOsnrIndex.setStatus("current")


class _Pm200fr20MesrlineOsnrPortn_Type(Integer32):
    """Custom type pm200fr20MesrlineOsnrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200fr20MesrlineOsnrPortn_Type.__name__ = "Integer32"
_Pm200fr20MesrlineOsnrPortn_Object = MibTableColumn
pm200fr20MesrlineOsnrPortn = _Pm200fr20MesrlineOsnrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 3, 3, 176, 1, 2),
    _Pm200fr20MesrlineOsnrPortn_Type()
)
pm200fr20MesrlineOsnrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MesrlineOsnrPortn.setStatus("current")
_Pm200fr20counters_ObjectIdentity = ObjectIdentity
pm200fr20counters = _Pm200fr20counters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4)
)
_Pm200fr20CntOther_ObjectIdentity = ObjectIdentity
pm200fr20CntOther = _Pm200fr20CntOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 1)
)
_Pm200fr20CntClient_ObjectIdentity = ObjectIdentity
pm200fr20CntClient = _Pm200fr20CntClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 2)
)
_Pm200fr20CntclientInputErrorCounterTable_Object = MibTable
pm200fr20CntclientInputErrorCounterTable = _Pm200fr20CntclientInputErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 2, 112)
)
if mibBuilder.loadTexts:
    pm200fr20CntclientInputErrorCounterTable.setStatus("current")
_Pm200fr20CntclientInputErrorCounterEntry_Object = MibTableRow
pm200fr20CntclientInputErrorCounterEntry = _Pm200fr20CntclientInputErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 2, 112, 1)
)
pm200fr20CntclientInputErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20CntclientInputErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20CntclientInputErrorCounterEntry.setStatus("current")


class _Pm200fr20CntclientInputErrorCounterIndex_Type(Integer32):
    """Custom type pm200fr20CntclientInputErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20CntclientInputErrorCounterIndex_Type.__name__ = "Integer32"
_Pm200fr20CntclientInputErrorCounterIndex_Object = MibTableColumn
pm200fr20CntclientInputErrorCounterIndex = _Pm200fr20CntclientInputErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 2, 112, 1, 1),
    _Pm200fr20CntclientInputErrorCounterIndex_Type()
)
pm200fr20CntclientInputErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntclientInputErrorCounterIndex.setStatus("current")
_Pm200fr20CntclientInputErrorCounterValuePortn_Type = Counter32
_Pm200fr20CntclientInputErrorCounterValuePortn_Object = MibTableColumn
pm200fr20CntclientInputErrorCounterValuePortn = _Pm200fr20CntclientInputErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 2, 112, 1, 2),
    _Pm200fr20CntclientInputErrorCounterValuePortn_Type()
)
pm200fr20CntclientInputErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntclientInputErrorCounterValuePortn.setStatus("current")
_Pm200fr20CntclientInputErrorCounterErrorPortn_Type = EkiOnOff
_Pm200fr20CntclientInputErrorCounterErrorPortn_Object = MibTableColumn
pm200fr20CntclientInputErrorCounterErrorPortn = _Pm200fr20CntclientInputErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 2, 112, 1, 3),
    _Pm200fr20CntclientInputErrorCounterErrorPortn_Type()
)
pm200fr20CntclientInputErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntclientInputErrorCounterErrorPortn.setStatus("current")
_Pm200fr20CntclientInputErrorCounterOverloadPortn_Type = EkiOnOff
_Pm200fr20CntclientInputErrorCounterOverloadPortn_Object = MibTableColumn
pm200fr20CntclientInputErrorCounterOverloadPortn = _Pm200fr20CntclientInputErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 2, 112, 1, 4),
    _Pm200fr20CntclientInputErrorCounterOverloadPortn_Type()
)
pm200fr20CntclientInputErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntclientInputErrorCounterOverloadPortn.setStatus("current")
_Pm200fr20CntclientCbipCounterTable_Object = MibTable
pm200fr20CntclientCbipCounterTable = _Pm200fr20CntclientCbipCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 2, 144)
)
if mibBuilder.loadTexts:
    pm200fr20CntclientCbipCounterTable.setStatus("current")
_Pm200fr20CntclientCbipCounterEntry_Object = MibTableRow
pm200fr20CntclientCbipCounterEntry = _Pm200fr20CntclientCbipCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 2, 144, 1)
)
pm200fr20CntclientCbipCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20CntclientCbipCounterIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20CntclientCbipCounterEntry.setStatus("current")


class _Pm200fr20CntclientCbipCounterIndex_Type(Integer32):
    """Custom type pm200fr20CntclientCbipCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20CntclientCbipCounterIndex_Type.__name__ = "Integer32"
_Pm200fr20CntclientCbipCounterIndex_Object = MibTableColumn
pm200fr20CntclientCbipCounterIndex = _Pm200fr20CntclientCbipCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 2, 144, 1, 1),
    _Pm200fr20CntclientCbipCounterIndex_Type()
)
pm200fr20CntclientCbipCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntclientCbipCounterIndex.setStatus("current")
_Pm200fr20CntclientCbipCounterValuePortn_Type = Counter32
_Pm200fr20CntclientCbipCounterValuePortn_Object = MibTableColumn
pm200fr20CntclientCbipCounterValuePortn = _Pm200fr20CntclientCbipCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 2, 144, 1, 2),
    _Pm200fr20CntclientCbipCounterValuePortn_Type()
)
pm200fr20CntclientCbipCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntclientCbipCounterValuePortn.setStatus("current")
_Pm200fr20CntclientCbipCounterErrorPortn_Type = EkiOnOff
_Pm200fr20CntclientCbipCounterErrorPortn_Object = MibTableColumn
pm200fr20CntclientCbipCounterErrorPortn = _Pm200fr20CntclientCbipCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 2, 144, 1, 3),
    _Pm200fr20CntclientCbipCounterErrorPortn_Type()
)
pm200fr20CntclientCbipCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntclientCbipCounterErrorPortn.setStatus("current")
_Pm200fr20CntclientCbipCounterOverloadPortn_Type = EkiOnOff
_Pm200fr20CntclientCbipCounterOverloadPortn_Object = MibTableColumn
pm200fr20CntclientCbipCounterOverloadPortn = _Pm200fr20CntclientCbipCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 2, 144, 1, 4),
    _Pm200fr20CntclientCbipCounterOverloadPortn_Type()
)
pm200fr20CntclientCbipCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntclientCbipCounterOverloadPortn.setStatus("current")
_Pm200fr20CntLine_ObjectIdentity = ObjectIdentity
pm200fr20CntLine = _Pm200fr20CntLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3)
)
_Pm200fr20CntlocalLineSmBip8ErrorCounterTable_Object = MibTable
pm200fr20CntlocalLineSmBip8ErrorCounterTable = _Pm200fr20CntlocalLineSmBip8ErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 192)
)
if mibBuilder.loadTexts:
    pm200fr20CntlocalLineSmBip8ErrorCounterTable.setStatus("current")
_Pm200fr20CntlocalLineSmBip8ErrorCounterEntry_Object = MibTableRow
pm200fr20CntlocalLineSmBip8ErrorCounterEntry = _Pm200fr20CntlocalLineSmBip8ErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 192, 1)
)
pm200fr20CntlocalLineSmBip8ErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20CntlocalLineSmBip8ErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20CntlocalLineSmBip8ErrorCounterEntry.setStatus("current")


class _Pm200fr20CntlocalLineSmBip8ErrorCounterIndex_Type(Integer32):
    """Custom type pm200fr20CntlocalLineSmBip8ErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20CntlocalLineSmBip8ErrorCounterIndex_Type.__name__ = "Integer32"
_Pm200fr20CntlocalLineSmBip8ErrorCounterIndex_Object = MibTableColumn
pm200fr20CntlocalLineSmBip8ErrorCounterIndex = _Pm200fr20CntlocalLineSmBip8ErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 192, 1, 1),
    _Pm200fr20CntlocalLineSmBip8ErrorCounterIndex_Type()
)
pm200fr20CntlocalLineSmBip8ErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntlocalLineSmBip8ErrorCounterIndex.setStatus("current")
_Pm200fr20CntlocalLineSmBip8ErrorCounterValuePortn_Type = Counter64
_Pm200fr20CntlocalLineSmBip8ErrorCounterValuePortn_Object = MibTableColumn
pm200fr20CntlocalLineSmBip8ErrorCounterValuePortn = _Pm200fr20CntlocalLineSmBip8ErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 192, 1, 2),
    _Pm200fr20CntlocalLineSmBip8ErrorCounterValuePortn_Type()
)
pm200fr20CntlocalLineSmBip8ErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntlocalLineSmBip8ErrorCounterValuePortn.setStatus("current")
_Pm200fr20CntlocalLineSmBip8ErrorCounterErrorPortn_Type = EkiOnOff
_Pm200fr20CntlocalLineSmBip8ErrorCounterErrorPortn_Object = MibTableColumn
pm200fr20CntlocalLineSmBip8ErrorCounterErrorPortn = _Pm200fr20CntlocalLineSmBip8ErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 192, 1, 3),
    _Pm200fr20CntlocalLineSmBip8ErrorCounterErrorPortn_Type()
)
pm200fr20CntlocalLineSmBip8ErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntlocalLineSmBip8ErrorCounterErrorPortn.setStatus("current")
_Pm200fr20CntlocalLineSmBip8ErrorCounterOverloadPortn_Type = EkiOnOff
_Pm200fr20CntlocalLineSmBip8ErrorCounterOverloadPortn_Object = MibTableColumn
pm200fr20CntlocalLineSmBip8ErrorCounterOverloadPortn = _Pm200fr20CntlocalLineSmBip8ErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 192, 1, 4),
    _Pm200fr20CntlocalLineSmBip8ErrorCounterOverloadPortn_Type()
)
pm200fr20CntlocalLineSmBip8ErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntlocalLineSmBip8ErrorCounterOverloadPortn.setStatus("current")
_Pm200fr20CntlocalLineFecCorrectedErrorsCounterTable_Object = MibTable
pm200fr20CntlocalLineFecCorrectedErrorsCounterTable = _Pm200fr20CntlocalLineFecCorrectedErrorsCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 193)
)
if mibBuilder.loadTexts:
    pm200fr20CntlocalLineFecCorrectedErrorsCounterTable.setStatus("current")
_Pm200fr20CntlocalLineFecCorrectedErrorsCounterEntry_Object = MibTableRow
pm200fr20CntlocalLineFecCorrectedErrorsCounterEntry = _Pm200fr20CntlocalLineFecCorrectedErrorsCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 193, 1)
)
pm200fr20CntlocalLineFecCorrectedErrorsCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20CntlocalLineFecCorrectedErrorsCounterIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20CntlocalLineFecCorrectedErrorsCounterEntry.setStatus("current")


class _Pm200fr20CntlocalLineFecCorrectedErrorsCounterIndex_Type(Integer32):
    """Custom type pm200fr20CntlocalLineFecCorrectedErrorsCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20CntlocalLineFecCorrectedErrorsCounterIndex_Type.__name__ = "Integer32"
_Pm200fr20CntlocalLineFecCorrectedErrorsCounterIndex_Object = MibTableColumn
pm200fr20CntlocalLineFecCorrectedErrorsCounterIndex = _Pm200fr20CntlocalLineFecCorrectedErrorsCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 193, 1, 1),
    _Pm200fr20CntlocalLineFecCorrectedErrorsCounterIndex_Type()
)
pm200fr20CntlocalLineFecCorrectedErrorsCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntlocalLineFecCorrectedErrorsCounterIndex.setStatus("current")
_Pm200fr20CntlocalLineFecCorrectedErrorsCounterValuePortn_Type = Counter64
_Pm200fr20CntlocalLineFecCorrectedErrorsCounterValuePortn_Object = MibTableColumn
pm200fr20CntlocalLineFecCorrectedErrorsCounterValuePortn = _Pm200fr20CntlocalLineFecCorrectedErrorsCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 193, 1, 2),
    _Pm200fr20CntlocalLineFecCorrectedErrorsCounterValuePortn_Type()
)
pm200fr20CntlocalLineFecCorrectedErrorsCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntlocalLineFecCorrectedErrorsCounterValuePortn.setStatus("current")
_Pm200fr20CntlocalLineFecCorrectedErrorsCounterErrorPortn_Type = EkiOnOff
_Pm200fr20CntlocalLineFecCorrectedErrorsCounterErrorPortn_Object = MibTableColumn
pm200fr20CntlocalLineFecCorrectedErrorsCounterErrorPortn = _Pm200fr20CntlocalLineFecCorrectedErrorsCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 193, 1, 3),
    _Pm200fr20CntlocalLineFecCorrectedErrorsCounterErrorPortn_Type()
)
pm200fr20CntlocalLineFecCorrectedErrorsCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntlocalLineFecCorrectedErrorsCounterErrorPortn.setStatus("current")
_Pm200fr20CntlocalLineFecCorrectedErrorsCounterOverloadPortn_Type = EkiOnOff
_Pm200fr20CntlocalLineFecCorrectedErrorsCounterOverloadPortn_Object = MibTableColumn
pm200fr20CntlocalLineFecCorrectedErrorsCounterOverloadPortn = _Pm200fr20CntlocalLineFecCorrectedErrorsCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 193, 1, 4),
    _Pm200fr20CntlocalLineFecCorrectedErrorsCounterOverloadPortn_Type()
)
pm200fr20CntlocalLineFecCorrectedErrorsCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntlocalLineFecCorrectedErrorsCounterOverloadPortn.setStatus("current")
_Pm200fr20CntremoteLineSmBip8ErrorCounterTable_Object = MibTable
pm200fr20CntremoteLineSmBip8ErrorCounterTable = _Pm200fr20CntremoteLineSmBip8ErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 194)
)
if mibBuilder.loadTexts:
    pm200fr20CntremoteLineSmBip8ErrorCounterTable.setStatus("current")
_Pm200fr20CntremoteLineSmBip8ErrorCounterEntry_Object = MibTableRow
pm200fr20CntremoteLineSmBip8ErrorCounterEntry = _Pm200fr20CntremoteLineSmBip8ErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 194, 1)
)
pm200fr20CntremoteLineSmBip8ErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20CntremoteLineSmBip8ErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20CntremoteLineSmBip8ErrorCounterEntry.setStatus("current")


class _Pm200fr20CntremoteLineSmBip8ErrorCounterIndex_Type(Integer32):
    """Custom type pm200fr20CntremoteLineSmBip8ErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20CntremoteLineSmBip8ErrorCounterIndex_Type.__name__ = "Integer32"
_Pm200fr20CntremoteLineSmBip8ErrorCounterIndex_Object = MibTableColumn
pm200fr20CntremoteLineSmBip8ErrorCounterIndex = _Pm200fr20CntremoteLineSmBip8ErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 194, 1, 1),
    _Pm200fr20CntremoteLineSmBip8ErrorCounterIndex_Type()
)
pm200fr20CntremoteLineSmBip8ErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntremoteLineSmBip8ErrorCounterIndex.setStatus("current")
_Pm200fr20CntremoteLineSmBip8ErrorCounterValuePortn_Type = Counter64
_Pm200fr20CntremoteLineSmBip8ErrorCounterValuePortn_Object = MibTableColumn
pm200fr20CntremoteLineSmBip8ErrorCounterValuePortn = _Pm200fr20CntremoteLineSmBip8ErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 194, 1, 2),
    _Pm200fr20CntremoteLineSmBip8ErrorCounterValuePortn_Type()
)
pm200fr20CntremoteLineSmBip8ErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntremoteLineSmBip8ErrorCounterValuePortn.setStatus("current")
_Pm200fr20CntremoteLineSmBip8ErrorCounterErrorPortn_Type = EkiOnOff
_Pm200fr20CntremoteLineSmBip8ErrorCounterErrorPortn_Object = MibTableColumn
pm200fr20CntremoteLineSmBip8ErrorCounterErrorPortn = _Pm200fr20CntremoteLineSmBip8ErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 194, 1, 3),
    _Pm200fr20CntremoteLineSmBip8ErrorCounterErrorPortn_Type()
)
pm200fr20CntremoteLineSmBip8ErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntremoteLineSmBip8ErrorCounterErrorPortn.setStatus("current")
_Pm200fr20CntremoteLineSmBip8ErrorCounterOverloadPortn_Type = EkiOnOff
_Pm200fr20CntremoteLineSmBip8ErrorCounterOverloadPortn_Object = MibTableColumn
pm200fr20CntremoteLineSmBip8ErrorCounterOverloadPortn = _Pm200fr20CntremoteLineSmBip8ErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 194, 1, 4),
    _Pm200fr20CntremoteLineSmBip8ErrorCounterOverloadPortn_Type()
)
pm200fr20CntremoteLineSmBip8ErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntremoteLineSmBip8ErrorCounterOverloadPortn.setStatus("current")
_Pm200fr20CntlineDfrmTimCntTable_Object = MibTable
pm200fr20CntlineDfrmTimCntTable = _Pm200fr20CntlineDfrmTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 195)
)
if mibBuilder.loadTexts:
    pm200fr20CntlineDfrmTimCntTable.setStatus("current")
_Pm200fr20CntlineDfrmTimCntEntry_Object = MibTableRow
pm200fr20CntlineDfrmTimCntEntry = _Pm200fr20CntlineDfrmTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 195, 1)
)
pm200fr20CntlineDfrmTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20CntlineDfrmTimCntIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20CntlineDfrmTimCntEntry.setStatus("current")


class _Pm200fr20CntlineDfrmTimCntIndex_Type(Integer32):
    """Custom type pm200fr20CntlineDfrmTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20CntlineDfrmTimCntIndex_Type.__name__ = "Integer32"
_Pm200fr20CntlineDfrmTimCntIndex_Object = MibTableColumn
pm200fr20CntlineDfrmTimCntIndex = _Pm200fr20CntlineDfrmTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 195, 1, 1),
    _Pm200fr20CntlineDfrmTimCntIndex_Type()
)
pm200fr20CntlineDfrmTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntlineDfrmTimCntIndex.setStatus("current")
_Pm200fr20CntlineDfrmTimCntValuePortn_Type = Counter64
_Pm200fr20CntlineDfrmTimCntValuePortn_Object = MibTableColumn
pm200fr20CntlineDfrmTimCntValuePortn = _Pm200fr20CntlineDfrmTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 195, 1, 2),
    _Pm200fr20CntlineDfrmTimCntValuePortn_Type()
)
pm200fr20CntlineDfrmTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntlineDfrmTimCntValuePortn.setStatus("current")
_Pm200fr20CntlineDfrmTimCntErrorPortn_Type = EkiOnOff
_Pm200fr20CntlineDfrmTimCntErrorPortn_Object = MibTableColumn
pm200fr20CntlineDfrmTimCntErrorPortn = _Pm200fr20CntlineDfrmTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 195, 1, 3),
    _Pm200fr20CntlineDfrmTimCntErrorPortn_Type()
)
pm200fr20CntlineDfrmTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntlineDfrmTimCntErrorPortn.setStatus("current")
_Pm200fr20CntlineDfrmTimCntOverloadPortn_Type = EkiOnOff
_Pm200fr20CntlineDfrmTimCntOverloadPortn_Object = MibTableColumn
pm200fr20CntlineDfrmTimCntOverloadPortn = _Pm200fr20CntlineDfrmTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 195, 1, 4),
    _Pm200fr20CntlineDfrmTimCntOverloadPortn_Type()
)
pm200fr20CntlineDfrmTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntlineDfrmTimCntOverloadPortn.setStatus("current")
_Pm200fr20CntlocalLineTrscvPreSdFecErrorCounterTable_Object = MibTable
pm200fr20CntlocalLineTrscvPreSdFecErrorCounterTable = _Pm200fr20CntlocalLineTrscvPreSdFecErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 196)
)
if mibBuilder.loadTexts:
    pm200fr20CntlocalLineTrscvPreSdFecErrorCounterTable.setStatus("current")
_Pm200fr20CntlocalLineTrscvPreSdFecErrorCounterEntry_Object = MibTableRow
pm200fr20CntlocalLineTrscvPreSdFecErrorCounterEntry = _Pm200fr20CntlocalLineTrscvPreSdFecErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 196, 1)
)
pm200fr20CntlocalLineTrscvPreSdFecErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20CntlocalLineTrscvPreSdFecErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20CntlocalLineTrscvPreSdFecErrorCounterEntry.setStatus("current")


class _Pm200fr20CntlocalLineTrscvPreSdFecErrorCounterIndex_Type(Integer32):
    """Custom type pm200fr20CntlocalLineTrscvPreSdFecErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20CntlocalLineTrscvPreSdFecErrorCounterIndex_Type.__name__ = "Integer32"
_Pm200fr20CntlocalLineTrscvPreSdFecErrorCounterIndex_Object = MibTableColumn
pm200fr20CntlocalLineTrscvPreSdFecErrorCounterIndex = _Pm200fr20CntlocalLineTrscvPreSdFecErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 196, 1, 1),
    _Pm200fr20CntlocalLineTrscvPreSdFecErrorCounterIndex_Type()
)
pm200fr20CntlocalLineTrscvPreSdFecErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntlocalLineTrscvPreSdFecErrorCounterIndex.setStatus("current")
_Pm200fr20CntlocalLineTrscvPreSdFecErrorCounterValuePortn_Type = Counter64
_Pm200fr20CntlocalLineTrscvPreSdFecErrorCounterValuePortn_Object = MibTableColumn
pm200fr20CntlocalLineTrscvPreSdFecErrorCounterValuePortn = _Pm200fr20CntlocalLineTrscvPreSdFecErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 196, 1, 2),
    _Pm200fr20CntlocalLineTrscvPreSdFecErrorCounterValuePortn_Type()
)
pm200fr20CntlocalLineTrscvPreSdFecErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntlocalLineTrscvPreSdFecErrorCounterValuePortn.setStatus("current")
_Pm200fr20CntlocalLineTrscvPreSdFecErrorCounterErrorPortn_Type = EkiOnOff
_Pm200fr20CntlocalLineTrscvPreSdFecErrorCounterErrorPortn_Object = MibTableColumn
pm200fr20CntlocalLineTrscvPreSdFecErrorCounterErrorPortn = _Pm200fr20CntlocalLineTrscvPreSdFecErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 196, 1, 3),
    _Pm200fr20CntlocalLineTrscvPreSdFecErrorCounterErrorPortn_Type()
)
pm200fr20CntlocalLineTrscvPreSdFecErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntlocalLineTrscvPreSdFecErrorCounterErrorPortn.setStatus("current")
_Pm200fr20CntlocalLineTrscvPreSdFecErrorCounterOverloadPortn_Type = EkiOnOff
_Pm200fr20CntlocalLineTrscvPreSdFecErrorCounterOverloadPortn_Object = MibTableColumn
pm200fr20CntlocalLineTrscvPreSdFecErrorCounterOverloadPortn = _Pm200fr20CntlocalLineTrscvPreSdFecErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 196, 1, 4),
    _Pm200fr20CntlocalLineTrscvPreSdFecErrorCounterOverloadPortn_Type()
)
pm200fr20CntlocalLineTrscvPreSdFecErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntlocalLineTrscvPreSdFecErrorCounterOverloadPortn.setStatus("current")
_Pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterTable_Object = MibTable
pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterTable = _Pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 197)
)
if mibBuilder.loadTexts:
    pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterTable.setStatus("current")
_Pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterEntry_Object = MibTableRow
pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterEntry = _Pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 197, 1)
)
pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterEntry.setStatus("current")


class _Pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterIndex_Type(Integer32):
    """Custom type pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterIndex_Type.__name__ = "Integer32"
_Pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterIndex_Object = MibTableColumn
pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterIndex = _Pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 197, 1, 1),
    _Pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterIndex_Type()
)
pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterIndex.setStatus("current")
_Pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn_Type = Counter64
_Pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn_Object = MibTableColumn
pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn = _Pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 197, 1, 2),
    _Pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn_Type()
)
pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn.setStatus("current")
_Pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn_Type = EkiOnOff
_Pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn_Object = MibTableColumn
pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn = _Pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 197, 1, 3),
    _Pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn_Type()
)
pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn.setStatus("current")
_Pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn_Type = EkiOnOff
_Pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn_Object = MibTableColumn
pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn = _Pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 197, 1, 4),
    _Pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn_Type()
)
pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn.setStatus("current")
_Pm200fr20CntlocalLineTrscvPreSdFecBitCounterTable_Object = MibTable
pm200fr20CntlocalLineTrscvPreSdFecBitCounterTable = _Pm200fr20CntlocalLineTrscvPreSdFecBitCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 198)
)
if mibBuilder.loadTexts:
    pm200fr20CntlocalLineTrscvPreSdFecBitCounterTable.setStatus("current")
_Pm200fr20CntlocalLineTrscvPreSdFecBitCounterEntry_Object = MibTableRow
pm200fr20CntlocalLineTrscvPreSdFecBitCounterEntry = _Pm200fr20CntlocalLineTrscvPreSdFecBitCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 198, 1)
)
pm200fr20CntlocalLineTrscvPreSdFecBitCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20CntlocalLineTrscvPreSdFecBitCounterIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20CntlocalLineTrscvPreSdFecBitCounterEntry.setStatus("current")


class _Pm200fr20CntlocalLineTrscvPreSdFecBitCounterIndex_Type(Integer32):
    """Custom type pm200fr20CntlocalLineTrscvPreSdFecBitCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20CntlocalLineTrscvPreSdFecBitCounterIndex_Type.__name__ = "Integer32"
_Pm200fr20CntlocalLineTrscvPreSdFecBitCounterIndex_Object = MibTableColumn
pm200fr20CntlocalLineTrscvPreSdFecBitCounterIndex = _Pm200fr20CntlocalLineTrscvPreSdFecBitCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 198, 1, 1),
    _Pm200fr20CntlocalLineTrscvPreSdFecBitCounterIndex_Type()
)
pm200fr20CntlocalLineTrscvPreSdFecBitCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntlocalLineTrscvPreSdFecBitCounterIndex.setStatus("current")
_Pm200fr20CntlocalLineTrscvPreSdFecBitCounterValuePortn_Type = Counter64
_Pm200fr20CntlocalLineTrscvPreSdFecBitCounterValuePortn_Object = MibTableColumn
pm200fr20CntlocalLineTrscvPreSdFecBitCounterValuePortn = _Pm200fr20CntlocalLineTrscvPreSdFecBitCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 198, 1, 2),
    _Pm200fr20CntlocalLineTrscvPreSdFecBitCounterValuePortn_Type()
)
pm200fr20CntlocalLineTrscvPreSdFecBitCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntlocalLineTrscvPreSdFecBitCounterValuePortn.setStatus("current")
_Pm200fr20CntlocalLineTrscvPreSdFecBitCounterErrorPortn_Type = EkiOnOff
_Pm200fr20CntlocalLineTrscvPreSdFecBitCounterErrorPortn_Object = MibTableColumn
pm200fr20CntlocalLineTrscvPreSdFecBitCounterErrorPortn = _Pm200fr20CntlocalLineTrscvPreSdFecBitCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 198, 1, 3),
    _Pm200fr20CntlocalLineTrscvPreSdFecBitCounterErrorPortn_Type()
)
pm200fr20CntlocalLineTrscvPreSdFecBitCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntlocalLineTrscvPreSdFecBitCounterErrorPortn.setStatus("current")
_Pm200fr20CntlocalLineTrscvPreSdFecBitCounterOverloadPortn_Type = EkiOnOff
_Pm200fr20CntlocalLineTrscvPreSdFecBitCounterOverloadPortn_Object = MibTableColumn
pm200fr20CntlocalLineTrscvPreSdFecBitCounterOverloadPortn = _Pm200fr20CntlocalLineTrscvPreSdFecBitCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 198, 1, 4),
    _Pm200fr20CntlocalLineTrscvPreSdFecBitCounterOverloadPortn_Type()
)
pm200fr20CntlocalLineTrscvPreSdFecBitCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntlocalLineTrscvPreSdFecBitCounterOverloadPortn.setStatus("current")
_Pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterTable_Object = MibTable
pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterTable = _Pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 199)
)
if mibBuilder.loadTexts:
    pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterTable.setStatus("current")
_Pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterEntry_Object = MibTableRow
pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterEntry = _Pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 199, 1)
)
pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterEntry.setStatus("current")


class _Pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterIndex_Type(Integer32):
    """Custom type pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterIndex_Type.__name__ = "Integer32"
_Pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterIndex_Object = MibTableColumn
pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterIndex = _Pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 199, 1, 1),
    _Pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterIndex_Type()
)
pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterIndex.setStatus("current")
_Pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn_Type = Counter64
_Pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn_Object = MibTableColumn
pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn = _Pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 199, 1, 2),
    _Pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn_Type()
)
pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn.setStatus("current")
_Pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn_Type = EkiOnOff
_Pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn_Object = MibTableColumn
pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn = _Pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 199, 1, 3),
    _Pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn_Type()
)
pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn.setStatus("current")
_Pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn_Type = EkiOnOff
_Pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn_Object = MibTableColumn
pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn = _Pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 4, 3, 199, 1, 4),
    _Pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn_Type()
)
pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn.setStatus("current")
_Pm200fr20controlsWrite_ObjectIdentity = ObjectIdentity
pm200fr20controlsWrite = _Pm200fr20controlsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6)
)
_Pm200fr20CtrlOther_ObjectIdentity = ObjectIdentity
pm200fr20CtrlOther = _Pm200fr20CtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 1)
)
_Pm200fr20CtrlconfMgnt1_ObjectIdentity = ObjectIdentity
pm200fr20CtrlconfMgnt1 = _Pm200fr20CtrlconfMgnt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 1, 1)
)
_Pm200fr20CtrlConf1Load1_Type = EkiOnOff
_Pm200fr20CtrlConf1Load1_Object = MibScalar
pm200fr20CtrlConf1Load1 = _Pm200fr20CtrlConf1Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 1, 1, 1),
    _Pm200fr20CtrlConf1Load1_Type()
)
pm200fr20CtrlConf1Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CtrlConf1Load1.setStatus("current")
_Pm200fr20CtrlConf2Load1_Type = EkiOnOff
_Pm200fr20CtrlConf2Load1_Object = MibScalar
pm200fr20CtrlConf2Load1 = _Pm200fr20CtrlConf2Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 1, 1, 2),
    _Pm200fr20CtrlConf2Load1_Type()
)
pm200fr20CtrlConf2Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CtrlConf2Load1.setStatus("current")
_Pm200fr20CtrlConf2Flash1_Type = EkiOnOff
_Pm200fr20CtrlConf2Flash1_Object = MibScalar
pm200fr20CtrlConf2Flash1 = _Pm200fr20CtrlConf2Flash1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 1, 1, 10),
    _Pm200fr20CtrlConf2Flash1_Type()
)
pm200fr20CtrlConf2Flash1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CtrlConf2Flash1.setStatus("current")
_Pm200fr20CtrlConf2Clear1_Type = EkiOnOff
_Pm200fr20CtrlConf2Clear1_Object = MibScalar
pm200fr20CtrlConf2Clear1 = _Pm200fr20CtrlConf2Clear1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 1, 1, 14),
    _Pm200fr20CtrlConf2Clear1_Type()
)
pm200fr20CtrlConf2Clear1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CtrlConf2Clear1.setStatus("current")
_Pm200fr20Ctrlsynth4_ObjectIdentity = ObjectIdentity
pm200fr20Ctrlsynth4 = _Pm200fr20Ctrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 1, 4)
)
_Pm200fr20CtrlCorrelatOn_Type = EkiOnOff
_Pm200fr20CtrlCorrelatOn_Object = MibScalar
pm200fr20CtrlCorrelatOn = _Pm200fr20CtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 1, 4, 1),
    _Pm200fr20CtrlCorrelatOn_Type()
)
pm200fr20CtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CtrlCorrelatOn.setStatus("current")
_Pm200fr20CtrlCorrelatOff_Type = EkiOnOff
_Pm200fr20CtrlCorrelatOff_Object = MibScalar
pm200fr20CtrlCorrelatOff = _Pm200fr20CtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 1, 4, 2),
    _Pm200fr20CtrlCorrelatOff_Type()
)
pm200fr20CtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CtrlCorrelatOff.setStatus("current")
_Pm200fr20CtrlswMgnt_ObjectIdentity = ObjectIdentity
pm200fr20CtrlswMgnt = _Pm200fr20CtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 1, 5)
)
_Pm200fr20CtrlColdReset_Type = EkiOnOff
_Pm200fr20CtrlColdReset_Object = MibScalar
pm200fr20CtrlColdReset = _Pm200fr20CtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 1, 5, 2),
    _Pm200fr20CtrlColdReset_Type()
)
pm200fr20CtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CtrlColdReset.setStatus("current")
_Pm200fr20CtrlWarmReset_Type = EkiOnOff
_Pm200fr20CtrlWarmReset_Object = MibScalar
pm200fr20CtrlWarmReset = _Pm200fr20CtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 1, 5, 3),
    _Pm200fr20CtrlWarmReset_Type()
)
pm200fr20CtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CtrlWarmReset.setStatus("current")
_Pm200fr20CtrlLoadSwBank1_Type = EkiOnOff
_Pm200fr20CtrlLoadSwBank1_Object = MibScalar
pm200fr20CtrlLoadSwBank1 = _Pm200fr20CtrlLoadSwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 1, 5, 5),
    _Pm200fr20CtrlLoadSwBank1_Type()
)
pm200fr20CtrlLoadSwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CtrlLoadSwBank1.setStatus("current")
_Pm200fr20CtrlLoadSwBank2_Type = EkiOnOff
_Pm200fr20CtrlLoadSwBank2_Object = MibScalar
pm200fr20CtrlLoadSwBank2 = _Pm200fr20CtrlLoadSwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 1, 5, 6),
    _Pm200fr20CtrlLoadSwBank2_Type()
)
pm200fr20CtrlLoadSwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CtrlLoadSwBank2.setStatus("current")
_Pm200fr20CtrlgwMgnt_ObjectIdentity = ObjectIdentity
pm200fr20CtrlgwMgnt = _Pm200fr20CtrlgwMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 1, 6)
)
_Pm200fr20CtrlCurrentGwReset_Type = EkiOnOff
_Pm200fr20CtrlCurrentGwReset_Object = MibScalar
pm200fr20CtrlCurrentGwReset = _Pm200fr20CtrlCurrentGwReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 1, 6, 1),
    _Pm200fr20CtrlCurrentGwReset_Type()
)
pm200fr20CtrlCurrentGwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CtrlCurrentGwReset.setStatus("current")
_Pm200fr20CtrlLoadGwBank1_Type = EkiOnOff
_Pm200fr20CtrlLoadGwBank1_Object = MibScalar
pm200fr20CtrlLoadGwBank1 = _Pm200fr20CtrlLoadGwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 1, 6, 5),
    _Pm200fr20CtrlLoadGwBank1_Type()
)
pm200fr20CtrlLoadGwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CtrlLoadGwBank1.setStatus("current")
_Pm200fr20CtrlLoadGwBank2_Type = EkiOnOff
_Pm200fr20CtrlLoadGwBank2_Object = MibScalar
pm200fr20CtrlLoadGwBank2 = _Pm200fr20CtrlLoadGwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 1, 6, 6),
    _Pm200fr20CtrlLoadGwBank2_Type()
)
pm200fr20CtrlLoadGwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CtrlLoadGwBank2.setStatus("current")
_Pm200fr20CtrlLoadGwBank3_Type = EkiOnOff
_Pm200fr20CtrlLoadGwBank3_Object = MibScalar
pm200fr20CtrlLoadGwBank3 = _Pm200fr20CtrlLoadGwBank3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 1, 6, 7),
    _Pm200fr20CtrlLoadGwBank3_Type()
)
pm200fr20CtrlLoadGwBank3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CtrlLoadGwBank3.setStatus("current")
_Pm200fr20CtrlLoadGwBank4_Type = EkiOnOff
_Pm200fr20CtrlLoadGwBank4_Object = MibScalar
pm200fr20CtrlLoadGwBank4 = _Pm200fr20CtrlLoadGwBank4_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 1, 6, 8),
    _Pm200fr20CtrlLoadGwBank4_Type()
)
pm200fr20CtrlLoadGwBank4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CtrlLoadGwBank4.setStatus("current")
_Pm200fr20CtrlledTest_ObjectIdentity = ObjectIdentity
pm200fr20CtrlledTest = _Pm200fr20CtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 1, 192)
)
_Pm200fr20CtrlGreenLed_Type = EkiOnOff
_Pm200fr20CtrlGreenLed_Object = MibScalar
pm200fr20CtrlGreenLed = _Pm200fr20CtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 1, 192, 1),
    _Pm200fr20CtrlGreenLed_Type()
)
pm200fr20CtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CtrlGreenLed.setStatus("current")
_Pm200fr20CtrlRedLed_Type = EkiOnOff
_Pm200fr20CtrlRedLed_Object = MibScalar
pm200fr20CtrlRedLed = _Pm200fr20CtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 1, 192, 2),
    _Pm200fr20CtrlRedLed_Type()
)
pm200fr20CtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CtrlRedLed.setStatus("current")
_Pm200fr20CtrlLedOff_Type = EkiOnOff
_Pm200fr20CtrlLedOff_Object = MibScalar
pm200fr20CtrlLedOff = _Pm200fr20CtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 1, 192, 3),
    _Pm200fr20CtrlLedOff_Type()
)
pm200fr20CtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CtrlLedOff.setStatus("current")
_Pm200fr20CtrlinitSwitchMarvell_ObjectIdentity = ObjectIdentity
pm200fr20CtrlinitSwitchMarvell = _Pm200fr20CtrlinitSwitchMarvell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 1, 201)
)
_Pm200fr20CtrlInitSwitchMarvell_Type = EkiOnOff
_Pm200fr20CtrlInitSwitchMarvell_Object = MibScalar
pm200fr20CtrlInitSwitchMarvell = _Pm200fr20CtrlInitSwitchMarvell_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 1, 201, 1),
    _Pm200fr20CtrlInitSwitchMarvell_Type()
)
pm200fr20CtrlInitSwitchMarvell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CtrlInitSwitchMarvell.setStatus("current")
_Pm200fr20CtrlresetCount_ObjectIdentity = ObjectIdentity
pm200fr20CtrlresetCount = _Pm200fr20CtrlresetCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 1, 259)
)
_Pm200fr20CtrlResetcount_Type = EkiOnOff
_Pm200fr20CtrlResetcount_Object = MibScalar
pm200fr20CtrlResetcount = _Pm200fr20CtrlResetcount_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 1, 259, 1),
    _Pm200fr20CtrlResetcount_Type()
)
pm200fr20CtrlResetcount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CtrlResetcount.setStatus("current")
_Pm200fr20CtrlresetRmon_ObjectIdentity = ObjectIdentity
pm200fr20CtrlresetRmon = _Pm200fr20CtrlresetRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 1, 260)
)
_Pm200fr20CtrlResetrmon_Type = EkiOnOff
_Pm200fr20CtrlResetrmon_Object = MibScalar
pm200fr20CtrlResetrmon = _Pm200fr20CtrlResetrmon_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 1, 260, 1),
    _Pm200fr20CtrlResetrmon_Type()
)
pm200fr20CtrlResetrmon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CtrlResetrmon.setStatus("current")
_Pm200fr20CtrlresetMeasurements_ObjectIdentity = ObjectIdentity
pm200fr20CtrlresetMeasurements = _Pm200fr20CtrlresetMeasurements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 1, 261)
)
_Pm200fr20CtrlResetmeasurements_Type = EkiOnOff
_Pm200fr20CtrlResetmeasurements_Object = MibScalar
pm200fr20CtrlResetmeasurements = _Pm200fr20CtrlResetmeasurements_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 1, 261, 1),
    _Pm200fr20CtrlResetmeasurements_Type()
)
pm200fr20CtrlResetmeasurements.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CtrlResetmeasurements.setStatus("current")
_Pm200fr20CtrlClient_ObjectIdentity = ObjectIdentity
pm200fr20CtrlClient = _Pm200fr20CtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 2)
)
_Pm200fr20CtrlaccessLoopTable_Object = MibTable
pm200fr20CtrlaccessLoopTable = _Pm200fr20CtrlaccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 2, 16)
)
if mibBuilder.loadTexts:
    pm200fr20CtrlaccessLoopTable.setStatus("current")
_Pm200fr20CtrlaccessLoopEntry_Object = MibTableRow
pm200fr20CtrlaccessLoopEntry = _Pm200fr20CtrlaccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 2, 16, 1)
)
pm200fr20CtrlaccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20CtrlaccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20CtrlaccessLoopEntry.setStatus("current")


class _Pm200fr20CtrlaccessLoopIndex_Type(Integer32):
    """Custom type pm200fr20CtrlaccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20CtrlaccessLoopIndex_Type.__name__ = "Integer32"
_Pm200fr20CtrlaccessLoopIndex_Object = MibTableColumn
pm200fr20CtrlaccessLoopIndex = _Pm200fr20CtrlaccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 2, 16, 1, 1),
    _Pm200fr20CtrlaccessLoopIndex_Type()
)
pm200fr20CtrlaccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CtrlaccessLoopIndex.setStatus("current")
_Pm200fr20CtrlaccessLoopPortn_Type = EkiState
_Pm200fr20CtrlaccessLoopPortn_Object = MibTableColumn
pm200fr20CtrlaccessLoopPortn = _Pm200fr20CtrlaccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 2, 16, 1, 2),
    _Pm200fr20CtrlaccessLoopPortn_Type()
)
pm200fr20CtrlaccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CtrlaccessLoopPortn.setStatus("current")
_Pm200fr20CtrlclientLoopToLineTable_Object = MibTable
pm200fr20CtrlclientLoopToLineTable = _Pm200fr20CtrlclientLoopToLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 2, 17)
)
if mibBuilder.loadTexts:
    pm200fr20CtrlclientLoopToLineTable.setStatus("current")
_Pm200fr20CtrlclientLoopToLineEntry_Object = MibTableRow
pm200fr20CtrlclientLoopToLineEntry = _Pm200fr20CtrlclientLoopToLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 2, 17, 1)
)
pm200fr20CtrlclientLoopToLineEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20CtrlclientLoopToLineIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20CtrlclientLoopToLineEntry.setStatus("current")


class _Pm200fr20CtrlclientLoopToLineIndex_Type(Integer32):
    """Custom type pm200fr20CtrlclientLoopToLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20CtrlclientLoopToLineIndex_Type.__name__ = "Integer32"
_Pm200fr20CtrlclientLoopToLineIndex_Object = MibTableColumn
pm200fr20CtrlclientLoopToLineIndex = _Pm200fr20CtrlclientLoopToLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 2, 17, 1, 1),
    _Pm200fr20CtrlclientLoopToLineIndex_Type()
)
pm200fr20CtrlclientLoopToLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CtrlclientLoopToLineIndex.setStatus("current")
_Pm200fr20CtrlclientLoopToLinePortn_Type = EkiState
_Pm200fr20CtrlclientLoopToLinePortn_Object = MibTableColumn
pm200fr20CtrlclientLoopToLinePortn = _Pm200fr20CtrlclientLoopToLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 2, 17, 1, 2),
    _Pm200fr20CtrlclientLoopToLinePortn_Type()
)
pm200fr20CtrlclientLoopToLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CtrlclientLoopToLinePortn.setStatus("current")
_Pm200fr20CtrlcsfUpInsTable_Object = MibTable
pm200fr20CtrlcsfUpInsTable = _Pm200fr20CtrlcsfUpInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 2, 21)
)
if mibBuilder.loadTexts:
    pm200fr20CtrlcsfUpInsTable.setStatus("current")
_Pm200fr20CtrlcsfUpInsEntry_Object = MibTableRow
pm200fr20CtrlcsfUpInsEntry = _Pm200fr20CtrlcsfUpInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 2, 21, 1)
)
pm200fr20CtrlcsfUpInsEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20CtrlcsfUpInsIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20CtrlcsfUpInsEntry.setStatus("current")


class _Pm200fr20CtrlcsfUpInsIndex_Type(Integer32):
    """Custom type pm200fr20CtrlcsfUpInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20CtrlcsfUpInsIndex_Type.__name__ = "Integer32"
_Pm200fr20CtrlcsfUpInsIndex_Object = MibTableColumn
pm200fr20CtrlcsfUpInsIndex = _Pm200fr20CtrlcsfUpInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 2, 21, 1, 1),
    _Pm200fr20CtrlcsfUpInsIndex_Type()
)
pm200fr20CtrlcsfUpInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CtrlcsfUpInsIndex.setStatus("current")
_Pm200fr20CtrlcsfUpInsPortn_Type = EkiState
_Pm200fr20CtrlcsfUpInsPortn_Object = MibTableColumn
pm200fr20CtrlcsfUpInsPortn = _Pm200fr20CtrlcsfUpInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 2, 21, 1, 2),
    _Pm200fr20CtrlcsfUpInsPortn_Type()
)
pm200fr20CtrlcsfUpInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CtrlcsfUpInsPortn.setStatus("current")
_Pm200fr20CtrlcaisDwInsTable_Object = MibTable
pm200fr20CtrlcaisDwInsTable = _Pm200fr20CtrlcaisDwInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 2, 22)
)
if mibBuilder.loadTexts:
    pm200fr20CtrlcaisDwInsTable.setStatus("current")
_Pm200fr20CtrlcaisDwInsEntry_Object = MibTableRow
pm200fr20CtrlcaisDwInsEntry = _Pm200fr20CtrlcaisDwInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 2, 22, 1)
)
pm200fr20CtrlcaisDwInsEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20CtrlcaisDwInsIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20CtrlcaisDwInsEntry.setStatus("current")


class _Pm200fr20CtrlcaisDwInsIndex_Type(Integer32):
    """Custom type pm200fr20CtrlcaisDwInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20CtrlcaisDwInsIndex_Type.__name__ = "Integer32"
_Pm200fr20CtrlcaisDwInsIndex_Object = MibTableColumn
pm200fr20CtrlcaisDwInsIndex = _Pm200fr20CtrlcaisDwInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 2, 22, 1, 1),
    _Pm200fr20CtrlcaisDwInsIndex_Type()
)
pm200fr20CtrlcaisDwInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CtrlcaisDwInsIndex.setStatus("current")
_Pm200fr20CtrlcaisDwInsPortn_Type = EkiState
_Pm200fr20CtrlcaisDwInsPortn_Object = MibTableColumn
pm200fr20CtrlcaisDwInsPortn = _Pm200fr20CtrlcaisDwInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 2, 22, 1, 2),
    _Pm200fr20CtrlcaisDwInsPortn_Type()
)
pm200fr20CtrlcaisDwInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CtrlcaisDwInsPortn.setStatus("current")
_Pm200fr20CtrlclientResetAllCountTable_Object = MibTable
pm200fr20CtrlclientResetAllCountTable = _Pm200fr20CtrlclientResetAllCountTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 2, 262)
)
if mibBuilder.loadTexts:
    pm200fr20CtrlclientResetAllCountTable.setStatus("current")
_Pm200fr20CtrlclientResetAllCountEntry_Object = MibTableRow
pm200fr20CtrlclientResetAllCountEntry = _Pm200fr20CtrlclientResetAllCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 2, 262, 1)
)
pm200fr20CtrlclientResetAllCountEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20CtrlclientResetAllCountIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20CtrlclientResetAllCountEntry.setStatus("current")


class _Pm200fr20CtrlclientResetAllCountIndex_Type(Integer32):
    """Custom type pm200fr20CtrlclientResetAllCountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20CtrlclientResetAllCountIndex_Type.__name__ = "Integer32"
_Pm200fr20CtrlclientResetAllCountIndex_Object = MibTableColumn
pm200fr20CtrlclientResetAllCountIndex = _Pm200fr20CtrlclientResetAllCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 2, 262, 1, 1),
    _Pm200fr20CtrlclientResetAllCountIndex_Type()
)
pm200fr20CtrlclientResetAllCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CtrlclientResetAllCountIndex.setStatus("current")
_Pm200fr20CtrlclientResetAllCountsPortn_Type = EkiState
_Pm200fr20CtrlclientResetAllCountsPortn_Object = MibTableColumn
pm200fr20CtrlclientResetAllCountsPortn = _Pm200fr20CtrlclientResetAllCountsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 2, 262, 1, 2),
    _Pm200fr20CtrlclientResetAllCountsPortn_Type()
)
pm200fr20CtrlclientResetAllCountsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CtrlclientResetAllCountsPortn.setStatus("current")
_Pm200fr20CtrlLine_ObjectIdentity = ObjectIdentity
pm200fr20CtrlLine = _Pm200fr20CtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 3)
)
_Pm200fr20CtrlcommAccessLoopTable_Object = MibTable
pm200fr20CtrlcommAccessLoopTable = _Pm200fr20CtrlcommAccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 3, 64)
)
if mibBuilder.loadTexts:
    pm200fr20CtrlcommAccessLoopTable.setStatus("current")
_Pm200fr20CtrlcommAccessLoopEntry_Object = MibTableRow
pm200fr20CtrlcommAccessLoopEntry = _Pm200fr20CtrlcommAccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 3, 64, 1)
)
pm200fr20CtrlcommAccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20CtrlcommAccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20CtrlcommAccessLoopEntry.setStatus("current")


class _Pm200fr20CtrlcommAccessLoopIndex_Type(Integer32):
    """Custom type pm200fr20CtrlcommAccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20CtrlcommAccessLoopIndex_Type.__name__ = "Integer32"
_Pm200fr20CtrlcommAccessLoopIndex_Object = MibTableColumn
pm200fr20CtrlcommAccessLoopIndex = _Pm200fr20CtrlcommAccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 3, 64, 1, 1),
    _Pm200fr20CtrlcommAccessLoopIndex_Type()
)
pm200fr20CtrlcommAccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CtrlcommAccessLoopIndex.setStatus("current")
_Pm200fr20CtrlcommAccessLoopPortn_Type = EkiState
_Pm200fr20CtrlcommAccessLoopPortn_Object = MibTableColumn
pm200fr20CtrlcommAccessLoopPortn = _Pm200fr20CtrlcommAccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 3, 64, 1, 2),
    _Pm200fr20CtrlcommAccessLoopPortn_Type()
)
pm200fr20CtrlcommAccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CtrlcommAccessLoopPortn.setStatus("current")
_Pm200fr20CtrllineLoopTable_Object = MibTable
pm200fr20CtrllineLoopTable = _Pm200fr20CtrllineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 3, 66)
)
if mibBuilder.loadTexts:
    pm200fr20CtrllineLoopTable.setStatus("current")
_Pm200fr20CtrllineLoopEntry_Object = MibTableRow
pm200fr20CtrllineLoopEntry = _Pm200fr20CtrllineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 3, 66, 1)
)
pm200fr20CtrllineLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20CtrllineLoopIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20CtrllineLoopEntry.setStatus("current")


class _Pm200fr20CtrllineLoopIndex_Type(Integer32):
    """Custom type pm200fr20CtrllineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20CtrllineLoopIndex_Type.__name__ = "Integer32"
_Pm200fr20CtrllineLoopIndex_Object = MibTableColumn
pm200fr20CtrllineLoopIndex = _Pm200fr20CtrllineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 3, 66, 1, 1),
    _Pm200fr20CtrllineLoopIndex_Type()
)
pm200fr20CtrllineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CtrllineLoopIndex.setStatus("current")
_Pm200fr20CtrllineLoopPortn_Type = EkiState
_Pm200fr20CtrllineLoopPortn_Object = MibTableColumn
pm200fr20CtrllineLoopPortn = _Pm200fr20CtrllineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 3, 66, 1, 2),
    _Pm200fr20CtrllineLoopPortn_Type()
)
pm200fr20CtrllineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CtrllineLoopPortn.setStatus("current")
_Pm200fr20CtrlfecDisableTable_Object = MibTable
pm200fr20CtrlfecDisableTable = _Pm200fr20CtrlfecDisableTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 3, 69)
)
if mibBuilder.loadTexts:
    pm200fr20CtrlfecDisableTable.setStatus("current")
_Pm200fr20CtrlfecDisableEntry_Object = MibTableRow
pm200fr20CtrlfecDisableEntry = _Pm200fr20CtrlfecDisableEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 3, 69, 1)
)
pm200fr20CtrlfecDisableEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20CtrlfecDisableIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20CtrlfecDisableEntry.setStatus("current")


class _Pm200fr20CtrlfecDisableIndex_Type(Integer32):
    """Custom type pm200fr20CtrlfecDisableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20CtrlfecDisableIndex_Type.__name__ = "Integer32"
_Pm200fr20CtrlfecDisableIndex_Object = MibTableColumn
pm200fr20CtrlfecDisableIndex = _Pm200fr20CtrlfecDisableIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 3, 69, 1, 1),
    _Pm200fr20CtrlfecDisableIndex_Type()
)
pm200fr20CtrlfecDisableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CtrlfecDisableIndex.setStatus("current")
_Pm200fr20CtrlfecDisablePortn_Type = EkiState
_Pm200fr20CtrlfecDisablePortn_Object = MibTableColumn
pm200fr20CtrlfecDisablePortn = _Pm200fr20CtrlfecDisablePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 3, 69, 1, 2),
    _Pm200fr20CtrlfecDisablePortn_Type()
)
pm200fr20CtrlfecDisablePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CtrlfecDisablePortn.setStatus("current")
_Pm200fr20CtrlmsaLineLoopTable_Object = MibTable
pm200fr20CtrlmsaLineLoopTable = _Pm200fr20CtrlmsaLineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 3, 209)
)
if mibBuilder.loadTexts:
    pm200fr20CtrlmsaLineLoopTable.setStatus("current")
_Pm200fr20CtrlmsaLineLoopEntry_Object = MibTableRow
pm200fr20CtrlmsaLineLoopEntry = _Pm200fr20CtrlmsaLineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 3, 209, 1)
)
pm200fr20CtrlmsaLineLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20CtrlmsaLineLoopIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20CtrlmsaLineLoopEntry.setStatus("current")


class _Pm200fr20CtrlmsaLineLoopIndex_Type(Integer32):
    """Custom type pm200fr20CtrlmsaLineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20CtrlmsaLineLoopIndex_Type.__name__ = "Integer32"
_Pm200fr20CtrlmsaLineLoopIndex_Object = MibTableColumn
pm200fr20CtrlmsaLineLoopIndex = _Pm200fr20CtrlmsaLineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 3, 209, 1, 1),
    _Pm200fr20CtrlmsaLineLoopIndex_Type()
)
pm200fr20CtrlmsaLineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CtrlmsaLineLoopIndex.setStatus("current")
_Pm200fr20CtrlmsaLineLoopPortn_Type = EkiState
_Pm200fr20CtrlmsaLineLoopPortn_Object = MibTableColumn
pm200fr20CtrlmsaLineLoopPortn = _Pm200fr20CtrlmsaLineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 3, 209, 1, 2),
    _Pm200fr20CtrlmsaLineLoopPortn_Type()
)
pm200fr20CtrlmsaLineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CtrlmsaLineLoopPortn.setStatus("current")
_Pm200fr20CtrlmsaTxResetTable_Object = MibTable
pm200fr20CtrlmsaTxResetTable = _Pm200fr20CtrlmsaTxResetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 3, 210)
)
if mibBuilder.loadTexts:
    pm200fr20CtrlmsaTxResetTable.setStatus("current")
_Pm200fr20CtrlmsaTxResetEntry_Object = MibTableRow
pm200fr20CtrlmsaTxResetEntry = _Pm200fr20CtrlmsaTxResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 3, 210, 1)
)
pm200fr20CtrlmsaTxResetEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20CtrlmsaTxResetIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20CtrlmsaTxResetEntry.setStatus("current")


class _Pm200fr20CtrlmsaTxResetIndex_Type(Integer32):
    """Custom type pm200fr20CtrlmsaTxResetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20CtrlmsaTxResetIndex_Type.__name__ = "Integer32"
_Pm200fr20CtrlmsaTxResetIndex_Object = MibTableColumn
pm200fr20CtrlmsaTxResetIndex = _Pm200fr20CtrlmsaTxResetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 3, 210, 1, 1),
    _Pm200fr20CtrlmsaTxResetIndex_Type()
)
pm200fr20CtrlmsaTxResetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CtrlmsaTxResetIndex.setStatus("current")
_Pm200fr20CtrlmsaTxResetPortn_Type = EkiState
_Pm200fr20CtrlmsaTxResetPortn_Object = MibTableColumn
pm200fr20CtrlmsaTxResetPortn = _Pm200fr20CtrlmsaTxResetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 3, 210, 1, 2),
    _Pm200fr20CtrlmsaTxResetPortn_Type()
)
pm200fr20CtrlmsaTxResetPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CtrlmsaTxResetPortn.setStatus("current")
_Pm200fr20CtrlmsaRxResetTable_Object = MibTable
pm200fr20CtrlmsaRxResetTable = _Pm200fr20CtrlmsaRxResetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 3, 211)
)
if mibBuilder.loadTexts:
    pm200fr20CtrlmsaRxResetTable.setStatus("current")
_Pm200fr20CtrlmsaRxResetEntry_Object = MibTableRow
pm200fr20CtrlmsaRxResetEntry = _Pm200fr20CtrlmsaRxResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 3, 211, 1)
)
pm200fr20CtrlmsaRxResetEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20CtrlmsaRxResetIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20CtrlmsaRxResetEntry.setStatus("current")


class _Pm200fr20CtrlmsaRxResetIndex_Type(Integer32):
    """Custom type pm200fr20CtrlmsaRxResetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20CtrlmsaRxResetIndex_Type.__name__ = "Integer32"
_Pm200fr20CtrlmsaRxResetIndex_Object = MibTableColumn
pm200fr20CtrlmsaRxResetIndex = _Pm200fr20CtrlmsaRxResetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 3, 211, 1, 1),
    _Pm200fr20CtrlmsaRxResetIndex_Type()
)
pm200fr20CtrlmsaRxResetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CtrlmsaRxResetIndex.setStatus("current")
_Pm200fr20CtrlmsaRxResetPortn_Type = EkiState
_Pm200fr20CtrlmsaRxResetPortn_Object = MibTableColumn
pm200fr20CtrlmsaRxResetPortn = _Pm200fr20CtrlmsaRxResetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 3, 211, 1, 2),
    _Pm200fr20CtrlmsaRxResetPortn_Type()
)
pm200fr20CtrlmsaRxResetPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CtrlmsaRxResetPortn.setStatus("current")
_Pm200fr20CtrlmsaShutdownTable_Object = MibTable
pm200fr20CtrlmsaShutdownTable = _Pm200fr20CtrlmsaShutdownTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 3, 212)
)
if mibBuilder.loadTexts:
    pm200fr20CtrlmsaShutdownTable.setStatus("current")
_Pm200fr20CtrlmsaShutdownEntry_Object = MibTableRow
pm200fr20CtrlmsaShutdownEntry = _Pm200fr20CtrlmsaShutdownEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 3, 212, 1)
)
pm200fr20CtrlmsaShutdownEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20CtrlmsaShutdownIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20CtrlmsaShutdownEntry.setStatus("current")


class _Pm200fr20CtrlmsaShutdownIndex_Type(Integer32):
    """Custom type pm200fr20CtrlmsaShutdownIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20CtrlmsaShutdownIndex_Type.__name__ = "Integer32"
_Pm200fr20CtrlmsaShutdownIndex_Object = MibTableColumn
pm200fr20CtrlmsaShutdownIndex = _Pm200fr20CtrlmsaShutdownIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 3, 212, 1, 1),
    _Pm200fr20CtrlmsaShutdownIndex_Type()
)
pm200fr20CtrlmsaShutdownIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CtrlmsaShutdownIndex.setStatus("current")
_Pm200fr20CtrlmsaShutdownPortn_Type = EkiState
_Pm200fr20CtrlmsaShutdownPortn_Object = MibTableColumn
pm200fr20CtrlmsaShutdownPortn = _Pm200fr20CtrlmsaShutdownPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 3, 212, 1, 2),
    _Pm200fr20CtrlmsaShutdownPortn_Type()
)
pm200fr20CtrlmsaShutdownPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CtrlmsaShutdownPortn.setStatus("current")
_Pm200fr20CtrllineResetAllCountTable_Object = MibTable
pm200fr20CtrllineResetAllCountTable = _Pm200fr20CtrllineResetAllCountTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 3, 263)
)
if mibBuilder.loadTexts:
    pm200fr20CtrllineResetAllCountTable.setStatus("current")
_Pm200fr20CtrllineResetAllCountEntry_Object = MibTableRow
pm200fr20CtrllineResetAllCountEntry = _Pm200fr20CtrllineResetAllCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 3, 263, 1)
)
pm200fr20CtrllineResetAllCountEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20CtrllineResetAllCountIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20CtrllineResetAllCountEntry.setStatus("current")


class _Pm200fr20CtrllineResetAllCountIndex_Type(Integer32):
    """Custom type pm200fr20CtrllineResetAllCountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20CtrllineResetAllCountIndex_Type.__name__ = "Integer32"
_Pm200fr20CtrllineResetAllCountIndex_Object = MibTableColumn
pm200fr20CtrllineResetAllCountIndex = _Pm200fr20CtrllineResetAllCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 3, 263, 1, 1),
    _Pm200fr20CtrllineResetAllCountIndex_Type()
)
pm200fr20CtrllineResetAllCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CtrllineResetAllCountIndex.setStatus("current")
_Pm200fr20CtrllineResetAllCountsPortn_Type = EkiState
_Pm200fr20CtrllineResetAllCountsPortn_Object = MibTableColumn
pm200fr20CtrllineResetAllCountsPortn = _Pm200fr20CtrllineResetAllCountsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 6, 3, 263, 1, 2),
    _Pm200fr20CtrllineResetAllCountsPortn_Type()
)
pm200fr20CtrllineResetAllCountsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CtrllineResetAllCountsPortn.setStatus("current")
_Pm200fr20ri_ObjectIdentity = ObjectIdentity
pm200fr20ri = _Pm200fr20ri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 7)
)
_Pm200fr20riTable_ObjectIdentity = ObjectIdentity
pm200fr20riTable = _Pm200fr20riTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 7, 1)
)
_Pm200fr20RinvSfpTable_Object = MibTable
pm200fr20RinvSfpTable = _Pm200fr20RinvSfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 7, 1, 1)
)
if mibBuilder.loadTexts:
    pm200fr20RinvSfpTable.setStatus("current")
_Pm200fr20RinvSfpEntry_Object = MibTableRow
pm200fr20RinvSfpEntry = _Pm200fr20RinvSfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 7, 1, 1, 1)
)
pm200fr20RinvSfpEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20RinvSfpIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20RinvSfpEntry.setStatus("current")


class _Pm200fr20RinvSfpIndex_Type(Integer32):
    """Custom type pm200fr20RinvSfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm200fr20RinvSfpIndex_Type.__name__ = "Integer32"
_Pm200fr20RinvSfpIndex_Object = MibTableColumn
pm200fr20RinvSfpIndex = _Pm200fr20RinvSfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 7, 1, 1, 1, 1),
    _Pm200fr20RinvSfpIndex_Type()
)
pm200fr20RinvSfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20RinvSfpIndex.setStatus("current")
_Pm200fr20Rinvsfp_Type = DisplayString
_Pm200fr20Rinvsfp_Object = MibTableColumn
pm200fr20Rinvsfp = _Pm200fr20Rinvsfp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 7, 1, 1, 1, 2),
    _Pm200fr20Rinvsfp_Type()
)
pm200fr20Rinvsfp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20Rinvsfp.setStatus("current")
_Pm200fr20RinvLineTable_Object = MibTable
pm200fr20RinvLineTable = _Pm200fr20RinvLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pm200fr20RinvLineTable.setStatus("current")
_Pm200fr20RinvLineEntry_Object = MibTableRow
pm200fr20RinvLineEntry = _Pm200fr20RinvLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 7, 1, 2, 1)
)
pm200fr20RinvLineEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20RinvLineIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20RinvLineEntry.setStatus("current")


class _Pm200fr20RinvLineIndex_Type(Integer32):
    """Custom type pm200fr20RinvLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm200fr20RinvLineIndex_Type.__name__ = "Integer32"
_Pm200fr20RinvLineIndex_Object = MibTableColumn
pm200fr20RinvLineIndex = _Pm200fr20RinvLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 7, 1, 2, 1, 1),
    _Pm200fr20RinvLineIndex_Type()
)
pm200fr20RinvLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20RinvLineIndex.setStatus("current")
_Pm200fr20RinvxfpLine_Type = DisplayString
_Pm200fr20RinvxfpLine_Object = MibTableColumn
pm200fr20RinvxfpLine = _Pm200fr20RinvxfpLine_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 7, 1, 2, 1, 2),
    _Pm200fr20RinvxfpLine_Type()
)
pm200fr20RinvxfpLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20RinvxfpLine.setStatus("current")
_Pm200fr20RinvReloadInventory_Type = EkiOnOff
_Pm200fr20RinvReloadInventory_Object = MibScalar
pm200fr20RinvReloadInventory = _Pm200fr20RinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 7, 2),
    _Pm200fr20RinvReloadInventory_Type()
)
pm200fr20RinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20RinvReloadInventory.setStatus("current")
_Pm200fr20RinvHwPlatform_Type = DisplayString
_Pm200fr20RinvHwPlatform_Object = MibScalar
pm200fr20RinvHwPlatform = _Pm200fr20RinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 7, 3),
    _Pm200fr20RinvHwPlatform_Type()
)
pm200fr20RinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20RinvHwPlatform.setStatus("current")
_Pm200fr20RinvModulePlatform_Type = DisplayString
_Pm200fr20RinvModulePlatform_Object = MibScalar
pm200fr20RinvModulePlatform = _Pm200fr20RinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 7, 4),
    _Pm200fr20RinvModulePlatform_Type()
)
pm200fr20RinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20RinvModulePlatform.setStatus("current")
_Pm200fr20RinvSwPlatform_Type = DisplayString
_Pm200fr20RinvSwPlatform_Object = MibScalar
pm200fr20RinvSwPlatform = _Pm200fr20RinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 7, 5),
    _Pm200fr20RinvSwPlatform_Type()
)
pm200fr20RinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20RinvSwPlatform.setStatus("current")
_Pm200fr20RinvGwPlatform_Type = DisplayString
_Pm200fr20RinvGwPlatform_Object = MibScalar
pm200fr20RinvGwPlatform = _Pm200fr20RinvGwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 7, 6),
    _Pm200fr20RinvGwPlatform_Type()
)
pm200fr20RinvGwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20RinvGwPlatform.setStatus("current")
_Pm200fr20download_ObjectIdentity = ObjectIdentity
pm200fr20download = _Pm200fr20download_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 8)
)
_Pm200fr20DwlOther_ObjectIdentity = ObjectIdentity
pm200fr20DwlOther = _Pm200fr20DwlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 8, 1)
)
_Pm200fr20DwlrestartProcess_ObjectIdentity = ObjectIdentity
pm200fr20DwlrestartProcess = _Pm200fr20DwlrestartProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 8, 1, 0)
)
_Pm200fr20DwlWarmRestartProcessed_Type = EkiOnOff
_Pm200fr20DwlWarmRestartProcessed_Object = MibScalar
pm200fr20DwlWarmRestartProcessed = _Pm200fr20DwlWarmRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 8, 1, 0, 1),
    _Pm200fr20DwlWarmRestartProcessed_Type()
)
pm200fr20DwlWarmRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20DwlWarmRestartProcessed.setStatus("current")
_Pm200fr20DwlColdRestartProcessed_Type = EkiOnOff
_Pm200fr20DwlColdRestartProcessed_Object = MibScalar
pm200fr20DwlColdRestartProcessed = _Pm200fr20DwlColdRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 8, 1, 0, 2),
    _Pm200fr20DwlColdRestartProcessed_Type()
)
pm200fr20DwlColdRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20DwlColdRestartProcessed.setStatus("current")
_Pm200fr20DwlswBanksUsed_ObjectIdentity = ObjectIdentity
pm200fr20DwlswBanksUsed = _Pm200fr20DwlswBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 8, 1, 1)
)
_Pm200fr20DwlSwBank1Used_Type = EkiOnOff
_Pm200fr20DwlSwBank1Used_Object = MibScalar
pm200fr20DwlSwBank1Used = _Pm200fr20DwlSwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 8, 1, 1, 1),
    _Pm200fr20DwlSwBank1Used_Type()
)
pm200fr20DwlSwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20DwlSwBank1Used.setStatus("current")
_Pm200fr20DwlSwBank2Used_Type = EkiOnOff
_Pm200fr20DwlSwBank2Used_Object = MibScalar
pm200fr20DwlSwBank2Used = _Pm200fr20DwlSwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 8, 1, 1, 2),
    _Pm200fr20DwlSwBank2Used_Type()
)
pm200fr20DwlSwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20DwlSwBank2Used.setStatus("current")
_Pm200fr20DwlSwBank1Notempty_Type = EkiOnOff
_Pm200fr20DwlSwBank1Notempty_Object = MibScalar
pm200fr20DwlSwBank1Notempty = _Pm200fr20DwlSwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 8, 1, 1, 5),
    _Pm200fr20DwlSwBank1Notempty_Type()
)
pm200fr20DwlSwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20DwlSwBank1Notempty.setStatus("current")
_Pm200fr20DwlSwBank2Notempty_Type = EkiOnOff
_Pm200fr20DwlSwBank2Notempty_Object = MibScalar
pm200fr20DwlSwBank2Notempty = _Pm200fr20DwlSwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 8, 1, 1, 6),
    _Pm200fr20DwlSwBank2Notempty_Type()
)
pm200fr20DwlSwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20DwlSwBank2Notempty.setStatus("current")
_Pm200fr20DwlgwBanksUsed_ObjectIdentity = ObjectIdentity
pm200fr20DwlgwBanksUsed = _Pm200fr20DwlgwBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 8, 1, 2)
)
_Pm200fr20DwlGwBank1Used_Type = EkiOnOff
_Pm200fr20DwlGwBank1Used_Object = MibScalar
pm200fr20DwlGwBank1Used = _Pm200fr20DwlGwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 8, 1, 2, 1),
    _Pm200fr20DwlGwBank1Used_Type()
)
pm200fr20DwlGwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20DwlGwBank1Used.setStatus("current")
_Pm200fr20DwlGwBank2Used_Type = EkiOnOff
_Pm200fr20DwlGwBank2Used_Object = MibScalar
pm200fr20DwlGwBank2Used = _Pm200fr20DwlGwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 8, 1, 2, 2),
    _Pm200fr20DwlGwBank2Used_Type()
)
pm200fr20DwlGwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20DwlGwBank2Used.setStatus("current")
_Pm200fr20DwlGwBank3Used_Type = EkiOnOff
_Pm200fr20DwlGwBank3Used_Object = MibScalar
pm200fr20DwlGwBank3Used = _Pm200fr20DwlGwBank3Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 8, 1, 2, 3),
    _Pm200fr20DwlGwBank3Used_Type()
)
pm200fr20DwlGwBank3Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20DwlGwBank3Used.setStatus("current")
_Pm200fr20DwlGwBank4Used_Type = EkiOnOff
_Pm200fr20DwlGwBank4Used_Object = MibScalar
pm200fr20DwlGwBank4Used = _Pm200fr20DwlGwBank4Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 8, 1, 2, 4),
    _Pm200fr20DwlGwBank4Used_Type()
)
pm200fr20DwlGwBank4Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20DwlGwBank4Used.setStatus("current")
_Pm200fr20DwlGwBank1Notempty_Type = EkiOnOff
_Pm200fr20DwlGwBank1Notempty_Object = MibScalar
pm200fr20DwlGwBank1Notempty = _Pm200fr20DwlGwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 8, 1, 2, 5),
    _Pm200fr20DwlGwBank1Notempty_Type()
)
pm200fr20DwlGwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20DwlGwBank1Notempty.setStatus("current")
_Pm200fr20DwlGwBank2Notempty_Type = EkiOnOff
_Pm200fr20DwlGwBank2Notempty_Object = MibScalar
pm200fr20DwlGwBank2Notempty = _Pm200fr20DwlGwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 8, 1, 2, 6),
    _Pm200fr20DwlGwBank2Notempty_Type()
)
pm200fr20DwlGwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20DwlGwBank2Notempty.setStatus("current")
_Pm200fr20DwlGwBank3Notempty_Type = EkiOnOff
_Pm200fr20DwlGwBank3Notempty_Object = MibScalar
pm200fr20DwlGwBank3Notempty = _Pm200fr20DwlGwBank3Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 8, 1, 2, 7),
    _Pm200fr20DwlGwBank3Notempty_Type()
)
pm200fr20DwlGwBank3Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20DwlGwBank3Notempty.setStatus("current")
_Pm200fr20DwlGwBank4Notempty_Type = EkiOnOff
_Pm200fr20DwlGwBank4Notempty_Object = MibScalar
pm200fr20DwlGwBank4Notempty = _Pm200fr20DwlGwBank4Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 8, 1, 2, 8),
    _Pm200fr20DwlGwBank4Notempty_Type()
)
pm200fr20DwlGwBank4Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20DwlGwBank4Notempty.setStatus("current")
_Pm200fr20DwlClient_ObjectIdentity = ObjectIdentity
pm200fr20DwlClient = _Pm200fr20DwlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 8, 2)
)
_Pm200fr20DwlLine_ObjectIdentity = ObjectIdentity
pm200fr20DwlLine = _Pm200fr20DwlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 8, 3)
)
_Pm200fr20Config_ObjectIdentity = ObjectIdentity
pm200fr20Config = _Pm200fr20Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9)
)
_Pm200fr20CfgAccessCAisCsf_ObjectIdentity = ObjectIdentity
pm200fr20CfgAccessCAisCsf = _Pm200fr20CfgAccessCAisCsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 1)
)
_Pm200fr20CfgClientcaiscsfTable_Object = MibTable
pm200fr20CfgClientcaiscsfTable = _Pm200fr20CfgClientcaiscsfTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 1, 1)
)
if mibBuilder.loadTexts:
    pm200fr20CfgClientcaiscsfTable.setStatus("current")
_Pm200fr20CfgClientcaiscsfEntry_Object = MibTableRow
pm200fr20CfgClientcaiscsfEntry = _Pm200fr20CfgClientcaiscsfEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 1, 1, 1)
)
pm200fr20CfgClientcaiscsfEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20CfgClientcaiscsfIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20CfgClientcaiscsfEntry.setStatus("current")


class _Pm200fr20CfgClientcaiscsfIndex_Type(Integer32):
    """Custom type pm200fr20CfgClientcaiscsfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20CfgClientcaiscsfIndex_Type.__name__ = "Integer32"
_Pm200fr20CfgClientcaiscsfIndex_Object = MibTableColumn
pm200fr20CfgClientcaiscsfIndex = _Pm200fr20CfgClientcaiscsfIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 1, 1, 1, 1),
    _Pm200fr20CfgClientcaiscsfIndex_Type()
)
pm200fr20CfgClientcaiscsfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CfgClientcaiscsfIndex.setStatus("current")


class _Pm200fr20CfgReservePortn_Type(Unsigned32):
    """Custom type pm200fr20CfgReservePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200fr20CfgReservePortn_Type.__name__ = "Unsigned32"
_Pm200fr20CfgReservePortn_Object = MibTableColumn
pm200fr20CfgReservePortn = _Pm200fr20CfgReservePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 1, 1, 1, 3),
    _Pm200fr20CfgReservePortn_Type()
)
pm200fr20CfgReservePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CfgReservePortn.setStatus("current")
_Pm200fr20CfgStartup_ObjectIdentity = ObjectIdentity
pm200fr20CfgStartup = _Pm200fr20CfgStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 2)
)
_Pm200fr20CfgClientStartupTable_Object = MibTable
pm200fr20CfgClientStartupTable = _Pm200fr20CfgClientStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 2, 1)
)
if mibBuilder.loadTexts:
    pm200fr20CfgClientStartupTable.setStatus("current")
_Pm200fr20CfgClientStartupEntry_Object = MibTableRow
pm200fr20CfgClientStartupEntry = _Pm200fr20CfgClientStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 2, 1, 1)
)
pm200fr20CfgClientStartupEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20CfgClientStartupIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20CfgClientStartupEntry.setStatus("current")


class _Pm200fr20CfgClientStartupIndex_Type(Integer32):
    """Custom type pm200fr20CfgClientStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20CfgClientStartupIndex_Type.__name__ = "Integer32"
_Pm200fr20CfgClientStartupIndex_Object = MibTableColumn
pm200fr20CfgClientStartupIndex = _Pm200fr20CfgClientStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 2, 1, 1, 1),
    _Pm200fr20CfgClientStartupIndex_Type()
)
pm200fr20CfgClientStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CfgClientStartupIndex.setStatus("current")


class _Pm200fr20CfgSystConfPortPortn_Type(Unsigned32):
    """Custom type pm200fr20CfgSystConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200fr20CfgSystConfPortPortn_Type.__name__ = "Unsigned32"
_Pm200fr20CfgSystConfPortPortn_Object = MibTableColumn
pm200fr20CfgSystConfPortPortn = _Pm200fr20CfgSystConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 2, 1, 1, 3),
    _Pm200fr20CfgSystConfPortPortn_Type()
)
pm200fr20CfgSystConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CfgSystConfPortPortn.setStatus("current")


class _Pm200fr20CfgNetConfPortPortn_Type(Unsigned32):
    """Custom type pm200fr20CfgNetConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200fr20CfgNetConfPortPortn_Type.__name__ = "Unsigned32"
_Pm200fr20CfgNetConfPortPortn_Object = MibTableColumn
pm200fr20CfgNetConfPortPortn = _Pm200fr20CfgNetConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 2, 1, 1, 4),
    _Pm200fr20CfgNetConfPortPortn_Type()
)
pm200fr20CfgNetConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CfgNetConfPortPortn.setStatus("current")


class _Pm200fr20CfgOptionsPortPortn_Type(Unsigned32):
    """Custom type pm200fr20CfgOptionsPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200fr20CfgOptionsPortPortn_Type.__name__ = "Unsigned32"
_Pm200fr20CfgOptionsPortPortn_Object = MibTableColumn
pm200fr20CfgOptionsPortPortn = _Pm200fr20CfgOptionsPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 2, 1, 1, 14),
    _Pm200fr20CfgOptionsPortPortn_Type()
)
pm200fr20CfgOptionsPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CfgOptionsPortPortn.setStatus("current")
_Pm200fr20CfgLineStartupTable_Object = MibTable
pm200fr20CfgLineStartupTable = _Pm200fr20CfgLineStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 2, 2)
)
if mibBuilder.loadTexts:
    pm200fr20CfgLineStartupTable.setStatus("current")
_Pm200fr20CfgLineStartupEntry_Object = MibTableRow
pm200fr20CfgLineStartupEntry = _Pm200fr20CfgLineStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 2, 2, 1)
)
pm200fr20CfgLineStartupEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20CfgLineStartupIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20CfgLineStartupEntry.setStatus("current")


class _Pm200fr20CfgLineStartupIndex_Type(Integer32):
    """Custom type pm200fr20CfgLineStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20CfgLineStartupIndex_Type.__name__ = "Integer32"
_Pm200fr20CfgLineStartupIndex_Object = MibTableColumn
pm200fr20CfgLineStartupIndex = _Pm200fr20CfgLineStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 2, 2, 1, 1),
    _Pm200fr20CfgLineStartupIndex_Type()
)
pm200fr20CfgLineStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CfgLineStartupIndex.setStatus("current")


class _Pm200fr20CfgSystConfLinePortn_Type(Unsigned32):
    """Custom type pm200fr20CfgSystConfLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200fr20CfgSystConfLinePortn_Type.__name__ = "Unsigned32"
_Pm200fr20CfgSystConfLinePortn_Object = MibTableColumn
pm200fr20CfgSystConfLinePortn = _Pm200fr20CfgSystConfLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 2, 2, 1, 3),
    _Pm200fr20CfgSystConfLinePortn_Type()
)
pm200fr20CfgSystConfLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CfgSystConfLinePortn.setStatus("current")


class _Pm200fr20CfgOptionsLinePortn_Type(Unsigned32):
    """Custom type pm200fr20CfgOptionsLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200fr20CfgOptionsLinePortn_Type.__name__ = "Unsigned32"
_Pm200fr20CfgOptionsLinePortn_Object = MibTableColumn
pm200fr20CfgOptionsLinePortn = _Pm200fr20CfgOptionsLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 2, 2, 1, 14),
    _Pm200fr20CfgOptionsLinePortn_Type()
)
pm200fr20CfgOptionsLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CfgOptionsLinePortn.setStatus("current")
_Pm200fr20CfgXfpTable_Object = MibTable
pm200fr20CfgXfpTable = _Pm200fr20CfgXfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 2, 3)
)
if mibBuilder.loadTexts:
    pm200fr20CfgXfpTable.setStatus("current")
_Pm200fr20CfgXfpEntry_Object = MibTableRow
pm200fr20CfgXfpEntry = _Pm200fr20CfgXfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 2, 3, 1)
)
pm200fr20CfgXfpEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20CfgXfpIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20CfgXfpEntry.setStatus("current")


class _Pm200fr20CfgXfpIndex_Type(Integer32):
    """Custom type pm200fr20CfgXfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20CfgXfpIndex_Type.__name__ = "Integer32"
_Pm200fr20CfgXfpIndex_Object = MibTableColumn
pm200fr20CfgXfpIndex = _Pm200fr20CfgXfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 2, 3, 1, 1),
    _Pm200fr20CfgXfpIndex_Type()
)
pm200fr20CfgXfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CfgXfpIndex.setStatus("current")


class _Pm200fr20CfgSystConfMsaLinePortn_Type(Unsigned32):
    """Custom type pm200fr20CfgSystConfMsaLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200fr20CfgSystConfMsaLinePortn_Type.__name__ = "Unsigned32"
_Pm200fr20CfgSystConfMsaLinePortn_Object = MibTableColumn
pm200fr20CfgSystConfMsaLinePortn = _Pm200fr20CfgSystConfMsaLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 2, 3, 1, 3),
    _Pm200fr20CfgSystConfMsaLinePortn_Type()
)
pm200fr20CfgSystConfMsaLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CfgSystConfMsaLinePortn.setStatus("current")
_Pm200fr20CfgLabels_ObjectIdentity = ObjectIdentity
pm200fr20CfgLabels = _Pm200fr20CfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 3)
)
_Pm200fr20CfgLabelclientTable_Object = MibTable
pm200fr20CfgLabelclientTable = _Pm200fr20CfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 3, 1)
)
if mibBuilder.loadTexts:
    pm200fr20CfgLabelclientTable.setStatus("current")
_Pm200fr20CfgLabelclientEntry_Object = MibTableRow
pm200fr20CfgLabelclientEntry = _Pm200fr20CfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 3, 1, 1)
)
pm200fr20CfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20CfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20CfgLabelclientEntry.setStatus("current")


class _Pm200fr20CfgLabelclientIndex_Type(Integer32):
    """Custom type pm200fr20CfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20CfgLabelclientIndex_Type.__name__ = "Integer32"
_Pm200fr20CfgLabelclientIndex_Object = MibTableColumn
pm200fr20CfgLabelclientIndex = _Pm200fr20CfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 3, 1, 1, 1),
    _Pm200fr20CfgLabelclientIndex_Type()
)
pm200fr20CfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CfgLabelclientIndex.setStatus("current")


class _Pm200fr20CfgLabelclientPortn_Type(DisplayString):
    """Custom type pm200fr20CfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm200fr20CfgLabelclientPortn_Type.__name__ = "DisplayString"
_Pm200fr20CfgLabelclientPortn_Object = MibTableColumn
pm200fr20CfgLabelclientPortn = _Pm200fr20CfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 3, 1, 1, 3),
    _Pm200fr20CfgLabelclientPortn_Type()
)
pm200fr20CfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CfgLabelclientPortn.setStatus("current")
_Pm200fr20CfgLabellineTable_Object = MibTable
pm200fr20CfgLabellineTable = _Pm200fr20CfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 3, 2)
)
if mibBuilder.loadTexts:
    pm200fr20CfgLabellineTable.setStatus("current")
_Pm200fr20CfgLabellineEntry_Object = MibTableRow
pm200fr20CfgLabellineEntry = _Pm200fr20CfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 3, 2, 1)
)
pm200fr20CfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20CfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20CfgLabellineEntry.setStatus("current")


class _Pm200fr20CfgLabellineIndex_Type(Integer32):
    """Custom type pm200fr20CfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20CfgLabellineIndex_Type.__name__ = "Integer32"
_Pm200fr20CfgLabellineIndex_Object = MibTableColumn
pm200fr20CfgLabellineIndex = _Pm200fr20CfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 3, 2, 1, 1),
    _Pm200fr20CfgLabellineIndex_Type()
)
pm200fr20CfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CfgLabellineIndex.setStatus("current")


class _Pm200fr20CfgLabellinePortn_Type(DisplayString):
    """Custom type pm200fr20CfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm200fr20CfgLabellinePortn_Type.__name__ = "DisplayString"
_Pm200fr20CfgLabellinePortn_Object = MibTableColumn
pm200fr20CfgLabellinePortn = _Pm200fr20CfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 3, 2, 1, 3),
    _Pm200fr20CfgLabellinePortn_Type()
)
pm200fr20CfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CfgLabellinePortn.setStatus("current")
_Pm200fr20CfgStartuptlh_ObjectIdentity = ObjectIdentity
pm200fr20CfgStartuptlh = _Pm200fr20CfgStartuptlh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 4)
)
_Pm200fr20CfgOtxtlhTable_Object = MibTable
pm200fr20CfgOtxtlhTable = _Pm200fr20CfgOtxtlhTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 4, 1)
)
if mibBuilder.loadTexts:
    pm200fr20CfgOtxtlhTable.setStatus("current")
_Pm200fr20CfgOtxtlhEntry_Object = MibTableRow
pm200fr20CfgOtxtlhEntry = _Pm200fr20CfgOtxtlhEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 4, 1, 1)
)
pm200fr20CfgOtxtlhEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20CfgOtxtlhIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20CfgOtxtlhEntry.setStatus("current")


class _Pm200fr20CfgOtxtlhIndex_Type(Integer32):
    """Custom type pm200fr20CfgOtxtlhIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20CfgOtxtlhIndex_Type.__name__ = "Integer32"
_Pm200fr20CfgOtxtlhIndex_Object = MibTableColumn
pm200fr20CfgOtxtlhIndex = _Pm200fr20CfgOtxtlhIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 4, 1, 1, 1),
    _Pm200fr20CfgOtxtlhIndex_Type()
)
pm200fr20CfgOtxtlhIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CfgOtxtlhIndex.setStatus("current")


class _Pm200fr20CfgLinePwrLaserPortn_Type(Unsigned32):
    """Custom type pm200fr20CfgLinePwrLaserPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200fr20CfgLinePwrLaserPortn_Type.__name__ = "Unsigned32"
_Pm200fr20CfgLinePwrLaserPortn_Object = MibTableColumn
pm200fr20CfgLinePwrLaserPortn = _Pm200fr20CfgLinePwrLaserPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 4, 1, 1, 6),
    _Pm200fr20CfgLinePwrLaserPortn_Type()
)
pm200fr20CfgLinePwrLaserPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CfgLinePwrLaserPortn.setStatus("current")


class _Pm200fr20CfgLineFCurrentPortn_Type(Unsigned32):
    """Custom type pm200fr20CfgLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200fr20CfgLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Pm200fr20CfgLineFCurrentPortn_Object = MibTableColumn
pm200fr20CfgLineFCurrentPortn = _Pm200fr20CfgLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 4, 1, 1, 7),
    _Pm200fr20CfgLineFCurrentPortn_Type()
)
pm200fr20CfgLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CfgLineFCurrentPortn.setStatus("current")


class _Pm200fr20CfgLineGridCurrentPortn_Type(Unsigned32):
    """Custom type pm200fr20CfgLineGridCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200fr20CfgLineGridCurrentPortn_Type.__name__ = "Unsigned32"
_Pm200fr20CfgLineGridCurrentPortn_Object = MibTableColumn
pm200fr20CfgLineGridCurrentPortn = _Pm200fr20CfgLineGridCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 4, 1, 1, 8),
    _Pm200fr20CfgLineGridCurrentPortn_Type()
)
pm200fr20CfgLineGridCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CfgLineGridCurrentPortn.setStatus("current")


class _Pm200fr20CfgFPortn_Type(Unsigned32):
    """Custom type pm200fr20CfgFPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200fr20CfgFPortn_Type.__name__ = "Unsigned32"
_Pm200fr20CfgFPortn_Object = MibTableColumn
pm200fr20CfgFPortn = _Pm200fr20CfgFPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 4, 1, 1, 9),
    _Pm200fr20CfgFPortn_Type()
)
pm200fr20CfgFPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CfgFPortn.setStatus("current")


class _Pm200fr20CfgRxLineFCurrentPortn_Type(Unsigned32):
    """Custom type pm200fr20CfgRxLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200fr20CfgRxLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Pm200fr20CfgRxLineFCurrentPortn_Object = MibTableColumn
pm200fr20CfgRxLineFCurrentPortn = _Pm200fr20CfgRxLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 4, 1, 1, 10),
    _Pm200fr20CfgRxLineFCurrentPortn_Type()
)
pm200fr20CfgRxLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CfgRxLineFCurrentPortn.setStatus("current")
_Pm200fr20CfgOther_ObjectIdentity = ObjectIdentity
pm200fr20CfgOther = _Pm200fr20CfgOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 5)
)
_Pm200fr20tablemoduleOther_ObjectIdentity = ObjectIdentity
pm200fr20tablemoduleOther = _Pm200fr20tablemoduleOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 5, 1)
)


class _Pm200fr20Cfgmode_Type(Unsigned32):
    """Custom type pm200fr20Cfgmode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200fr20Cfgmode_Type.__name__ = "Unsigned32"
_Pm200fr20Cfgmode_Object = MibScalar
pm200fr20Cfgmode = _Pm200fr20Cfgmode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 5, 1, 2),
    _Pm200fr20Cfgmode_Type()
)
pm200fr20Cfgmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20Cfgmode.setStatus("current")


class _Pm200fr20CfgfanLowSpeedThreshold_Type(Unsigned32):
    """Custom type pm200fr20CfgfanLowSpeedThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200fr20CfgfanLowSpeedThreshold_Type.__name__ = "Unsigned32"
_Pm200fr20CfgfanLowSpeedThreshold_Object = MibScalar
pm200fr20CfgfanLowSpeedThreshold = _Pm200fr20CfgfanLowSpeedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 5, 1, 3),
    _Pm200fr20CfgfanLowSpeedThreshold_Type()
)
pm200fr20CfgfanLowSpeedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CfgfanLowSpeedThreshold.setStatus("current")


class _Pm200fr20CfgfanHighSpeedThreshold_Type(Unsigned32):
    """Custom type pm200fr20CfgfanHighSpeedThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200fr20CfgfanHighSpeedThreshold_Type.__name__ = "Unsigned32"
_Pm200fr20CfgfanHighSpeedThreshold_Object = MibScalar
pm200fr20CfgfanHighSpeedThreshold = _Pm200fr20CfgfanHighSpeedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 5, 1, 4),
    _Pm200fr20CfgfanHighSpeedThreshold_Type()
)
pm200fr20CfgfanHighSpeedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CfgfanHighSpeedThreshold.setStatus("current")


class _Pm200fr20CfgprotocolMode_Type(Unsigned32):
    """Custom type pm200fr20CfgprotocolMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200fr20CfgprotocolMode_Type.__name__ = "Unsigned32"
_Pm200fr20CfgprotocolMode_Object = MibScalar
pm200fr20CfgprotocolMode = _Pm200fr20CfgprotocolMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 5, 1, 5),
    _Pm200fr20CfgprotocolMode_Type()
)
pm200fr20CfgprotocolMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CfgprotocolMode.setStatus("current")
_Pm200fr20CfgStartuptablefive_ObjectIdentity = ObjectIdentity
pm200fr20CfgStartuptablefive = _Pm200fr20CfgStartuptablefive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 6)
)
_Pm200fr20CfgOtxtlhcapabilitiesTable_Object = MibTable
pm200fr20CfgOtxtlhcapabilitiesTable = _Pm200fr20CfgOtxtlhcapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 6, 1)
)
if mibBuilder.loadTexts:
    pm200fr20CfgOtxtlhcapabilitiesTable.setStatus("current")
_Pm200fr20CfgOtxtlhcapabilitiesEntry_Object = MibTableRow
pm200fr20CfgOtxtlhcapabilitiesEntry = _Pm200fr20CfgOtxtlhcapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 6, 1, 1)
)
pm200fr20CfgOtxtlhcapabilitiesEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20CfgOtxtlhcapabilitiesIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20CfgOtxtlhcapabilitiesEntry.setStatus("current")


class _Pm200fr20CfgOtxtlhcapabilitiesIndex_Type(Integer32):
    """Custom type pm200fr20CfgOtxtlhcapabilitiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20CfgOtxtlhcapabilitiesIndex_Type.__name__ = "Integer32"
_Pm200fr20CfgOtxtlhcapabilitiesIndex_Object = MibTableColumn
pm200fr20CfgOtxtlhcapabilitiesIndex = _Pm200fr20CfgOtxtlhcapabilitiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 6, 1, 1, 1),
    _Pm200fr20CfgOtxtlhcapabilitiesIndex_Type()
)
pm200fr20CfgOtxtlhcapabilitiesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CfgOtxtlhcapabilitiesIndex.setStatus("current")


class _Pm200fr20CfgComponentTypePortn_Type(Unsigned32):
    """Custom type pm200fr20CfgComponentTypePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200fr20CfgComponentTypePortn_Type.__name__ = "Unsigned32"
_Pm200fr20CfgComponentTypePortn_Object = MibTableColumn
pm200fr20CfgComponentTypePortn = _Pm200fr20CfgComponentTypePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 6, 1, 1, 3),
    _Pm200fr20CfgComponentTypePortn_Type()
)
pm200fr20CfgComponentTypePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CfgComponentTypePortn.setStatus("current")


class _Pm200fr20CfgMiscellaneousPortn_Type(Unsigned32):
    """Custom type pm200fr20CfgMiscellaneousPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200fr20CfgMiscellaneousPortn_Type.__name__ = "Unsigned32"
_Pm200fr20CfgMiscellaneousPortn_Object = MibTableColumn
pm200fr20CfgMiscellaneousPortn = _Pm200fr20CfgMiscellaneousPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 6, 1, 1, 4),
    _Pm200fr20CfgMiscellaneousPortn_Type()
)
pm200fr20CfgMiscellaneousPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CfgMiscellaneousPortn.setStatus("current")


class _Pm200fr20CfgFirstChannelPortn_Type(Unsigned32):
    """Custom type pm200fr20CfgFirstChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200fr20CfgFirstChannelPortn_Type.__name__ = "Unsigned32"
_Pm200fr20CfgFirstChannelPortn_Object = MibTableColumn
pm200fr20CfgFirstChannelPortn = _Pm200fr20CfgFirstChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 6, 1, 1, 5),
    _Pm200fr20CfgFirstChannelPortn_Type()
)
pm200fr20CfgFirstChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CfgFirstChannelPortn.setStatus("current")


class _Pm200fr20CfgLastChannelPortn_Type(Unsigned32):
    """Custom type pm200fr20CfgLastChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200fr20CfgLastChannelPortn_Type.__name__ = "Unsigned32"
_Pm200fr20CfgLastChannelPortn_Object = MibTableColumn
pm200fr20CfgLastChannelPortn = _Pm200fr20CfgLastChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 6, 1, 1, 6),
    _Pm200fr20CfgLastChannelPortn_Type()
)
pm200fr20CfgLastChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CfgLastChannelPortn.setStatus("current")


class _Pm200fr20CfgGridPortn_Type(Unsigned32):
    """Custom type pm200fr20CfgGridPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200fr20CfgGridPortn_Type.__name__ = "Unsigned32"
_Pm200fr20CfgGridPortn_Object = MibTableColumn
pm200fr20CfgGridPortn = _Pm200fr20CfgGridPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 6, 1, 1, 7),
    _Pm200fr20CfgGridPortn_Type()
)
pm200fr20CfgGridPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20CfgGridPortn.setStatus("current")
_Pm200fr20CfgWriteConfiguration_Type = EkiOnOff
_Pm200fr20CfgWriteConfiguration_Object = MibScalar
pm200fr20CfgWriteConfiguration = _Pm200fr20CfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 9, 257),
    _Pm200fr20CfgWriteConfiguration_Type()
)
pm200fr20CfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20CfgWriteConfiguration.setStatus("current")
_Pm200fr20traps_ObjectIdentity = ObjectIdentity
pm200fr20traps = _Pm200fr20traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 10)
)


class _Pm200fr20trapPortNumber_Type(Integer32):
    """Custom type pm200fr20trapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm200fr20trapPortNumber_Type.__name__ = "Integer32"
_Pm200fr20trapPortNumber_Object = MibScalar
pm200fr20trapPortNumber = _Pm200fr20trapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 10, 2),
    _Pm200fr20trapPortNumber_Type()
)
pm200fr20trapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20trapPortNumber.setStatus("current")


class _Pm200fr20trapLineNumber_Type(Integer32):
    """Custom type pm200fr20trapLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm200fr20trapLineNumber_Type.__name__ = "Integer32"
_Pm200fr20trapLineNumber_Object = MibScalar
pm200fr20trapLineNumber = _Pm200fr20trapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 10, 3),
    _Pm200fr20trapLineNumber_Type()
)
pm200fr20trapLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20trapLineNumber.setStatus("current")


class _Pm200fr20trapBoardNumber_Type(Integer32):
    """Custom type pm200fr20trapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm200fr20trapBoardNumber_Type.__name__ = "Integer32"
_Pm200fr20trapBoardNumber_Object = MibScalar
pm200fr20trapBoardNumber = _Pm200fr20trapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 10, 4),
    _Pm200fr20trapBoardNumber_Type()
)
pm200fr20trapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20trapBoardNumber.setStatus("current")
_Pm200fr20Monitoring_ObjectIdentity = ObjectIdentity
pm200fr20Monitoring = _Pm200fr20Monitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11)
)
_Pm200fr20MonOther_ObjectIdentity = ObjectIdentity
pm200fr20MonOther = _Pm200fr20MonOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 1)
)
_Pm200fr20MonRmon_ObjectIdentity = ObjectIdentity
pm200fr20MonRmon = _Pm200fr20MonRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 1, 3)
)
_Pm200fr20MonClient_ObjectIdentity = ObjectIdentity
pm200fr20MonClient = _Pm200fr20MonClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2)
)
_Pm200fr20MonClientRmonCounter_ObjectIdentity = ObjectIdentity
pm200fr20MonClientRmonCounter = _Pm200fr20MonClientRmonCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4)
)
_Pm200fr20MonupRmonBytesCounterClientInputTable_Object = MibTable
pm200fr20MonupRmonBytesCounterClientInputTable = _Pm200fr20MonupRmonBytesCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 16)
)
if mibBuilder.loadTexts:
    pm200fr20MonupRmonBytesCounterClientInputTable.setStatus("current")
_Pm200fr20MonupRmonBytesCounterClientInputEntry_Object = MibTableRow
pm200fr20MonupRmonBytesCounterClientInputEntry = _Pm200fr20MonupRmonBytesCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 16, 1)
)
pm200fr20MonupRmonBytesCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20MonupRmonBytesCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20MonupRmonBytesCounterClientInputEntry.setStatus("current")


class _Pm200fr20MonupRmonBytesCounterClientInputIndex_Type(Integer32):
    """Custom type pm200fr20MonupRmonBytesCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20MonupRmonBytesCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm200fr20MonupRmonBytesCounterClientInputIndex_Object = MibTableColumn
pm200fr20MonupRmonBytesCounterClientInputIndex = _Pm200fr20MonupRmonBytesCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 16, 1, 1),
    _Pm200fr20MonupRmonBytesCounterClientInputIndex_Type()
)
pm200fr20MonupRmonBytesCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MonupRmonBytesCounterClientInputIndex.setStatus("current")
_Pm200fr20MonupRmonBytesCounterClientInputValuePortn_Type = Counter64
_Pm200fr20MonupRmonBytesCounterClientInputValuePortn_Object = MibTableColumn
pm200fr20MonupRmonBytesCounterClientInputValuePortn = _Pm200fr20MonupRmonBytesCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 16, 1, 2),
    _Pm200fr20MonupRmonBytesCounterClientInputValuePortn_Type()
)
pm200fr20MonupRmonBytesCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MonupRmonBytesCounterClientInputValuePortn.setStatus("current")
_Pm200fr20MonupRmonBytesCounterClientInputErrorPortn_Type = EkiOnOff
_Pm200fr20MonupRmonBytesCounterClientInputErrorPortn_Object = MibTableColumn
pm200fr20MonupRmonBytesCounterClientInputErrorPortn = _Pm200fr20MonupRmonBytesCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 16, 1, 3),
    _Pm200fr20MonupRmonBytesCounterClientInputErrorPortn_Type()
)
pm200fr20MonupRmonBytesCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MonupRmonBytesCounterClientInputErrorPortn.setStatus("current")
_Pm200fr20MonupRmonBytesCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm200fr20MonupRmonBytesCounterClientInputOverloadPortn_Object = MibTableColumn
pm200fr20MonupRmonBytesCounterClientInputOverloadPortn = _Pm200fr20MonupRmonBytesCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 16, 1, 4),
    _Pm200fr20MonupRmonBytesCounterClientInputOverloadPortn_Type()
)
pm200fr20MonupRmonBytesCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MonupRmonBytesCounterClientInputOverloadPortn.setStatus("current")
_Pm200fr20MonupRmonCrcErrorsCounterClientInputTable_Object = MibTable
pm200fr20MonupRmonCrcErrorsCounterClientInputTable = _Pm200fr20MonupRmonCrcErrorsCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 48)
)
if mibBuilder.loadTexts:
    pm200fr20MonupRmonCrcErrorsCounterClientInputTable.setStatus("current")
_Pm200fr20MonupRmonCrcErrorsCounterClientInputEntry_Object = MibTableRow
pm200fr20MonupRmonCrcErrorsCounterClientInputEntry = _Pm200fr20MonupRmonCrcErrorsCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 48, 1)
)
pm200fr20MonupRmonCrcErrorsCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20MonupRmonCrcErrorsCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20MonupRmonCrcErrorsCounterClientInputEntry.setStatus("current")


class _Pm200fr20MonupRmonCrcErrorsCounterClientInputIndex_Type(Integer32):
    """Custom type pm200fr20MonupRmonCrcErrorsCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20MonupRmonCrcErrorsCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm200fr20MonupRmonCrcErrorsCounterClientInputIndex_Object = MibTableColumn
pm200fr20MonupRmonCrcErrorsCounterClientInputIndex = _Pm200fr20MonupRmonCrcErrorsCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 48, 1, 1),
    _Pm200fr20MonupRmonCrcErrorsCounterClientInputIndex_Type()
)
pm200fr20MonupRmonCrcErrorsCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MonupRmonCrcErrorsCounterClientInputIndex.setStatus("current")
_Pm200fr20MonupRmonCrcErrorsCounterClientInputValuePortn_Type = Counter64
_Pm200fr20MonupRmonCrcErrorsCounterClientInputValuePortn_Object = MibTableColumn
pm200fr20MonupRmonCrcErrorsCounterClientInputValuePortn = _Pm200fr20MonupRmonCrcErrorsCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 48, 1, 2),
    _Pm200fr20MonupRmonCrcErrorsCounterClientInputValuePortn_Type()
)
pm200fr20MonupRmonCrcErrorsCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MonupRmonCrcErrorsCounterClientInputValuePortn.setStatus("current")
_Pm200fr20MonupRmonCrcErrorsCounterClientInputErrorPortn_Type = EkiOnOff
_Pm200fr20MonupRmonCrcErrorsCounterClientInputErrorPortn_Object = MibTableColumn
pm200fr20MonupRmonCrcErrorsCounterClientInputErrorPortn = _Pm200fr20MonupRmonCrcErrorsCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 48, 1, 3),
    _Pm200fr20MonupRmonCrcErrorsCounterClientInputErrorPortn_Type()
)
pm200fr20MonupRmonCrcErrorsCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MonupRmonCrcErrorsCounterClientInputErrorPortn.setStatus("current")
_Pm200fr20MonupRmonCrcErrorsCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm200fr20MonupRmonCrcErrorsCounterClientInputOverloadPortn_Object = MibTableColumn
pm200fr20MonupRmonCrcErrorsCounterClientInputOverloadPortn = _Pm200fr20MonupRmonCrcErrorsCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 48, 1, 4),
    _Pm200fr20MonupRmonCrcErrorsCounterClientInputOverloadPortn_Type()
)
pm200fr20MonupRmonCrcErrorsCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MonupRmonCrcErrorsCounterClientInputOverloadPortn.setStatus("current")
_Pm200fr20MonupRmonPacketsCounterClientInputTable_Object = MibTable
pm200fr20MonupRmonPacketsCounterClientInputTable = _Pm200fr20MonupRmonPacketsCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 80)
)
if mibBuilder.loadTexts:
    pm200fr20MonupRmonPacketsCounterClientInputTable.setStatus("current")
_Pm200fr20MonupRmonPacketsCounterClientInputEntry_Object = MibTableRow
pm200fr20MonupRmonPacketsCounterClientInputEntry = _Pm200fr20MonupRmonPacketsCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 80, 1)
)
pm200fr20MonupRmonPacketsCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20MonupRmonPacketsCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20MonupRmonPacketsCounterClientInputEntry.setStatus("current")


class _Pm200fr20MonupRmonPacketsCounterClientInputIndex_Type(Integer32):
    """Custom type pm200fr20MonupRmonPacketsCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20MonupRmonPacketsCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm200fr20MonupRmonPacketsCounterClientInputIndex_Object = MibTableColumn
pm200fr20MonupRmonPacketsCounterClientInputIndex = _Pm200fr20MonupRmonPacketsCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 80, 1, 1),
    _Pm200fr20MonupRmonPacketsCounterClientInputIndex_Type()
)
pm200fr20MonupRmonPacketsCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MonupRmonPacketsCounterClientInputIndex.setStatus("current")
_Pm200fr20MonupRmonPacketsCounterClientInputValuePortn_Type = Counter64
_Pm200fr20MonupRmonPacketsCounterClientInputValuePortn_Object = MibTableColumn
pm200fr20MonupRmonPacketsCounterClientInputValuePortn = _Pm200fr20MonupRmonPacketsCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 80, 1, 2),
    _Pm200fr20MonupRmonPacketsCounterClientInputValuePortn_Type()
)
pm200fr20MonupRmonPacketsCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MonupRmonPacketsCounterClientInputValuePortn.setStatus("current")
_Pm200fr20MonupRmonPacketsCounterClientInputErrorPortn_Type = EkiOnOff
_Pm200fr20MonupRmonPacketsCounterClientInputErrorPortn_Object = MibTableColumn
pm200fr20MonupRmonPacketsCounterClientInputErrorPortn = _Pm200fr20MonupRmonPacketsCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 80, 1, 3),
    _Pm200fr20MonupRmonPacketsCounterClientInputErrorPortn_Type()
)
pm200fr20MonupRmonPacketsCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MonupRmonPacketsCounterClientInputErrorPortn.setStatus("current")
_Pm200fr20MonupRmonPacketsCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm200fr20MonupRmonPacketsCounterClientInputOverloadPortn_Object = MibTableColumn
pm200fr20MonupRmonPacketsCounterClientInputOverloadPortn = _Pm200fr20MonupRmonPacketsCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 80, 1, 4),
    _Pm200fr20MonupRmonPacketsCounterClientInputOverloadPortn_Type()
)
pm200fr20MonupRmonPacketsCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MonupRmonPacketsCounterClientInputOverloadPortn.setStatus("current")
_Pm200fr20MonupRmonBroadcastCounterClientInputTable_Object = MibTable
pm200fr20MonupRmonBroadcastCounterClientInputTable = _Pm200fr20MonupRmonBroadcastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 112)
)
if mibBuilder.loadTexts:
    pm200fr20MonupRmonBroadcastCounterClientInputTable.setStatus("current")
_Pm200fr20MonupRmonBroadcastCounterClientInputEntry_Object = MibTableRow
pm200fr20MonupRmonBroadcastCounterClientInputEntry = _Pm200fr20MonupRmonBroadcastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 112, 1)
)
pm200fr20MonupRmonBroadcastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20MonupRmonBroadcastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20MonupRmonBroadcastCounterClientInputEntry.setStatus("current")


class _Pm200fr20MonupRmonBroadcastCounterClientInputIndex_Type(Integer32):
    """Custom type pm200fr20MonupRmonBroadcastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20MonupRmonBroadcastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm200fr20MonupRmonBroadcastCounterClientInputIndex_Object = MibTableColumn
pm200fr20MonupRmonBroadcastCounterClientInputIndex = _Pm200fr20MonupRmonBroadcastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 112, 1, 1),
    _Pm200fr20MonupRmonBroadcastCounterClientInputIndex_Type()
)
pm200fr20MonupRmonBroadcastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MonupRmonBroadcastCounterClientInputIndex.setStatus("current")
_Pm200fr20MonupRmonBroadcastCounterClientInputValuePortn_Type = Counter64
_Pm200fr20MonupRmonBroadcastCounterClientInputValuePortn_Object = MibTableColumn
pm200fr20MonupRmonBroadcastCounterClientInputValuePortn = _Pm200fr20MonupRmonBroadcastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 112, 1, 2),
    _Pm200fr20MonupRmonBroadcastCounterClientInputValuePortn_Type()
)
pm200fr20MonupRmonBroadcastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MonupRmonBroadcastCounterClientInputValuePortn.setStatus("current")
_Pm200fr20MonupRmonBroadcastCounterClientInputErrorPortn_Type = EkiOnOff
_Pm200fr20MonupRmonBroadcastCounterClientInputErrorPortn_Object = MibTableColumn
pm200fr20MonupRmonBroadcastCounterClientInputErrorPortn = _Pm200fr20MonupRmonBroadcastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 112, 1, 3),
    _Pm200fr20MonupRmonBroadcastCounterClientInputErrorPortn_Type()
)
pm200fr20MonupRmonBroadcastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MonupRmonBroadcastCounterClientInputErrorPortn.setStatus("current")
_Pm200fr20MonupRmonBroadcastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm200fr20MonupRmonBroadcastCounterClientInputOverloadPortn_Object = MibTableColumn
pm200fr20MonupRmonBroadcastCounterClientInputOverloadPortn = _Pm200fr20MonupRmonBroadcastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 112, 1, 4),
    _Pm200fr20MonupRmonBroadcastCounterClientInputOverloadPortn_Type()
)
pm200fr20MonupRmonBroadcastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MonupRmonBroadcastCounterClientInputOverloadPortn.setStatus("current")
_Pm200fr20MonupRmonMulticastCounterClientInputTable_Object = MibTable
pm200fr20MonupRmonMulticastCounterClientInputTable = _Pm200fr20MonupRmonMulticastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 144)
)
if mibBuilder.loadTexts:
    pm200fr20MonupRmonMulticastCounterClientInputTable.setStatus("current")
_Pm200fr20MonupRmonMulticastCounterClientInputEntry_Object = MibTableRow
pm200fr20MonupRmonMulticastCounterClientInputEntry = _Pm200fr20MonupRmonMulticastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 144, 1)
)
pm200fr20MonupRmonMulticastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20MonupRmonMulticastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20MonupRmonMulticastCounterClientInputEntry.setStatus("current")


class _Pm200fr20MonupRmonMulticastCounterClientInputIndex_Type(Integer32):
    """Custom type pm200fr20MonupRmonMulticastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20MonupRmonMulticastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm200fr20MonupRmonMulticastCounterClientInputIndex_Object = MibTableColumn
pm200fr20MonupRmonMulticastCounterClientInputIndex = _Pm200fr20MonupRmonMulticastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 144, 1, 1),
    _Pm200fr20MonupRmonMulticastCounterClientInputIndex_Type()
)
pm200fr20MonupRmonMulticastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MonupRmonMulticastCounterClientInputIndex.setStatus("current")
_Pm200fr20MonupRmonMulticastCounterClientInputValuePortn_Type = Counter64
_Pm200fr20MonupRmonMulticastCounterClientInputValuePortn_Object = MibTableColumn
pm200fr20MonupRmonMulticastCounterClientInputValuePortn = _Pm200fr20MonupRmonMulticastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 144, 1, 2),
    _Pm200fr20MonupRmonMulticastCounterClientInputValuePortn_Type()
)
pm200fr20MonupRmonMulticastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MonupRmonMulticastCounterClientInputValuePortn.setStatus("current")
_Pm200fr20MonupRmonMulticastCounterClientInputErrorPortn_Type = EkiOnOff
_Pm200fr20MonupRmonMulticastCounterClientInputErrorPortn_Object = MibTableColumn
pm200fr20MonupRmonMulticastCounterClientInputErrorPortn = _Pm200fr20MonupRmonMulticastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 144, 1, 3),
    _Pm200fr20MonupRmonMulticastCounterClientInputErrorPortn_Type()
)
pm200fr20MonupRmonMulticastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MonupRmonMulticastCounterClientInputErrorPortn.setStatus("current")
_Pm200fr20MonupRmonMulticastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm200fr20MonupRmonMulticastCounterClientInputOverloadPortn_Object = MibTableColumn
pm200fr20MonupRmonMulticastCounterClientInputOverloadPortn = _Pm200fr20MonupRmonMulticastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 144, 1, 4),
    _Pm200fr20MonupRmonMulticastCounterClientInputOverloadPortn_Type()
)
pm200fr20MonupRmonMulticastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MonupRmonMulticastCounterClientInputOverloadPortn.setStatus("current")
_Pm200fr20MonupRmonPauseFrameCounterClientInputTable_Object = MibTable
pm200fr20MonupRmonPauseFrameCounterClientInputTable = _Pm200fr20MonupRmonPauseFrameCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 176)
)
if mibBuilder.loadTexts:
    pm200fr20MonupRmonPauseFrameCounterClientInputTable.setStatus("current")
_Pm200fr20MonupRmonPauseFrameCounterClientInputEntry_Object = MibTableRow
pm200fr20MonupRmonPauseFrameCounterClientInputEntry = _Pm200fr20MonupRmonPauseFrameCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 176, 1)
)
pm200fr20MonupRmonPauseFrameCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20MonupRmonPauseFrameCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20MonupRmonPauseFrameCounterClientInputEntry.setStatus("current")


class _Pm200fr20MonupRmonPauseFrameCounterClientInputIndex_Type(Integer32):
    """Custom type pm200fr20MonupRmonPauseFrameCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20MonupRmonPauseFrameCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm200fr20MonupRmonPauseFrameCounterClientInputIndex_Object = MibTableColumn
pm200fr20MonupRmonPauseFrameCounterClientInputIndex = _Pm200fr20MonupRmonPauseFrameCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 176, 1, 1),
    _Pm200fr20MonupRmonPauseFrameCounterClientInputIndex_Type()
)
pm200fr20MonupRmonPauseFrameCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MonupRmonPauseFrameCounterClientInputIndex.setStatus("current")
_Pm200fr20MonupRmonPauseFrameCounterClientInputValuePortn_Type = Counter64
_Pm200fr20MonupRmonPauseFrameCounterClientInputValuePortn_Object = MibTableColumn
pm200fr20MonupRmonPauseFrameCounterClientInputValuePortn = _Pm200fr20MonupRmonPauseFrameCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 176, 1, 2),
    _Pm200fr20MonupRmonPauseFrameCounterClientInputValuePortn_Type()
)
pm200fr20MonupRmonPauseFrameCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MonupRmonPauseFrameCounterClientInputValuePortn.setStatus("current")
_Pm200fr20MonupRmonPauseFrameCounterClientInputErrorPortn_Type = EkiOnOff
_Pm200fr20MonupRmonPauseFrameCounterClientInputErrorPortn_Object = MibTableColumn
pm200fr20MonupRmonPauseFrameCounterClientInputErrorPortn = _Pm200fr20MonupRmonPauseFrameCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 176, 1, 3),
    _Pm200fr20MonupRmonPauseFrameCounterClientInputErrorPortn_Type()
)
pm200fr20MonupRmonPauseFrameCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MonupRmonPauseFrameCounterClientInputErrorPortn.setStatus("current")
_Pm200fr20MonupRmonPauseFrameCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm200fr20MonupRmonPauseFrameCounterClientInputOverloadPortn_Object = MibTableColumn
pm200fr20MonupRmonPauseFrameCounterClientInputOverloadPortn = _Pm200fr20MonupRmonPauseFrameCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 176, 1, 4),
    _Pm200fr20MonupRmonPauseFrameCounterClientInputOverloadPortn_Type()
)
pm200fr20MonupRmonPauseFrameCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MonupRmonPauseFrameCounterClientInputOverloadPortn.setStatus("current")
_Pm200fr20MonupRmonUnicastCounterClientInputTable_Object = MibTable
pm200fr20MonupRmonUnicastCounterClientInputTable = _Pm200fr20MonupRmonUnicastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 304)
)
if mibBuilder.loadTexts:
    pm200fr20MonupRmonUnicastCounterClientInputTable.setStatus("current")
_Pm200fr20MonupRmonUnicastCounterClientInputEntry_Object = MibTableRow
pm200fr20MonupRmonUnicastCounterClientInputEntry = _Pm200fr20MonupRmonUnicastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 304, 1)
)
pm200fr20MonupRmonUnicastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20MonupRmonUnicastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20MonupRmonUnicastCounterClientInputEntry.setStatus("current")


class _Pm200fr20MonupRmonUnicastCounterClientInputIndex_Type(Integer32):
    """Custom type pm200fr20MonupRmonUnicastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20MonupRmonUnicastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm200fr20MonupRmonUnicastCounterClientInputIndex_Object = MibTableColumn
pm200fr20MonupRmonUnicastCounterClientInputIndex = _Pm200fr20MonupRmonUnicastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 304, 1, 1),
    _Pm200fr20MonupRmonUnicastCounterClientInputIndex_Type()
)
pm200fr20MonupRmonUnicastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MonupRmonUnicastCounterClientInputIndex.setStatus("current")
_Pm200fr20MonupRmonUnicastCounterClientInputValuePortn_Type = Counter64
_Pm200fr20MonupRmonUnicastCounterClientInputValuePortn_Object = MibTableColumn
pm200fr20MonupRmonUnicastCounterClientInputValuePortn = _Pm200fr20MonupRmonUnicastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 304, 1, 2),
    _Pm200fr20MonupRmonUnicastCounterClientInputValuePortn_Type()
)
pm200fr20MonupRmonUnicastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MonupRmonUnicastCounterClientInputValuePortn.setStatus("current")
_Pm200fr20MonupRmonUnicastCounterClientInputErrorPortn_Type = EkiOnOff
_Pm200fr20MonupRmonUnicastCounterClientInputErrorPortn_Object = MibTableColumn
pm200fr20MonupRmonUnicastCounterClientInputErrorPortn = _Pm200fr20MonupRmonUnicastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 304, 1, 3),
    _Pm200fr20MonupRmonUnicastCounterClientInputErrorPortn_Type()
)
pm200fr20MonupRmonUnicastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MonupRmonUnicastCounterClientInputErrorPortn.setStatus("current")
_Pm200fr20MonupRmonUnicastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm200fr20MonupRmonUnicastCounterClientInputOverloadPortn_Object = MibTableColumn
pm200fr20MonupRmonUnicastCounterClientInputOverloadPortn = _Pm200fr20MonupRmonUnicastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 304, 1, 4),
    _Pm200fr20MonupRmonUnicastCounterClientInputOverloadPortn_Type()
)
pm200fr20MonupRmonUnicastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MonupRmonUnicastCounterClientInputOverloadPortn.setStatus("current")
_Pm200fr20MonupRmonNonunicastCounterClientInputTable_Object = MibTable
pm200fr20MonupRmonNonunicastCounterClientInputTable = _Pm200fr20MonupRmonNonunicastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 336)
)
if mibBuilder.loadTexts:
    pm200fr20MonupRmonNonunicastCounterClientInputTable.setStatus("current")
_Pm200fr20MonupRmonNonunicastCounterClientInputEntry_Object = MibTableRow
pm200fr20MonupRmonNonunicastCounterClientInputEntry = _Pm200fr20MonupRmonNonunicastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 336, 1)
)
pm200fr20MonupRmonNonunicastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20MonupRmonNonunicastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20MonupRmonNonunicastCounterClientInputEntry.setStatus("current")


class _Pm200fr20MonupRmonNonunicastCounterClientInputIndex_Type(Integer32):
    """Custom type pm200fr20MonupRmonNonunicastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20MonupRmonNonunicastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm200fr20MonupRmonNonunicastCounterClientInputIndex_Object = MibTableColumn
pm200fr20MonupRmonNonunicastCounterClientInputIndex = _Pm200fr20MonupRmonNonunicastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 336, 1, 1),
    _Pm200fr20MonupRmonNonunicastCounterClientInputIndex_Type()
)
pm200fr20MonupRmonNonunicastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MonupRmonNonunicastCounterClientInputIndex.setStatus("current")
_Pm200fr20MonupRmonNonunicastCounterClientInputValuePortn_Type = Counter64
_Pm200fr20MonupRmonNonunicastCounterClientInputValuePortn_Object = MibTableColumn
pm200fr20MonupRmonNonunicastCounterClientInputValuePortn = _Pm200fr20MonupRmonNonunicastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 336, 1, 2),
    _Pm200fr20MonupRmonNonunicastCounterClientInputValuePortn_Type()
)
pm200fr20MonupRmonNonunicastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MonupRmonNonunicastCounterClientInputValuePortn.setStatus("current")
_Pm200fr20MonupRmonNonunicastCounterClientInputErrorPortn_Type = EkiOnOff
_Pm200fr20MonupRmonNonunicastCounterClientInputErrorPortn_Object = MibTableColumn
pm200fr20MonupRmonNonunicastCounterClientInputErrorPortn = _Pm200fr20MonupRmonNonunicastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 336, 1, 3),
    _Pm200fr20MonupRmonNonunicastCounterClientInputErrorPortn_Type()
)
pm200fr20MonupRmonNonunicastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MonupRmonNonunicastCounterClientInputErrorPortn.setStatus("current")
_Pm200fr20MonupRmonNonunicastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm200fr20MonupRmonNonunicastCounterClientInputOverloadPortn_Object = MibTableColumn
pm200fr20MonupRmonNonunicastCounterClientInputOverloadPortn = _Pm200fr20MonupRmonNonunicastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 336, 1, 4),
    _Pm200fr20MonupRmonNonunicastCounterClientInputOverloadPortn_Type()
)
pm200fr20MonupRmonNonunicastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MonupRmonNonunicastCounterClientInputOverloadPortn.setStatus("current")
_Pm200fr20MondownRmonBytesCounterClientOutputTable_Object = MibTable
pm200fr20MondownRmonBytesCounterClientOutputTable = _Pm200fr20MondownRmonBytesCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 400)
)
if mibBuilder.loadTexts:
    pm200fr20MondownRmonBytesCounterClientOutputTable.setStatus("current")
_Pm200fr20MondownRmonBytesCounterClientOutputEntry_Object = MibTableRow
pm200fr20MondownRmonBytesCounterClientOutputEntry = _Pm200fr20MondownRmonBytesCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 400, 1)
)
pm200fr20MondownRmonBytesCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20MondownRmonBytesCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20MondownRmonBytesCounterClientOutputEntry.setStatus("current")


class _Pm200fr20MondownRmonBytesCounterClientOutputIndex_Type(Integer32):
    """Custom type pm200fr20MondownRmonBytesCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20MondownRmonBytesCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm200fr20MondownRmonBytesCounterClientOutputIndex_Object = MibTableColumn
pm200fr20MondownRmonBytesCounterClientOutputIndex = _Pm200fr20MondownRmonBytesCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 400, 1, 1),
    _Pm200fr20MondownRmonBytesCounterClientOutputIndex_Type()
)
pm200fr20MondownRmonBytesCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MondownRmonBytesCounterClientOutputIndex.setStatus("current")
_Pm200fr20MondownRmonBytesCounterClientOutputValuePortn_Type = Counter64
_Pm200fr20MondownRmonBytesCounterClientOutputValuePortn_Object = MibTableColumn
pm200fr20MondownRmonBytesCounterClientOutputValuePortn = _Pm200fr20MondownRmonBytesCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 400, 1, 2),
    _Pm200fr20MondownRmonBytesCounterClientOutputValuePortn_Type()
)
pm200fr20MondownRmonBytesCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MondownRmonBytesCounterClientOutputValuePortn.setStatus("current")
_Pm200fr20MondownRmonBytesCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm200fr20MondownRmonBytesCounterClientOutputErrorPortn_Object = MibTableColumn
pm200fr20MondownRmonBytesCounterClientOutputErrorPortn = _Pm200fr20MondownRmonBytesCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 400, 1, 3),
    _Pm200fr20MondownRmonBytesCounterClientOutputErrorPortn_Type()
)
pm200fr20MondownRmonBytesCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MondownRmonBytesCounterClientOutputErrorPortn.setStatus("current")
_Pm200fr20MondownRmonBytesCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm200fr20MondownRmonBytesCounterClientOutputOverloadPortn_Object = MibTableColumn
pm200fr20MondownRmonBytesCounterClientOutputOverloadPortn = _Pm200fr20MondownRmonBytesCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 400, 1, 4),
    _Pm200fr20MondownRmonBytesCounterClientOutputOverloadPortn_Type()
)
pm200fr20MondownRmonBytesCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MondownRmonBytesCounterClientOutputOverloadPortn.setStatus("current")
_Pm200fr20MondownRmonCrcErrorsCounterClientOutputTable_Object = MibTable
pm200fr20MondownRmonCrcErrorsCounterClientOutputTable = _Pm200fr20MondownRmonCrcErrorsCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 432)
)
if mibBuilder.loadTexts:
    pm200fr20MondownRmonCrcErrorsCounterClientOutputTable.setStatus("current")
_Pm200fr20MondownRmonCrcErrorsCounterClientOutputEntry_Object = MibTableRow
pm200fr20MondownRmonCrcErrorsCounterClientOutputEntry = _Pm200fr20MondownRmonCrcErrorsCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 432, 1)
)
pm200fr20MondownRmonCrcErrorsCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20MondownRmonCrcErrorsCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20MondownRmonCrcErrorsCounterClientOutputEntry.setStatus("current")


class _Pm200fr20MondownRmonCrcErrorsCounterClientOutputIndex_Type(Integer32):
    """Custom type pm200fr20MondownRmonCrcErrorsCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20MondownRmonCrcErrorsCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm200fr20MondownRmonCrcErrorsCounterClientOutputIndex_Object = MibTableColumn
pm200fr20MondownRmonCrcErrorsCounterClientOutputIndex = _Pm200fr20MondownRmonCrcErrorsCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 432, 1, 1),
    _Pm200fr20MondownRmonCrcErrorsCounterClientOutputIndex_Type()
)
pm200fr20MondownRmonCrcErrorsCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MondownRmonCrcErrorsCounterClientOutputIndex.setStatus("current")
_Pm200fr20MondownRmonCrcErrorsCounterClientOutputValuePortn_Type = Counter64
_Pm200fr20MondownRmonCrcErrorsCounterClientOutputValuePortn_Object = MibTableColumn
pm200fr20MondownRmonCrcErrorsCounterClientOutputValuePortn = _Pm200fr20MondownRmonCrcErrorsCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 432, 1, 2),
    _Pm200fr20MondownRmonCrcErrorsCounterClientOutputValuePortn_Type()
)
pm200fr20MondownRmonCrcErrorsCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MondownRmonCrcErrorsCounterClientOutputValuePortn.setStatus("current")
_Pm200fr20MondownRmonCrcErrorsCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm200fr20MondownRmonCrcErrorsCounterClientOutputErrorPortn_Object = MibTableColumn
pm200fr20MondownRmonCrcErrorsCounterClientOutputErrorPortn = _Pm200fr20MondownRmonCrcErrorsCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 432, 1, 3),
    _Pm200fr20MondownRmonCrcErrorsCounterClientOutputErrorPortn_Type()
)
pm200fr20MondownRmonCrcErrorsCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MondownRmonCrcErrorsCounterClientOutputErrorPortn.setStatus("current")
_Pm200fr20MondownRmonCrcErrorsCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm200fr20MondownRmonCrcErrorsCounterClientOutputOverloadPortn_Object = MibTableColumn
pm200fr20MondownRmonCrcErrorsCounterClientOutputOverloadPortn = _Pm200fr20MondownRmonCrcErrorsCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 432, 1, 4),
    _Pm200fr20MondownRmonCrcErrorsCounterClientOutputOverloadPortn_Type()
)
pm200fr20MondownRmonCrcErrorsCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MondownRmonCrcErrorsCounterClientOutputOverloadPortn.setStatus("current")
_Pm200fr20MondownRmonPacketsCounterClientOutputTable_Object = MibTable
pm200fr20MondownRmonPacketsCounterClientOutputTable = _Pm200fr20MondownRmonPacketsCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 464)
)
if mibBuilder.loadTexts:
    pm200fr20MondownRmonPacketsCounterClientOutputTable.setStatus("current")
_Pm200fr20MondownRmonPacketsCounterClientOutputEntry_Object = MibTableRow
pm200fr20MondownRmonPacketsCounterClientOutputEntry = _Pm200fr20MondownRmonPacketsCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 464, 1)
)
pm200fr20MondownRmonPacketsCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20MondownRmonPacketsCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20MondownRmonPacketsCounterClientOutputEntry.setStatus("current")


class _Pm200fr20MondownRmonPacketsCounterClientOutputIndex_Type(Integer32):
    """Custom type pm200fr20MondownRmonPacketsCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20MondownRmonPacketsCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm200fr20MondownRmonPacketsCounterClientOutputIndex_Object = MibTableColumn
pm200fr20MondownRmonPacketsCounterClientOutputIndex = _Pm200fr20MondownRmonPacketsCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 464, 1, 1),
    _Pm200fr20MondownRmonPacketsCounterClientOutputIndex_Type()
)
pm200fr20MondownRmonPacketsCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MondownRmonPacketsCounterClientOutputIndex.setStatus("current")
_Pm200fr20MondownRmonPacketsCounterClientOutputValuePortn_Type = Counter64
_Pm200fr20MondownRmonPacketsCounterClientOutputValuePortn_Object = MibTableColumn
pm200fr20MondownRmonPacketsCounterClientOutputValuePortn = _Pm200fr20MondownRmonPacketsCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 464, 1, 2),
    _Pm200fr20MondownRmonPacketsCounterClientOutputValuePortn_Type()
)
pm200fr20MondownRmonPacketsCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MondownRmonPacketsCounterClientOutputValuePortn.setStatus("current")
_Pm200fr20MondownRmonPacketsCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm200fr20MondownRmonPacketsCounterClientOutputErrorPortn_Object = MibTableColumn
pm200fr20MondownRmonPacketsCounterClientOutputErrorPortn = _Pm200fr20MondownRmonPacketsCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 464, 1, 3),
    _Pm200fr20MondownRmonPacketsCounterClientOutputErrorPortn_Type()
)
pm200fr20MondownRmonPacketsCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MondownRmonPacketsCounterClientOutputErrorPortn.setStatus("current")
_Pm200fr20MondownRmonPacketsCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm200fr20MondownRmonPacketsCounterClientOutputOverloadPortn_Object = MibTableColumn
pm200fr20MondownRmonPacketsCounterClientOutputOverloadPortn = _Pm200fr20MondownRmonPacketsCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 464, 1, 4),
    _Pm200fr20MondownRmonPacketsCounterClientOutputOverloadPortn_Type()
)
pm200fr20MondownRmonPacketsCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MondownRmonPacketsCounterClientOutputOverloadPortn.setStatus("current")
_Pm200fr20MondownRmonBroadcastCounterClientOutputTable_Object = MibTable
pm200fr20MondownRmonBroadcastCounterClientOutputTable = _Pm200fr20MondownRmonBroadcastCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 496)
)
if mibBuilder.loadTexts:
    pm200fr20MondownRmonBroadcastCounterClientOutputTable.setStatus("current")
_Pm200fr20MondownRmonBroadcastCounterClientOutputEntry_Object = MibTableRow
pm200fr20MondownRmonBroadcastCounterClientOutputEntry = _Pm200fr20MondownRmonBroadcastCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 496, 1)
)
pm200fr20MondownRmonBroadcastCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20MondownRmonBroadcastCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20MondownRmonBroadcastCounterClientOutputEntry.setStatus("current")


class _Pm200fr20MondownRmonBroadcastCounterClientOutputIndex_Type(Integer32):
    """Custom type pm200fr20MondownRmonBroadcastCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20MondownRmonBroadcastCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm200fr20MondownRmonBroadcastCounterClientOutputIndex_Object = MibTableColumn
pm200fr20MondownRmonBroadcastCounterClientOutputIndex = _Pm200fr20MondownRmonBroadcastCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 496, 1, 1),
    _Pm200fr20MondownRmonBroadcastCounterClientOutputIndex_Type()
)
pm200fr20MondownRmonBroadcastCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MondownRmonBroadcastCounterClientOutputIndex.setStatus("current")
_Pm200fr20MondownRmonBroadcastCounterClientOutputValuePortn_Type = Counter64
_Pm200fr20MondownRmonBroadcastCounterClientOutputValuePortn_Object = MibTableColumn
pm200fr20MondownRmonBroadcastCounterClientOutputValuePortn = _Pm200fr20MondownRmonBroadcastCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 496, 1, 2),
    _Pm200fr20MondownRmonBroadcastCounterClientOutputValuePortn_Type()
)
pm200fr20MondownRmonBroadcastCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MondownRmonBroadcastCounterClientOutputValuePortn.setStatus("current")
_Pm200fr20MondownRmonBroadcastCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm200fr20MondownRmonBroadcastCounterClientOutputErrorPortn_Object = MibTableColumn
pm200fr20MondownRmonBroadcastCounterClientOutputErrorPortn = _Pm200fr20MondownRmonBroadcastCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 496, 1, 3),
    _Pm200fr20MondownRmonBroadcastCounterClientOutputErrorPortn_Type()
)
pm200fr20MondownRmonBroadcastCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MondownRmonBroadcastCounterClientOutputErrorPortn.setStatus("current")
_Pm200fr20MondownRmonBroadcastCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm200fr20MondownRmonBroadcastCounterClientOutputOverloadPortn_Object = MibTableColumn
pm200fr20MondownRmonBroadcastCounterClientOutputOverloadPortn = _Pm200fr20MondownRmonBroadcastCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 496, 1, 4),
    _Pm200fr20MondownRmonBroadcastCounterClientOutputOverloadPortn_Type()
)
pm200fr20MondownRmonBroadcastCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MondownRmonBroadcastCounterClientOutputOverloadPortn.setStatus("current")
_Pm200fr20MondownRmonMulticastCounterClientOutputTable_Object = MibTable
pm200fr20MondownRmonMulticastCounterClientOutputTable = _Pm200fr20MondownRmonMulticastCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 528)
)
if mibBuilder.loadTexts:
    pm200fr20MondownRmonMulticastCounterClientOutputTable.setStatus("current")
_Pm200fr20MondownRmonMulticastCounterClientOutputEntry_Object = MibTableRow
pm200fr20MondownRmonMulticastCounterClientOutputEntry = _Pm200fr20MondownRmonMulticastCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 528, 1)
)
pm200fr20MondownRmonMulticastCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20MondownRmonMulticastCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20MondownRmonMulticastCounterClientOutputEntry.setStatus("current")


class _Pm200fr20MondownRmonMulticastCounterClientOutputIndex_Type(Integer32):
    """Custom type pm200fr20MondownRmonMulticastCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20MondownRmonMulticastCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm200fr20MondownRmonMulticastCounterClientOutputIndex_Object = MibTableColumn
pm200fr20MondownRmonMulticastCounterClientOutputIndex = _Pm200fr20MondownRmonMulticastCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 528, 1, 1),
    _Pm200fr20MondownRmonMulticastCounterClientOutputIndex_Type()
)
pm200fr20MondownRmonMulticastCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MondownRmonMulticastCounterClientOutputIndex.setStatus("current")
_Pm200fr20MondownRmonMulticastCounterClientOutputValuePortn_Type = Counter64
_Pm200fr20MondownRmonMulticastCounterClientOutputValuePortn_Object = MibTableColumn
pm200fr20MondownRmonMulticastCounterClientOutputValuePortn = _Pm200fr20MondownRmonMulticastCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 528, 1, 2),
    _Pm200fr20MondownRmonMulticastCounterClientOutputValuePortn_Type()
)
pm200fr20MondownRmonMulticastCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MondownRmonMulticastCounterClientOutputValuePortn.setStatus("current")
_Pm200fr20MondownRmonMulticastCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm200fr20MondownRmonMulticastCounterClientOutputErrorPortn_Object = MibTableColumn
pm200fr20MondownRmonMulticastCounterClientOutputErrorPortn = _Pm200fr20MondownRmonMulticastCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 528, 1, 3),
    _Pm200fr20MondownRmonMulticastCounterClientOutputErrorPortn_Type()
)
pm200fr20MondownRmonMulticastCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MondownRmonMulticastCounterClientOutputErrorPortn.setStatus("current")
_Pm200fr20MondownRmonMulticastCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm200fr20MondownRmonMulticastCounterClientOutputOverloadPortn_Object = MibTableColumn
pm200fr20MondownRmonMulticastCounterClientOutputOverloadPortn = _Pm200fr20MondownRmonMulticastCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 528, 1, 4),
    _Pm200fr20MondownRmonMulticastCounterClientOutputOverloadPortn_Type()
)
pm200fr20MondownRmonMulticastCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MondownRmonMulticastCounterClientOutputOverloadPortn.setStatus("current")
_Pm200fr20MondownRmonPauseFrameCounterClientOutputTable_Object = MibTable
pm200fr20MondownRmonPauseFrameCounterClientOutputTable = _Pm200fr20MondownRmonPauseFrameCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 560)
)
if mibBuilder.loadTexts:
    pm200fr20MondownRmonPauseFrameCounterClientOutputTable.setStatus("current")
_Pm200fr20MondownRmonPauseFrameCounterClientOutputEntry_Object = MibTableRow
pm200fr20MondownRmonPauseFrameCounterClientOutputEntry = _Pm200fr20MondownRmonPauseFrameCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 560, 1)
)
pm200fr20MondownRmonPauseFrameCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20MondownRmonPauseFrameCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20MondownRmonPauseFrameCounterClientOutputEntry.setStatus("current")


class _Pm200fr20MondownRmonPauseFrameCounterClientOutputIndex_Type(Integer32):
    """Custom type pm200fr20MondownRmonPauseFrameCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20MondownRmonPauseFrameCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm200fr20MondownRmonPauseFrameCounterClientOutputIndex_Object = MibTableColumn
pm200fr20MondownRmonPauseFrameCounterClientOutputIndex = _Pm200fr20MondownRmonPauseFrameCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 560, 1, 1),
    _Pm200fr20MondownRmonPauseFrameCounterClientOutputIndex_Type()
)
pm200fr20MondownRmonPauseFrameCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MondownRmonPauseFrameCounterClientOutputIndex.setStatus("current")
_Pm200fr20MondownRmonPauseFrameCounterClientOutputValuePortn_Type = Counter64
_Pm200fr20MondownRmonPauseFrameCounterClientOutputValuePortn_Object = MibTableColumn
pm200fr20MondownRmonPauseFrameCounterClientOutputValuePortn = _Pm200fr20MondownRmonPauseFrameCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 560, 1, 2),
    _Pm200fr20MondownRmonPauseFrameCounterClientOutputValuePortn_Type()
)
pm200fr20MondownRmonPauseFrameCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MondownRmonPauseFrameCounterClientOutputValuePortn.setStatus("current")
_Pm200fr20MondownRmonPauseFrameCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm200fr20MondownRmonPauseFrameCounterClientOutputErrorPortn_Object = MibTableColumn
pm200fr20MondownRmonPauseFrameCounterClientOutputErrorPortn = _Pm200fr20MondownRmonPauseFrameCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 560, 1, 3),
    _Pm200fr20MondownRmonPauseFrameCounterClientOutputErrorPortn_Type()
)
pm200fr20MondownRmonPauseFrameCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MondownRmonPauseFrameCounterClientOutputErrorPortn.setStatus("current")
_Pm200fr20MondownRmonPauseFrameCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm200fr20MondownRmonPauseFrameCounterClientOutputOverloadPortn_Object = MibTableColumn
pm200fr20MondownRmonPauseFrameCounterClientOutputOverloadPortn = _Pm200fr20MondownRmonPauseFrameCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 560, 1, 4),
    _Pm200fr20MondownRmonPauseFrameCounterClientOutputOverloadPortn_Type()
)
pm200fr20MondownRmonPauseFrameCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MondownRmonPauseFrameCounterClientOutputOverloadPortn.setStatus("current")
_Pm200fr20MondownRmonUnicastCounterClientOutputTable_Object = MibTable
pm200fr20MondownRmonUnicastCounterClientOutputTable = _Pm200fr20MondownRmonUnicastCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 688)
)
if mibBuilder.loadTexts:
    pm200fr20MondownRmonUnicastCounterClientOutputTable.setStatus("current")
_Pm200fr20MondownRmonUnicastCounterClientOutputEntry_Object = MibTableRow
pm200fr20MondownRmonUnicastCounterClientOutputEntry = _Pm200fr20MondownRmonUnicastCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 688, 1)
)
pm200fr20MondownRmonUnicastCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20MondownRmonUnicastCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20MondownRmonUnicastCounterClientOutputEntry.setStatus("current")


class _Pm200fr20MondownRmonUnicastCounterClientOutputIndex_Type(Integer32):
    """Custom type pm200fr20MondownRmonUnicastCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20MondownRmonUnicastCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm200fr20MondownRmonUnicastCounterClientOutputIndex_Object = MibTableColumn
pm200fr20MondownRmonUnicastCounterClientOutputIndex = _Pm200fr20MondownRmonUnicastCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 688, 1, 1),
    _Pm200fr20MondownRmonUnicastCounterClientOutputIndex_Type()
)
pm200fr20MondownRmonUnicastCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MondownRmonUnicastCounterClientOutputIndex.setStatus("current")
_Pm200fr20MondownRmonUnicastCounterClientOutputValuePortn_Type = Counter64
_Pm200fr20MondownRmonUnicastCounterClientOutputValuePortn_Object = MibTableColumn
pm200fr20MondownRmonUnicastCounterClientOutputValuePortn = _Pm200fr20MondownRmonUnicastCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 688, 1, 2),
    _Pm200fr20MondownRmonUnicastCounterClientOutputValuePortn_Type()
)
pm200fr20MondownRmonUnicastCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MondownRmonUnicastCounterClientOutputValuePortn.setStatus("current")
_Pm200fr20MondownRmonUnicastCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm200fr20MondownRmonUnicastCounterClientOutputErrorPortn_Object = MibTableColumn
pm200fr20MondownRmonUnicastCounterClientOutputErrorPortn = _Pm200fr20MondownRmonUnicastCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 688, 1, 3),
    _Pm200fr20MondownRmonUnicastCounterClientOutputErrorPortn_Type()
)
pm200fr20MondownRmonUnicastCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MondownRmonUnicastCounterClientOutputErrorPortn.setStatus("current")
_Pm200fr20MondownRmonUnicastCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm200fr20MondownRmonUnicastCounterClientOutputOverloadPortn_Object = MibTableColumn
pm200fr20MondownRmonUnicastCounterClientOutputOverloadPortn = _Pm200fr20MondownRmonUnicastCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 688, 1, 4),
    _Pm200fr20MondownRmonUnicastCounterClientOutputOverloadPortn_Type()
)
pm200fr20MondownRmonUnicastCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MondownRmonUnicastCounterClientOutputOverloadPortn.setStatus("current")
_Pm200fr20MondownRmonNonunicastCounterClientOutputTable_Object = MibTable
pm200fr20MondownRmonNonunicastCounterClientOutputTable = _Pm200fr20MondownRmonNonunicastCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 720)
)
if mibBuilder.loadTexts:
    pm200fr20MondownRmonNonunicastCounterClientOutputTable.setStatus("current")
_Pm200fr20MondownRmonNonunicastCounterClientOutputEntry_Object = MibTableRow
pm200fr20MondownRmonNonunicastCounterClientOutputEntry = _Pm200fr20MondownRmonNonunicastCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 720, 1)
)
pm200fr20MondownRmonNonunicastCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20MondownRmonNonunicastCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20MondownRmonNonunicastCounterClientOutputEntry.setStatus("current")


class _Pm200fr20MondownRmonNonunicastCounterClientOutputIndex_Type(Integer32):
    """Custom type pm200fr20MondownRmonNonunicastCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20MondownRmonNonunicastCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm200fr20MondownRmonNonunicastCounterClientOutputIndex_Object = MibTableColumn
pm200fr20MondownRmonNonunicastCounterClientOutputIndex = _Pm200fr20MondownRmonNonunicastCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 720, 1, 1),
    _Pm200fr20MondownRmonNonunicastCounterClientOutputIndex_Type()
)
pm200fr20MondownRmonNonunicastCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MondownRmonNonunicastCounterClientOutputIndex.setStatus("current")
_Pm200fr20MondownRmonNonunicastCounterClientOutputValuePortn_Type = Counter64
_Pm200fr20MondownRmonNonunicastCounterClientOutputValuePortn_Object = MibTableColumn
pm200fr20MondownRmonNonunicastCounterClientOutputValuePortn = _Pm200fr20MondownRmonNonunicastCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 720, 1, 2),
    _Pm200fr20MondownRmonNonunicastCounterClientOutputValuePortn_Type()
)
pm200fr20MondownRmonNonunicastCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MondownRmonNonunicastCounterClientOutputValuePortn.setStatus("current")
_Pm200fr20MondownRmonNonunicastCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm200fr20MondownRmonNonunicastCounterClientOutputErrorPortn_Object = MibTableColumn
pm200fr20MondownRmonNonunicastCounterClientOutputErrorPortn = _Pm200fr20MondownRmonNonunicastCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 720, 1, 3),
    _Pm200fr20MondownRmonNonunicastCounterClientOutputErrorPortn_Type()
)
pm200fr20MondownRmonNonunicastCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MondownRmonNonunicastCounterClientOutputErrorPortn.setStatus("current")
_Pm200fr20MondownRmonNonunicastCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm200fr20MondownRmonNonunicastCounterClientOutputOverloadPortn_Object = MibTableColumn
pm200fr20MondownRmonNonunicastCounterClientOutputOverloadPortn = _Pm200fr20MondownRmonNonunicastCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 2, 4, 720, 1, 4),
    _Pm200fr20MondownRmonNonunicastCounterClientOutputOverloadPortn_Type()
)
pm200fr20MondownRmonNonunicastCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20MondownRmonNonunicastCounterClientOutputOverloadPortn.setStatus("current")
_Pm200fr20MonPerfOther_ObjectIdentity = ObjectIdentity
pm200fr20MonPerfOther = _Pm200fr20MonPerfOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 5)
)
_Pm200fr20MonPerfSync_ObjectIdentity = ObjectIdentity
pm200fr20MonPerfSync = _Pm200fr20MonPerfSync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 5, 1)
)
_Pm200fr20PerfEnable_Type = EkiOnOff
_Pm200fr20PerfEnable_Object = MibScalar
pm200fr20PerfEnable = _Pm200fr20PerfEnable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 5, 1, 257),
    _Pm200fr20PerfEnable_Type()
)
pm200fr20PerfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20PerfEnable.setStatus("current")
_Pm200fr20Perf15minSync_Type = EkiOnOff
_Pm200fr20Perf15minSync_Object = MibScalar
pm200fr20Perf15minSync = _Pm200fr20Perf15minSync_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 5, 1, 259),
    _Pm200fr20Perf15minSync_Type()
)
pm200fr20Perf15minSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20Perf15minSync.setStatus("current")
_Pm200fr20Perf24hSync_Type = EkiOnOff
_Pm200fr20Perf24hSync_Object = MibScalar
pm200fr20Perf24hSync = _Pm200fr20Perf24hSync_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 5, 1, 260),
    _Pm200fr20Perf24hSync_Type()
)
pm200fr20Perf24hSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20Perf24hSync.setStatus("current")
_Pm200fr20MonPerfTimeStamp_ObjectIdentity = ObjectIdentity
pm200fr20MonPerfTimeStamp = _Pm200fr20MonPerfTimeStamp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 5, 2)
)
_Pm200fr20Perf15MinShort_Type = EkiOnOff
_Pm200fr20Perf15MinShort_Object = MibScalar
pm200fr20Perf15MinShort = _Pm200fr20Perf15MinShort_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 5, 2, 1),
    _Pm200fr20Perf15MinShort_Type()
)
pm200fr20Perf15MinShort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20Perf15MinShort.setStatus("current")
_Pm200fr20Perf15MinLong_Type = EkiOnOff
_Pm200fr20Perf15MinLong_Object = MibScalar
pm200fr20Perf15MinLong = _Pm200fr20Perf15MinLong_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 5, 2, 2),
    _Pm200fr20Perf15MinLong_Type()
)
pm200fr20Perf15MinLong.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20Perf15MinLong.setStatus("current")
_Pm200fr20Perf24HoursShort_Type = Counter32
_Pm200fr20Perf24HoursShort_Object = MibScalar
pm200fr20Perf24HoursShort = _Pm200fr20Perf24HoursShort_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 5, 2, 5),
    _Pm200fr20Perf24HoursShort_Type()
)
pm200fr20Perf24HoursShort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20Perf24HoursShort.setStatus("current")
_Pm200fr20Perf24HoursLong_Type = Counter32
_Pm200fr20Perf24HoursLong_Object = MibScalar
pm200fr20Perf24HoursLong = _Pm200fr20Perf24HoursLong_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 5, 2, 6),
    _Pm200fr20Perf24HoursLong_Type()
)
pm200fr20Perf24HoursLong.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20Perf24HoursLong.setStatus("current")
_Pm200fr20PerfCurrent15MinElapsedTime_Type = Counter32
_Pm200fr20PerfCurrent15MinElapsedTime_Object = MibScalar
pm200fr20PerfCurrent15MinElapsedTime = _Pm200fr20PerfCurrent15MinElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 5, 2, 7),
    _Pm200fr20PerfCurrent15MinElapsedTime_Type()
)
pm200fr20PerfCurrent15MinElapsedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20PerfCurrent15MinElapsedTime.setStatus("current")
_Pm200fr20PerfCurrent24HoursElapsedTime_Type = Counter32
_Pm200fr20PerfCurrent24HoursElapsedTime_Object = MibScalar
pm200fr20PerfCurrent24HoursElapsedTime = _Pm200fr20PerfCurrent24HoursElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 5, 2, 8),
    _Pm200fr20PerfCurrent24HoursElapsedTime_Type()
)
pm200fr20PerfCurrent24HoursElapsedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200fr20PerfCurrent24HoursElapsedTime.setStatus("current")
_Pm200fr20MonPerfClient_ObjectIdentity = ObjectIdentity
pm200fr20MonPerfClient = _Pm200fr20MonPerfClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6)
)
_Pm200fr20PerfTelecomInputClientCurrent15StatTable_Object = MibTable
pm200fr20PerfTelecomInputClientCurrent15StatTable = _Pm200fr20PerfTelecomInputClientCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 16)
)
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientCurrent15StatTable.setStatus("current")
_Pm200fr20PerfTelecomInputClientCurrent15StatEntry_Object = MibTableRow
pm200fr20PerfTelecomInputClientCurrent15StatEntry = _Pm200fr20PerfTelecomInputClientCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 16, 1)
)
pm200fr20PerfTelecomInputClientCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20PerfTelecomInputClientCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientCurrent15StatEntry.setStatus("current")


class _Pm200fr20PerfTelecomInputClientCurrent15StatIndex_Type(Integer32):
    """Custom type pm200fr20PerfTelecomInputClientCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20PerfTelecomInputClientCurrent15StatIndex_Type.__name__ = "Integer32"
_Pm200fr20PerfTelecomInputClientCurrent15StatIndex_Object = MibTableColumn
pm200fr20PerfTelecomInputClientCurrent15StatIndex = _Pm200fr20PerfTelecomInputClientCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 16, 1, 1),
    _Pm200fr20PerfTelecomInputClientCurrent15StatIndex_Type()
)
pm200fr20PerfTelecomInputClientCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientCurrent15StatIndex.setStatus("current")
_Pm200fr20PerfTelecomInputClientCurrent15StatInvCvPortn_Type = EkiOnOff
_Pm200fr20PerfTelecomInputClientCurrent15StatInvCvPortn_Object = MibTableColumn
pm200fr20PerfTelecomInputClientCurrent15StatInvCvPortn = _Pm200fr20PerfTelecomInputClientCurrent15StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 16, 1, 2),
    _Pm200fr20PerfTelecomInputClientCurrent15StatInvCvPortn_Type()
)
pm200fr20PerfTelecomInputClientCurrent15StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientCurrent15StatInvCvPortn.setStatus("current")
_Pm200fr20PerfTelecomInputClientCurrent15StatCvValuePortn_Type = Unsigned32
_Pm200fr20PerfTelecomInputClientCurrent15StatCvValuePortn_Object = MibTableColumn
pm200fr20PerfTelecomInputClientCurrent15StatCvValuePortn = _Pm200fr20PerfTelecomInputClientCurrent15StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 16, 1, 3),
    _Pm200fr20PerfTelecomInputClientCurrent15StatCvValuePortn_Type()
)
pm200fr20PerfTelecomInputClientCurrent15StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientCurrent15StatCvValuePortn.setStatus("current")
_Pm200fr20PerfTelecomInputClientCurrent15StatInvEsPortn_Type = EkiOnOff
_Pm200fr20PerfTelecomInputClientCurrent15StatInvEsPortn_Object = MibTableColumn
pm200fr20PerfTelecomInputClientCurrent15StatInvEsPortn = _Pm200fr20PerfTelecomInputClientCurrent15StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 16, 1, 4),
    _Pm200fr20PerfTelecomInputClientCurrent15StatInvEsPortn_Type()
)
pm200fr20PerfTelecomInputClientCurrent15StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientCurrent15StatInvEsPortn.setStatus("current")
_Pm200fr20PerfTelecomInputClientCurrent15StatEsValuePortn_Type = Unsigned32
_Pm200fr20PerfTelecomInputClientCurrent15StatEsValuePortn_Object = MibTableColumn
pm200fr20PerfTelecomInputClientCurrent15StatEsValuePortn = _Pm200fr20PerfTelecomInputClientCurrent15StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 16, 1, 5),
    _Pm200fr20PerfTelecomInputClientCurrent15StatEsValuePortn_Type()
)
pm200fr20PerfTelecomInputClientCurrent15StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientCurrent15StatEsValuePortn.setStatus("current")
_Pm200fr20PerfTelecomInputClientCurrent15StatInvSesPortn_Type = EkiOnOff
_Pm200fr20PerfTelecomInputClientCurrent15StatInvSesPortn_Object = MibTableColumn
pm200fr20PerfTelecomInputClientCurrent15StatInvSesPortn = _Pm200fr20PerfTelecomInputClientCurrent15StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 16, 1, 6),
    _Pm200fr20PerfTelecomInputClientCurrent15StatInvSesPortn_Type()
)
pm200fr20PerfTelecomInputClientCurrent15StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientCurrent15StatInvSesPortn.setStatus("current")
_Pm200fr20PerfTelecomInputClientCurrent15StatSesValuePortn_Type = Unsigned32
_Pm200fr20PerfTelecomInputClientCurrent15StatSesValuePortn_Object = MibTableColumn
pm200fr20PerfTelecomInputClientCurrent15StatSesValuePortn = _Pm200fr20PerfTelecomInputClientCurrent15StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 16, 1, 7),
    _Pm200fr20PerfTelecomInputClientCurrent15StatSesValuePortn_Type()
)
pm200fr20PerfTelecomInputClientCurrent15StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientCurrent15StatSesValuePortn.setStatus("current")
_Pm200fr20PerfTelecomInputClientCurrent15StatInvSefsPortn_Type = EkiOnOff
_Pm200fr20PerfTelecomInputClientCurrent15StatInvSefsPortn_Object = MibTableColumn
pm200fr20PerfTelecomInputClientCurrent15StatInvSefsPortn = _Pm200fr20PerfTelecomInputClientCurrent15StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 16, 1, 8),
    _Pm200fr20PerfTelecomInputClientCurrent15StatInvSefsPortn_Type()
)
pm200fr20PerfTelecomInputClientCurrent15StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientCurrent15StatInvSefsPortn.setStatus("current")
_Pm200fr20PerfTelecomInputClientCurrent15StatSefsValuePortn_Type = Unsigned32
_Pm200fr20PerfTelecomInputClientCurrent15StatSefsValuePortn_Object = MibTableColumn
pm200fr20PerfTelecomInputClientCurrent15StatSefsValuePortn = _Pm200fr20PerfTelecomInputClientCurrent15StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 16, 1, 9),
    _Pm200fr20PerfTelecomInputClientCurrent15StatSefsValuePortn_Type()
)
pm200fr20PerfTelecomInputClientCurrent15StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientCurrent15StatSefsValuePortn.setStatus("current")
_Pm200fr20PerfTelecomInputClientCurrent15StatInvUasPortn_Type = EkiOnOff
_Pm200fr20PerfTelecomInputClientCurrent15StatInvUasPortn_Object = MibTableColumn
pm200fr20PerfTelecomInputClientCurrent15StatInvUasPortn = _Pm200fr20PerfTelecomInputClientCurrent15StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 16, 1, 10),
    _Pm200fr20PerfTelecomInputClientCurrent15StatInvUasPortn_Type()
)
pm200fr20PerfTelecomInputClientCurrent15StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientCurrent15StatInvUasPortn.setStatus("current")
_Pm200fr20PerfTelecomInputClientCurrent15StatUasValuePortn_Type = Unsigned32
_Pm200fr20PerfTelecomInputClientCurrent15StatUasValuePortn_Object = MibTableColumn
pm200fr20PerfTelecomInputClientCurrent15StatUasValuePortn = _Pm200fr20PerfTelecomInputClientCurrent15StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 16, 1, 11),
    _Pm200fr20PerfTelecomInputClientCurrent15StatUasValuePortn_Type()
)
pm200fr20PerfTelecomInputClientCurrent15StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientCurrent15StatUasValuePortn.setStatus("current")
_Pm200fr20PerfTelecomInputClientPast15StatHistoryPort1Table_Object = MibTable
pm200fr20PerfTelecomInputClientPast15StatHistoryPort1Table = _Pm200fr20PerfTelecomInputClientPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 48)
)
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientPast15StatHistoryPort1Table.setStatus("current")
_Pm200fr20PerfTelecomInputClientPast15StatHistoryPort1Entry_Object = MibTableRow
pm200fr20PerfTelecomInputClientPast15StatHistoryPort1Entry = _Pm200fr20PerfTelecomInputClientPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 48, 1)
)
pm200fr20PerfTelecomInputClientPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20PerfTelecomInputClientPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientPast15StatHistoryPort1Entry.setStatus("current")


class _Pm200fr20PerfTelecomInputClientPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pm200fr20PerfTelecomInputClientPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20PerfTelecomInputClientPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm200fr20PerfTelecomInputClientPast15StatHistoryPort1Index_Object = MibTableColumn
pm200fr20PerfTelecomInputClientPast15StatHistoryPort1Index = _Pm200fr20PerfTelecomInputClientPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 48, 1, 1),
    _Pm200fr20PerfTelecomInputClientPast15StatHistoryPort1Index_Type()
)
pm200fr20PerfTelecomInputClientPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientPast15StatHistoryPort1Index.setStatus("current")
_Pm200fr20PerfTelecomInputClientPast15StatHistoryInvCvPort1_Type = EkiOnOff
_Pm200fr20PerfTelecomInputClientPast15StatHistoryInvCvPort1_Object = MibTableColumn
pm200fr20PerfTelecomInputClientPast15StatHistoryInvCvPort1 = _Pm200fr20PerfTelecomInputClientPast15StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 48, 1, 2),
    _Pm200fr20PerfTelecomInputClientPast15StatHistoryInvCvPort1_Type()
)
pm200fr20PerfTelecomInputClientPast15StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientPast15StatHistoryInvCvPort1.setStatus("current")
_Pm200fr20PerfTelecomInputClientPast15StatHistoryCvValuePort1_Type = Unsigned32
_Pm200fr20PerfTelecomInputClientPast15StatHistoryCvValuePort1_Object = MibTableColumn
pm200fr20PerfTelecomInputClientPast15StatHistoryCvValuePort1 = _Pm200fr20PerfTelecomInputClientPast15StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 48, 1, 3),
    _Pm200fr20PerfTelecomInputClientPast15StatHistoryCvValuePort1_Type()
)
pm200fr20PerfTelecomInputClientPast15StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientPast15StatHistoryCvValuePort1.setStatus("current")
_Pm200fr20PerfTelecomInputClientPast15StatHistoryInvEsPort1_Type = EkiOnOff
_Pm200fr20PerfTelecomInputClientPast15StatHistoryInvEsPort1_Object = MibTableColumn
pm200fr20PerfTelecomInputClientPast15StatHistoryInvEsPort1 = _Pm200fr20PerfTelecomInputClientPast15StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 48, 1, 4),
    _Pm200fr20PerfTelecomInputClientPast15StatHistoryInvEsPort1_Type()
)
pm200fr20PerfTelecomInputClientPast15StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientPast15StatHistoryInvEsPort1.setStatus("current")
_Pm200fr20PerfTelecomInputClientPast15StatHistoryEsValuePort1_Type = Unsigned32
_Pm200fr20PerfTelecomInputClientPast15StatHistoryEsValuePort1_Object = MibTableColumn
pm200fr20PerfTelecomInputClientPast15StatHistoryEsValuePort1 = _Pm200fr20PerfTelecomInputClientPast15StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 48, 1, 5),
    _Pm200fr20PerfTelecomInputClientPast15StatHistoryEsValuePort1_Type()
)
pm200fr20PerfTelecomInputClientPast15StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientPast15StatHistoryEsValuePort1.setStatus("current")
_Pm200fr20PerfTelecomInputClientPast15StatHistoryInvSesPort1_Type = EkiOnOff
_Pm200fr20PerfTelecomInputClientPast15StatHistoryInvSesPort1_Object = MibTableColumn
pm200fr20PerfTelecomInputClientPast15StatHistoryInvSesPort1 = _Pm200fr20PerfTelecomInputClientPast15StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 48, 1, 6),
    _Pm200fr20PerfTelecomInputClientPast15StatHistoryInvSesPort1_Type()
)
pm200fr20PerfTelecomInputClientPast15StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientPast15StatHistoryInvSesPort1.setStatus("current")
_Pm200fr20PerfTelecomInputClientPast15StatHistorySesValuePort1_Type = Unsigned32
_Pm200fr20PerfTelecomInputClientPast15StatHistorySesValuePort1_Object = MibTableColumn
pm200fr20PerfTelecomInputClientPast15StatHistorySesValuePort1 = _Pm200fr20PerfTelecomInputClientPast15StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 48, 1, 7),
    _Pm200fr20PerfTelecomInputClientPast15StatHistorySesValuePort1_Type()
)
pm200fr20PerfTelecomInputClientPast15StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientPast15StatHistorySesValuePort1.setStatus("current")
_Pm200fr20PerfTelecomInputClientPast15StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm200fr20PerfTelecomInputClientPast15StatHistoryInvSefsPort1_Object = MibTableColumn
pm200fr20PerfTelecomInputClientPast15StatHistoryInvSefsPort1 = _Pm200fr20PerfTelecomInputClientPast15StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 48, 1, 8),
    _Pm200fr20PerfTelecomInputClientPast15StatHistoryInvSefsPort1_Type()
)
pm200fr20PerfTelecomInputClientPast15StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientPast15StatHistoryInvSefsPort1.setStatus("current")
_Pm200fr20PerfTelecomInputClientPast15StatHistorySefsValuePort1_Type = Unsigned32
_Pm200fr20PerfTelecomInputClientPast15StatHistorySefsValuePort1_Object = MibTableColumn
pm200fr20PerfTelecomInputClientPast15StatHistorySefsValuePort1 = _Pm200fr20PerfTelecomInputClientPast15StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 48, 1, 9),
    _Pm200fr20PerfTelecomInputClientPast15StatHistorySefsValuePort1_Type()
)
pm200fr20PerfTelecomInputClientPast15StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientPast15StatHistorySefsValuePort1.setStatus("current")
_Pm200fr20PerfTelecomInputClientPast15StatHistoryInvUasPort1_Type = EkiOnOff
_Pm200fr20PerfTelecomInputClientPast15StatHistoryInvUasPort1_Object = MibTableColumn
pm200fr20PerfTelecomInputClientPast15StatHistoryInvUasPort1 = _Pm200fr20PerfTelecomInputClientPast15StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 48, 1, 10),
    _Pm200fr20PerfTelecomInputClientPast15StatHistoryInvUasPort1_Type()
)
pm200fr20PerfTelecomInputClientPast15StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientPast15StatHistoryInvUasPort1.setStatus("current")
_Pm200fr20PerfTelecomInputClientPast15StatHistoryUasValuePort1_Type = Unsigned32
_Pm200fr20PerfTelecomInputClientPast15StatHistoryUasValuePort1_Object = MibTableColumn
pm200fr20PerfTelecomInputClientPast15StatHistoryUasValuePort1 = _Pm200fr20PerfTelecomInputClientPast15StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 48, 1, 11),
    _Pm200fr20PerfTelecomInputClientPast15StatHistoryUasValuePort1_Type()
)
pm200fr20PerfTelecomInputClientPast15StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientPast15StatHistoryUasValuePort1.setStatus("current")
_Pm200fr20PerfTelecomInputClientCurrent24StatTable_Object = MibTable
pm200fr20PerfTelecomInputClientCurrent24StatTable = _Pm200fr20PerfTelecomInputClientCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 80)
)
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientCurrent24StatTable.setStatus("current")
_Pm200fr20PerfTelecomInputClientCurrent24StatEntry_Object = MibTableRow
pm200fr20PerfTelecomInputClientCurrent24StatEntry = _Pm200fr20PerfTelecomInputClientCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 80, 1)
)
pm200fr20PerfTelecomInputClientCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20PerfTelecomInputClientCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientCurrent24StatEntry.setStatus("current")


class _Pm200fr20PerfTelecomInputClientCurrent24StatIndex_Type(Integer32):
    """Custom type pm200fr20PerfTelecomInputClientCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20PerfTelecomInputClientCurrent24StatIndex_Type.__name__ = "Integer32"
_Pm200fr20PerfTelecomInputClientCurrent24StatIndex_Object = MibTableColumn
pm200fr20PerfTelecomInputClientCurrent24StatIndex = _Pm200fr20PerfTelecomInputClientCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 80, 1, 1),
    _Pm200fr20PerfTelecomInputClientCurrent24StatIndex_Type()
)
pm200fr20PerfTelecomInputClientCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientCurrent24StatIndex.setStatus("current")
_Pm200fr20PerfTelecomInputClientCurrent24StatInvCvPortn_Type = EkiOnOff
_Pm200fr20PerfTelecomInputClientCurrent24StatInvCvPortn_Object = MibTableColumn
pm200fr20PerfTelecomInputClientCurrent24StatInvCvPortn = _Pm200fr20PerfTelecomInputClientCurrent24StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 80, 1, 2),
    _Pm200fr20PerfTelecomInputClientCurrent24StatInvCvPortn_Type()
)
pm200fr20PerfTelecomInputClientCurrent24StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientCurrent24StatInvCvPortn.setStatus("current")
_Pm200fr20PerfTelecomInputClientCurrent24StatCvValuePortn_Type = Unsigned32
_Pm200fr20PerfTelecomInputClientCurrent24StatCvValuePortn_Object = MibTableColumn
pm200fr20PerfTelecomInputClientCurrent24StatCvValuePortn = _Pm200fr20PerfTelecomInputClientCurrent24StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 80, 1, 3),
    _Pm200fr20PerfTelecomInputClientCurrent24StatCvValuePortn_Type()
)
pm200fr20PerfTelecomInputClientCurrent24StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientCurrent24StatCvValuePortn.setStatus("current")
_Pm200fr20PerfTelecomInputClientCurrent24StatInvEsPortn_Type = EkiOnOff
_Pm200fr20PerfTelecomInputClientCurrent24StatInvEsPortn_Object = MibTableColumn
pm200fr20PerfTelecomInputClientCurrent24StatInvEsPortn = _Pm200fr20PerfTelecomInputClientCurrent24StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 80, 1, 4),
    _Pm200fr20PerfTelecomInputClientCurrent24StatInvEsPortn_Type()
)
pm200fr20PerfTelecomInputClientCurrent24StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientCurrent24StatInvEsPortn.setStatus("current")
_Pm200fr20PerfTelecomInputClientCurrent24StatEsValuePortn_Type = Unsigned32
_Pm200fr20PerfTelecomInputClientCurrent24StatEsValuePortn_Object = MibTableColumn
pm200fr20PerfTelecomInputClientCurrent24StatEsValuePortn = _Pm200fr20PerfTelecomInputClientCurrent24StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 80, 1, 5),
    _Pm200fr20PerfTelecomInputClientCurrent24StatEsValuePortn_Type()
)
pm200fr20PerfTelecomInputClientCurrent24StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientCurrent24StatEsValuePortn.setStatus("current")
_Pm200fr20PerfTelecomInputClientCurrent24StatInvSesPortn_Type = EkiOnOff
_Pm200fr20PerfTelecomInputClientCurrent24StatInvSesPortn_Object = MibTableColumn
pm200fr20PerfTelecomInputClientCurrent24StatInvSesPortn = _Pm200fr20PerfTelecomInputClientCurrent24StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 80, 1, 6),
    _Pm200fr20PerfTelecomInputClientCurrent24StatInvSesPortn_Type()
)
pm200fr20PerfTelecomInputClientCurrent24StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientCurrent24StatInvSesPortn.setStatus("current")
_Pm200fr20PerfTelecomInputClientCurrent24StatSesValuePortn_Type = Unsigned32
_Pm200fr20PerfTelecomInputClientCurrent24StatSesValuePortn_Object = MibTableColumn
pm200fr20PerfTelecomInputClientCurrent24StatSesValuePortn = _Pm200fr20PerfTelecomInputClientCurrent24StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 80, 1, 7),
    _Pm200fr20PerfTelecomInputClientCurrent24StatSesValuePortn_Type()
)
pm200fr20PerfTelecomInputClientCurrent24StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientCurrent24StatSesValuePortn.setStatus("current")
_Pm200fr20PerfTelecomInputClientCurrent24StatInvSefsPortn_Type = EkiOnOff
_Pm200fr20PerfTelecomInputClientCurrent24StatInvSefsPortn_Object = MibTableColumn
pm200fr20PerfTelecomInputClientCurrent24StatInvSefsPortn = _Pm200fr20PerfTelecomInputClientCurrent24StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 80, 1, 8),
    _Pm200fr20PerfTelecomInputClientCurrent24StatInvSefsPortn_Type()
)
pm200fr20PerfTelecomInputClientCurrent24StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientCurrent24StatInvSefsPortn.setStatus("current")
_Pm200fr20PerfTelecomInputClientCurrent24StatSefsValuePortn_Type = Unsigned32
_Pm200fr20PerfTelecomInputClientCurrent24StatSefsValuePortn_Object = MibTableColumn
pm200fr20PerfTelecomInputClientCurrent24StatSefsValuePortn = _Pm200fr20PerfTelecomInputClientCurrent24StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 80, 1, 9),
    _Pm200fr20PerfTelecomInputClientCurrent24StatSefsValuePortn_Type()
)
pm200fr20PerfTelecomInputClientCurrent24StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientCurrent24StatSefsValuePortn.setStatus("current")
_Pm200fr20PerfTelecomInputClientCurrent24StatInvUasPortn_Type = EkiOnOff
_Pm200fr20PerfTelecomInputClientCurrent24StatInvUasPortn_Object = MibTableColumn
pm200fr20PerfTelecomInputClientCurrent24StatInvUasPortn = _Pm200fr20PerfTelecomInputClientCurrent24StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 80, 1, 10),
    _Pm200fr20PerfTelecomInputClientCurrent24StatInvUasPortn_Type()
)
pm200fr20PerfTelecomInputClientCurrent24StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientCurrent24StatInvUasPortn.setStatus("current")
_Pm200fr20PerfTelecomInputClientCurrent24StatUasValuePortn_Type = Unsigned32
_Pm200fr20PerfTelecomInputClientCurrent24StatUasValuePortn_Object = MibTableColumn
pm200fr20PerfTelecomInputClientCurrent24StatUasValuePortn = _Pm200fr20PerfTelecomInputClientCurrent24StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 80, 1, 11),
    _Pm200fr20PerfTelecomInputClientCurrent24StatUasValuePortn_Type()
)
pm200fr20PerfTelecomInputClientCurrent24StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientCurrent24StatUasValuePortn.setStatus("current")
_Pm200fr20PerfTelecomInputClientPast24StatHistoryPort1Table_Object = MibTable
pm200fr20PerfTelecomInputClientPast24StatHistoryPort1Table = _Pm200fr20PerfTelecomInputClientPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 112)
)
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientPast24StatHistoryPort1Table.setStatus("current")
_Pm200fr20PerfTelecomInputClientPast24StatHistoryPort1Entry_Object = MibTableRow
pm200fr20PerfTelecomInputClientPast24StatHistoryPort1Entry = _Pm200fr20PerfTelecomInputClientPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 112, 1)
)
pm200fr20PerfTelecomInputClientPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20PerfTelecomInputClientPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientPast24StatHistoryPort1Entry.setStatus("current")


class _Pm200fr20PerfTelecomInputClientPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pm200fr20PerfTelecomInputClientPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20PerfTelecomInputClientPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm200fr20PerfTelecomInputClientPast24StatHistoryPort1Index_Object = MibTableColumn
pm200fr20PerfTelecomInputClientPast24StatHistoryPort1Index = _Pm200fr20PerfTelecomInputClientPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 112, 1, 1),
    _Pm200fr20PerfTelecomInputClientPast24StatHistoryPort1Index_Type()
)
pm200fr20PerfTelecomInputClientPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientPast24StatHistoryPort1Index.setStatus("current")
_Pm200fr20PerfTelecomInputClientPast24StatHistoryInvCvPort1_Type = EkiOnOff
_Pm200fr20PerfTelecomInputClientPast24StatHistoryInvCvPort1_Object = MibTableColumn
pm200fr20PerfTelecomInputClientPast24StatHistoryInvCvPort1 = _Pm200fr20PerfTelecomInputClientPast24StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 112, 1, 2),
    _Pm200fr20PerfTelecomInputClientPast24StatHistoryInvCvPort1_Type()
)
pm200fr20PerfTelecomInputClientPast24StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientPast24StatHistoryInvCvPort1.setStatus("current")
_Pm200fr20PerfTelecomInputClientPast24StatHistoryCvValuePort1_Type = Unsigned32
_Pm200fr20PerfTelecomInputClientPast24StatHistoryCvValuePort1_Object = MibTableColumn
pm200fr20PerfTelecomInputClientPast24StatHistoryCvValuePort1 = _Pm200fr20PerfTelecomInputClientPast24StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 112, 1, 3),
    _Pm200fr20PerfTelecomInputClientPast24StatHistoryCvValuePort1_Type()
)
pm200fr20PerfTelecomInputClientPast24StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientPast24StatHistoryCvValuePort1.setStatus("current")
_Pm200fr20PerfTelecomInputClientPast24StatHistoryInvEsPort1_Type = EkiOnOff
_Pm200fr20PerfTelecomInputClientPast24StatHistoryInvEsPort1_Object = MibTableColumn
pm200fr20PerfTelecomInputClientPast24StatHistoryInvEsPort1 = _Pm200fr20PerfTelecomInputClientPast24StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 112, 1, 4),
    _Pm200fr20PerfTelecomInputClientPast24StatHistoryInvEsPort1_Type()
)
pm200fr20PerfTelecomInputClientPast24StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientPast24StatHistoryInvEsPort1.setStatus("current")
_Pm200fr20PerfTelecomInputClientPast24StatHistoryEsValuePort1_Type = Unsigned32
_Pm200fr20PerfTelecomInputClientPast24StatHistoryEsValuePort1_Object = MibTableColumn
pm200fr20PerfTelecomInputClientPast24StatHistoryEsValuePort1 = _Pm200fr20PerfTelecomInputClientPast24StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 112, 1, 5),
    _Pm200fr20PerfTelecomInputClientPast24StatHistoryEsValuePort1_Type()
)
pm200fr20PerfTelecomInputClientPast24StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientPast24StatHistoryEsValuePort1.setStatus("current")
_Pm200fr20PerfTelecomInputClientPast24StatHistoryInvSesPort1_Type = EkiOnOff
_Pm200fr20PerfTelecomInputClientPast24StatHistoryInvSesPort1_Object = MibTableColumn
pm200fr20PerfTelecomInputClientPast24StatHistoryInvSesPort1 = _Pm200fr20PerfTelecomInputClientPast24StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 112, 1, 6),
    _Pm200fr20PerfTelecomInputClientPast24StatHistoryInvSesPort1_Type()
)
pm200fr20PerfTelecomInputClientPast24StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientPast24StatHistoryInvSesPort1.setStatus("current")
_Pm200fr20PerfTelecomInputClientPast24StatHistorySesValuePort1_Type = Unsigned32
_Pm200fr20PerfTelecomInputClientPast24StatHistorySesValuePort1_Object = MibTableColumn
pm200fr20PerfTelecomInputClientPast24StatHistorySesValuePort1 = _Pm200fr20PerfTelecomInputClientPast24StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 112, 1, 7),
    _Pm200fr20PerfTelecomInputClientPast24StatHistorySesValuePort1_Type()
)
pm200fr20PerfTelecomInputClientPast24StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientPast24StatHistorySesValuePort1.setStatus("current")
_Pm200fr20PerfTelecomInputClientPast24StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm200fr20PerfTelecomInputClientPast24StatHistoryInvSefsPort1_Object = MibTableColumn
pm200fr20PerfTelecomInputClientPast24StatHistoryInvSefsPort1 = _Pm200fr20PerfTelecomInputClientPast24StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 112, 1, 8),
    _Pm200fr20PerfTelecomInputClientPast24StatHistoryInvSefsPort1_Type()
)
pm200fr20PerfTelecomInputClientPast24StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientPast24StatHistoryInvSefsPort1.setStatus("current")
_Pm200fr20PerfTelecomInputClientPast24StatHistorySefsValuePort1_Type = Unsigned32
_Pm200fr20PerfTelecomInputClientPast24StatHistorySefsValuePort1_Object = MibTableColumn
pm200fr20PerfTelecomInputClientPast24StatHistorySefsValuePort1 = _Pm200fr20PerfTelecomInputClientPast24StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 112, 1, 9),
    _Pm200fr20PerfTelecomInputClientPast24StatHistorySefsValuePort1_Type()
)
pm200fr20PerfTelecomInputClientPast24StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientPast24StatHistorySefsValuePort1.setStatus("current")
_Pm200fr20PerfTelecomInputClientPast24StatHistoryInvUasPort1_Type = EkiOnOff
_Pm200fr20PerfTelecomInputClientPast24StatHistoryInvUasPort1_Object = MibTableColumn
pm200fr20PerfTelecomInputClientPast24StatHistoryInvUasPort1 = _Pm200fr20PerfTelecomInputClientPast24StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 112, 1, 10),
    _Pm200fr20PerfTelecomInputClientPast24StatHistoryInvUasPort1_Type()
)
pm200fr20PerfTelecomInputClientPast24StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientPast24StatHistoryInvUasPort1.setStatus("current")
_Pm200fr20PerfTelecomInputClientPast24StatHistoryUasValuePort1_Type = Unsigned32
_Pm200fr20PerfTelecomInputClientPast24StatHistoryUasValuePort1_Object = MibTableColumn
pm200fr20PerfTelecomInputClientPast24StatHistoryUasValuePort1 = _Pm200fr20PerfTelecomInputClientPast24StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 112, 1, 11),
    _Pm200fr20PerfTelecomInputClientPast24StatHistoryUasValuePort1_Type()
)
pm200fr20PerfTelecomInputClientPast24StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomInputClientPast24StatHistoryUasValuePort1.setStatus("current")
_Pm200fr20PerfTelecomOutputClientCurrent15StatTable_Object = MibTable
pm200fr20PerfTelecomOutputClientCurrent15StatTable = _Pm200fr20PerfTelecomOutputClientCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 144)
)
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientCurrent15StatTable.setStatus("current")
_Pm200fr20PerfTelecomOutputClientCurrent15StatEntry_Object = MibTableRow
pm200fr20PerfTelecomOutputClientCurrent15StatEntry = _Pm200fr20PerfTelecomOutputClientCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 144, 1)
)
pm200fr20PerfTelecomOutputClientCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20PerfTelecomOutputClientCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientCurrent15StatEntry.setStatus("current")


class _Pm200fr20PerfTelecomOutputClientCurrent15StatIndex_Type(Integer32):
    """Custom type pm200fr20PerfTelecomOutputClientCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20PerfTelecomOutputClientCurrent15StatIndex_Type.__name__ = "Integer32"
_Pm200fr20PerfTelecomOutputClientCurrent15StatIndex_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientCurrent15StatIndex = _Pm200fr20PerfTelecomOutputClientCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 144, 1, 1),
    _Pm200fr20PerfTelecomOutputClientCurrent15StatIndex_Type()
)
pm200fr20PerfTelecomOutputClientCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientCurrent15StatIndex.setStatus("current")
_Pm200fr20PerfTelecomOutputClientCurrent15StatInvCvPortn_Type = EkiOnOff
_Pm200fr20PerfTelecomOutputClientCurrent15StatInvCvPortn_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientCurrent15StatInvCvPortn = _Pm200fr20PerfTelecomOutputClientCurrent15StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 144, 1, 2),
    _Pm200fr20PerfTelecomOutputClientCurrent15StatInvCvPortn_Type()
)
pm200fr20PerfTelecomOutputClientCurrent15StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientCurrent15StatInvCvPortn.setStatus("current")
_Pm200fr20PerfTelecomOutputClientCurrent15StatCvValuePortn_Type = Unsigned32
_Pm200fr20PerfTelecomOutputClientCurrent15StatCvValuePortn_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientCurrent15StatCvValuePortn = _Pm200fr20PerfTelecomOutputClientCurrent15StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 144, 1, 3),
    _Pm200fr20PerfTelecomOutputClientCurrent15StatCvValuePortn_Type()
)
pm200fr20PerfTelecomOutputClientCurrent15StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientCurrent15StatCvValuePortn.setStatus("current")
_Pm200fr20PerfTelecomOutputClientCurrent15StatInvEsPortn_Type = EkiOnOff
_Pm200fr20PerfTelecomOutputClientCurrent15StatInvEsPortn_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientCurrent15StatInvEsPortn = _Pm200fr20PerfTelecomOutputClientCurrent15StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 144, 1, 4),
    _Pm200fr20PerfTelecomOutputClientCurrent15StatInvEsPortn_Type()
)
pm200fr20PerfTelecomOutputClientCurrent15StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientCurrent15StatInvEsPortn.setStatus("current")
_Pm200fr20PerfTelecomOutputClientCurrent15StatEsValuePortn_Type = Unsigned32
_Pm200fr20PerfTelecomOutputClientCurrent15StatEsValuePortn_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientCurrent15StatEsValuePortn = _Pm200fr20PerfTelecomOutputClientCurrent15StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 144, 1, 5),
    _Pm200fr20PerfTelecomOutputClientCurrent15StatEsValuePortn_Type()
)
pm200fr20PerfTelecomOutputClientCurrent15StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientCurrent15StatEsValuePortn.setStatus("current")
_Pm200fr20PerfTelecomOutputClientCurrent15StatInvSesPortn_Type = EkiOnOff
_Pm200fr20PerfTelecomOutputClientCurrent15StatInvSesPortn_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientCurrent15StatInvSesPortn = _Pm200fr20PerfTelecomOutputClientCurrent15StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 144, 1, 6),
    _Pm200fr20PerfTelecomOutputClientCurrent15StatInvSesPortn_Type()
)
pm200fr20PerfTelecomOutputClientCurrent15StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientCurrent15StatInvSesPortn.setStatus("current")
_Pm200fr20PerfTelecomOutputClientCurrent15StatSesValuePortn_Type = Unsigned32
_Pm200fr20PerfTelecomOutputClientCurrent15StatSesValuePortn_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientCurrent15StatSesValuePortn = _Pm200fr20PerfTelecomOutputClientCurrent15StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 144, 1, 7),
    _Pm200fr20PerfTelecomOutputClientCurrent15StatSesValuePortn_Type()
)
pm200fr20PerfTelecomOutputClientCurrent15StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientCurrent15StatSesValuePortn.setStatus("current")
_Pm200fr20PerfTelecomOutputClientCurrent15StatInvSefsPortn_Type = EkiOnOff
_Pm200fr20PerfTelecomOutputClientCurrent15StatInvSefsPortn_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientCurrent15StatInvSefsPortn = _Pm200fr20PerfTelecomOutputClientCurrent15StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 144, 1, 8),
    _Pm200fr20PerfTelecomOutputClientCurrent15StatInvSefsPortn_Type()
)
pm200fr20PerfTelecomOutputClientCurrent15StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientCurrent15StatInvSefsPortn.setStatus("current")
_Pm200fr20PerfTelecomOutputClientCurrent15StatSefsValuePortn_Type = Unsigned32
_Pm200fr20PerfTelecomOutputClientCurrent15StatSefsValuePortn_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientCurrent15StatSefsValuePortn = _Pm200fr20PerfTelecomOutputClientCurrent15StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 144, 1, 9),
    _Pm200fr20PerfTelecomOutputClientCurrent15StatSefsValuePortn_Type()
)
pm200fr20PerfTelecomOutputClientCurrent15StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientCurrent15StatSefsValuePortn.setStatus("current")
_Pm200fr20PerfTelecomOutputClientCurrent15StatInvUasPortn_Type = EkiOnOff
_Pm200fr20PerfTelecomOutputClientCurrent15StatInvUasPortn_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientCurrent15StatInvUasPortn = _Pm200fr20PerfTelecomOutputClientCurrent15StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 144, 1, 10),
    _Pm200fr20PerfTelecomOutputClientCurrent15StatInvUasPortn_Type()
)
pm200fr20PerfTelecomOutputClientCurrent15StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientCurrent15StatInvUasPortn.setStatus("current")
_Pm200fr20PerfTelecomOutputClientCurrent15StatUasValuePortn_Type = Unsigned32
_Pm200fr20PerfTelecomOutputClientCurrent15StatUasValuePortn_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientCurrent15StatUasValuePortn = _Pm200fr20PerfTelecomOutputClientCurrent15StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 144, 1, 11),
    _Pm200fr20PerfTelecomOutputClientCurrent15StatUasValuePortn_Type()
)
pm200fr20PerfTelecomOutputClientCurrent15StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientCurrent15StatUasValuePortn.setStatus("current")
_Pm200fr20PerfTelecomOutputClientPast15StatHistoryPort1Table_Object = MibTable
pm200fr20PerfTelecomOutputClientPast15StatHistoryPort1Table = _Pm200fr20PerfTelecomOutputClientPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 176)
)
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientPast15StatHistoryPort1Table.setStatus("current")
_Pm200fr20PerfTelecomOutputClientPast15StatHistoryPort1Entry_Object = MibTableRow
pm200fr20PerfTelecomOutputClientPast15StatHistoryPort1Entry = _Pm200fr20PerfTelecomOutputClientPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 176, 1)
)
pm200fr20PerfTelecomOutputClientPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20PerfTelecomOutputClientPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientPast15StatHistoryPort1Entry.setStatus("current")


class _Pm200fr20PerfTelecomOutputClientPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pm200fr20PerfTelecomOutputClientPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20PerfTelecomOutputClientPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm200fr20PerfTelecomOutputClientPast15StatHistoryPort1Index_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientPast15StatHistoryPort1Index = _Pm200fr20PerfTelecomOutputClientPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 176, 1, 1),
    _Pm200fr20PerfTelecomOutputClientPast15StatHistoryPort1Index_Type()
)
pm200fr20PerfTelecomOutputClientPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientPast15StatHistoryPort1Index.setStatus("current")
_Pm200fr20PerfTelecomOutputClientPast15StatHistoryInvCvPort1_Type = EkiOnOff
_Pm200fr20PerfTelecomOutputClientPast15StatHistoryInvCvPort1_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientPast15StatHistoryInvCvPort1 = _Pm200fr20PerfTelecomOutputClientPast15StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 176, 1, 2),
    _Pm200fr20PerfTelecomOutputClientPast15StatHistoryInvCvPort1_Type()
)
pm200fr20PerfTelecomOutputClientPast15StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientPast15StatHistoryInvCvPort1.setStatus("current")
_Pm200fr20PerfTelecomOutputClientPast15StatHistoryCvValuePort1_Type = Unsigned32
_Pm200fr20PerfTelecomOutputClientPast15StatHistoryCvValuePort1_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientPast15StatHistoryCvValuePort1 = _Pm200fr20PerfTelecomOutputClientPast15StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 176, 1, 3),
    _Pm200fr20PerfTelecomOutputClientPast15StatHistoryCvValuePort1_Type()
)
pm200fr20PerfTelecomOutputClientPast15StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientPast15StatHistoryCvValuePort1.setStatus("current")
_Pm200fr20PerfTelecomOutputClientPast15StatHistoryInvEsPort1_Type = EkiOnOff
_Pm200fr20PerfTelecomOutputClientPast15StatHistoryInvEsPort1_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientPast15StatHistoryInvEsPort1 = _Pm200fr20PerfTelecomOutputClientPast15StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 176, 1, 4),
    _Pm200fr20PerfTelecomOutputClientPast15StatHistoryInvEsPort1_Type()
)
pm200fr20PerfTelecomOutputClientPast15StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientPast15StatHistoryInvEsPort1.setStatus("current")
_Pm200fr20PerfTelecomOutputClientPast15StatHistoryEsValuePort1_Type = Unsigned32
_Pm200fr20PerfTelecomOutputClientPast15StatHistoryEsValuePort1_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientPast15StatHistoryEsValuePort1 = _Pm200fr20PerfTelecomOutputClientPast15StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 176, 1, 5),
    _Pm200fr20PerfTelecomOutputClientPast15StatHistoryEsValuePort1_Type()
)
pm200fr20PerfTelecomOutputClientPast15StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientPast15StatHistoryEsValuePort1.setStatus("current")
_Pm200fr20PerfTelecomOutputClientPast15StatHistoryInvSesPort1_Type = EkiOnOff
_Pm200fr20PerfTelecomOutputClientPast15StatHistoryInvSesPort1_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientPast15StatHistoryInvSesPort1 = _Pm200fr20PerfTelecomOutputClientPast15StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 176, 1, 6),
    _Pm200fr20PerfTelecomOutputClientPast15StatHistoryInvSesPort1_Type()
)
pm200fr20PerfTelecomOutputClientPast15StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientPast15StatHistoryInvSesPort1.setStatus("current")
_Pm200fr20PerfTelecomOutputClientPast15StatHistorySesValuePort1_Type = Unsigned32
_Pm200fr20PerfTelecomOutputClientPast15StatHistorySesValuePort1_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientPast15StatHistorySesValuePort1 = _Pm200fr20PerfTelecomOutputClientPast15StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 176, 1, 7),
    _Pm200fr20PerfTelecomOutputClientPast15StatHistorySesValuePort1_Type()
)
pm200fr20PerfTelecomOutputClientPast15StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientPast15StatHistorySesValuePort1.setStatus("current")
_Pm200fr20PerfTelecomOutputClientPast15StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm200fr20PerfTelecomOutputClientPast15StatHistoryInvSefsPort1_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientPast15StatHistoryInvSefsPort1 = _Pm200fr20PerfTelecomOutputClientPast15StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 176, 1, 8),
    _Pm200fr20PerfTelecomOutputClientPast15StatHistoryInvSefsPort1_Type()
)
pm200fr20PerfTelecomOutputClientPast15StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientPast15StatHistoryInvSefsPort1.setStatus("current")
_Pm200fr20PerfTelecomOutputClientPast15StatHistorySefsValuePort1_Type = Unsigned32
_Pm200fr20PerfTelecomOutputClientPast15StatHistorySefsValuePort1_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientPast15StatHistorySefsValuePort1 = _Pm200fr20PerfTelecomOutputClientPast15StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 176, 1, 9),
    _Pm200fr20PerfTelecomOutputClientPast15StatHistorySefsValuePort1_Type()
)
pm200fr20PerfTelecomOutputClientPast15StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientPast15StatHistorySefsValuePort1.setStatus("current")
_Pm200fr20PerfTelecomOutputClientPast15StatHistoryInvUasPort1_Type = EkiOnOff
_Pm200fr20PerfTelecomOutputClientPast15StatHistoryInvUasPort1_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientPast15StatHistoryInvUasPort1 = _Pm200fr20PerfTelecomOutputClientPast15StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 176, 1, 10),
    _Pm200fr20PerfTelecomOutputClientPast15StatHistoryInvUasPort1_Type()
)
pm200fr20PerfTelecomOutputClientPast15StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientPast15StatHistoryInvUasPort1.setStatus("current")
_Pm200fr20PerfTelecomOutputClientPast15StatHistoryUasValuePort1_Type = Unsigned32
_Pm200fr20PerfTelecomOutputClientPast15StatHistoryUasValuePort1_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientPast15StatHistoryUasValuePort1 = _Pm200fr20PerfTelecomOutputClientPast15StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 176, 1, 11),
    _Pm200fr20PerfTelecomOutputClientPast15StatHistoryUasValuePort1_Type()
)
pm200fr20PerfTelecomOutputClientPast15StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientPast15StatHistoryUasValuePort1.setStatus("current")
_Pm200fr20PerfTelecomOutputClientCurrent24StatTable_Object = MibTable
pm200fr20PerfTelecomOutputClientCurrent24StatTable = _Pm200fr20PerfTelecomOutputClientCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 208)
)
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientCurrent24StatTable.setStatus("current")
_Pm200fr20PerfTelecomOutputClientCurrent24StatEntry_Object = MibTableRow
pm200fr20PerfTelecomOutputClientCurrent24StatEntry = _Pm200fr20PerfTelecomOutputClientCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 208, 1)
)
pm200fr20PerfTelecomOutputClientCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20PerfTelecomOutputClientCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientCurrent24StatEntry.setStatus("current")


class _Pm200fr20PerfTelecomOutputClientCurrent24StatIndex_Type(Integer32):
    """Custom type pm200fr20PerfTelecomOutputClientCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20PerfTelecomOutputClientCurrent24StatIndex_Type.__name__ = "Integer32"
_Pm200fr20PerfTelecomOutputClientCurrent24StatIndex_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientCurrent24StatIndex = _Pm200fr20PerfTelecomOutputClientCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 208, 1, 1),
    _Pm200fr20PerfTelecomOutputClientCurrent24StatIndex_Type()
)
pm200fr20PerfTelecomOutputClientCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientCurrent24StatIndex.setStatus("current")
_Pm200fr20PerfTelecomOutputClientCurrent24StatInvCvPortn_Type = EkiOnOff
_Pm200fr20PerfTelecomOutputClientCurrent24StatInvCvPortn_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientCurrent24StatInvCvPortn = _Pm200fr20PerfTelecomOutputClientCurrent24StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 208, 1, 2),
    _Pm200fr20PerfTelecomOutputClientCurrent24StatInvCvPortn_Type()
)
pm200fr20PerfTelecomOutputClientCurrent24StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientCurrent24StatInvCvPortn.setStatus("current")
_Pm200fr20PerfTelecomOutputClientCurrent24StatCvValuePortn_Type = Unsigned32
_Pm200fr20PerfTelecomOutputClientCurrent24StatCvValuePortn_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientCurrent24StatCvValuePortn = _Pm200fr20PerfTelecomOutputClientCurrent24StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 208, 1, 3),
    _Pm200fr20PerfTelecomOutputClientCurrent24StatCvValuePortn_Type()
)
pm200fr20PerfTelecomOutputClientCurrent24StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientCurrent24StatCvValuePortn.setStatus("current")
_Pm200fr20PerfTelecomOutputClientCurrent24StatInvEsPortn_Type = EkiOnOff
_Pm200fr20PerfTelecomOutputClientCurrent24StatInvEsPortn_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientCurrent24StatInvEsPortn = _Pm200fr20PerfTelecomOutputClientCurrent24StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 208, 1, 4),
    _Pm200fr20PerfTelecomOutputClientCurrent24StatInvEsPortn_Type()
)
pm200fr20PerfTelecomOutputClientCurrent24StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientCurrent24StatInvEsPortn.setStatus("current")
_Pm200fr20PerfTelecomOutputClientCurrent24StatEsValuePortn_Type = Unsigned32
_Pm200fr20PerfTelecomOutputClientCurrent24StatEsValuePortn_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientCurrent24StatEsValuePortn = _Pm200fr20PerfTelecomOutputClientCurrent24StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 208, 1, 5),
    _Pm200fr20PerfTelecomOutputClientCurrent24StatEsValuePortn_Type()
)
pm200fr20PerfTelecomOutputClientCurrent24StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientCurrent24StatEsValuePortn.setStatus("current")
_Pm200fr20PerfTelecomOutputClientCurrent24StatInvSesPortn_Type = EkiOnOff
_Pm200fr20PerfTelecomOutputClientCurrent24StatInvSesPortn_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientCurrent24StatInvSesPortn = _Pm200fr20PerfTelecomOutputClientCurrent24StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 208, 1, 6),
    _Pm200fr20PerfTelecomOutputClientCurrent24StatInvSesPortn_Type()
)
pm200fr20PerfTelecomOutputClientCurrent24StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientCurrent24StatInvSesPortn.setStatus("current")
_Pm200fr20PerfTelecomOutputClientCurrent24StatSesValuePortn_Type = Unsigned32
_Pm200fr20PerfTelecomOutputClientCurrent24StatSesValuePortn_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientCurrent24StatSesValuePortn = _Pm200fr20PerfTelecomOutputClientCurrent24StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 208, 1, 7),
    _Pm200fr20PerfTelecomOutputClientCurrent24StatSesValuePortn_Type()
)
pm200fr20PerfTelecomOutputClientCurrent24StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientCurrent24StatSesValuePortn.setStatus("current")
_Pm200fr20PerfTelecomOutputClientCurrent24StatInvSefsPortn_Type = EkiOnOff
_Pm200fr20PerfTelecomOutputClientCurrent24StatInvSefsPortn_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientCurrent24StatInvSefsPortn = _Pm200fr20PerfTelecomOutputClientCurrent24StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 208, 1, 8),
    _Pm200fr20PerfTelecomOutputClientCurrent24StatInvSefsPortn_Type()
)
pm200fr20PerfTelecomOutputClientCurrent24StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientCurrent24StatInvSefsPortn.setStatus("current")
_Pm200fr20PerfTelecomOutputClientCurrent24StatSefsValuePortn_Type = Unsigned32
_Pm200fr20PerfTelecomOutputClientCurrent24StatSefsValuePortn_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientCurrent24StatSefsValuePortn = _Pm200fr20PerfTelecomOutputClientCurrent24StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 208, 1, 9),
    _Pm200fr20PerfTelecomOutputClientCurrent24StatSefsValuePortn_Type()
)
pm200fr20PerfTelecomOutputClientCurrent24StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientCurrent24StatSefsValuePortn.setStatus("current")
_Pm200fr20PerfTelecomOutputClientCurrent24StatInvUasPortn_Type = EkiOnOff
_Pm200fr20PerfTelecomOutputClientCurrent24StatInvUasPortn_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientCurrent24StatInvUasPortn = _Pm200fr20PerfTelecomOutputClientCurrent24StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 208, 1, 10),
    _Pm200fr20PerfTelecomOutputClientCurrent24StatInvUasPortn_Type()
)
pm200fr20PerfTelecomOutputClientCurrent24StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientCurrent24StatInvUasPortn.setStatus("current")
_Pm200fr20PerfTelecomOutputClientCurrent24StatUasValuePortn_Type = Unsigned32
_Pm200fr20PerfTelecomOutputClientCurrent24StatUasValuePortn_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientCurrent24StatUasValuePortn = _Pm200fr20PerfTelecomOutputClientCurrent24StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 208, 1, 11),
    _Pm200fr20PerfTelecomOutputClientCurrent24StatUasValuePortn_Type()
)
pm200fr20PerfTelecomOutputClientCurrent24StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientCurrent24StatUasValuePortn.setStatus("current")
_Pm200fr20PerfTelecomOutputClientPast24StatHistoryPort1Table_Object = MibTable
pm200fr20PerfTelecomOutputClientPast24StatHistoryPort1Table = _Pm200fr20PerfTelecomOutputClientPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 240)
)
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientPast24StatHistoryPort1Table.setStatus("current")
_Pm200fr20PerfTelecomOutputClientPast24StatHistoryPort1Entry_Object = MibTableRow
pm200fr20PerfTelecomOutputClientPast24StatHistoryPort1Entry = _Pm200fr20PerfTelecomOutputClientPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 240, 1)
)
pm200fr20PerfTelecomOutputClientPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20PerfTelecomOutputClientPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientPast24StatHistoryPort1Entry.setStatus("current")


class _Pm200fr20PerfTelecomOutputClientPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pm200fr20PerfTelecomOutputClientPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20PerfTelecomOutputClientPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm200fr20PerfTelecomOutputClientPast24StatHistoryPort1Index_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientPast24StatHistoryPort1Index = _Pm200fr20PerfTelecomOutputClientPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 240, 1, 1),
    _Pm200fr20PerfTelecomOutputClientPast24StatHistoryPort1Index_Type()
)
pm200fr20PerfTelecomOutputClientPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientPast24StatHistoryPort1Index.setStatus("current")
_Pm200fr20PerfTelecomOutputClientPast24StatHistoryInvCvPort1_Type = EkiOnOff
_Pm200fr20PerfTelecomOutputClientPast24StatHistoryInvCvPort1_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientPast24StatHistoryInvCvPort1 = _Pm200fr20PerfTelecomOutputClientPast24StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 240, 1, 2),
    _Pm200fr20PerfTelecomOutputClientPast24StatHistoryInvCvPort1_Type()
)
pm200fr20PerfTelecomOutputClientPast24StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientPast24StatHistoryInvCvPort1.setStatus("current")
_Pm200fr20PerfTelecomOutputClientPast24StatHistoryCvValuePort1_Type = Unsigned32
_Pm200fr20PerfTelecomOutputClientPast24StatHistoryCvValuePort1_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientPast24StatHistoryCvValuePort1 = _Pm200fr20PerfTelecomOutputClientPast24StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 240, 1, 3),
    _Pm200fr20PerfTelecomOutputClientPast24StatHistoryCvValuePort1_Type()
)
pm200fr20PerfTelecomOutputClientPast24StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientPast24StatHistoryCvValuePort1.setStatus("current")
_Pm200fr20PerfTelecomOutputClientPast24StatHistoryInvEsPort1_Type = EkiOnOff
_Pm200fr20PerfTelecomOutputClientPast24StatHistoryInvEsPort1_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientPast24StatHistoryInvEsPort1 = _Pm200fr20PerfTelecomOutputClientPast24StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 240, 1, 4),
    _Pm200fr20PerfTelecomOutputClientPast24StatHistoryInvEsPort1_Type()
)
pm200fr20PerfTelecomOutputClientPast24StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientPast24StatHistoryInvEsPort1.setStatus("current")
_Pm200fr20PerfTelecomOutputClientPast24StatHistoryEsValuePort1_Type = Unsigned32
_Pm200fr20PerfTelecomOutputClientPast24StatHistoryEsValuePort1_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientPast24StatHistoryEsValuePort1 = _Pm200fr20PerfTelecomOutputClientPast24StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 240, 1, 5),
    _Pm200fr20PerfTelecomOutputClientPast24StatHistoryEsValuePort1_Type()
)
pm200fr20PerfTelecomOutputClientPast24StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientPast24StatHistoryEsValuePort1.setStatus("current")
_Pm200fr20PerfTelecomOutputClientPast24StatHistoryInvSesPort1_Type = EkiOnOff
_Pm200fr20PerfTelecomOutputClientPast24StatHistoryInvSesPort1_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientPast24StatHistoryInvSesPort1 = _Pm200fr20PerfTelecomOutputClientPast24StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 240, 1, 6),
    _Pm200fr20PerfTelecomOutputClientPast24StatHistoryInvSesPort1_Type()
)
pm200fr20PerfTelecomOutputClientPast24StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientPast24StatHistoryInvSesPort1.setStatus("current")
_Pm200fr20PerfTelecomOutputClientPast24StatHistorySesValuePort1_Type = Unsigned32
_Pm200fr20PerfTelecomOutputClientPast24StatHistorySesValuePort1_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientPast24StatHistorySesValuePort1 = _Pm200fr20PerfTelecomOutputClientPast24StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 240, 1, 7),
    _Pm200fr20PerfTelecomOutputClientPast24StatHistorySesValuePort1_Type()
)
pm200fr20PerfTelecomOutputClientPast24StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientPast24StatHistorySesValuePort1.setStatus("current")
_Pm200fr20PerfTelecomOutputClientPast24StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm200fr20PerfTelecomOutputClientPast24StatHistoryInvSefsPort1_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientPast24StatHistoryInvSefsPort1 = _Pm200fr20PerfTelecomOutputClientPast24StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 240, 1, 8),
    _Pm200fr20PerfTelecomOutputClientPast24StatHistoryInvSefsPort1_Type()
)
pm200fr20PerfTelecomOutputClientPast24StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientPast24StatHistoryInvSefsPort1.setStatus("current")
_Pm200fr20PerfTelecomOutputClientPast24StatHistorySefsValuePort1_Type = Unsigned32
_Pm200fr20PerfTelecomOutputClientPast24StatHistorySefsValuePort1_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientPast24StatHistorySefsValuePort1 = _Pm200fr20PerfTelecomOutputClientPast24StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 240, 1, 9),
    _Pm200fr20PerfTelecomOutputClientPast24StatHistorySefsValuePort1_Type()
)
pm200fr20PerfTelecomOutputClientPast24StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientPast24StatHistorySefsValuePort1.setStatus("current")
_Pm200fr20PerfTelecomOutputClientPast24StatHistoryInvUasPort1_Type = EkiOnOff
_Pm200fr20PerfTelecomOutputClientPast24StatHistoryInvUasPort1_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientPast24StatHistoryInvUasPort1 = _Pm200fr20PerfTelecomOutputClientPast24StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 240, 1, 10),
    _Pm200fr20PerfTelecomOutputClientPast24StatHistoryInvUasPort1_Type()
)
pm200fr20PerfTelecomOutputClientPast24StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientPast24StatHistoryInvUasPort1.setStatus("current")
_Pm200fr20PerfTelecomOutputClientPast24StatHistoryUasValuePort1_Type = Unsigned32
_Pm200fr20PerfTelecomOutputClientPast24StatHistoryUasValuePort1_Object = MibTableColumn
pm200fr20PerfTelecomOutputClientPast24StatHistoryUasValuePort1 = _Pm200fr20PerfTelecomOutputClientPast24StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 240, 1, 11),
    _Pm200fr20PerfTelecomOutputClientPast24StatHistoryUasValuePort1_Type()
)
pm200fr20PerfTelecomOutputClientPast24StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomOutputClientPast24StatHistoryUasValuePort1.setStatus("current")
_Pm200fr20PerfDatacomClientCurrent15StatTable_Object = MibTable
pm200fr20PerfDatacomClientCurrent15StatTable = _Pm200fr20PerfDatacomClientCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 848)
)
if mibBuilder.loadTexts:
    pm200fr20PerfDatacomClientCurrent15StatTable.setStatus("current")
_Pm200fr20PerfDatacomClientCurrent15StatEntry_Object = MibTableRow
pm200fr20PerfDatacomClientCurrent15StatEntry = _Pm200fr20PerfDatacomClientCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 848, 1)
)
pm200fr20PerfDatacomClientCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20PerfDatacomClientCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20PerfDatacomClientCurrent15StatEntry.setStatus("current")


class _Pm200fr20PerfDatacomClientCurrent15StatIndex_Type(Integer32):
    """Custom type pm200fr20PerfDatacomClientCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20PerfDatacomClientCurrent15StatIndex_Type.__name__ = "Integer32"
_Pm200fr20PerfDatacomClientCurrent15StatIndex_Object = MibTableColumn
pm200fr20PerfDatacomClientCurrent15StatIndex = _Pm200fr20PerfDatacomClientCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 848, 1, 1),
    _Pm200fr20PerfDatacomClientCurrent15StatIndex_Type()
)
pm200fr20PerfDatacomClientCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfDatacomClientCurrent15StatIndex.setStatus("current")
_Pm200fr20perfdatacomclientCurrent15StatInCrcCountInvPortn_Type = EkiOnOff
_Pm200fr20perfdatacomclientCurrent15StatInCrcCountInvPortn_Object = MibTableColumn
pm200fr20perfdatacomclientCurrent15StatInCrcCountInvPortn = _Pm200fr20perfdatacomclientCurrent15StatInCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 848, 1, 4),
    _Pm200fr20perfdatacomclientCurrent15StatInCrcCountInvPortn_Type()
)
pm200fr20perfdatacomclientCurrent15StatInCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20perfdatacomclientCurrent15StatInCrcCountInvPortn.setStatus("current")
_Pm200fr20perfdatacomclientCurrent15StatInCrcCountPortn_Type = Counter64
_Pm200fr20perfdatacomclientCurrent15StatInCrcCountPortn_Object = MibTableColumn
pm200fr20perfdatacomclientCurrent15StatInCrcCountPortn = _Pm200fr20perfdatacomclientCurrent15StatInCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 848, 1, 5),
    _Pm200fr20perfdatacomclientCurrent15StatInCrcCountPortn_Type()
)
pm200fr20perfdatacomclientCurrent15StatInCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20perfdatacomclientCurrent15StatInCrcCountPortn.setStatus("current")
_Pm200fr20perfdatacomclientCurrent15StatInPacketCountInvPortn_Type = EkiOnOff
_Pm200fr20perfdatacomclientCurrent15StatInPacketCountInvPortn_Object = MibTableColumn
pm200fr20perfdatacomclientCurrent15StatInPacketCountInvPortn = _Pm200fr20perfdatacomclientCurrent15StatInPacketCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 848, 1, 6),
    _Pm200fr20perfdatacomclientCurrent15StatInPacketCountInvPortn_Type()
)
pm200fr20perfdatacomclientCurrent15StatInPacketCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20perfdatacomclientCurrent15StatInPacketCountInvPortn.setStatus("current")
_Pm200fr20perfdatacomclientCurrent15StatInPacketCountPortn_Type = Counter64
_Pm200fr20perfdatacomclientCurrent15StatInPacketCountPortn_Object = MibTableColumn
pm200fr20perfdatacomclientCurrent15StatInPacketCountPortn = _Pm200fr20perfdatacomclientCurrent15StatInPacketCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 848, 1, 7),
    _Pm200fr20perfdatacomclientCurrent15StatInPacketCountPortn_Type()
)
pm200fr20perfdatacomclientCurrent15StatInPacketCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20perfdatacomclientCurrent15StatInPacketCountPortn.setStatus("current")
_Pm200fr20perfdatacomclientCurrent15StatOutCrcCountInvPortn_Type = EkiOnOff
_Pm200fr20perfdatacomclientCurrent15StatOutCrcCountInvPortn_Object = MibTableColumn
pm200fr20perfdatacomclientCurrent15StatOutCrcCountInvPortn = _Pm200fr20perfdatacomclientCurrent15StatOutCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 848, 1, 28),
    _Pm200fr20perfdatacomclientCurrent15StatOutCrcCountInvPortn_Type()
)
pm200fr20perfdatacomclientCurrent15StatOutCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20perfdatacomclientCurrent15StatOutCrcCountInvPortn.setStatus("current")
_Pm200fr20perfdatacomclientCurrent15StatOutCrcCountPortn_Type = Counter64
_Pm200fr20perfdatacomclientCurrent15StatOutCrcCountPortn_Object = MibTableColumn
pm200fr20perfdatacomclientCurrent15StatOutCrcCountPortn = _Pm200fr20perfdatacomclientCurrent15StatOutCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 848, 1, 29),
    _Pm200fr20perfdatacomclientCurrent15StatOutCrcCountPortn_Type()
)
pm200fr20perfdatacomclientCurrent15StatOutCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20perfdatacomclientCurrent15StatOutCrcCountPortn.setStatus("current")
_Pm200fr20perfdatacomclientCurrent15StatOutPacketCountInvPortn_Type = EkiOnOff
_Pm200fr20perfdatacomclientCurrent15StatOutPacketCountInvPortn_Object = MibTableColumn
pm200fr20perfdatacomclientCurrent15StatOutPacketCountInvPortn = _Pm200fr20perfdatacomclientCurrent15StatOutPacketCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 848, 1, 30),
    _Pm200fr20perfdatacomclientCurrent15StatOutPacketCountInvPortn_Type()
)
pm200fr20perfdatacomclientCurrent15StatOutPacketCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20perfdatacomclientCurrent15StatOutPacketCountInvPortn.setStatus("current")
_Pm200fr20perfdatacomclientCurrent15StatOutPacketCountPortn_Type = Counter64
_Pm200fr20perfdatacomclientCurrent15StatOutPacketCountPortn_Object = MibTableColumn
pm200fr20perfdatacomclientCurrent15StatOutPacketCountPortn = _Pm200fr20perfdatacomclientCurrent15StatOutPacketCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 848, 1, 31),
    _Pm200fr20perfdatacomclientCurrent15StatOutPacketCountPortn_Type()
)
pm200fr20perfdatacomclientCurrent15StatOutPacketCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20perfdatacomclientCurrent15StatOutPacketCountPortn.setStatus("current")
_Pm200fr20PerfDatacomClientPast15StatHistoryPort1Table_Object = MibTable
pm200fr20PerfDatacomClientPast15StatHistoryPort1Table = _Pm200fr20PerfDatacomClientPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 880)
)
if mibBuilder.loadTexts:
    pm200fr20PerfDatacomClientPast15StatHistoryPort1Table.setStatus("current")
_Pm200fr20PerfDatacomClientPast15StatHistoryPort1Entry_Object = MibTableRow
pm200fr20PerfDatacomClientPast15StatHistoryPort1Entry = _Pm200fr20PerfDatacomClientPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 880, 1)
)
pm200fr20PerfDatacomClientPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20PerfDatacomClientPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm200fr20PerfDatacomClientPast15StatHistoryPort1Entry.setStatus("current")


class _Pm200fr20PerfDatacomClientPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pm200fr20PerfDatacomClientPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20PerfDatacomClientPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm200fr20PerfDatacomClientPast15StatHistoryPort1Index_Object = MibTableColumn
pm200fr20PerfDatacomClientPast15StatHistoryPort1Index = _Pm200fr20PerfDatacomClientPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 880, 1, 1),
    _Pm200fr20PerfDatacomClientPast15StatHistoryPort1Index_Type()
)
pm200fr20PerfDatacomClientPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfDatacomClientPast15StatHistoryPort1Index.setStatus("current")
_Pm200fr20perfdatacomclientPast15StatInCrcCountInvPort1_Type = EkiOnOff
_Pm200fr20perfdatacomclientPast15StatInCrcCountInvPort1_Object = MibTableColumn
pm200fr20perfdatacomclientPast15StatInCrcCountInvPort1 = _Pm200fr20perfdatacomclientPast15StatInCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 880, 1, 4),
    _Pm200fr20perfdatacomclientPast15StatInCrcCountInvPort1_Type()
)
pm200fr20perfdatacomclientPast15StatInCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20perfdatacomclientPast15StatInCrcCountInvPort1.setStatus("current")
_Pm200fr20perfdatacomclientPast15StatInCrcCountPort1_Type = Counter64
_Pm200fr20perfdatacomclientPast15StatInCrcCountPort1_Object = MibTableColumn
pm200fr20perfdatacomclientPast15StatInCrcCountPort1 = _Pm200fr20perfdatacomclientPast15StatInCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 880, 1, 5),
    _Pm200fr20perfdatacomclientPast15StatInCrcCountPort1_Type()
)
pm200fr20perfdatacomclientPast15StatInCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20perfdatacomclientPast15StatInCrcCountPort1.setStatus("current")
_Pm200fr20perfdatacomclientPast15StatInPacketCountInvPort1_Type = EkiOnOff
_Pm200fr20perfdatacomclientPast15StatInPacketCountInvPort1_Object = MibTableColumn
pm200fr20perfdatacomclientPast15StatInPacketCountInvPort1 = _Pm200fr20perfdatacomclientPast15StatInPacketCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 880, 1, 6),
    _Pm200fr20perfdatacomclientPast15StatInPacketCountInvPort1_Type()
)
pm200fr20perfdatacomclientPast15StatInPacketCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20perfdatacomclientPast15StatInPacketCountInvPort1.setStatus("current")
_Pm200fr20perfdatacomclientPast15StatInPacketCountPort1_Type = Counter64
_Pm200fr20perfdatacomclientPast15StatInPacketCountPort1_Object = MibTableColumn
pm200fr20perfdatacomclientPast15StatInPacketCountPort1 = _Pm200fr20perfdatacomclientPast15StatInPacketCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 880, 1, 7),
    _Pm200fr20perfdatacomclientPast15StatInPacketCountPort1_Type()
)
pm200fr20perfdatacomclientPast15StatInPacketCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20perfdatacomclientPast15StatInPacketCountPort1.setStatus("current")
_Pm200fr20perfdatacomclientPast15StatOutCrcCountInvPort1_Type = EkiOnOff
_Pm200fr20perfdatacomclientPast15StatOutCrcCountInvPort1_Object = MibTableColumn
pm200fr20perfdatacomclientPast15StatOutCrcCountInvPort1 = _Pm200fr20perfdatacomclientPast15StatOutCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 880, 1, 28),
    _Pm200fr20perfdatacomclientPast15StatOutCrcCountInvPort1_Type()
)
pm200fr20perfdatacomclientPast15StatOutCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20perfdatacomclientPast15StatOutCrcCountInvPort1.setStatus("current")
_Pm200fr20perfdatacomclientPast15StatOutCrcCountPort1_Type = Counter64
_Pm200fr20perfdatacomclientPast15StatOutCrcCountPort1_Object = MibTableColumn
pm200fr20perfdatacomclientPast15StatOutCrcCountPort1 = _Pm200fr20perfdatacomclientPast15StatOutCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 880, 1, 29),
    _Pm200fr20perfdatacomclientPast15StatOutCrcCountPort1_Type()
)
pm200fr20perfdatacomclientPast15StatOutCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20perfdatacomclientPast15StatOutCrcCountPort1.setStatus("current")
_Pm200fr20perfdatacomclientPast15StatOutPacketCountInvPort1_Type = EkiOnOff
_Pm200fr20perfdatacomclientPast15StatOutPacketCountInvPort1_Object = MibTableColumn
pm200fr20perfdatacomclientPast15StatOutPacketCountInvPort1 = _Pm200fr20perfdatacomclientPast15StatOutPacketCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 880, 1, 30),
    _Pm200fr20perfdatacomclientPast15StatOutPacketCountInvPort1_Type()
)
pm200fr20perfdatacomclientPast15StatOutPacketCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20perfdatacomclientPast15StatOutPacketCountInvPort1.setStatus("current")
_Pm200fr20perfdatacomclientPast15StatOutPacketCountPort1_Type = Counter64
_Pm200fr20perfdatacomclientPast15StatOutPacketCountPort1_Object = MibTableColumn
pm200fr20perfdatacomclientPast15StatOutPacketCountPort1 = _Pm200fr20perfdatacomclientPast15StatOutPacketCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 880, 1, 31),
    _Pm200fr20perfdatacomclientPast15StatOutPacketCountPort1_Type()
)
pm200fr20perfdatacomclientPast15StatOutPacketCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20perfdatacomclientPast15StatOutPacketCountPort1.setStatus("current")
_Pm200fr20PerfDatacomClientCurrent24StatTable_Object = MibTable
pm200fr20PerfDatacomClientCurrent24StatTable = _Pm200fr20PerfDatacomClientCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 912)
)
if mibBuilder.loadTexts:
    pm200fr20PerfDatacomClientCurrent24StatTable.setStatus("current")
_Pm200fr20PerfDatacomClientCurrent24StatEntry_Object = MibTableRow
pm200fr20PerfDatacomClientCurrent24StatEntry = _Pm200fr20PerfDatacomClientCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 912, 1)
)
pm200fr20PerfDatacomClientCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20PerfDatacomClientCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20PerfDatacomClientCurrent24StatEntry.setStatus("current")


class _Pm200fr20PerfDatacomClientCurrent24StatIndex_Type(Integer32):
    """Custom type pm200fr20PerfDatacomClientCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20PerfDatacomClientCurrent24StatIndex_Type.__name__ = "Integer32"
_Pm200fr20PerfDatacomClientCurrent24StatIndex_Object = MibTableColumn
pm200fr20PerfDatacomClientCurrent24StatIndex = _Pm200fr20PerfDatacomClientCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 912, 1, 1),
    _Pm200fr20PerfDatacomClientCurrent24StatIndex_Type()
)
pm200fr20PerfDatacomClientCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfDatacomClientCurrent24StatIndex.setStatus("current")
_Pm200fr20perfdatacomclientCurrent24StatInCrcCountInvPortn_Type = EkiOnOff
_Pm200fr20perfdatacomclientCurrent24StatInCrcCountInvPortn_Object = MibTableColumn
pm200fr20perfdatacomclientCurrent24StatInCrcCountInvPortn = _Pm200fr20perfdatacomclientCurrent24StatInCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 912, 1, 4),
    _Pm200fr20perfdatacomclientCurrent24StatInCrcCountInvPortn_Type()
)
pm200fr20perfdatacomclientCurrent24StatInCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20perfdatacomclientCurrent24StatInCrcCountInvPortn.setStatus("current")
_Pm200fr20perfdatacomclientCurrent24StatInCrcCountPortn_Type = Counter64
_Pm200fr20perfdatacomclientCurrent24StatInCrcCountPortn_Object = MibTableColumn
pm200fr20perfdatacomclientCurrent24StatInCrcCountPortn = _Pm200fr20perfdatacomclientCurrent24StatInCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 912, 1, 5),
    _Pm200fr20perfdatacomclientCurrent24StatInCrcCountPortn_Type()
)
pm200fr20perfdatacomclientCurrent24StatInCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20perfdatacomclientCurrent24StatInCrcCountPortn.setStatus("current")
_Pm200fr20perfdatacomclientCurrent24StatInPacketCountInvPortn_Type = EkiOnOff
_Pm200fr20perfdatacomclientCurrent24StatInPacketCountInvPortn_Object = MibTableColumn
pm200fr20perfdatacomclientCurrent24StatInPacketCountInvPortn = _Pm200fr20perfdatacomclientCurrent24StatInPacketCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 912, 1, 6),
    _Pm200fr20perfdatacomclientCurrent24StatInPacketCountInvPortn_Type()
)
pm200fr20perfdatacomclientCurrent24StatInPacketCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20perfdatacomclientCurrent24StatInPacketCountInvPortn.setStatus("current")
_Pm200fr20perfdatacomclientCurrent24StatInPacketCountPortn_Type = Counter64
_Pm200fr20perfdatacomclientCurrent24StatInPacketCountPortn_Object = MibTableColumn
pm200fr20perfdatacomclientCurrent24StatInPacketCountPortn = _Pm200fr20perfdatacomclientCurrent24StatInPacketCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 912, 1, 7),
    _Pm200fr20perfdatacomclientCurrent24StatInPacketCountPortn_Type()
)
pm200fr20perfdatacomclientCurrent24StatInPacketCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20perfdatacomclientCurrent24StatInPacketCountPortn.setStatus("current")
_Pm200fr20perfdatacomclientCurrent24StatOutCrcCountInvPortn_Type = EkiOnOff
_Pm200fr20perfdatacomclientCurrent24StatOutCrcCountInvPortn_Object = MibTableColumn
pm200fr20perfdatacomclientCurrent24StatOutCrcCountInvPortn = _Pm200fr20perfdatacomclientCurrent24StatOutCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 912, 1, 28),
    _Pm200fr20perfdatacomclientCurrent24StatOutCrcCountInvPortn_Type()
)
pm200fr20perfdatacomclientCurrent24StatOutCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20perfdatacomclientCurrent24StatOutCrcCountInvPortn.setStatus("current")
_Pm200fr20perfdatacomclientCurrent24StatOutCrcCountPortn_Type = Counter64
_Pm200fr20perfdatacomclientCurrent24StatOutCrcCountPortn_Object = MibTableColumn
pm200fr20perfdatacomclientCurrent24StatOutCrcCountPortn = _Pm200fr20perfdatacomclientCurrent24StatOutCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 912, 1, 29),
    _Pm200fr20perfdatacomclientCurrent24StatOutCrcCountPortn_Type()
)
pm200fr20perfdatacomclientCurrent24StatOutCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20perfdatacomclientCurrent24StatOutCrcCountPortn.setStatus("current")
_Pm200fr20perfdatacomclientCurrent24StatOutPacketCountInvPortn_Type = EkiOnOff
_Pm200fr20perfdatacomclientCurrent24StatOutPacketCountInvPortn_Object = MibTableColumn
pm200fr20perfdatacomclientCurrent24StatOutPacketCountInvPortn = _Pm200fr20perfdatacomclientCurrent24StatOutPacketCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 912, 1, 30),
    _Pm200fr20perfdatacomclientCurrent24StatOutPacketCountInvPortn_Type()
)
pm200fr20perfdatacomclientCurrent24StatOutPacketCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20perfdatacomclientCurrent24StatOutPacketCountInvPortn.setStatus("current")
_Pm200fr20perfdatacomclientCurrent24StatOutPacketCountPortn_Type = Counter64
_Pm200fr20perfdatacomclientCurrent24StatOutPacketCountPortn_Object = MibTableColumn
pm200fr20perfdatacomclientCurrent24StatOutPacketCountPortn = _Pm200fr20perfdatacomclientCurrent24StatOutPacketCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 912, 1, 31),
    _Pm200fr20perfdatacomclientCurrent24StatOutPacketCountPortn_Type()
)
pm200fr20perfdatacomclientCurrent24StatOutPacketCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20perfdatacomclientCurrent24StatOutPacketCountPortn.setStatus("current")
_Pm200fr20PerfDatacomClientPast24StatHistoryPort1Table_Object = MibTable
pm200fr20PerfDatacomClientPast24StatHistoryPort1Table = _Pm200fr20PerfDatacomClientPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 944)
)
if mibBuilder.loadTexts:
    pm200fr20PerfDatacomClientPast24StatHistoryPort1Table.setStatus("current")
_Pm200fr20PerfDatacomClientPast24StatHistoryPort1Entry_Object = MibTableRow
pm200fr20PerfDatacomClientPast24StatHistoryPort1Entry = _Pm200fr20PerfDatacomClientPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 944, 1)
)
pm200fr20PerfDatacomClientPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20PerfDatacomClientPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm200fr20PerfDatacomClientPast24StatHistoryPort1Entry.setStatus("current")


class _Pm200fr20PerfDatacomClientPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pm200fr20PerfDatacomClientPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20PerfDatacomClientPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm200fr20PerfDatacomClientPast24StatHistoryPort1Index_Object = MibTableColumn
pm200fr20PerfDatacomClientPast24StatHistoryPort1Index = _Pm200fr20PerfDatacomClientPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 944, 1, 1),
    _Pm200fr20PerfDatacomClientPast24StatHistoryPort1Index_Type()
)
pm200fr20PerfDatacomClientPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfDatacomClientPast24StatHistoryPort1Index.setStatus("current")
_Pm200fr20perfdatacomclientPast24StatInCrcCountInvPort1_Type = EkiOnOff
_Pm200fr20perfdatacomclientPast24StatInCrcCountInvPort1_Object = MibTableColumn
pm200fr20perfdatacomclientPast24StatInCrcCountInvPort1 = _Pm200fr20perfdatacomclientPast24StatInCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 944, 1, 4),
    _Pm200fr20perfdatacomclientPast24StatInCrcCountInvPort1_Type()
)
pm200fr20perfdatacomclientPast24StatInCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20perfdatacomclientPast24StatInCrcCountInvPort1.setStatus("current")
_Pm200fr20perfdatacomclientPast24StatInCrcCountPort1_Type = Counter64
_Pm200fr20perfdatacomclientPast24StatInCrcCountPort1_Object = MibTableColumn
pm200fr20perfdatacomclientPast24StatInCrcCountPort1 = _Pm200fr20perfdatacomclientPast24StatInCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 944, 1, 5),
    _Pm200fr20perfdatacomclientPast24StatInCrcCountPort1_Type()
)
pm200fr20perfdatacomclientPast24StatInCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20perfdatacomclientPast24StatInCrcCountPort1.setStatus("current")
_Pm200fr20perfdatacomclientPast24StatInPacketCountInvPort1_Type = EkiOnOff
_Pm200fr20perfdatacomclientPast24StatInPacketCountInvPort1_Object = MibTableColumn
pm200fr20perfdatacomclientPast24StatInPacketCountInvPort1 = _Pm200fr20perfdatacomclientPast24StatInPacketCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 944, 1, 6),
    _Pm200fr20perfdatacomclientPast24StatInPacketCountInvPort1_Type()
)
pm200fr20perfdatacomclientPast24StatInPacketCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20perfdatacomclientPast24StatInPacketCountInvPort1.setStatus("current")
_Pm200fr20perfdatacomclientPast24StatInPacketCountPort1_Type = Counter64
_Pm200fr20perfdatacomclientPast24StatInPacketCountPort1_Object = MibTableColumn
pm200fr20perfdatacomclientPast24StatInPacketCountPort1 = _Pm200fr20perfdatacomclientPast24StatInPacketCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 944, 1, 7),
    _Pm200fr20perfdatacomclientPast24StatInPacketCountPort1_Type()
)
pm200fr20perfdatacomclientPast24StatInPacketCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20perfdatacomclientPast24StatInPacketCountPort1.setStatus("current")
_Pm200fr20perfdatacomclientPast24StatOutCrcCountInvPort1_Type = EkiOnOff
_Pm200fr20perfdatacomclientPast24StatOutCrcCountInvPort1_Object = MibTableColumn
pm200fr20perfdatacomclientPast24StatOutCrcCountInvPort1 = _Pm200fr20perfdatacomclientPast24StatOutCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 944, 1, 28),
    _Pm200fr20perfdatacomclientPast24StatOutCrcCountInvPort1_Type()
)
pm200fr20perfdatacomclientPast24StatOutCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20perfdatacomclientPast24StatOutCrcCountInvPort1.setStatus("current")
_Pm200fr20perfdatacomclientPast24StatOutCrcCountPort1_Type = Counter64
_Pm200fr20perfdatacomclientPast24StatOutCrcCountPort1_Object = MibTableColumn
pm200fr20perfdatacomclientPast24StatOutCrcCountPort1 = _Pm200fr20perfdatacomclientPast24StatOutCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 944, 1, 29),
    _Pm200fr20perfdatacomclientPast24StatOutCrcCountPort1_Type()
)
pm200fr20perfdatacomclientPast24StatOutCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20perfdatacomclientPast24StatOutCrcCountPort1.setStatus("current")
_Pm200fr20perfdatacomclientPast24StatOutPacketCountInvPort1_Type = EkiOnOff
_Pm200fr20perfdatacomclientPast24StatOutPacketCountInvPort1_Object = MibTableColumn
pm200fr20perfdatacomclientPast24StatOutPacketCountInvPort1 = _Pm200fr20perfdatacomclientPast24StatOutPacketCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 944, 1, 30),
    _Pm200fr20perfdatacomclientPast24StatOutPacketCountInvPort1_Type()
)
pm200fr20perfdatacomclientPast24StatOutPacketCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20perfdatacomclientPast24StatOutPacketCountInvPort1.setStatus("current")
_Pm200fr20perfdatacomclientPast24StatOutPacketCountPort1_Type = Counter64
_Pm200fr20perfdatacomclientPast24StatOutPacketCountPort1_Object = MibTableColumn
pm200fr20perfdatacomclientPast24StatOutPacketCountPort1 = _Pm200fr20perfdatacomclientPast24StatOutPacketCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 6, 944, 1, 31),
    _Pm200fr20perfdatacomclientPast24StatOutPacketCountPort1_Type()
)
pm200fr20perfdatacomclientPast24StatOutPacketCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20perfdatacomclientPast24StatOutPacketCountPort1.setStatus("current")
_Pm200fr20MonPerfLine_ObjectIdentity = ObjectIdentity
pm200fr20MonPerfLine = _Pm200fr20MonPerfLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7)
)
_Pm200fr20PerfTelecomLinePostFecCurrent15StatTable_Object = MibTable
pm200fr20PerfTelecomLinePostFecCurrent15StatTable = _Pm200fr20PerfTelecomLinePostFecCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 336)
)
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecCurrent15StatTable.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecCurrent15StatEntry_Object = MibTableRow
pm200fr20PerfTelecomLinePostFecCurrent15StatEntry = _Pm200fr20PerfTelecomLinePostFecCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 336, 1)
)
pm200fr20PerfTelecomLinePostFecCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20PerfTelecomLinePostFecCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecCurrent15StatEntry.setStatus("current")


class _Pm200fr20PerfTelecomLinePostFecCurrent15StatIndex_Type(Integer32):
    """Custom type pm200fr20PerfTelecomLinePostFecCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20PerfTelecomLinePostFecCurrent15StatIndex_Type.__name__ = "Integer32"
_Pm200fr20PerfTelecomLinePostFecCurrent15StatIndex_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecCurrent15StatIndex = _Pm200fr20PerfTelecomLinePostFecCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 336, 1, 1),
    _Pm200fr20PerfTelecomLinePostFecCurrent15StatIndex_Type()
)
pm200fr20PerfTelecomLinePostFecCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecCurrent15StatIndex.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecCurrent15StatInvCvPortn_Type = EkiOnOff
_Pm200fr20PerfTelecomLinePostFecCurrent15StatInvCvPortn_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecCurrent15StatInvCvPortn = _Pm200fr20PerfTelecomLinePostFecCurrent15StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 336, 1, 2),
    _Pm200fr20PerfTelecomLinePostFecCurrent15StatInvCvPortn_Type()
)
pm200fr20PerfTelecomLinePostFecCurrent15StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecCurrent15StatInvCvPortn.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecCurrent15StatCvValuePortn_Type = Unsigned32
_Pm200fr20PerfTelecomLinePostFecCurrent15StatCvValuePortn_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecCurrent15StatCvValuePortn = _Pm200fr20PerfTelecomLinePostFecCurrent15StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 336, 1, 3),
    _Pm200fr20PerfTelecomLinePostFecCurrent15StatCvValuePortn_Type()
)
pm200fr20PerfTelecomLinePostFecCurrent15StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecCurrent15StatCvValuePortn.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecCurrent15StatInvEsPortn_Type = EkiOnOff
_Pm200fr20PerfTelecomLinePostFecCurrent15StatInvEsPortn_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecCurrent15StatInvEsPortn = _Pm200fr20PerfTelecomLinePostFecCurrent15StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 336, 1, 4),
    _Pm200fr20PerfTelecomLinePostFecCurrent15StatInvEsPortn_Type()
)
pm200fr20PerfTelecomLinePostFecCurrent15StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecCurrent15StatInvEsPortn.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecCurrent15StatEsValuePortn_Type = Unsigned32
_Pm200fr20PerfTelecomLinePostFecCurrent15StatEsValuePortn_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecCurrent15StatEsValuePortn = _Pm200fr20PerfTelecomLinePostFecCurrent15StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 336, 1, 5),
    _Pm200fr20PerfTelecomLinePostFecCurrent15StatEsValuePortn_Type()
)
pm200fr20PerfTelecomLinePostFecCurrent15StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecCurrent15StatEsValuePortn.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecCurrent15StatInvSesPortn_Type = EkiOnOff
_Pm200fr20PerfTelecomLinePostFecCurrent15StatInvSesPortn_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecCurrent15StatInvSesPortn = _Pm200fr20PerfTelecomLinePostFecCurrent15StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 336, 1, 6),
    _Pm200fr20PerfTelecomLinePostFecCurrent15StatInvSesPortn_Type()
)
pm200fr20PerfTelecomLinePostFecCurrent15StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecCurrent15StatInvSesPortn.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecCurrent15StatSesValuePortn_Type = Unsigned32
_Pm200fr20PerfTelecomLinePostFecCurrent15StatSesValuePortn_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecCurrent15StatSesValuePortn = _Pm200fr20PerfTelecomLinePostFecCurrent15StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 336, 1, 7),
    _Pm200fr20PerfTelecomLinePostFecCurrent15StatSesValuePortn_Type()
)
pm200fr20PerfTelecomLinePostFecCurrent15StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecCurrent15StatSesValuePortn.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecCurrent15StatInvSefsPortn_Type = EkiOnOff
_Pm200fr20PerfTelecomLinePostFecCurrent15StatInvSefsPortn_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecCurrent15StatInvSefsPortn = _Pm200fr20PerfTelecomLinePostFecCurrent15StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 336, 1, 8),
    _Pm200fr20PerfTelecomLinePostFecCurrent15StatInvSefsPortn_Type()
)
pm200fr20PerfTelecomLinePostFecCurrent15StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecCurrent15StatInvSefsPortn.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecCurrent15StatSefsValuePortn_Type = Unsigned32
_Pm200fr20PerfTelecomLinePostFecCurrent15StatSefsValuePortn_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecCurrent15StatSefsValuePortn = _Pm200fr20PerfTelecomLinePostFecCurrent15StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 336, 1, 9),
    _Pm200fr20PerfTelecomLinePostFecCurrent15StatSefsValuePortn_Type()
)
pm200fr20PerfTelecomLinePostFecCurrent15StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecCurrent15StatSefsValuePortn.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecCurrent15StatInvUasPortn_Type = EkiOnOff
_Pm200fr20PerfTelecomLinePostFecCurrent15StatInvUasPortn_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecCurrent15StatInvUasPortn = _Pm200fr20PerfTelecomLinePostFecCurrent15StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 336, 1, 10),
    _Pm200fr20PerfTelecomLinePostFecCurrent15StatInvUasPortn_Type()
)
pm200fr20PerfTelecomLinePostFecCurrent15StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecCurrent15StatInvUasPortn.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecCurrent15StatUasValuePortn_Type = Unsigned32
_Pm200fr20PerfTelecomLinePostFecCurrent15StatUasValuePortn_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecCurrent15StatUasValuePortn = _Pm200fr20PerfTelecomLinePostFecCurrent15StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 336, 1, 11),
    _Pm200fr20PerfTelecomLinePostFecCurrent15StatUasValuePortn_Type()
)
pm200fr20PerfTelecomLinePostFecCurrent15StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecCurrent15StatUasValuePortn.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecPast15StatHistoryPort1Table_Object = MibTable
pm200fr20PerfTelecomLinePostFecPast15StatHistoryPort1Table = _Pm200fr20PerfTelecomLinePostFecPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 337)
)
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecPast15StatHistoryPort1Table.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecPast15StatHistoryPort1Entry_Object = MibTableRow
pm200fr20PerfTelecomLinePostFecPast15StatHistoryPort1Entry = _Pm200fr20PerfTelecomLinePostFecPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 337, 1)
)
pm200fr20PerfTelecomLinePostFecPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20PerfTelecomLinePostFecPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecPast15StatHistoryPort1Entry.setStatus("current")


class _Pm200fr20PerfTelecomLinePostFecPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pm200fr20PerfTelecomLinePostFecPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20PerfTelecomLinePostFecPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm200fr20PerfTelecomLinePostFecPast15StatHistoryPort1Index_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecPast15StatHistoryPort1Index = _Pm200fr20PerfTelecomLinePostFecPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 337, 1, 1),
    _Pm200fr20PerfTelecomLinePostFecPast15StatHistoryPort1Index_Type()
)
pm200fr20PerfTelecomLinePostFecPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecPast15StatHistoryPort1Index.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvCvPort1_Type = EkiOnOff
_Pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvCvPort1_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvCvPort1 = _Pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 337, 1, 2),
    _Pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvCvPort1_Type()
)
pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvCvPort1.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecPast15StatHistoryCvValuePort1_Type = Unsigned32
_Pm200fr20PerfTelecomLinePostFecPast15StatHistoryCvValuePort1_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecPast15StatHistoryCvValuePort1 = _Pm200fr20PerfTelecomLinePostFecPast15StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 337, 1, 3),
    _Pm200fr20PerfTelecomLinePostFecPast15StatHistoryCvValuePort1_Type()
)
pm200fr20PerfTelecomLinePostFecPast15StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecPast15StatHistoryCvValuePort1.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvEsPort1_Type = EkiOnOff
_Pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvEsPort1_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvEsPort1 = _Pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 337, 1, 4),
    _Pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvEsPort1_Type()
)
pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvEsPort1.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecPast15StatHistoryEsValuePort1_Type = Unsigned32
_Pm200fr20PerfTelecomLinePostFecPast15StatHistoryEsValuePort1_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecPast15StatHistoryEsValuePort1 = _Pm200fr20PerfTelecomLinePostFecPast15StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 337, 1, 5),
    _Pm200fr20PerfTelecomLinePostFecPast15StatHistoryEsValuePort1_Type()
)
pm200fr20PerfTelecomLinePostFecPast15StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecPast15StatHistoryEsValuePort1.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvSesPort1_Type = EkiOnOff
_Pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvSesPort1_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvSesPort1 = _Pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 337, 1, 6),
    _Pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvSesPort1_Type()
)
pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvSesPort1.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecPast15StatHistorySesValuePort1_Type = Unsigned32
_Pm200fr20PerfTelecomLinePostFecPast15StatHistorySesValuePort1_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecPast15StatHistorySesValuePort1 = _Pm200fr20PerfTelecomLinePostFecPast15StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 337, 1, 7),
    _Pm200fr20PerfTelecomLinePostFecPast15StatHistorySesValuePort1_Type()
)
pm200fr20PerfTelecomLinePostFecPast15StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecPast15StatHistorySesValuePort1.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvSefsPort1_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvSefsPort1 = _Pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 337, 1, 8),
    _Pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvSefsPort1_Type()
)
pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvSefsPort1.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecPast15StatHistorySefsValuePort1_Type = Unsigned32
_Pm200fr20PerfTelecomLinePostFecPast15StatHistorySefsValuePort1_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecPast15StatHistorySefsValuePort1 = _Pm200fr20PerfTelecomLinePostFecPast15StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 337, 1, 9),
    _Pm200fr20PerfTelecomLinePostFecPast15StatHistorySefsValuePort1_Type()
)
pm200fr20PerfTelecomLinePostFecPast15StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecPast15StatHistorySefsValuePort1.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvUasPort1_Type = EkiOnOff
_Pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvUasPort1_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvUasPort1 = _Pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 337, 1, 10),
    _Pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvUasPort1_Type()
)
pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvUasPort1.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecPast15StatHistoryUasValuePort1_Type = Unsigned32
_Pm200fr20PerfTelecomLinePostFecPast15StatHistoryUasValuePort1_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecPast15StatHistoryUasValuePort1 = _Pm200fr20PerfTelecomLinePostFecPast15StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 337, 1, 11),
    _Pm200fr20PerfTelecomLinePostFecPast15StatHistoryUasValuePort1_Type()
)
pm200fr20PerfTelecomLinePostFecPast15StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecPast15StatHistoryUasValuePort1.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecCurrent24StatTable_Object = MibTable
pm200fr20PerfTelecomLinePostFecCurrent24StatTable = _Pm200fr20PerfTelecomLinePostFecCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 338)
)
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecCurrent24StatTable.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecCurrent24StatEntry_Object = MibTableRow
pm200fr20PerfTelecomLinePostFecCurrent24StatEntry = _Pm200fr20PerfTelecomLinePostFecCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 338, 1)
)
pm200fr20PerfTelecomLinePostFecCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20PerfTelecomLinePostFecCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecCurrent24StatEntry.setStatus("current")


class _Pm200fr20PerfTelecomLinePostFecCurrent24StatIndex_Type(Integer32):
    """Custom type pm200fr20PerfTelecomLinePostFecCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20PerfTelecomLinePostFecCurrent24StatIndex_Type.__name__ = "Integer32"
_Pm200fr20PerfTelecomLinePostFecCurrent24StatIndex_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecCurrent24StatIndex = _Pm200fr20PerfTelecomLinePostFecCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 338, 1, 1),
    _Pm200fr20PerfTelecomLinePostFecCurrent24StatIndex_Type()
)
pm200fr20PerfTelecomLinePostFecCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecCurrent24StatIndex.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecCurrent24StatInvCvPortn_Type = EkiOnOff
_Pm200fr20PerfTelecomLinePostFecCurrent24StatInvCvPortn_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecCurrent24StatInvCvPortn = _Pm200fr20PerfTelecomLinePostFecCurrent24StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 338, 1, 2),
    _Pm200fr20PerfTelecomLinePostFecCurrent24StatInvCvPortn_Type()
)
pm200fr20PerfTelecomLinePostFecCurrent24StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecCurrent24StatInvCvPortn.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecCurrent24StatCvValuePortn_Type = Unsigned32
_Pm200fr20PerfTelecomLinePostFecCurrent24StatCvValuePortn_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecCurrent24StatCvValuePortn = _Pm200fr20PerfTelecomLinePostFecCurrent24StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 338, 1, 3),
    _Pm200fr20PerfTelecomLinePostFecCurrent24StatCvValuePortn_Type()
)
pm200fr20PerfTelecomLinePostFecCurrent24StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecCurrent24StatCvValuePortn.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecCurrent24StatInvEsPortn_Type = EkiOnOff
_Pm200fr20PerfTelecomLinePostFecCurrent24StatInvEsPortn_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecCurrent24StatInvEsPortn = _Pm200fr20PerfTelecomLinePostFecCurrent24StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 338, 1, 4),
    _Pm200fr20PerfTelecomLinePostFecCurrent24StatInvEsPortn_Type()
)
pm200fr20PerfTelecomLinePostFecCurrent24StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecCurrent24StatInvEsPortn.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecCurrent24StatEsValuePortn_Type = Unsigned32
_Pm200fr20PerfTelecomLinePostFecCurrent24StatEsValuePortn_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecCurrent24StatEsValuePortn = _Pm200fr20PerfTelecomLinePostFecCurrent24StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 338, 1, 5),
    _Pm200fr20PerfTelecomLinePostFecCurrent24StatEsValuePortn_Type()
)
pm200fr20PerfTelecomLinePostFecCurrent24StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecCurrent24StatEsValuePortn.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecCurrent24StatInvSesPortn_Type = EkiOnOff
_Pm200fr20PerfTelecomLinePostFecCurrent24StatInvSesPortn_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecCurrent24StatInvSesPortn = _Pm200fr20PerfTelecomLinePostFecCurrent24StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 338, 1, 6),
    _Pm200fr20PerfTelecomLinePostFecCurrent24StatInvSesPortn_Type()
)
pm200fr20PerfTelecomLinePostFecCurrent24StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecCurrent24StatInvSesPortn.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecCurrent24StatSesValuePortn_Type = Unsigned32
_Pm200fr20PerfTelecomLinePostFecCurrent24StatSesValuePortn_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecCurrent24StatSesValuePortn = _Pm200fr20PerfTelecomLinePostFecCurrent24StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 338, 1, 7),
    _Pm200fr20PerfTelecomLinePostFecCurrent24StatSesValuePortn_Type()
)
pm200fr20PerfTelecomLinePostFecCurrent24StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecCurrent24StatSesValuePortn.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecCurrent24StatInvSefsPortn_Type = EkiOnOff
_Pm200fr20PerfTelecomLinePostFecCurrent24StatInvSefsPortn_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecCurrent24StatInvSefsPortn = _Pm200fr20PerfTelecomLinePostFecCurrent24StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 338, 1, 8),
    _Pm200fr20PerfTelecomLinePostFecCurrent24StatInvSefsPortn_Type()
)
pm200fr20PerfTelecomLinePostFecCurrent24StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecCurrent24StatInvSefsPortn.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecCurrent24StatSefsValuePortn_Type = Unsigned32
_Pm200fr20PerfTelecomLinePostFecCurrent24StatSefsValuePortn_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecCurrent24StatSefsValuePortn = _Pm200fr20PerfTelecomLinePostFecCurrent24StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 338, 1, 9),
    _Pm200fr20PerfTelecomLinePostFecCurrent24StatSefsValuePortn_Type()
)
pm200fr20PerfTelecomLinePostFecCurrent24StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecCurrent24StatSefsValuePortn.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecCurrent24StatInvUasPortn_Type = EkiOnOff
_Pm200fr20PerfTelecomLinePostFecCurrent24StatInvUasPortn_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecCurrent24StatInvUasPortn = _Pm200fr20PerfTelecomLinePostFecCurrent24StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 338, 1, 10),
    _Pm200fr20PerfTelecomLinePostFecCurrent24StatInvUasPortn_Type()
)
pm200fr20PerfTelecomLinePostFecCurrent24StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecCurrent24StatInvUasPortn.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecCurrent24StatUasValuePortn_Type = Unsigned32
_Pm200fr20PerfTelecomLinePostFecCurrent24StatUasValuePortn_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecCurrent24StatUasValuePortn = _Pm200fr20PerfTelecomLinePostFecCurrent24StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 338, 1, 11),
    _Pm200fr20PerfTelecomLinePostFecCurrent24StatUasValuePortn_Type()
)
pm200fr20PerfTelecomLinePostFecCurrent24StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecCurrent24StatUasValuePortn.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecPast24StatHistoryPort1Table_Object = MibTable
pm200fr20PerfTelecomLinePostFecPast24StatHistoryPort1Table = _Pm200fr20PerfTelecomLinePostFecPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 339)
)
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecPast24StatHistoryPort1Table.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecPast24StatHistoryPort1Entry_Object = MibTableRow
pm200fr20PerfTelecomLinePostFecPast24StatHistoryPort1Entry = _Pm200fr20PerfTelecomLinePostFecPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 339, 1)
)
pm200fr20PerfTelecomLinePostFecPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20PerfTelecomLinePostFecPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecPast24StatHistoryPort1Entry.setStatus("current")


class _Pm200fr20PerfTelecomLinePostFecPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pm200fr20PerfTelecomLinePostFecPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20PerfTelecomLinePostFecPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm200fr20PerfTelecomLinePostFecPast24StatHistoryPort1Index_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecPast24StatHistoryPort1Index = _Pm200fr20PerfTelecomLinePostFecPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 339, 1, 1),
    _Pm200fr20PerfTelecomLinePostFecPast24StatHistoryPort1Index_Type()
)
pm200fr20PerfTelecomLinePostFecPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecPast24StatHistoryPort1Index.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvCvPort1_Type = EkiOnOff
_Pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvCvPort1_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvCvPort1 = _Pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 339, 1, 2),
    _Pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvCvPort1_Type()
)
pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvCvPort1.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecPast24StatHistoryCvValuePort1_Type = Unsigned32
_Pm200fr20PerfTelecomLinePostFecPast24StatHistoryCvValuePort1_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecPast24StatHistoryCvValuePort1 = _Pm200fr20PerfTelecomLinePostFecPast24StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 339, 1, 3),
    _Pm200fr20PerfTelecomLinePostFecPast24StatHistoryCvValuePort1_Type()
)
pm200fr20PerfTelecomLinePostFecPast24StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecPast24StatHistoryCvValuePort1.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvEsPort1_Type = EkiOnOff
_Pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvEsPort1_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvEsPort1 = _Pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 339, 1, 4),
    _Pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvEsPort1_Type()
)
pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvEsPort1.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecPast24StatHistoryEsValuePort1_Type = Unsigned32
_Pm200fr20PerfTelecomLinePostFecPast24StatHistoryEsValuePort1_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecPast24StatHistoryEsValuePort1 = _Pm200fr20PerfTelecomLinePostFecPast24StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 339, 1, 5),
    _Pm200fr20PerfTelecomLinePostFecPast24StatHistoryEsValuePort1_Type()
)
pm200fr20PerfTelecomLinePostFecPast24StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecPast24StatHistoryEsValuePort1.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvSesPort1_Type = EkiOnOff
_Pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvSesPort1_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvSesPort1 = _Pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 339, 1, 6),
    _Pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvSesPort1_Type()
)
pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvSesPort1.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecPast24StatHistorySesValuePort1_Type = Unsigned32
_Pm200fr20PerfTelecomLinePostFecPast24StatHistorySesValuePort1_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecPast24StatHistorySesValuePort1 = _Pm200fr20PerfTelecomLinePostFecPast24StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 339, 1, 7),
    _Pm200fr20PerfTelecomLinePostFecPast24StatHistorySesValuePort1_Type()
)
pm200fr20PerfTelecomLinePostFecPast24StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecPast24StatHistorySesValuePort1.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvSefsPort1_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvSefsPort1 = _Pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 339, 1, 8),
    _Pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvSefsPort1_Type()
)
pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvSefsPort1.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecPast24StatHistorySefsValuePort1_Type = Unsigned32
_Pm200fr20PerfTelecomLinePostFecPast24StatHistorySefsValuePort1_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecPast24StatHistorySefsValuePort1 = _Pm200fr20PerfTelecomLinePostFecPast24StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 339, 1, 9),
    _Pm200fr20PerfTelecomLinePostFecPast24StatHistorySefsValuePort1_Type()
)
pm200fr20PerfTelecomLinePostFecPast24StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecPast24StatHistorySefsValuePort1.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvUasPort1_Type = EkiOnOff
_Pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvUasPort1_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvUasPort1 = _Pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 339, 1, 10),
    _Pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvUasPort1_Type()
)
pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvUasPort1.setStatus("current")
_Pm200fr20PerfTelecomLinePostFecPast24StatHistoryUasValuePort1_Type = Unsigned32
_Pm200fr20PerfTelecomLinePostFecPast24StatHistoryUasValuePort1_Object = MibTableColumn
pm200fr20PerfTelecomLinePostFecPast24StatHistoryUasValuePort1 = _Pm200fr20PerfTelecomLinePostFecPast24StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 339, 1, 11),
    _Pm200fr20PerfTelecomLinePostFecPast24StatHistoryUasValuePort1_Type()
)
pm200fr20PerfTelecomLinePostFecPast24StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomLinePostFecPast24StatHistoryUasValuePort1.setStatus("current")
_Pm200fr20PerfTelecomBerLinePreFecCurrent15StatTable_Object = MibTable
pm200fr20PerfTelecomBerLinePreFecCurrent15StatTable = _Pm200fr20PerfTelecomBerLinePreFecCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 352)
)
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomBerLinePreFecCurrent15StatTable.setStatus("current")
_Pm200fr20PerfTelecomBerLinePreFecCurrent15StatEntry_Object = MibTableRow
pm200fr20PerfTelecomBerLinePreFecCurrent15StatEntry = _Pm200fr20PerfTelecomBerLinePreFecCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 352, 1)
)
pm200fr20PerfTelecomBerLinePreFecCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20PerfTelecomBerLinePreFecCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomBerLinePreFecCurrent15StatEntry.setStatus("current")


class _Pm200fr20PerfTelecomBerLinePreFecCurrent15StatIndex_Type(Integer32):
    """Custom type pm200fr20PerfTelecomBerLinePreFecCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20PerfTelecomBerLinePreFecCurrent15StatIndex_Type.__name__ = "Integer32"
_Pm200fr20PerfTelecomBerLinePreFecCurrent15StatIndex_Object = MibTableColumn
pm200fr20PerfTelecomBerLinePreFecCurrent15StatIndex = _Pm200fr20PerfTelecomBerLinePreFecCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 352, 1, 1),
    _Pm200fr20PerfTelecomBerLinePreFecCurrent15StatIndex_Type()
)
pm200fr20PerfTelecomBerLinePreFecCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomBerLinePreFecCurrent15StatIndex.setStatus("current")
_Pm200fr20PerfTelecomBerLinePreFecCurrent15StatInvBerPortn_Type = EkiOnOff
_Pm200fr20PerfTelecomBerLinePreFecCurrent15StatInvBerPortn_Object = MibTableColumn
pm200fr20PerfTelecomBerLinePreFecCurrent15StatInvBerPortn = _Pm200fr20PerfTelecomBerLinePreFecCurrent15StatInvBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 352, 1, 2),
    _Pm200fr20PerfTelecomBerLinePreFecCurrent15StatInvBerPortn_Type()
)
pm200fr20PerfTelecomBerLinePreFecCurrent15StatInvBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomBerLinePreFecCurrent15StatInvBerPortn.setStatus("current")
_Pm200fr20PerfTelecomBerLinePreFecCurrent15StatBerValuePortn_Type = Unsigned32
_Pm200fr20PerfTelecomBerLinePreFecCurrent15StatBerValuePortn_Object = MibTableColumn
pm200fr20PerfTelecomBerLinePreFecCurrent15StatBerValuePortn = _Pm200fr20PerfTelecomBerLinePreFecCurrent15StatBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 352, 1, 3),
    _Pm200fr20PerfTelecomBerLinePreFecCurrent15StatBerValuePortn_Type()
)
pm200fr20PerfTelecomBerLinePreFecCurrent15StatBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomBerLinePreFecCurrent15StatBerValuePortn.setStatus("current")
_Pm200fr20PerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn_Type = EkiOnOff
_Pm200fr20PerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn_Object = MibTableColumn
pm200fr20PerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn = _Pm200fr20PerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 352, 1, 4),
    _Pm200fr20PerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn_Type()
)
pm200fr20PerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn.setStatus("current")
_Pm200fr20PerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn_Type = Unsigned32
_Pm200fr20PerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn_Object = MibTableColumn
pm200fr20PerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn = _Pm200fr20PerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 352, 1, 5),
    _Pm200fr20PerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn_Type()
)
pm200fr20PerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn.setStatus("current")
_Pm200fr20PerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn_Type = EkiOnOff
_Pm200fr20PerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn_Object = MibTableColumn
pm200fr20PerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn = _Pm200fr20PerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 352, 1, 6),
    _Pm200fr20PerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn_Type()
)
pm200fr20PerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn.setStatus("current")
_Pm200fr20PerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn_Type = Unsigned32
_Pm200fr20PerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn_Object = MibTableColumn
pm200fr20PerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn = _Pm200fr20PerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 352, 1, 7),
    _Pm200fr20PerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn_Type()
)
pm200fr20PerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn.setStatus("current")
_Pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryPort1Table_Object = MibTable
pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryPort1Table = _Pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 353)
)
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryPort1Table.setStatus("current")
_Pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryPort1Entry_Object = MibTableRow
pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryPort1Entry = _Pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 353, 1)
)
pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryPort1Entry.setStatus("current")


class _Pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Object = MibTableColumn
pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryPort1Index = _Pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 353, 1, 1),
    _Pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Type()
)
pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryPort1Index.setStatus("current")
_Pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1_Type = EkiOnOff
_Pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1_Object = MibTableColumn
pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1 = _Pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 353, 1, 2),
    _Pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1_Type()
)
pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1.setStatus("current")
_Pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1_Type = Unsigned32
_Pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1_Object = MibTableColumn
pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1 = _Pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 353, 1, 3),
    _Pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1_Type()
)
pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1.setStatus("current")
_Pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1_Type = EkiOnOff
_Pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1_Object = MibTableColumn
pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1 = _Pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 353, 1, 4),
    _Pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1_Type()
)
pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1.setStatus("current")
_Pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1_Type = Unsigned32
_Pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1_Object = MibTableColumn
pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1 = _Pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 353, 1, 5),
    _Pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1_Type()
)
pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1.setStatus("current")
_Pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1_Type = EkiOnOff
_Pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1_Object = MibTableColumn
pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1 = _Pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 353, 1, 6),
    _Pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1_Type()
)
pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1.setStatus("current")
_Pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1_Type = Unsigned32
_Pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1_Object = MibTableColumn
pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1 = _Pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 353, 1, 7),
    _Pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1_Type()
)
pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1.setStatus("current")
_Pm200fr20PerfTelecomBerLinePreFecCurrent24StatTable_Object = MibTable
pm200fr20PerfTelecomBerLinePreFecCurrent24StatTable = _Pm200fr20PerfTelecomBerLinePreFecCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 354)
)
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomBerLinePreFecCurrent24StatTable.setStatus("current")
_Pm200fr20PerfTelecomBerLinePreFecCurrent24StatEntry_Object = MibTableRow
pm200fr20PerfTelecomBerLinePreFecCurrent24StatEntry = _Pm200fr20PerfTelecomBerLinePreFecCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 354, 1)
)
pm200fr20PerfTelecomBerLinePreFecCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20PerfTelecomBerLinePreFecCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomBerLinePreFecCurrent24StatEntry.setStatus("current")


class _Pm200fr20PerfTelecomBerLinePreFecCurrent24StatIndex_Type(Integer32):
    """Custom type pm200fr20PerfTelecomBerLinePreFecCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20PerfTelecomBerLinePreFecCurrent24StatIndex_Type.__name__ = "Integer32"
_Pm200fr20PerfTelecomBerLinePreFecCurrent24StatIndex_Object = MibTableColumn
pm200fr20PerfTelecomBerLinePreFecCurrent24StatIndex = _Pm200fr20PerfTelecomBerLinePreFecCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 354, 1, 1),
    _Pm200fr20PerfTelecomBerLinePreFecCurrent24StatIndex_Type()
)
pm200fr20PerfTelecomBerLinePreFecCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomBerLinePreFecCurrent24StatIndex.setStatus("current")
_Pm200fr20PerfTelecomBerLinePreFecCurrent24StatInvBerPortn_Type = EkiOnOff
_Pm200fr20PerfTelecomBerLinePreFecCurrent24StatInvBerPortn_Object = MibTableColumn
pm200fr20PerfTelecomBerLinePreFecCurrent24StatInvBerPortn = _Pm200fr20PerfTelecomBerLinePreFecCurrent24StatInvBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 354, 1, 2),
    _Pm200fr20PerfTelecomBerLinePreFecCurrent24StatInvBerPortn_Type()
)
pm200fr20PerfTelecomBerLinePreFecCurrent24StatInvBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomBerLinePreFecCurrent24StatInvBerPortn.setStatus("current")
_Pm200fr20PerfTelecomBerLinePreFecCurrent24StatBerValuePortn_Type = Unsigned32
_Pm200fr20PerfTelecomBerLinePreFecCurrent24StatBerValuePortn_Object = MibTableColumn
pm200fr20PerfTelecomBerLinePreFecCurrent24StatBerValuePortn = _Pm200fr20PerfTelecomBerLinePreFecCurrent24StatBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 354, 1, 3),
    _Pm200fr20PerfTelecomBerLinePreFecCurrent24StatBerValuePortn_Type()
)
pm200fr20PerfTelecomBerLinePreFecCurrent24StatBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomBerLinePreFecCurrent24StatBerValuePortn.setStatus("current")
_Pm200fr20PerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn_Type = EkiOnOff
_Pm200fr20PerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn_Object = MibTableColumn
pm200fr20PerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn = _Pm200fr20PerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 354, 1, 4),
    _Pm200fr20PerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn_Type()
)
pm200fr20PerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn.setStatus("current")
_Pm200fr20PerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn_Type = Unsigned32
_Pm200fr20PerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn_Object = MibTableColumn
pm200fr20PerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn = _Pm200fr20PerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 354, 1, 5),
    _Pm200fr20PerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn_Type()
)
pm200fr20PerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn.setStatus("current")
_Pm200fr20PerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn_Type = EkiOnOff
_Pm200fr20PerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn_Object = MibTableColumn
pm200fr20PerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn = _Pm200fr20PerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 354, 1, 6),
    _Pm200fr20PerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn_Type()
)
pm200fr20PerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn.setStatus("current")
_Pm200fr20PerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn_Type = Unsigned32
_Pm200fr20PerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn_Object = MibTableColumn
pm200fr20PerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn = _Pm200fr20PerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 354, 1, 7),
    _Pm200fr20PerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn_Type()
)
pm200fr20PerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn.setStatus("current")
_Pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryPort1Table_Object = MibTable
pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryPort1Table = _Pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 355)
)
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryPort1Table.setStatus("current")
_Pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryPort1Entry_Object = MibTableRow
pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryPort1Entry = _Pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 355, 1)
)
pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm200fr20-MIB", "pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryPort1Entry.setStatus("current")


class _Pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Object = MibTableColumn
pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryPort1Index = _Pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 355, 1, 1),
    _Pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Type()
)
pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryPort1Index.setStatus("current")
_Pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1_Type = EkiOnOff
_Pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1_Object = MibTableColumn
pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1 = _Pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 355, 1, 2),
    _Pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1_Type()
)
pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1.setStatus("current")
_Pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1_Type = Unsigned32
_Pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1_Object = MibTableColumn
pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1 = _Pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 355, 1, 3),
    _Pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1_Type()
)
pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1.setStatus("current")
_Pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1_Type = EkiOnOff
_Pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1_Object = MibTableColumn
pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1 = _Pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 355, 1, 4),
    _Pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1_Type()
)
pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1.setStatus("current")
_Pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1_Type = Unsigned32
_Pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1_Object = MibTableColumn
pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1 = _Pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 355, 1, 5),
    _Pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1_Type()
)
pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1.setStatus("current")
_Pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1_Type = EkiOnOff
_Pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1_Object = MibTableColumn
pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1 = _Pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 355, 1, 6),
    _Pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1_Type()
)
pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1.setStatus("current")
_Pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1_Type = Unsigned32
_Pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1_Object = MibTableColumn
pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1 = _Pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 87, 11, 7, 355, 1, 7),
    _Pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1_Type()
)
pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1.setStatus("current")

# Managed Objects groups


# Notification objects

pm200fr20LineTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 87, 10, 30)
)
pm200fr20LineTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm200fr20-MIB", "pm200fr20AlmLineDdmWarningPortn"),
        ("EKINOPS-Pm200fr20-MIB", "pm200fr20trapLineNumber"),
        ("EKINOPS-Pm200fr20-MIB", "pm200fr20trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm200fr20LineTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm200fr20LineTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 87, 10, 31)
)
pm200fr20LineTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm200fr20-MIB", "pm200fr20AlmLineDdmWarningPortn"),
        ("EKINOPS-Pm200fr20-MIB", "pm200fr20trapLineNumber"),
        ("EKINOPS-Pm200fr20-MIB", "pm200fr20trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm200fr20LineTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm200fr20LineTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 87, 10, 32)
)
pm200fr20LineTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm200fr20-MIB", "pm200fr20AlmLineDdmAlmPortn"),
        ("EKINOPS-Pm200fr20-MIB", "pm200fr20trapLineNumber"),
        ("EKINOPS-Pm200fr20-MIB", "pm200fr20trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm200fr20LineTrapUrgentGoesOn.setStatus(
        "current"
    )

pm200fr20LineTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 87, 10, 33)
)
pm200fr20LineTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm200fr20-MIB", "pm200fr20AlmLineDdmAlmPortn"),
        ("EKINOPS-Pm200fr20-MIB", "pm200fr20trapLineNumber"),
        ("EKINOPS-Pm200fr20-MIB", "pm200fr20trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm200fr20LineTrapUrgentGoesOff.setStatus(
        "current"
    )

pm200fr20LineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 87, 10, 34)
)
pm200fr20LineTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm200fr20-MIB", "pm200fr20AlmLineFailPortn"),
        ("EKINOPS-Pm200fr20-MIB", "pm200fr20AlmLineHwFailPortn"),
        ("EKINOPS-Pm200fr20-MIB", "pm200fr20trapLineNumber"),
        ("EKINOPS-Pm200fr20-MIB", "pm200fr20trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm200fr20LineTrapCritGoesOn.setStatus(
        "current"
    )

pm200fr20LineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 87, 10, 35)
)
pm200fr20LineTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm200fr20-MIB", "pm200fr20AlmLineFailPortn"),
        ("EKINOPS-Pm200fr20-MIB", "pm200fr20AlmLineHwFailPortn"),
        ("EKINOPS-Pm200fr20-MIB", "pm200fr20trapLineNumber"),
        ("EKINOPS-Pm200fr20-MIB", "pm200fr20trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm200fr20LineTrapCritGoesOff.setStatus(
        "current"
    )

pm200fr20ClientTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 87, 10, 40)
)
pm200fr20ClientTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm200fr20-MIB", "pm200fr20AlmSfpDdmWarningPortn"),
        ("EKINOPS-Pm200fr20-MIB", "pm200fr20trapPortNumber"),
        ("EKINOPS-Pm200fr20-MIB", "pm200fr20trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm200fr20ClientTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm200fr20ClientTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 87, 10, 41)
)
pm200fr20ClientTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm200fr20-MIB", "pm200fr20AlmSfpDdmWarningPortn"),
        ("EKINOPS-Pm200fr20-MIB", "pm200fr20trapPortNumber"),
        ("EKINOPS-Pm200fr20-MIB", "pm200fr20trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm200fr20ClientTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm200fr20ClientTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 87, 10, 42)
)
pm200fr20ClientTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm200fr20-MIB", "pm200fr20AlmSfpDdmAlmPortn"),
        ("EKINOPS-Pm200fr20-MIB", "pm200fr20trapPortNumber"),
        ("EKINOPS-Pm200fr20-MIB", "pm200fr20trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm200fr20ClientTrapUrgentGoesOn.setStatus(
        "current"
    )

pm200fr20ClientTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 87, 10, 43)
)
pm200fr20ClientTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm200fr20-MIB", "pm200fr20AlmSfpDdmAlmPortn"),
        ("EKINOPS-Pm200fr20-MIB", "pm200fr20trapPortNumber"),
        ("EKINOPS-Pm200fr20-MIB", "pm200fr20trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm200fr20ClientTrapUrgentGoesOff.setStatus(
        "current"
    )

pm200fr20ClientTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 87, 10, 44)
)
pm200fr20ClientTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm200fr20-MIB", "pm200fr20AlmFailAccPortn"),
        ("EKINOPS-Pm200fr20-MIB", "pm200fr20AlmHwFailAccPortn"),
        ("EKINOPS-Pm200fr20-MIB", "pm200fr20trapPortNumber"),
        ("EKINOPS-Pm200fr20-MIB", "pm200fr20trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm200fr20ClientTrapCritGoesOn.setStatus(
        "current"
    )

pm200fr20ClientTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 87, 10, 45)
)
pm200fr20ClientTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm200fr20-MIB", "pm200fr20AlmFailAccPortn"),
        ("EKINOPS-Pm200fr20-MIB", "pm200fr20AlmHwFailAccPortn"),
        ("EKINOPS-Pm200fr20-MIB", "pm200fr20trapPortNumber"),
        ("EKINOPS-Pm200fr20-MIB", "pm200fr20trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm200fr20ClientTrapCritGoesOff.setStatus(
        "current"
    )

pm200fr20PowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 87, 10, 50)
)
pm200fr20PowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm200fr20-MIB", "pm200fr20AlmDefFuseB"),
        ("EKINOPS-Pm200fr20-MIB", "pm200fr20AlmDefFuseA"),
        ("EKINOPS-Pm200fr20-MIB", "pm200fr20trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm200fr20PowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pm200fr20PowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 87, 10, 51)
)
pm200fr20PowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm200fr20-MIB", "pm200fr20AlmDefFuseB"),
        ("EKINOPS-Pm200fr20-MIB", "pm200fr20AlmDefFuseA"),
        ("EKINOPS-Pm200fr20-MIB", "pm200fr20trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm200fr20PowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Pm200fr20-MIB",
    **{"Pm200fr20OtxGrid": Pm200fr20OtxGrid,
       "Pm200fr20ClientProtocolA": Pm200fr20ClientProtocolA,
       "Pm200fr20ClientProtocolB": Pm200fr20ClientProtocolB,
       "Pm200fr20ClientProtocolC": Pm200fr20ClientProtocolC,
       "Pm200fr20ProtocolMode": Pm200fr20ProtocolMode,
       "Pm200fr20OtxChannel": Pm200fr20OtxChannel,
       "Pm200fr20OrxChannel": Pm200fr20OrxChannel,
       "Pm200fr20DccMode": Pm200fr20DccMode,
       "modulePm200fr20": modulePm200fr20,
       "pm200fr20alarms": pm200fr20alarms,
       "pm200fr20AlmOther": pm200fr20AlmOther,
       "pm200fr20AlmOtherNurg": pm200fr20AlmOtherNurg,
       "pm200fr20AlmsynthAlm2": pm200fr20AlmsynthAlm2,
       "pm200fr20AlmConfTableSave": pm200fr20AlmConfTableSave,
       "pm200fr20AlmInvUpload": pm200fr20AlmInvUpload,
       "pm200fr20AlmConfTableLoad": pm200fr20AlmConfTableLoad,
       "pm200fr20AlmCorrelatOff": pm200fr20AlmCorrelatOff,
       "pm200fr20AlmMaintenanceOn": pm200fr20AlmMaintenanceOn,
       "pm200fr20AlmOtherUrg": pm200fr20AlmOtherUrg,
       "pm200fr20AlmmodFanFail": pm200fr20AlmmodFanFail,
       "pm200fr20AlmFanFail": pm200fr20AlmFanFail,
       "pm200fr20AlmFanHighSpeed": pm200fr20AlmFanHighSpeed,
       "pm200fr20AlmOtherCrit": pm200fr20AlmOtherCrit,
       "pm200fr20AlmsynthAlm0": pm200fr20AlmsynthAlm0,
       "pm200fr20AlmFailFan": pm200fr20AlmFailFan,
       "pm200fr20AlmModGlobFail": pm200fr20AlmModGlobFail,
       "pm200fr20AlmDefFuseA": pm200fr20AlmDefFuseA,
       "pm200fr20AlmDefFuseB": pm200fr20AlmDefFuseB,
       "pm200fr20AlmmsaModuleState": pm200fr20AlmmsaModuleState,
       "pm200fr20AlmMsaReady": pm200fr20AlmMsaReady,
       "pm200fr20AlmMsaFault": pm200fr20AlmMsaFault,
       "pm200fr20AlmClient": pm200fr20AlmClient,
       "pm200fr20AlmClientNurg": pm200fr20AlmClientNurg,
       "pm200fr20AlmclientSfpWarnDdmTable": pm200fr20AlmclientSfpWarnDdmTable,
       "pm200fr20AlmclientSfpWarnDdmEntry": pm200fr20AlmclientSfpWarnDdmEntry,
       "pm200fr20AlmclientSfpWarnDdmIndex": pm200fr20AlmclientSfpWarnDdmIndex,
       "pm200fr20AlmTxPwLowWngPortn": pm200fr20AlmTxPwLowWngPortn,
       "pm200fr20AlmTxPwrHighWngPortn": pm200fr20AlmTxPwrHighWngPortn,
       "pm200fr20AlmTxBiasLowWngPortn": pm200fr20AlmTxBiasLowWngPortn,
       "pm200fr20AlmTxBiasHighWngPortn": pm200fr20AlmTxBiasHighWngPortn,
       "pm200fr20AlmVccLowWngPortn": pm200fr20AlmVccLowWngPortn,
       "pm200fr20AlmVccHighWngPortn": pm200fr20AlmVccHighWngPortn,
       "pm200fr20AlmTempLowWngPortn": pm200fr20AlmTempLowWngPortn,
       "pm200fr20AlmTempHighWngPortn": pm200fr20AlmTempHighWngPortn,
       "pm200fr20AlmRxPwrLowWngPortn": pm200fr20AlmRxPwrLowWngPortn,
       "pm200fr20AlmRxPwrHighWngPortn": pm200fr20AlmRxPwrHighWngPortn,
       "pm200fr20AlmClientUrg": pm200fr20AlmClientUrg,
       "pm200fr20AlmclientHostLaneFaultTable": pm200fr20AlmclientHostLaneFaultTable,
       "pm200fr20AlmclientHostLaneFaultEntry": pm200fr20AlmclientHostLaneFaultEntry,
       "pm200fr20AlmclientHostLaneFaultIndex": pm200fr20AlmclientHostLaneFaultIndex,
       "pm200fr20AlmClientLossOfSyncPortn": pm200fr20AlmClientLossOfSyncPortn,
       "pm200fr20AlmClientInputLossOfSigPortn": pm200fr20AlmClientInputLossOfSigPortn,
       "pm200fr20AlmClientLanesMarkerUnlockPortn": pm200fr20AlmClientLanesMarkerUnlockPortn,
       "pm200fr20AlmClientLanes6466UnlockPortn": pm200fr20AlmClientLanes6466UnlockPortn,
       "pm200fr20AlmClientLanesNotAlignedPortn": pm200fr20AlmClientLanesNotAlignedPortn,
       "pm200fr20AlmClientCsfDetectedPortn": pm200fr20AlmClientCsfDetectedPortn,
       "pm200fr20AlmClientTxHostLolPortn": pm200fr20AlmClientTxHostLolPortn,
       "pm200fr20AlmClientLaneTxFifoErrorPortn": pm200fr20AlmClientLaneTxFifoErrorPortn,
       "pm200fr20AlmLfDetectedPortn": pm200fr20AlmLfDetectedPortn,
       "pm200fr20AlmRfDetectedPortn": pm200fr20AlmRfDetectedPortn,
       "pm200fr20AlmStm64ProtocDetectedPortn": pm200fr20AlmStm64ProtocDetectedPortn,
       "pm200fr20Alm10gbeProtocDetectedPortn": pm200fr20Alm10gbeProtocDetectedPortn,
       "pm200fr20AlmOtu2ProtocDetectedPortn": pm200fr20AlmOtu2ProtocDetectedPortn,
       "pm200fr20AlmOtu2eProtocDetectedPortn": pm200fr20AlmOtu2eProtocDetectedPortn,
       "pm200fr20AlmclientSfpAlmDdmTable": pm200fr20AlmclientSfpAlmDdmTable,
       "pm200fr20AlmclientSfpAlmDdmEntry": pm200fr20AlmclientSfpAlmDdmEntry,
       "pm200fr20AlmclientSfpAlmDdmIndex": pm200fr20AlmclientSfpAlmDdmIndex,
       "pm200fr20AlmTxPwrLowAlaPortn": pm200fr20AlmTxPwrLowAlaPortn,
       "pm200fr20AlmTxPwrHighAlaPortn": pm200fr20AlmTxPwrHighAlaPortn,
       "pm200fr20AlmTxBiasLowAlaPortn": pm200fr20AlmTxBiasLowAlaPortn,
       "pm200fr20AlmTxBiasHighAlaPortn": pm200fr20AlmTxBiasHighAlaPortn,
       "pm200fr20AlmVccLowAlaPortn": pm200fr20AlmVccLowAlaPortn,
       "pm200fr20AlmVccHighAlaPortn": pm200fr20AlmVccHighAlaPortn,
       "pm200fr20AlmTempLowAlaPortn": pm200fr20AlmTempLowAlaPortn,
       "pm200fr20AlmTempHighAlaPortn": pm200fr20AlmTempHighAlaPortn,
       "pm200fr20AlmRxPwrLowAlaPortn": pm200fr20AlmRxPwrLowAlaPortn,
       "pm200fr20AlmRxPwrHighAlaPortn": pm200fr20AlmRxPwrHighAlaPortn,
       "pm200fr20AlmclientOtnAlmTable": pm200fr20AlmclientOtnAlmTable,
       "pm200fr20AlmclientOtnAlmEntry": pm200fr20AlmclientOtnAlmEntry,
       "pm200fr20AlmclientOtnAlmIndex": pm200fr20AlmclientOtnAlmIndex,
       "pm200fr20AlmClientOtu2eDlomPortn": pm200fr20AlmClientOtu2eDlomPortn,
       "pm200fr20AlmClientCrit": pm200fr20AlmClientCrit,
       "pm200fr20AlmsynthAlmPortTable": pm200fr20AlmsynthAlmPortTable,
       "pm200fr20AlmsynthAlmPortEntry": pm200fr20AlmsynthAlmPortEntry,
       "pm200fr20AlmsynthAlmPortIndex": pm200fr20AlmsynthAlmPortIndex,
       "pm200fr20AlmSfpAbsentPortn": pm200fr20AlmSfpAbsentPortn,
       "pm200fr20AlmDdmAbsentPortn": pm200fr20AlmDdmAbsentPortn,
       "pm200fr20AlmHwFailAccPortn": pm200fr20AlmHwFailAccPortn,
       "pm200fr20AlmDwLsdPortn": pm200fr20AlmDwLsdPortn,
       "pm200fr20AlmClientLocalOosPortn": pm200fr20AlmClientLocalOosPortn,
       "pm200fr20AlmClientRemoteOosPortn": pm200fr20AlmClientRemoteOosPortn,
       "pm200fr20AlmDwCaisPortn": pm200fr20AlmDwCaisPortn,
       "pm200fr20AlmSfpDdmWarningPortn": pm200fr20AlmSfpDdmWarningPortn,
       "pm200fr20AlmSfpDdmAlmPortn": pm200fr20AlmSfpDdmAlmPortn,
       "pm200fr20AlmFailAccPortn": pm200fr20AlmFailAccPortn,
       "pm200fr20AlmUpCsfPortn": pm200fr20AlmUpCsfPortn,
       "pm200fr20AlmLine": pm200fr20AlmLine,
       "pm200fr20AlmLineNurg": pm200fr20AlmLineNurg,
       "pm200fr20AlmlineQsfpWarnDdmTable": pm200fr20AlmlineQsfpWarnDdmTable,
       "pm200fr20AlmlineQsfpWarnDdmEntry": pm200fr20AlmlineQsfpWarnDdmEntry,
       "pm200fr20AlmlineQsfpWarnDdmIndex": pm200fr20AlmlineQsfpWarnDdmIndex,
       "pm200fr20AlmLineTxPwLowWngPortn": pm200fr20AlmLineTxPwLowWngPortn,
       "pm200fr20AlmLineTxPwrHighWngPortn": pm200fr20AlmLineTxPwrHighWngPortn,
       "pm200fr20AlmLineTxBiasLowWngPortn": pm200fr20AlmLineTxBiasLowWngPortn,
       "pm200fr20AlmLineTxBiasHighWngPortn": pm200fr20AlmLineTxBiasHighWngPortn,
       "pm200fr20AlmLineVccLowWngPortn": pm200fr20AlmLineVccLowWngPortn,
       "pm200fr20AlmLineVccHighWngPortn": pm200fr20AlmLineVccHighWngPortn,
       "pm200fr20AlmLineTempLowWngPortn": pm200fr20AlmLineTempLowWngPortn,
       "pm200fr20AlmLineTempHighWngPortn": pm200fr20AlmLineTempHighWngPortn,
       "pm200fr20AlmLineRxPwrLowWngPortn": pm200fr20AlmLineRxPwrLowWngPortn,
       "pm200fr20AlmLineRxPwrHighWngPortn": pm200fr20AlmLineRxPwrHighWngPortn,
       "pm200fr20AlmLineUrg": pm200fr20AlmLineUrg,
       "pm200fr20AlmlineHostLaneFaultTable": pm200fr20AlmlineHostLaneFaultTable,
       "pm200fr20AlmlineHostLaneFaultEntry": pm200fr20AlmlineHostLaneFaultEntry,
       "pm200fr20AlmlineHostLaneFaultIndex": pm200fr20AlmlineHostLaneFaultIndex,
       "pm200fr20AlmLineInputLossOfSignalPortn": pm200fr20AlmLineInputLossOfSignalPortn,
       "pm200fr20AlmLineLossOfFramePortn": pm200fr20AlmLineLossOfFramePortn,
       "pm200fr20AlmLineSmBdiInsertedPortn": pm200fr20AlmLineSmBdiInsertedPortn,
       "pm200fr20AlmLineSmBdiDetectedPortn": pm200fr20AlmLineSmBdiDetectedPortn,
       "pm200fr20AlmLineSmIaeInsertedPortn": pm200fr20AlmLineSmIaeInsertedPortn,
       "pm200fr20AlmLineSmIaeDetectedPortn": pm200fr20AlmLineSmIaeDetectedPortn,
       "pm200fr20AlmOtu4DdegPortn": pm200fr20AlmOtu4DdegPortn,
       "pm200fr20AlmClientOtu4DtimPortn": pm200fr20AlmClientOtu4DtimPortn,
       "pm200fr20AlmLineOchr4DlosPPortn": pm200fr20AlmLineOchr4DlosPPortn,
       "pm200fr20AlmLineOtu4DlomPortn": pm200fr20AlmLineOtu4DlomPortn,
       "pm200fr20AlmlineOdu4AlmTable": pm200fr20AlmlineOdu4AlmTable,
       "pm200fr20AlmlineOdu4AlmEntry": pm200fr20AlmlineOdu4AlmEntry,
       "pm200fr20AlmlineOdu4AlmIndex": pm200fr20AlmlineOdu4AlmIndex,
       "pm200fr20AlmLineOdu4DplmPortn": pm200fr20AlmLineOdu4DplmPortn,
       "pm200fr20AlmLineOdu4DdegPortn": pm200fr20AlmLineOdu4DdegPortn,
       "pm200fr20AlmLineOdu4IaisPortn": pm200fr20AlmLineOdu4IaisPortn,
       "pm200fr20AlmLineOdu4DtimPortn": pm200fr20AlmLineOdu4DtimPortn,
       "pm200fr20AlmLineOdu4DaisPortn": pm200fr20AlmLineOdu4DaisPortn,
       "pm200fr20AlmLineOdu4IociPortn": pm200fr20AlmLineOdu4IociPortn,
       "pm200fr20AlmLineOdu4DociPortn": pm200fr20AlmLineOdu4DociPortn,
       "pm200fr20AlmLineOdu4IbdiPortn": pm200fr20AlmLineOdu4IbdiPortn,
       "pm200fr20AlmLineOdu4DbdiPortn": pm200fr20AlmLineOdu4DbdiPortn,
       "pm200fr20AlmLineOdu4IlckPortn": pm200fr20AlmLineOdu4IlckPortn,
       "pm200fr20AlmLineOdu4DlckPortn": pm200fr20AlmLineOdu4DlckPortn,
       "pm200fr20AlmLineCrit": pm200fr20AlmLineCrit,
       "pm200fr20AlmsynthAlmLineTable": pm200fr20AlmsynthAlmLineTable,
       "pm200fr20AlmsynthAlmLineEntry": pm200fr20AlmsynthAlmLineEntry,
       "pm200fr20AlmsynthAlmLineIndex": pm200fr20AlmsynthAlmLineIndex,
       "pm200fr20AlmXfpAbsentPortn": pm200fr20AlmXfpAbsentPortn,
       "pm200fr20AlmXfpInitNotComplPortn": pm200fr20AlmXfpInitNotComplPortn,
       "pm200fr20AlmLineHwFailPortn": pm200fr20AlmLineHwFailPortn,
       "pm200fr20AlmXfpTxOffPortn": pm200fr20AlmXfpTxOffPortn,
       "pm200fr20AlmLineLocalOosPortn": pm200fr20AlmLineLocalOosPortn,
       "pm200fr20AlmUpRdiInsPortn": pm200fr20AlmUpRdiInsPortn,
       "pm200fr20AlmLineDdmWarningPortn": pm200fr20AlmLineDdmWarningPortn,
       "pm200fr20AlmLineDdmAlmPortn": pm200fr20AlmLineDdmAlmPortn,
       "pm200fr20AlmLineFailPortn": pm200fr20AlmLineFailPortn,
       "pm200fr20measures": pm200fr20measures,
       "pm200fr20MesrOther": pm200fr20MesrOther,
       "pm200fr20Mesrsynth0": pm200fr20Mesrsynth0,
       "pm200fr20Mesrsynth1": pm200fr20Mesrsynth1,
       "pm200fr20MesrpmIntervalNumber": pm200fr20MesrpmIntervalNumber,
       "pm200fr20MesrlineNetTxLaserOutputPwrAverage": pm200fr20MesrlineNetTxLaserOutputPwrAverage,
       "pm200fr20MesrlineNetTxLaserTempAverage": pm200fr20MesrlineNetTxLaserTempAverage,
       "pm200fr20MesrlineNetTxBiasCurrentAverage": pm200fr20MesrlineNetTxBiasCurrentAverage,
       "pm200fr20MesrlineNetRxInputPwrAverage": pm200fr20MesrlineNetRxInputPwrAverage,
       "pm200fr20MesrlineResidualChromaticDispAverage": pm200fr20MesrlineResidualChromaticDispAverage,
       "pm200fr20MesrlineDiffGroupDelayAverage": pm200fr20MesrlineDiffGroupDelayAverage,
       "pm200fr20MesrlineQFactorAverage": pm200fr20MesrlineQFactorAverage,
       "pm200fr20MesrlineCarrierFreqOffsetAverage": pm200fr20MesrlineCarrierFreqOffsetAverage,
       "pm200fr20MesrlineOsnrAverage": pm200fr20MesrlineOsnrAverage,
       "pm200fr20MesrclientNetTxTempMin": pm200fr20MesrclientNetTxTempMin,
       "pm200fr20MesrclientNetTxBiasMin": pm200fr20MesrclientNetTxBiasMin,
       "pm200fr20MesrclientNetTxPwrMin": pm200fr20MesrclientNetTxPwrMin,
       "pm200fr20MesrclientNetRxPwrMin": pm200fr20MesrclientNetRxPwrMin,
       "pm200fr20MesrlineNetTxLaserOutputPwrMin": pm200fr20MesrlineNetTxLaserOutputPwrMin,
       "pm200fr20MesrlineNetTxLaserTempMin": pm200fr20MesrlineNetTxLaserTempMin,
       "pm200fr20MesrlineNetTxBiasCurrentMin": pm200fr20MesrlineNetTxBiasCurrentMin,
       "pm200fr20MesrlineNetRxInputPwrMin": pm200fr20MesrlineNetRxInputPwrMin,
       "pm200fr20MesrlineResidualChromaticDispMin": pm200fr20MesrlineResidualChromaticDispMin,
       "pm200fr20MesrlineDiffGroupDelayMin": pm200fr20MesrlineDiffGroupDelayMin,
       "pm200fr20MesrlineQFactorMin": pm200fr20MesrlineQFactorMin,
       "pm200fr20MesrlineCarrierFreqOffsetMin": pm200fr20MesrlineCarrierFreqOffsetMin,
       "pm200fr20MesrlineOsnrMin": pm200fr20MesrlineOsnrMin,
       "pm200fr20MesrclientNetTxTempMax": pm200fr20MesrclientNetTxTempMax,
       "pm200fr20MesrclientNetTxBiasMax": pm200fr20MesrclientNetTxBiasMax,
       "pm200fr20MesrclientNetTxPwrMax": pm200fr20MesrclientNetTxPwrMax,
       "pm200fr20MesrclientNetRxPwrMax": pm200fr20MesrclientNetRxPwrMax,
       "pm200fr20MesrlineNetTxLaserOutputPwrMax": pm200fr20MesrlineNetTxLaserOutputPwrMax,
       "pm200fr20MesrlineNetTxLaserTempMax": pm200fr20MesrlineNetTxLaserTempMax,
       "pm200fr20MesrlineNetTxBiasCurrentMax": pm200fr20MesrlineNetTxBiasCurrentMax,
       "pm200fr20MesrlineNetRxInputPwrMax": pm200fr20MesrlineNetRxInputPwrMax,
       "pm200fr20MesrlineResidualChromaticDispMax": pm200fr20MesrlineResidualChromaticDispMax,
       "pm200fr20MesrlineDiffGroupDelayMax": pm200fr20MesrlineDiffGroupDelayMax,
       "pm200fr20MesrlineQFactorMax": pm200fr20MesrlineQFactorMax,
       "pm200fr20MesrlineCarrierFreqOffsetMax": pm200fr20MesrlineCarrierFreqOffsetMax,
       "pm200fr20MesrlineOsnrMax": pm200fr20MesrlineOsnrMax,
       "pm200fr20MesrlineTrscvTemp": pm200fr20MesrlineTrscvTemp,
       "pm200fr20MesrlineTrscvVoltage": pm200fr20MesrlineTrscvVoltage,
       "pm200fr20MesrClient": pm200fr20MesrClient,
       "pm200fr20MesrclientTxTempTable": pm200fr20MesrclientTxTempTable,
       "pm200fr20MesrclientTxTempEntry": pm200fr20MesrclientTxTempEntry,
       "pm200fr20MesrclientTxTempIndex": pm200fr20MesrclientTxTempIndex,
       "pm200fr20MesrclientTxTempPortn": pm200fr20MesrclientTxTempPortn,
       "pm200fr20MesrclientTxBiasTable": pm200fr20MesrclientTxBiasTable,
       "pm200fr20MesrclientTxBiasEntry": pm200fr20MesrclientTxBiasEntry,
       "pm200fr20MesrclientTxBiasIndex": pm200fr20MesrclientTxBiasIndex,
       "pm200fr20MesrclientTxBiasPortn": pm200fr20MesrclientTxBiasPortn,
       "pm200fr20MesrclientTxPwrTable": pm200fr20MesrclientTxPwrTable,
       "pm200fr20MesrclientTxPwrEntry": pm200fr20MesrclientTxPwrEntry,
       "pm200fr20MesrclientTxPwrIndex": pm200fr20MesrclientTxPwrIndex,
       "pm200fr20MesrclientTxPwrPortn": pm200fr20MesrclientTxPwrPortn,
       "pm200fr20MesrclientRxPwrTable": pm200fr20MesrclientRxPwrTable,
       "pm200fr20MesrclientRxPwrEntry": pm200fr20MesrclientRxPwrEntry,
       "pm200fr20MesrclientRxPwrIndex": pm200fr20MesrclientRxPwrIndex,
       "pm200fr20MesrclientRxPwrPortn": pm200fr20MesrclientRxPwrPortn,
       "pm200fr20MesrLine": pm200fr20MesrLine,
       "pm200fr20MesrlineNetTxLaserOutputPwrTable": pm200fr20MesrlineNetTxLaserOutputPwrTable,
       "pm200fr20MesrlineNetTxLaserOutputPwrEntry": pm200fr20MesrlineNetTxLaserOutputPwrEntry,
       "pm200fr20MesrlineNetTxLaserOutputPwrIndex": pm200fr20MesrlineNetTxLaserOutputPwrIndex,
       "pm200fr20MesrlineNetTxLaserOutputPwrPortn": pm200fr20MesrlineNetTxLaserOutputPwrPortn,
       "pm200fr20MesrlineNetTxLaserTempTable": pm200fr20MesrlineNetTxLaserTempTable,
       "pm200fr20MesrlineNetTxLaserTempEntry": pm200fr20MesrlineNetTxLaserTempEntry,
       "pm200fr20MesrlineNetTxLaserTempIndex": pm200fr20MesrlineNetTxLaserTempIndex,
       "pm200fr20MesrlineNetTxLaserTempPortn": pm200fr20MesrlineNetTxLaserTempPortn,
       "pm200fr20MesrlineNetTxBiasCurrentTable": pm200fr20MesrlineNetTxBiasCurrentTable,
       "pm200fr20MesrlineNetTxBiasCurrentEntry": pm200fr20MesrlineNetTxBiasCurrentEntry,
       "pm200fr20MesrlineNetTxBiasCurrentIndex": pm200fr20MesrlineNetTxBiasCurrentIndex,
       "pm200fr20MesrlineNetTxBiasCurrentPortn": pm200fr20MesrlineNetTxBiasCurrentPortn,
       "pm200fr20MesrlineNetRxInputPwrTable": pm200fr20MesrlineNetRxInputPwrTable,
       "pm200fr20MesrlineNetRxInputPwrEntry": pm200fr20MesrlineNetRxInputPwrEntry,
       "pm200fr20MesrlineNetRxInputPwrIndex": pm200fr20MesrlineNetRxInputPwrIndex,
       "pm200fr20MesrlineNetRxInputPwrPortn": pm200fr20MesrlineNetRxInputPwrPortn,
       "pm200fr20MesrlineResidualChromaticDispTable": pm200fr20MesrlineResidualChromaticDispTable,
       "pm200fr20MesrlineResidualChromaticDispEntry": pm200fr20MesrlineResidualChromaticDispEntry,
       "pm200fr20MesrlineResidualChromaticDispIndex": pm200fr20MesrlineResidualChromaticDispIndex,
       "pm200fr20MesrlineResidualChromaticDispPortn": pm200fr20MesrlineResidualChromaticDispPortn,
       "pm200fr20MesrlineDiffGroupDelayTable": pm200fr20MesrlineDiffGroupDelayTable,
       "pm200fr20MesrlineDiffGroupDelayEntry": pm200fr20MesrlineDiffGroupDelayEntry,
       "pm200fr20MesrlineDiffGroupDelayIndex": pm200fr20MesrlineDiffGroupDelayIndex,
       "pm200fr20MesrlineDiffGroupDelayPortn": pm200fr20MesrlineDiffGroupDelayPortn,
       "pm200fr20MesrlineQFactorTable": pm200fr20MesrlineQFactorTable,
       "pm200fr20MesrlineQFactorEntry": pm200fr20MesrlineQFactorEntry,
       "pm200fr20MesrlineQFactorIndex": pm200fr20MesrlineQFactorIndex,
       "pm200fr20MesrlineQFactorPortn": pm200fr20MesrlineQFactorPortn,
       "pm200fr20MesrlineCarrierFreqOffsetTable": pm200fr20MesrlineCarrierFreqOffsetTable,
       "pm200fr20MesrlineCarrierFreqOffsetEntry": pm200fr20MesrlineCarrierFreqOffsetEntry,
       "pm200fr20MesrlineCarrierFreqOffsetIndex": pm200fr20MesrlineCarrierFreqOffsetIndex,
       "pm200fr20MesrlineCarrierFreqOffsetPortn": pm200fr20MesrlineCarrierFreqOffsetPortn,
       "pm200fr20MesrlineOsnrTable": pm200fr20MesrlineOsnrTable,
       "pm200fr20MesrlineOsnrEntry": pm200fr20MesrlineOsnrEntry,
       "pm200fr20MesrlineOsnrIndex": pm200fr20MesrlineOsnrIndex,
       "pm200fr20MesrlineOsnrPortn": pm200fr20MesrlineOsnrPortn,
       "pm200fr20counters": pm200fr20counters,
       "pm200fr20CntOther": pm200fr20CntOther,
       "pm200fr20CntClient": pm200fr20CntClient,
       "pm200fr20CntclientInputErrorCounterTable": pm200fr20CntclientInputErrorCounterTable,
       "pm200fr20CntclientInputErrorCounterEntry": pm200fr20CntclientInputErrorCounterEntry,
       "pm200fr20CntclientInputErrorCounterIndex": pm200fr20CntclientInputErrorCounterIndex,
       "pm200fr20CntclientInputErrorCounterValuePortn": pm200fr20CntclientInputErrorCounterValuePortn,
       "pm200fr20CntclientInputErrorCounterErrorPortn": pm200fr20CntclientInputErrorCounterErrorPortn,
       "pm200fr20CntclientInputErrorCounterOverloadPortn": pm200fr20CntclientInputErrorCounterOverloadPortn,
       "pm200fr20CntclientCbipCounterTable": pm200fr20CntclientCbipCounterTable,
       "pm200fr20CntclientCbipCounterEntry": pm200fr20CntclientCbipCounterEntry,
       "pm200fr20CntclientCbipCounterIndex": pm200fr20CntclientCbipCounterIndex,
       "pm200fr20CntclientCbipCounterValuePortn": pm200fr20CntclientCbipCounterValuePortn,
       "pm200fr20CntclientCbipCounterErrorPortn": pm200fr20CntclientCbipCounterErrorPortn,
       "pm200fr20CntclientCbipCounterOverloadPortn": pm200fr20CntclientCbipCounterOverloadPortn,
       "pm200fr20CntLine": pm200fr20CntLine,
       "pm200fr20CntlocalLineSmBip8ErrorCounterTable": pm200fr20CntlocalLineSmBip8ErrorCounterTable,
       "pm200fr20CntlocalLineSmBip8ErrorCounterEntry": pm200fr20CntlocalLineSmBip8ErrorCounterEntry,
       "pm200fr20CntlocalLineSmBip8ErrorCounterIndex": pm200fr20CntlocalLineSmBip8ErrorCounterIndex,
       "pm200fr20CntlocalLineSmBip8ErrorCounterValuePortn": pm200fr20CntlocalLineSmBip8ErrorCounterValuePortn,
       "pm200fr20CntlocalLineSmBip8ErrorCounterErrorPortn": pm200fr20CntlocalLineSmBip8ErrorCounterErrorPortn,
       "pm200fr20CntlocalLineSmBip8ErrorCounterOverloadPortn": pm200fr20CntlocalLineSmBip8ErrorCounterOverloadPortn,
       "pm200fr20CntlocalLineFecCorrectedErrorsCounterTable": pm200fr20CntlocalLineFecCorrectedErrorsCounterTable,
       "pm200fr20CntlocalLineFecCorrectedErrorsCounterEntry": pm200fr20CntlocalLineFecCorrectedErrorsCounterEntry,
       "pm200fr20CntlocalLineFecCorrectedErrorsCounterIndex": pm200fr20CntlocalLineFecCorrectedErrorsCounterIndex,
       "pm200fr20CntlocalLineFecCorrectedErrorsCounterValuePortn": pm200fr20CntlocalLineFecCorrectedErrorsCounterValuePortn,
       "pm200fr20CntlocalLineFecCorrectedErrorsCounterErrorPortn": pm200fr20CntlocalLineFecCorrectedErrorsCounterErrorPortn,
       "pm200fr20CntlocalLineFecCorrectedErrorsCounterOverloadPortn": pm200fr20CntlocalLineFecCorrectedErrorsCounterOverloadPortn,
       "pm200fr20CntremoteLineSmBip8ErrorCounterTable": pm200fr20CntremoteLineSmBip8ErrorCounterTable,
       "pm200fr20CntremoteLineSmBip8ErrorCounterEntry": pm200fr20CntremoteLineSmBip8ErrorCounterEntry,
       "pm200fr20CntremoteLineSmBip8ErrorCounterIndex": pm200fr20CntremoteLineSmBip8ErrorCounterIndex,
       "pm200fr20CntremoteLineSmBip8ErrorCounterValuePortn": pm200fr20CntremoteLineSmBip8ErrorCounterValuePortn,
       "pm200fr20CntremoteLineSmBip8ErrorCounterErrorPortn": pm200fr20CntremoteLineSmBip8ErrorCounterErrorPortn,
       "pm200fr20CntremoteLineSmBip8ErrorCounterOverloadPortn": pm200fr20CntremoteLineSmBip8ErrorCounterOverloadPortn,
       "pm200fr20CntlineDfrmTimCntTable": pm200fr20CntlineDfrmTimCntTable,
       "pm200fr20CntlineDfrmTimCntEntry": pm200fr20CntlineDfrmTimCntEntry,
       "pm200fr20CntlineDfrmTimCntIndex": pm200fr20CntlineDfrmTimCntIndex,
       "pm200fr20CntlineDfrmTimCntValuePortn": pm200fr20CntlineDfrmTimCntValuePortn,
       "pm200fr20CntlineDfrmTimCntErrorPortn": pm200fr20CntlineDfrmTimCntErrorPortn,
       "pm200fr20CntlineDfrmTimCntOverloadPortn": pm200fr20CntlineDfrmTimCntOverloadPortn,
       "pm200fr20CntlocalLineTrscvPreSdFecErrorCounterTable": pm200fr20CntlocalLineTrscvPreSdFecErrorCounterTable,
       "pm200fr20CntlocalLineTrscvPreSdFecErrorCounterEntry": pm200fr20CntlocalLineTrscvPreSdFecErrorCounterEntry,
       "pm200fr20CntlocalLineTrscvPreSdFecErrorCounterIndex": pm200fr20CntlocalLineTrscvPreSdFecErrorCounterIndex,
       "pm200fr20CntlocalLineTrscvPreSdFecErrorCounterValuePortn": pm200fr20CntlocalLineTrscvPreSdFecErrorCounterValuePortn,
       "pm200fr20CntlocalLineTrscvPreSdFecErrorCounterErrorPortn": pm200fr20CntlocalLineTrscvPreSdFecErrorCounterErrorPortn,
       "pm200fr20CntlocalLineTrscvPreSdFecErrorCounterOverloadPortn": pm200fr20CntlocalLineTrscvPreSdFecErrorCounterOverloadPortn,
       "pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterTable": pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterTable,
       "pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterEntry": pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterEntry,
       "pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterIndex": pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterIndex,
       "pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn": pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn,
       "pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn": pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn,
       "pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn": pm200fr20CntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn,
       "pm200fr20CntlocalLineTrscvPreSdFecBitCounterTable": pm200fr20CntlocalLineTrscvPreSdFecBitCounterTable,
       "pm200fr20CntlocalLineTrscvPreSdFecBitCounterEntry": pm200fr20CntlocalLineTrscvPreSdFecBitCounterEntry,
       "pm200fr20CntlocalLineTrscvPreSdFecBitCounterIndex": pm200fr20CntlocalLineTrscvPreSdFecBitCounterIndex,
       "pm200fr20CntlocalLineTrscvPreSdFecBitCounterValuePortn": pm200fr20CntlocalLineTrscvPreSdFecBitCounterValuePortn,
       "pm200fr20CntlocalLineTrscvPreSdFecBitCounterErrorPortn": pm200fr20CntlocalLineTrscvPreSdFecBitCounterErrorPortn,
       "pm200fr20CntlocalLineTrscvPreSdFecBitCounterOverloadPortn": pm200fr20CntlocalLineTrscvPreSdFecBitCounterOverloadPortn,
       "pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterTable": pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterTable,
       "pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterEntry": pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterEntry,
       "pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterIndex": pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterIndex,
       "pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn": pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn,
       "pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn": pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn,
       "pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn": pm200fr20CntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn,
       "pm200fr20controlsWrite": pm200fr20controlsWrite,
       "pm200fr20CtrlOther": pm200fr20CtrlOther,
       "pm200fr20CtrlconfMgnt1": pm200fr20CtrlconfMgnt1,
       "pm200fr20CtrlConf1Load1": pm200fr20CtrlConf1Load1,
       "pm200fr20CtrlConf2Load1": pm200fr20CtrlConf2Load1,
       "pm200fr20CtrlConf2Flash1": pm200fr20CtrlConf2Flash1,
       "pm200fr20CtrlConf2Clear1": pm200fr20CtrlConf2Clear1,
       "pm200fr20Ctrlsynth4": pm200fr20Ctrlsynth4,
       "pm200fr20CtrlCorrelatOn": pm200fr20CtrlCorrelatOn,
       "pm200fr20CtrlCorrelatOff": pm200fr20CtrlCorrelatOff,
       "pm200fr20CtrlswMgnt": pm200fr20CtrlswMgnt,
       "pm200fr20CtrlColdReset": pm200fr20CtrlColdReset,
       "pm200fr20CtrlWarmReset": pm200fr20CtrlWarmReset,
       "pm200fr20CtrlLoadSwBank1": pm200fr20CtrlLoadSwBank1,
       "pm200fr20CtrlLoadSwBank2": pm200fr20CtrlLoadSwBank2,
       "pm200fr20CtrlgwMgnt": pm200fr20CtrlgwMgnt,
       "pm200fr20CtrlCurrentGwReset": pm200fr20CtrlCurrentGwReset,
       "pm200fr20CtrlLoadGwBank1": pm200fr20CtrlLoadGwBank1,
       "pm200fr20CtrlLoadGwBank2": pm200fr20CtrlLoadGwBank2,
       "pm200fr20CtrlLoadGwBank3": pm200fr20CtrlLoadGwBank3,
       "pm200fr20CtrlLoadGwBank4": pm200fr20CtrlLoadGwBank4,
       "pm200fr20CtrlledTest": pm200fr20CtrlledTest,
       "pm200fr20CtrlGreenLed": pm200fr20CtrlGreenLed,
       "pm200fr20CtrlRedLed": pm200fr20CtrlRedLed,
       "pm200fr20CtrlLedOff": pm200fr20CtrlLedOff,
       "pm200fr20CtrlinitSwitchMarvell": pm200fr20CtrlinitSwitchMarvell,
       "pm200fr20CtrlInitSwitchMarvell": pm200fr20CtrlInitSwitchMarvell,
       "pm200fr20CtrlresetCount": pm200fr20CtrlresetCount,
       "pm200fr20CtrlResetcount": pm200fr20CtrlResetcount,
       "pm200fr20CtrlresetRmon": pm200fr20CtrlresetRmon,
       "pm200fr20CtrlResetrmon": pm200fr20CtrlResetrmon,
       "pm200fr20CtrlresetMeasurements": pm200fr20CtrlresetMeasurements,
       "pm200fr20CtrlResetmeasurements": pm200fr20CtrlResetmeasurements,
       "pm200fr20CtrlClient": pm200fr20CtrlClient,
       "pm200fr20CtrlaccessLoopTable": pm200fr20CtrlaccessLoopTable,
       "pm200fr20CtrlaccessLoopEntry": pm200fr20CtrlaccessLoopEntry,
       "pm200fr20CtrlaccessLoopIndex": pm200fr20CtrlaccessLoopIndex,
       "pm200fr20CtrlaccessLoopPortn": pm200fr20CtrlaccessLoopPortn,
       "pm200fr20CtrlclientLoopToLineTable": pm200fr20CtrlclientLoopToLineTable,
       "pm200fr20CtrlclientLoopToLineEntry": pm200fr20CtrlclientLoopToLineEntry,
       "pm200fr20CtrlclientLoopToLineIndex": pm200fr20CtrlclientLoopToLineIndex,
       "pm200fr20CtrlclientLoopToLinePortn": pm200fr20CtrlclientLoopToLinePortn,
       "pm200fr20CtrlcsfUpInsTable": pm200fr20CtrlcsfUpInsTable,
       "pm200fr20CtrlcsfUpInsEntry": pm200fr20CtrlcsfUpInsEntry,
       "pm200fr20CtrlcsfUpInsIndex": pm200fr20CtrlcsfUpInsIndex,
       "pm200fr20CtrlcsfUpInsPortn": pm200fr20CtrlcsfUpInsPortn,
       "pm200fr20CtrlcaisDwInsTable": pm200fr20CtrlcaisDwInsTable,
       "pm200fr20CtrlcaisDwInsEntry": pm200fr20CtrlcaisDwInsEntry,
       "pm200fr20CtrlcaisDwInsIndex": pm200fr20CtrlcaisDwInsIndex,
       "pm200fr20CtrlcaisDwInsPortn": pm200fr20CtrlcaisDwInsPortn,
       "pm200fr20CtrlclientResetAllCountTable": pm200fr20CtrlclientResetAllCountTable,
       "pm200fr20CtrlclientResetAllCountEntry": pm200fr20CtrlclientResetAllCountEntry,
       "pm200fr20CtrlclientResetAllCountIndex": pm200fr20CtrlclientResetAllCountIndex,
       "pm200fr20CtrlclientResetAllCountsPortn": pm200fr20CtrlclientResetAllCountsPortn,
       "pm200fr20CtrlLine": pm200fr20CtrlLine,
       "pm200fr20CtrlcommAccessLoopTable": pm200fr20CtrlcommAccessLoopTable,
       "pm200fr20CtrlcommAccessLoopEntry": pm200fr20CtrlcommAccessLoopEntry,
       "pm200fr20CtrlcommAccessLoopIndex": pm200fr20CtrlcommAccessLoopIndex,
       "pm200fr20CtrlcommAccessLoopPortn": pm200fr20CtrlcommAccessLoopPortn,
       "pm200fr20CtrllineLoopTable": pm200fr20CtrllineLoopTable,
       "pm200fr20CtrllineLoopEntry": pm200fr20CtrllineLoopEntry,
       "pm200fr20CtrllineLoopIndex": pm200fr20CtrllineLoopIndex,
       "pm200fr20CtrllineLoopPortn": pm200fr20CtrllineLoopPortn,
       "pm200fr20CtrlfecDisableTable": pm200fr20CtrlfecDisableTable,
       "pm200fr20CtrlfecDisableEntry": pm200fr20CtrlfecDisableEntry,
       "pm200fr20CtrlfecDisableIndex": pm200fr20CtrlfecDisableIndex,
       "pm200fr20CtrlfecDisablePortn": pm200fr20CtrlfecDisablePortn,
       "pm200fr20CtrlmsaLineLoopTable": pm200fr20CtrlmsaLineLoopTable,
       "pm200fr20CtrlmsaLineLoopEntry": pm200fr20CtrlmsaLineLoopEntry,
       "pm200fr20CtrlmsaLineLoopIndex": pm200fr20CtrlmsaLineLoopIndex,
       "pm200fr20CtrlmsaLineLoopPortn": pm200fr20CtrlmsaLineLoopPortn,
       "pm200fr20CtrlmsaTxResetTable": pm200fr20CtrlmsaTxResetTable,
       "pm200fr20CtrlmsaTxResetEntry": pm200fr20CtrlmsaTxResetEntry,
       "pm200fr20CtrlmsaTxResetIndex": pm200fr20CtrlmsaTxResetIndex,
       "pm200fr20CtrlmsaTxResetPortn": pm200fr20CtrlmsaTxResetPortn,
       "pm200fr20CtrlmsaRxResetTable": pm200fr20CtrlmsaRxResetTable,
       "pm200fr20CtrlmsaRxResetEntry": pm200fr20CtrlmsaRxResetEntry,
       "pm200fr20CtrlmsaRxResetIndex": pm200fr20CtrlmsaRxResetIndex,
       "pm200fr20CtrlmsaRxResetPortn": pm200fr20CtrlmsaRxResetPortn,
       "pm200fr20CtrlmsaShutdownTable": pm200fr20CtrlmsaShutdownTable,
       "pm200fr20CtrlmsaShutdownEntry": pm200fr20CtrlmsaShutdownEntry,
       "pm200fr20CtrlmsaShutdownIndex": pm200fr20CtrlmsaShutdownIndex,
       "pm200fr20CtrlmsaShutdownPortn": pm200fr20CtrlmsaShutdownPortn,
       "pm200fr20CtrllineResetAllCountTable": pm200fr20CtrllineResetAllCountTable,
       "pm200fr20CtrllineResetAllCountEntry": pm200fr20CtrllineResetAllCountEntry,
       "pm200fr20CtrllineResetAllCountIndex": pm200fr20CtrllineResetAllCountIndex,
       "pm200fr20CtrllineResetAllCountsPortn": pm200fr20CtrllineResetAllCountsPortn,
       "pm200fr20ri": pm200fr20ri,
       "pm200fr20riTable": pm200fr20riTable,
       "pm200fr20RinvSfpTable": pm200fr20RinvSfpTable,
       "pm200fr20RinvSfpEntry": pm200fr20RinvSfpEntry,
       "pm200fr20RinvSfpIndex": pm200fr20RinvSfpIndex,
       "pm200fr20Rinvsfp": pm200fr20Rinvsfp,
       "pm200fr20RinvLineTable": pm200fr20RinvLineTable,
       "pm200fr20RinvLineEntry": pm200fr20RinvLineEntry,
       "pm200fr20RinvLineIndex": pm200fr20RinvLineIndex,
       "pm200fr20RinvxfpLine": pm200fr20RinvxfpLine,
       "pm200fr20RinvReloadInventory": pm200fr20RinvReloadInventory,
       "pm200fr20RinvHwPlatform": pm200fr20RinvHwPlatform,
       "pm200fr20RinvModulePlatform": pm200fr20RinvModulePlatform,
       "pm200fr20RinvSwPlatform": pm200fr20RinvSwPlatform,
       "pm200fr20RinvGwPlatform": pm200fr20RinvGwPlatform,
       "pm200fr20download": pm200fr20download,
       "pm200fr20DwlOther": pm200fr20DwlOther,
       "pm200fr20DwlrestartProcess": pm200fr20DwlrestartProcess,
       "pm200fr20DwlWarmRestartProcessed": pm200fr20DwlWarmRestartProcessed,
       "pm200fr20DwlColdRestartProcessed": pm200fr20DwlColdRestartProcessed,
       "pm200fr20DwlswBanksUsed": pm200fr20DwlswBanksUsed,
       "pm200fr20DwlSwBank1Used": pm200fr20DwlSwBank1Used,
       "pm200fr20DwlSwBank2Used": pm200fr20DwlSwBank2Used,
       "pm200fr20DwlSwBank1Notempty": pm200fr20DwlSwBank1Notempty,
       "pm200fr20DwlSwBank2Notempty": pm200fr20DwlSwBank2Notempty,
       "pm200fr20DwlgwBanksUsed": pm200fr20DwlgwBanksUsed,
       "pm200fr20DwlGwBank1Used": pm200fr20DwlGwBank1Used,
       "pm200fr20DwlGwBank2Used": pm200fr20DwlGwBank2Used,
       "pm200fr20DwlGwBank3Used": pm200fr20DwlGwBank3Used,
       "pm200fr20DwlGwBank4Used": pm200fr20DwlGwBank4Used,
       "pm200fr20DwlGwBank1Notempty": pm200fr20DwlGwBank1Notempty,
       "pm200fr20DwlGwBank2Notempty": pm200fr20DwlGwBank2Notempty,
       "pm200fr20DwlGwBank3Notempty": pm200fr20DwlGwBank3Notempty,
       "pm200fr20DwlGwBank4Notempty": pm200fr20DwlGwBank4Notempty,
       "pm200fr20DwlClient": pm200fr20DwlClient,
       "pm200fr20DwlLine": pm200fr20DwlLine,
       "pm200fr20Config": pm200fr20Config,
       "pm200fr20CfgAccessCAisCsf": pm200fr20CfgAccessCAisCsf,
       "pm200fr20CfgClientcaiscsfTable": pm200fr20CfgClientcaiscsfTable,
       "pm200fr20CfgClientcaiscsfEntry": pm200fr20CfgClientcaiscsfEntry,
       "pm200fr20CfgClientcaiscsfIndex": pm200fr20CfgClientcaiscsfIndex,
       "pm200fr20CfgReservePortn": pm200fr20CfgReservePortn,
       "pm200fr20CfgStartup": pm200fr20CfgStartup,
       "pm200fr20CfgClientStartupTable": pm200fr20CfgClientStartupTable,
       "pm200fr20CfgClientStartupEntry": pm200fr20CfgClientStartupEntry,
       "pm200fr20CfgClientStartupIndex": pm200fr20CfgClientStartupIndex,
       "pm200fr20CfgSystConfPortPortn": pm200fr20CfgSystConfPortPortn,
       "pm200fr20CfgNetConfPortPortn": pm200fr20CfgNetConfPortPortn,
       "pm200fr20CfgOptionsPortPortn": pm200fr20CfgOptionsPortPortn,
       "pm200fr20CfgLineStartupTable": pm200fr20CfgLineStartupTable,
       "pm200fr20CfgLineStartupEntry": pm200fr20CfgLineStartupEntry,
       "pm200fr20CfgLineStartupIndex": pm200fr20CfgLineStartupIndex,
       "pm200fr20CfgSystConfLinePortn": pm200fr20CfgSystConfLinePortn,
       "pm200fr20CfgOptionsLinePortn": pm200fr20CfgOptionsLinePortn,
       "pm200fr20CfgXfpTable": pm200fr20CfgXfpTable,
       "pm200fr20CfgXfpEntry": pm200fr20CfgXfpEntry,
       "pm200fr20CfgXfpIndex": pm200fr20CfgXfpIndex,
       "pm200fr20CfgSystConfMsaLinePortn": pm200fr20CfgSystConfMsaLinePortn,
       "pm200fr20CfgLabels": pm200fr20CfgLabels,
       "pm200fr20CfgLabelclientTable": pm200fr20CfgLabelclientTable,
       "pm200fr20CfgLabelclientEntry": pm200fr20CfgLabelclientEntry,
       "pm200fr20CfgLabelclientIndex": pm200fr20CfgLabelclientIndex,
       "pm200fr20CfgLabelclientPortn": pm200fr20CfgLabelclientPortn,
       "pm200fr20CfgLabellineTable": pm200fr20CfgLabellineTable,
       "pm200fr20CfgLabellineEntry": pm200fr20CfgLabellineEntry,
       "pm200fr20CfgLabellineIndex": pm200fr20CfgLabellineIndex,
       "pm200fr20CfgLabellinePortn": pm200fr20CfgLabellinePortn,
       "pm200fr20CfgStartuptlh": pm200fr20CfgStartuptlh,
       "pm200fr20CfgOtxtlhTable": pm200fr20CfgOtxtlhTable,
       "pm200fr20CfgOtxtlhEntry": pm200fr20CfgOtxtlhEntry,
       "pm200fr20CfgOtxtlhIndex": pm200fr20CfgOtxtlhIndex,
       "pm200fr20CfgLinePwrLaserPortn": pm200fr20CfgLinePwrLaserPortn,
       "pm200fr20CfgLineFCurrentPortn": pm200fr20CfgLineFCurrentPortn,
       "pm200fr20CfgLineGridCurrentPortn": pm200fr20CfgLineGridCurrentPortn,
       "pm200fr20CfgFPortn": pm200fr20CfgFPortn,
       "pm200fr20CfgRxLineFCurrentPortn": pm200fr20CfgRxLineFCurrentPortn,
       "pm200fr20CfgOther": pm200fr20CfgOther,
       "pm200fr20tablemoduleOther": pm200fr20tablemoduleOther,
       "pm200fr20Cfgmode": pm200fr20Cfgmode,
       "pm200fr20CfgfanLowSpeedThreshold": pm200fr20CfgfanLowSpeedThreshold,
       "pm200fr20CfgfanHighSpeedThreshold": pm200fr20CfgfanHighSpeedThreshold,
       "pm200fr20CfgprotocolMode": pm200fr20CfgprotocolMode,
       "pm200fr20CfgStartuptablefive": pm200fr20CfgStartuptablefive,
       "pm200fr20CfgOtxtlhcapabilitiesTable": pm200fr20CfgOtxtlhcapabilitiesTable,
       "pm200fr20CfgOtxtlhcapabilitiesEntry": pm200fr20CfgOtxtlhcapabilitiesEntry,
       "pm200fr20CfgOtxtlhcapabilitiesIndex": pm200fr20CfgOtxtlhcapabilitiesIndex,
       "pm200fr20CfgComponentTypePortn": pm200fr20CfgComponentTypePortn,
       "pm200fr20CfgMiscellaneousPortn": pm200fr20CfgMiscellaneousPortn,
       "pm200fr20CfgFirstChannelPortn": pm200fr20CfgFirstChannelPortn,
       "pm200fr20CfgLastChannelPortn": pm200fr20CfgLastChannelPortn,
       "pm200fr20CfgGridPortn": pm200fr20CfgGridPortn,
       "pm200fr20CfgWriteConfiguration": pm200fr20CfgWriteConfiguration,
       "pm200fr20traps": pm200fr20traps,
       "pm200fr20trapPortNumber": pm200fr20trapPortNumber,
       "pm200fr20trapLineNumber": pm200fr20trapLineNumber,
       "pm200fr20trapBoardNumber": pm200fr20trapBoardNumber,
       "pm200fr20LineTrapNotUrgentGoesOn": pm200fr20LineTrapNotUrgentGoesOn,
       "pm200fr20LineTrapNotUrgentGoesOff": pm200fr20LineTrapNotUrgentGoesOff,
       "pm200fr20LineTrapUrgentGoesOn": pm200fr20LineTrapUrgentGoesOn,
       "pm200fr20LineTrapUrgentGoesOff": pm200fr20LineTrapUrgentGoesOff,
       "pm200fr20LineTrapCritGoesOn": pm200fr20LineTrapCritGoesOn,
       "pm200fr20LineTrapCritGoesOff": pm200fr20LineTrapCritGoesOff,
       "pm200fr20ClientTrapNotUrgentGoesOn": pm200fr20ClientTrapNotUrgentGoesOn,
       "pm200fr20ClientTrapNotUrgentGoesOff": pm200fr20ClientTrapNotUrgentGoesOff,
       "pm200fr20ClientTrapUrgentGoesOn": pm200fr20ClientTrapUrgentGoesOn,
       "pm200fr20ClientTrapUrgentGoesOff": pm200fr20ClientTrapUrgentGoesOff,
       "pm200fr20ClientTrapCritGoesOn": pm200fr20ClientTrapCritGoesOn,
       "pm200fr20ClientTrapCritGoesOff": pm200fr20ClientTrapCritGoesOff,
       "pm200fr20PowerTrapUrgentGoesOn": pm200fr20PowerTrapUrgentGoesOn,
       "pm200fr20PowerTrapUrgentGoesOff": pm200fr20PowerTrapUrgentGoesOff,
       "pm200fr20Monitoring": pm200fr20Monitoring,
       "pm200fr20MonOther": pm200fr20MonOther,
       "pm200fr20MonRmon": pm200fr20MonRmon,
       "pm200fr20MonClient": pm200fr20MonClient,
       "pm200fr20MonClientRmonCounter": pm200fr20MonClientRmonCounter,
       "pm200fr20MonupRmonBytesCounterClientInputTable": pm200fr20MonupRmonBytesCounterClientInputTable,
       "pm200fr20MonupRmonBytesCounterClientInputEntry": pm200fr20MonupRmonBytesCounterClientInputEntry,
       "pm200fr20MonupRmonBytesCounterClientInputIndex": pm200fr20MonupRmonBytesCounterClientInputIndex,
       "pm200fr20MonupRmonBytesCounterClientInputValuePortn": pm200fr20MonupRmonBytesCounterClientInputValuePortn,
       "pm200fr20MonupRmonBytesCounterClientInputErrorPortn": pm200fr20MonupRmonBytesCounterClientInputErrorPortn,
       "pm200fr20MonupRmonBytesCounterClientInputOverloadPortn": pm200fr20MonupRmonBytesCounterClientInputOverloadPortn,
       "pm200fr20MonupRmonCrcErrorsCounterClientInputTable": pm200fr20MonupRmonCrcErrorsCounterClientInputTable,
       "pm200fr20MonupRmonCrcErrorsCounterClientInputEntry": pm200fr20MonupRmonCrcErrorsCounterClientInputEntry,
       "pm200fr20MonupRmonCrcErrorsCounterClientInputIndex": pm200fr20MonupRmonCrcErrorsCounterClientInputIndex,
       "pm200fr20MonupRmonCrcErrorsCounterClientInputValuePortn": pm200fr20MonupRmonCrcErrorsCounterClientInputValuePortn,
       "pm200fr20MonupRmonCrcErrorsCounterClientInputErrorPortn": pm200fr20MonupRmonCrcErrorsCounterClientInputErrorPortn,
       "pm200fr20MonupRmonCrcErrorsCounterClientInputOverloadPortn": pm200fr20MonupRmonCrcErrorsCounterClientInputOverloadPortn,
       "pm200fr20MonupRmonPacketsCounterClientInputTable": pm200fr20MonupRmonPacketsCounterClientInputTable,
       "pm200fr20MonupRmonPacketsCounterClientInputEntry": pm200fr20MonupRmonPacketsCounterClientInputEntry,
       "pm200fr20MonupRmonPacketsCounterClientInputIndex": pm200fr20MonupRmonPacketsCounterClientInputIndex,
       "pm200fr20MonupRmonPacketsCounterClientInputValuePortn": pm200fr20MonupRmonPacketsCounterClientInputValuePortn,
       "pm200fr20MonupRmonPacketsCounterClientInputErrorPortn": pm200fr20MonupRmonPacketsCounterClientInputErrorPortn,
       "pm200fr20MonupRmonPacketsCounterClientInputOverloadPortn": pm200fr20MonupRmonPacketsCounterClientInputOverloadPortn,
       "pm200fr20MonupRmonBroadcastCounterClientInputTable": pm200fr20MonupRmonBroadcastCounterClientInputTable,
       "pm200fr20MonupRmonBroadcastCounterClientInputEntry": pm200fr20MonupRmonBroadcastCounterClientInputEntry,
       "pm200fr20MonupRmonBroadcastCounterClientInputIndex": pm200fr20MonupRmonBroadcastCounterClientInputIndex,
       "pm200fr20MonupRmonBroadcastCounterClientInputValuePortn": pm200fr20MonupRmonBroadcastCounterClientInputValuePortn,
       "pm200fr20MonupRmonBroadcastCounterClientInputErrorPortn": pm200fr20MonupRmonBroadcastCounterClientInputErrorPortn,
       "pm200fr20MonupRmonBroadcastCounterClientInputOverloadPortn": pm200fr20MonupRmonBroadcastCounterClientInputOverloadPortn,
       "pm200fr20MonupRmonMulticastCounterClientInputTable": pm200fr20MonupRmonMulticastCounterClientInputTable,
       "pm200fr20MonupRmonMulticastCounterClientInputEntry": pm200fr20MonupRmonMulticastCounterClientInputEntry,
       "pm200fr20MonupRmonMulticastCounterClientInputIndex": pm200fr20MonupRmonMulticastCounterClientInputIndex,
       "pm200fr20MonupRmonMulticastCounterClientInputValuePortn": pm200fr20MonupRmonMulticastCounterClientInputValuePortn,
       "pm200fr20MonupRmonMulticastCounterClientInputErrorPortn": pm200fr20MonupRmonMulticastCounterClientInputErrorPortn,
       "pm200fr20MonupRmonMulticastCounterClientInputOverloadPortn": pm200fr20MonupRmonMulticastCounterClientInputOverloadPortn,
       "pm200fr20MonupRmonPauseFrameCounterClientInputTable": pm200fr20MonupRmonPauseFrameCounterClientInputTable,
       "pm200fr20MonupRmonPauseFrameCounterClientInputEntry": pm200fr20MonupRmonPauseFrameCounterClientInputEntry,
       "pm200fr20MonupRmonPauseFrameCounterClientInputIndex": pm200fr20MonupRmonPauseFrameCounterClientInputIndex,
       "pm200fr20MonupRmonPauseFrameCounterClientInputValuePortn": pm200fr20MonupRmonPauseFrameCounterClientInputValuePortn,
       "pm200fr20MonupRmonPauseFrameCounterClientInputErrorPortn": pm200fr20MonupRmonPauseFrameCounterClientInputErrorPortn,
       "pm200fr20MonupRmonPauseFrameCounterClientInputOverloadPortn": pm200fr20MonupRmonPauseFrameCounterClientInputOverloadPortn,
       "pm200fr20MonupRmonUnicastCounterClientInputTable": pm200fr20MonupRmonUnicastCounterClientInputTable,
       "pm200fr20MonupRmonUnicastCounterClientInputEntry": pm200fr20MonupRmonUnicastCounterClientInputEntry,
       "pm200fr20MonupRmonUnicastCounterClientInputIndex": pm200fr20MonupRmonUnicastCounterClientInputIndex,
       "pm200fr20MonupRmonUnicastCounterClientInputValuePortn": pm200fr20MonupRmonUnicastCounterClientInputValuePortn,
       "pm200fr20MonupRmonUnicastCounterClientInputErrorPortn": pm200fr20MonupRmonUnicastCounterClientInputErrorPortn,
       "pm200fr20MonupRmonUnicastCounterClientInputOverloadPortn": pm200fr20MonupRmonUnicastCounterClientInputOverloadPortn,
       "pm200fr20MonupRmonNonunicastCounterClientInputTable": pm200fr20MonupRmonNonunicastCounterClientInputTable,
       "pm200fr20MonupRmonNonunicastCounterClientInputEntry": pm200fr20MonupRmonNonunicastCounterClientInputEntry,
       "pm200fr20MonupRmonNonunicastCounterClientInputIndex": pm200fr20MonupRmonNonunicastCounterClientInputIndex,
       "pm200fr20MonupRmonNonunicastCounterClientInputValuePortn": pm200fr20MonupRmonNonunicastCounterClientInputValuePortn,
       "pm200fr20MonupRmonNonunicastCounterClientInputErrorPortn": pm200fr20MonupRmonNonunicastCounterClientInputErrorPortn,
       "pm200fr20MonupRmonNonunicastCounterClientInputOverloadPortn": pm200fr20MonupRmonNonunicastCounterClientInputOverloadPortn,
       "pm200fr20MondownRmonBytesCounterClientOutputTable": pm200fr20MondownRmonBytesCounterClientOutputTable,
       "pm200fr20MondownRmonBytesCounterClientOutputEntry": pm200fr20MondownRmonBytesCounterClientOutputEntry,
       "pm200fr20MondownRmonBytesCounterClientOutputIndex": pm200fr20MondownRmonBytesCounterClientOutputIndex,
       "pm200fr20MondownRmonBytesCounterClientOutputValuePortn": pm200fr20MondownRmonBytesCounterClientOutputValuePortn,
       "pm200fr20MondownRmonBytesCounterClientOutputErrorPortn": pm200fr20MondownRmonBytesCounterClientOutputErrorPortn,
       "pm200fr20MondownRmonBytesCounterClientOutputOverloadPortn": pm200fr20MondownRmonBytesCounterClientOutputOverloadPortn,
       "pm200fr20MondownRmonCrcErrorsCounterClientOutputTable": pm200fr20MondownRmonCrcErrorsCounterClientOutputTable,
       "pm200fr20MondownRmonCrcErrorsCounterClientOutputEntry": pm200fr20MondownRmonCrcErrorsCounterClientOutputEntry,
       "pm200fr20MondownRmonCrcErrorsCounterClientOutputIndex": pm200fr20MondownRmonCrcErrorsCounterClientOutputIndex,
       "pm200fr20MondownRmonCrcErrorsCounterClientOutputValuePortn": pm200fr20MondownRmonCrcErrorsCounterClientOutputValuePortn,
       "pm200fr20MondownRmonCrcErrorsCounterClientOutputErrorPortn": pm200fr20MondownRmonCrcErrorsCounterClientOutputErrorPortn,
       "pm200fr20MondownRmonCrcErrorsCounterClientOutputOverloadPortn": pm200fr20MondownRmonCrcErrorsCounterClientOutputOverloadPortn,
       "pm200fr20MondownRmonPacketsCounterClientOutputTable": pm200fr20MondownRmonPacketsCounterClientOutputTable,
       "pm200fr20MondownRmonPacketsCounterClientOutputEntry": pm200fr20MondownRmonPacketsCounterClientOutputEntry,
       "pm200fr20MondownRmonPacketsCounterClientOutputIndex": pm200fr20MondownRmonPacketsCounterClientOutputIndex,
       "pm200fr20MondownRmonPacketsCounterClientOutputValuePortn": pm200fr20MondownRmonPacketsCounterClientOutputValuePortn,
       "pm200fr20MondownRmonPacketsCounterClientOutputErrorPortn": pm200fr20MondownRmonPacketsCounterClientOutputErrorPortn,
       "pm200fr20MondownRmonPacketsCounterClientOutputOverloadPortn": pm200fr20MondownRmonPacketsCounterClientOutputOverloadPortn,
       "pm200fr20MondownRmonBroadcastCounterClientOutputTable": pm200fr20MondownRmonBroadcastCounterClientOutputTable,
       "pm200fr20MondownRmonBroadcastCounterClientOutputEntry": pm200fr20MondownRmonBroadcastCounterClientOutputEntry,
       "pm200fr20MondownRmonBroadcastCounterClientOutputIndex": pm200fr20MondownRmonBroadcastCounterClientOutputIndex,
       "pm200fr20MondownRmonBroadcastCounterClientOutputValuePortn": pm200fr20MondownRmonBroadcastCounterClientOutputValuePortn,
       "pm200fr20MondownRmonBroadcastCounterClientOutputErrorPortn": pm200fr20MondownRmonBroadcastCounterClientOutputErrorPortn,
       "pm200fr20MondownRmonBroadcastCounterClientOutputOverloadPortn": pm200fr20MondownRmonBroadcastCounterClientOutputOverloadPortn,
       "pm200fr20MondownRmonMulticastCounterClientOutputTable": pm200fr20MondownRmonMulticastCounterClientOutputTable,
       "pm200fr20MondownRmonMulticastCounterClientOutputEntry": pm200fr20MondownRmonMulticastCounterClientOutputEntry,
       "pm200fr20MondownRmonMulticastCounterClientOutputIndex": pm200fr20MondownRmonMulticastCounterClientOutputIndex,
       "pm200fr20MondownRmonMulticastCounterClientOutputValuePortn": pm200fr20MondownRmonMulticastCounterClientOutputValuePortn,
       "pm200fr20MondownRmonMulticastCounterClientOutputErrorPortn": pm200fr20MondownRmonMulticastCounterClientOutputErrorPortn,
       "pm200fr20MondownRmonMulticastCounterClientOutputOverloadPortn": pm200fr20MondownRmonMulticastCounterClientOutputOverloadPortn,
       "pm200fr20MondownRmonPauseFrameCounterClientOutputTable": pm200fr20MondownRmonPauseFrameCounterClientOutputTable,
       "pm200fr20MondownRmonPauseFrameCounterClientOutputEntry": pm200fr20MondownRmonPauseFrameCounterClientOutputEntry,
       "pm200fr20MondownRmonPauseFrameCounterClientOutputIndex": pm200fr20MondownRmonPauseFrameCounterClientOutputIndex,
       "pm200fr20MondownRmonPauseFrameCounterClientOutputValuePortn": pm200fr20MondownRmonPauseFrameCounterClientOutputValuePortn,
       "pm200fr20MondownRmonPauseFrameCounterClientOutputErrorPortn": pm200fr20MondownRmonPauseFrameCounterClientOutputErrorPortn,
       "pm200fr20MondownRmonPauseFrameCounterClientOutputOverloadPortn": pm200fr20MondownRmonPauseFrameCounterClientOutputOverloadPortn,
       "pm200fr20MondownRmonUnicastCounterClientOutputTable": pm200fr20MondownRmonUnicastCounterClientOutputTable,
       "pm200fr20MondownRmonUnicastCounterClientOutputEntry": pm200fr20MondownRmonUnicastCounterClientOutputEntry,
       "pm200fr20MondownRmonUnicastCounterClientOutputIndex": pm200fr20MondownRmonUnicastCounterClientOutputIndex,
       "pm200fr20MondownRmonUnicastCounterClientOutputValuePortn": pm200fr20MondownRmonUnicastCounterClientOutputValuePortn,
       "pm200fr20MondownRmonUnicastCounterClientOutputErrorPortn": pm200fr20MondownRmonUnicastCounterClientOutputErrorPortn,
       "pm200fr20MondownRmonUnicastCounterClientOutputOverloadPortn": pm200fr20MondownRmonUnicastCounterClientOutputOverloadPortn,
       "pm200fr20MondownRmonNonunicastCounterClientOutputTable": pm200fr20MondownRmonNonunicastCounterClientOutputTable,
       "pm200fr20MondownRmonNonunicastCounterClientOutputEntry": pm200fr20MondownRmonNonunicastCounterClientOutputEntry,
       "pm200fr20MondownRmonNonunicastCounterClientOutputIndex": pm200fr20MondownRmonNonunicastCounterClientOutputIndex,
       "pm200fr20MondownRmonNonunicastCounterClientOutputValuePortn": pm200fr20MondownRmonNonunicastCounterClientOutputValuePortn,
       "pm200fr20MondownRmonNonunicastCounterClientOutputErrorPortn": pm200fr20MondownRmonNonunicastCounterClientOutputErrorPortn,
       "pm200fr20MondownRmonNonunicastCounterClientOutputOverloadPortn": pm200fr20MondownRmonNonunicastCounterClientOutputOverloadPortn,
       "pm200fr20MonPerfOther": pm200fr20MonPerfOther,
       "pm200fr20MonPerfSync": pm200fr20MonPerfSync,
       "pm200fr20PerfEnable": pm200fr20PerfEnable,
       "pm200fr20Perf15minSync": pm200fr20Perf15minSync,
       "pm200fr20Perf24hSync": pm200fr20Perf24hSync,
       "pm200fr20MonPerfTimeStamp": pm200fr20MonPerfTimeStamp,
       "pm200fr20Perf15MinShort": pm200fr20Perf15MinShort,
       "pm200fr20Perf15MinLong": pm200fr20Perf15MinLong,
       "pm200fr20Perf24HoursShort": pm200fr20Perf24HoursShort,
       "pm200fr20Perf24HoursLong": pm200fr20Perf24HoursLong,
       "pm200fr20PerfCurrent15MinElapsedTime": pm200fr20PerfCurrent15MinElapsedTime,
       "pm200fr20PerfCurrent24HoursElapsedTime": pm200fr20PerfCurrent24HoursElapsedTime,
       "pm200fr20MonPerfClient": pm200fr20MonPerfClient,
       "pm200fr20PerfTelecomInputClientCurrent15StatTable": pm200fr20PerfTelecomInputClientCurrent15StatTable,
       "pm200fr20PerfTelecomInputClientCurrent15StatEntry": pm200fr20PerfTelecomInputClientCurrent15StatEntry,
       "pm200fr20PerfTelecomInputClientCurrent15StatIndex": pm200fr20PerfTelecomInputClientCurrent15StatIndex,
       "pm200fr20PerfTelecomInputClientCurrent15StatInvCvPortn": pm200fr20PerfTelecomInputClientCurrent15StatInvCvPortn,
       "pm200fr20PerfTelecomInputClientCurrent15StatCvValuePortn": pm200fr20PerfTelecomInputClientCurrent15StatCvValuePortn,
       "pm200fr20PerfTelecomInputClientCurrent15StatInvEsPortn": pm200fr20PerfTelecomInputClientCurrent15StatInvEsPortn,
       "pm200fr20PerfTelecomInputClientCurrent15StatEsValuePortn": pm200fr20PerfTelecomInputClientCurrent15StatEsValuePortn,
       "pm200fr20PerfTelecomInputClientCurrent15StatInvSesPortn": pm200fr20PerfTelecomInputClientCurrent15StatInvSesPortn,
       "pm200fr20PerfTelecomInputClientCurrent15StatSesValuePortn": pm200fr20PerfTelecomInputClientCurrent15StatSesValuePortn,
       "pm200fr20PerfTelecomInputClientCurrent15StatInvSefsPortn": pm200fr20PerfTelecomInputClientCurrent15StatInvSefsPortn,
       "pm200fr20PerfTelecomInputClientCurrent15StatSefsValuePortn": pm200fr20PerfTelecomInputClientCurrent15StatSefsValuePortn,
       "pm200fr20PerfTelecomInputClientCurrent15StatInvUasPortn": pm200fr20PerfTelecomInputClientCurrent15StatInvUasPortn,
       "pm200fr20PerfTelecomInputClientCurrent15StatUasValuePortn": pm200fr20PerfTelecomInputClientCurrent15StatUasValuePortn,
       "pm200fr20PerfTelecomInputClientPast15StatHistoryPort1Table": pm200fr20PerfTelecomInputClientPast15StatHistoryPort1Table,
       "pm200fr20PerfTelecomInputClientPast15StatHistoryPort1Entry": pm200fr20PerfTelecomInputClientPast15StatHistoryPort1Entry,
       "pm200fr20PerfTelecomInputClientPast15StatHistoryPort1Index": pm200fr20PerfTelecomInputClientPast15StatHistoryPort1Index,
       "pm200fr20PerfTelecomInputClientPast15StatHistoryInvCvPort1": pm200fr20PerfTelecomInputClientPast15StatHistoryInvCvPort1,
       "pm200fr20PerfTelecomInputClientPast15StatHistoryCvValuePort1": pm200fr20PerfTelecomInputClientPast15StatHistoryCvValuePort1,
       "pm200fr20PerfTelecomInputClientPast15StatHistoryInvEsPort1": pm200fr20PerfTelecomInputClientPast15StatHistoryInvEsPort1,
       "pm200fr20PerfTelecomInputClientPast15StatHistoryEsValuePort1": pm200fr20PerfTelecomInputClientPast15StatHistoryEsValuePort1,
       "pm200fr20PerfTelecomInputClientPast15StatHistoryInvSesPort1": pm200fr20PerfTelecomInputClientPast15StatHistoryInvSesPort1,
       "pm200fr20PerfTelecomInputClientPast15StatHistorySesValuePort1": pm200fr20PerfTelecomInputClientPast15StatHistorySesValuePort1,
       "pm200fr20PerfTelecomInputClientPast15StatHistoryInvSefsPort1": pm200fr20PerfTelecomInputClientPast15StatHistoryInvSefsPort1,
       "pm200fr20PerfTelecomInputClientPast15StatHistorySefsValuePort1": pm200fr20PerfTelecomInputClientPast15StatHistorySefsValuePort1,
       "pm200fr20PerfTelecomInputClientPast15StatHistoryInvUasPort1": pm200fr20PerfTelecomInputClientPast15StatHistoryInvUasPort1,
       "pm200fr20PerfTelecomInputClientPast15StatHistoryUasValuePort1": pm200fr20PerfTelecomInputClientPast15StatHistoryUasValuePort1,
       "pm200fr20PerfTelecomInputClientCurrent24StatTable": pm200fr20PerfTelecomInputClientCurrent24StatTable,
       "pm200fr20PerfTelecomInputClientCurrent24StatEntry": pm200fr20PerfTelecomInputClientCurrent24StatEntry,
       "pm200fr20PerfTelecomInputClientCurrent24StatIndex": pm200fr20PerfTelecomInputClientCurrent24StatIndex,
       "pm200fr20PerfTelecomInputClientCurrent24StatInvCvPortn": pm200fr20PerfTelecomInputClientCurrent24StatInvCvPortn,
       "pm200fr20PerfTelecomInputClientCurrent24StatCvValuePortn": pm200fr20PerfTelecomInputClientCurrent24StatCvValuePortn,
       "pm200fr20PerfTelecomInputClientCurrent24StatInvEsPortn": pm200fr20PerfTelecomInputClientCurrent24StatInvEsPortn,
       "pm200fr20PerfTelecomInputClientCurrent24StatEsValuePortn": pm200fr20PerfTelecomInputClientCurrent24StatEsValuePortn,
       "pm200fr20PerfTelecomInputClientCurrent24StatInvSesPortn": pm200fr20PerfTelecomInputClientCurrent24StatInvSesPortn,
       "pm200fr20PerfTelecomInputClientCurrent24StatSesValuePortn": pm200fr20PerfTelecomInputClientCurrent24StatSesValuePortn,
       "pm200fr20PerfTelecomInputClientCurrent24StatInvSefsPortn": pm200fr20PerfTelecomInputClientCurrent24StatInvSefsPortn,
       "pm200fr20PerfTelecomInputClientCurrent24StatSefsValuePortn": pm200fr20PerfTelecomInputClientCurrent24StatSefsValuePortn,
       "pm200fr20PerfTelecomInputClientCurrent24StatInvUasPortn": pm200fr20PerfTelecomInputClientCurrent24StatInvUasPortn,
       "pm200fr20PerfTelecomInputClientCurrent24StatUasValuePortn": pm200fr20PerfTelecomInputClientCurrent24StatUasValuePortn,
       "pm200fr20PerfTelecomInputClientPast24StatHistoryPort1Table": pm200fr20PerfTelecomInputClientPast24StatHistoryPort1Table,
       "pm200fr20PerfTelecomInputClientPast24StatHistoryPort1Entry": pm200fr20PerfTelecomInputClientPast24StatHistoryPort1Entry,
       "pm200fr20PerfTelecomInputClientPast24StatHistoryPort1Index": pm200fr20PerfTelecomInputClientPast24StatHistoryPort1Index,
       "pm200fr20PerfTelecomInputClientPast24StatHistoryInvCvPort1": pm200fr20PerfTelecomInputClientPast24StatHistoryInvCvPort1,
       "pm200fr20PerfTelecomInputClientPast24StatHistoryCvValuePort1": pm200fr20PerfTelecomInputClientPast24StatHistoryCvValuePort1,
       "pm200fr20PerfTelecomInputClientPast24StatHistoryInvEsPort1": pm200fr20PerfTelecomInputClientPast24StatHistoryInvEsPort1,
       "pm200fr20PerfTelecomInputClientPast24StatHistoryEsValuePort1": pm200fr20PerfTelecomInputClientPast24StatHistoryEsValuePort1,
       "pm200fr20PerfTelecomInputClientPast24StatHistoryInvSesPort1": pm200fr20PerfTelecomInputClientPast24StatHistoryInvSesPort1,
       "pm200fr20PerfTelecomInputClientPast24StatHistorySesValuePort1": pm200fr20PerfTelecomInputClientPast24StatHistorySesValuePort1,
       "pm200fr20PerfTelecomInputClientPast24StatHistoryInvSefsPort1": pm200fr20PerfTelecomInputClientPast24StatHistoryInvSefsPort1,
       "pm200fr20PerfTelecomInputClientPast24StatHistorySefsValuePort1": pm200fr20PerfTelecomInputClientPast24StatHistorySefsValuePort1,
       "pm200fr20PerfTelecomInputClientPast24StatHistoryInvUasPort1": pm200fr20PerfTelecomInputClientPast24StatHistoryInvUasPort1,
       "pm200fr20PerfTelecomInputClientPast24StatHistoryUasValuePort1": pm200fr20PerfTelecomInputClientPast24StatHistoryUasValuePort1,
       "pm200fr20PerfTelecomOutputClientCurrent15StatTable": pm200fr20PerfTelecomOutputClientCurrent15StatTable,
       "pm200fr20PerfTelecomOutputClientCurrent15StatEntry": pm200fr20PerfTelecomOutputClientCurrent15StatEntry,
       "pm200fr20PerfTelecomOutputClientCurrent15StatIndex": pm200fr20PerfTelecomOutputClientCurrent15StatIndex,
       "pm200fr20PerfTelecomOutputClientCurrent15StatInvCvPortn": pm200fr20PerfTelecomOutputClientCurrent15StatInvCvPortn,
       "pm200fr20PerfTelecomOutputClientCurrent15StatCvValuePortn": pm200fr20PerfTelecomOutputClientCurrent15StatCvValuePortn,
       "pm200fr20PerfTelecomOutputClientCurrent15StatInvEsPortn": pm200fr20PerfTelecomOutputClientCurrent15StatInvEsPortn,
       "pm200fr20PerfTelecomOutputClientCurrent15StatEsValuePortn": pm200fr20PerfTelecomOutputClientCurrent15StatEsValuePortn,
       "pm200fr20PerfTelecomOutputClientCurrent15StatInvSesPortn": pm200fr20PerfTelecomOutputClientCurrent15StatInvSesPortn,
       "pm200fr20PerfTelecomOutputClientCurrent15StatSesValuePortn": pm200fr20PerfTelecomOutputClientCurrent15StatSesValuePortn,
       "pm200fr20PerfTelecomOutputClientCurrent15StatInvSefsPortn": pm200fr20PerfTelecomOutputClientCurrent15StatInvSefsPortn,
       "pm200fr20PerfTelecomOutputClientCurrent15StatSefsValuePortn": pm200fr20PerfTelecomOutputClientCurrent15StatSefsValuePortn,
       "pm200fr20PerfTelecomOutputClientCurrent15StatInvUasPortn": pm200fr20PerfTelecomOutputClientCurrent15StatInvUasPortn,
       "pm200fr20PerfTelecomOutputClientCurrent15StatUasValuePortn": pm200fr20PerfTelecomOutputClientCurrent15StatUasValuePortn,
       "pm200fr20PerfTelecomOutputClientPast15StatHistoryPort1Table": pm200fr20PerfTelecomOutputClientPast15StatHistoryPort1Table,
       "pm200fr20PerfTelecomOutputClientPast15StatHistoryPort1Entry": pm200fr20PerfTelecomOutputClientPast15StatHistoryPort1Entry,
       "pm200fr20PerfTelecomOutputClientPast15StatHistoryPort1Index": pm200fr20PerfTelecomOutputClientPast15StatHistoryPort1Index,
       "pm200fr20PerfTelecomOutputClientPast15StatHistoryInvCvPort1": pm200fr20PerfTelecomOutputClientPast15StatHistoryInvCvPort1,
       "pm200fr20PerfTelecomOutputClientPast15StatHistoryCvValuePort1": pm200fr20PerfTelecomOutputClientPast15StatHistoryCvValuePort1,
       "pm200fr20PerfTelecomOutputClientPast15StatHistoryInvEsPort1": pm200fr20PerfTelecomOutputClientPast15StatHistoryInvEsPort1,
       "pm200fr20PerfTelecomOutputClientPast15StatHistoryEsValuePort1": pm200fr20PerfTelecomOutputClientPast15StatHistoryEsValuePort1,
       "pm200fr20PerfTelecomOutputClientPast15StatHistoryInvSesPort1": pm200fr20PerfTelecomOutputClientPast15StatHistoryInvSesPort1,
       "pm200fr20PerfTelecomOutputClientPast15StatHistorySesValuePort1": pm200fr20PerfTelecomOutputClientPast15StatHistorySesValuePort1,
       "pm200fr20PerfTelecomOutputClientPast15StatHistoryInvSefsPort1": pm200fr20PerfTelecomOutputClientPast15StatHistoryInvSefsPort1,
       "pm200fr20PerfTelecomOutputClientPast15StatHistorySefsValuePort1": pm200fr20PerfTelecomOutputClientPast15StatHistorySefsValuePort1,
       "pm200fr20PerfTelecomOutputClientPast15StatHistoryInvUasPort1": pm200fr20PerfTelecomOutputClientPast15StatHistoryInvUasPort1,
       "pm200fr20PerfTelecomOutputClientPast15StatHistoryUasValuePort1": pm200fr20PerfTelecomOutputClientPast15StatHistoryUasValuePort1,
       "pm200fr20PerfTelecomOutputClientCurrent24StatTable": pm200fr20PerfTelecomOutputClientCurrent24StatTable,
       "pm200fr20PerfTelecomOutputClientCurrent24StatEntry": pm200fr20PerfTelecomOutputClientCurrent24StatEntry,
       "pm200fr20PerfTelecomOutputClientCurrent24StatIndex": pm200fr20PerfTelecomOutputClientCurrent24StatIndex,
       "pm200fr20PerfTelecomOutputClientCurrent24StatInvCvPortn": pm200fr20PerfTelecomOutputClientCurrent24StatInvCvPortn,
       "pm200fr20PerfTelecomOutputClientCurrent24StatCvValuePortn": pm200fr20PerfTelecomOutputClientCurrent24StatCvValuePortn,
       "pm200fr20PerfTelecomOutputClientCurrent24StatInvEsPortn": pm200fr20PerfTelecomOutputClientCurrent24StatInvEsPortn,
       "pm200fr20PerfTelecomOutputClientCurrent24StatEsValuePortn": pm200fr20PerfTelecomOutputClientCurrent24StatEsValuePortn,
       "pm200fr20PerfTelecomOutputClientCurrent24StatInvSesPortn": pm200fr20PerfTelecomOutputClientCurrent24StatInvSesPortn,
       "pm200fr20PerfTelecomOutputClientCurrent24StatSesValuePortn": pm200fr20PerfTelecomOutputClientCurrent24StatSesValuePortn,
       "pm200fr20PerfTelecomOutputClientCurrent24StatInvSefsPortn": pm200fr20PerfTelecomOutputClientCurrent24StatInvSefsPortn,
       "pm200fr20PerfTelecomOutputClientCurrent24StatSefsValuePortn": pm200fr20PerfTelecomOutputClientCurrent24StatSefsValuePortn,
       "pm200fr20PerfTelecomOutputClientCurrent24StatInvUasPortn": pm200fr20PerfTelecomOutputClientCurrent24StatInvUasPortn,
       "pm200fr20PerfTelecomOutputClientCurrent24StatUasValuePortn": pm200fr20PerfTelecomOutputClientCurrent24StatUasValuePortn,
       "pm200fr20PerfTelecomOutputClientPast24StatHistoryPort1Table": pm200fr20PerfTelecomOutputClientPast24StatHistoryPort1Table,
       "pm200fr20PerfTelecomOutputClientPast24StatHistoryPort1Entry": pm200fr20PerfTelecomOutputClientPast24StatHistoryPort1Entry,
       "pm200fr20PerfTelecomOutputClientPast24StatHistoryPort1Index": pm200fr20PerfTelecomOutputClientPast24StatHistoryPort1Index,
       "pm200fr20PerfTelecomOutputClientPast24StatHistoryInvCvPort1": pm200fr20PerfTelecomOutputClientPast24StatHistoryInvCvPort1,
       "pm200fr20PerfTelecomOutputClientPast24StatHistoryCvValuePort1": pm200fr20PerfTelecomOutputClientPast24StatHistoryCvValuePort1,
       "pm200fr20PerfTelecomOutputClientPast24StatHistoryInvEsPort1": pm200fr20PerfTelecomOutputClientPast24StatHistoryInvEsPort1,
       "pm200fr20PerfTelecomOutputClientPast24StatHistoryEsValuePort1": pm200fr20PerfTelecomOutputClientPast24StatHistoryEsValuePort1,
       "pm200fr20PerfTelecomOutputClientPast24StatHistoryInvSesPort1": pm200fr20PerfTelecomOutputClientPast24StatHistoryInvSesPort1,
       "pm200fr20PerfTelecomOutputClientPast24StatHistorySesValuePort1": pm200fr20PerfTelecomOutputClientPast24StatHistorySesValuePort1,
       "pm200fr20PerfTelecomOutputClientPast24StatHistoryInvSefsPort1": pm200fr20PerfTelecomOutputClientPast24StatHistoryInvSefsPort1,
       "pm200fr20PerfTelecomOutputClientPast24StatHistorySefsValuePort1": pm200fr20PerfTelecomOutputClientPast24StatHistorySefsValuePort1,
       "pm200fr20PerfTelecomOutputClientPast24StatHistoryInvUasPort1": pm200fr20PerfTelecomOutputClientPast24StatHistoryInvUasPort1,
       "pm200fr20PerfTelecomOutputClientPast24StatHistoryUasValuePort1": pm200fr20PerfTelecomOutputClientPast24StatHistoryUasValuePort1,
       "pm200fr20PerfDatacomClientCurrent15StatTable": pm200fr20PerfDatacomClientCurrent15StatTable,
       "pm200fr20PerfDatacomClientCurrent15StatEntry": pm200fr20PerfDatacomClientCurrent15StatEntry,
       "pm200fr20PerfDatacomClientCurrent15StatIndex": pm200fr20PerfDatacomClientCurrent15StatIndex,
       "pm200fr20perfdatacomclientCurrent15StatInCrcCountInvPortn": pm200fr20perfdatacomclientCurrent15StatInCrcCountInvPortn,
       "pm200fr20perfdatacomclientCurrent15StatInCrcCountPortn": pm200fr20perfdatacomclientCurrent15StatInCrcCountPortn,
       "pm200fr20perfdatacomclientCurrent15StatInPacketCountInvPortn": pm200fr20perfdatacomclientCurrent15StatInPacketCountInvPortn,
       "pm200fr20perfdatacomclientCurrent15StatInPacketCountPortn": pm200fr20perfdatacomclientCurrent15StatInPacketCountPortn,
       "pm200fr20perfdatacomclientCurrent15StatOutCrcCountInvPortn": pm200fr20perfdatacomclientCurrent15StatOutCrcCountInvPortn,
       "pm200fr20perfdatacomclientCurrent15StatOutCrcCountPortn": pm200fr20perfdatacomclientCurrent15StatOutCrcCountPortn,
       "pm200fr20perfdatacomclientCurrent15StatOutPacketCountInvPortn": pm200fr20perfdatacomclientCurrent15StatOutPacketCountInvPortn,
       "pm200fr20perfdatacomclientCurrent15StatOutPacketCountPortn": pm200fr20perfdatacomclientCurrent15StatOutPacketCountPortn,
       "pm200fr20PerfDatacomClientPast15StatHistoryPort1Table": pm200fr20PerfDatacomClientPast15StatHistoryPort1Table,
       "pm200fr20PerfDatacomClientPast15StatHistoryPort1Entry": pm200fr20PerfDatacomClientPast15StatHistoryPort1Entry,
       "pm200fr20PerfDatacomClientPast15StatHistoryPort1Index": pm200fr20PerfDatacomClientPast15StatHistoryPort1Index,
       "pm200fr20perfdatacomclientPast15StatInCrcCountInvPort1": pm200fr20perfdatacomclientPast15StatInCrcCountInvPort1,
       "pm200fr20perfdatacomclientPast15StatInCrcCountPort1": pm200fr20perfdatacomclientPast15StatInCrcCountPort1,
       "pm200fr20perfdatacomclientPast15StatInPacketCountInvPort1": pm200fr20perfdatacomclientPast15StatInPacketCountInvPort1,
       "pm200fr20perfdatacomclientPast15StatInPacketCountPort1": pm200fr20perfdatacomclientPast15StatInPacketCountPort1,
       "pm200fr20perfdatacomclientPast15StatOutCrcCountInvPort1": pm200fr20perfdatacomclientPast15StatOutCrcCountInvPort1,
       "pm200fr20perfdatacomclientPast15StatOutCrcCountPort1": pm200fr20perfdatacomclientPast15StatOutCrcCountPort1,
       "pm200fr20perfdatacomclientPast15StatOutPacketCountInvPort1": pm200fr20perfdatacomclientPast15StatOutPacketCountInvPort1,
       "pm200fr20perfdatacomclientPast15StatOutPacketCountPort1": pm200fr20perfdatacomclientPast15StatOutPacketCountPort1,
       "pm200fr20PerfDatacomClientCurrent24StatTable": pm200fr20PerfDatacomClientCurrent24StatTable,
       "pm200fr20PerfDatacomClientCurrent24StatEntry": pm200fr20PerfDatacomClientCurrent24StatEntry,
       "pm200fr20PerfDatacomClientCurrent24StatIndex": pm200fr20PerfDatacomClientCurrent24StatIndex,
       "pm200fr20perfdatacomclientCurrent24StatInCrcCountInvPortn": pm200fr20perfdatacomclientCurrent24StatInCrcCountInvPortn,
       "pm200fr20perfdatacomclientCurrent24StatInCrcCountPortn": pm200fr20perfdatacomclientCurrent24StatInCrcCountPortn,
       "pm200fr20perfdatacomclientCurrent24StatInPacketCountInvPortn": pm200fr20perfdatacomclientCurrent24StatInPacketCountInvPortn,
       "pm200fr20perfdatacomclientCurrent24StatInPacketCountPortn": pm200fr20perfdatacomclientCurrent24StatInPacketCountPortn,
       "pm200fr20perfdatacomclientCurrent24StatOutCrcCountInvPortn": pm200fr20perfdatacomclientCurrent24StatOutCrcCountInvPortn,
       "pm200fr20perfdatacomclientCurrent24StatOutCrcCountPortn": pm200fr20perfdatacomclientCurrent24StatOutCrcCountPortn,
       "pm200fr20perfdatacomclientCurrent24StatOutPacketCountInvPortn": pm200fr20perfdatacomclientCurrent24StatOutPacketCountInvPortn,
       "pm200fr20perfdatacomclientCurrent24StatOutPacketCountPortn": pm200fr20perfdatacomclientCurrent24StatOutPacketCountPortn,
       "pm200fr20PerfDatacomClientPast24StatHistoryPort1Table": pm200fr20PerfDatacomClientPast24StatHistoryPort1Table,
       "pm200fr20PerfDatacomClientPast24StatHistoryPort1Entry": pm200fr20PerfDatacomClientPast24StatHistoryPort1Entry,
       "pm200fr20PerfDatacomClientPast24StatHistoryPort1Index": pm200fr20PerfDatacomClientPast24StatHistoryPort1Index,
       "pm200fr20perfdatacomclientPast24StatInCrcCountInvPort1": pm200fr20perfdatacomclientPast24StatInCrcCountInvPort1,
       "pm200fr20perfdatacomclientPast24StatInCrcCountPort1": pm200fr20perfdatacomclientPast24StatInCrcCountPort1,
       "pm200fr20perfdatacomclientPast24StatInPacketCountInvPort1": pm200fr20perfdatacomclientPast24StatInPacketCountInvPort1,
       "pm200fr20perfdatacomclientPast24StatInPacketCountPort1": pm200fr20perfdatacomclientPast24StatInPacketCountPort1,
       "pm200fr20perfdatacomclientPast24StatOutCrcCountInvPort1": pm200fr20perfdatacomclientPast24StatOutCrcCountInvPort1,
       "pm200fr20perfdatacomclientPast24StatOutCrcCountPort1": pm200fr20perfdatacomclientPast24StatOutCrcCountPort1,
       "pm200fr20perfdatacomclientPast24StatOutPacketCountInvPort1": pm200fr20perfdatacomclientPast24StatOutPacketCountInvPort1,
       "pm200fr20perfdatacomclientPast24StatOutPacketCountPort1": pm200fr20perfdatacomclientPast24StatOutPacketCountPort1,
       "pm200fr20MonPerfLine": pm200fr20MonPerfLine,
       "pm200fr20PerfTelecomLinePostFecCurrent15StatTable": pm200fr20PerfTelecomLinePostFecCurrent15StatTable,
       "pm200fr20PerfTelecomLinePostFecCurrent15StatEntry": pm200fr20PerfTelecomLinePostFecCurrent15StatEntry,
       "pm200fr20PerfTelecomLinePostFecCurrent15StatIndex": pm200fr20PerfTelecomLinePostFecCurrent15StatIndex,
       "pm200fr20PerfTelecomLinePostFecCurrent15StatInvCvPortn": pm200fr20PerfTelecomLinePostFecCurrent15StatInvCvPortn,
       "pm200fr20PerfTelecomLinePostFecCurrent15StatCvValuePortn": pm200fr20PerfTelecomLinePostFecCurrent15StatCvValuePortn,
       "pm200fr20PerfTelecomLinePostFecCurrent15StatInvEsPortn": pm200fr20PerfTelecomLinePostFecCurrent15StatInvEsPortn,
       "pm200fr20PerfTelecomLinePostFecCurrent15StatEsValuePortn": pm200fr20PerfTelecomLinePostFecCurrent15StatEsValuePortn,
       "pm200fr20PerfTelecomLinePostFecCurrent15StatInvSesPortn": pm200fr20PerfTelecomLinePostFecCurrent15StatInvSesPortn,
       "pm200fr20PerfTelecomLinePostFecCurrent15StatSesValuePortn": pm200fr20PerfTelecomLinePostFecCurrent15StatSesValuePortn,
       "pm200fr20PerfTelecomLinePostFecCurrent15StatInvSefsPortn": pm200fr20PerfTelecomLinePostFecCurrent15StatInvSefsPortn,
       "pm200fr20PerfTelecomLinePostFecCurrent15StatSefsValuePortn": pm200fr20PerfTelecomLinePostFecCurrent15StatSefsValuePortn,
       "pm200fr20PerfTelecomLinePostFecCurrent15StatInvUasPortn": pm200fr20PerfTelecomLinePostFecCurrent15StatInvUasPortn,
       "pm200fr20PerfTelecomLinePostFecCurrent15StatUasValuePortn": pm200fr20PerfTelecomLinePostFecCurrent15StatUasValuePortn,
       "pm200fr20PerfTelecomLinePostFecPast15StatHistoryPort1Table": pm200fr20PerfTelecomLinePostFecPast15StatHistoryPort1Table,
       "pm200fr20PerfTelecomLinePostFecPast15StatHistoryPort1Entry": pm200fr20PerfTelecomLinePostFecPast15StatHistoryPort1Entry,
       "pm200fr20PerfTelecomLinePostFecPast15StatHistoryPort1Index": pm200fr20PerfTelecomLinePostFecPast15StatHistoryPort1Index,
       "pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvCvPort1": pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvCvPort1,
       "pm200fr20PerfTelecomLinePostFecPast15StatHistoryCvValuePort1": pm200fr20PerfTelecomLinePostFecPast15StatHistoryCvValuePort1,
       "pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvEsPort1": pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvEsPort1,
       "pm200fr20PerfTelecomLinePostFecPast15StatHistoryEsValuePort1": pm200fr20PerfTelecomLinePostFecPast15StatHistoryEsValuePort1,
       "pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvSesPort1": pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvSesPort1,
       "pm200fr20PerfTelecomLinePostFecPast15StatHistorySesValuePort1": pm200fr20PerfTelecomLinePostFecPast15StatHistorySesValuePort1,
       "pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvSefsPort1": pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvSefsPort1,
       "pm200fr20PerfTelecomLinePostFecPast15StatHistorySefsValuePort1": pm200fr20PerfTelecomLinePostFecPast15StatHistorySefsValuePort1,
       "pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvUasPort1": pm200fr20PerfTelecomLinePostFecPast15StatHistoryInvUasPort1,
       "pm200fr20PerfTelecomLinePostFecPast15StatHistoryUasValuePort1": pm200fr20PerfTelecomLinePostFecPast15StatHistoryUasValuePort1,
       "pm200fr20PerfTelecomLinePostFecCurrent24StatTable": pm200fr20PerfTelecomLinePostFecCurrent24StatTable,
       "pm200fr20PerfTelecomLinePostFecCurrent24StatEntry": pm200fr20PerfTelecomLinePostFecCurrent24StatEntry,
       "pm200fr20PerfTelecomLinePostFecCurrent24StatIndex": pm200fr20PerfTelecomLinePostFecCurrent24StatIndex,
       "pm200fr20PerfTelecomLinePostFecCurrent24StatInvCvPortn": pm200fr20PerfTelecomLinePostFecCurrent24StatInvCvPortn,
       "pm200fr20PerfTelecomLinePostFecCurrent24StatCvValuePortn": pm200fr20PerfTelecomLinePostFecCurrent24StatCvValuePortn,
       "pm200fr20PerfTelecomLinePostFecCurrent24StatInvEsPortn": pm200fr20PerfTelecomLinePostFecCurrent24StatInvEsPortn,
       "pm200fr20PerfTelecomLinePostFecCurrent24StatEsValuePortn": pm200fr20PerfTelecomLinePostFecCurrent24StatEsValuePortn,
       "pm200fr20PerfTelecomLinePostFecCurrent24StatInvSesPortn": pm200fr20PerfTelecomLinePostFecCurrent24StatInvSesPortn,
       "pm200fr20PerfTelecomLinePostFecCurrent24StatSesValuePortn": pm200fr20PerfTelecomLinePostFecCurrent24StatSesValuePortn,
       "pm200fr20PerfTelecomLinePostFecCurrent24StatInvSefsPortn": pm200fr20PerfTelecomLinePostFecCurrent24StatInvSefsPortn,
       "pm200fr20PerfTelecomLinePostFecCurrent24StatSefsValuePortn": pm200fr20PerfTelecomLinePostFecCurrent24StatSefsValuePortn,
       "pm200fr20PerfTelecomLinePostFecCurrent24StatInvUasPortn": pm200fr20PerfTelecomLinePostFecCurrent24StatInvUasPortn,
       "pm200fr20PerfTelecomLinePostFecCurrent24StatUasValuePortn": pm200fr20PerfTelecomLinePostFecCurrent24StatUasValuePortn,
       "pm200fr20PerfTelecomLinePostFecPast24StatHistoryPort1Table": pm200fr20PerfTelecomLinePostFecPast24StatHistoryPort1Table,
       "pm200fr20PerfTelecomLinePostFecPast24StatHistoryPort1Entry": pm200fr20PerfTelecomLinePostFecPast24StatHistoryPort1Entry,
       "pm200fr20PerfTelecomLinePostFecPast24StatHistoryPort1Index": pm200fr20PerfTelecomLinePostFecPast24StatHistoryPort1Index,
       "pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvCvPort1": pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvCvPort1,
       "pm200fr20PerfTelecomLinePostFecPast24StatHistoryCvValuePort1": pm200fr20PerfTelecomLinePostFecPast24StatHistoryCvValuePort1,
       "pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvEsPort1": pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvEsPort1,
       "pm200fr20PerfTelecomLinePostFecPast24StatHistoryEsValuePort1": pm200fr20PerfTelecomLinePostFecPast24StatHistoryEsValuePort1,
       "pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvSesPort1": pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvSesPort1,
       "pm200fr20PerfTelecomLinePostFecPast24StatHistorySesValuePort1": pm200fr20PerfTelecomLinePostFecPast24StatHistorySesValuePort1,
       "pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvSefsPort1": pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvSefsPort1,
       "pm200fr20PerfTelecomLinePostFecPast24StatHistorySefsValuePort1": pm200fr20PerfTelecomLinePostFecPast24StatHistorySefsValuePort1,
       "pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvUasPort1": pm200fr20PerfTelecomLinePostFecPast24StatHistoryInvUasPort1,
       "pm200fr20PerfTelecomLinePostFecPast24StatHistoryUasValuePort1": pm200fr20PerfTelecomLinePostFecPast24StatHistoryUasValuePort1,
       "pm200fr20PerfTelecomBerLinePreFecCurrent15StatTable": pm200fr20PerfTelecomBerLinePreFecCurrent15StatTable,
       "pm200fr20PerfTelecomBerLinePreFecCurrent15StatEntry": pm200fr20PerfTelecomBerLinePreFecCurrent15StatEntry,
       "pm200fr20PerfTelecomBerLinePreFecCurrent15StatIndex": pm200fr20PerfTelecomBerLinePreFecCurrent15StatIndex,
       "pm200fr20PerfTelecomBerLinePreFecCurrent15StatInvBerPortn": pm200fr20PerfTelecomBerLinePreFecCurrent15StatInvBerPortn,
       "pm200fr20PerfTelecomBerLinePreFecCurrent15StatBerValuePortn": pm200fr20PerfTelecomBerLinePreFecCurrent15StatBerValuePortn,
       "pm200fr20PerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn": pm200fr20PerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn,
       "pm200fr20PerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn": pm200fr20PerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn,
       "pm200fr20PerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn": pm200fr20PerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn,
       "pm200fr20PerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn": pm200fr20PerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn,
       "pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryPort1Table": pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryPort1Table,
       "pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryPort1Entry": pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryPort1Entry,
       "pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryPort1Index": pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryPort1Index,
       "pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1": pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1,
       "pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1": pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1,
       "pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1": pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1,
       "pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1": pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1,
       "pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1": pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1,
       "pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1": pm200fr20PerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1,
       "pm200fr20PerfTelecomBerLinePreFecCurrent24StatTable": pm200fr20PerfTelecomBerLinePreFecCurrent24StatTable,
       "pm200fr20PerfTelecomBerLinePreFecCurrent24StatEntry": pm200fr20PerfTelecomBerLinePreFecCurrent24StatEntry,
       "pm200fr20PerfTelecomBerLinePreFecCurrent24StatIndex": pm200fr20PerfTelecomBerLinePreFecCurrent24StatIndex,
       "pm200fr20PerfTelecomBerLinePreFecCurrent24StatInvBerPortn": pm200fr20PerfTelecomBerLinePreFecCurrent24StatInvBerPortn,
       "pm200fr20PerfTelecomBerLinePreFecCurrent24StatBerValuePortn": pm200fr20PerfTelecomBerLinePreFecCurrent24StatBerValuePortn,
       "pm200fr20PerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn": pm200fr20PerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn,
       "pm200fr20PerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn": pm200fr20PerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn,
       "pm200fr20PerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn": pm200fr20PerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn,
       "pm200fr20PerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn": pm200fr20PerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn,
       "pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryPort1Table": pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryPort1Table,
       "pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryPort1Entry": pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryPort1Entry,
       "pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryPort1Index": pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryPort1Index,
       "pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1": pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1,
       "pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1": pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1,
       "pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1": pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1,
       "pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1": pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1,
       "pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1": pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1,
       "pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1": pm200fr20PerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1}
)
