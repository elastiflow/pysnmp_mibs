# SNMP MIB module (EKINOPS-Pme1008-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Pme1008-MIB.mib
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

modulePme1008 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79)
)
if mibBuilder.loadTexts:
    modulePme1008.setRevisions(
        ("2016-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Pme1008OtxGrid(TextualConvention, Integer32):
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



class Pme1008DccMode(TextualConvention, Integer32):
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



class Pme1008LineChannel(TextualConvention, Integer32):
    status = "current"


class Pme1008Odu2SapiMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("sapi", 1),
          ("dapi", 2),
          ("sapidapi", 3))
    )



class Pme1008Otu2SapiMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("sapi", 1),
          ("dapi", 2),
          ("sapidapi", 3))
    )



class Pme1008ClientProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("protocolclientvalue2", 2),
          ("protocolclientvalue3", 3),
          ("protocolclientvalue4", 4),
          ("protocolclientvalue6", 6),
          ("protocolclientvalue7", 7))
    )



# MIB Managed Objects in the order of their OIDs

_Pme1008alarms_ObjectIdentity = ObjectIdentity
pme1008alarms = _Pme1008alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2)
)
_Pme1008AlmOther_ObjectIdentity = ObjectIdentity
pme1008AlmOther = _Pme1008AlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 1)
)
_Pme1008AlmOtherNurg_ObjectIdentity = ObjectIdentity
pme1008AlmOtherNurg = _Pme1008AlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 1, 1)
)
_Pme1008AlmsynthAlm2_ObjectIdentity = ObjectIdentity
pme1008AlmsynthAlm2 = _Pme1008AlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 1, 1, 2)
)
_Pme1008AlmConfTableSave_Type = EkiOnOff
_Pme1008AlmConfTableSave_Object = MibScalar
pme1008AlmConfTableSave = _Pme1008AlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 1, 1, 2, 1),
    _Pme1008AlmConfTableSave_Type()
)
pme1008AlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmConfTableSave.setStatus("current")
_Pme1008AlmInvUpload_Type = EkiOnOff
_Pme1008AlmInvUpload_Object = MibScalar
pme1008AlmInvUpload = _Pme1008AlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 1, 1, 2, 2),
    _Pme1008AlmInvUpload_Type()
)
pme1008AlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmInvUpload.setStatus("current")
_Pme1008AlmConfTableLoad_Type = EkiOnOff
_Pme1008AlmConfTableLoad_Object = MibScalar
pme1008AlmConfTableLoad = _Pme1008AlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 1, 1, 2, 3),
    _Pme1008AlmConfTableLoad_Type()
)
pme1008AlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmConfTableLoad.setStatus("current")
_Pme1008AlmCorrelatOff_Type = EkiOnOff
_Pme1008AlmCorrelatOff_Object = MibScalar
pme1008AlmCorrelatOff = _Pme1008AlmCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 1, 1, 2, 4),
    _Pme1008AlmCorrelatOff_Type()
)
pme1008AlmCorrelatOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmCorrelatOff.setStatus("current")
_Pme1008AlmOtherUrg_ObjectIdentity = ObjectIdentity
pme1008AlmOtherUrg = _Pme1008AlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 1, 2)
)
_Pme1008AlmOtherCrit_ObjectIdentity = ObjectIdentity
pme1008AlmOtherCrit = _Pme1008AlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 1, 3)
)
_Pme1008AlmsynthAlm0_ObjectIdentity = ObjectIdentity
pme1008AlmsynthAlm0 = _Pme1008AlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 1, 3, 0)
)
_Pme1008AlmModGlobFail_Type = EkiOnOff
_Pme1008AlmModGlobFail_Object = MibScalar
pme1008AlmModGlobFail = _Pme1008AlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 1, 3, 0, 9),
    _Pme1008AlmModGlobFail_Type()
)
pme1008AlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmModGlobFail.setStatus("current")
_Pme1008AlmDefFuseA_Type = EkiOnOff
_Pme1008AlmDefFuseA_Object = MibScalar
pme1008AlmDefFuseA = _Pme1008AlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 1, 3, 0, 15),
    _Pme1008AlmDefFuseA_Type()
)
pme1008AlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmDefFuseA.setStatus("current")
_Pme1008AlmDefFuseB_Type = EkiOnOff
_Pme1008AlmDefFuseB_Object = MibScalar
pme1008AlmDefFuseB = _Pme1008AlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 1, 3, 0, 16),
    _Pme1008AlmDefFuseB_Type()
)
pme1008AlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmDefFuseB.setStatus("current")
_Pme1008AlmClient_ObjectIdentity = ObjectIdentity
pme1008AlmClient = _Pme1008AlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2)
)
_Pme1008AlmClientNurg_ObjectIdentity = ObjectIdentity
pme1008AlmClientNurg = _Pme1008AlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 1)
)
_Pme1008AlmclientSfpWarnDdmTable_Object = MibTable
pme1008AlmclientSfpWarnDdmTable = _Pme1008AlmclientSfpWarnDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 1, 232)
)
if mibBuilder.loadTexts:
    pme1008AlmclientSfpWarnDdmTable.setStatus("current")
_Pme1008AlmclientSfpWarnDdmEntry_Object = MibTableRow
pme1008AlmclientSfpWarnDdmEntry = _Pme1008AlmclientSfpWarnDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 1, 232, 1)
)
pme1008AlmclientSfpWarnDdmEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008AlmclientSfpWarnDdmIndex"),
)
if mibBuilder.loadTexts:
    pme1008AlmclientSfpWarnDdmEntry.setStatus("current")


class _Pme1008AlmclientSfpWarnDdmIndex_Type(Integer32):
    """Custom type pme1008AlmclientSfpWarnDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008AlmclientSfpWarnDdmIndex_Type.__name__ = "Integer32"
_Pme1008AlmclientSfpWarnDdmIndex_Object = MibTableColumn
pme1008AlmclientSfpWarnDdmIndex = _Pme1008AlmclientSfpWarnDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 1, 232, 1, 1),
    _Pme1008AlmclientSfpWarnDdmIndex_Type()
)
pme1008AlmclientSfpWarnDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmclientSfpWarnDdmIndex.setStatus("current")
_Pme1008AlmClientTxPwLowWngPortn_Type = EkiOnOff
_Pme1008AlmClientTxPwLowWngPortn_Object = MibTableColumn
pme1008AlmClientTxPwLowWngPortn = _Pme1008AlmClientTxPwLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 1, 232, 1, 2),
    _Pme1008AlmClientTxPwLowWngPortn_Type()
)
pme1008AlmClientTxPwLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmClientTxPwLowWngPortn.setStatus("current")
_Pme1008AlmClientTxPwrHighWngPortn_Type = EkiOnOff
_Pme1008AlmClientTxPwrHighWngPortn_Object = MibTableColumn
pme1008AlmClientTxPwrHighWngPortn = _Pme1008AlmClientTxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 1, 232, 1, 3),
    _Pme1008AlmClientTxPwrHighWngPortn_Type()
)
pme1008AlmClientTxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmClientTxPwrHighWngPortn.setStatus("current")
_Pme1008AlmClientTxBiasLowWngPortn_Type = EkiOnOff
_Pme1008AlmClientTxBiasLowWngPortn_Object = MibTableColumn
pme1008AlmClientTxBiasLowWngPortn = _Pme1008AlmClientTxBiasLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 1, 232, 1, 4),
    _Pme1008AlmClientTxBiasLowWngPortn_Type()
)
pme1008AlmClientTxBiasLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmClientTxBiasLowWngPortn.setStatus("current")
_Pme1008AlmClientTxBiasHighWngPortn_Type = EkiOnOff
_Pme1008AlmClientTxBiasHighWngPortn_Object = MibTableColumn
pme1008AlmClientTxBiasHighWngPortn = _Pme1008AlmClientTxBiasHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 1, 232, 1, 5),
    _Pme1008AlmClientTxBiasHighWngPortn_Type()
)
pme1008AlmClientTxBiasHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmClientTxBiasHighWngPortn.setStatus("current")
_Pme1008AlmClientVccLowWngPortn_Type = EkiOnOff
_Pme1008AlmClientVccLowWngPortn_Object = MibTableColumn
pme1008AlmClientVccLowWngPortn = _Pme1008AlmClientVccLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 1, 232, 1, 6),
    _Pme1008AlmClientVccLowWngPortn_Type()
)
pme1008AlmClientVccLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmClientVccLowWngPortn.setStatus("current")
_Pme1008AlmClientVccHighWngPortn_Type = EkiOnOff
_Pme1008AlmClientVccHighWngPortn_Object = MibTableColumn
pme1008AlmClientVccHighWngPortn = _Pme1008AlmClientVccHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 1, 232, 1, 7),
    _Pme1008AlmClientVccHighWngPortn_Type()
)
pme1008AlmClientVccHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmClientVccHighWngPortn.setStatus("current")
_Pme1008AlmClientTempLowWngPortn_Type = EkiOnOff
_Pme1008AlmClientTempLowWngPortn_Object = MibTableColumn
pme1008AlmClientTempLowWngPortn = _Pme1008AlmClientTempLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 1, 232, 1, 8),
    _Pme1008AlmClientTempLowWngPortn_Type()
)
pme1008AlmClientTempLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmClientTempLowWngPortn.setStatus("current")
_Pme1008AlmClientTempHighWngPortn_Type = EkiOnOff
_Pme1008AlmClientTempHighWngPortn_Object = MibTableColumn
pme1008AlmClientTempHighWngPortn = _Pme1008AlmClientTempHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 1, 232, 1, 9),
    _Pme1008AlmClientTempHighWngPortn_Type()
)
pme1008AlmClientTempHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmClientTempHighWngPortn.setStatus("current")
_Pme1008AlmClientRxPwrLowWngPortn_Type = EkiOnOff
_Pme1008AlmClientRxPwrLowWngPortn_Object = MibTableColumn
pme1008AlmClientRxPwrLowWngPortn = _Pme1008AlmClientRxPwrLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 1, 232, 1, 16),
    _Pme1008AlmClientRxPwrLowWngPortn_Type()
)
pme1008AlmClientRxPwrLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmClientRxPwrLowWngPortn.setStatus("current")
_Pme1008AlmClientRxPwrHighWngPortn_Type = EkiOnOff
_Pme1008AlmClientRxPwrHighWngPortn_Object = MibTableColumn
pme1008AlmClientRxPwrHighWngPortn = _Pme1008AlmClientRxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 1, 232, 1, 17),
    _Pme1008AlmClientRxPwrHighWngPortn_Type()
)
pme1008AlmClientRxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmClientRxPwrHighWngPortn.setStatus("current")
_Pme1008AlmClientUrg_ObjectIdentity = ObjectIdentity
pme1008AlmClientUrg = _Pme1008AlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 2)
)
_Pme1008AlmclientHostLaneFaultTable_Object = MibTable
pme1008AlmclientHostLaneFaultTable = _Pme1008AlmclientHostLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 2, 88)
)
if mibBuilder.loadTexts:
    pme1008AlmclientHostLaneFaultTable.setStatus("current")
_Pme1008AlmclientHostLaneFaultEntry_Object = MibTableRow
pme1008AlmclientHostLaneFaultEntry = _Pme1008AlmclientHostLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 2, 88, 1)
)
pme1008AlmclientHostLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008AlmclientHostLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    pme1008AlmclientHostLaneFaultEntry.setStatus("current")


class _Pme1008AlmclientHostLaneFaultIndex_Type(Integer32):
    """Custom type pme1008AlmclientHostLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008AlmclientHostLaneFaultIndex_Type.__name__ = "Integer32"
_Pme1008AlmclientHostLaneFaultIndex_Object = MibTableColumn
pme1008AlmclientHostLaneFaultIndex = _Pme1008AlmclientHostLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 2, 88, 1, 1),
    _Pme1008AlmclientHostLaneFaultIndex_Type()
)
pme1008AlmclientHostLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmclientHostLaneFaultIndex.setStatus("current")
_Pme1008AlmClientLossOfSyncPortn_Type = EkiOnOff
_Pme1008AlmClientLossOfSyncPortn_Object = MibTableColumn
pme1008AlmClientLossOfSyncPortn = _Pme1008AlmClientLossOfSyncPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 2, 88, 1, 2),
    _Pme1008AlmClientLossOfSyncPortn_Type()
)
pme1008AlmClientLossOfSyncPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmClientLossOfSyncPortn.setStatus("current")
_Pme1008AlmClientInputLossOfSigPortn_Type = EkiOnOff
_Pme1008AlmClientInputLossOfSigPortn_Object = MibTableColumn
pme1008AlmClientInputLossOfSigPortn = _Pme1008AlmClientInputLossOfSigPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 2, 88, 1, 3),
    _Pme1008AlmClientInputLossOfSigPortn_Type()
)
pme1008AlmClientInputLossOfSigPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmClientInputLossOfSigPortn.setStatus("current")
_Pme1008AlmClientCsfDetectedPortn_Type = EkiOnOff
_Pme1008AlmClientCsfDetectedPortn_Object = MibTableColumn
pme1008AlmClientCsfDetectedPortn = _Pme1008AlmClientCsfDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 2, 88, 1, 7),
    _Pme1008AlmClientCsfDetectedPortn_Type()
)
pme1008AlmClientCsfDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmClientCsfDetectedPortn.setStatus("current")
_Pme1008AlmClientLaneTxFifoErrorPortn_Type = EkiOnOff
_Pme1008AlmClientLaneTxFifoErrorPortn_Object = MibTableColumn
pme1008AlmClientLaneTxFifoErrorPortn = _Pme1008AlmClientLaneTxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 2, 88, 1, 11),
    _Pme1008AlmClientLaneTxFifoErrorPortn_Type()
)
pme1008AlmClientLaneTxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmClientLaneTxFifoErrorPortn.setStatus("current")
_Pme1008AlmclientSfpAlmDdmTable_Object = MibTable
pme1008AlmclientSfpAlmDdmTable = _Pme1008AlmclientSfpAlmDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 2, 216)
)
if mibBuilder.loadTexts:
    pme1008AlmclientSfpAlmDdmTable.setStatus("current")
_Pme1008AlmclientSfpAlmDdmEntry_Object = MibTableRow
pme1008AlmclientSfpAlmDdmEntry = _Pme1008AlmclientSfpAlmDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 2, 216, 1)
)
pme1008AlmclientSfpAlmDdmEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008AlmclientSfpAlmDdmIndex"),
)
if mibBuilder.loadTexts:
    pme1008AlmclientSfpAlmDdmEntry.setStatus("current")


class _Pme1008AlmclientSfpAlmDdmIndex_Type(Integer32):
    """Custom type pme1008AlmclientSfpAlmDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008AlmclientSfpAlmDdmIndex_Type.__name__ = "Integer32"
_Pme1008AlmclientSfpAlmDdmIndex_Object = MibTableColumn
pme1008AlmclientSfpAlmDdmIndex = _Pme1008AlmclientSfpAlmDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 2, 216, 1, 1),
    _Pme1008AlmclientSfpAlmDdmIndex_Type()
)
pme1008AlmclientSfpAlmDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmclientSfpAlmDdmIndex.setStatus("current")
_Pme1008AlmClientTxPwrLowAlaPortn_Type = EkiOnOff
_Pme1008AlmClientTxPwrLowAlaPortn_Object = MibTableColumn
pme1008AlmClientTxPwrLowAlaPortn = _Pme1008AlmClientTxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 2, 216, 1, 2),
    _Pme1008AlmClientTxPwrLowAlaPortn_Type()
)
pme1008AlmClientTxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmClientTxPwrLowAlaPortn.setStatus("current")
_Pme1008AlmClientTxPwrHighAlaPortn_Type = EkiOnOff
_Pme1008AlmClientTxPwrHighAlaPortn_Object = MibTableColumn
pme1008AlmClientTxPwrHighAlaPortn = _Pme1008AlmClientTxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 2, 216, 1, 3),
    _Pme1008AlmClientTxPwrHighAlaPortn_Type()
)
pme1008AlmClientTxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmClientTxPwrHighAlaPortn.setStatus("current")
_Pme1008AlmClientTxBiasLowAlaPortn_Type = EkiOnOff
_Pme1008AlmClientTxBiasLowAlaPortn_Object = MibTableColumn
pme1008AlmClientTxBiasLowAlaPortn = _Pme1008AlmClientTxBiasLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 2, 216, 1, 4),
    _Pme1008AlmClientTxBiasLowAlaPortn_Type()
)
pme1008AlmClientTxBiasLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmClientTxBiasLowAlaPortn.setStatus("current")
_Pme1008AlmClientTxBiasHighAlaPortn_Type = EkiOnOff
_Pme1008AlmClientTxBiasHighAlaPortn_Object = MibTableColumn
pme1008AlmClientTxBiasHighAlaPortn = _Pme1008AlmClientTxBiasHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 2, 216, 1, 5),
    _Pme1008AlmClientTxBiasHighAlaPortn_Type()
)
pme1008AlmClientTxBiasHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmClientTxBiasHighAlaPortn.setStatus("current")
_Pme1008AlmClientVccLowAlaPortn_Type = EkiOnOff
_Pme1008AlmClientVccLowAlaPortn_Object = MibTableColumn
pme1008AlmClientVccLowAlaPortn = _Pme1008AlmClientVccLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 2, 216, 1, 6),
    _Pme1008AlmClientVccLowAlaPortn_Type()
)
pme1008AlmClientVccLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmClientVccLowAlaPortn.setStatus("current")
_Pme1008AlmClientVccHighAlaPortn_Type = EkiOnOff
_Pme1008AlmClientVccHighAlaPortn_Object = MibTableColumn
pme1008AlmClientVccHighAlaPortn = _Pme1008AlmClientVccHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 2, 216, 1, 7),
    _Pme1008AlmClientVccHighAlaPortn_Type()
)
pme1008AlmClientVccHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmClientVccHighAlaPortn.setStatus("current")
_Pme1008AlmClientTempLowAlaPortn_Type = EkiOnOff
_Pme1008AlmClientTempLowAlaPortn_Object = MibTableColumn
pme1008AlmClientTempLowAlaPortn = _Pme1008AlmClientTempLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 2, 216, 1, 8),
    _Pme1008AlmClientTempLowAlaPortn_Type()
)
pme1008AlmClientTempLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmClientTempLowAlaPortn.setStatus("current")
_Pme1008AlmClientTempHighAlaPortn_Type = EkiOnOff
_Pme1008AlmClientTempHighAlaPortn_Object = MibTableColumn
pme1008AlmClientTempHighAlaPortn = _Pme1008AlmClientTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 2, 216, 1, 9),
    _Pme1008AlmClientTempHighAlaPortn_Type()
)
pme1008AlmClientTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmClientTempHighAlaPortn.setStatus("current")
_Pme1008AlmClientRxPwrLowAlaPortn_Type = EkiOnOff
_Pme1008AlmClientRxPwrLowAlaPortn_Object = MibTableColumn
pme1008AlmClientRxPwrLowAlaPortn = _Pme1008AlmClientRxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 2, 216, 1, 16),
    _Pme1008AlmClientRxPwrLowAlaPortn_Type()
)
pme1008AlmClientRxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmClientRxPwrLowAlaPortn.setStatus("current")
_Pme1008AlmClientRxPwrHighAlaPortn_Type = EkiOnOff
_Pme1008AlmClientRxPwrHighAlaPortn_Object = MibTableColumn
pme1008AlmClientRxPwrHighAlaPortn = _Pme1008AlmClientRxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 2, 216, 1, 17),
    _Pme1008AlmClientRxPwrHighAlaPortn_Type()
)
pme1008AlmClientRxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmClientRxPwrHighAlaPortn.setStatus("current")
_Pme1008AlmClientCrit_ObjectIdentity = ObjectIdentity
pme1008AlmClientCrit = _Pme1008AlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 3)
)
_Pme1008AlmsynthAlmPortTable_Object = MibTable
pme1008AlmsynthAlmPortTable = _Pme1008AlmsynthAlmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    pme1008AlmsynthAlmPortTable.setStatus("current")
_Pme1008AlmsynthAlmPortEntry_Object = MibTableRow
pme1008AlmsynthAlmPortEntry = _Pme1008AlmsynthAlmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 3, 8, 1)
)
pme1008AlmsynthAlmPortEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008AlmsynthAlmPortIndex"),
)
if mibBuilder.loadTexts:
    pme1008AlmsynthAlmPortEntry.setStatus("current")


class _Pme1008AlmsynthAlmPortIndex_Type(Integer32):
    """Custom type pme1008AlmsynthAlmPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008AlmsynthAlmPortIndex_Type.__name__ = "Integer32"
_Pme1008AlmsynthAlmPortIndex_Object = MibTableColumn
pme1008AlmsynthAlmPortIndex = _Pme1008AlmsynthAlmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 3, 8, 1, 1),
    _Pme1008AlmsynthAlmPortIndex_Type()
)
pme1008AlmsynthAlmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmsynthAlmPortIndex.setStatus("current")
_Pme1008AlmSfpAbsentPortn_Type = EkiOnOff
_Pme1008AlmSfpAbsentPortn_Object = MibTableColumn
pme1008AlmSfpAbsentPortn = _Pme1008AlmSfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 3, 8, 1, 2),
    _Pme1008AlmSfpAbsentPortn_Type()
)
pme1008AlmSfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmSfpAbsentPortn.setStatus("current")
_Pme1008AlmDdmAbsentPortn_Type = EkiOnOff
_Pme1008AlmDdmAbsentPortn_Object = MibTableColumn
pme1008AlmDdmAbsentPortn = _Pme1008AlmDdmAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 3, 8, 1, 3),
    _Pme1008AlmDdmAbsentPortn_Type()
)
pme1008AlmDdmAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmDdmAbsentPortn.setStatus("current")
_Pme1008AlmHwFailAccPortn_Type = EkiOnOff
_Pme1008AlmHwFailAccPortn_Object = MibTableColumn
pme1008AlmHwFailAccPortn = _Pme1008AlmHwFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 3, 8, 1, 5),
    _Pme1008AlmHwFailAccPortn_Type()
)
pme1008AlmHwFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmHwFailAccPortn.setStatus("current")
_Pme1008AlmDwLsdPortn_Type = EkiOnOff
_Pme1008AlmDwLsdPortn_Object = MibTableColumn
pme1008AlmDwLsdPortn = _Pme1008AlmDwLsdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 3, 8, 1, 6),
    _Pme1008AlmDwLsdPortn_Type()
)
pme1008AlmDwLsdPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmDwLsdPortn.setStatus("current")
_Pme1008AlmClientLocalOosPortn_Type = EkiOnOff
_Pme1008AlmClientLocalOosPortn_Object = MibTableColumn
pme1008AlmClientLocalOosPortn = _Pme1008AlmClientLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 3, 8, 1, 7),
    _Pme1008AlmClientLocalOosPortn_Type()
)
pme1008AlmClientLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmClientLocalOosPortn.setStatus("current")
_Pme1008AlmClientRemoteOosPortn_Type = EkiOnOff
_Pme1008AlmClientRemoteOosPortn_Object = MibTableColumn
pme1008AlmClientRemoteOosPortn = _Pme1008AlmClientRemoteOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 3, 8, 1, 8),
    _Pme1008AlmClientRemoteOosPortn_Type()
)
pme1008AlmClientRemoteOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmClientRemoteOosPortn.setStatus("current")
_Pme1008AlmDwCaisPortn_Type = EkiOnOff
_Pme1008AlmDwCaisPortn_Object = MibTableColumn
pme1008AlmDwCaisPortn = _Pme1008AlmDwCaisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 3, 8, 1, 9),
    _Pme1008AlmDwCaisPortn_Type()
)
pme1008AlmDwCaisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmDwCaisPortn.setStatus("current")
_Pme1008AlmSfpDdmWarningPortn_Type = EkiOnOff
_Pme1008AlmSfpDdmWarningPortn_Object = MibTableColumn
pme1008AlmSfpDdmWarningPortn = _Pme1008AlmSfpDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 3, 8, 1, 10),
    _Pme1008AlmSfpDdmWarningPortn_Type()
)
pme1008AlmSfpDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmSfpDdmWarningPortn.setStatus("current")
_Pme1008AlmSfpDdmAlmPortn_Type = EkiOnOff
_Pme1008AlmSfpDdmAlmPortn_Object = MibTableColumn
pme1008AlmSfpDdmAlmPortn = _Pme1008AlmSfpDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 3, 8, 1, 11),
    _Pme1008AlmSfpDdmAlmPortn_Type()
)
pme1008AlmSfpDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmSfpDdmAlmPortn.setStatus("current")
_Pme1008AlmFailAccPortn_Type = EkiOnOff
_Pme1008AlmFailAccPortn_Object = MibTableColumn
pme1008AlmFailAccPortn = _Pme1008AlmFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 3, 8, 1, 13),
    _Pme1008AlmFailAccPortn_Type()
)
pme1008AlmFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmFailAccPortn.setStatus("current")
_Pme1008AlmUpCsfPortn_Type = EkiOnOff
_Pme1008AlmUpCsfPortn_Object = MibTableColumn
pme1008AlmUpCsfPortn = _Pme1008AlmUpCsfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 2, 3, 8, 1, 17),
    _Pme1008AlmUpCsfPortn_Type()
)
pme1008AlmUpCsfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmUpCsfPortn.setStatus("current")
_Pme1008AlmLine_ObjectIdentity = ObjectIdentity
pme1008AlmLine = _Pme1008AlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3)
)
_Pme1008AlmLineNurg_ObjectIdentity = ObjectIdentity
pme1008AlmLineNurg = _Pme1008AlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 1)
)
_Pme1008AlmLineUrg_ObjectIdentity = ObjectIdentity
pme1008AlmLineUrg = _Pme1008AlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 2)
)
_Pme1008AlmlineNetworkLaneAlarmWarning1Table_Object = MibTable
pme1008AlmlineNetworkLaneAlarmWarning1Table = _Pme1008AlmlineNetworkLaneAlarmWarning1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 2, 104)
)
if mibBuilder.loadTexts:
    pme1008AlmlineNetworkLaneAlarmWarning1Table.setStatus("current")
_Pme1008AlmlineNetworkLaneAlarmWarning1Entry_Object = MibTableRow
pme1008AlmlineNetworkLaneAlarmWarning1Entry = _Pme1008AlmlineNetworkLaneAlarmWarning1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 2, 104, 1)
)
pme1008AlmlineNetworkLaneAlarmWarning1Entry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008AlmlineNetworkLaneAlarmWarning1Index"),
)
if mibBuilder.loadTexts:
    pme1008AlmlineNetworkLaneAlarmWarning1Entry.setStatus("current")


class _Pme1008AlmlineNetworkLaneAlarmWarning1Index_Type(Integer32):
    """Custom type pme1008AlmlineNetworkLaneAlarmWarning1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008AlmlineNetworkLaneAlarmWarning1Index_Type.__name__ = "Integer32"
_Pme1008AlmlineNetworkLaneAlarmWarning1Index_Object = MibTableColumn
pme1008AlmlineNetworkLaneAlarmWarning1Index = _Pme1008AlmlineNetworkLaneAlarmWarning1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 2, 104, 1, 1),
    _Pme1008AlmlineNetworkLaneAlarmWarning1Index_Type()
)
pme1008AlmlineNetworkLaneAlarmWarning1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmlineNetworkLaneAlarmWarning1Index.setStatus("current")
_Pme1008AlmLineTxPwrLowAlaPortn_Type = EkiOnOff
_Pme1008AlmLineTxPwrLowAlaPortn_Object = MibTableColumn
pme1008AlmLineTxPwrLowAlaPortn = _Pme1008AlmLineTxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 2, 104, 1, 2),
    _Pme1008AlmLineTxPwrLowAlaPortn_Type()
)
pme1008AlmLineTxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmLineTxPwrLowAlaPortn.setStatus("current")
_Pme1008AlmLineTxPwrHighAlaPortn_Type = EkiOnOff
_Pme1008AlmLineTxPwrHighAlaPortn_Object = MibTableColumn
pme1008AlmLineTxPwrHighAlaPortn = _Pme1008AlmLineTxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 2, 104, 1, 3),
    _Pme1008AlmLineTxPwrHighAlaPortn_Type()
)
pme1008AlmLineTxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmLineTxPwrHighAlaPortn.setStatus("current")
_Pme1008AlmLineTxBiasLowAlaPortn_Type = EkiOnOff
_Pme1008AlmLineTxBiasLowAlaPortn_Object = MibTableColumn
pme1008AlmLineTxBiasLowAlaPortn = _Pme1008AlmLineTxBiasLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 2, 104, 1, 4),
    _Pme1008AlmLineTxBiasLowAlaPortn_Type()
)
pme1008AlmLineTxBiasLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmLineTxBiasLowAlaPortn.setStatus("current")
_Pme1008AlmLineTxBiasHighAlaPortn_Type = EkiOnOff
_Pme1008AlmLineTxBiasHighAlaPortn_Object = MibTableColumn
pme1008AlmLineTxBiasHighAlaPortn = _Pme1008AlmLineTxBiasHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 2, 104, 1, 5),
    _Pme1008AlmLineTxBiasHighAlaPortn_Type()
)
pme1008AlmLineTxBiasHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmLineTxBiasHighAlaPortn.setStatus("current")
_Pme1008AlmLineVccLowAlaPortn_Type = EkiOnOff
_Pme1008AlmLineVccLowAlaPortn_Object = MibTableColumn
pme1008AlmLineVccLowAlaPortn = _Pme1008AlmLineVccLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 2, 104, 1, 6),
    _Pme1008AlmLineVccLowAlaPortn_Type()
)
pme1008AlmLineVccLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmLineVccLowAlaPortn.setStatus("current")
_Pme1008AlmLineVccHighAlaPortn_Type = EkiOnOff
_Pme1008AlmLineVccHighAlaPortn_Object = MibTableColumn
pme1008AlmLineVccHighAlaPortn = _Pme1008AlmLineVccHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 2, 104, 1, 7),
    _Pme1008AlmLineVccHighAlaPortn_Type()
)
pme1008AlmLineVccHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmLineVccHighAlaPortn.setStatus("current")
_Pme1008AlmLineTempLowAlaPortn_Type = EkiOnOff
_Pme1008AlmLineTempLowAlaPortn_Object = MibTableColumn
pme1008AlmLineTempLowAlaPortn = _Pme1008AlmLineTempLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 2, 104, 1, 8),
    _Pme1008AlmLineTempLowAlaPortn_Type()
)
pme1008AlmLineTempLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmLineTempLowAlaPortn.setStatus("current")
_Pme1008AlmLineTempHighAlaPortn_Type = EkiOnOff
_Pme1008AlmLineTempHighAlaPortn_Object = MibTableColumn
pme1008AlmLineTempHighAlaPortn = _Pme1008AlmLineTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 2, 104, 1, 9),
    _Pme1008AlmLineTempHighAlaPortn_Type()
)
pme1008AlmLineTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmLineTempHighAlaPortn.setStatus("current")
_Pme1008AlmLineRxPwrLowAlaPortn_Type = EkiOnOff
_Pme1008AlmLineRxPwrLowAlaPortn_Object = MibTableColumn
pme1008AlmLineRxPwrLowAlaPortn = _Pme1008AlmLineRxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 2, 104, 1, 16),
    _Pme1008AlmLineRxPwrLowAlaPortn_Type()
)
pme1008AlmLineRxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmLineRxPwrLowAlaPortn.setStatus("current")
_Pme1008AlmLineRxPwrHighAlaPortn_Type = EkiOnOff
_Pme1008AlmLineRxPwrHighAlaPortn_Object = MibTableColumn
pme1008AlmLineRxPwrHighAlaPortn = _Pme1008AlmLineRxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 2, 104, 1, 17),
    _Pme1008AlmLineRxPwrHighAlaPortn_Type()
)
pme1008AlmLineRxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmLineRxPwrHighAlaPortn.setStatus("current")
_Pme1008AlmlineNetworkLaneAlarmWarning2Table_Object = MibTable
pme1008AlmlineNetworkLaneAlarmWarning2Table = _Pme1008AlmlineNetworkLaneAlarmWarning2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 2, 120)
)
if mibBuilder.loadTexts:
    pme1008AlmlineNetworkLaneAlarmWarning2Table.setStatus("current")
_Pme1008AlmlineNetworkLaneAlarmWarning2Entry_Object = MibTableRow
pme1008AlmlineNetworkLaneAlarmWarning2Entry = _Pme1008AlmlineNetworkLaneAlarmWarning2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 2, 120, 1)
)
pme1008AlmlineNetworkLaneAlarmWarning2Entry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008AlmlineNetworkLaneAlarmWarning2Index"),
)
if mibBuilder.loadTexts:
    pme1008AlmlineNetworkLaneAlarmWarning2Entry.setStatus("current")


class _Pme1008AlmlineNetworkLaneAlarmWarning2Index_Type(Integer32):
    """Custom type pme1008AlmlineNetworkLaneAlarmWarning2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008AlmlineNetworkLaneAlarmWarning2Index_Type.__name__ = "Integer32"
_Pme1008AlmlineNetworkLaneAlarmWarning2Index_Object = MibTableColumn
pme1008AlmlineNetworkLaneAlarmWarning2Index = _Pme1008AlmlineNetworkLaneAlarmWarning2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 2, 120, 1, 1),
    _Pme1008AlmlineNetworkLaneAlarmWarning2Index_Type()
)
pme1008AlmlineNetworkLaneAlarmWarning2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmlineNetworkLaneAlarmWarning2Index.setStatus("current")
_Pme1008AlmLineTxPwLowWngPortn_Type = EkiOnOff
_Pme1008AlmLineTxPwLowWngPortn_Object = MibTableColumn
pme1008AlmLineTxPwLowWngPortn = _Pme1008AlmLineTxPwLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 2, 120, 1, 2),
    _Pme1008AlmLineTxPwLowWngPortn_Type()
)
pme1008AlmLineTxPwLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmLineTxPwLowWngPortn.setStatus("current")
_Pme1008AlmLineTxPwrHighWngPortn_Type = EkiOnOff
_Pme1008AlmLineTxPwrHighWngPortn_Object = MibTableColumn
pme1008AlmLineTxPwrHighWngPortn = _Pme1008AlmLineTxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 2, 120, 1, 3),
    _Pme1008AlmLineTxPwrHighWngPortn_Type()
)
pme1008AlmLineTxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmLineTxPwrHighWngPortn.setStatus("current")
_Pme1008AlmLineTxBiasLowWngPortn_Type = EkiOnOff
_Pme1008AlmLineTxBiasLowWngPortn_Object = MibTableColumn
pme1008AlmLineTxBiasLowWngPortn = _Pme1008AlmLineTxBiasLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 2, 120, 1, 4),
    _Pme1008AlmLineTxBiasLowWngPortn_Type()
)
pme1008AlmLineTxBiasLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmLineTxBiasLowWngPortn.setStatus("current")
_Pme1008AlmLineTxBiasHighWngPortn_Type = EkiOnOff
_Pme1008AlmLineTxBiasHighWngPortn_Object = MibTableColumn
pme1008AlmLineTxBiasHighWngPortn = _Pme1008AlmLineTxBiasHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 2, 120, 1, 5),
    _Pme1008AlmLineTxBiasHighWngPortn_Type()
)
pme1008AlmLineTxBiasHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmLineTxBiasHighWngPortn.setStatus("current")
_Pme1008AlmLineVccLowWngPortn_Type = EkiOnOff
_Pme1008AlmLineVccLowWngPortn_Object = MibTableColumn
pme1008AlmLineVccLowWngPortn = _Pme1008AlmLineVccLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 2, 120, 1, 6),
    _Pme1008AlmLineVccLowWngPortn_Type()
)
pme1008AlmLineVccLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmLineVccLowWngPortn.setStatus("current")
_Pme1008AlmLineVccHighWngPortn_Type = EkiOnOff
_Pme1008AlmLineVccHighWngPortn_Object = MibTableColumn
pme1008AlmLineVccHighWngPortn = _Pme1008AlmLineVccHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 2, 120, 1, 7),
    _Pme1008AlmLineVccHighWngPortn_Type()
)
pme1008AlmLineVccHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmLineVccHighWngPortn.setStatus("current")
_Pme1008AlmLineTempLowWngPortn_Type = EkiOnOff
_Pme1008AlmLineTempLowWngPortn_Object = MibTableColumn
pme1008AlmLineTempLowWngPortn = _Pme1008AlmLineTempLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 2, 120, 1, 8),
    _Pme1008AlmLineTempLowWngPortn_Type()
)
pme1008AlmLineTempLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmLineTempLowWngPortn.setStatus("current")
_Pme1008AlmLineTempHighWngPortn_Type = EkiOnOff
_Pme1008AlmLineTempHighWngPortn_Object = MibTableColumn
pme1008AlmLineTempHighWngPortn = _Pme1008AlmLineTempHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 2, 120, 1, 9),
    _Pme1008AlmLineTempHighWngPortn_Type()
)
pme1008AlmLineTempHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmLineTempHighWngPortn.setStatus("current")
_Pme1008AlmLineRxPwrLowWngPortn_Type = EkiOnOff
_Pme1008AlmLineRxPwrLowWngPortn_Object = MibTableColumn
pme1008AlmLineRxPwrLowWngPortn = _Pme1008AlmLineRxPwrLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 2, 120, 1, 16),
    _Pme1008AlmLineRxPwrLowWngPortn_Type()
)
pme1008AlmLineRxPwrLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmLineRxPwrLowWngPortn.setStatus("current")
_Pme1008AlmLineRxPwrHighWngPortn_Type = EkiOnOff
_Pme1008AlmLineRxPwrHighWngPortn_Object = MibTableColumn
pme1008AlmLineRxPwrHighWngPortn = _Pme1008AlmLineRxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 2, 120, 1, 17),
    _Pme1008AlmLineRxPwrHighWngPortn_Type()
)
pme1008AlmLineRxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmLineRxPwrHighWngPortn.setStatus("current")
_Pme1008AlmlineHostLaneFaultTable_Object = MibTable
pme1008AlmlineHostLaneFaultTable = _Pme1008AlmlineHostLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 2, 152)
)
if mibBuilder.loadTexts:
    pme1008AlmlineHostLaneFaultTable.setStatus("current")
_Pme1008AlmlineHostLaneFaultEntry_Object = MibTableRow
pme1008AlmlineHostLaneFaultEntry = _Pme1008AlmlineHostLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 2, 152, 1)
)
pme1008AlmlineHostLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008AlmlineHostLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    pme1008AlmlineHostLaneFaultEntry.setStatus("current")


class _Pme1008AlmlineHostLaneFaultIndex_Type(Integer32):
    """Custom type pme1008AlmlineHostLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008AlmlineHostLaneFaultIndex_Type.__name__ = "Integer32"
_Pme1008AlmlineHostLaneFaultIndex_Object = MibTableColumn
pme1008AlmlineHostLaneFaultIndex = _Pme1008AlmlineHostLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 2, 152, 1, 1),
    _Pme1008AlmlineHostLaneFaultIndex_Type()
)
pme1008AlmlineHostLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmlineHostLaneFaultIndex.setStatus("current")
_Pme1008AlmLineInputLossOfSignalPortn_Type = EkiOnOff
_Pme1008AlmLineInputLossOfSignalPortn_Object = MibTableColumn
pme1008AlmLineInputLossOfSignalPortn = _Pme1008AlmLineInputLossOfSignalPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 2, 152, 1, 2),
    _Pme1008AlmLineInputLossOfSignalPortn_Type()
)
pme1008AlmLineInputLossOfSignalPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmLineInputLossOfSignalPortn.setStatus("current")
_Pme1008AlmLineLossOfFramePortn_Type = EkiOnOff
_Pme1008AlmLineLossOfFramePortn_Object = MibTableColumn
pme1008AlmLineLossOfFramePortn = _Pme1008AlmLineLossOfFramePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 2, 152, 1, 3),
    _Pme1008AlmLineLossOfFramePortn_Type()
)
pme1008AlmLineLossOfFramePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmLineLossOfFramePortn.setStatus("current")
_Pme1008AlmLineCrit_ObjectIdentity = ObjectIdentity
pme1008AlmLineCrit = _Pme1008AlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 3)
)
_Pme1008AlmsynthAlmLineTable_Object = MibTable
pme1008AlmsynthAlmLineTable = _Pme1008AlmsynthAlmLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 3, 24)
)
if mibBuilder.loadTexts:
    pme1008AlmsynthAlmLineTable.setStatus("current")
_Pme1008AlmsynthAlmLineEntry_Object = MibTableRow
pme1008AlmsynthAlmLineEntry = _Pme1008AlmsynthAlmLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 3, 24, 1)
)
pme1008AlmsynthAlmLineEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008AlmsynthAlmLineIndex"),
)
if mibBuilder.loadTexts:
    pme1008AlmsynthAlmLineEntry.setStatus("current")


class _Pme1008AlmsynthAlmLineIndex_Type(Integer32):
    """Custom type pme1008AlmsynthAlmLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008AlmsynthAlmLineIndex_Type.__name__ = "Integer32"
_Pme1008AlmsynthAlmLineIndex_Object = MibTableColumn
pme1008AlmsynthAlmLineIndex = _Pme1008AlmsynthAlmLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 3, 24, 1, 1),
    _Pme1008AlmsynthAlmLineIndex_Type()
)
pme1008AlmsynthAlmLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmsynthAlmLineIndex.setStatus("current")
_Pme1008AlmLineSfpAbsentPortn_Type = EkiOnOff
_Pme1008AlmLineSfpAbsentPortn_Object = MibTableColumn
pme1008AlmLineSfpAbsentPortn = _Pme1008AlmLineSfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 3, 24, 1, 2),
    _Pme1008AlmLineSfpAbsentPortn_Type()
)
pme1008AlmLineSfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmLineSfpAbsentPortn.setStatus("current")
_Pme1008AlmLineDdmAbsentPortn_Type = EkiOnOff
_Pme1008AlmLineDdmAbsentPortn_Object = MibTableColumn
pme1008AlmLineDdmAbsentPortn = _Pme1008AlmLineDdmAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 3, 24, 1, 3),
    _Pme1008AlmLineDdmAbsentPortn_Type()
)
pme1008AlmLineDdmAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmLineDdmAbsentPortn.setStatus("current")
_Pme1008AlmLineHwFailPortn_Type = EkiOnOff
_Pme1008AlmLineHwFailPortn_Object = MibTableColumn
pme1008AlmLineHwFailPortn = _Pme1008AlmLineHwFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 3, 24, 1, 5),
    _Pme1008AlmLineHwFailPortn_Type()
)
pme1008AlmLineHwFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmLineHwFailPortn.setStatus("current")
_Pme1008AlmLineTxOffPortn_Type = EkiOnOff
_Pme1008AlmLineTxOffPortn_Object = MibTableColumn
pme1008AlmLineTxOffPortn = _Pme1008AlmLineTxOffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 3, 24, 1, 6),
    _Pme1008AlmLineTxOffPortn_Type()
)
pme1008AlmLineTxOffPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmLineTxOffPortn.setStatus("current")
_Pme1008AlmLineLocalOosPortn_Type = EkiOnOff
_Pme1008AlmLineLocalOosPortn_Object = MibTableColumn
pme1008AlmLineLocalOosPortn = _Pme1008AlmLineLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 3, 24, 1, 7),
    _Pme1008AlmLineLocalOosPortn_Type()
)
pme1008AlmLineLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmLineLocalOosPortn.setStatus("current")
_Pme1008AlmUpRdiInsPortn_Type = EkiOnOff
_Pme1008AlmUpRdiInsPortn_Object = MibTableColumn
pme1008AlmUpRdiInsPortn = _Pme1008AlmUpRdiInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 3, 24, 1, 9),
    _Pme1008AlmUpRdiInsPortn_Type()
)
pme1008AlmUpRdiInsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmUpRdiInsPortn.setStatus("current")
_Pme1008AlmLineDdmWarningPortn_Type = EkiOnOff
_Pme1008AlmLineDdmWarningPortn_Object = MibTableColumn
pme1008AlmLineDdmWarningPortn = _Pme1008AlmLineDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 3, 24, 1, 10),
    _Pme1008AlmLineDdmWarningPortn_Type()
)
pme1008AlmLineDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmLineDdmWarningPortn.setStatus("current")
_Pme1008AlmLineDdmAlmPortn_Type = EkiOnOff
_Pme1008AlmLineDdmAlmPortn_Object = MibTableColumn
pme1008AlmLineDdmAlmPortn = _Pme1008AlmLineDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 3, 24, 1, 11),
    _Pme1008AlmLineDdmAlmPortn_Type()
)
pme1008AlmLineDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmLineDdmAlmPortn.setStatus("current")
_Pme1008AlmLineFailPortn_Type = EkiOnOff
_Pme1008AlmLineFailPortn_Object = MibTableColumn
pme1008AlmLineFailPortn = _Pme1008AlmLineFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 2, 3, 3, 24, 1, 13),
    _Pme1008AlmLineFailPortn_Type()
)
pme1008AlmLineFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008AlmLineFailPortn.setStatus("current")
_Pme1008measures_ObjectIdentity = ObjectIdentity
pme1008measures = _Pme1008measures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 3)
)
_Pme1008MesrOther_ObjectIdentity = ObjectIdentity
pme1008MesrOther = _Pme1008MesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 3, 1)
)
_Pme1008MesrClient_ObjectIdentity = ObjectIdentity
pme1008MesrClient = _Pme1008MesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 3, 2)
)
_Pme1008MesrclientTempTable_Object = MibTable
pme1008MesrclientTempTable = _Pme1008MesrclientTempTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 3, 2, 16)
)
if mibBuilder.loadTexts:
    pme1008MesrclientTempTable.setStatus("current")
_Pme1008MesrclientTempEntry_Object = MibTableRow
pme1008MesrclientTempEntry = _Pme1008MesrclientTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 3, 2, 16, 1)
)
pme1008MesrclientTempEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008MesrclientTempIndex"),
)
if mibBuilder.loadTexts:
    pme1008MesrclientTempEntry.setStatus("current")


class _Pme1008MesrclientTempIndex_Type(Integer32):
    """Custom type pme1008MesrclientTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008MesrclientTempIndex_Type.__name__ = "Integer32"
_Pme1008MesrclientTempIndex_Object = MibTableColumn
pme1008MesrclientTempIndex = _Pme1008MesrclientTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 3, 2, 16, 1, 1),
    _Pme1008MesrclientTempIndex_Type()
)
pme1008MesrclientTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MesrclientTempIndex.setStatus("current")


class _Pme1008MesrclientTempPortn_Type(Integer32):
    """Custom type pme1008MesrclientTempPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pme1008MesrclientTempPortn_Type.__name__ = "Integer32"
_Pme1008MesrclientTempPortn_Object = MibTableColumn
pme1008MesrclientTempPortn = _Pme1008MesrclientTempPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 3, 2, 16, 1, 2),
    _Pme1008MesrclientTempPortn_Type()
)
pme1008MesrclientTempPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MesrclientTempPortn.setStatus("current")
_Pme1008MesrclientTxBiasTable_Object = MibTable
pme1008MesrclientTxBiasTable = _Pme1008MesrclientTxBiasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 3, 2, 32)
)
if mibBuilder.loadTexts:
    pme1008MesrclientTxBiasTable.setStatus("current")
_Pme1008MesrclientTxBiasEntry_Object = MibTableRow
pme1008MesrclientTxBiasEntry = _Pme1008MesrclientTxBiasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 3, 2, 32, 1)
)
pme1008MesrclientTxBiasEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008MesrclientTxBiasIndex"),
)
if mibBuilder.loadTexts:
    pme1008MesrclientTxBiasEntry.setStatus("current")


class _Pme1008MesrclientTxBiasIndex_Type(Integer32):
    """Custom type pme1008MesrclientTxBiasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008MesrclientTxBiasIndex_Type.__name__ = "Integer32"
_Pme1008MesrclientTxBiasIndex_Object = MibTableColumn
pme1008MesrclientTxBiasIndex = _Pme1008MesrclientTxBiasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 3, 2, 32, 1, 1),
    _Pme1008MesrclientTxBiasIndex_Type()
)
pme1008MesrclientTxBiasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MesrclientTxBiasIndex.setStatus("current")


class _Pme1008MesrclientTxBiasPortn_Type(Integer32):
    """Custom type pme1008MesrclientTxBiasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pme1008MesrclientTxBiasPortn_Type.__name__ = "Integer32"
_Pme1008MesrclientTxBiasPortn_Object = MibTableColumn
pme1008MesrclientTxBiasPortn = _Pme1008MesrclientTxBiasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 3, 2, 32, 1, 2),
    _Pme1008MesrclientTxBiasPortn_Type()
)
pme1008MesrclientTxBiasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MesrclientTxBiasPortn.setStatus("current")
_Pme1008MesrclientTxPwrTable_Object = MibTable
pme1008MesrclientTxPwrTable = _Pme1008MesrclientTxPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 3, 2, 48)
)
if mibBuilder.loadTexts:
    pme1008MesrclientTxPwrTable.setStatus("current")
_Pme1008MesrclientTxPwrEntry_Object = MibTableRow
pme1008MesrclientTxPwrEntry = _Pme1008MesrclientTxPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 3, 2, 48, 1)
)
pme1008MesrclientTxPwrEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008MesrclientTxPwrIndex"),
)
if mibBuilder.loadTexts:
    pme1008MesrclientTxPwrEntry.setStatus("current")


class _Pme1008MesrclientTxPwrIndex_Type(Integer32):
    """Custom type pme1008MesrclientTxPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008MesrclientTxPwrIndex_Type.__name__ = "Integer32"
_Pme1008MesrclientTxPwrIndex_Object = MibTableColumn
pme1008MesrclientTxPwrIndex = _Pme1008MesrclientTxPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 3, 2, 48, 1, 1),
    _Pme1008MesrclientTxPwrIndex_Type()
)
pme1008MesrclientTxPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MesrclientTxPwrIndex.setStatus("current")


class _Pme1008MesrclientTxPwrPortn_Type(Integer32):
    """Custom type pme1008MesrclientTxPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pme1008MesrclientTxPwrPortn_Type.__name__ = "Integer32"
_Pme1008MesrclientTxPwrPortn_Object = MibTableColumn
pme1008MesrclientTxPwrPortn = _Pme1008MesrclientTxPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 3, 2, 48, 1, 2),
    _Pme1008MesrclientTxPwrPortn_Type()
)
pme1008MesrclientTxPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MesrclientTxPwrPortn.setStatus("current")
_Pme1008MesrclientRxPwrTable_Object = MibTable
pme1008MesrclientRxPwrTable = _Pme1008MesrclientRxPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 3, 2, 64)
)
if mibBuilder.loadTexts:
    pme1008MesrclientRxPwrTable.setStatus("current")
_Pme1008MesrclientRxPwrEntry_Object = MibTableRow
pme1008MesrclientRxPwrEntry = _Pme1008MesrclientRxPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 3, 2, 64, 1)
)
pme1008MesrclientRxPwrEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008MesrclientRxPwrIndex"),
)
if mibBuilder.loadTexts:
    pme1008MesrclientRxPwrEntry.setStatus("current")


class _Pme1008MesrclientRxPwrIndex_Type(Integer32):
    """Custom type pme1008MesrclientRxPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008MesrclientRxPwrIndex_Type.__name__ = "Integer32"
_Pme1008MesrclientRxPwrIndex_Object = MibTableColumn
pme1008MesrclientRxPwrIndex = _Pme1008MesrclientRxPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 3, 2, 64, 1, 1),
    _Pme1008MesrclientRxPwrIndex_Type()
)
pme1008MesrclientRxPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MesrclientRxPwrIndex.setStatus("current")


class _Pme1008MesrclientRxPwrPortn_Type(Integer32):
    """Custom type pme1008MesrclientRxPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pme1008MesrclientRxPwrPortn_Type.__name__ = "Integer32"
_Pme1008MesrclientRxPwrPortn_Object = MibTableColumn
pme1008MesrclientRxPwrPortn = _Pme1008MesrclientRxPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 3, 2, 64, 1, 2),
    _Pme1008MesrclientRxPwrPortn_Type()
)
pme1008MesrclientRxPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MesrclientRxPwrPortn.setStatus("current")
_Pme1008MesrLine_ObjectIdentity = ObjectIdentity
pme1008MesrLine = _Pme1008MesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 3, 3)
)
_Pme1008MesrlineTxPwrTable_Object = MibTable
pme1008MesrlineTxPwrTable = _Pme1008MesrlineTxPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 3, 3, 80)
)
if mibBuilder.loadTexts:
    pme1008MesrlineTxPwrTable.setStatus("current")
_Pme1008MesrlineTxPwrEntry_Object = MibTableRow
pme1008MesrlineTxPwrEntry = _Pme1008MesrlineTxPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 3, 3, 80, 1)
)
pme1008MesrlineTxPwrEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008MesrlineTxPwrIndex"),
)
if mibBuilder.loadTexts:
    pme1008MesrlineTxPwrEntry.setStatus("current")


class _Pme1008MesrlineTxPwrIndex_Type(Integer32):
    """Custom type pme1008MesrlineTxPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008MesrlineTxPwrIndex_Type.__name__ = "Integer32"
_Pme1008MesrlineTxPwrIndex_Object = MibTableColumn
pme1008MesrlineTxPwrIndex = _Pme1008MesrlineTxPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 3, 3, 80, 1, 1),
    _Pme1008MesrlineTxPwrIndex_Type()
)
pme1008MesrlineTxPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MesrlineTxPwrIndex.setStatus("current")


class _Pme1008MesrlineTxPwrPortn_Type(Integer32):
    """Custom type pme1008MesrlineTxPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pme1008MesrlineTxPwrPortn_Type.__name__ = "Integer32"
_Pme1008MesrlineTxPwrPortn_Object = MibTableColumn
pme1008MesrlineTxPwrPortn = _Pme1008MesrlineTxPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 3, 3, 80, 1, 2),
    _Pme1008MesrlineTxPwrPortn_Type()
)
pme1008MesrlineTxPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MesrlineTxPwrPortn.setStatus("current")
_Pme1008MesrlineTempTable_Object = MibTable
pme1008MesrlineTempTable = _Pme1008MesrlineTempTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 3, 3, 96)
)
if mibBuilder.loadTexts:
    pme1008MesrlineTempTable.setStatus("current")
_Pme1008MesrlineTempEntry_Object = MibTableRow
pme1008MesrlineTempEntry = _Pme1008MesrlineTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 3, 3, 96, 1)
)
pme1008MesrlineTempEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008MesrlineTempIndex"),
)
if mibBuilder.loadTexts:
    pme1008MesrlineTempEntry.setStatus("current")


class _Pme1008MesrlineTempIndex_Type(Integer32):
    """Custom type pme1008MesrlineTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008MesrlineTempIndex_Type.__name__ = "Integer32"
_Pme1008MesrlineTempIndex_Object = MibTableColumn
pme1008MesrlineTempIndex = _Pme1008MesrlineTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 3, 3, 96, 1, 1),
    _Pme1008MesrlineTempIndex_Type()
)
pme1008MesrlineTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MesrlineTempIndex.setStatus("current")


class _Pme1008MesrlineTempPortn_Type(Integer32):
    """Custom type pme1008MesrlineTempPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pme1008MesrlineTempPortn_Type.__name__ = "Integer32"
_Pme1008MesrlineTempPortn_Object = MibTableColumn
pme1008MesrlineTempPortn = _Pme1008MesrlineTempPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 3, 3, 96, 1, 2),
    _Pme1008MesrlineTempPortn_Type()
)
pme1008MesrlineTempPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MesrlineTempPortn.setStatus("current")
_Pme1008MesrlineTxBiasTable_Object = MibTable
pme1008MesrlineTxBiasTable = _Pme1008MesrlineTxBiasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 3, 3, 112)
)
if mibBuilder.loadTexts:
    pme1008MesrlineTxBiasTable.setStatus("current")
_Pme1008MesrlineTxBiasEntry_Object = MibTableRow
pme1008MesrlineTxBiasEntry = _Pme1008MesrlineTxBiasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 3, 3, 112, 1)
)
pme1008MesrlineTxBiasEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008MesrlineTxBiasIndex"),
)
if mibBuilder.loadTexts:
    pme1008MesrlineTxBiasEntry.setStatus("current")


class _Pme1008MesrlineTxBiasIndex_Type(Integer32):
    """Custom type pme1008MesrlineTxBiasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008MesrlineTxBiasIndex_Type.__name__ = "Integer32"
_Pme1008MesrlineTxBiasIndex_Object = MibTableColumn
pme1008MesrlineTxBiasIndex = _Pme1008MesrlineTxBiasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 3, 3, 112, 1, 1),
    _Pme1008MesrlineTxBiasIndex_Type()
)
pme1008MesrlineTxBiasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MesrlineTxBiasIndex.setStatus("current")


class _Pme1008MesrlineTxBiasPortn_Type(Integer32):
    """Custom type pme1008MesrlineTxBiasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pme1008MesrlineTxBiasPortn_Type.__name__ = "Integer32"
_Pme1008MesrlineTxBiasPortn_Object = MibTableColumn
pme1008MesrlineTxBiasPortn = _Pme1008MesrlineTxBiasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 3, 3, 112, 1, 2),
    _Pme1008MesrlineTxBiasPortn_Type()
)
pme1008MesrlineTxBiasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MesrlineTxBiasPortn.setStatus("current")
_Pme1008MesrlineRxPwrTable_Object = MibTable
pme1008MesrlineRxPwrTable = _Pme1008MesrlineRxPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 3, 3, 128)
)
if mibBuilder.loadTexts:
    pme1008MesrlineRxPwrTable.setStatus("current")
_Pme1008MesrlineRxPwrEntry_Object = MibTableRow
pme1008MesrlineRxPwrEntry = _Pme1008MesrlineRxPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 3, 3, 128, 1)
)
pme1008MesrlineRxPwrEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008MesrlineRxPwrIndex"),
)
if mibBuilder.loadTexts:
    pme1008MesrlineRxPwrEntry.setStatus("current")


class _Pme1008MesrlineRxPwrIndex_Type(Integer32):
    """Custom type pme1008MesrlineRxPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008MesrlineRxPwrIndex_Type.__name__ = "Integer32"
_Pme1008MesrlineRxPwrIndex_Object = MibTableColumn
pme1008MesrlineRxPwrIndex = _Pme1008MesrlineRxPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 3, 3, 128, 1, 1),
    _Pme1008MesrlineRxPwrIndex_Type()
)
pme1008MesrlineRxPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MesrlineRxPwrIndex.setStatus("current")


class _Pme1008MesrlineRxPwrPortn_Type(Integer32):
    """Custom type pme1008MesrlineRxPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pme1008MesrlineRxPwrPortn_Type.__name__ = "Integer32"
_Pme1008MesrlineRxPwrPortn_Object = MibTableColumn
pme1008MesrlineRxPwrPortn = _Pme1008MesrlineRxPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 3, 3, 128, 1, 2),
    _Pme1008MesrlineRxPwrPortn_Type()
)
pme1008MesrlineRxPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MesrlineRxPwrPortn.setStatus("current")
_Pme1008counters_ObjectIdentity = ObjectIdentity
pme1008counters = _Pme1008counters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 4)
)
_Pme1008CntOther_ObjectIdentity = ObjectIdentity
pme1008CntOther = _Pme1008CntOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 4, 1)
)
_Pme1008CntClient_ObjectIdentity = ObjectIdentity
pme1008CntClient = _Pme1008CntClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 4, 2)
)
_Pme1008CntclientCbipCounterTable_Object = MibTable
pme1008CntclientCbipCounterTable = _Pme1008CntclientCbipCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 4, 2, 96)
)
if mibBuilder.loadTexts:
    pme1008CntclientCbipCounterTable.setStatus("current")
_Pme1008CntclientCbipCounterEntry_Object = MibTableRow
pme1008CntclientCbipCounterEntry = _Pme1008CntclientCbipCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 4, 2, 96, 1)
)
pme1008CntclientCbipCounterEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008CntclientCbipCounterIndex"),
)
if mibBuilder.loadTexts:
    pme1008CntclientCbipCounterEntry.setStatus("current")


class _Pme1008CntclientCbipCounterIndex_Type(Integer32):
    """Custom type pme1008CntclientCbipCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008CntclientCbipCounterIndex_Type.__name__ = "Integer32"
_Pme1008CntclientCbipCounterIndex_Object = MibTableColumn
pme1008CntclientCbipCounterIndex = _Pme1008CntclientCbipCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 4, 2, 96, 1, 1),
    _Pme1008CntclientCbipCounterIndex_Type()
)
pme1008CntclientCbipCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CntclientCbipCounterIndex.setStatus("current")
_Pme1008CntclientCbipCounterValuePortn_Type = Counter32
_Pme1008CntclientCbipCounterValuePortn_Object = MibTableColumn
pme1008CntclientCbipCounterValuePortn = _Pme1008CntclientCbipCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 4, 2, 96, 1, 2),
    _Pme1008CntclientCbipCounterValuePortn_Type()
)
pme1008CntclientCbipCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CntclientCbipCounterValuePortn.setStatus("current")
_Pme1008CntclientCbipCounterErrorPortn_Type = EkiOnOff
_Pme1008CntclientCbipCounterErrorPortn_Object = MibTableColumn
pme1008CntclientCbipCounterErrorPortn = _Pme1008CntclientCbipCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 4, 2, 96, 1, 3),
    _Pme1008CntclientCbipCounterErrorPortn_Type()
)
pme1008CntclientCbipCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CntclientCbipCounterErrorPortn.setStatus("current")
_Pme1008CntclientCbipCounterOverloadPortn_Type = EkiOnOff
_Pme1008CntclientCbipCounterOverloadPortn_Object = MibTableColumn
pme1008CntclientCbipCounterOverloadPortn = _Pme1008CntclientCbipCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 4, 2, 96, 1, 4),
    _Pme1008CntclientCbipCounterOverloadPortn_Type()
)
pme1008CntclientCbipCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CntclientCbipCounterOverloadPortn.setStatus("current")
_Pme1008CntLine_ObjectIdentity = ObjectIdentity
pme1008CntLine = _Pme1008CntLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 4, 3)
)
_Pme1008CntlocalLineSmBip8ErrorCounterTable_Object = MibTable
pme1008CntlocalLineSmBip8ErrorCounterTable = _Pme1008CntlocalLineSmBip8ErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 4, 3, 192)
)
if mibBuilder.loadTexts:
    pme1008CntlocalLineSmBip8ErrorCounterTable.setStatus("current")
_Pme1008CntlocalLineSmBip8ErrorCounterEntry_Object = MibTableRow
pme1008CntlocalLineSmBip8ErrorCounterEntry = _Pme1008CntlocalLineSmBip8ErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 4, 3, 192, 1)
)
pme1008CntlocalLineSmBip8ErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008CntlocalLineSmBip8ErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pme1008CntlocalLineSmBip8ErrorCounterEntry.setStatus("current")


class _Pme1008CntlocalLineSmBip8ErrorCounterIndex_Type(Integer32):
    """Custom type pme1008CntlocalLineSmBip8ErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008CntlocalLineSmBip8ErrorCounterIndex_Type.__name__ = "Integer32"
_Pme1008CntlocalLineSmBip8ErrorCounterIndex_Object = MibTableColumn
pme1008CntlocalLineSmBip8ErrorCounterIndex = _Pme1008CntlocalLineSmBip8ErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 4, 3, 192, 1, 1),
    _Pme1008CntlocalLineSmBip8ErrorCounterIndex_Type()
)
pme1008CntlocalLineSmBip8ErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CntlocalLineSmBip8ErrorCounterIndex.setStatus("current")
_Pme1008CntlocalLineSmBip8ErrorCounterValuePortn_Type = Counter32
_Pme1008CntlocalLineSmBip8ErrorCounterValuePortn_Object = MibTableColumn
pme1008CntlocalLineSmBip8ErrorCounterValuePortn = _Pme1008CntlocalLineSmBip8ErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 4, 3, 192, 1, 2),
    _Pme1008CntlocalLineSmBip8ErrorCounterValuePortn_Type()
)
pme1008CntlocalLineSmBip8ErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CntlocalLineSmBip8ErrorCounterValuePortn.setStatus("current")
_Pme1008CntlocalLineSmBip8ErrorCounterErrorPortn_Type = EkiOnOff
_Pme1008CntlocalLineSmBip8ErrorCounterErrorPortn_Object = MibTableColumn
pme1008CntlocalLineSmBip8ErrorCounterErrorPortn = _Pme1008CntlocalLineSmBip8ErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 4, 3, 192, 1, 3),
    _Pme1008CntlocalLineSmBip8ErrorCounterErrorPortn_Type()
)
pme1008CntlocalLineSmBip8ErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CntlocalLineSmBip8ErrorCounterErrorPortn.setStatus("current")
_Pme1008CntlocalLineSmBip8ErrorCounterOverloadPortn_Type = EkiOnOff
_Pme1008CntlocalLineSmBip8ErrorCounterOverloadPortn_Object = MibTableColumn
pme1008CntlocalLineSmBip8ErrorCounterOverloadPortn = _Pme1008CntlocalLineSmBip8ErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 4, 3, 192, 1, 4),
    _Pme1008CntlocalLineSmBip8ErrorCounterOverloadPortn_Type()
)
pme1008CntlocalLineSmBip8ErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CntlocalLineSmBip8ErrorCounterOverloadPortn.setStatus("current")
_Pme1008CntlineDfrmTimCntTable_Object = MibTable
pme1008CntlineDfrmTimCntTable = _Pme1008CntlineDfrmTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 4, 3, 216)
)
if mibBuilder.loadTexts:
    pme1008CntlineDfrmTimCntTable.setStatus("current")
_Pme1008CntlineDfrmTimCntEntry_Object = MibTableRow
pme1008CntlineDfrmTimCntEntry = _Pme1008CntlineDfrmTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 4, 3, 216, 1)
)
pme1008CntlineDfrmTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008CntlineDfrmTimCntIndex"),
)
if mibBuilder.loadTexts:
    pme1008CntlineDfrmTimCntEntry.setStatus("current")


class _Pme1008CntlineDfrmTimCntIndex_Type(Integer32):
    """Custom type pme1008CntlineDfrmTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008CntlineDfrmTimCntIndex_Type.__name__ = "Integer32"
_Pme1008CntlineDfrmTimCntIndex_Object = MibTableColumn
pme1008CntlineDfrmTimCntIndex = _Pme1008CntlineDfrmTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 4, 3, 216, 1, 1),
    _Pme1008CntlineDfrmTimCntIndex_Type()
)
pme1008CntlineDfrmTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CntlineDfrmTimCntIndex.setStatus("current")
_Pme1008CntlineDfrmTimCntValuePortn_Type = Counter32
_Pme1008CntlineDfrmTimCntValuePortn_Object = MibTableColumn
pme1008CntlineDfrmTimCntValuePortn = _Pme1008CntlineDfrmTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 4, 3, 216, 1, 2),
    _Pme1008CntlineDfrmTimCntValuePortn_Type()
)
pme1008CntlineDfrmTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CntlineDfrmTimCntValuePortn.setStatus("current")
_Pme1008CntlineDfrmTimCntErrorPortn_Type = EkiOnOff
_Pme1008CntlineDfrmTimCntErrorPortn_Object = MibTableColumn
pme1008CntlineDfrmTimCntErrorPortn = _Pme1008CntlineDfrmTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 4, 3, 216, 1, 3),
    _Pme1008CntlineDfrmTimCntErrorPortn_Type()
)
pme1008CntlineDfrmTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CntlineDfrmTimCntErrorPortn.setStatus("current")
_Pme1008CntlineDfrmTimCntOverloadPortn_Type = EkiOnOff
_Pme1008CntlineDfrmTimCntOverloadPortn_Object = MibTableColumn
pme1008CntlineDfrmTimCntOverloadPortn = _Pme1008CntlineDfrmTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 4, 3, 216, 1, 4),
    _Pme1008CntlineDfrmTimCntOverloadPortn_Type()
)
pme1008CntlineDfrmTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CntlineDfrmTimCntOverloadPortn.setStatus("current")
_Pme1008CntCountersReset_Type = EkiOnOff
_Pme1008CntCountersReset_Object = MibScalar
pme1008CntCountersReset = _Pme1008CntCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 4, 259),
    _Pme1008CntCountersReset_Type()
)
pme1008CntCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CntCountersReset.setStatus("current")
_Pme1008CntCountersStop_Type = EkiOnOff
_Pme1008CntCountersStop_Object = MibScalar
pme1008CntCountersStop = _Pme1008CntCountersStop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 4, 260),
    _Pme1008CntCountersStop_Type()
)
pme1008CntCountersStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CntCountersStop.setStatus("current")
_Pme1008controlsWrite_ObjectIdentity = ObjectIdentity
pme1008controlsWrite = _Pme1008controlsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6)
)
_Pme1008CtrlOther_ObjectIdentity = ObjectIdentity
pme1008CtrlOther = _Pme1008CtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 1)
)
_Pme1008CtrlconfMgnt1_ObjectIdentity = ObjectIdentity
pme1008CtrlconfMgnt1 = _Pme1008CtrlconfMgnt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 1, 1)
)
_Pme1008CtrlConf1Load1_Type = EkiOnOff
_Pme1008CtrlConf1Load1_Object = MibScalar
pme1008CtrlConf1Load1 = _Pme1008CtrlConf1Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 1, 1, 1),
    _Pme1008CtrlConf1Load1_Type()
)
pme1008CtrlConf1Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CtrlConf1Load1.setStatus("current")
_Pme1008CtrlConf2Load1_Type = EkiOnOff
_Pme1008CtrlConf2Load1_Object = MibScalar
pme1008CtrlConf2Load1 = _Pme1008CtrlConf2Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 1, 1, 2),
    _Pme1008CtrlConf2Load1_Type()
)
pme1008CtrlConf2Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CtrlConf2Load1.setStatus("current")
_Pme1008CtrlConf2Flash1_Type = EkiOnOff
_Pme1008CtrlConf2Flash1_Object = MibScalar
pme1008CtrlConf2Flash1 = _Pme1008CtrlConf2Flash1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 1, 1, 10),
    _Pme1008CtrlConf2Flash1_Type()
)
pme1008CtrlConf2Flash1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CtrlConf2Flash1.setStatus("current")
_Pme1008CtrlConf2Clear1_Type = EkiOnOff
_Pme1008CtrlConf2Clear1_Object = MibScalar
pme1008CtrlConf2Clear1 = _Pme1008CtrlConf2Clear1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 1, 1, 14),
    _Pme1008CtrlConf2Clear1_Type()
)
pme1008CtrlConf2Clear1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CtrlConf2Clear1.setStatus("current")
_Pme1008Ctrlsynth4_ObjectIdentity = ObjectIdentity
pme1008Ctrlsynth4 = _Pme1008Ctrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 1, 4)
)
_Pme1008CtrlCorrelatOn_Type = EkiOnOff
_Pme1008CtrlCorrelatOn_Object = MibScalar
pme1008CtrlCorrelatOn = _Pme1008CtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 1, 4, 1),
    _Pme1008CtrlCorrelatOn_Type()
)
pme1008CtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CtrlCorrelatOn.setStatus("current")
_Pme1008CtrlCorrelatOff_Type = EkiOnOff
_Pme1008CtrlCorrelatOff_Object = MibScalar
pme1008CtrlCorrelatOff = _Pme1008CtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 1, 4, 2),
    _Pme1008CtrlCorrelatOff_Type()
)
pme1008CtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CtrlCorrelatOff.setStatus("current")
_Pme1008CtrlswMgnt_ObjectIdentity = ObjectIdentity
pme1008CtrlswMgnt = _Pme1008CtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 1, 5)
)
_Pme1008CtrlColdReset_Type = EkiOnOff
_Pme1008CtrlColdReset_Object = MibScalar
pme1008CtrlColdReset = _Pme1008CtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 1, 5, 2),
    _Pme1008CtrlColdReset_Type()
)
pme1008CtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CtrlColdReset.setStatus("current")
_Pme1008CtrlWarmReset_Type = EkiOnOff
_Pme1008CtrlWarmReset_Object = MibScalar
pme1008CtrlWarmReset = _Pme1008CtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 1, 5, 3),
    _Pme1008CtrlWarmReset_Type()
)
pme1008CtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CtrlWarmReset.setStatus("current")
_Pme1008CtrlLoadSwBank1_Type = EkiOnOff
_Pme1008CtrlLoadSwBank1_Object = MibScalar
pme1008CtrlLoadSwBank1 = _Pme1008CtrlLoadSwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 1, 5, 5),
    _Pme1008CtrlLoadSwBank1_Type()
)
pme1008CtrlLoadSwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CtrlLoadSwBank1.setStatus("current")
_Pme1008CtrlLoadSwBank2_Type = EkiOnOff
_Pme1008CtrlLoadSwBank2_Object = MibScalar
pme1008CtrlLoadSwBank2 = _Pme1008CtrlLoadSwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 1, 5, 6),
    _Pme1008CtrlLoadSwBank2_Type()
)
pme1008CtrlLoadSwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CtrlLoadSwBank2.setStatus("current")
_Pme1008CtrlgwMgnt_ObjectIdentity = ObjectIdentity
pme1008CtrlgwMgnt = _Pme1008CtrlgwMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 1, 6)
)
_Pme1008CtrlCurrentGwReset_Type = EkiOnOff
_Pme1008CtrlCurrentGwReset_Object = MibScalar
pme1008CtrlCurrentGwReset = _Pme1008CtrlCurrentGwReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 1, 6, 1),
    _Pme1008CtrlCurrentGwReset_Type()
)
pme1008CtrlCurrentGwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CtrlCurrentGwReset.setStatus("current")
_Pme1008CtrlLoadGwBank1_Type = EkiOnOff
_Pme1008CtrlLoadGwBank1_Object = MibScalar
pme1008CtrlLoadGwBank1 = _Pme1008CtrlLoadGwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 1, 6, 5),
    _Pme1008CtrlLoadGwBank1_Type()
)
pme1008CtrlLoadGwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CtrlLoadGwBank1.setStatus("current")
_Pme1008CtrlLoadGwBank2_Type = EkiOnOff
_Pme1008CtrlLoadGwBank2_Object = MibScalar
pme1008CtrlLoadGwBank2 = _Pme1008CtrlLoadGwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 1, 6, 6),
    _Pme1008CtrlLoadGwBank2_Type()
)
pme1008CtrlLoadGwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CtrlLoadGwBank2.setStatus("current")
_Pme1008CtrlLoadGwBank3_Type = EkiOnOff
_Pme1008CtrlLoadGwBank3_Object = MibScalar
pme1008CtrlLoadGwBank3 = _Pme1008CtrlLoadGwBank3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 1, 6, 7),
    _Pme1008CtrlLoadGwBank3_Type()
)
pme1008CtrlLoadGwBank3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CtrlLoadGwBank3.setStatus("current")
_Pme1008CtrlLoadGwBank4_Type = EkiOnOff
_Pme1008CtrlLoadGwBank4_Object = MibScalar
pme1008CtrlLoadGwBank4 = _Pme1008CtrlLoadGwBank4_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 1, 6, 8),
    _Pme1008CtrlLoadGwBank4_Type()
)
pme1008CtrlLoadGwBank4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CtrlLoadGwBank4.setStatus("current")
_Pme1008CtrlledTest_ObjectIdentity = ObjectIdentity
pme1008CtrlledTest = _Pme1008CtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 1, 192)
)
_Pme1008CtrlGreenLed_Type = EkiOnOff
_Pme1008CtrlGreenLed_Object = MibScalar
pme1008CtrlGreenLed = _Pme1008CtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 1, 192, 1),
    _Pme1008CtrlGreenLed_Type()
)
pme1008CtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CtrlGreenLed.setStatus("current")
_Pme1008CtrlRedLed_Type = EkiOnOff
_Pme1008CtrlRedLed_Object = MibScalar
pme1008CtrlRedLed = _Pme1008CtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 1, 192, 2),
    _Pme1008CtrlRedLed_Type()
)
pme1008CtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CtrlRedLed.setStatus("current")
_Pme1008CtrlLedOff_Type = EkiOnOff
_Pme1008CtrlLedOff_Object = MibScalar
pme1008CtrlLedOff = _Pme1008CtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 1, 192, 3),
    _Pme1008CtrlLedOff_Type()
)
pme1008CtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CtrlLedOff.setStatus("current")
_Pme1008CtrlClient_ObjectIdentity = ObjectIdentity
pme1008CtrlClient = _Pme1008CtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 2)
)
_Pme1008CtrlaccessLoopTable_Object = MibTable
pme1008CtrlaccessLoopTable = _Pme1008CtrlaccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 2, 16)
)
if mibBuilder.loadTexts:
    pme1008CtrlaccessLoopTable.setStatus("current")
_Pme1008CtrlaccessLoopEntry_Object = MibTableRow
pme1008CtrlaccessLoopEntry = _Pme1008CtrlaccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 2, 16, 1)
)
pme1008CtrlaccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008CtrlaccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pme1008CtrlaccessLoopEntry.setStatus("current")


class _Pme1008CtrlaccessLoopIndex_Type(Integer32):
    """Custom type pme1008CtrlaccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008CtrlaccessLoopIndex_Type.__name__ = "Integer32"
_Pme1008CtrlaccessLoopIndex_Object = MibTableColumn
pme1008CtrlaccessLoopIndex = _Pme1008CtrlaccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 2, 16, 1, 1),
    _Pme1008CtrlaccessLoopIndex_Type()
)
pme1008CtrlaccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CtrlaccessLoopIndex.setStatus("current")
_Pme1008CtrlaccessLoopPortn_Type = EkiState
_Pme1008CtrlaccessLoopPortn_Object = MibTableColumn
pme1008CtrlaccessLoopPortn = _Pme1008CtrlaccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 2, 16, 1, 2),
    _Pme1008CtrlaccessLoopPortn_Type()
)
pme1008CtrlaccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CtrlaccessLoopPortn.setStatus("current")
_Pme1008CtrlclientLoopToLineTable_Object = MibTable
pme1008CtrlclientLoopToLineTable = _Pme1008CtrlclientLoopToLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 2, 17)
)
if mibBuilder.loadTexts:
    pme1008CtrlclientLoopToLineTable.setStatus("current")
_Pme1008CtrlclientLoopToLineEntry_Object = MibTableRow
pme1008CtrlclientLoopToLineEntry = _Pme1008CtrlclientLoopToLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 2, 17, 1)
)
pme1008CtrlclientLoopToLineEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008CtrlclientLoopToLineIndex"),
)
if mibBuilder.loadTexts:
    pme1008CtrlclientLoopToLineEntry.setStatus("current")


class _Pme1008CtrlclientLoopToLineIndex_Type(Integer32):
    """Custom type pme1008CtrlclientLoopToLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008CtrlclientLoopToLineIndex_Type.__name__ = "Integer32"
_Pme1008CtrlclientLoopToLineIndex_Object = MibTableColumn
pme1008CtrlclientLoopToLineIndex = _Pme1008CtrlclientLoopToLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 2, 17, 1, 1),
    _Pme1008CtrlclientLoopToLineIndex_Type()
)
pme1008CtrlclientLoopToLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CtrlclientLoopToLineIndex.setStatus("current")
_Pme1008CtrlclientLoopToLinePortn_Type = EkiState
_Pme1008CtrlclientLoopToLinePortn_Object = MibTableColumn
pme1008CtrlclientLoopToLinePortn = _Pme1008CtrlclientLoopToLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 2, 17, 1, 2),
    _Pme1008CtrlclientLoopToLinePortn_Type()
)
pme1008CtrlclientLoopToLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CtrlclientLoopToLinePortn.setStatus("current")
_Pme1008CtrlcsfUpInsTable_Object = MibTable
pme1008CtrlcsfUpInsTable = _Pme1008CtrlcsfUpInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 2, 21)
)
if mibBuilder.loadTexts:
    pme1008CtrlcsfUpInsTable.setStatus("current")
_Pme1008CtrlcsfUpInsEntry_Object = MibTableRow
pme1008CtrlcsfUpInsEntry = _Pme1008CtrlcsfUpInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 2, 21, 1)
)
pme1008CtrlcsfUpInsEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008CtrlcsfUpInsIndex"),
)
if mibBuilder.loadTexts:
    pme1008CtrlcsfUpInsEntry.setStatus("current")


class _Pme1008CtrlcsfUpInsIndex_Type(Integer32):
    """Custom type pme1008CtrlcsfUpInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008CtrlcsfUpInsIndex_Type.__name__ = "Integer32"
_Pme1008CtrlcsfUpInsIndex_Object = MibTableColumn
pme1008CtrlcsfUpInsIndex = _Pme1008CtrlcsfUpInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 2, 21, 1, 1),
    _Pme1008CtrlcsfUpInsIndex_Type()
)
pme1008CtrlcsfUpInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CtrlcsfUpInsIndex.setStatus("current")
_Pme1008CtrlcsfUpInsPortn_Type = EkiState
_Pme1008CtrlcsfUpInsPortn_Object = MibTableColumn
pme1008CtrlcsfUpInsPortn = _Pme1008CtrlcsfUpInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 2, 21, 1, 2),
    _Pme1008CtrlcsfUpInsPortn_Type()
)
pme1008CtrlcsfUpInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CtrlcsfUpInsPortn.setStatus("current")
_Pme1008CtrlcaisDwInsTable_Object = MibTable
pme1008CtrlcaisDwInsTable = _Pme1008CtrlcaisDwInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 2, 22)
)
if mibBuilder.loadTexts:
    pme1008CtrlcaisDwInsTable.setStatus("current")
_Pme1008CtrlcaisDwInsEntry_Object = MibTableRow
pme1008CtrlcaisDwInsEntry = _Pme1008CtrlcaisDwInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 2, 22, 1)
)
pme1008CtrlcaisDwInsEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008CtrlcaisDwInsIndex"),
)
if mibBuilder.loadTexts:
    pme1008CtrlcaisDwInsEntry.setStatus("current")


class _Pme1008CtrlcaisDwInsIndex_Type(Integer32):
    """Custom type pme1008CtrlcaisDwInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008CtrlcaisDwInsIndex_Type.__name__ = "Integer32"
_Pme1008CtrlcaisDwInsIndex_Object = MibTableColumn
pme1008CtrlcaisDwInsIndex = _Pme1008CtrlcaisDwInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 2, 22, 1, 1),
    _Pme1008CtrlcaisDwInsIndex_Type()
)
pme1008CtrlcaisDwInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CtrlcaisDwInsIndex.setStatus("current")
_Pme1008CtrlcaisDwInsPortn_Type = EkiState
_Pme1008CtrlcaisDwInsPortn_Object = MibTableColumn
pme1008CtrlcaisDwInsPortn = _Pme1008CtrlcaisDwInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 2, 22, 1, 2),
    _Pme1008CtrlcaisDwInsPortn_Type()
)
pme1008CtrlcaisDwInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CtrlcaisDwInsPortn.setStatus("current")
_Pme1008CtrlclientOciTable_Object = MibTable
pme1008CtrlclientOciTable = _Pme1008CtrlclientOciTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 2, 23)
)
if mibBuilder.loadTexts:
    pme1008CtrlclientOciTable.setStatus("current")
_Pme1008CtrlclientOciEntry_Object = MibTableRow
pme1008CtrlclientOciEntry = _Pme1008CtrlclientOciEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 2, 23, 1)
)
pme1008CtrlclientOciEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008CtrlclientOciIndex"),
)
if mibBuilder.loadTexts:
    pme1008CtrlclientOciEntry.setStatus("current")


class _Pme1008CtrlclientOciIndex_Type(Integer32):
    """Custom type pme1008CtrlclientOciIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008CtrlclientOciIndex_Type.__name__ = "Integer32"
_Pme1008CtrlclientOciIndex_Object = MibTableColumn
pme1008CtrlclientOciIndex = _Pme1008CtrlclientOciIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 2, 23, 1, 1),
    _Pme1008CtrlclientOciIndex_Type()
)
pme1008CtrlclientOciIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CtrlclientOciIndex.setStatus("current")
_Pme1008CtrlclientOciPortn_Type = EkiState
_Pme1008CtrlclientOciPortn_Object = MibTableColumn
pme1008CtrlclientOciPortn = _Pme1008CtrlclientOciPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 2, 23, 1, 2),
    _Pme1008CtrlclientOciPortn_Type()
)
pme1008CtrlclientOciPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CtrlclientOciPortn.setStatus("current")
_Pme1008CtrlclientLckTable_Object = MibTable
pme1008CtrlclientLckTable = _Pme1008CtrlclientLckTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 2, 24)
)
if mibBuilder.loadTexts:
    pme1008CtrlclientLckTable.setStatus("current")
_Pme1008CtrlclientLckEntry_Object = MibTableRow
pme1008CtrlclientLckEntry = _Pme1008CtrlclientLckEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 2, 24, 1)
)
pme1008CtrlclientLckEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008CtrlclientLckIndex"),
)
if mibBuilder.loadTexts:
    pme1008CtrlclientLckEntry.setStatus("current")


class _Pme1008CtrlclientLckIndex_Type(Integer32):
    """Custom type pme1008CtrlclientLckIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008CtrlclientLckIndex_Type.__name__ = "Integer32"
_Pme1008CtrlclientLckIndex_Object = MibTableColumn
pme1008CtrlclientLckIndex = _Pme1008CtrlclientLckIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 2, 24, 1, 1),
    _Pme1008CtrlclientLckIndex_Type()
)
pme1008CtrlclientLckIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CtrlclientLckIndex.setStatus("current")
_Pme1008CtrlclientLckPortn_Type = EkiState
_Pme1008CtrlclientLckPortn_Object = MibTableColumn
pme1008CtrlclientLckPortn = _Pme1008CtrlclientLckPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 2, 24, 1, 2),
    _Pme1008CtrlclientLckPortn_Type()
)
pme1008CtrlclientLckPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CtrlclientLckPortn.setStatus("current")
_Pme1008CtrlclientAisTable_Object = MibTable
pme1008CtrlclientAisTable = _Pme1008CtrlclientAisTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 2, 25)
)
if mibBuilder.loadTexts:
    pme1008CtrlclientAisTable.setStatus("current")
_Pme1008CtrlclientAisEntry_Object = MibTableRow
pme1008CtrlclientAisEntry = _Pme1008CtrlclientAisEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 2, 25, 1)
)
pme1008CtrlclientAisEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008CtrlclientAisIndex"),
)
if mibBuilder.loadTexts:
    pme1008CtrlclientAisEntry.setStatus("current")


class _Pme1008CtrlclientAisIndex_Type(Integer32):
    """Custom type pme1008CtrlclientAisIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008CtrlclientAisIndex_Type.__name__ = "Integer32"
_Pme1008CtrlclientAisIndex_Object = MibTableColumn
pme1008CtrlclientAisIndex = _Pme1008CtrlclientAisIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 2, 25, 1, 1),
    _Pme1008CtrlclientAisIndex_Type()
)
pme1008CtrlclientAisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CtrlclientAisIndex.setStatus("current")
_Pme1008CtrlclientAisPortn_Type = EkiState
_Pme1008CtrlclientAisPortn_Object = MibTableColumn
pme1008CtrlclientAisPortn = _Pme1008CtrlclientAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 2, 25, 1, 2),
    _Pme1008CtrlclientAisPortn_Type()
)
pme1008CtrlclientAisPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CtrlclientAisPortn.setStatus("current")
_Pme1008CtrlclientBdiTable_Object = MibTable
pme1008CtrlclientBdiTable = _Pme1008CtrlclientBdiTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 2, 26)
)
if mibBuilder.loadTexts:
    pme1008CtrlclientBdiTable.setStatus("current")
_Pme1008CtrlclientBdiEntry_Object = MibTableRow
pme1008CtrlclientBdiEntry = _Pme1008CtrlclientBdiEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 2, 26, 1)
)
pme1008CtrlclientBdiEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008CtrlclientBdiIndex"),
)
if mibBuilder.loadTexts:
    pme1008CtrlclientBdiEntry.setStatus("current")


class _Pme1008CtrlclientBdiIndex_Type(Integer32):
    """Custom type pme1008CtrlclientBdiIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008CtrlclientBdiIndex_Type.__name__ = "Integer32"
_Pme1008CtrlclientBdiIndex_Object = MibTableColumn
pme1008CtrlclientBdiIndex = _Pme1008CtrlclientBdiIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 2, 26, 1, 1),
    _Pme1008CtrlclientBdiIndex_Type()
)
pme1008CtrlclientBdiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CtrlclientBdiIndex.setStatus("current")
_Pme1008CtrlclientBdiPortn_Type = EkiState
_Pme1008CtrlclientBdiPortn_Object = MibTableColumn
pme1008CtrlclientBdiPortn = _Pme1008CtrlclientBdiPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 2, 26, 1, 2),
    _Pme1008CtrlclientBdiPortn_Type()
)
pme1008CtrlclientBdiPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CtrlclientBdiPortn.setStatus("current")
_Pme1008CtrlLine_ObjectIdentity = ObjectIdentity
pme1008CtrlLine = _Pme1008CtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 3)
)
_Pme1008CtrlcommAccessLoopTable_Object = MibTable
pme1008CtrlcommAccessLoopTable = _Pme1008CtrlcommAccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 3, 64)
)
if mibBuilder.loadTexts:
    pme1008CtrlcommAccessLoopTable.setStatus("current")
_Pme1008CtrlcommAccessLoopEntry_Object = MibTableRow
pme1008CtrlcommAccessLoopEntry = _Pme1008CtrlcommAccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 3, 64, 1)
)
pme1008CtrlcommAccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008CtrlcommAccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pme1008CtrlcommAccessLoopEntry.setStatus("current")


class _Pme1008CtrlcommAccessLoopIndex_Type(Integer32):
    """Custom type pme1008CtrlcommAccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008CtrlcommAccessLoopIndex_Type.__name__ = "Integer32"
_Pme1008CtrlcommAccessLoopIndex_Object = MibTableColumn
pme1008CtrlcommAccessLoopIndex = _Pme1008CtrlcommAccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 3, 64, 1, 1),
    _Pme1008CtrlcommAccessLoopIndex_Type()
)
pme1008CtrlcommAccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CtrlcommAccessLoopIndex.setStatus("current")
_Pme1008CtrlcommAccessLoopPortn_Type = EkiState
_Pme1008CtrlcommAccessLoopPortn_Object = MibTableColumn
pme1008CtrlcommAccessLoopPortn = _Pme1008CtrlcommAccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 3, 64, 1, 2),
    _Pme1008CtrlcommAccessLoopPortn_Type()
)
pme1008CtrlcommAccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CtrlcommAccessLoopPortn.setStatus("current")
_Pme1008CtrllineLoopTable_Object = MibTable
pme1008CtrllineLoopTable = _Pme1008CtrllineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 3, 66)
)
if mibBuilder.loadTexts:
    pme1008CtrllineLoopTable.setStatus("current")
_Pme1008CtrllineLoopEntry_Object = MibTableRow
pme1008CtrllineLoopEntry = _Pme1008CtrllineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 3, 66, 1)
)
pme1008CtrllineLoopEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008CtrllineLoopIndex"),
)
if mibBuilder.loadTexts:
    pme1008CtrllineLoopEntry.setStatus("current")


class _Pme1008CtrllineLoopIndex_Type(Integer32):
    """Custom type pme1008CtrllineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008CtrllineLoopIndex_Type.__name__ = "Integer32"
_Pme1008CtrllineLoopIndex_Object = MibTableColumn
pme1008CtrllineLoopIndex = _Pme1008CtrllineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 3, 66, 1, 1),
    _Pme1008CtrllineLoopIndex_Type()
)
pme1008CtrllineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CtrllineLoopIndex.setStatus("current")
_Pme1008CtrllineLoopPortn_Type = EkiState
_Pme1008CtrllineLoopPortn_Object = MibTableColumn
pme1008CtrllineLoopPortn = _Pme1008CtrllineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 3, 66, 1, 2),
    _Pme1008CtrllineLoopPortn_Type()
)
pme1008CtrllineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CtrllineLoopPortn.setStatus("current")
_Pme1008CtrlfecDisableTable_Object = MibTable
pme1008CtrlfecDisableTable = _Pme1008CtrlfecDisableTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 3, 69)
)
if mibBuilder.loadTexts:
    pme1008CtrlfecDisableTable.setStatus("current")
_Pme1008CtrlfecDisableEntry_Object = MibTableRow
pme1008CtrlfecDisableEntry = _Pme1008CtrlfecDisableEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 3, 69, 1)
)
pme1008CtrlfecDisableEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008CtrlfecDisableIndex"),
)
if mibBuilder.loadTexts:
    pme1008CtrlfecDisableEntry.setStatus("current")


class _Pme1008CtrlfecDisableIndex_Type(Integer32):
    """Custom type pme1008CtrlfecDisableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008CtrlfecDisableIndex_Type.__name__ = "Integer32"
_Pme1008CtrlfecDisableIndex_Object = MibTableColumn
pme1008CtrlfecDisableIndex = _Pme1008CtrlfecDisableIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 3, 69, 1, 1),
    _Pme1008CtrlfecDisableIndex_Type()
)
pme1008CtrlfecDisableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CtrlfecDisableIndex.setStatus("current")
_Pme1008CtrlfecDisablePortn_Type = EkiState
_Pme1008CtrlfecDisablePortn_Object = MibTableColumn
pme1008CtrlfecDisablePortn = _Pme1008CtrlfecDisablePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 3, 69, 1, 2),
    _Pme1008CtrlfecDisablePortn_Type()
)
pme1008CtrlfecDisablePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CtrlfecDisablePortn.setStatus("current")
_Pme1008CtrllineBdiTable_Object = MibTable
pme1008CtrllineBdiTable = _Pme1008CtrllineBdiTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 3, 70)
)
if mibBuilder.loadTexts:
    pme1008CtrllineBdiTable.setStatus("current")
_Pme1008CtrllineBdiEntry_Object = MibTableRow
pme1008CtrllineBdiEntry = _Pme1008CtrllineBdiEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 3, 70, 1)
)
pme1008CtrllineBdiEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008CtrllineBdiIndex"),
)
if mibBuilder.loadTexts:
    pme1008CtrllineBdiEntry.setStatus("current")


class _Pme1008CtrllineBdiIndex_Type(Integer32):
    """Custom type pme1008CtrllineBdiIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008CtrllineBdiIndex_Type.__name__ = "Integer32"
_Pme1008CtrllineBdiIndex_Object = MibTableColumn
pme1008CtrllineBdiIndex = _Pme1008CtrllineBdiIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 3, 70, 1, 1),
    _Pme1008CtrllineBdiIndex_Type()
)
pme1008CtrllineBdiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CtrllineBdiIndex.setStatus("current")
_Pme1008CtrllineBdiPortn_Type = EkiState
_Pme1008CtrllineBdiPortn_Object = MibTableColumn
pme1008CtrllineBdiPortn = _Pme1008CtrllineBdiPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 6, 3, 70, 1, 2),
    _Pme1008CtrllineBdiPortn_Type()
)
pme1008CtrllineBdiPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CtrllineBdiPortn.setStatus("current")
_Pme1008ri_ObjectIdentity = ObjectIdentity
pme1008ri = _Pme1008ri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 7)
)
_Pme1008riTable_ObjectIdentity = ObjectIdentity
pme1008riTable = _Pme1008riTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 7, 1)
)
_Pme1008RinvSfpTable_Object = MibTable
pme1008RinvSfpTable = _Pme1008RinvSfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 7, 1, 1)
)
if mibBuilder.loadTexts:
    pme1008RinvSfpTable.setStatus("current")
_Pme1008RinvSfpEntry_Object = MibTableRow
pme1008RinvSfpEntry = _Pme1008RinvSfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 7, 1, 1, 1)
)
pme1008RinvSfpEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008RinvSfpIndex"),
)
if mibBuilder.loadTexts:
    pme1008RinvSfpEntry.setStatus("current")


class _Pme1008RinvSfpIndex_Type(Integer32):
    """Custom type pme1008RinvSfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pme1008RinvSfpIndex_Type.__name__ = "Integer32"
_Pme1008RinvSfpIndex_Object = MibTableColumn
pme1008RinvSfpIndex = _Pme1008RinvSfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 7, 1, 1, 1, 1),
    _Pme1008RinvSfpIndex_Type()
)
pme1008RinvSfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008RinvSfpIndex.setStatus("current")
_Pme1008Rinvsfp_Type = DisplayString
_Pme1008Rinvsfp_Object = MibTableColumn
pme1008Rinvsfp = _Pme1008Rinvsfp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 7, 1, 1, 1, 2),
    _Pme1008Rinvsfp_Type()
)
pme1008Rinvsfp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008Rinvsfp.setStatus("current")
_Pme1008RinvLineTable_Object = MibTable
pme1008RinvLineTable = _Pme1008RinvLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pme1008RinvLineTable.setStatus("current")
_Pme1008RinvLineEntry_Object = MibTableRow
pme1008RinvLineEntry = _Pme1008RinvLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 7, 1, 2, 1)
)
pme1008RinvLineEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008RinvLineIndex"),
)
if mibBuilder.loadTexts:
    pme1008RinvLineEntry.setStatus("current")


class _Pme1008RinvLineIndex_Type(Integer32):
    """Custom type pme1008RinvLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pme1008RinvLineIndex_Type.__name__ = "Integer32"
_Pme1008RinvLineIndex_Object = MibTableColumn
pme1008RinvLineIndex = _Pme1008RinvLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 7, 1, 2, 1, 1),
    _Pme1008RinvLineIndex_Type()
)
pme1008RinvLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008RinvLineIndex.setStatus("current")
_Pme1008RinvxfpLine_Type = DisplayString
_Pme1008RinvxfpLine_Object = MibTableColumn
pme1008RinvxfpLine = _Pme1008RinvxfpLine_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 7, 1, 2, 1, 2),
    _Pme1008RinvxfpLine_Type()
)
pme1008RinvxfpLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008RinvxfpLine.setStatus("current")
_Pme1008RinvReloadInventory_Type = EkiOnOff
_Pme1008RinvReloadInventory_Object = MibScalar
pme1008RinvReloadInventory = _Pme1008RinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 7, 2),
    _Pme1008RinvReloadInventory_Type()
)
pme1008RinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008RinvReloadInventory.setStatus("current")
_Pme1008RinvHwPlatform_Type = DisplayString
_Pme1008RinvHwPlatform_Object = MibScalar
pme1008RinvHwPlatform = _Pme1008RinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 7, 3),
    _Pme1008RinvHwPlatform_Type()
)
pme1008RinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008RinvHwPlatform.setStatus("current")
_Pme1008RinvModulePlatform_Type = DisplayString
_Pme1008RinvModulePlatform_Object = MibScalar
pme1008RinvModulePlatform = _Pme1008RinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 7, 4),
    _Pme1008RinvModulePlatform_Type()
)
pme1008RinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008RinvModulePlatform.setStatus("current")
_Pme1008RinvSwPlatform_Type = DisplayString
_Pme1008RinvSwPlatform_Object = MibScalar
pme1008RinvSwPlatform = _Pme1008RinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 7, 5),
    _Pme1008RinvSwPlatform_Type()
)
pme1008RinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008RinvSwPlatform.setStatus("current")
_Pme1008RinvGwPlatform_Type = DisplayString
_Pme1008RinvGwPlatform_Object = MibScalar
pme1008RinvGwPlatform = _Pme1008RinvGwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 7, 6),
    _Pme1008RinvGwPlatform_Type()
)
pme1008RinvGwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008RinvGwPlatform.setStatus("current")
_Pme1008download_ObjectIdentity = ObjectIdentity
pme1008download = _Pme1008download_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 8)
)
_Pme1008DwlOther_ObjectIdentity = ObjectIdentity
pme1008DwlOther = _Pme1008DwlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 8, 1)
)
_Pme1008DwlrestartProcess_ObjectIdentity = ObjectIdentity
pme1008DwlrestartProcess = _Pme1008DwlrestartProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 8, 1, 0)
)
_Pme1008DwlWarmRestartProcessed_Type = EkiOnOff
_Pme1008DwlWarmRestartProcessed_Object = MibScalar
pme1008DwlWarmRestartProcessed = _Pme1008DwlWarmRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 8, 1, 0, 1),
    _Pme1008DwlWarmRestartProcessed_Type()
)
pme1008DwlWarmRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008DwlWarmRestartProcessed.setStatus("current")
_Pme1008DwlColdRestartProcessed_Type = EkiOnOff
_Pme1008DwlColdRestartProcessed_Object = MibScalar
pme1008DwlColdRestartProcessed = _Pme1008DwlColdRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 8, 1, 0, 2),
    _Pme1008DwlColdRestartProcessed_Type()
)
pme1008DwlColdRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008DwlColdRestartProcessed.setStatus("current")
_Pme1008DwlswBanksUsed_ObjectIdentity = ObjectIdentity
pme1008DwlswBanksUsed = _Pme1008DwlswBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 8, 1, 1)
)
_Pme1008DwlSwBank1Used_Type = EkiOnOff
_Pme1008DwlSwBank1Used_Object = MibScalar
pme1008DwlSwBank1Used = _Pme1008DwlSwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 8, 1, 1, 1),
    _Pme1008DwlSwBank1Used_Type()
)
pme1008DwlSwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008DwlSwBank1Used.setStatus("current")
_Pme1008DwlSwBank2Used_Type = EkiOnOff
_Pme1008DwlSwBank2Used_Object = MibScalar
pme1008DwlSwBank2Used = _Pme1008DwlSwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 8, 1, 1, 2),
    _Pme1008DwlSwBank2Used_Type()
)
pme1008DwlSwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008DwlSwBank2Used.setStatus("current")
_Pme1008DwlSwBank1Notempty_Type = EkiOnOff
_Pme1008DwlSwBank1Notempty_Object = MibScalar
pme1008DwlSwBank1Notempty = _Pme1008DwlSwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 8, 1, 1, 5),
    _Pme1008DwlSwBank1Notempty_Type()
)
pme1008DwlSwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008DwlSwBank1Notempty.setStatus("current")
_Pme1008DwlSwBank2Notempty_Type = EkiOnOff
_Pme1008DwlSwBank2Notempty_Object = MibScalar
pme1008DwlSwBank2Notempty = _Pme1008DwlSwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 8, 1, 1, 6),
    _Pme1008DwlSwBank2Notempty_Type()
)
pme1008DwlSwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008DwlSwBank2Notempty.setStatus("current")
_Pme1008DwlgwBanksUsed_ObjectIdentity = ObjectIdentity
pme1008DwlgwBanksUsed = _Pme1008DwlgwBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 8, 1, 2)
)
_Pme1008DwlGwBank1Used_Type = EkiOnOff
_Pme1008DwlGwBank1Used_Object = MibScalar
pme1008DwlGwBank1Used = _Pme1008DwlGwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 8, 1, 2, 1),
    _Pme1008DwlGwBank1Used_Type()
)
pme1008DwlGwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008DwlGwBank1Used.setStatus("current")
_Pme1008DwlGwBank2Used_Type = EkiOnOff
_Pme1008DwlGwBank2Used_Object = MibScalar
pme1008DwlGwBank2Used = _Pme1008DwlGwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 8, 1, 2, 2),
    _Pme1008DwlGwBank2Used_Type()
)
pme1008DwlGwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008DwlGwBank2Used.setStatus("current")
_Pme1008DwlGwBank3Used_Type = EkiOnOff
_Pme1008DwlGwBank3Used_Object = MibScalar
pme1008DwlGwBank3Used = _Pme1008DwlGwBank3Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 8, 1, 2, 3),
    _Pme1008DwlGwBank3Used_Type()
)
pme1008DwlGwBank3Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008DwlGwBank3Used.setStatus("current")
_Pme1008DwlGwBank4Used_Type = EkiOnOff
_Pme1008DwlGwBank4Used_Object = MibScalar
pme1008DwlGwBank4Used = _Pme1008DwlGwBank4Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 8, 1, 2, 4),
    _Pme1008DwlGwBank4Used_Type()
)
pme1008DwlGwBank4Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008DwlGwBank4Used.setStatus("current")
_Pme1008DwlGwBank1Notempty_Type = EkiOnOff
_Pme1008DwlGwBank1Notempty_Object = MibScalar
pme1008DwlGwBank1Notempty = _Pme1008DwlGwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 8, 1, 2, 5),
    _Pme1008DwlGwBank1Notempty_Type()
)
pme1008DwlGwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008DwlGwBank1Notempty.setStatus("current")
_Pme1008DwlGwBank2Notempty_Type = EkiOnOff
_Pme1008DwlGwBank2Notempty_Object = MibScalar
pme1008DwlGwBank2Notempty = _Pme1008DwlGwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 8, 1, 2, 6),
    _Pme1008DwlGwBank2Notempty_Type()
)
pme1008DwlGwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008DwlGwBank2Notempty.setStatus("current")
_Pme1008DwlGwBank3Notempty_Type = EkiOnOff
_Pme1008DwlGwBank3Notempty_Object = MibScalar
pme1008DwlGwBank3Notempty = _Pme1008DwlGwBank3Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 8, 1, 2, 7),
    _Pme1008DwlGwBank3Notempty_Type()
)
pme1008DwlGwBank3Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008DwlGwBank3Notempty.setStatus("current")
_Pme1008DwlGwBank4Notempty_Type = EkiOnOff
_Pme1008DwlGwBank4Notempty_Object = MibScalar
pme1008DwlGwBank4Notempty = _Pme1008DwlGwBank4Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 8, 1, 2, 8),
    _Pme1008DwlGwBank4Notempty_Type()
)
pme1008DwlGwBank4Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008DwlGwBank4Notempty.setStatus("current")
_Pme1008DwlClient_ObjectIdentity = ObjectIdentity
pme1008DwlClient = _Pme1008DwlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 8, 2)
)
_Pme1008DwlLine_ObjectIdentity = ObjectIdentity
pme1008DwlLine = _Pme1008DwlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 8, 3)
)
_Pme1008Config_ObjectIdentity = ObjectIdentity
pme1008Config = _Pme1008Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9)
)
_Pme1008CfgStartup_ObjectIdentity = ObjectIdentity
pme1008CfgStartup = _Pme1008CfgStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 1)
)
_Pme1008CfgClientStartupTable_Object = MibTable
pme1008CfgClientStartupTable = _Pme1008CfgClientStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 1, 1)
)
if mibBuilder.loadTexts:
    pme1008CfgClientStartupTable.setStatus("current")
_Pme1008CfgClientStartupEntry_Object = MibTableRow
pme1008CfgClientStartupEntry = _Pme1008CfgClientStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 1, 1, 1)
)
pme1008CfgClientStartupEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008CfgClientStartupIndex"),
)
if mibBuilder.loadTexts:
    pme1008CfgClientStartupEntry.setStatus("current")


class _Pme1008CfgClientStartupIndex_Type(Integer32):
    """Custom type pme1008CfgClientStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008CfgClientStartupIndex_Type.__name__ = "Integer32"
_Pme1008CfgClientStartupIndex_Object = MibTableColumn
pme1008CfgClientStartupIndex = _Pme1008CfgClientStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 1, 1, 1, 1),
    _Pme1008CfgClientStartupIndex_Type()
)
pme1008CfgClientStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CfgClientStartupIndex.setStatus("current")


class _Pme1008CfgSystConfPortPortn_Type(Unsigned32):
    """Custom type pme1008CfgSystConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pme1008CfgSystConfPortPortn_Type.__name__ = "Unsigned32"
_Pme1008CfgSystConfPortPortn_Object = MibTableColumn
pme1008CfgSystConfPortPortn = _Pme1008CfgSystConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 1, 1, 1, 3),
    _Pme1008CfgSystConfPortPortn_Type()
)
pme1008CfgSystConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CfgSystConfPortPortn.setStatus("current")


class _Pme1008CfgNetConfPortPortn_Type(Unsigned32):
    """Custom type pme1008CfgNetConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pme1008CfgNetConfPortPortn_Type.__name__ = "Unsigned32"
_Pme1008CfgNetConfPortPortn_Object = MibTableColumn
pme1008CfgNetConfPortPortn = _Pme1008CfgNetConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 1, 1, 1, 4),
    _Pme1008CfgNetConfPortPortn_Type()
)
pme1008CfgNetConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CfgNetConfPortPortn.setStatus("current")


class _Pme1008CfgOptionsPortPortn_Type(Unsigned32):
    """Custom type pme1008CfgOptionsPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pme1008CfgOptionsPortPortn_Type.__name__ = "Unsigned32"
_Pme1008CfgOptionsPortPortn_Object = MibTableColumn
pme1008CfgOptionsPortPortn = _Pme1008CfgOptionsPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 1, 1, 1, 14),
    _Pme1008CfgOptionsPortPortn_Type()
)
pme1008CfgOptionsPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CfgOptionsPortPortn.setStatus("current")
_Pme1008CfgLinexr1StartupTable_Object = MibTable
pme1008CfgLinexr1StartupTable = _Pme1008CfgLinexr1StartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 1, 2)
)
if mibBuilder.loadTexts:
    pme1008CfgLinexr1StartupTable.setStatus("current")
_Pme1008CfgLinexr1StartupEntry_Object = MibTableRow
pme1008CfgLinexr1StartupEntry = _Pme1008CfgLinexr1StartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 1, 2, 1)
)
pme1008CfgLinexr1StartupEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008CfgLinexr1StartupIndex"),
)
if mibBuilder.loadTexts:
    pme1008CfgLinexr1StartupEntry.setStatus("current")


class _Pme1008CfgLinexr1StartupIndex_Type(Integer32):
    """Custom type pme1008CfgLinexr1StartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008CfgLinexr1StartupIndex_Type.__name__ = "Integer32"
_Pme1008CfgLinexr1StartupIndex_Object = MibTableColumn
pme1008CfgLinexr1StartupIndex = _Pme1008CfgLinexr1StartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 1, 2, 1, 1),
    _Pme1008CfgLinexr1StartupIndex_Type()
)
pme1008CfgLinexr1StartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CfgLinexr1StartupIndex.setStatus("current")


class _Pme1008CfgSystConfLinePortn_Type(Unsigned32):
    """Custom type pme1008CfgSystConfLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pme1008CfgSystConfLinePortn_Type.__name__ = "Unsigned32"
_Pme1008CfgSystConfLinePortn_Object = MibTableColumn
pme1008CfgSystConfLinePortn = _Pme1008CfgSystConfLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 1, 2, 1, 3),
    _Pme1008CfgSystConfLinePortn_Type()
)
pme1008CfgSystConfLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CfgSystConfLinePortn.setStatus("current")


class _Pme1008CfgOptionsLinePortn_Type(Unsigned32):
    """Custom type pme1008CfgOptionsLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pme1008CfgOptionsLinePortn_Type.__name__ = "Unsigned32"
_Pme1008CfgOptionsLinePortn_Object = MibTableColumn
pme1008CfgOptionsLinePortn = _Pme1008CfgOptionsLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 1, 2, 1, 14),
    _Pme1008CfgOptionsLinePortn_Type()
)
pme1008CfgOptionsLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CfgOptionsLinePortn.setStatus("current")
_Pme1008CfgOtxtlhTable_Object = MibTable
pme1008CfgOtxtlhTable = _Pme1008CfgOtxtlhTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 1, 3)
)
if mibBuilder.loadTexts:
    pme1008CfgOtxtlhTable.setStatus("current")
_Pme1008CfgOtxtlhEntry_Object = MibTableRow
pme1008CfgOtxtlhEntry = _Pme1008CfgOtxtlhEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 1, 3, 1)
)
pme1008CfgOtxtlhEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008CfgOtxtlhIndex"),
)
if mibBuilder.loadTexts:
    pme1008CfgOtxtlhEntry.setStatus("current")


class _Pme1008CfgOtxtlhIndex_Type(Integer32):
    """Custom type pme1008CfgOtxtlhIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008CfgOtxtlhIndex_Type.__name__ = "Integer32"
_Pme1008CfgOtxtlhIndex_Object = MibTableColumn
pme1008CfgOtxtlhIndex = _Pme1008CfgOtxtlhIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 1, 3, 1, 1),
    _Pme1008CfgOtxtlhIndex_Type()
)
pme1008CfgOtxtlhIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CfgOtxtlhIndex.setStatus("current")


class _Pme1008CfgLineControlsPortn_Type(Unsigned32):
    """Custom type pme1008CfgLineControlsPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pme1008CfgLineControlsPortn_Type.__name__ = "Unsigned32"
_Pme1008CfgLineControlsPortn_Object = MibTableColumn
pme1008CfgLineControlsPortn = _Pme1008CfgLineControlsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 1, 3, 1, 3),
    _Pme1008CfgLineControlsPortn_Type()
)
pme1008CfgLineControlsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CfgLineControlsPortn.setStatus("deprecated")


class _Pme1008CfgLinePwrLaserPortn_Type(Unsigned32):
    """Custom type pme1008CfgLinePwrLaserPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pme1008CfgLinePwrLaserPortn_Type.__name__ = "Unsigned32"
_Pme1008CfgLinePwrLaserPortn_Object = MibTableColumn
pme1008CfgLinePwrLaserPortn = _Pme1008CfgLinePwrLaserPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 1, 3, 1, 6),
    _Pme1008CfgLinePwrLaserPortn_Type()
)
pme1008CfgLinePwrLaserPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CfgLinePwrLaserPortn.setStatus("current")


class _Pme1008CfgLineFCurrentPortn_Type(Unsigned32):
    """Custom type pme1008CfgLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pme1008CfgLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Pme1008CfgLineFCurrentPortn_Object = MibTableColumn
pme1008CfgLineFCurrentPortn = _Pme1008CfgLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 1, 3, 1, 7),
    _Pme1008CfgLineFCurrentPortn_Type()
)
pme1008CfgLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CfgLineFCurrentPortn.setStatus("current")


class _Pme1008CfgLineGridCurrentPortn_Type(Unsigned32):
    """Custom type pme1008CfgLineGridCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pme1008CfgLineGridCurrentPortn_Type.__name__ = "Unsigned32"
_Pme1008CfgLineGridCurrentPortn_Object = MibTableColumn
pme1008CfgLineGridCurrentPortn = _Pme1008CfgLineGridCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 1, 3, 1, 8),
    _Pme1008CfgLineGridCurrentPortn_Type()
)
pme1008CfgLineGridCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CfgLineGridCurrentPortn.setStatus("current")


class _Pme1008CfgLineFoPortn_Type(Unsigned32):
    """Custom type pme1008CfgLineFoPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pme1008CfgLineFoPortn_Type.__name__ = "Unsigned32"
_Pme1008CfgLineFoPortn_Object = MibTableColumn
pme1008CfgLineFoPortn = _Pme1008CfgLineFoPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 1, 3, 1, 9),
    _Pme1008CfgLineFoPortn_Type()
)
pme1008CfgLineFoPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CfgLineFoPortn.setStatus("current")
_Pme1008CfgLabels_ObjectIdentity = ObjectIdentity
pme1008CfgLabels = _Pme1008CfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 2)
)
_Pme1008CfgLabelclientTable_Object = MibTable
pme1008CfgLabelclientTable = _Pme1008CfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 2, 1)
)
if mibBuilder.loadTexts:
    pme1008CfgLabelclientTable.setStatus("current")
_Pme1008CfgLabelclientEntry_Object = MibTableRow
pme1008CfgLabelclientEntry = _Pme1008CfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 2, 1, 1)
)
pme1008CfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008CfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pme1008CfgLabelclientEntry.setStatus("current")


class _Pme1008CfgLabelclientIndex_Type(Integer32):
    """Custom type pme1008CfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008CfgLabelclientIndex_Type.__name__ = "Integer32"
_Pme1008CfgLabelclientIndex_Object = MibTableColumn
pme1008CfgLabelclientIndex = _Pme1008CfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 2, 1, 1, 1),
    _Pme1008CfgLabelclientIndex_Type()
)
pme1008CfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CfgLabelclientIndex.setStatus("current")


class _Pme1008CfgLabelclientPortn_Type(DisplayString):
    """Custom type pme1008CfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pme1008CfgLabelclientPortn_Type.__name__ = "DisplayString"
_Pme1008CfgLabelclientPortn_Object = MibTableColumn
pme1008CfgLabelclientPortn = _Pme1008CfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 2, 1, 1, 3),
    _Pme1008CfgLabelclientPortn_Type()
)
pme1008CfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CfgLabelclientPortn.setStatus("current")
_Pme1008CfgLabellineTable_Object = MibTable
pme1008CfgLabellineTable = _Pme1008CfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 2, 2)
)
if mibBuilder.loadTexts:
    pme1008CfgLabellineTable.setStatus("current")
_Pme1008CfgLabellineEntry_Object = MibTableRow
pme1008CfgLabellineEntry = _Pme1008CfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 2, 2, 1)
)
pme1008CfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008CfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pme1008CfgLabellineEntry.setStatus("current")


class _Pme1008CfgLabellineIndex_Type(Integer32):
    """Custom type pme1008CfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008CfgLabellineIndex_Type.__name__ = "Integer32"
_Pme1008CfgLabellineIndex_Object = MibTableColumn
pme1008CfgLabellineIndex = _Pme1008CfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 2, 2, 1, 1),
    _Pme1008CfgLabellineIndex_Type()
)
pme1008CfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CfgLabellineIndex.setStatus("current")


class _Pme1008CfgLabellinePortn_Type(DisplayString):
    """Custom type pme1008CfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pme1008CfgLabellinePortn_Type.__name__ = "DisplayString"
_Pme1008CfgLabellinePortn_Object = MibTableColumn
pme1008CfgLabellinePortn = _Pme1008CfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 2, 2, 1, 3),
    _Pme1008CfgLabellinePortn_Type()
)
pme1008CfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CfgLabellinePortn.setStatus("current")
_Pme1008CfgOther_ObjectIdentity = ObjectIdentity
pme1008CfgOther = _Pme1008CfgOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 3)
)
_Pme1008tablemoduleOther_ObjectIdentity = ObjectIdentity
pme1008tablemoduleOther = _Pme1008tablemoduleOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 3, 1)
)


class _Pme1008Cfgmode_Type(Unsigned32):
    """Custom type pme1008Cfgmode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pme1008Cfgmode_Type.__name__ = "Unsigned32"
_Pme1008Cfgmode_Object = MibScalar
pme1008Cfgmode = _Pme1008Cfgmode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 3, 1, 2),
    _Pme1008Cfgmode_Type()
)
pme1008Cfgmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008Cfgmode.setStatus("current")
_Pme1008CfgOdu2Clienta_ObjectIdentity = ObjectIdentity
pme1008CfgOdu2Clienta = _Pme1008CfgOdu2Clienta_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 4)
)
_Pme1008CfgClientStartupOduTable_Object = MibTable
pme1008CfgClientStartupOduTable = _Pme1008CfgClientStartupOduTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 4, 1)
)
if mibBuilder.loadTexts:
    pme1008CfgClientStartupOduTable.setStatus("current")
_Pme1008CfgClientStartupOduEntry_Object = MibTableRow
pme1008CfgClientStartupOduEntry = _Pme1008CfgClientStartupOduEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 4, 1, 1)
)
pme1008CfgClientStartupOduEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008CfgClientStartupOduIndex"),
)
if mibBuilder.loadTexts:
    pme1008CfgClientStartupOduEntry.setStatus("current")


class _Pme1008CfgClientStartupOduIndex_Type(Integer32):
    """Custom type pme1008CfgClientStartupOduIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008CfgClientStartupOduIndex_Type.__name__ = "Integer32"
_Pme1008CfgClientStartupOduIndex_Object = MibTableColumn
pme1008CfgClientStartupOduIndex = _Pme1008CfgClientStartupOduIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 4, 1, 1, 1),
    _Pme1008CfgClientStartupOduIndex_Type()
)
pme1008CfgClientStartupOduIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CfgClientStartupOduIndex.setStatus("current")


class _Pme1008CfgOdu2ReserveLsbPortn_Type(Unsigned32):
    """Custom type pme1008CfgOdu2ReserveLsbPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pme1008CfgOdu2ReserveLsbPortn_Type.__name__ = "Unsigned32"
_Pme1008CfgOdu2ReserveLsbPortn_Object = MibTableColumn
pme1008CfgOdu2ReserveLsbPortn = _Pme1008CfgOdu2ReserveLsbPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 4, 1, 1, 3),
    _Pme1008CfgOdu2ReserveLsbPortn_Type()
)
pme1008CfgOdu2ReserveLsbPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CfgOdu2ReserveLsbPortn.setStatus("current")


class _Pme1008CfgOdu2DegthresholdPortn_Type(Unsigned32):
    """Custom type pme1008CfgOdu2DegthresholdPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pme1008CfgOdu2DegthresholdPortn_Type.__name__ = "Unsigned32"
_Pme1008CfgOdu2DegthresholdPortn_Object = MibTableColumn
pme1008CfgOdu2DegthresholdPortn = _Pme1008CfgOdu2DegthresholdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 4, 1, 1, 4),
    _Pme1008CfgOdu2DegthresholdPortn_Type()
)
pme1008CfgOdu2DegthresholdPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CfgOdu2DegthresholdPortn.setStatus("current")


class _Pme1008CfgOdu2DegmPortn_Type(Unsigned32):
    """Custom type pme1008CfgOdu2DegmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pme1008CfgOdu2DegmPortn_Type.__name__ = "Unsigned32"
_Pme1008CfgOdu2DegmPortn_Object = MibTableColumn
pme1008CfgOdu2DegmPortn = _Pme1008CfgOdu2DegmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 4, 1, 1, 5),
    _Pme1008CfgOdu2DegmPortn_Type()
)
pme1008CfgOdu2DegmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CfgOdu2DegmPortn.setStatus("current")


class _Pme1008CfgOdu2SettingsPortn_Type(Unsigned32):
    """Custom type pme1008CfgOdu2SettingsPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pme1008CfgOdu2SettingsPortn_Type.__name__ = "Unsigned32"
_Pme1008CfgOdu2SettingsPortn_Object = MibTableColumn
pme1008CfgOdu2SettingsPortn = _Pme1008CfgOdu2SettingsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 4, 1, 1, 6),
    _Pme1008CfgOdu2SettingsPortn_Type()
)
pme1008CfgOdu2SettingsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CfgOdu2SettingsPortn.setStatus("current")
_Pme1008CfgOtu2Line_ObjectIdentity = ObjectIdentity
pme1008CfgOtu2Line = _Pme1008CfgOtu2Line_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 5)
)
_Pme1008CfgLinexStartupOtuTable_Object = MibTable
pme1008CfgLinexStartupOtuTable = _Pme1008CfgLinexStartupOtuTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 5, 1)
)
if mibBuilder.loadTexts:
    pme1008CfgLinexStartupOtuTable.setStatus("current")
_Pme1008CfgLinexStartupOtuEntry_Object = MibTableRow
pme1008CfgLinexStartupOtuEntry = _Pme1008CfgLinexStartupOtuEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 5, 1, 1)
)
pme1008CfgLinexStartupOtuEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008CfgLinexStartupOtuIndex"),
)
if mibBuilder.loadTexts:
    pme1008CfgLinexStartupOtuEntry.setStatus("current")


class _Pme1008CfgLinexStartupOtuIndex_Type(Integer32):
    """Custom type pme1008CfgLinexStartupOtuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008CfgLinexStartupOtuIndex_Type.__name__ = "Integer32"
_Pme1008CfgLinexStartupOtuIndex_Object = MibTableColumn
pme1008CfgLinexStartupOtuIndex = _Pme1008CfgLinexStartupOtuIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 5, 1, 1, 1),
    _Pme1008CfgLinexStartupOtuIndex_Type()
)
pme1008CfgLinexStartupOtuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CfgLinexStartupOtuIndex.setStatus("current")


class _Pme1008CfgOtu2ReserveMsbPortn_Type(Unsigned32):
    """Custom type pme1008CfgOtu2ReserveMsbPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pme1008CfgOtu2ReserveMsbPortn_Type.__name__ = "Unsigned32"
_Pme1008CfgOtu2ReserveMsbPortn_Object = MibTableColumn
pme1008CfgOtu2ReserveMsbPortn = _Pme1008CfgOtu2ReserveMsbPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 5, 1, 1, 3),
    _Pme1008CfgOtu2ReserveMsbPortn_Type()
)
pme1008CfgOtu2ReserveMsbPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CfgOtu2ReserveMsbPortn.setStatus("current")


class _Pme1008CfgOtu2DegthresholdPortn_Type(Unsigned32):
    """Custom type pme1008CfgOtu2DegthresholdPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pme1008CfgOtu2DegthresholdPortn_Type.__name__ = "Unsigned32"
_Pme1008CfgOtu2DegthresholdPortn_Object = MibTableColumn
pme1008CfgOtu2DegthresholdPortn = _Pme1008CfgOtu2DegthresholdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 5, 1, 1, 4),
    _Pme1008CfgOtu2DegthresholdPortn_Type()
)
pme1008CfgOtu2DegthresholdPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CfgOtu2DegthresholdPortn.setStatus("current")


class _Pme1008CfgOtu2DegmPortn_Type(Unsigned32):
    """Custom type pme1008CfgOtu2DegmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pme1008CfgOtu2DegmPortn_Type.__name__ = "Unsigned32"
_Pme1008CfgOtu2DegmPortn_Object = MibTableColumn
pme1008CfgOtu2DegmPortn = _Pme1008CfgOtu2DegmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 5, 1, 1, 5),
    _Pme1008CfgOtu2DegmPortn_Type()
)
pme1008CfgOtu2DegmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CfgOtu2DegmPortn.setStatus("current")


class _Pme1008CfgOtu2SettingsPortn_Type(Unsigned32):
    """Custom type pme1008CfgOtu2SettingsPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pme1008CfgOtu2SettingsPortn_Type.__name__ = "Unsigned32"
_Pme1008CfgOtu2SettingsPortn_Object = MibTableColumn
pme1008CfgOtu2SettingsPortn = _Pme1008CfgOtu2SettingsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 5, 1, 1, 6),
    _Pme1008CfgOtu2SettingsPortn_Type()
)
pme1008CfgOtu2SettingsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CfgOtu2SettingsPortn.setStatus("current")
_Pme1008CfgSapiTxClient_ObjectIdentity = ObjectIdentity
pme1008CfgSapiTxClient = _Pme1008CfgSapiTxClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 6)
)
_Pme1008CfgClientSapiTxOduTable_Object = MibTable
pme1008CfgClientSapiTxOduTable = _Pme1008CfgClientSapiTxOduTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 6, 1)
)
if mibBuilder.loadTexts:
    pme1008CfgClientSapiTxOduTable.setStatus("current")
_Pme1008CfgClientSapiTxOduEntry_Object = MibTableRow
pme1008CfgClientSapiTxOduEntry = _Pme1008CfgClientSapiTxOduEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 6, 1, 1)
)
pme1008CfgClientSapiTxOduEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008CfgClientSapiTxOduIndex"),
)
if mibBuilder.loadTexts:
    pme1008CfgClientSapiTxOduEntry.setStatus("current")


class _Pme1008CfgClientSapiTxOduIndex_Type(Integer32):
    """Custom type pme1008CfgClientSapiTxOduIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008CfgClientSapiTxOduIndex_Type.__name__ = "Integer32"
_Pme1008CfgClientSapiTxOduIndex_Object = MibTableColumn
pme1008CfgClientSapiTxOduIndex = _Pme1008CfgClientSapiTxOduIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 6, 1, 1, 1),
    _Pme1008CfgClientSapiTxOduIndex_Type()
)
pme1008CfgClientSapiTxOduIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CfgClientSapiTxOduIndex.setStatus("current")


class _Pme1008CfgClientSapiTxSetupPortn_Type(DisplayString):
    """Custom type pme1008CfgClientSapiTxSetupPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pme1008CfgClientSapiTxSetupPortn_Type.__name__ = "DisplayString"
_Pme1008CfgClientSapiTxSetupPortn_Object = MibTableColumn
pme1008CfgClientSapiTxSetupPortn = _Pme1008CfgClientSapiTxSetupPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 6, 1, 1, 3),
    _Pme1008CfgClientSapiTxSetupPortn_Type()
)
pme1008CfgClientSapiTxSetupPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CfgClientSapiTxSetupPortn.setStatus("current")
_Pme1008CfgSapiExpClient_ObjectIdentity = ObjectIdentity
pme1008CfgSapiExpClient = _Pme1008CfgSapiExpClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 7)
)
_Pme1008CfgClientSapiExpOduTable_Object = MibTable
pme1008CfgClientSapiExpOduTable = _Pme1008CfgClientSapiExpOduTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 7, 1)
)
if mibBuilder.loadTexts:
    pme1008CfgClientSapiExpOduTable.setStatus("current")
_Pme1008CfgClientSapiExpOduEntry_Object = MibTableRow
pme1008CfgClientSapiExpOduEntry = _Pme1008CfgClientSapiExpOduEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 7, 1, 1)
)
pme1008CfgClientSapiExpOduEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008CfgClientSapiExpOduIndex"),
)
if mibBuilder.loadTexts:
    pme1008CfgClientSapiExpOduEntry.setStatus("current")


class _Pme1008CfgClientSapiExpOduIndex_Type(Integer32):
    """Custom type pme1008CfgClientSapiExpOduIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008CfgClientSapiExpOduIndex_Type.__name__ = "Integer32"
_Pme1008CfgClientSapiExpOduIndex_Object = MibTableColumn
pme1008CfgClientSapiExpOduIndex = _Pme1008CfgClientSapiExpOduIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 7, 1, 1, 1),
    _Pme1008CfgClientSapiExpOduIndex_Type()
)
pme1008CfgClientSapiExpOduIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CfgClientSapiExpOduIndex.setStatus("current")


class _Pme1008CfgClientSapiExpSetupPortn_Type(DisplayString):
    """Custom type pme1008CfgClientSapiExpSetupPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pme1008CfgClientSapiExpSetupPortn_Type.__name__ = "DisplayString"
_Pme1008CfgClientSapiExpSetupPortn_Object = MibTableColumn
pme1008CfgClientSapiExpSetupPortn = _Pme1008CfgClientSapiExpSetupPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 7, 1, 1, 3),
    _Pme1008CfgClientSapiExpSetupPortn_Type()
)
pme1008CfgClientSapiExpSetupPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CfgClientSapiExpSetupPortn.setStatus("current")
_Pme1008CfgSapiAccClient_ObjectIdentity = ObjectIdentity
pme1008CfgSapiAccClient = _Pme1008CfgSapiAccClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 8)
)
_Pme1008CfgClientSapiAccOduTable_Object = MibTable
pme1008CfgClientSapiAccOduTable = _Pme1008CfgClientSapiAccOduTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 8, 1)
)
if mibBuilder.loadTexts:
    pme1008CfgClientSapiAccOduTable.setStatus("current")
_Pme1008CfgClientSapiAccOduEntry_Object = MibTableRow
pme1008CfgClientSapiAccOduEntry = _Pme1008CfgClientSapiAccOduEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 8, 1, 1)
)
pme1008CfgClientSapiAccOduEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008CfgClientSapiAccOduIndex"),
)
if mibBuilder.loadTexts:
    pme1008CfgClientSapiAccOduEntry.setStatus("current")


class _Pme1008CfgClientSapiAccOduIndex_Type(Integer32):
    """Custom type pme1008CfgClientSapiAccOduIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008CfgClientSapiAccOduIndex_Type.__name__ = "Integer32"
_Pme1008CfgClientSapiAccOduIndex_Object = MibTableColumn
pme1008CfgClientSapiAccOduIndex = _Pme1008CfgClientSapiAccOduIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 8, 1, 1, 1),
    _Pme1008CfgClientSapiAccOduIndex_Type()
)
pme1008CfgClientSapiAccOduIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CfgClientSapiAccOduIndex.setStatus("current")


class _Pme1008CfgClientSapiAccSetupPortn_Type(DisplayString):
    """Custom type pme1008CfgClientSapiAccSetupPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pme1008CfgClientSapiAccSetupPortn_Type.__name__ = "DisplayString"
_Pme1008CfgClientSapiAccSetupPortn_Object = MibTableColumn
pme1008CfgClientSapiAccSetupPortn = _Pme1008CfgClientSapiAccSetupPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 8, 1, 1, 3),
    _Pme1008CfgClientSapiAccSetupPortn_Type()
)
pme1008CfgClientSapiAccSetupPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CfgClientSapiAccSetupPortn.setStatus("deprecated")
_Pme1008CfgDapiTxClient_ObjectIdentity = ObjectIdentity
pme1008CfgDapiTxClient = _Pme1008CfgDapiTxClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 9)
)
_Pme1008CfgClientDapiTxOduTable_Object = MibTable
pme1008CfgClientDapiTxOduTable = _Pme1008CfgClientDapiTxOduTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 9, 1)
)
if mibBuilder.loadTexts:
    pme1008CfgClientDapiTxOduTable.setStatus("current")
_Pme1008CfgClientDapiTxOduEntry_Object = MibTableRow
pme1008CfgClientDapiTxOduEntry = _Pme1008CfgClientDapiTxOduEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 9, 1, 1)
)
pme1008CfgClientDapiTxOduEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008CfgClientDapiTxOduIndex"),
)
if mibBuilder.loadTexts:
    pme1008CfgClientDapiTxOduEntry.setStatus("current")


class _Pme1008CfgClientDapiTxOduIndex_Type(Integer32):
    """Custom type pme1008CfgClientDapiTxOduIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008CfgClientDapiTxOduIndex_Type.__name__ = "Integer32"
_Pme1008CfgClientDapiTxOduIndex_Object = MibTableColumn
pme1008CfgClientDapiTxOduIndex = _Pme1008CfgClientDapiTxOduIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 9, 1, 1, 1),
    _Pme1008CfgClientDapiTxOduIndex_Type()
)
pme1008CfgClientDapiTxOduIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CfgClientDapiTxOduIndex.setStatus("current")


class _Pme1008CfgClientDapiTxSetupPortn_Type(DisplayString):
    """Custom type pme1008CfgClientDapiTxSetupPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pme1008CfgClientDapiTxSetupPortn_Type.__name__ = "DisplayString"
_Pme1008CfgClientDapiTxSetupPortn_Object = MibTableColumn
pme1008CfgClientDapiTxSetupPortn = _Pme1008CfgClientDapiTxSetupPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 9, 1, 1, 3),
    _Pme1008CfgClientDapiTxSetupPortn_Type()
)
pme1008CfgClientDapiTxSetupPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CfgClientDapiTxSetupPortn.setStatus("current")
_Pme1008CfgDapiExpClient_ObjectIdentity = ObjectIdentity
pme1008CfgDapiExpClient = _Pme1008CfgDapiExpClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 10)
)
_Pme1008CfgClientDapiExpOduTable_Object = MibTable
pme1008CfgClientDapiExpOduTable = _Pme1008CfgClientDapiExpOduTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 10, 1)
)
if mibBuilder.loadTexts:
    pme1008CfgClientDapiExpOduTable.setStatus("current")
_Pme1008CfgClientDapiExpOduEntry_Object = MibTableRow
pme1008CfgClientDapiExpOduEntry = _Pme1008CfgClientDapiExpOduEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 10, 1, 1)
)
pme1008CfgClientDapiExpOduEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008CfgClientDapiExpOduIndex"),
)
if mibBuilder.loadTexts:
    pme1008CfgClientDapiExpOduEntry.setStatus("current")


class _Pme1008CfgClientDapiExpOduIndex_Type(Integer32):
    """Custom type pme1008CfgClientDapiExpOduIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008CfgClientDapiExpOduIndex_Type.__name__ = "Integer32"
_Pme1008CfgClientDapiExpOduIndex_Object = MibTableColumn
pme1008CfgClientDapiExpOduIndex = _Pme1008CfgClientDapiExpOduIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 10, 1, 1, 1),
    _Pme1008CfgClientDapiExpOduIndex_Type()
)
pme1008CfgClientDapiExpOduIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CfgClientDapiExpOduIndex.setStatus("current")


class _Pme1008CfgClientDapiExpSetupPortn_Type(DisplayString):
    """Custom type pme1008CfgClientDapiExpSetupPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pme1008CfgClientDapiExpSetupPortn_Type.__name__ = "DisplayString"
_Pme1008CfgClientDapiExpSetupPortn_Object = MibTableColumn
pme1008CfgClientDapiExpSetupPortn = _Pme1008CfgClientDapiExpSetupPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 10, 1, 1, 3),
    _Pme1008CfgClientDapiExpSetupPortn_Type()
)
pme1008CfgClientDapiExpSetupPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CfgClientDapiExpSetupPortn.setStatus("current")
_Pme1008CfgDapiAccClient_ObjectIdentity = ObjectIdentity
pme1008CfgDapiAccClient = _Pme1008CfgDapiAccClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 11)
)
_Pme1008CfgClientDapiAccOduTable_Object = MibTable
pme1008CfgClientDapiAccOduTable = _Pme1008CfgClientDapiAccOduTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 11, 1)
)
if mibBuilder.loadTexts:
    pme1008CfgClientDapiAccOduTable.setStatus("current")
_Pme1008CfgClientDapiAccOduEntry_Object = MibTableRow
pme1008CfgClientDapiAccOduEntry = _Pme1008CfgClientDapiAccOduEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 11, 1, 1)
)
pme1008CfgClientDapiAccOduEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008CfgClientDapiAccOduIndex"),
)
if mibBuilder.loadTexts:
    pme1008CfgClientDapiAccOduEntry.setStatus("current")


class _Pme1008CfgClientDapiAccOduIndex_Type(Integer32):
    """Custom type pme1008CfgClientDapiAccOduIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008CfgClientDapiAccOduIndex_Type.__name__ = "Integer32"
_Pme1008CfgClientDapiAccOduIndex_Object = MibTableColumn
pme1008CfgClientDapiAccOduIndex = _Pme1008CfgClientDapiAccOduIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 11, 1, 1, 1),
    _Pme1008CfgClientDapiAccOduIndex_Type()
)
pme1008CfgClientDapiAccOduIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CfgClientDapiAccOduIndex.setStatus("current")


class _Pme1008CfgClientDapiAccSetupPortn_Type(DisplayString):
    """Custom type pme1008CfgClientDapiAccSetupPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pme1008CfgClientDapiAccSetupPortn_Type.__name__ = "DisplayString"
_Pme1008CfgClientDapiAccSetupPortn_Object = MibTableColumn
pme1008CfgClientDapiAccSetupPortn = _Pme1008CfgClientDapiAccSetupPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 11, 1, 1, 3),
    _Pme1008CfgClientDapiAccSetupPortn_Type()
)
pme1008CfgClientDapiAccSetupPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CfgClientDapiAccSetupPortn.setStatus("deprecated")
_Pme1008CfgSapiTxLine_ObjectIdentity = ObjectIdentity
pme1008CfgSapiTxLine = _Pme1008CfgSapiTxLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 12)
)
_Pme1008CfgLineSapiTxOtuTable_Object = MibTable
pme1008CfgLineSapiTxOtuTable = _Pme1008CfgLineSapiTxOtuTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 12, 1)
)
if mibBuilder.loadTexts:
    pme1008CfgLineSapiTxOtuTable.setStatus("current")
_Pme1008CfgLineSapiTxOtuEntry_Object = MibTableRow
pme1008CfgLineSapiTxOtuEntry = _Pme1008CfgLineSapiTxOtuEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 12, 1, 1)
)
pme1008CfgLineSapiTxOtuEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008CfgLineSapiTxOtuIndex"),
)
if mibBuilder.loadTexts:
    pme1008CfgLineSapiTxOtuEntry.setStatus("current")


class _Pme1008CfgLineSapiTxOtuIndex_Type(Integer32):
    """Custom type pme1008CfgLineSapiTxOtuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008CfgLineSapiTxOtuIndex_Type.__name__ = "Integer32"
_Pme1008CfgLineSapiTxOtuIndex_Object = MibTableColumn
pme1008CfgLineSapiTxOtuIndex = _Pme1008CfgLineSapiTxOtuIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 12, 1, 1, 1),
    _Pme1008CfgLineSapiTxOtuIndex_Type()
)
pme1008CfgLineSapiTxOtuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CfgLineSapiTxOtuIndex.setStatus("current")


class _Pme1008CfgLineSapiTxSetupPortn_Type(DisplayString):
    """Custom type pme1008CfgLineSapiTxSetupPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pme1008CfgLineSapiTxSetupPortn_Type.__name__ = "DisplayString"
_Pme1008CfgLineSapiTxSetupPortn_Object = MibTableColumn
pme1008CfgLineSapiTxSetupPortn = _Pme1008CfgLineSapiTxSetupPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 12, 1, 1, 3),
    _Pme1008CfgLineSapiTxSetupPortn_Type()
)
pme1008CfgLineSapiTxSetupPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CfgLineSapiTxSetupPortn.setStatus("current")
_Pme1008CfgSapiExpLine_ObjectIdentity = ObjectIdentity
pme1008CfgSapiExpLine = _Pme1008CfgSapiExpLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 13)
)
_Pme1008CfgLineSapiExpOtuTable_Object = MibTable
pme1008CfgLineSapiExpOtuTable = _Pme1008CfgLineSapiExpOtuTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 13, 1)
)
if mibBuilder.loadTexts:
    pme1008CfgLineSapiExpOtuTable.setStatus("current")
_Pme1008CfgLineSapiExpOtuEntry_Object = MibTableRow
pme1008CfgLineSapiExpOtuEntry = _Pme1008CfgLineSapiExpOtuEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 13, 1, 1)
)
pme1008CfgLineSapiExpOtuEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008CfgLineSapiExpOtuIndex"),
)
if mibBuilder.loadTexts:
    pme1008CfgLineSapiExpOtuEntry.setStatus("current")


class _Pme1008CfgLineSapiExpOtuIndex_Type(Integer32):
    """Custom type pme1008CfgLineSapiExpOtuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008CfgLineSapiExpOtuIndex_Type.__name__ = "Integer32"
_Pme1008CfgLineSapiExpOtuIndex_Object = MibTableColumn
pme1008CfgLineSapiExpOtuIndex = _Pme1008CfgLineSapiExpOtuIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 13, 1, 1, 1),
    _Pme1008CfgLineSapiExpOtuIndex_Type()
)
pme1008CfgLineSapiExpOtuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CfgLineSapiExpOtuIndex.setStatus("current")


class _Pme1008CfgLineSapiExpSetupPortn_Type(DisplayString):
    """Custom type pme1008CfgLineSapiExpSetupPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pme1008CfgLineSapiExpSetupPortn_Type.__name__ = "DisplayString"
_Pme1008CfgLineSapiExpSetupPortn_Object = MibTableColumn
pme1008CfgLineSapiExpSetupPortn = _Pme1008CfgLineSapiExpSetupPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 13, 1, 1, 3),
    _Pme1008CfgLineSapiExpSetupPortn_Type()
)
pme1008CfgLineSapiExpSetupPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CfgLineSapiExpSetupPortn.setStatus("current")
_Pme1008CfgSapiAccLine_ObjectIdentity = ObjectIdentity
pme1008CfgSapiAccLine = _Pme1008CfgSapiAccLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 14)
)
_Pme1008CfgLineSapiAccOtuTable_Object = MibTable
pme1008CfgLineSapiAccOtuTable = _Pme1008CfgLineSapiAccOtuTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 14, 1)
)
if mibBuilder.loadTexts:
    pme1008CfgLineSapiAccOtuTable.setStatus("current")
_Pme1008CfgLineSapiAccOtuEntry_Object = MibTableRow
pme1008CfgLineSapiAccOtuEntry = _Pme1008CfgLineSapiAccOtuEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 14, 1, 1)
)
pme1008CfgLineSapiAccOtuEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008CfgLineSapiAccOtuIndex"),
)
if mibBuilder.loadTexts:
    pme1008CfgLineSapiAccOtuEntry.setStatus("current")


class _Pme1008CfgLineSapiAccOtuIndex_Type(Integer32):
    """Custom type pme1008CfgLineSapiAccOtuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008CfgLineSapiAccOtuIndex_Type.__name__ = "Integer32"
_Pme1008CfgLineSapiAccOtuIndex_Object = MibTableColumn
pme1008CfgLineSapiAccOtuIndex = _Pme1008CfgLineSapiAccOtuIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 14, 1, 1, 1),
    _Pme1008CfgLineSapiAccOtuIndex_Type()
)
pme1008CfgLineSapiAccOtuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CfgLineSapiAccOtuIndex.setStatus("current")


class _Pme1008CfgLineSapiAccSetupPortn_Type(DisplayString):
    """Custom type pme1008CfgLineSapiAccSetupPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pme1008CfgLineSapiAccSetupPortn_Type.__name__ = "DisplayString"
_Pme1008CfgLineSapiAccSetupPortn_Object = MibTableColumn
pme1008CfgLineSapiAccSetupPortn = _Pme1008CfgLineSapiAccSetupPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 14, 1, 1, 3),
    _Pme1008CfgLineSapiAccSetupPortn_Type()
)
pme1008CfgLineSapiAccSetupPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CfgLineSapiAccSetupPortn.setStatus("deprecated")
_Pme1008CfgDapiTxLine_ObjectIdentity = ObjectIdentity
pme1008CfgDapiTxLine = _Pme1008CfgDapiTxLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 15)
)
_Pme1008CfgLineDapiTxOtuTable_Object = MibTable
pme1008CfgLineDapiTxOtuTable = _Pme1008CfgLineDapiTxOtuTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 15, 1)
)
if mibBuilder.loadTexts:
    pme1008CfgLineDapiTxOtuTable.setStatus("current")
_Pme1008CfgLineDapiTxOtuEntry_Object = MibTableRow
pme1008CfgLineDapiTxOtuEntry = _Pme1008CfgLineDapiTxOtuEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 15, 1, 1)
)
pme1008CfgLineDapiTxOtuEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008CfgLineDapiTxOtuIndex"),
)
if mibBuilder.loadTexts:
    pme1008CfgLineDapiTxOtuEntry.setStatus("current")


class _Pme1008CfgLineDapiTxOtuIndex_Type(Integer32):
    """Custom type pme1008CfgLineDapiTxOtuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008CfgLineDapiTxOtuIndex_Type.__name__ = "Integer32"
_Pme1008CfgLineDapiTxOtuIndex_Object = MibTableColumn
pme1008CfgLineDapiTxOtuIndex = _Pme1008CfgLineDapiTxOtuIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 15, 1, 1, 1),
    _Pme1008CfgLineDapiTxOtuIndex_Type()
)
pme1008CfgLineDapiTxOtuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CfgLineDapiTxOtuIndex.setStatus("current")


class _Pme1008CfgLineDapiTxSetupPortn_Type(DisplayString):
    """Custom type pme1008CfgLineDapiTxSetupPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pme1008CfgLineDapiTxSetupPortn_Type.__name__ = "DisplayString"
_Pme1008CfgLineDapiTxSetupPortn_Object = MibTableColumn
pme1008CfgLineDapiTxSetupPortn = _Pme1008CfgLineDapiTxSetupPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 15, 1, 1, 3),
    _Pme1008CfgLineDapiTxSetupPortn_Type()
)
pme1008CfgLineDapiTxSetupPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CfgLineDapiTxSetupPortn.setStatus("current")
_Pme1008CfgDapiExpLine_ObjectIdentity = ObjectIdentity
pme1008CfgDapiExpLine = _Pme1008CfgDapiExpLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 16)
)
_Pme1008CfgLineDapiExpOtuTable_Object = MibTable
pme1008CfgLineDapiExpOtuTable = _Pme1008CfgLineDapiExpOtuTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 16, 1)
)
if mibBuilder.loadTexts:
    pme1008CfgLineDapiExpOtuTable.setStatus("current")
_Pme1008CfgLineDapiExpOtuEntry_Object = MibTableRow
pme1008CfgLineDapiExpOtuEntry = _Pme1008CfgLineDapiExpOtuEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 16, 1, 1)
)
pme1008CfgLineDapiExpOtuEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008CfgLineDapiExpOtuIndex"),
)
if mibBuilder.loadTexts:
    pme1008CfgLineDapiExpOtuEntry.setStatus("current")


class _Pme1008CfgLineDapiExpOtuIndex_Type(Integer32):
    """Custom type pme1008CfgLineDapiExpOtuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008CfgLineDapiExpOtuIndex_Type.__name__ = "Integer32"
_Pme1008CfgLineDapiExpOtuIndex_Object = MibTableColumn
pme1008CfgLineDapiExpOtuIndex = _Pme1008CfgLineDapiExpOtuIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 16, 1, 1, 1),
    _Pme1008CfgLineDapiExpOtuIndex_Type()
)
pme1008CfgLineDapiExpOtuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CfgLineDapiExpOtuIndex.setStatus("current")


class _Pme1008CfgLineDapiExpSetupPortn_Type(DisplayString):
    """Custom type pme1008CfgLineDapiExpSetupPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pme1008CfgLineDapiExpSetupPortn_Type.__name__ = "DisplayString"
_Pme1008CfgLineDapiExpSetupPortn_Object = MibTableColumn
pme1008CfgLineDapiExpSetupPortn = _Pme1008CfgLineDapiExpSetupPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 16, 1, 1, 3),
    _Pme1008CfgLineDapiExpSetupPortn_Type()
)
pme1008CfgLineDapiExpSetupPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CfgLineDapiExpSetupPortn.setStatus("current")
_Pme1008CfgDapiAccLine_ObjectIdentity = ObjectIdentity
pme1008CfgDapiAccLine = _Pme1008CfgDapiAccLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 17)
)
_Pme1008CfgLineDapiAccOtuTable_Object = MibTable
pme1008CfgLineDapiAccOtuTable = _Pme1008CfgLineDapiAccOtuTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 17, 1)
)
if mibBuilder.loadTexts:
    pme1008CfgLineDapiAccOtuTable.setStatus("current")
_Pme1008CfgLineDapiAccOtuEntry_Object = MibTableRow
pme1008CfgLineDapiAccOtuEntry = _Pme1008CfgLineDapiAccOtuEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 17, 1, 1)
)
pme1008CfgLineDapiAccOtuEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008CfgLineDapiAccOtuIndex"),
)
if mibBuilder.loadTexts:
    pme1008CfgLineDapiAccOtuEntry.setStatus("current")


class _Pme1008CfgLineDapiAccOtuIndex_Type(Integer32):
    """Custom type pme1008CfgLineDapiAccOtuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008CfgLineDapiAccOtuIndex_Type.__name__ = "Integer32"
_Pme1008CfgLineDapiAccOtuIndex_Object = MibTableColumn
pme1008CfgLineDapiAccOtuIndex = _Pme1008CfgLineDapiAccOtuIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 17, 1, 1, 1),
    _Pme1008CfgLineDapiAccOtuIndex_Type()
)
pme1008CfgLineDapiAccOtuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CfgLineDapiAccOtuIndex.setStatus("current")


class _Pme1008CfgLineDapiAccSetupPortn_Type(DisplayString):
    """Custom type pme1008CfgLineDapiAccSetupPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pme1008CfgLineDapiAccSetupPortn_Type.__name__ = "DisplayString"
_Pme1008CfgLineDapiAccSetupPortn_Object = MibTableColumn
pme1008CfgLineDapiAccSetupPortn = _Pme1008CfgLineDapiAccSetupPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 17, 1, 1, 3),
    _Pme1008CfgLineDapiAccSetupPortn_Type()
)
pme1008CfgLineDapiAccSetupPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CfgLineDapiAccSetupPortn.setStatus("deprecated")
_Pme1008CfgStartuptablefive_ObjectIdentity = ObjectIdentity
pme1008CfgStartuptablefive = _Pme1008CfgStartuptablefive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 18)
)
_Pme1008CfgOtxtlhcapabilitiesTable_Object = MibTable
pme1008CfgOtxtlhcapabilitiesTable = _Pme1008CfgOtxtlhcapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 18, 1)
)
if mibBuilder.loadTexts:
    pme1008CfgOtxtlhcapabilitiesTable.setStatus("current")
_Pme1008CfgOtxtlhcapabilitiesEntry_Object = MibTableRow
pme1008CfgOtxtlhcapabilitiesEntry = _Pme1008CfgOtxtlhcapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 18, 1, 1)
)
pme1008CfgOtxtlhcapabilitiesEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008CfgOtxtlhcapabilitiesIndex"),
)
if mibBuilder.loadTexts:
    pme1008CfgOtxtlhcapabilitiesEntry.setStatus("current")


class _Pme1008CfgOtxtlhcapabilitiesIndex_Type(Integer32):
    """Custom type pme1008CfgOtxtlhcapabilitiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008CfgOtxtlhcapabilitiesIndex_Type.__name__ = "Integer32"
_Pme1008CfgOtxtlhcapabilitiesIndex_Object = MibTableColumn
pme1008CfgOtxtlhcapabilitiesIndex = _Pme1008CfgOtxtlhcapabilitiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 18, 1, 1, 1),
    _Pme1008CfgOtxtlhcapabilitiesIndex_Type()
)
pme1008CfgOtxtlhcapabilitiesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CfgOtxtlhcapabilitiesIndex.setStatus("current")


class _Pme1008CfgComponentTypePortn_Type(Unsigned32):
    """Custom type pme1008CfgComponentTypePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pme1008CfgComponentTypePortn_Type.__name__ = "Unsigned32"
_Pme1008CfgComponentTypePortn_Object = MibTableColumn
pme1008CfgComponentTypePortn = _Pme1008CfgComponentTypePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 18, 1, 1, 3),
    _Pme1008CfgComponentTypePortn_Type()
)
pme1008CfgComponentTypePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CfgComponentTypePortn.setStatus("current")


class _Pme1008CfgMiscellaneousPortn_Type(Unsigned32):
    """Custom type pme1008CfgMiscellaneousPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pme1008CfgMiscellaneousPortn_Type.__name__ = "Unsigned32"
_Pme1008CfgMiscellaneousPortn_Object = MibTableColumn
pme1008CfgMiscellaneousPortn = _Pme1008CfgMiscellaneousPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 18, 1, 1, 4),
    _Pme1008CfgMiscellaneousPortn_Type()
)
pme1008CfgMiscellaneousPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CfgMiscellaneousPortn.setStatus("current")


class _Pme1008CfgFirstChannelPortn_Type(Unsigned32):
    """Custom type pme1008CfgFirstChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pme1008CfgFirstChannelPortn_Type.__name__ = "Unsigned32"
_Pme1008CfgFirstChannelPortn_Object = MibTableColumn
pme1008CfgFirstChannelPortn = _Pme1008CfgFirstChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 18, 1, 1, 5),
    _Pme1008CfgFirstChannelPortn_Type()
)
pme1008CfgFirstChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CfgFirstChannelPortn.setStatus("current")


class _Pme1008CfgLastChannelPortn_Type(Unsigned32):
    """Custom type pme1008CfgLastChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pme1008CfgLastChannelPortn_Type.__name__ = "Unsigned32"
_Pme1008CfgLastChannelPortn_Object = MibTableColumn
pme1008CfgLastChannelPortn = _Pme1008CfgLastChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 18, 1, 1, 6),
    _Pme1008CfgLastChannelPortn_Type()
)
pme1008CfgLastChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CfgLastChannelPortn.setStatus("current")


class _Pme1008CfgGridPortn_Type(Unsigned32):
    """Custom type pme1008CfgGridPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pme1008CfgGridPortn_Type.__name__ = "Unsigned32"
_Pme1008CfgGridPortn_Object = MibTableColumn
pme1008CfgGridPortn = _Pme1008CfgGridPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 18, 1, 1, 7),
    _Pme1008CfgGridPortn_Type()
)
pme1008CfgGridPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008CfgGridPortn.setStatus("current")
_Pme1008CfgWriteConfiguration_Type = EkiOnOff
_Pme1008CfgWriteConfiguration_Object = MibScalar
pme1008CfgWriteConfiguration = _Pme1008CfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 9, 257),
    _Pme1008CfgWriteConfiguration_Type()
)
pme1008CfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008CfgWriteConfiguration.setStatus("current")
_Pme1008traps_ObjectIdentity = ObjectIdentity
pme1008traps = _Pme1008traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 10)
)


class _Pme1008trapPortNumber_Type(Integer32):
    """Custom type pme1008trapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pme1008trapPortNumber_Type.__name__ = "Integer32"
_Pme1008trapPortNumber_Object = MibScalar
pme1008trapPortNumber = _Pme1008trapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 10, 2),
    _Pme1008trapPortNumber_Type()
)
pme1008trapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008trapPortNumber.setStatus("current")


class _Pme1008trapLineNumber_Type(Integer32):
    """Custom type pme1008trapLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pme1008trapLineNumber_Type.__name__ = "Integer32"
_Pme1008trapLineNumber_Object = MibScalar
pme1008trapLineNumber = _Pme1008trapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 10, 3),
    _Pme1008trapLineNumber_Type()
)
pme1008trapLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008trapLineNumber.setStatus("current")


class _Pme1008trapBoardNumber_Type(Integer32):
    """Custom type pme1008trapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pme1008trapBoardNumber_Type.__name__ = "Integer32"
_Pme1008trapBoardNumber_Object = MibScalar
pme1008trapBoardNumber = _Pme1008trapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 10, 4),
    _Pme1008trapBoardNumber_Type()
)
pme1008trapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008trapBoardNumber.setStatus("current")
_Pme1008Monitoring_ObjectIdentity = ObjectIdentity
pme1008Monitoring = _Pme1008Monitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11)
)
_Pme1008MonOther_ObjectIdentity = ObjectIdentity
pme1008MonOther = _Pme1008MonOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 1)
)
_Pme1008MonRmon_ObjectIdentity = ObjectIdentity
pme1008MonRmon = _Pme1008MonRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 1, 3)
)
_Pme1008MonCountersReset_Type = EkiOnOff
_Pme1008MonCountersReset_Object = MibScalar
pme1008MonCountersReset = _Pme1008MonCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 1, 3, 359),
    _Pme1008MonCountersReset_Type()
)
pme1008MonCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008MonCountersReset.setStatus("current")
_Pme1008MonCountersStop_Type = EkiOnOff
_Pme1008MonCountersStop_Object = MibScalar
pme1008MonCountersStop = _Pme1008MonCountersStop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 1, 3, 360),
    _Pme1008MonCountersStop_Type()
)
pme1008MonCountersStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pme1008MonCountersStop.setStatus("current")
_Pme1008MonClient_ObjectIdentity = ObjectIdentity
pme1008MonClient = _Pme1008MonClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2)
)
_Pme1008MonClientRmonCounter_ObjectIdentity = ObjectIdentity
pme1008MonClientRmonCounter = _Pme1008MonClientRmonCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4)
)
_Pme1008MonupRmonBytesCounterClientInputTable_Object = MibTable
pme1008MonupRmonBytesCounterClientInputTable = _Pme1008MonupRmonBytesCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 16)
)
if mibBuilder.loadTexts:
    pme1008MonupRmonBytesCounterClientInputTable.setStatus("current")
_Pme1008MonupRmonBytesCounterClientInputEntry_Object = MibTableRow
pme1008MonupRmonBytesCounterClientInputEntry = _Pme1008MonupRmonBytesCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 16, 1)
)
pme1008MonupRmonBytesCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008MonupRmonBytesCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pme1008MonupRmonBytesCounterClientInputEntry.setStatus("current")


class _Pme1008MonupRmonBytesCounterClientInputIndex_Type(Integer32):
    """Custom type pme1008MonupRmonBytesCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008MonupRmonBytesCounterClientInputIndex_Type.__name__ = "Integer32"
_Pme1008MonupRmonBytesCounterClientInputIndex_Object = MibTableColumn
pme1008MonupRmonBytesCounterClientInputIndex = _Pme1008MonupRmonBytesCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 16, 1, 1),
    _Pme1008MonupRmonBytesCounterClientInputIndex_Type()
)
pme1008MonupRmonBytesCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MonupRmonBytesCounterClientInputIndex.setStatus("current")
_Pme1008MonupRmonBytesCounterClientInputValuePortn_Type = Counter64
_Pme1008MonupRmonBytesCounterClientInputValuePortn_Object = MibTableColumn
pme1008MonupRmonBytesCounterClientInputValuePortn = _Pme1008MonupRmonBytesCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 16, 1, 2),
    _Pme1008MonupRmonBytesCounterClientInputValuePortn_Type()
)
pme1008MonupRmonBytesCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MonupRmonBytesCounterClientInputValuePortn.setStatus("current")
_Pme1008MonupRmonBytesCounterClientInputErrorPortn_Type = EkiOnOff
_Pme1008MonupRmonBytesCounterClientInputErrorPortn_Object = MibTableColumn
pme1008MonupRmonBytesCounterClientInputErrorPortn = _Pme1008MonupRmonBytesCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 16, 1, 3),
    _Pme1008MonupRmonBytesCounterClientInputErrorPortn_Type()
)
pme1008MonupRmonBytesCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MonupRmonBytesCounterClientInputErrorPortn.setStatus("current")
_Pme1008MonupRmonBytesCounterClientInputOverloadPortn_Type = EkiOnOff
_Pme1008MonupRmonBytesCounterClientInputOverloadPortn_Object = MibTableColumn
pme1008MonupRmonBytesCounterClientInputOverloadPortn = _Pme1008MonupRmonBytesCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 16, 1, 4),
    _Pme1008MonupRmonBytesCounterClientInputOverloadPortn_Type()
)
pme1008MonupRmonBytesCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MonupRmonBytesCounterClientInputOverloadPortn.setStatus("current")
_Pme1008MonupRmonCrcErrorsCounterClientInputTable_Object = MibTable
pme1008MonupRmonCrcErrorsCounterClientInputTable = _Pme1008MonupRmonCrcErrorsCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 32)
)
if mibBuilder.loadTexts:
    pme1008MonupRmonCrcErrorsCounterClientInputTable.setStatus("current")
_Pme1008MonupRmonCrcErrorsCounterClientInputEntry_Object = MibTableRow
pme1008MonupRmonCrcErrorsCounterClientInputEntry = _Pme1008MonupRmonCrcErrorsCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 32, 1)
)
pme1008MonupRmonCrcErrorsCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008MonupRmonCrcErrorsCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pme1008MonupRmonCrcErrorsCounterClientInputEntry.setStatus("current")


class _Pme1008MonupRmonCrcErrorsCounterClientInputIndex_Type(Integer32):
    """Custom type pme1008MonupRmonCrcErrorsCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008MonupRmonCrcErrorsCounterClientInputIndex_Type.__name__ = "Integer32"
_Pme1008MonupRmonCrcErrorsCounterClientInputIndex_Object = MibTableColumn
pme1008MonupRmonCrcErrorsCounterClientInputIndex = _Pme1008MonupRmonCrcErrorsCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 32, 1, 1),
    _Pme1008MonupRmonCrcErrorsCounterClientInputIndex_Type()
)
pme1008MonupRmonCrcErrorsCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MonupRmonCrcErrorsCounterClientInputIndex.setStatus("current")
_Pme1008MonupRmonCrcErrorsCounterClientInputValuePortn_Type = Counter64
_Pme1008MonupRmonCrcErrorsCounterClientInputValuePortn_Object = MibTableColumn
pme1008MonupRmonCrcErrorsCounterClientInputValuePortn = _Pme1008MonupRmonCrcErrorsCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 32, 1, 2),
    _Pme1008MonupRmonCrcErrorsCounterClientInputValuePortn_Type()
)
pme1008MonupRmonCrcErrorsCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MonupRmonCrcErrorsCounterClientInputValuePortn.setStatus("current")
_Pme1008MonupRmonCrcErrorsCounterClientInputErrorPortn_Type = EkiOnOff
_Pme1008MonupRmonCrcErrorsCounterClientInputErrorPortn_Object = MibTableColumn
pme1008MonupRmonCrcErrorsCounterClientInputErrorPortn = _Pme1008MonupRmonCrcErrorsCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 32, 1, 3),
    _Pme1008MonupRmonCrcErrorsCounterClientInputErrorPortn_Type()
)
pme1008MonupRmonCrcErrorsCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MonupRmonCrcErrorsCounterClientInputErrorPortn.setStatus("current")
_Pme1008MonupRmonCrcErrorsCounterClientInputOverloadPortn_Type = EkiOnOff
_Pme1008MonupRmonCrcErrorsCounterClientInputOverloadPortn_Object = MibTableColumn
pme1008MonupRmonCrcErrorsCounterClientInputOverloadPortn = _Pme1008MonupRmonCrcErrorsCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 32, 1, 4),
    _Pme1008MonupRmonCrcErrorsCounterClientInputOverloadPortn_Type()
)
pme1008MonupRmonCrcErrorsCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MonupRmonCrcErrorsCounterClientInputOverloadPortn.setStatus("current")
_Pme1008MonupRmonPacketsCounterClientInputTable_Object = MibTable
pme1008MonupRmonPacketsCounterClientInputTable = _Pme1008MonupRmonPacketsCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 48)
)
if mibBuilder.loadTexts:
    pme1008MonupRmonPacketsCounterClientInputTable.setStatus("current")
_Pme1008MonupRmonPacketsCounterClientInputEntry_Object = MibTableRow
pme1008MonupRmonPacketsCounterClientInputEntry = _Pme1008MonupRmonPacketsCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 48, 1)
)
pme1008MonupRmonPacketsCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008MonupRmonPacketsCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pme1008MonupRmonPacketsCounterClientInputEntry.setStatus("current")


class _Pme1008MonupRmonPacketsCounterClientInputIndex_Type(Integer32):
    """Custom type pme1008MonupRmonPacketsCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008MonupRmonPacketsCounterClientInputIndex_Type.__name__ = "Integer32"
_Pme1008MonupRmonPacketsCounterClientInputIndex_Object = MibTableColumn
pme1008MonupRmonPacketsCounterClientInputIndex = _Pme1008MonupRmonPacketsCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 48, 1, 1),
    _Pme1008MonupRmonPacketsCounterClientInputIndex_Type()
)
pme1008MonupRmonPacketsCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MonupRmonPacketsCounterClientInputIndex.setStatus("current")
_Pme1008MonupRmonPacketsCounterClientInputValuePortn_Type = Counter64
_Pme1008MonupRmonPacketsCounterClientInputValuePortn_Object = MibTableColumn
pme1008MonupRmonPacketsCounterClientInputValuePortn = _Pme1008MonupRmonPacketsCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 48, 1, 2),
    _Pme1008MonupRmonPacketsCounterClientInputValuePortn_Type()
)
pme1008MonupRmonPacketsCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MonupRmonPacketsCounterClientInputValuePortn.setStatus("current")
_Pme1008MonupRmonPacketsCounterClientInputErrorPortn_Type = EkiOnOff
_Pme1008MonupRmonPacketsCounterClientInputErrorPortn_Object = MibTableColumn
pme1008MonupRmonPacketsCounterClientInputErrorPortn = _Pme1008MonupRmonPacketsCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 48, 1, 3),
    _Pme1008MonupRmonPacketsCounterClientInputErrorPortn_Type()
)
pme1008MonupRmonPacketsCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MonupRmonPacketsCounterClientInputErrorPortn.setStatus("current")
_Pme1008MonupRmonPacketsCounterClientInputOverloadPortn_Type = EkiOnOff
_Pme1008MonupRmonPacketsCounterClientInputOverloadPortn_Object = MibTableColumn
pme1008MonupRmonPacketsCounterClientInputOverloadPortn = _Pme1008MonupRmonPacketsCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 48, 1, 4),
    _Pme1008MonupRmonPacketsCounterClientInputOverloadPortn_Type()
)
pme1008MonupRmonPacketsCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MonupRmonPacketsCounterClientInputOverloadPortn.setStatus("current")
_Pme1008MonupRmonBroadcastCounterClientInputTable_Object = MibTable
pme1008MonupRmonBroadcastCounterClientInputTable = _Pme1008MonupRmonBroadcastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 64)
)
if mibBuilder.loadTexts:
    pme1008MonupRmonBroadcastCounterClientInputTable.setStatus("current")
_Pme1008MonupRmonBroadcastCounterClientInputEntry_Object = MibTableRow
pme1008MonupRmonBroadcastCounterClientInputEntry = _Pme1008MonupRmonBroadcastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 64, 1)
)
pme1008MonupRmonBroadcastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008MonupRmonBroadcastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pme1008MonupRmonBroadcastCounterClientInputEntry.setStatus("current")


class _Pme1008MonupRmonBroadcastCounterClientInputIndex_Type(Integer32):
    """Custom type pme1008MonupRmonBroadcastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008MonupRmonBroadcastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pme1008MonupRmonBroadcastCounterClientInputIndex_Object = MibTableColumn
pme1008MonupRmonBroadcastCounterClientInputIndex = _Pme1008MonupRmonBroadcastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 64, 1, 1),
    _Pme1008MonupRmonBroadcastCounterClientInputIndex_Type()
)
pme1008MonupRmonBroadcastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MonupRmonBroadcastCounterClientInputIndex.setStatus("current")
_Pme1008MonupRmonBroadcastCounterClientInputValuePortn_Type = Counter64
_Pme1008MonupRmonBroadcastCounterClientInputValuePortn_Object = MibTableColumn
pme1008MonupRmonBroadcastCounterClientInputValuePortn = _Pme1008MonupRmonBroadcastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 64, 1, 2),
    _Pme1008MonupRmonBroadcastCounterClientInputValuePortn_Type()
)
pme1008MonupRmonBroadcastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MonupRmonBroadcastCounterClientInputValuePortn.setStatus("current")
_Pme1008MonupRmonBroadcastCounterClientInputErrorPortn_Type = EkiOnOff
_Pme1008MonupRmonBroadcastCounterClientInputErrorPortn_Object = MibTableColumn
pme1008MonupRmonBroadcastCounterClientInputErrorPortn = _Pme1008MonupRmonBroadcastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 64, 1, 3),
    _Pme1008MonupRmonBroadcastCounterClientInputErrorPortn_Type()
)
pme1008MonupRmonBroadcastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MonupRmonBroadcastCounterClientInputErrorPortn.setStatus("current")
_Pme1008MonupRmonBroadcastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pme1008MonupRmonBroadcastCounterClientInputOverloadPortn_Object = MibTableColumn
pme1008MonupRmonBroadcastCounterClientInputOverloadPortn = _Pme1008MonupRmonBroadcastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 64, 1, 4),
    _Pme1008MonupRmonBroadcastCounterClientInputOverloadPortn_Type()
)
pme1008MonupRmonBroadcastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MonupRmonBroadcastCounterClientInputOverloadPortn.setStatus("current")
_Pme1008MonupRmonMulticastCounterClientInputTable_Object = MibTable
pme1008MonupRmonMulticastCounterClientInputTable = _Pme1008MonupRmonMulticastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 80)
)
if mibBuilder.loadTexts:
    pme1008MonupRmonMulticastCounterClientInputTable.setStatus("current")
_Pme1008MonupRmonMulticastCounterClientInputEntry_Object = MibTableRow
pme1008MonupRmonMulticastCounterClientInputEntry = _Pme1008MonupRmonMulticastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 80, 1)
)
pme1008MonupRmonMulticastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008MonupRmonMulticastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pme1008MonupRmonMulticastCounterClientInputEntry.setStatus("current")


class _Pme1008MonupRmonMulticastCounterClientInputIndex_Type(Integer32):
    """Custom type pme1008MonupRmonMulticastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008MonupRmonMulticastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pme1008MonupRmonMulticastCounterClientInputIndex_Object = MibTableColumn
pme1008MonupRmonMulticastCounterClientInputIndex = _Pme1008MonupRmonMulticastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 80, 1, 1),
    _Pme1008MonupRmonMulticastCounterClientInputIndex_Type()
)
pme1008MonupRmonMulticastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MonupRmonMulticastCounterClientInputIndex.setStatus("current")
_Pme1008MonupRmonMulticastCounterClientInputValuePortn_Type = Counter64
_Pme1008MonupRmonMulticastCounterClientInputValuePortn_Object = MibTableColumn
pme1008MonupRmonMulticastCounterClientInputValuePortn = _Pme1008MonupRmonMulticastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 80, 1, 2),
    _Pme1008MonupRmonMulticastCounterClientInputValuePortn_Type()
)
pme1008MonupRmonMulticastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MonupRmonMulticastCounterClientInputValuePortn.setStatus("current")
_Pme1008MonupRmonMulticastCounterClientInputErrorPortn_Type = EkiOnOff
_Pme1008MonupRmonMulticastCounterClientInputErrorPortn_Object = MibTableColumn
pme1008MonupRmonMulticastCounterClientInputErrorPortn = _Pme1008MonupRmonMulticastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 80, 1, 3),
    _Pme1008MonupRmonMulticastCounterClientInputErrorPortn_Type()
)
pme1008MonupRmonMulticastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MonupRmonMulticastCounterClientInputErrorPortn.setStatus("current")
_Pme1008MonupRmonMulticastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pme1008MonupRmonMulticastCounterClientInputOverloadPortn_Object = MibTableColumn
pme1008MonupRmonMulticastCounterClientInputOverloadPortn = _Pme1008MonupRmonMulticastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 80, 1, 4),
    _Pme1008MonupRmonMulticastCounterClientInputOverloadPortn_Type()
)
pme1008MonupRmonMulticastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MonupRmonMulticastCounterClientInputOverloadPortn.setStatus("current")
_Pme1008MonupRmonPauseFrameCounterClientInputTable_Object = MibTable
pme1008MonupRmonPauseFrameCounterClientInputTable = _Pme1008MonupRmonPauseFrameCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 96)
)
if mibBuilder.loadTexts:
    pme1008MonupRmonPauseFrameCounterClientInputTable.setStatus("current")
_Pme1008MonupRmonPauseFrameCounterClientInputEntry_Object = MibTableRow
pme1008MonupRmonPauseFrameCounterClientInputEntry = _Pme1008MonupRmonPauseFrameCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 96, 1)
)
pme1008MonupRmonPauseFrameCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008MonupRmonPauseFrameCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pme1008MonupRmonPauseFrameCounterClientInputEntry.setStatus("current")


class _Pme1008MonupRmonPauseFrameCounterClientInputIndex_Type(Integer32):
    """Custom type pme1008MonupRmonPauseFrameCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008MonupRmonPauseFrameCounterClientInputIndex_Type.__name__ = "Integer32"
_Pme1008MonupRmonPauseFrameCounterClientInputIndex_Object = MibTableColumn
pme1008MonupRmonPauseFrameCounterClientInputIndex = _Pme1008MonupRmonPauseFrameCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 96, 1, 1),
    _Pme1008MonupRmonPauseFrameCounterClientInputIndex_Type()
)
pme1008MonupRmonPauseFrameCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MonupRmonPauseFrameCounterClientInputIndex.setStatus("current")
_Pme1008MonupRmonPauseFrameCounterClientInputValuePortn_Type = Counter64
_Pme1008MonupRmonPauseFrameCounterClientInputValuePortn_Object = MibTableColumn
pme1008MonupRmonPauseFrameCounterClientInputValuePortn = _Pme1008MonupRmonPauseFrameCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 96, 1, 2),
    _Pme1008MonupRmonPauseFrameCounterClientInputValuePortn_Type()
)
pme1008MonupRmonPauseFrameCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MonupRmonPauseFrameCounterClientInputValuePortn.setStatus("current")
_Pme1008MonupRmonPauseFrameCounterClientInputErrorPortn_Type = EkiOnOff
_Pme1008MonupRmonPauseFrameCounterClientInputErrorPortn_Object = MibTableColumn
pme1008MonupRmonPauseFrameCounterClientInputErrorPortn = _Pme1008MonupRmonPauseFrameCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 96, 1, 3),
    _Pme1008MonupRmonPauseFrameCounterClientInputErrorPortn_Type()
)
pme1008MonupRmonPauseFrameCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MonupRmonPauseFrameCounterClientInputErrorPortn.setStatus("current")
_Pme1008MonupRmonPauseFrameCounterClientInputOverloadPortn_Type = EkiOnOff
_Pme1008MonupRmonPauseFrameCounterClientInputOverloadPortn_Object = MibTableColumn
pme1008MonupRmonPauseFrameCounterClientInputOverloadPortn = _Pme1008MonupRmonPauseFrameCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 96, 1, 4),
    _Pme1008MonupRmonPauseFrameCounterClientInputOverloadPortn_Type()
)
pme1008MonupRmonPauseFrameCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MonupRmonPauseFrameCounterClientInputOverloadPortn.setStatus("current")
_Pme1008MondwRmonCrcErrorsCounterClientOutputTable_Object = MibTable
pme1008MondwRmonCrcErrorsCounterClientOutputTable = _Pme1008MondwRmonCrcErrorsCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 224)
)
if mibBuilder.loadTexts:
    pme1008MondwRmonCrcErrorsCounterClientOutputTable.setStatus("current")
_Pme1008MondwRmonCrcErrorsCounterClientOutputEntry_Object = MibTableRow
pme1008MondwRmonCrcErrorsCounterClientOutputEntry = _Pme1008MondwRmonCrcErrorsCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 224, 1)
)
pme1008MondwRmonCrcErrorsCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008MondwRmonCrcErrorsCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pme1008MondwRmonCrcErrorsCounterClientOutputEntry.setStatus("current")


class _Pme1008MondwRmonCrcErrorsCounterClientOutputIndex_Type(Integer32):
    """Custom type pme1008MondwRmonCrcErrorsCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008MondwRmonCrcErrorsCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pme1008MondwRmonCrcErrorsCounterClientOutputIndex_Object = MibTableColumn
pme1008MondwRmonCrcErrorsCounterClientOutputIndex = _Pme1008MondwRmonCrcErrorsCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 224, 1, 1),
    _Pme1008MondwRmonCrcErrorsCounterClientOutputIndex_Type()
)
pme1008MondwRmonCrcErrorsCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MondwRmonCrcErrorsCounterClientOutputIndex.setStatus("current")
_Pme1008MondwRmonCrcErrorsCounterClientOutputValuePortn_Type = Counter64
_Pme1008MondwRmonCrcErrorsCounterClientOutputValuePortn_Object = MibTableColumn
pme1008MondwRmonCrcErrorsCounterClientOutputValuePortn = _Pme1008MondwRmonCrcErrorsCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 224, 1, 2),
    _Pme1008MondwRmonCrcErrorsCounterClientOutputValuePortn_Type()
)
pme1008MondwRmonCrcErrorsCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MondwRmonCrcErrorsCounterClientOutputValuePortn.setStatus("current")
_Pme1008MondwRmonCrcErrorsCounterClientOutputErrorPortn_Type = EkiOnOff
_Pme1008MondwRmonCrcErrorsCounterClientOutputErrorPortn_Object = MibTableColumn
pme1008MondwRmonCrcErrorsCounterClientOutputErrorPortn = _Pme1008MondwRmonCrcErrorsCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 224, 1, 3),
    _Pme1008MondwRmonCrcErrorsCounterClientOutputErrorPortn_Type()
)
pme1008MondwRmonCrcErrorsCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MondwRmonCrcErrorsCounterClientOutputErrorPortn.setStatus("current")
_Pme1008MondwRmonCrcErrorsCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pme1008MondwRmonCrcErrorsCounterClientOutputOverloadPortn_Object = MibTableColumn
pme1008MondwRmonCrcErrorsCounterClientOutputOverloadPortn = _Pme1008MondwRmonCrcErrorsCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 224, 1, 4),
    _Pme1008MondwRmonCrcErrorsCounterClientOutputOverloadPortn_Type()
)
pme1008MondwRmonCrcErrorsCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MondwRmonCrcErrorsCounterClientOutputOverloadPortn.setStatus("current")
_Pme1008MondwRmonPacketsCounterClientOutputTable_Object = MibTable
pme1008MondwRmonPacketsCounterClientOutputTable = _Pme1008MondwRmonPacketsCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 240)
)
if mibBuilder.loadTexts:
    pme1008MondwRmonPacketsCounterClientOutputTable.setStatus("current")
_Pme1008MondwRmonPacketsCounterClientOutputEntry_Object = MibTableRow
pme1008MondwRmonPacketsCounterClientOutputEntry = _Pme1008MondwRmonPacketsCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 240, 1)
)
pme1008MondwRmonPacketsCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pme1008-MIB", "pme1008MondwRmonPacketsCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pme1008MondwRmonPacketsCounterClientOutputEntry.setStatus("current")


class _Pme1008MondwRmonPacketsCounterClientOutputIndex_Type(Integer32):
    """Custom type pme1008MondwRmonPacketsCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pme1008MondwRmonPacketsCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pme1008MondwRmonPacketsCounterClientOutputIndex_Object = MibTableColumn
pme1008MondwRmonPacketsCounterClientOutputIndex = _Pme1008MondwRmonPacketsCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 240, 1, 1),
    _Pme1008MondwRmonPacketsCounterClientOutputIndex_Type()
)
pme1008MondwRmonPacketsCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MondwRmonPacketsCounterClientOutputIndex.setStatus("current")
_Pme1008MondwRmonPacketsCounterClientOutputValuePortn_Type = Counter64
_Pme1008MondwRmonPacketsCounterClientOutputValuePortn_Object = MibTableColumn
pme1008MondwRmonPacketsCounterClientOutputValuePortn = _Pme1008MondwRmonPacketsCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 240, 1, 2),
    _Pme1008MondwRmonPacketsCounterClientOutputValuePortn_Type()
)
pme1008MondwRmonPacketsCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MondwRmonPacketsCounterClientOutputValuePortn.setStatus("current")
_Pme1008MondwRmonPacketsCounterClientOutputErrorPortn_Type = EkiOnOff
_Pme1008MondwRmonPacketsCounterClientOutputErrorPortn_Object = MibTableColumn
pme1008MondwRmonPacketsCounterClientOutputErrorPortn = _Pme1008MondwRmonPacketsCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 240, 1, 3),
    _Pme1008MondwRmonPacketsCounterClientOutputErrorPortn_Type()
)
pme1008MondwRmonPacketsCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MondwRmonPacketsCounterClientOutputErrorPortn.setStatus("current")
_Pme1008MondwRmonPacketsCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pme1008MondwRmonPacketsCounterClientOutputOverloadPortn_Object = MibTableColumn
pme1008MondwRmonPacketsCounterClientOutputOverloadPortn = _Pme1008MondwRmonPacketsCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 79, 11, 2, 4, 240, 1, 4),
    _Pme1008MondwRmonPacketsCounterClientOutputOverloadPortn_Type()
)
pme1008MondwRmonPacketsCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pme1008MondwRmonPacketsCounterClientOutputOverloadPortn.setStatus("current")

# Managed Objects groups


# Notification objects

pme1008LineTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 79, 10, 30)
)
pme1008LineTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pme1008-MIB", "pme1008AlmLineDdmWarningPortn"),
        ("EKINOPS-Pme1008-MIB", "pme1008trapLineNumber"),
        ("EKINOPS-Pme1008-MIB", "pme1008trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pme1008LineTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pme1008LineTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 79, 10, 31)
)
pme1008LineTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pme1008-MIB", "pme1008AlmLineDdmWarningPortn"),
        ("EKINOPS-Pme1008-MIB", "pme1008trapLineNumber"),
        ("EKINOPS-Pme1008-MIB", "pme1008trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pme1008LineTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pme1008LineTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 79, 10, 32)
)
pme1008LineTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pme1008-MIB", "pme1008AlmLineDdmAlmPortn"),
        ("EKINOPS-Pme1008-MIB", "pme1008trapLineNumber"),
        ("EKINOPS-Pme1008-MIB", "pme1008trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pme1008LineTrapUrgentGoesOn.setStatus(
        "current"
    )

pme1008LineTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 79, 10, 33)
)
pme1008LineTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pme1008-MIB", "pme1008AlmLineDdmAlmPortn"),
        ("EKINOPS-Pme1008-MIB", "pme1008trapLineNumber"),
        ("EKINOPS-Pme1008-MIB", "pme1008trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pme1008LineTrapUrgentGoesOff.setStatus(
        "current"
    )

pme1008LineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 79, 10, 34)
)
pme1008LineTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pme1008-MIB", "pme1008AlmLineFailPortn"),
        ("EKINOPS-Pme1008-MIB", "pme1008AlmLineHwFailPortn"),
        ("EKINOPS-Pme1008-MIB", "pme1008trapLineNumber"),
        ("EKINOPS-Pme1008-MIB", "pme1008trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pme1008LineTrapCritGoesOn.setStatus(
        "current"
    )

pme1008LineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 79, 10, 35)
)
pme1008LineTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pme1008-MIB", "pme1008AlmLineFailPortn"),
        ("EKINOPS-Pme1008-MIB", "pme1008AlmLineHwFailPortn"),
        ("EKINOPS-Pme1008-MIB", "pme1008trapLineNumber"),
        ("EKINOPS-Pme1008-MIB", "pme1008trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pme1008LineTrapCritGoesOff.setStatus(
        "current"
    )

pme1008ClientTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 79, 10, 40)
)
pme1008ClientTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pme1008-MIB", "pme1008AlmSfpDdmWarningPortn"),
        ("EKINOPS-Pme1008-MIB", "pme1008trapPortNumber"),
        ("EKINOPS-Pme1008-MIB", "pme1008trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pme1008ClientTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pme1008ClientTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 79, 10, 41)
)
pme1008ClientTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pme1008-MIB", "pme1008AlmSfpDdmWarningPortn"),
        ("EKINOPS-Pme1008-MIB", "pme1008trapPortNumber"),
        ("EKINOPS-Pme1008-MIB", "pme1008trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pme1008ClientTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pme1008ClientTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 79, 10, 42)
)
pme1008ClientTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pme1008-MIB", "pme1008AlmSfpDdmAlmPortn"),
        ("EKINOPS-Pme1008-MIB", "pme1008trapPortNumber"),
        ("EKINOPS-Pme1008-MIB", "pme1008trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pme1008ClientTrapUrgentGoesOn.setStatus(
        "current"
    )

pme1008ClientTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 79, 10, 43)
)
pme1008ClientTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pme1008-MIB", "pme1008AlmSfpDdmAlmPortn"),
        ("EKINOPS-Pme1008-MIB", "pme1008trapPortNumber"),
        ("EKINOPS-Pme1008-MIB", "pme1008trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pme1008ClientTrapUrgentGoesOff.setStatus(
        "current"
    )

pme1008ClientTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 79, 10, 44)
)
pme1008ClientTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pme1008-MIB", "pme1008AlmFailAccPortn"),
        ("EKINOPS-Pme1008-MIB", "pme1008AlmHwFailAccPortn"),
        ("EKINOPS-Pme1008-MIB", "pme1008trapPortNumber"),
        ("EKINOPS-Pme1008-MIB", "pme1008trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pme1008ClientTrapCritGoesOn.setStatus(
        "current"
    )

pme1008ClientTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 79, 10, 45)
)
pme1008ClientTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pme1008-MIB", "pme1008AlmFailAccPortn"),
        ("EKINOPS-Pme1008-MIB", "pme1008AlmHwFailAccPortn"),
        ("EKINOPS-Pme1008-MIB", "pme1008trapPortNumber"),
        ("EKINOPS-Pme1008-MIB", "pme1008trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pme1008ClientTrapCritGoesOff.setStatus(
        "current"
    )

pme1008PowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 79, 10, 50)
)
pme1008PowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pme1008-MIB", "pme1008AlmDefFuseB"),
        ("EKINOPS-Pme1008-MIB", "pme1008AlmDefFuseA"),
        ("EKINOPS-Pme1008-MIB", "pme1008trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pme1008PowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pme1008PowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 79, 10, 51)
)
pme1008PowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pme1008-MIB", "pme1008AlmDefFuseB"),
        ("EKINOPS-Pme1008-MIB", "pme1008AlmDefFuseA"),
        ("EKINOPS-Pme1008-MIB", "pme1008trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pme1008PowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Pme1008-MIB",
    **{"Pme1008OtxGrid": Pme1008OtxGrid,
       "Pme1008DccMode": Pme1008DccMode,
       "Pme1008LineChannel": Pme1008LineChannel,
       "Pme1008Odu2SapiMode": Pme1008Odu2SapiMode,
       "Pme1008Otu2SapiMode": Pme1008Otu2SapiMode,
       "Pme1008ClientProtocol": Pme1008ClientProtocol,
       "modulePme1008": modulePme1008,
       "pme1008alarms": pme1008alarms,
       "pme1008AlmOther": pme1008AlmOther,
       "pme1008AlmOtherNurg": pme1008AlmOtherNurg,
       "pme1008AlmsynthAlm2": pme1008AlmsynthAlm2,
       "pme1008AlmConfTableSave": pme1008AlmConfTableSave,
       "pme1008AlmInvUpload": pme1008AlmInvUpload,
       "pme1008AlmConfTableLoad": pme1008AlmConfTableLoad,
       "pme1008AlmCorrelatOff": pme1008AlmCorrelatOff,
       "pme1008AlmOtherUrg": pme1008AlmOtherUrg,
       "pme1008AlmOtherCrit": pme1008AlmOtherCrit,
       "pme1008AlmsynthAlm0": pme1008AlmsynthAlm0,
       "pme1008AlmModGlobFail": pme1008AlmModGlobFail,
       "pme1008AlmDefFuseA": pme1008AlmDefFuseA,
       "pme1008AlmDefFuseB": pme1008AlmDefFuseB,
       "pme1008AlmClient": pme1008AlmClient,
       "pme1008AlmClientNurg": pme1008AlmClientNurg,
       "pme1008AlmclientSfpWarnDdmTable": pme1008AlmclientSfpWarnDdmTable,
       "pme1008AlmclientSfpWarnDdmEntry": pme1008AlmclientSfpWarnDdmEntry,
       "pme1008AlmclientSfpWarnDdmIndex": pme1008AlmclientSfpWarnDdmIndex,
       "pme1008AlmClientTxPwLowWngPortn": pme1008AlmClientTxPwLowWngPortn,
       "pme1008AlmClientTxPwrHighWngPortn": pme1008AlmClientTxPwrHighWngPortn,
       "pme1008AlmClientTxBiasLowWngPortn": pme1008AlmClientTxBiasLowWngPortn,
       "pme1008AlmClientTxBiasHighWngPortn": pme1008AlmClientTxBiasHighWngPortn,
       "pme1008AlmClientVccLowWngPortn": pme1008AlmClientVccLowWngPortn,
       "pme1008AlmClientVccHighWngPortn": pme1008AlmClientVccHighWngPortn,
       "pme1008AlmClientTempLowWngPortn": pme1008AlmClientTempLowWngPortn,
       "pme1008AlmClientTempHighWngPortn": pme1008AlmClientTempHighWngPortn,
       "pme1008AlmClientRxPwrLowWngPortn": pme1008AlmClientRxPwrLowWngPortn,
       "pme1008AlmClientRxPwrHighWngPortn": pme1008AlmClientRxPwrHighWngPortn,
       "pme1008AlmClientUrg": pme1008AlmClientUrg,
       "pme1008AlmclientHostLaneFaultTable": pme1008AlmclientHostLaneFaultTable,
       "pme1008AlmclientHostLaneFaultEntry": pme1008AlmclientHostLaneFaultEntry,
       "pme1008AlmclientHostLaneFaultIndex": pme1008AlmclientHostLaneFaultIndex,
       "pme1008AlmClientLossOfSyncPortn": pme1008AlmClientLossOfSyncPortn,
       "pme1008AlmClientInputLossOfSigPortn": pme1008AlmClientInputLossOfSigPortn,
       "pme1008AlmClientCsfDetectedPortn": pme1008AlmClientCsfDetectedPortn,
       "pme1008AlmClientLaneTxFifoErrorPortn": pme1008AlmClientLaneTxFifoErrorPortn,
       "pme1008AlmclientSfpAlmDdmTable": pme1008AlmclientSfpAlmDdmTable,
       "pme1008AlmclientSfpAlmDdmEntry": pme1008AlmclientSfpAlmDdmEntry,
       "pme1008AlmclientSfpAlmDdmIndex": pme1008AlmclientSfpAlmDdmIndex,
       "pme1008AlmClientTxPwrLowAlaPortn": pme1008AlmClientTxPwrLowAlaPortn,
       "pme1008AlmClientTxPwrHighAlaPortn": pme1008AlmClientTxPwrHighAlaPortn,
       "pme1008AlmClientTxBiasLowAlaPortn": pme1008AlmClientTxBiasLowAlaPortn,
       "pme1008AlmClientTxBiasHighAlaPortn": pme1008AlmClientTxBiasHighAlaPortn,
       "pme1008AlmClientVccLowAlaPortn": pme1008AlmClientVccLowAlaPortn,
       "pme1008AlmClientVccHighAlaPortn": pme1008AlmClientVccHighAlaPortn,
       "pme1008AlmClientTempLowAlaPortn": pme1008AlmClientTempLowAlaPortn,
       "pme1008AlmClientTempHighAlaPortn": pme1008AlmClientTempHighAlaPortn,
       "pme1008AlmClientRxPwrLowAlaPortn": pme1008AlmClientRxPwrLowAlaPortn,
       "pme1008AlmClientRxPwrHighAlaPortn": pme1008AlmClientRxPwrHighAlaPortn,
       "pme1008AlmClientCrit": pme1008AlmClientCrit,
       "pme1008AlmsynthAlmPortTable": pme1008AlmsynthAlmPortTable,
       "pme1008AlmsynthAlmPortEntry": pme1008AlmsynthAlmPortEntry,
       "pme1008AlmsynthAlmPortIndex": pme1008AlmsynthAlmPortIndex,
       "pme1008AlmSfpAbsentPortn": pme1008AlmSfpAbsentPortn,
       "pme1008AlmDdmAbsentPortn": pme1008AlmDdmAbsentPortn,
       "pme1008AlmHwFailAccPortn": pme1008AlmHwFailAccPortn,
       "pme1008AlmDwLsdPortn": pme1008AlmDwLsdPortn,
       "pme1008AlmClientLocalOosPortn": pme1008AlmClientLocalOosPortn,
       "pme1008AlmClientRemoteOosPortn": pme1008AlmClientRemoteOosPortn,
       "pme1008AlmDwCaisPortn": pme1008AlmDwCaisPortn,
       "pme1008AlmSfpDdmWarningPortn": pme1008AlmSfpDdmWarningPortn,
       "pme1008AlmSfpDdmAlmPortn": pme1008AlmSfpDdmAlmPortn,
       "pme1008AlmFailAccPortn": pme1008AlmFailAccPortn,
       "pme1008AlmUpCsfPortn": pme1008AlmUpCsfPortn,
       "pme1008AlmLine": pme1008AlmLine,
       "pme1008AlmLineNurg": pme1008AlmLineNurg,
       "pme1008AlmLineUrg": pme1008AlmLineUrg,
       "pme1008AlmlineNetworkLaneAlarmWarning1Table": pme1008AlmlineNetworkLaneAlarmWarning1Table,
       "pme1008AlmlineNetworkLaneAlarmWarning1Entry": pme1008AlmlineNetworkLaneAlarmWarning1Entry,
       "pme1008AlmlineNetworkLaneAlarmWarning1Index": pme1008AlmlineNetworkLaneAlarmWarning1Index,
       "pme1008AlmLineTxPwrLowAlaPortn": pme1008AlmLineTxPwrLowAlaPortn,
       "pme1008AlmLineTxPwrHighAlaPortn": pme1008AlmLineTxPwrHighAlaPortn,
       "pme1008AlmLineTxBiasLowAlaPortn": pme1008AlmLineTxBiasLowAlaPortn,
       "pme1008AlmLineTxBiasHighAlaPortn": pme1008AlmLineTxBiasHighAlaPortn,
       "pme1008AlmLineVccLowAlaPortn": pme1008AlmLineVccLowAlaPortn,
       "pme1008AlmLineVccHighAlaPortn": pme1008AlmLineVccHighAlaPortn,
       "pme1008AlmLineTempLowAlaPortn": pme1008AlmLineTempLowAlaPortn,
       "pme1008AlmLineTempHighAlaPortn": pme1008AlmLineTempHighAlaPortn,
       "pme1008AlmLineRxPwrLowAlaPortn": pme1008AlmLineRxPwrLowAlaPortn,
       "pme1008AlmLineRxPwrHighAlaPortn": pme1008AlmLineRxPwrHighAlaPortn,
       "pme1008AlmlineNetworkLaneAlarmWarning2Table": pme1008AlmlineNetworkLaneAlarmWarning2Table,
       "pme1008AlmlineNetworkLaneAlarmWarning2Entry": pme1008AlmlineNetworkLaneAlarmWarning2Entry,
       "pme1008AlmlineNetworkLaneAlarmWarning2Index": pme1008AlmlineNetworkLaneAlarmWarning2Index,
       "pme1008AlmLineTxPwLowWngPortn": pme1008AlmLineTxPwLowWngPortn,
       "pme1008AlmLineTxPwrHighWngPortn": pme1008AlmLineTxPwrHighWngPortn,
       "pme1008AlmLineTxBiasLowWngPortn": pme1008AlmLineTxBiasLowWngPortn,
       "pme1008AlmLineTxBiasHighWngPortn": pme1008AlmLineTxBiasHighWngPortn,
       "pme1008AlmLineVccLowWngPortn": pme1008AlmLineVccLowWngPortn,
       "pme1008AlmLineVccHighWngPortn": pme1008AlmLineVccHighWngPortn,
       "pme1008AlmLineTempLowWngPortn": pme1008AlmLineTempLowWngPortn,
       "pme1008AlmLineTempHighWngPortn": pme1008AlmLineTempHighWngPortn,
       "pme1008AlmLineRxPwrLowWngPortn": pme1008AlmLineRxPwrLowWngPortn,
       "pme1008AlmLineRxPwrHighWngPortn": pme1008AlmLineRxPwrHighWngPortn,
       "pme1008AlmlineHostLaneFaultTable": pme1008AlmlineHostLaneFaultTable,
       "pme1008AlmlineHostLaneFaultEntry": pme1008AlmlineHostLaneFaultEntry,
       "pme1008AlmlineHostLaneFaultIndex": pme1008AlmlineHostLaneFaultIndex,
       "pme1008AlmLineInputLossOfSignalPortn": pme1008AlmLineInputLossOfSignalPortn,
       "pme1008AlmLineLossOfFramePortn": pme1008AlmLineLossOfFramePortn,
       "pme1008AlmLineCrit": pme1008AlmLineCrit,
       "pme1008AlmsynthAlmLineTable": pme1008AlmsynthAlmLineTable,
       "pme1008AlmsynthAlmLineEntry": pme1008AlmsynthAlmLineEntry,
       "pme1008AlmsynthAlmLineIndex": pme1008AlmsynthAlmLineIndex,
       "pme1008AlmLineSfpAbsentPortn": pme1008AlmLineSfpAbsentPortn,
       "pme1008AlmLineDdmAbsentPortn": pme1008AlmLineDdmAbsentPortn,
       "pme1008AlmLineHwFailPortn": pme1008AlmLineHwFailPortn,
       "pme1008AlmLineTxOffPortn": pme1008AlmLineTxOffPortn,
       "pme1008AlmLineLocalOosPortn": pme1008AlmLineLocalOosPortn,
       "pme1008AlmUpRdiInsPortn": pme1008AlmUpRdiInsPortn,
       "pme1008AlmLineDdmWarningPortn": pme1008AlmLineDdmWarningPortn,
       "pme1008AlmLineDdmAlmPortn": pme1008AlmLineDdmAlmPortn,
       "pme1008AlmLineFailPortn": pme1008AlmLineFailPortn,
       "pme1008measures": pme1008measures,
       "pme1008MesrOther": pme1008MesrOther,
       "pme1008MesrClient": pme1008MesrClient,
       "pme1008MesrclientTempTable": pme1008MesrclientTempTable,
       "pme1008MesrclientTempEntry": pme1008MesrclientTempEntry,
       "pme1008MesrclientTempIndex": pme1008MesrclientTempIndex,
       "pme1008MesrclientTempPortn": pme1008MesrclientTempPortn,
       "pme1008MesrclientTxBiasTable": pme1008MesrclientTxBiasTable,
       "pme1008MesrclientTxBiasEntry": pme1008MesrclientTxBiasEntry,
       "pme1008MesrclientTxBiasIndex": pme1008MesrclientTxBiasIndex,
       "pme1008MesrclientTxBiasPortn": pme1008MesrclientTxBiasPortn,
       "pme1008MesrclientTxPwrTable": pme1008MesrclientTxPwrTable,
       "pme1008MesrclientTxPwrEntry": pme1008MesrclientTxPwrEntry,
       "pme1008MesrclientTxPwrIndex": pme1008MesrclientTxPwrIndex,
       "pme1008MesrclientTxPwrPortn": pme1008MesrclientTxPwrPortn,
       "pme1008MesrclientRxPwrTable": pme1008MesrclientRxPwrTable,
       "pme1008MesrclientRxPwrEntry": pme1008MesrclientRxPwrEntry,
       "pme1008MesrclientRxPwrIndex": pme1008MesrclientRxPwrIndex,
       "pme1008MesrclientRxPwrPortn": pme1008MesrclientRxPwrPortn,
       "pme1008MesrLine": pme1008MesrLine,
       "pme1008MesrlineTxPwrTable": pme1008MesrlineTxPwrTable,
       "pme1008MesrlineTxPwrEntry": pme1008MesrlineTxPwrEntry,
       "pme1008MesrlineTxPwrIndex": pme1008MesrlineTxPwrIndex,
       "pme1008MesrlineTxPwrPortn": pme1008MesrlineTxPwrPortn,
       "pme1008MesrlineTempTable": pme1008MesrlineTempTable,
       "pme1008MesrlineTempEntry": pme1008MesrlineTempEntry,
       "pme1008MesrlineTempIndex": pme1008MesrlineTempIndex,
       "pme1008MesrlineTempPortn": pme1008MesrlineTempPortn,
       "pme1008MesrlineTxBiasTable": pme1008MesrlineTxBiasTable,
       "pme1008MesrlineTxBiasEntry": pme1008MesrlineTxBiasEntry,
       "pme1008MesrlineTxBiasIndex": pme1008MesrlineTxBiasIndex,
       "pme1008MesrlineTxBiasPortn": pme1008MesrlineTxBiasPortn,
       "pme1008MesrlineRxPwrTable": pme1008MesrlineRxPwrTable,
       "pme1008MesrlineRxPwrEntry": pme1008MesrlineRxPwrEntry,
       "pme1008MesrlineRxPwrIndex": pme1008MesrlineRxPwrIndex,
       "pme1008MesrlineRxPwrPortn": pme1008MesrlineRxPwrPortn,
       "pme1008counters": pme1008counters,
       "pme1008CntOther": pme1008CntOther,
       "pme1008CntClient": pme1008CntClient,
       "pme1008CntclientCbipCounterTable": pme1008CntclientCbipCounterTable,
       "pme1008CntclientCbipCounterEntry": pme1008CntclientCbipCounterEntry,
       "pme1008CntclientCbipCounterIndex": pme1008CntclientCbipCounterIndex,
       "pme1008CntclientCbipCounterValuePortn": pme1008CntclientCbipCounterValuePortn,
       "pme1008CntclientCbipCounterErrorPortn": pme1008CntclientCbipCounterErrorPortn,
       "pme1008CntclientCbipCounterOverloadPortn": pme1008CntclientCbipCounterOverloadPortn,
       "pme1008CntLine": pme1008CntLine,
       "pme1008CntlocalLineSmBip8ErrorCounterTable": pme1008CntlocalLineSmBip8ErrorCounterTable,
       "pme1008CntlocalLineSmBip8ErrorCounterEntry": pme1008CntlocalLineSmBip8ErrorCounterEntry,
       "pme1008CntlocalLineSmBip8ErrorCounterIndex": pme1008CntlocalLineSmBip8ErrorCounterIndex,
       "pme1008CntlocalLineSmBip8ErrorCounterValuePortn": pme1008CntlocalLineSmBip8ErrorCounterValuePortn,
       "pme1008CntlocalLineSmBip8ErrorCounterErrorPortn": pme1008CntlocalLineSmBip8ErrorCounterErrorPortn,
       "pme1008CntlocalLineSmBip8ErrorCounterOverloadPortn": pme1008CntlocalLineSmBip8ErrorCounterOverloadPortn,
       "pme1008CntlineDfrmTimCntTable": pme1008CntlineDfrmTimCntTable,
       "pme1008CntlineDfrmTimCntEntry": pme1008CntlineDfrmTimCntEntry,
       "pme1008CntlineDfrmTimCntIndex": pme1008CntlineDfrmTimCntIndex,
       "pme1008CntlineDfrmTimCntValuePortn": pme1008CntlineDfrmTimCntValuePortn,
       "pme1008CntlineDfrmTimCntErrorPortn": pme1008CntlineDfrmTimCntErrorPortn,
       "pme1008CntlineDfrmTimCntOverloadPortn": pme1008CntlineDfrmTimCntOverloadPortn,
       "pme1008CntCountersReset": pme1008CntCountersReset,
       "pme1008CntCountersStop": pme1008CntCountersStop,
       "pme1008controlsWrite": pme1008controlsWrite,
       "pme1008CtrlOther": pme1008CtrlOther,
       "pme1008CtrlconfMgnt1": pme1008CtrlconfMgnt1,
       "pme1008CtrlConf1Load1": pme1008CtrlConf1Load1,
       "pme1008CtrlConf2Load1": pme1008CtrlConf2Load1,
       "pme1008CtrlConf2Flash1": pme1008CtrlConf2Flash1,
       "pme1008CtrlConf2Clear1": pme1008CtrlConf2Clear1,
       "pme1008Ctrlsynth4": pme1008Ctrlsynth4,
       "pme1008CtrlCorrelatOn": pme1008CtrlCorrelatOn,
       "pme1008CtrlCorrelatOff": pme1008CtrlCorrelatOff,
       "pme1008CtrlswMgnt": pme1008CtrlswMgnt,
       "pme1008CtrlColdReset": pme1008CtrlColdReset,
       "pme1008CtrlWarmReset": pme1008CtrlWarmReset,
       "pme1008CtrlLoadSwBank1": pme1008CtrlLoadSwBank1,
       "pme1008CtrlLoadSwBank2": pme1008CtrlLoadSwBank2,
       "pme1008CtrlgwMgnt": pme1008CtrlgwMgnt,
       "pme1008CtrlCurrentGwReset": pme1008CtrlCurrentGwReset,
       "pme1008CtrlLoadGwBank1": pme1008CtrlLoadGwBank1,
       "pme1008CtrlLoadGwBank2": pme1008CtrlLoadGwBank2,
       "pme1008CtrlLoadGwBank3": pme1008CtrlLoadGwBank3,
       "pme1008CtrlLoadGwBank4": pme1008CtrlLoadGwBank4,
       "pme1008CtrlledTest": pme1008CtrlledTest,
       "pme1008CtrlGreenLed": pme1008CtrlGreenLed,
       "pme1008CtrlRedLed": pme1008CtrlRedLed,
       "pme1008CtrlLedOff": pme1008CtrlLedOff,
       "pme1008CtrlClient": pme1008CtrlClient,
       "pme1008CtrlaccessLoopTable": pme1008CtrlaccessLoopTable,
       "pme1008CtrlaccessLoopEntry": pme1008CtrlaccessLoopEntry,
       "pme1008CtrlaccessLoopIndex": pme1008CtrlaccessLoopIndex,
       "pme1008CtrlaccessLoopPortn": pme1008CtrlaccessLoopPortn,
       "pme1008CtrlclientLoopToLineTable": pme1008CtrlclientLoopToLineTable,
       "pme1008CtrlclientLoopToLineEntry": pme1008CtrlclientLoopToLineEntry,
       "pme1008CtrlclientLoopToLineIndex": pme1008CtrlclientLoopToLineIndex,
       "pme1008CtrlclientLoopToLinePortn": pme1008CtrlclientLoopToLinePortn,
       "pme1008CtrlcsfUpInsTable": pme1008CtrlcsfUpInsTable,
       "pme1008CtrlcsfUpInsEntry": pme1008CtrlcsfUpInsEntry,
       "pme1008CtrlcsfUpInsIndex": pme1008CtrlcsfUpInsIndex,
       "pme1008CtrlcsfUpInsPortn": pme1008CtrlcsfUpInsPortn,
       "pme1008CtrlcaisDwInsTable": pme1008CtrlcaisDwInsTable,
       "pme1008CtrlcaisDwInsEntry": pme1008CtrlcaisDwInsEntry,
       "pme1008CtrlcaisDwInsIndex": pme1008CtrlcaisDwInsIndex,
       "pme1008CtrlcaisDwInsPortn": pme1008CtrlcaisDwInsPortn,
       "pme1008CtrlclientOciTable": pme1008CtrlclientOciTable,
       "pme1008CtrlclientOciEntry": pme1008CtrlclientOciEntry,
       "pme1008CtrlclientOciIndex": pme1008CtrlclientOciIndex,
       "pme1008CtrlclientOciPortn": pme1008CtrlclientOciPortn,
       "pme1008CtrlclientLckTable": pme1008CtrlclientLckTable,
       "pme1008CtrlclientLckEntry": pme1008CtrlclientLckEntry,
       "pme1008CtrlclientLckIndex": pme1008CtrlclientLckIndex,
       "pme1008CtrlclientLckPortn": pme1008CtrlclientLckPortn,
       "pme1008CtrlclientAisTable": pme1008CtrlclientAisTable,
       "pme1008CtrlclientAisEntry": pme1008CtrlclientAisEntry,
       "pme1008CtrlclientAisIndex": pme1008CtrlclientAisIndex,
       "pme1008CtrlclientAisPortn": pme1008CtrlclientAisPortn,
       "pme1008CtrlclientBdiTable": pme1008CtrlclientBdiTable,
       "pme1008CtrlclientBdiEntry": pme1008CtrlclientBdiEntry,
       "pme1008CtrlclientBdiIndex": pme1008CtrlclientBdiIndex,
       "pme1008CtrlclientBdiPortn": pme1008CtrlclientBdiPortn,
       "pme1008CtrlLine": pme1008CtrlLine,
       "pme1008CtrlcommAccessLoopTable": pme1008CtrlcommAccessLoopTable,
       "pme1008CtrlcommAccessLoopEntry": pme1008CtrlcommAccessLoopEntry,
       "pme1008CtrlcommAccessLoopIndex": pme1008CtrlcommAccessLoopIndex,
       "pme1008CtrlcommAccessLoopPortn": pme1008CtrlcommAccessLoopPortn,
       "pme1008CtrllineLoopTable": pme1008CtrllineLoopTable,
       "pme1008CtrllineLoopEntry": pme1008CtrllineLoopEntry,
       "pme1008CtrllineLoopIndex": pme1008CtrllineLoopIndex,
       "pme1008CtrllineLoopPortn": pme1008CtrllineLoopPortn,
       "pme1008CtrlfecDisableTable": pme1008CtrlfecDisableTable,
       "pme1008CtrlfecDisableEntry": pme1008CtrlfecDisableEntry,
       "pme1008CtrlfecDisableIndex": pme1008CtrlfecDisableIndex,
       "pme1008CtrlfecDisablePortn": pme1008CtrlfecDisablePortn,
       "pme1008CtrllineBdiTable": pme1008CtrllineBdiTable,
       "pme1008CtrllineBdiEntry": pme1008CtrllineBdiEntry,
       "pme1008CtrllineBdiIndex": pme1008CtrllineBdiIndex,
       "pme1008CtrllineBdiPortn": pme1008CtrllineBdiPortn,
       "pme1008ri": pme1008ri,
       "pme1008riTable": pme1008riTable,
       "pme1008RinvSfpTable": pme1008RinvSfpTable,
       "pme1008RinvSfpEntry": pme1008RinvSfpEntry,
       "pme1008RinvSfpIndex": pme1008RinvSfpIndex,
       "pme1008Rinvsfp": pme1008Rinvsfp,
       "pme1008RinvLineTable": pme1008RinvLineTable,
       "pme1008RinvLineEntry": pme1008RinvLineEntry,
       "pme1008RinvLineIndex": pme1008RinvLineIndex,
       "pme1008RinvxfpLine": pme1008RinvxfpLine,
       "pme1008RinvReloadInventory": pme1008RinvReloadInventory,
       "pme1008RinvHwPlatform": pme1008RinvHwPlatform,
       "pme1008RinvModulePlatform": pme1008RinvModulePlatform,
       "pme1008RinvSwPlatform": pme1008RinvSwPlatform,
       "pme1008RinvGwPlatform": pme1008RinvGwPlatform,
       "pme1008download": pme1008download,
       "pme1008DwlOther": pme1008DwlOther,
       "pme1008DwlrestartProcess": pme1008DwlrestartProcess,
       "pme1008DwlWarmRestartProcessed": pme1008DwlWarmRestartProcessed,
       "pme1008DwlColdRestartProcessed": pme1008DwlColdRestartProcessed,
       "pme1008DwlswBanksUsed": pme1008DwlswBanksUsed,
       "pme1008DwlSwBank1Used": pme1008DwlSwBank1Used,
       "pme1008DwlSwBank2Used": pme1008DwlSwBank2Used,
       "pme1008DwlSwBank1Notempty": pme1008DwlSwBank1Notempty,
       "pme1008DwlSwBank2Notempty": pme1008DwlSwBank2Notempty,
       "pme1008DwlgwBanksUsed": pme1008DwlgwBanksUsed,
       "pme1008DwlGwBank1Used": pme1008DwlGwBank1Used,
       "pme1008DwlGwBank2Used": pme1008DwlGwBank2Used,
       "pme1008DwlGwBank3Used": pme1008DwlGwBank3Used,
       "pme1008DwlGwBank4Used": pme1008DwlGwBank4Used,
       "pme1008DwlGwBank1Notempty": pme1008DwlGwBank1Notempty,
       "pme1008DwlGwBank2Notempty": pme1008DwlGwBank2Notempty,
       "pme1008DwlGwBank3Notempty": pme1008DwlGwBank3Notempty,
       "pme1008DwlGwBank4Notempty": pme1008DwlGwBank4Notempty,
       "pme1008DwlClient": pme1008DwlClient,
       "pme1008DwlLine": pme1008DwlLine,
       "pme1008Config": pme1008Config,
       "pme1008CfgStartup": pme1008CfgStartup,
       "pme1008CfgClientStartupTable": pme1008CfgClientStartupTable,
       "pme1008CfgClientStartupEntry": pme1008CfgClientStartupEntry,
       "pme1008CfgClientStartupIndex": pme1008CfgClientStartupIndex,
       "pme1008CfgSystConfPortPortn": pme1008CfgSystConfPortPortn,
       "pme1008CfgNetConfPortPortn": pme1008CfgNetConfPortPortn,
       "pme1008CfgOptionsPortPortn": pme1008CfgOptionsPortPortn,
       "pme1008CfgLinexr1StartupTable": pme1008CfgLinexr1StartupTable,
       "pme1008CfgLinexr1StartupEntry": pme1008CfgLinexr1StartupEntry,
       "pme1008CfgLinexr1StartupIndex": pme1008CfgLinexr1StartupIndex,
       "pme1008CfgSystConfLinePortn": pme1008CfgSystConfLinePortn,
       "pme1008CfgOptionsLinePortn": pme1008CfgOptionsLinePortn,
       "pme1008CfgOtxtlhTable": pme1008CfgOtxtlhTable,
       "pme1008CfgOtxtlhEntry": pme1008CfgOtxtlhEntry,
       "pme1008CfgOtxtlhIndex": pme1008CfgOtxtlhIndex,
       "pme1008CfgLineControlsPortn": pme1008CfgLineControlsPortn,
       "pme1008CfgLinePwrLaserPortn": pme1008CfgLinePwrLaserPortn,
       "pme1008CfgLineFCurrentPortn": pme1008CfgLineFCurrentPortn,
       "pme1008CfgLineGridCurrentPortn": pme1008CfgLineGridCurrentPortn,
       "pme1008CfgLineFoPortn": pme1008CfgLineFoPortn,
       "pme1008CfgLabels": pme1008CfgLabels,
       "pme1008CfgLabelclientTable": pme1008CfgLabelclientTable,
       "pme1008CfgLabelclientEntry": pme1008CfgLabelclientEntry,
       "pme1008CfgLabelclientIndex": pme1008CfgLabelclientIndex,
       "pme1008CfgLabelclientPortn": pme1008CfgLabelclientPortn,
       "pme1008CfgLabellineTable": pme1008CfgLabellineTable,
       "pme1008CfgLabellineEntry": pme1008CfgLabellineEntry,
       "pme1008CfgLabellineIndex": pme1008CfgLabellineIndex,
       "pme1008CfgLabellinePortn": pme1008CfgLabellinePortn,
       "pme1008CfgOther": pme1008CfgOther,
       "pme1008tablemoduleOther": pme1008tablemoduleOther,
       "pme1008Cfgmode": pme1008Cfgmode,
       "pme1008CfgOdu2Clienta": pme1008CfgOdu2Clienta,
       "pme1008CfgClientStartupOduTable": pme1008CfgClientStartupOduTable,
       "pme1008CfgClientStartupOduEntry": pme1008CfgClientStartupOduEntry,
       "pme1008CfgClientStartupOduIndex": pme1008CfgClientStartupOduIndex,
       "pme1008CfgOdu2ReserveLsbPortn": pme1008CfgOdu2ReserveLsbPortn,
       "pme1008CfgOdu2DegthresholdPortn": pme1008CfgOdu2DegthresholdPortn,
       "pme1008CfgOdu2DegmPortn": pme1008CfgOdu2DegmPortn,
       "pme1008CfgOdu2SettingsPortn": pme1008CfgOdu2SettingsPortn,
       "pme1008CfgOtu2Line": pme1008CfgOtu2Line,
       "pme1008CfgLinexStartupOtuTable": pme1008CfgLinexStartupOtuTable,
       "pme1008CfgLinexStartupOtuEntry": pme1008CfgLinexStartupOtuEntry,
       "pme1008CfgLinexStartupOtuIndex": pme1008CfgLinexStartupOtuIndex,
       "pme1008CfgOtu2ReserveMsbPortn": pme1008CfgOtu2ReserveMsbPortn,
       "pme1008CfgOtu2DegthresholdPortn": pme1008CfgOtu2DegthresholdPortn,
       "pme1008CfgOtu2DegmPortn": pme1008CfgOtu2DegmPortn,
       "pme1008CfgOtu2SettingsPortn": pme1008CfgOtu2SettingsPortn,
       "pme1008CfgSapiTxClient": pme1008CfgSapiTxClient,
       "pme1008CfgClientSapiTxOduTable": pme1008CfgClientSapiTxOduTable,
       "pme1008CfgClientSapiTxOduEntry": pme1008CfgClientSapiTxOduEntry,
       "pme1008CfgClientSapiTxOduIndex": pme1008CfgClientSapiTxOduIndex,
       "pme1008CfgClientSapiTxSetupPortn": pme1008CfgClientSapiTxSetupPortn,
       "pme1008CfgSapiExpClient": pme1008CfgSapiExpClient,
       "pme1008CfgClientSapiExpOduTable": pme1008CfgClientSapiExpOduTable,
       "pme1008CfgClientSapiExpOduEntry": pme1008CfgClientSapiExpOduEntry,
       "pme1008CfgClientSapiExpOduIndex": pme1008CfgClientSapiExpOduIndex,
       "pme1008CfgClientSapiExpSetupPortn": pme1008CfgClientSapiExpSetupPortn,
       "pme1008CfgSapiAccClient": pme1008CfgSapiAccClient,
       "pme1008CfgClientSapiAccOduTable": pme1008CfgClientSapiAccOduTable,
       "pme1008CfgClientSapiAccOduEntry": pme1008CfgClientSapiAccOduEntry,
       "pme1008CfgClientSapiAccOduIndex": pme1008CfgClientSapiAccOduIndex,
       "pme1008CfgClientSapiAccSetupPortn": pme1008CfgClientSapiAccSetupPortn,
       "pme1008CfgDapiTxClient": pme1008CfgDapiTxClient,
       "pme1008CfgClientDapiTxOduTable": pme1008CfgClientDapiTxOduTable,
       "pme1008CfgClientDapiTxOduEntry": pme1008CfgClientDapiTxOduEntry,
       "pme1008CfgClientDapiTxOduIndex": pme1008CfgClientDapiTxOduIndex,
       "pme1008CfgClientDapiTxSetupPortn": pme1008CfgClientDapiTxSetupPortn,
       "pme1008CfgDapiExpClient": pme1008CfgDapiExpClient,
       "pme1008CfgClientDapiExpOduTable": pme1008CfgClientDapiExpOduTable,
       "pme1008CfgClientDapiExpOduEntry": pme1008CfgClientDapiExpOduEntry,
       "pme1008CfgClientDapiExpOduIndex": pme1008CfgClientDapiExpOduIndex,
       "pme1008CfgClientDapiExpSetupPortn": pme1008CfgClientDapiExpSetupPortn,
       "pme1008CfgDapiAccClient": pme1008CfgDapiAccClient,
       "pme1008CfgClientDapiAccOduTable": pme1008CfgClientDapiAccOduTable,
       "pme1008CfgClientDapiAccOduEntry": pme1008CfgClientDapiAccOduEntry,
       "pme1008CfgClientDapiAccOduIndex": pme1008CfgClientDapiAccOduIndex,
       "pme1008CfgClientDapiAccSetupPortn": pme1008CfgClientDapiAccSetupPortn,
       "pme1008CfgSapiTxLine": pme1008CfgSapiTxLine,
       "pme1008CfgLineSapiTxOtuTable": pme1008CfgLineSapiTxOtuTable,
       "pme1008CfgLineSapiTxOtuEntry": pme1008CfgLineSapiTxOtuEntry,
       "pme1008CfgLineSapiTxOtuIndex": pme1008CfgLineSapiTxOtuIndex,
       "pme1008CfgLineSapiTxSetupPortn": pme1008CfgLineSapiTxSetupPortn,
       "pme1008CfgSapiExpLine": pme1008CfgSapiExpLine,
       "pme1008CfgLineSapiExpOtuTable": pme1008CfgLineSapiExpOtuTable,
       "pme1008CfgLineSapiExpOtuEntry": pme1008CfgLineSapiExpOtuEntry,
       "pme1008CfgLineSapiExpOtuIndex": pme1008CfgLineSapiExpOtuIndex,
       "pme1008CfgLineSapiExpSetupPortn": pme1008CfgLineSapiExpSetupPortn,
       "pme1008CfgSapiAccLine": pme1008CfgSapiAccLine,
       "pme1008CfgLineSapiAccOtuTable": pme1008CfgLineSapiAccOtuTable,
       "pme1008CfgLineSapiAccOtuEntry": pme1008CfgLineSapiAccOtuEntry,
       "pme1008CfgLineSapiAccOtuIndex": pme1008CfgLineSapiAccOtuIndex,
       "pme1008CfgLineSapiAccSetupPortn": pme1008CfgLineSapiAccSetupPortn,
       "pme1008CfgDapiTxLine": pme1008CfgDapiTxLine,
       "pme1008CfgLineDapiTxOtuTable": pme1008CfgLineDapiTxOtuTable,
       "pme1008CfgLineDapiTxOtuEntry": pme1008CfgLineDapiTxOtuEntry,
       "pme1008CfgLineDapiTxOtuIndex": pme1008CfgLineDapiTxOtuIndex,
       "pme1008CfgLineDapiTxSetupPortn": pme1008CfgLineDapiTxSetupPortn,
       "pme1008CfgDapiExpLine": pme1008CfgDapiExpLine,
       "pme1008CfgLineDapiExpOtuTable": pme1008CfgLineDapiExpOtuTable,
       "pme1008CfgLineDapiExpOtuEntry": pme1008CfgLineDapiExpOtuEntry,
       "pme1008CfgLineDapiExpOtuIndex": pme1008CfgLineDapiExpOtuIndex,
       "pme1008CfgLineDapiExpSetupPortn": pme1008CfgLineDapiExpSetupPortn,
       "pme1008CfgDapiAccLine": pme1008CfgDapiAccLine,
       "pme1008CfgLineDapiAccOtuTable": pme1008CfgLineDapiAccOtuTable,
       "pme1008CfgLineDapiAccOtuEntry": pme1008CfgLineDapiAccOtuEntry,
       "pme1008CfgLineDapiAccOtuIndex": pme1008CfgLineDapiAccOtuIndex,
       "pme1008CfgLineDapiAccSetupPortn": pme1008CfgLineDapiAccSetupPortn,
       "pme1008CfgStartuptablefive": pme1008CfgStartuptablefive,
       "pme1008CfgOtxtlhcapabilitiesTable": pme1008CfgOtxtlhcapabilitiesTable,
       "pme1008CfgOtxtlhcapabilitiesEntry": pme1008CfgOtxtlhcapabilitiesEntry,
       "pme1008CfgOtxtlhcapabilitiesIndex": pme1008CfgOtxtlhcapabilitiesIndex,
       "pme1008CfgComponentTypePortn": pme1008CfgComponentTypePortn,
       "pme1008CfgMiscellaneousPortn": pme1008CfgMiscellaneousPortn,
       "pme1008CfgFirstChannelPortn": pme1008CfgFirstChannelPortn,
       "pme1008CfgLastChannelPortn": pme1008CfgLastChannelPortn,
       "pme1008CfgGridPortn": pme1008CfgGridPortn,
       "pme1008CfgWriteConfiguration": pme1008CfgWriteConfiguration,
       "pme1008traps": pme1008traps,
       "pme1008trapPortNumber": pme1008trapPortNumber,
       "pme1008trapLineNumber": pme1008trapLineNumber,
       "pme1008trapBoardNumber": pme1008trapBoardNumber,
       "pme1008LineTrapNotUrgentGoesOn": pme1008LineTrapNotUrgentGoesOn,
       "pme1008LineTrapNotUrgentGoesOff": pme1008LineTrapNotUrgentGoesOff,
       "pme1008LineTrapUrgentGoesOn": pme1008LineTrapUrgentGoesOn,
       "pme1008LineTrapUrgentGoesOff": pme1008LineTrapUrgentGoesOff,
       "pme1008LineTrapCritGoesOn": pme1008LineTrapCritGoesOn,
       "pme1008LineTrapCritGoesOff": pme1008LineTrapCritGoesOff,
       "pme1008ClientTrapNotUrgentGoesOn": pme1008ClientTrapNotUrgentGoesOn,
       "pme1008ClientTrapNotUrgentGoesOff": pme1008ClientTrapNotUrgentGoesOff,
       "pme1008ClientTrapUrgentGoesOn": pme1008ClientTrapUrgentGoesOn,
       "pme1008ClientTrapUrgentGoesOff": pme1008ClientTrapUrgentGoesOff,
       "pme1008ClientTrapCritGoesOn": pme1008ClientTrapCritGoesOn,
       "pme1008ClientTrapCritGoesOff": pme1008ClientTrapCritGoesOff,
       "pme1008PowerTrapUrgentGoesOn": pme1008PowerTrapUrgentGoesOn,
       "pme1008PowerTrapUrgentGoesOff": pme1008PowerTrapUrgentGoesOff,
       "pme1008Monitoring": pme1008Monitoring,
       "pme1008MonOther": pme1008MonOther,
       "pme1008MonRmon": pme1008MonRmon,
       "pme1008MonCountersReset": pme1008MonCountersReset,
       "pme1008MonCountersStop": pme1008MonCountersStop,
       "pme1008MonClient": pme1008MonClient,
       "pme1008MonClientRmonCounter": pme1008MonClientRmonCounter,
       "pme1008MonupRmonBytesCounterClientInputTable": pme1008MonupRmonBytesCounterClientInputTable,
       "pme1008MonupRmonBytesCounterClientInputEntry": pme1008MonupRmonBytesCounterClientInputEntry,
       "pme1008MonupRmonBytesCounterClientInputIndex": pme1008MonupRmonBytesCounterClientInputIndex,
       "pme1008MonupRmonBytesCounterClientInputValuePortn": pme1008MonupRmonBytesCounterClientInputValuePortn,
       "pme1008MonupRmonBytesCounterClientInputErrorPortn": pme1008MonupRmonBytesCounterClientInputErrorPortn,
       "pme1008MonupRmonBytesCounterClientInputOverloadPortn": pme1008MonupRmonBytesCounterClientInputOverloadPortn,
       "pme1008MonupRmonCrcErrorsCounterClientInputTable": pme1008MonupRmonCrcErrorsCounterClientInputTable,
       "pme1008MonupRmonCrcErrorsCounterClientInputEntry": pme1008MonupRmonCrcErrorsCounterClientInputEntry,
       "pme1008MonupRmonCrcErrorsCounterClientInputIndex": pme1008MonupRmonCrcErrorsCounterClientInputIndex,
       "pme1008MonupRmonCrcErrorsCounterClientInputValuePortn": pme1008MonupRmonCrcErrorsCounterClientInputValuePortn,
       "pme1008MonupRmonCrcErrorsCounterClientInputErrorPortn": pme1008MonupRmonCrcErrorsCounterClientInputErrorPortn,
       "pme1008MonupRmonCrcErrorsCounterClientInputOverloadPortn": pme1008MonupRmonCrcErrorsCounterClientInputOverloadPortn,
       "pme1008MonupRmonPacketsCounterClientInputTable": pme1008MonupRmonPacketsCounterClientInputTable,
       "pme1008MonupRmonPacketsCounterClientInputEntry": pme1008MonupRmonPacketsCounterClientInputEntry,
       "pme1008MonupRmonPacketsCounterClientInputIndex": pme1008MonupRmonPacketsCounterClientInputIndex,
       "pme1008MonupRmonPacketsCounterClientInputValuePortn": pme1008MonupRmonPacketsCounterClientInputValuePortn,
       "pme1008MonupRmonPacketsCounterClientInputErrorPortn": pme1008MonupRmonPacketsCounterClientInputErrorPortn,
       "pme1008MonupRmonPacketsCounterClientInputOverloadPortn": pme1008MonupRmonPacketsCounterClientInputOverloadPortn,
       "pme1008MonupRmonBroadcastCounterClientInputTable": pme1008MonupRmonBroadcastCounterClientInputTable,
       "pme1008MonupRmonBroadcastCounterClientInputEntry": pme1008MonupRmonBroadcastCounterClientInputEntry,
       "pme1008MonupRmonBroadcastCounterClientInputIndex": pme1008MonupRmonBroadcastCounterClientInputIndex,
       "pme1008MonupRmonBroadcastCounterClientInputValuePortn": pme1008MonupRmonBroadcastCounterClientInputValuePortn,
       "pme1008MonupRmonBroadcastCounterClientInputErrorPortn": pme1008MonupRmonBroadcastCounterClientInputErrorPortn,
       "pme1008MonupRmonBroadcastCounterClientInputOverloadPortn": pme1008MonupRmonBroadcastCounterClientInputOverloadPortn,
       "pme1008MonupRmonMulticastCounterClientInputTable": pme1008MonupRmonMulticastCounterClientInputTable,
       "pme1008MonupRmonMulticastCounterClientInputEntry": pme1008MonupRmonMulticastCounterClientInputEntry,
       "pme1008MonupRmonMulticastCounterClientInputIndex": pme1008MonupRmonMulticastCounterClientInputIndex,
       "pme1008MonupRmonMulticastCounterClientInputValuePortn": pme1008MonupRmonMulticastCounterClientInputValuePortn,
       "pme1008MonupRmonMulticastCounterClientInputErrorPortn": pme1008MonupRmonMulticastCounterClientInputErrorPortn,
       "pme1008MonupRmonMulticastCounterClientInputOverloadPortn": pme1008MonupRmonMulticastCounterClientInputOverloadPortn,
       "pme1008MonupRmonPauseFrameCounterClientInputTable": pme1008MonupRmonPauseFrameCounterClientInputTable,
       "pme1008MonupRmonPauseFrameCounterClientInputEntry": pme1008MonupRmonPauseFrameCounterClientInputEntry,
       "pme1008MonupRmonPauseFrameCounterClientInputIndex": pme1008MonupRmonPauseFrameCounterClientInputIndex,
       "pme1008MonupRmonPauseFrameCounterClientInputValuePortn": pme1008MonupRmonPauseFrameCounterClientInputValuePortn,
       "pme1008MonupRmonPauseFrameCounterClientInputErrorPortn": pme1008MonupRmonPauseFrameCounterClientInputErrorPortn,
       "pme1008MonupRmonPauseFrameCounterClientInputOverloadPortn": pme1008MonupRmonPauseFrameCounterClientInputOverloadPortn,
       "pme1008MondwRmonCrcErrorsCounterClientOutputTable": pme1008MondwRmonCrcErrorsCounterClientOutputTable,
       "pme1008MondwRmonCrcErrorsCounterClientOutputEntry": pme1008MondwRmonCrcErrorsCounterClientOutputEntry,
       "pme1008MondwRmonCrcErrorsCounterClientOutputIndex": pme1008MondwRmonCrcErrorsCounterClientOutputIndex,
       "pme1008MondwRmonCrcErrorsCounterClientOutputValuePortn": pme1008MondwRmonCrcErrorsCounterClientOutputValuePortn,
       "pme1008MondwRmonCrcErrorsCounterClientOutputErrorPortn": pme1008MondwRmonCrcErrorsCounterClientOutputErrorPortn,
       "pme1008MondwRmonCrcErrorsCounterClientOutputOverloadPortn": pme1008MondwRmonCrcErrorsCounterClientOutputOverloadPortn,
       "pme1008MondwRmonPacketsCounterClientOutputTable": pme1008MondwRmonPacketsCounterClientOutputTable,
       "pme1008MondwRmonPacketsCounterClientOutputEntry": pme1008MondwRmonPacketsCounterClientOutputEntry,
       "pme1008MondwRmonPacketsCounterClientOutputIndex": pme1008MondwRmonPacketsCounterClientOutputIndex,
       "pme1008MondwRmonPacketsCounterClientOutputValuePortn": pme1008MondwRmonPacketsCounterClientOutputValuePortn,
       "pme1008MondwRmonPacketsCounterClientOutputErrorPortn": pme1008MondwRmonPacketsCounterClientOutputErrorPortn,
       "pme1008MondwRmonPacketsCounterClientOutputOverloadPortn": pme1008MondwRmonPacketsCounterClientOutputOverloadPortn}
)
