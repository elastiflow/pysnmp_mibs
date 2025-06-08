# SNMP MIB module (EKINOPS-Pm124fe-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Pm124fe-MIB.mib
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

modulePm124fe = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44)
)
if mibBuilder.loadTexts:
    modulePm124fe.setRevisions(
        ("2009-11-12 00:00",
         "2010-04-09 00:00",
         "2010-11-05 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Pm124fealarms_ObjectIdentity = ObjectIdentity
pm124fealarms = _Pm124fealarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2)
)
_Pm124feAlmOther_ObjectIdentity = ObjectIdentity
pm124feAlmOther = _Pm124feAlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 1)
)
_Pm124feAlmOtherNurg_ObjectIdentity = ObjectIdentity
pm124feAlmOtherNurg = _Pm124feAlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 1, 1)
)
_Pm124feAlmsynthAlm2_ObjectIdentity = ObjectIdentity
pm124feAlmsynthAlm2 = _Pm124feAlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 1, 1, 2)
)
_Pm124feAlmConfTableSave_Type = EkiOnOff
_Pm124feAlmConfTableSave_Object = MibScalar
pm124feAlmConfTableSave = _Pm124feAlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 1, 1, 2, 1),
    _Pm124feAlmConfTableSave_Type()
)
pm124feAlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmConfTableSave.setStatus("current")
_Pm124feAlmInvUpload_Type = EkiOnOff
_Pm124feAlmInvUpload_Object = MibScalar
pm124feAlmInvUpload = _Pm124feAlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 1, 1, 2, 2),
    _Pm124feAlmInvUpload_Type()
)
pm124feAlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmInvUpload.setStatus("current")
_Pm124feAlmConfTableLoad_Type = EkiOnOff
_Pm124feAlmConfTableLoad_Object = MibScalar
pm124feAlmConfTableLoad = _Pm124feAlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 1, 1, 2, 3),
    _Pm124feAlmConfTableLoad_Type()
)
pm124feAlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmConfTableLoad.setStatus("current")
_Pm124feAlmCorrelatOff_Type = EkiOnOff
_Pm124feAlmCorrelatOff_Object = MibScalar
pm124feAlmCorrelatOff = _Pm124feAlmCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 1, 1, 2, 4),
    _Pm124feAlmCorrelatOff_Type()
)
pm124feAlmCorrelatOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmCorrelatOff.setStatus("current")
_Pm124feAlmOtherUrg_ObjectIdentity = ObjectIdentity
pm124feAlmOtherUrg = _Pm124feAlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 1, 2)
)
_Pm124feAlmOtherCrit_ObjectIdentity = ObjectIdentity
pm124feAlmOtherCrit = _Pm124feAlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 1, 3)
)
_Pm124feAlmsynthAlm0_ObjectIdentity = ObjectIdentity
pm124feAlmsynthAlm0 = _Pm124feAlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 1, 3, 0)
)
_Pm124feAlmModuleGlobFailure_Type = EkiOnOff
_Pm124feAlmModuleGlobFailure_Object = MibScalar
pm124feAlmModuleGlobFailure = _Pm124feAlmModuleGlobFailure_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 1, 3, 0, 9),
    _Pm124feAlmModuleGlobFailure_Type()
)
pm124feAlmModuleGlobFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmModuleGlobFailure.setStatus("current")
_Pm124feAlmDefFuseA_Type = EkiOnOff
_Pm124feAlmDefFuseA_Object = MibScalar
pm124feAlmDefFuseA = _Pm124feAlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 1, 3, 0, 15),
    _Pm124feAlmDefFuseA_Type()
)
pm124feAlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmDefFuseA.setStatus("current")
_Pm124feAlmDefFuseB_Type = EkiOnOff
_Pm124feAlmDefFuseB_Object = MibScalar
pm124feAlmDefFuseB = _Pm124feAlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 1, 3, 0, 16),
    _Pm124feAlmDefFuseB_Type()
)
pm124feAlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmDefFuseB.setStatus("current")
_Pm124feAlmClient_ObjectIdentity = ObjectIdentity
pm124feAlmClient = _Pm124feAlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2)
)
_Pm124feAlmClientNurg_ObjectIdentity = ObjectIdentity
pm124feAlmClientNurg = _Pm124feAlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 1)
)
_Pm124feAlmclientSfpWarnDdmTable_Object = MibTable
pm124feAlmclientSfpWarnDdmTable = _Pm124feAlmclientSfpWarnDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 1, 32)
)
if mibBuilder.loadTexts:
    pm124feAlmclientSfpWarnDdmTable.setStatus("current")
_Pm124feAlmclientSfpWarnDdmEntry_Object = MibTableRow
pm124feAlmclientSfpWarnDdmEntry = _Pm124feAlmclientSfpWarnDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 1, 32, 1)
)
pm124feAlmclientSfpWarnDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm124fe-MIB", "pm124feAlmclientSfpWarnDdmIndex"),
)
if mibBuilder.loadTexts:
    pm124feAlmclientSfpWarnDdmEntry.setStatus("current")


class _Pm124feAlmclientSfpWarnDdmIndex_Type(Integer32):
    """Custom type pm124feAlmclientSfpWarnDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124feAlmclientSfpWarnDdmIndex_Type.__name__ = "Integer32"
_Pm124feAlmclientSfpWarnDdmIndex_Object = MibTableColumn
pm124feAlmclientSfpWarnDdmIndex = _Pm124feAlmclientSfpWarnDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 1, 32, 1, 1),
    _Pm124feAlmclientSfpWarnDdmIndex_Type()
)
pm124feAlmclientSfpWarnDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmclientSfpWarnDdmIndex.setStatus("current")
_Pm124feAlmClientTxPwLowWngPortn_Type = EkiOnOff
_Pm124feAlmClientTxPwLowWngPortn_Object = MibTableColumn
pm124feAlmClientTxPwLowWngPortn = _Pm124feAlmClientTxPwLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 1, 32, 1, 2),
    _Pm124feAlmClientTxPwLowWngPortn_Type()
)
pm124feAlmClientTxPwLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmClientTxPwLowWngPortn.setStatus("current")
_Pm124feAlmClientTxPwrHighWngPortn_Type = EkiOnOff
_Pm124feAlmClientTxPwrHighWngPortn_Object = MibTableColumn
pm124feAlmClientTxPwrHighWngPortn = _Pm124feAlmClientTxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 1, 32, 1, 3),
    _Pm124feAlmClientTxPwrHighWngPortn_Type()
)
pm124feAlmClientTxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmClientTxPwrHighWngPortn.setStatus("current")
_Pm124feAlmClientTxBiasLowWngPortn_Type = EkiOnOff
_Pm124feAlmClientTxBiasLowWngPortn_Object = MibTableColumn
pm124feAlmClientTxBiasLowWngPortn = _Pm124feAlmClientTxBiasLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 1, 32, 1, 4),
    _Pm124feAlmClientTxBiasLowWngPortn_Type()
)
pm124feAlmClientTxBiasLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmClientTxBiasLowWngPortn.setStatus("current")
_Pm124feAlmClientTxBiasHighWngPortn_Type = EkiOnOff
_Pm124feAlmClientTxBiasHighWngPortn_Object = MibTableColumn
pm124feAlmClientTxBiasHighWngPortn = _Pm124feAlmClientTxBiasHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 1, 32, 1, 5),
    _Pm124feAlmClientTxBiasHighWngPortn_Type()
)
pm124feAlmClientTxBiasHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmClientTxBiasHighWngPortn.setStatus("current")
_Pm124feAlmClientVccLowWngPortn_Type = EkiOnOff
_Pm124feAlmClientVccLowWngPortn_Object = MibTableColumn
pm124feAlmClientVccLowWngPortn = _Pm124feAlmClientVccLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 1, 32, 1, 6),
    _Pm124feAlmClientVccLowWngPortn_Type()
)
pm124feAlmClientVccLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmClientVccLowWngPortn.setStatus("current")
_Pm124feAlmClientVccHighWngPortn_Type = EkiOnOff
_Pm124feAlmClientVccHighWngPortn_Object = MibTableColumn
pm124feAlmClientVccHighWngPortn = _Pm124feAlmClientVccHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 1, 32, 1, 7),
    _Pm124feAlmClientVccHighWngPortn_Type()
)
pm124feAlmClientVccHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmClientVccHighWngPortn.setStatus("current")
_Pm124feAlmClientTempLowWngPortn_Type = EkiOnOff
_Pm124feAlmClientTempLowWngPortn_Object = MibTableColumn
pm124feAlmClientTempLowWngPortn = _Pm124feAlmClientTempLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 1, 32, 1, 8),
    _Pm124feAlmClientTempLowWngPortn_Type()
)
pm124feAlmClientTempLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmClientTempLowWngPortn.setStatus("current")
_Pm124feAlmClientTempHighWngPortn_Type = EkiOnOff
_Pm124feAlmClientTempHighWngPortn_Object = MibTableColumn
pm124feAlmClientTempHighWngPortn = _Pm124feAlmClientTempHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 1, 32, 1, 9),
    _Pm124feAlmClientTempHighWngPortn_Type()
)
pm124feAlmClientTempHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmClientTempHighWngPortn.setStatus("current")
_Pm124feAlmClientRxPwrLowWngPortn_Type = EkiOnOff
_Pm124feAlmClientRxPwrLowWngPortn_Object = MibTableColumn
pm124feAlmClientRxPwrLowWngPortn = _Pm124feAlmClientRxPwrLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 1, 32, 1, 16),
    _Pm124feAlmClientRxPwrLowWngPortn_Type()
)
pm124feAlmClientRxPwrLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmClientRxPwrLowWngPortn.setStatus("current")
_Pm124feAlmClientRxPwrHighWngPortn_Type = EkiOnOff
_Pm124feAlmClientRxPwrHighWngPortn_Object = MibTableColumn
pm124feAlmClientRxPwrHighWngPortn = _Pm124feAlmClientRxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 1, 32, 1, 17),
    _Pm124feAlmClientRxPwrHighWngPortn_Type()
)
pm124feAlmClientRxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmClientRxPwrHighWngPortn.setStatus("current")
_Pm124feAlmClientUrg_ObjectIdentity = ObjectIdentity
pm124feAlmClientUrg = _Pm124feAlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 2)
)
_Pm124feAlmclientSfpAlmDdmTable_Object = MibTable
pm124feAlmclientSfpAlmDdmTable = _Pm124feAlmclientSfpAlmDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 2, 24)
)
if mibBuilder.loadTexts:
    pm124feAlmclientSfpAlmDdmTable.setStatus("current")
_Pm124feAlmclientSfpAlmDdmEntry_Object = MibTableRow
pm124feAlmclientSfpAlmDdmEntry = _Pm124feAlmclientSfpAlmDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 2, 24, 1)
)
pm124feAlmclientSfpAlmDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm124fe-MIB", "pm124feAlmclientSfpAlmDdmIndex"),
)
if mibBuilder.loadTexts:
    pm124feAlmclientSfpAlmDdmEntry.setStatus("current")


class _Pm124feAlmclientSfpAlmDdmIndex_Type(Integer32):
    """Custom type pm124feAlmclientSfpAlmDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124feAlmclientSfpAlmDdmIndex_Type.__name__ = "Integer32"
_Pm124feAlmclientSfpAlmDdmIndex_Object = MibTableColumn
pm124feAlmclientSfpAlmDdmIndex = _Pm124feAlmclientSfpAlmDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 2, 24, 1, 1),
    _Pm124feAlmclientSfpAlmDdmIndex_Type()
)
pm124feAlmclientSfpAlmDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmclientSfpAlmDdmIndex.setStatus("current")
_Pm124feAlmClientTxPwrLowAlaPortn_Type = EkiOnOff
_Pm124feAlmClientTxPwrLowAlaPortn_Object = MibTableColumn
pm124feAlmClientTxPwrLowAlaPortn = _Pm124feAlmClientTxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 2, 24, 1, 2),
    _Pm124feAlmClientTxPwrLowAlaPortn_Type()
)
pm124feAlmClientTxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmClientTxPwrLowAlaPortn.setStatus("current")
_Pm124feAlmClientClientTxPwrHighAlaPortn_Type = EkiOnOff
_Pm124feAlmClientClientTxPwrHighAlaPortn_Object = MibTableColumn
pm124feAlmClientClientTxPwrHighAlaPortn = _Pm124feAlmClientClientTxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 2, 24, 1, 3),
    _Pm124feAlmClientClientTxPwrHighAlaPortn_Type()
)
pm124feAlmClientClientTxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmClientClientTxPwrHighAlaPortn.setStatus("current")
_Pm124feAlmClientTxBiasLowAlaPortn_Type = EkiOnOff
_Pm124feAlmClientTxBiasLowAlaPortn_Object = MibTableColumn
pm124feAlmClientTxBiasLowAlaPortn = _Pm124feAlmClientTxBiasLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 2, 24, 1, 4),
    _Pm124feAlmClientTxBiasLowAlaPortn_Type()
)
pm124feAlmClientTxBiasLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmClientTxBiasLowAlaPortn.setStatus("current")
_Pm124feAlmClientTxBiasHighAlaPortn_Type = EkiOnOff
_Pm124feAlmClientTxBiasHighAlaPortn_Object = MibTableColumn
pm124feAlmClientTxBiasHighAlaPortn = _Pm124feAlmClientTxBiasHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 2, 24, 1, 5),
    _Pm124feAlmClientTxBiasHighAlaPortn_Type()
)
pm124feAlmClientTxBiasHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmClientTxBiasHighAlaPortn.setStatus("current")
_Pm124feAlmClientVccLowAlaPortn_Type = EkiOnOff
_Pm124feAlmClientVccLowAlaPortn_Object = MibTableColumn
pm124feAlmClientVccLowAlaPortn = _Pm124feAlmClientVccLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 2, 24, 1, 6),
    _Pm124feAlmClientVccLowAlaPortn_Type()
)
pm124feAlmClientVccLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmClientVccLowAlaPortn.setStatus("current")
_Pm124feAlmClientVccHighAlaPortn_Type = EkiOnOff
_Pm124feAlmClientVccHighAlaPortn_Object = MibTableColumn
pm124feAlmClientVccHighAlaPortn = _Pm124feAlmClientVccHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 2, 24, 1, 7),
    _Pm124feAlmClientVccHighAlaPortn_Type()
)
pm124feAlmClientVccHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmClientVccHighAlaPortn.setStatus("current")
_Pm124feAlmClientTempLowAlaPortn_Type = EkiOnOff
_Pm124feAlmClientTempLowAlaPortn_Object = MibTableColumn
pm124feAlmClientTempLowAlaPortn = _Pm124feAlmClientTempLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 2, 24, 1, 8),
    _Pm124feAlmClientTempLowAlaPortn_Type()
)
pm124feAlmClientTempLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmClientTempLowAlaPortn.setStatus("current")
_Pm124feAlmClientTempHighAlaPortn_Type = EkiOnOff
_Pm124feAlmClientTempHighAlaPortn_Object = MibTableColumn
pm124feAlmClientTempHighAlaPortn = _Pm124feAlmClientTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 2, 24, 1, 9),
    _Pm124feAlmClientTempHighAlaPortn_Type()
)
pm124feAlmClientTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmClientTempHighAlaPortn.setStatus("current")
_Pm124feAlmClientRxPwrLowAlaPortn_Type = EkiOnOff
_Pm124feAlmClientRxPwrLowAlaPortn_Object = MibTableColumn
pm124feAlmClientRxPwrLowAlaPortn = _Pm124feAlmClientRxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 2, 24, 1, 16),
    _Pm124feAlmClientRxPwrLowAlaPortn_Type()
)
pm124feAlmClientRxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmClientRxPwrLowAlaPortn.setStatus("current")
_Pm124feAlmClientRxPwrHighAlaPortn_Type = EkiOnOff
_Pm124feAlmClientRxPwrHighAlaPortn_Object = MibTableColumn
pm124feAlmClientRxPwrHighAlaPortn = _Pm124feAlmClientRxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 2, 24, 1, 17),
    _Pm124feAlmClientRxPwrHighAlaPortn_Type()
)
pm124feAlmClientRxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmClientRxPwrHighAlaPortn.setStatus("current")
_Pm124feAlmClientCrit_ObjectIdentity = ObjectIdentity
pm124feAlmClientCrit = _Pm124feAlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 3)
)
_Pm124feAlmsynthAlmPortTable_Object = MibTable
pm124feAlmsynthAlmPortTable = _Pm124feAlmsynthAlmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    pm124feAlmsynthAlmPortTable.setStatus("current")
_Pm124feAlmsynthAlmPortEntry_Object = MibTableRow
pm124feAlmsynthAlmPortEntry = _Pm124feAlmsynthAlmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 3, 8, 1)
)
pm124feAlmsynthAlmPortEntry.setIndexNames(
    (0, "EKINOPS-Pm124fe-MIB", "pm124feAlmsynthAlmPortIndex"),
)
if mibBuilder.loadTexts:
    pm124feAlmsynthAlmPortEntry.setStatus("current")


class _Pm124feAlmsynthAlmPortIndex_Type(Integer32):
    """Custom type pm124feAlmsynthAlmPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124feAlmsynthAlmPortIndex_Type.__name__ = "Integer32"
_Pm124feAlmsynthAlmPortIndex_Object = MibTableColumn
pm124feAlmsynthAlmPortIndex = _Pm124feAlmsynthAlmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 3, 8, 1, 1),
    _Pm124feAlmsynthAlmPortIndex_Type()
)
pm124feAlmsynthAlmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmsynthAlmPortIndex.setStatus("current")
_Pm124feAlmClientSfpAbsentPortn_Type = EkiOnOff
_Pm124feAlmClientSfpAbsentPortn_Object = MibTableColumn
pm124feAlmClientSfpAbsentPortn = _Pm124feAlmClientSfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 3, 8, 1, 2),
    _Pm124feAlmClientSfpAbsentPortn_Type()
)
pm124feAlmClientSfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmClientSfpAbsentPortn.setStatus("current")
_Pm124feAlmClientDdmAbsentPortn_Type = EkiOnOff
_Pm124feAlmClientDdmAbsentPortn_Object = MibTableColumn
pm124feAlmClientDdmAbsentPortn = _Pm124feAlmClientDdmAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 3, 8, 1, 3),
    _Pm124feAlmClientDdmAbsentPortn_Type()
)
pm124feAlmClientDdmAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmClientDdmAbsentPortn.setStatus("current")
_Pm124feAlmClientHwFailAccPortn_Type = EkiOnOff
_Pm124feAlmClientHwFailAccPortn_Object = MibTableColumn
pm124feAlmClientHwFailAccPortn = _Pm124feAlmClientHwFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 3, 8, 1, 5),
    _Pm124feAlmClientHwFailAccPortn_Type()
)
pm124feAlmClientHwFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmClientHwFailAccPortn.setStatus("current")
_Pm124feAlmClientLsdPortn_Type = EkiOnOff
_Pm124feAlmClientLsdPortn_Object = MibTableColumn
pm124feAlmClientLsdPortn = _Pm124feAlmClientLsdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 3, 8, 1, 6),
    _Pm124feAlmClientLsdPortn_Type()
)
pm124feAlmClientLsdPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmClientLsdPortn.setStatus("current")
_Pm124feAlmClientLocalOosPortn_Type = EkiOnOff
_Pm124feAlmClientLocalOosPortn_Object = MibTableColumn
pm124feAlmClientLocalOosPortn = _Pm124feAlmClientLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 3, 8, 1, 7),
    _Pm124feAlmClientLocalOosPortn_Type()
)
pm124feAlmClientLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmClientLocalOosPortn.setStatus("current")
_Pm124feAlmClientRemoteOosPortn_Type = EkiOnOff
_Pm124feAlmClientRemoteOosPortn_Object = MibTableColumn
pm124feAlmClientRemoteOosPortn = _Pm124feAlmClientRemoteOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 3, 8, 1, 8),
    _Pm124feAlmClientRemoteOosPortn_Type()
)
pm124feAlmClientRemoteOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmClientRemoteOosPortn.setStatus("current")
_Pm124feAlmClientDwCaisPortn_Type = EkiOnOff
_Pm124feAlmClientDwCaisPortn_Object = MibTableColumn
pm124feAlmClientDwCaisPortn = _Pm124feAlmClientDwCaisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 3, 8, 1, 9),
    _Pm124feAlmClientDwCaisPortn_Type()
)
pm124feAlmClientDwCaisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmClientDwCaisPortn.setStatus("current")
_Pm124feAlmClientSfpDdmWarningPortn_Type = EkiOnOff
_Pm124feAlmClientSfpDdmWarningPortn_Object = MibTableColumn
pm124feAlmClientSfpDdmWarningPortn = _Pm124feAlmClientSfpDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 3, 8, 1, 10),
    _Pm124feAlmClientSfpDdmWarningPortn_Type()
)
pm124feAlmClientSfpDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmClientSfpDdmWarningPortn.setStatus("current")
_Pm124feAlmClientSfpDdmAlmPortn_Type = EkiOnOff
_Pm124feAlmClientSfpDdmAlmPortn_Object = MibTableColumn
pm124feAlmClientSfpDdmAlmPortn = _Pm124feAlmClientSfpDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 3, 8, 1, 11),
    _Pm124feAlmClientSfpDdmAlmPortn_Type()
)
pm124feAlmClientSfpDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmClientSfpDdmAlmPortn.setStatus("current")
_Pm124feAlmClientFailAccPortn_Type = EkiOnOff
_Pm124feAlmClientFailAccPortn_Object = MibTableColumn
pm124feAlmClientFailAccPortn = _Pm124feAlmClientFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 3, 8, 1, 13),
    _Pm124feAlmClientFailAccPortn_Type()
)
pm124feAlmClientFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmClientFailAccPortn.setStatus("current")
_Pm124feAlmClientUpCsfPortn_Type = EkiOnOff
_Pm124feAlmClientUpCsfPortn_Object = MibTableColumn
pm124feAlmClientUpCsfPortn = _Pm124feAlmClientUpCsfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 3, 8, 1, 17),
    _Pm124feAlmClientUpCsfPortn_Type()
)
pm124feAlmClientUpCsfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmClientUpCsfPortn.setStatus("current")
_Pm124feAlmclientAccessioAlmTable_Object = MibTable
pm124feAlmclientAccessioAlmTable = _Pm124feAlmclientAccessioAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 3, 16)
)
if mibBuilder.loadTexts:
    pm124feAlmclientAccessioAlmTable.setStatus("current")
_Pm124feAlmclientAccessioAlmEntry_Object = MibTableRow
pm124feAlmclientAccessioAlmEntry = _Pm124feAlmclientAccessioAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 3, 16, 1)
)
pm124feAlmclientAccessioAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm124fe-MIB", "pm124feAlmclientAccessioAlmIndex"),
)
if mibBuilder.loadTexts:
    pm124feAlmclientAccessioAlmEntry.setStatus("current")


class _Pm124feAlmclientAccessioAlmIndex_Type(Integer32):
    """Custom type pm124feAlmclientAccessioAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124feAlmclientAccessioAlmIndex_Type.__name__ = "Integer32"
_Pm124feAlmclientAccessioAlmIndex_Object = MibTableColumn
pm124feAlmclientAccessioAlmIndex = _Pm124feAlmclientAccessioAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 3, 16, 1, 1),
    _Pm124feAlmclientAccessioAlmIndex_Type()
)
pm124feAlmclientAccessioAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmclientAccessioAlmIndex.setStatus("current")
_Pm124feAlmClientLasFailPortn_Type = EkiOnOff
_Pm124feAlmClientLasFailPortn_Object = MibTableColumn
pm124feAlmClientLasFailPortn = _Pm124feAlmClientLasFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 3, 16, 1, 2),
    _Pm124feAlmClientLasFailPortn_Type()
)
pm124feAlmClientLasFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmClientLasFailPortn.setStatus("current")
_Pm124feAlmClientLosPortn_Type = EkiOnOff
_Pm124feAlmClientLosPortn_Object = MibTableColumn
pm124feAlmClientLosPortn = _Pm124feAlmClientLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 3, 16, 1, 5),
    _Pm124feAlmClientLosPortn_Type()
)
pm124feAlmClientLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmClientLosPortn.setStatus("current")
_Pm124feAlmclientAccAlmTable_Object = MibTable
pm124feAlmclientAccAlmTable = _Pm124feAlmclientAccAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 3, 40)
)
if mibBuilder.loadTexts:
    pm124feAlmclientAccAlmTable.setStatus("current")
_Pm124feAlmclientAccAlmEntry_Object = MibTableRow
pm124feAlmclientAccAlmEntry = _Pm124feAlmclientAccAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 3, 40, 1)
)
pm124feAlmclientAccAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm124fe-MIB", "pm124feAlmclientAccAlmIndex"),
)
if mibBuilder.loadTexts:
    pm124feAlmclientAccAlmEntry.setStatus("current")


class _Pm124feAlmclientAccAlmIndex_Type(Integer32):
    """Custom type pm124feAlmclientAccAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124feAlmclientAccAlmIndex_Type.__name__ = "Integer32"
_Pm124feAlmclientAccAlmIndex_Object = MibTableColumn
pm124feAlmclientAccAlmIndex = _Pm124feAlmclientAccAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 3, 40, 1, 1),
    _Pm124feAlmclientAccAlmIndex_Type()
)
pm124feAlmclientAccAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmclientAccAlmIndex.setStatus("current")
_Pm124feAlmClientOosPortn_Type = EkiOnOff
_Pm124feAlmClientOosPortn_Object = MibTableColumn
pm124feAlmClientOosPortn = _Pm124feAlmClientOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 3, 40, 1, 2),
    _Pm124feAlmClientOosPortn_Type()
)
pm124feAlmClientOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmClientOosPortn.setStatus("current")
_Pm124feAlmClientUpEsOvlPortn_Type = EkiOnOff
_Pm124feAlmClientUpEsOvlPortn_Object = MibTableColumn
pm124feAlmClientUpEsOvlPortn = _Pm124feAlmClientUpEsOvlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 3, 40, 1, 11),
    _Pm124feAlmClientUpEsOvlPortn_Type()
)
pm124feAlmClientUpEsOvlPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmClientUpEsOvlPortn.setStatus("current")
_Pm124feAlmClientCsfDetPortn_Type = EkiOnOff
_Pm124feAlmClientCsfDetPortn_Object = MibTableColumn
pm124feAlmClientCsfDetPortn = _Pm124feAlmClientCsfDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 3, 40, 1, 12),
    _Pm124feAlmClientCsfDetPortn_Type()
)
pm124feAlmClientCsfDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmClientCsfDetPortn.setStatus("current")
_Pm124feAlmClientDwEsOvlPortn_Type = EkiOnOff
_Pm124feAlmClientDwEsOvlPortn_Object = MibTableColumn
pm124feAlmClientDwEsOvlPortn = _Pm124feAlmClientDwEsOvlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 2, 3, 40, 1, 15),
    _Pm124feAlmClientDwEsOvlPortn_Type()
)
pm124feAlmClientDwEsOvlPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmClientDwEsOvlPortn.setStatus("current")
_Pm124feAlmLine_ObjectIdentity = ObjectIdentity
pm124feAlmLine = _Pm124feAlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3)
)
_Pm124feAlmLineNurg_ObjectIdentity = ObjectIdentity
pm124feAlmLineNurg = _Pm124feAlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 1)
)
_Pm124feAlmlineSfpWarnDdmTable_Object = MibTable
pm124feAlmlineSfpWarnDdmTable = _Pm124feAlmlineSfpWarnDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 1, 66)
)
if mibBuilder.loadTexts:
    pm124feAlmlineSfpWarnDdmTable.setStatus("current")
_Pm124feAlmlineSfpWarnDdmEntry_Object = MibTableRow
pm124feAlmlineSfpWarnDdmEntry = _Pm124feAlmlineSfpWarnDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 1, 66, 1)
)
pm124feAlmlineSfpWarnDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm124fe-MIB", "pm124feAlmlineSfpWarnDdmIndex"),
)
if mibBuilder.loadTexts:
    pm124feAlmlineSfpWarnDdmEntry.setStatus("current")


class _Pm124feAlmlineSfpWarnDdmIndex_Type(Integer32):
    """Custom type pm124feAlmlineSfpWarnDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124feAlmlineSfpWarnDdmIndex_Type.__name__ = "Integer32"
_Pm124feAlmlineSfpWarnDdmIndex_Object = MibTableColumn
pm124feAlmlineSfpWarnDdmIndex = _Pm124feAlmlineSfpWarnDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 1, 66, 1, 1),
    _Pm124feAlmlineSfpWarnDdmIndex_Type()
)
pm124feAlmlineSfpWarnDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmlineSfpWarnDdmIndex.setStatus("current")
_Pm124feAlmLineTxPwLowWngPortn_Type = EkiOnOff
_Pm124feAlmLineTxPwLowWngPortn_Object = MibTableColumn
pm124feAlmLineTxPwLowWngPortn = _Pm124feAlmLineTxPwLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 1, 66, 1, 2),
    _Pm124feAlmLineTxPwLowWngPortn_Type()
)
pm124feAlmLineTxPwLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmLineTxPwLowWngPortn.setStatus("current")
_Pm124feAlmLineTxPwrHighWngPortn_Type = EkiOnOff
_Pm124feAlmLineTxPwrHighWngPortn_Object = MibTableColumn
pm124feAlmLineTxPwrHighWngPortn = _Pm124feAlmLineTxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 1, 66, 1, 3),
    _Pm124feAlmLineTxPwrHighWngPortn_Type()
)
pm124feAlmLineTxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmLineTxPwrHighWngPortn.setStatus("current")
_Pm124feAlmLineTxBiasLowWngPortn_Type = EkiOnOff
_Pm124feAlmLineTxBiasLowWngPortn_Object = MibTableColumn
pm124feAlmLineTxBiasLowWngPortn = _Pm124feAlmLineTxBiasLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 1, 66, 1, 4),
    _Pm124feAlmLineTxBiasLowWngPortn_Type()
)
pm124feAlmLineTxBiasLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmLineTxBiasLowWngPortn.setStatus("current")
_Pm124feAlmLineTxBiasHighWngPortn_Type = EkiOnOff
_Pm124feAlmLineTxBiasHighWngPortn_Object = MibTableColumn
pm124feAlmLineTxBiasHighWngPortn = _Pm124feAlmLineTxBiasHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 1, 66, 1, 5),
    _Pm124feAlmLineTxBiasHighWngPortn_Type()
)
pm124feAlmLineTxBiasHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmLineTxBiasHighWngPortn.setStatus("current")
_Pm124feAlmLineVccLowWngPortn_Type = EkiOnOff
_Pm124feAlmLineVccLowWngPortn_Object = MibTableColumn
pm124feAlmLineVccLowWngPortn = _Pm124feAlmLineVccLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 1, 66, 1, 6),
    _Pm124feAlmLineVccLowWngPortn_Type()
)
pm124feAlmLineVccLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmLineVccLowWngPortn.setStatus("current")
_Pm124feAlmLineVccHighWngPortn_Type = EkiOnOff
_Pm124feAlmLineVccHighWngPortn_Object = MibTableColumn
pm124feAlmLineVccHighWngPortn = _Pm124feAlmLineVccHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 1, 66, 1, 7),
    _Pm124feAlmLineVccHighWngPortn_Type()
)
pm124feAlmLineVccHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmLineVccHighWngPortn.setStatus("current")
_Pm124feAlmLineTempLowWngPortn_Type = EkiOnOff
_Pm124feAlmLineTempLowWngPortn_Object = MibTableColumn
pm124feAlmLineTempLowWngPortn = _Pm124feAlmLineTempLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 1, 66, 1, 8),
    _Pm124feAlmLineTempLowWngPortn_Type()
)
pm124feAlmLineTempLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmLineTempLowWngPortn.setStatus("current")
_Pm124feAlmLineTempHighWngPortn_Type = EkiOnOff
_Pm124feAlmLineTempHighWngPortn_Object = MibTableColumn
pm124feAlmLineTempHighWngPortn = _Pm124feAlmLineTempHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 1, 66, 1, 9),
    _Pm124feAlmLineTempHighWngPortn_Type()
)
pm124feAlmLineTempHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmLineTempHighWngPortn.setStatus("current")
_Pm124feAlmLineRxPwrLowWngPortn_Type = EkiOnOff
_Pm124feAlmLineRxPwrLowWngPortn_Object = MibTableColumn
pm124feAlmLineRxPwrLowWngPortn = _Pm124feAlmLineRxPwrLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 1, 66, 1, 16),
    _Pm124feAlmLineRxPwrLowWngPortn_Type()
)
pm124feAlmLineRxPwrLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmLineRxPwrLowWngPortn.setStatus("current")
_Pm124feAlmLineRxPwrHighWngPortn_Type = EkiOnOff
_Pm124feAlmLineRxPwrHighWngPortn_Object = MibTableColumn
pm124feAlmLineRxPwrHighWngPortn = _Pm124feAlmLineRxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 1, 66, 1, 17),
    _Pm124feAlmLineRxPwrHighWngPortn_Type()
)
pm124feAlmLineRxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmLineRxPwrHighWngPortn.setStatus("current")
_Pm124feAlmLineUrg_ObjectIdentity = ObjectIdentity
pm124feAlmLineUrg = _Pm124feAlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 2)
)
_Pm124feAlmlineSfpAlmDdmTable_Object = MibTable
pm124feAlmlineSfpAlmDdmTable = _Pm124feAlmlineSfpAlmDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 2, 65)
)
if mibBuilder.loadTexts:
    pm124feAlmlineSfpAlmDdmTable.setStatus("current")
_Pm124feAlmlineSfpAlmDdmEntry_Object = MibTableRow
pm124feAlmlineSfpAlmDdmEntry = _Pm124feAlmlineSfpAlmDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 2, 65, 1)
)
pm124feAlmlineSfpAlmDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm124fe-MIB", "pm124feAlmlineSfpAlmDdmIndex"),
)
if mibBuilder.loadTexts:
    pm124feAlmlineSfpAlmDdmEntry.setStatus("current")


class _Pm124feAlmlineSfpAlmDdmIndex_Type(Integer32):
    """Custom type pm124feAlmlineSfpAlmDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124feAlmlineSfpAlmDdmIndex_Type.__name__ = "Integer32"
_Pm124feAlmlineSfpAlmDdmIndex_Object = MibTableColumn
pm124feAlmlineSfpAlmDdmIndex = _Pm124feAlmlineSfpAlmDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 2, 65, 1, 1),
    _Pm124feAlmlineSfpAlmDdmIndex_Type()
)
pm124feAlmlineSfpAlmDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmlineSfpAlmDdmIndex.setStatus("current")
_Pm124feAlmLineTxPwrLowAlaPortn_Type = EkiOnOff
_Pm124feAlmLineTxPwrLowAlaPortn_Object = MibTableColumn
pm124feAlmLineTxPwrLowAlaPortn = _Pm124feAlmLineTxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 2, 65, 1, 2),
    _Pm124feAlmLineTxPwrLowAlaPortn_Type()
)
pm124feAlmLineTxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmLineTxPwrLowAlaPortn.setStatus("current")
_Pm124feAlmLineTxPwrHighAlaPortn_Type = EkiOnOff
_Pm124feAlmLineTxPwrHighAlaPortn_Object = MibTableColumn
pm124feAlmLineTxPwrHighAlaPortn = _Pm124feAlmLineTxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 2, 65, 1, 3),
    _Pm124feAlmLineTxPwrHighAlaPortn_Type()
)
pm124feAlmLineTxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmLineTxPwrHighAlaPortn.setStatus("current")
_Pm124feAlmLineTxBiasLowAlaPortn_Type = EkiOnOff
_Pm124feAlmLineTxBiasLowAlaPortn_Object = MibTableColumn
pm124feAlmLineTxBiasLowAlaPortn = _Pm124feAlmLineTxBiasLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 2, 65, 1, 4),
    _Pm124feAlmLineTxBiasLowAlaPortn_Type()
)
pm124feAlmLineTxBiasLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmLineTxBiasLowAlaPortn.setStatus("current")
_Pm124feAlmLineTxBiasHighAlaPortn_Type = EkiOnOff
_Pm124feAlmLineTxBiasHighAlaPortn_Object = MibTableColumn
pm124feAlmLineTxBiasHighAlaPortn = _Pm124feAlmLineTxBiasHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 2, 65, 1, 5),
    _Pm124feAlmLineTxBiasHighAlaPortn_Type()
)
pm124feAlmLineTxBiasHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmLineTxBiasHighAlaPortn.setStatus("current")
_Pm124feAlmLineVccLowAlaPortn_Type = EkiOnOff
_Pm124feAlmLineVccLowAlaPortn_Object = MibTableColumn
pm124feAlmLineVccLowAlaPortn = _Pm124feAlmLineVccLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 2, 65, 1, 6),
    _Pm124feAlmLineVccLowAlaPortn_Type()
)
pm124feAlmLineVccLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmLineVccLowAlaPortn.setStatus("current")
_Pm124feAlmLineVccHighAlaPortn_Type = EkiOnOff
_Pm124feAlmLineVccHighAlaPortn_Object = MibTableColumn
pm124feAlmLineVccHighAlaPortn = _Pm124feAlmLineVccHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 2, 65, 1, 7),
    _Pm124feAlmLineVccHighAlaPortn_Type()
)
pm124feAlmLineVccHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmLineVccHighAlaPortn.setStatus("current")
_Pm124feAlmLineTempLowAlaPortn_Type = EkiOnOff
_Pm124feAlmLineTempLowAlaPortn_Object = MibTableColumn
pm124feAlmLineTempLowAlaPortn = _Pm124feAlmLineTempLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 2, 65, 1, 8),
    _Pm124feAlmLineTempLowAlaPortn_Type()
)
pm124feAlmLineTempLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmLineTempLowAlaPortn.setStatus("current")
_Pm124feAlmLineTempHighAlaPortn_Type = EkiOnOff
_Pm124feAlmLineTempHighAlaPortn_Object = MibTableColumn
pm124feAlmLineTempHighAlaPortn = _Pm124feAlmLineTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 2, 65, 1, 9),
    _Pm124feAlmLineTempHighAlaPortn_Type()
)
pm124feAlmLineTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmLineTempHighAlaPortn.setStatus("current")
_Pm124feAlmLineRxPwrLowAlaPortn_Type = EkiOnOff
_Pm124feAlmLineRxPwrLowAlaPortn_Object = MibTableColumn
pm124feAlmLineRxPwrLowAlaPortn = _Pm124feAlmLineRxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 2, 65, 1, 16),
    _Pm124feAlmLineRxPwrLowAlaPortn_Type()
)
pm124feAlmLineRxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmLineRxPwrLowAlaPortn.setStatus("current")
_Pm124feAlmLineRxPwrHighAlaPortn_Type = EkiOnOff
_Pm124feAlmLineRxPwrHighAlaPortn_Object = MibTableColumn
pm124feAlmLineRxPwrHighAlaPortn = _Pm124feAlmLineRxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 2, 65, 1, 17),
    _Pm124feAlmLineRxPwrHighAlaPortn_Type()
)
pm124feAlmLineRxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmLineRxPwrHighAlaPortn.setStatus("current")
_Pm124feAlmLineCrit_ObjectIdentity = ObjectIdentity
pm124feAlmLineCrit = _Pm124feAlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 3)
)
_Pm124feAlmsynthAlmLineTable_Object = MibTable
pm124feAlmsynthAlmLineTable = _Pm124feAlmsynthAlmLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 3, 7)
)
if mibBuilder.loadTexts:
    pm124feAlmsynthAlmLineTable.setStatus("current")
_Pm124feAlmsynthAlmLineEntry_Object = MibTableRow
pm124feAlmsynthAlmLineEntry = _Pm124feAlmsynthAlmLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 3, 7, 1)
)
pm124feAlmsynthAlmLineEntry.setIndexNames(
    (0, "EKINOPS-Pm124fe-MIB", "pm124feAlmsynthAlmLineIndex"),
)
if mibBuilder.loadTexts:
    pm124feAlmsynthAlmLineEntry.setStatus("current")


class _Pm124feAlmsynthAlmLineIndex_Type(Integer32):
    """Custom type pm124feAlmsynthAlmLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124feAlmsynthAlmLineIndex_Type.__name__ = "Integer32"
_Pm124feAlmsynthAlmLineIndex_Object = MibTableColumn
pm124feAlmsynthAlmLineIndex = _Pm124feAlmsynthAlmLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 3, 7, 1, 1),
    _Pm124feAlmsynthAlmLineIndex_Type()
)
pm124feAlmsynthAlmLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmsynthAlmLineIndex.setStatus("current")
_Pm124feAlmLineSfpAbsentPortn_Type = EkiOnOff
_Pm124feAlmLineSfpAbsentPortn_Object = MibTableColumn
pm124feAlmLineSfpAbsentPortn = _Pm124feAlmLineSfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 3, 7, 1, 2),
    _Pm124feAlmLineSfpAbsentPortn_Type()
)
pm124feAlmLineSfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmLineSfpAbsentPortn.setStatus("current")
_Pm124feAlmLineDdmAbsentPortn_Type = EkiOnOff
_Pm124feAlmLineDdmAbsentPortn_Object = MibTableColumn
pm124feAlmLineDdmAbsentPortn = _Pm124feAlmLineDdmAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 3, 7, 1, 3),
    _Pm124feAlmLineDdmAbsentPortn_Type()
)
pm124feAlmLineDdmAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmLineDdmAbsentPortn.setStatus("current")
_Pm124feAlmLineHwFailPortn_Type = EkiOnOff
_Pm124feAlmLineHwFailPortn_Object = MibTableColumn
pm124feAlmLineHwFailPortn = _Pm124feAlmLineHwFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 3, 7, 1, 5),
    _Pm124feAlmLineHwFailPortn_Type()
)
pm124feAlmLineHwFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmLineHwFailPortn.setStatus("current")
_Pm124feAlmLineLsdPortn_Type = EkiOnOff
_Pm124feAlmLineLsdPortn_Object = MibTableColumn
pm124feAlmLineLsdPortn = _Pm124feAlmLineLsdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 3, 7, 1, 6),
    _Pm124feAlmLineLsdPortn_Type()
)
pm124feAlmLineLsdPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmLineLsdPortn.setStatus("current")
_Pm124feAlmLineLocalOosPortn_Type = EkiOnOff
_Pm124feAlmLineLocalOosPortn_Object = MibTableColumn
pm124feAlmLineLocalOosPortn = _Pm124feAlmLineLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 3, 7, 1, 7),
    _Pm124feAlmLineLocalOosPortn_Type()
)
pm124feAlmLineLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmLineLocalOosPortn.setStatus("current")
_Pm124feAlmLineDdmWarningPortn_Type = EkiOnOff
_Pm124feAlmLineDdmWarningPortn_Object = MibTableColumn
pm124feAlmLineDdmWarningPortn = _Pm124feAlmLineDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 3, 7, 1, 10),
    _Pm124feAlmLineDdmWarningPortn_Type()
)
pm124feAlmLineDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmLineDdmWarningPortn.setStatus("current")
_Pm124feAlmLineDdmAlmPortn_Type = EkiOnOff
_Pm124feAlmLineDdmAlmPortn_Object = MibTableColumn
pm124feAlmLineDdmAlmPortn = _Pm124feAlmLineDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 3, 7, 1, 11),
    _Pm124feAlmLineDdmAlmPortn_Type()
)
pm124feAlmLineDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmLineDdmAlmPortn.setStatus("current")
_Pm124feAlmLineFailPortn_Type = EkiOnOff
_Pm124feAlmLineFailPortn_Object = MibTableColumn
pm124feAlmLineFailPortn = _Pm124feAlmLineFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 3, 7, 1, 13),
    _Pm124feAlmLineFailPortn_Type()
)
pm124feAlmLineFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmLineFailPortn.setStatus("current")
_Pm124feAlmlineAccessioAlmTable_Object = MibTable
pm124feAlmlineAccessioAlmTable = _Pm124feAlmlineAccessioAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 3, 64)
)
if mibBuilder.loadTexts:
    pm124feAlmlineAccessioAlmTable.setStatus("current")
_Pm124feAlmlineAccessioAlmEntry_Object = MibTableRow
pm124feAlmlineAccessioAlmEntry = _Pm124feAlmlineAccessioAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 3, 64, 1)
)
pm124feAlmlineAccessioAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm124fe-MIB", "pm124feAlmlineAccessioAlmIndex"),
)
if mibBuilder.loadTexts:
    pm124feAlmlineAccessioAlmEntry.setStatus("current")


class _Pm124feAlmlineAccessioAlmIndex_Type(Integer32):
    """Custom type pm124feAlmlineAccessioAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124feAlmlineAccessioAlmIndex_Type.__name__ = "Integer32"
_Pm124feAlmlineAccessioAlmIndex_Object = MibTableColumn
pm124feAlmlineAccessioAlmIndex = _Pm124feAlmlineAccessioAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 3, 64, 1, 1),
    _Pm124feAlmlineAccessioAlmIndex_Type()
)
pm124feAlmlineAccessioAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmlineAccessioAlmIndex.setStatus("current")
_Pm124feAlmLineLasFailPortn_Type = EkiOnOff
_Pm124feAlmLineLasFailPortn_Object = MibTableColumn
pm124feAlmLineLasFailPortn = _Pm124feAlmLineLasFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 3, 64, 1, 2),
    _Pm124feAlmLineLasFailPortn_Type()
)
pm124feAlmLineLasFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmLineLasFailPortn.setStatus("current")
_Pm124feAlmLineLosPortn_Type = EkiOnOff
_Pm124feAlmLineLosPortn_Object = MibTableColumn
pm124feAlmLineLosPortn = _Pm124feAlmLineLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 3, 64, 1, 5),
    _Pm124feAlmLineLosPortn_Type()
)
pm124feAlmLineLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmLineLosPortn.setStatus("current")
_Pm124feAlmLineLossSyncPortn_Type = EkiOnOff
_Pm124feAlmLineLossSyncPortn_Object = MibTableColumn
pm124feAlmLineLossSyncPortn = _Pm124feAlmLineLossSyncPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 2, 3, 3, 64, 1, 7),
    _Pm124feAlmLineLossSyncPortn_Type()
)
pm124feAlmLineLossSyncPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feAlmLineLossSyncPortn.setStatus("current")
_Pm124femeasures_ObjectIdentity = ObjectIdentity
pm124femeasures = _Pm124femeasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3)
)
_Pm124feMesrOther_ObjectIdentity = ObjectIdentity
pm124feMesrOther = _Pm124feMesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 1)
)
_Pm124feMesrClient_ObjectIdentity = ObjectIdentity
pm124feMesrClient = _Pm124feMesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 2)
)
_Pm124feMesrclientTemperatureTable_Object = MibTable
pm124feMesrclientTemperatureTable = _Pm124feMesrclientTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 2, 16)
)
if mibBuilder.loadTexts:
    pm124feMesrclientTemperatureTable.setStatus("current")
_Pm124feMesrclientTemperatureEntry_Object = MibTableRow
pm124feMesrclientTemperatureEntry = _Pm124feMesrclientTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 2, 16, 1)
)
pm124feMesrclientTemperatureEntry.setIndexNames(
    (0, "EKINOPS-Pm124fe-MIB", "pm124feMesrclientTemperatureIndex"),
)
if mibBuilder.loadTexts:
    pm124feMesrclientTemperatureEntry.setStatus("current")


class _Pm124feMesrclientTemperatureIndex_Type(Integer32):
    """Custom type pm124feMesrclientTemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124feMesrclientTemperatureIndex_Type.__name__ = "Integer32"
_Pm124feMesrclientTemperatureIndex_Object = MibTableColumn
pm124feMesrclientTemperatureIndex = _Pm124feMesrclientTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 2, 16, 1, 1),
    _Pm124feMesrclientTemperatureIndex_Type()
)
pm124feMesrclientTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feMesrclientTemperatureIndex.setStatus("current")


class _Pm124feMesrclientTemperaturePortn_Type(Integer32):
    """Custom type pm124feMesrclientTemperaturePortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm124feMesrclientTemperaturePortn_Type.__name__ = "Integer32"
_Pm124feMesrclientTemperaturePortn_Object = MibTableColumn
pm124feMesrclientTemperaturePortn = _Pm124feMesrclientTemperaturePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 2, 16, 1, 2),
    _Pm124feMesrclientTemperaturePortn_Type()
)
pm124feMesrclientTemperaturePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feMesrclientTemperaturePortn.setStatus("current")
_Pm124feMesrclientVoltTable_Object = MibTable
pm124feMesrclientVoltTable = _Pm124feMesrclientVoltTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 2, 24)
)
if mibBuilder.loadTexts:
    pm124feMesrclientVoltTable.setStatus("current")
_Pm124feMesrclientVoltEntry_Object = MibTableRow
pm124feMesrclientVoltEntry = _Pm124feMesrclientVoltEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 2, 24, 1)
)
pm124feMesrclientVoltEntry.setIndexNames(
    (0, "EKINOPS-Pm124fe-MIB", "pm124feMesrclientVoltIndex"),
)
if mibBuilder.loadTexts:
    pm124feMesrclientVoltEntry.setStatus("current")


class _Pm124feMesrclientVoltIndex_Type(Integer32):
    """Custom type pm124feMesrclientVoltIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124feMesrclientVoltIndex_Type.__name__ = "Integer32"
_Pm124feMesrclientVoltIndex_Object = MibTableColumn
pm124feMesrclientVoltIndex = _Pm124feMesrclientVoltIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 2, 24, 1, 1),
    _Pm124feMesrclientVoltIndex_Type()
)
pm124feMesrclientVoltIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feMesrclientVoltIndex.setStatus("current")


class _Pm124feMesrclientVoltPortn_Type(Integer32):
    """Custom type pm124feMesrclientVoltPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm124feMesrclientVoltPortn_Type.__name__ = "Integer32"
_Pm124feMesrclientVoltPortn_Object = MibTableColumn
pm124feMesrclientVoltPortn = _Pm124feMesrclientVoltPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 2, 24, 1, 2),
    _Pm124feMesrclientVoltPortn_Type()
)
pm124feMesrclientVoltPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feMesrclientVoltPortn.setStatus("current")
_Pm124feMesrclientTxBiasTable_Object = MibTable
pm124feMesrclientTxBiasTable = _Pm124feMesrclientTxBiasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 2, 32)
)
if mibBuilder.loadTexts:
    pm124feMesrclientTxBiasTable.setStatus("current")
_Pm124feMesrclientTxBiasEntry_Object = MibTableRow
pm124feMesrclientTxBiasEntry = _Pm124feMesrclientTxBiasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 2, 32, 1)
)
pm124feMesrclientTxBiasEntry.setIndexNames(
    (0, "EKINOPS-Pm124fe-MIB", "pm124feMesrclientTxBiasIndex"),
)
if mibBuilder.loadTexts:
    pm124feMesrclientTxBiasEntry.setStatus("current")


class _Pm124feMesrclientTxBiasIndex_Type(Integer32):
    """Custom type pm124feMesrclientTxBiasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124feMesrclientTxBiasIndex_Type.__name__ = "Integer32"
_Pm124feMesrclientTxBiasIndex_Object = MibTableColumn
pm124feMesrclientTxBiasIndex = _Pm124feMesrclientTxBiasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 2, 32, 1, 1),
    _Pm124feMesrclientTxBiasIndex_Type()
)
pm124feMesrclientTxBiasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feMesrclientTxBiasIndex.setStatus("current")


class _Pm124feMesrclientTxBiasPortn_Type(Integer32):
    """Custom type pm124feMesrclientTxBiasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm124feMesrclientTxBiasPortn_Type.__name__ = "Integer32"
_Pm124feMesrclientTxBiasPortn_Object = MibTableColumn
pm124feMesrclientTxBiasPortn = _Pm124feMesrclientTxBiasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 2, 32, 1, 2),
    _Pm124feMesrclientTxBiasPortn_Type()
)
pm124feMesrclientTxBiasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feMesrclientTxBiasPortn.setStatus("current")
_Pm124feMesrclientTxPowerTable_Object = MibTable
pm124feMesrclientTxPowerTable = _Pm124feMesrclientTxPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 2, 40)
)
if mibBuilder.loadTexts:
    pm124feMesrclientTxPowerTable.setStatus("current")
_Pm124feMesrclientTxPowerEntry_Object = MibTableRow
pm124feMesrclientTxPowerEntry = _Pm124feMesrclientTxPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 2, 40, 1)
)
pm124feMesrclientTxPowerEntry.setIndexNames(
    (0, "EKINOPS-Pm124fe-MIB", "pm124feMesrclientTxPowerIndex"),
)
if mibBuilder.loadTexts:
    pm124feMesrclientTxPowerEntry.setStatus("current")


class _Pm124feMesrclientTxPowerIndex_Type(Integer32):
    """Custom type pm124feMesrclientTxPowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124feMesrclientTxPowerIndex_Type.__name__ = "Integer32"
_Pm124feMesrclientTxPowerIndex_Object = MibTableColumn
pm124feMesrclientTxPowerIndex = _Pm124feMesrclientTxPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 2, 40, 1, 1),
    _Pm124feMesrclientTxPowerIndex_Type()
)
pm124feMesrclientTxPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feMesrclientTxPowerIndex.setStatus("current")


class _Pm124feMesrclientTxPowerPortn_Type(Integer32):
    """Custom type pm124feMesrclientTxPowerPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm124feMesrclientTxPowerPortn_Type.__name__ = "Integer32"
_Pm124feMesrclientTxPowerPortn_Object = MibTableColumn
pm124feMesrclientTxPowerPortn = _Pm124feMesrclientTxPowerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 2, 40, 1, 2),
    _Pm124feMesrclientTxPowerPortn_Type()
)
pm124feMesrclientTxPowerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feMesrclientTxPowerPortn.setStatus("current")
_Pm124feMesrclientRxPowerTable_Object = MibTable
pm124feMesrclientRxPowerTable = _Pm124feMesrclientRxPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 2, 48)
)
if mibBuilder.loadTexts:
    pm124feMesrclientRxPowerTable.setStatus("current")
_Pm124feMesrclientRxPowerEntry_Object = MibTableRow
pm124feMesrclientRxPowerEntry = _Pm124feMesrclientRxPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 2, 48, 1)
)
pm124feMesrclientRxPowerEntry.setIndexNames(
    (0, "EKINOPS-Pm124fe-MIB", "pm124feMesrclientRxPowerIndex"),
)
if mibBuilder.loadTexts:
    pm124feMesrclientRxPowerEntry.setStatus("current")


class _Pm124feMesrclientRxPowerIndex_Type(Integer32):
    """Custom type pm124feMesrclientRxPowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124feMesrclientRxPowerIndex_Type.__name__ = "Integer32"
_Pm124feMesrclientRxPowerIndex_Object = MibTableColumn
pm124feMesrclientRxPowerIndex = _Pm124feMesrclientRxPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 2, 48, 1, 1),
    _Pm124feMesrclientRxPowerIndex_Type()
)
pm124feMesrclientRxPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feMesrclientRxPowerIndex.setStatus("current")


class _Pm124feMesrclientRxPowerPortn_Type(Integer32):
    """Custom type pm124feMesrclientRxPowerPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm124feMesrclientRxPowerPortn_Type.__name__ = "Integer32"
_Pm124feMesrclientRxPowerPortn_Object = MibTableColumn
pm124feMesrclientRxPowerPortn = _Pm124feMesrclientRxPowerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 2, 48, 1, 2),
    _Pm124feMesrclientRxPowerPortn_Type()
)
pm124feMesrclientRxPowerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feMesrclientRxPowerPortn.setStatus("current")
_Pm124feMesrLine_ObjectIdentity = ObjectIdentity
pm124feMesrLine = _Pm124feMesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 3)
)
_Pm124feMesrlineTemperatureTable_Object = MibTable
pm124feMesrlineTemperatureTable = _Pm124feMesrlineTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 3, 64)
)
if mibBuilder.loadTexts:
    pm124feMesrlineTemperatureTable.setStatus("current")
_Pm124feMesrlineTemperatureEntry_Object = MibTableRow
pm124feMesrlineTemperatureEntry = _Pm124feMesrlineTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 3, 64, 1)
)
pm124feMesrlineTemperatureEntry.setIndexNames(
    (0, "EKINOPS-Pm124fe-MIB", "pm124feMesrlineTemperatureIndex"),
)
if mibBuilder.loadTexts:
    pm124feMesrlineTemperatureEntry.setStatus("current")


class _Pm124feMesrlineTemperatureIndex_Type(Integer32):
    """Custom type pm124feMesrlineTemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124feMesrlineTemperatureIndex_Type.__name__ = "Integer32"
_Pm124feMesrlineTemperatureIndex_Object = MibTableColumn
pm124feMesrlineTemperatureIndex = _Pm124feMesrlineTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 3, 64, 1, 1),
    _Pm124feMesrlineTemperatureIndex_Type()
)
pm124feMesrlineTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feMesrlineTemperatureIndex.setStatus("current")


class _Pm124feMesrlineTemperaturePortn_Type(Integer32):
    """Custom type pm124feMesrlineTemperaturePortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm124feMesrlineTemperaturePortn_Type.__name__ = "Integer32"
_Pm124feMesrlineTemperaturePortn_Object = MibTableColumn
pm124feMesrlineTemperaturePortn = _Pm124feMesrlineTemperaturePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 3, 64, 1, 2),
    _Pm124feMesrlineTemperaturePortn_Type()
)
pm124feMesrlineTemperaturePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feMesrlineTemperaturePortn.setStatus("current")
_Pm124feMesrlineVoltTable_Object = MibTable
pm124feMesrlineVoltTable = _Pm124feMesrlineVoltTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 3, 65)
)
if mibBuilder.loadTexts:
    pm124feMesrlineVoltTable.setStatus("current")
_Pm124feMesrlineVoltEntry_Object = MibTableRow
pm124feMesrlineVoltEntry = _Pm124feMesrlineVoltEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 3, 65, 1)
)
pm124feMesrlineVoltEntry.setIndexNames(
    (0, "EKINOPS-Pm124fe-MIB", "pm124feMesrlineVoltIndex"),
)
if mibBuilder.loadTexts:
    pm124feMesrlineVoltEntry.setStatus("current")


class _Pm124feMesrlineVoltIndex_Type(Integer32):
    """Custom type pm124feMesrlineVoltIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124feMesrlineVoltIndex_Type.__name__ = "Integer32"
_Pm124feMesrlineVoltIndex_Object = MibTableColumn
pm124feMesrlineVoltIndex = _Pm124feMesrlineVoltIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 3, 65, 1, 1),
    _Pm124feMesrlineVoltIndex_Type()
)
pm124feMesrlineVoltIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feMesrlineVoltIndex.setStatus("current")


class _Pm124feMesrlineVoltPortn_Type(Integer32):
    """Custom type pm124feMesrlineVoltPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm124feMesrlineVoltPortn_Type.__name__ = "Integer32"
_Pm124feMesrlineVoltPortn_Object = MibTableColumn
pm124feMesrlineVoltPortn = _Pm124feMesrlineVoltPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 3, 65, 1, 2),
    _Pm124feMesrlineVoltPortn_Type()
)
pm124feMesrlineVoltPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feMesrlineVoltPortn.setStatus("current")
_Pm124feMesrlineTxBiasTable_Object = MibTable
pm124feMesrlineTxBiasTable = _Pm124feMesrlineTxBiasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 3, 66)
)
if mibBuilder.loadTexts:
    pm124feMesrlineTxBiasTable.setStatus("current")
_Pm124feMesrlineTxBiasEntry_Object = MibTableRow
pm124feMesrlineTxBiasEntry = _Pm124feMesrlineTxBiasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 3, 66, 1)
)
pm124feMesrlineTxBiasEntry.setIndexNames(
    (0, "EKINOPS-Pm124fe-MIB", "pm124feMesrlineTxBiasIndex"),
)
if mibBuilder.loadTexts:
    pm124feMesrlineTxBiasEntry.setStatus("current")


class _Pm124feMesrlineTxBiasIndex_Type(Integer32):
    """Custom type pm124feMesrlineTxBiasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124feMesrlineTxBiasIndex_Type.__name__ = "Integer32"
_Pm124feMesrlineTxBiasIndex_Object = MibTableColumn
pm124feMesrlineTxBiasIndex = _Pm124feMesrlineTxBiasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 3, 66, 1, 1),
    _Pm124feMesrlineTxBiasIndex_Type()
)
pm124feMesrlineTxBiasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feMesrlineTxBiasIndex.setStatus("current")


class _Pm124feMesrlineTxBiasPortn_Type(Integer32):
    """Custom type pm124feMesrlineTxBiasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm124feMesrlineTxBiasPortn_Type.__name__ = "Integer32"
_Pm124feMesrlineTxBiasPortn_Object = MibTableColumn
pm124feMesrlineTxBiasPortn = _Pm124feMesrlineTxBiasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 3, 66, 1, 2),
    _Pm124feMesrlineTxBiasPortn_Type()
)
pm124feMesrlineTxBiasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feMesrlineTxBiasPortn.setStatus("current")
_Pm124feMesrlineTxPowerTable_Object = MibTable
pm124feMesrlineTxPowerTable = _Pm124feMesrlineTxPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 3, 67)
)
if mibBuilder.loadTexts:
    pm124feMesrlineTxPowerTable.setStatus("current")
_Pm124feMesrlineTxPowerEntry_Object = MibTableRow
pm124feMesrlineTxPowerEntry = _Pm124feMesrlineTxPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 3, 67, 1)
)
pm124feMesrlineTxPowerEntry.setIndexNames(
    (0, "EKINOPS-Pm124fe-MIB", "pm124feMesrlineTxPowerIndex"),
)
if mibBuilder.loadTexts:
    pm124feMesrlineTxPowerEntry.setStatus("current")


class _Pm124feMesrlineTxPowerIndex_Type(Integer32):
    """Custom type pm124feMesrlineTxPowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124feMesrlineTxPowerIndex_Type.__name__ = "Integer32"
_Pm124feMesrlineTxPowerIndex_Object = MibTableColumn
pm124feMesrlineTxPowerIndex = _Pm124feMesrlineTxPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 3, 67, 1, 1),
    _Pm124feMesrlineTxPowerIndex_Type()
)
pm124feMesrlineTxPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feMesrlineTxPowerIndex.setStatus("current")


class _Pm124feMesrlineTxPowerPortn_Type(Integer32):
    """Custom type pm124feMesrlineTxPowerPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm124feMesrlineTxPowerPortn_Type.__name__ = "Integer32"
_Pm124feMesrlineTxPowerPortn_Object = MibTableColumn
pm124feMesrlineTxPowerPortn = _Pm124feMesrlineTxPowerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 3, 67, 1, 2),
    _Pm124feMesrlineTxPowerPortn_Type()
)
pm124feMesrlineTxPowerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feMesrlineTxPowerPortn.setStatus("current")
_Pm124feMesrlineRxPowerTable_Object = MibTable
pm124feMesrlineRxPowerTable = _Pm124feMesrlineRxPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 3, 68)
)
if mibBuilder.loadTexts:
    pm124feMesrlineRxPowerTable.setStatus("current")
_Pm124feMesrlineRxPowerEntry_Object = MibTableRow
pm124feMesrlineRxPowerEntry = _Pm124feMesrlineRxPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 3, 68, 1)
)
pm124feMesrlineRxPowerEntry.setIndexNames(
    (0, "EKINOPS-Pm124fe-MIB", "pm124feMesrlineRxPowerIndex"),
)
if mibBuilder.loadTexts:
    pm124feMesrlineRxPowerEntry.setStatus("current")


class _Pm124feMesrlineRxPowerIndex_Type(Integer32):
    """Custom type pm124feMesrlineRxPowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124feMesrlineRxPowerIndex_Type.__name__ = "Integer32"
_Pm124feMesrlineRxPowerIndex_Object = MibTableColumn
pm124feMesrlineRxPowerIndex = _Pm124feMesrlineRxPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 3, 68, 1, 1),
    _Pm124feMesrlineRxPowerIndex_Type()
)
pm124feMesrlineRxPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feMesrlineRxPowerIndex.setStatus("current")


class _Pm124feMesrlineRxPowerPortn_Type(Integer32):
    """Custom type pm124feMesrlineRxPowerPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm124feMesrlineRxPowerPortn_Type.__name__ = "Integer32"
_Pm124feMesrlineRxPowerPortn_Object = MibTableColumn
pm124feMesrlineRxPowerPortn = _Pm124feMesrlineRxPowerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 3, 3, 68, 1, 2),
    _Pm124feMesrlineRxPowerPortn_Type()
)
pm124feMesrlineRxPowerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feMesrlineRxPowerPortn.setStatus("current")
_Pm124fecounters_ObjectIdentity = ObjectIdentity
pm124fecounters = _Pm124fecounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 4)
)
_Pm124feCntOther_ObjectIdentity = ObjectIdentity
pm124feCntOther = _Pm124feCntOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 4, 1)
)
_Pm124feCntClient_ObjectIdentity = ObjectIdentity
pm124feCntClient = _Pm124feCntClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 4, 2)
)
_Pm124feCntclientCbipErrCntTable_Object = MibTable
pm124feCntclientCbipErrCntTable = _Pm124feCntclientCbipErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 4, 2, 16)
)
if mibBuilder.loadTexts:
    pm124feCntclientCbipErrCntTable.setStatus("current")
_Pm124feCntclientCbipErrCntEntry_Object = MibTableRow
pm124feCntclientCbipErrCntEntry = _Pm124feCntclientCbipErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 4, 2, 16, 1)
)
pm124feCntclientCbipErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pm124fe-MIB", "pm124feCntclientCbipErrCntIndex"),
)
if mibBuilder.loadTexts:
    pm124feCntclientCbipErrCntEntry.setStatus("current")


class _Pm124feCntclientCbipErrCntIndex_Type(Integer32):
    """Custom type pm124feCntclientCbipErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124feCntclientCbipErrCntIndex_Type.__name__ = "Integer32"
_Pm124feCntclientCbipErrCntIndex_Object = MibTableColumn
pm124feCntclientCbipErrCntIndex = _Pm124feCntclientCbipErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 4, 2, 16, 1, 1),
    _Pm124feCntclientCbipErrCntIndex_Type()
)
pm124feCntclientCbipErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feCntclientCbipErrCntIndex.setStatus("current")
_Pm124feCntclientCbipErrCntValuePortn_Type = Counter32
_Pm124feCntclientCbipErrCntValuePortn_Object = MibTableColumn
pm124feCntclientCbipErrCntValuePortn = _Pm124feCntclientCbipErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 4, 2, 16, 1, 2),
    _Pm124feCntclientCbipErrCntValuePortn_Type()
)
pm124feCntclientCbipErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feCntclientCbipErrCntValuePortn.setStatus("current")
_Pm124feCntclientCbipErrCntErrorPortn_Type = EkiOnOff
_Pm124feCntclientCbipErrCntErrorPortn_Object = MibTableColumn
pm124feCntclientCbipErrCntErrorPortn = _Pm124feCntclientCbipErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 4, 2, 16, 1, 3),
    _Pm124feCntclientCbipErrCntErrorPortn_Type()
)
pm124feCntclientCbipErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feCntclientCbipErrCntErrorPortn.setStatus("current")
_Pm124feCntclientCbipErrCntOverloadPortn_Type = EkiOnOff
_Pm124feCntclientCbipErrCntOverloadPortn_Object = MibTableColumn
pm124feCntclientCbipErrCntOverloadPortn = _Pm124feCntclientCbipErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 4, 2, 16, 1, 4),
    _Pm124feCntclientCbipErrCntOverloadPortn_Type()
)
pm124feCntclientCbipErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feCntclientCbipErrCntOverloadPortn.setStatus("current")
_Pm124feCntclientFcsErrCntTable_Object = MibTable
pm124feCntclientFcsErrCntTable = _Pm124feCntclientFcsErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 4, 2, 24)
)
if mibBuilder.loadTexts:
    pm124feCntclientFcsErrCntTable.setStatus("current")
_Pm124feCntclientFcsErrCntEntry_Object = MibTableRow
pm124feCntclientFcsErrCntEntry = _Pm124feCntclientFcsErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 4, 2, 24, 1)
)
pm124feCntclientFcsErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pm124fe-MIB", "pm124feCntclientFcsErrCntIndex"),
)
if mibBuilder.loadTexts:
    pm124feCntclientFcsErrCntEntry.setStatus("current")


class _Pm124feCntclientFcsErrCntIndex_Type(Integer32):
    """Custom type pm124feCntclientFcsErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124feCntclientFcsErrCntIndex_Type.__name__ = "Integer32"
_Pm124feCntclientFcsErrCntIndex_Object = MibTableColumn
pm124feCntclientFcsErrCntIndex = _Pm124feCntclientFcsErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 4, 2, 24, 1, 1),
    _Pm124feCntclientFcsErrCntIndex_Type()
)
pm124feCntclientFcsErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feCntclientFcsErrCntIndex.setStatus("current")
_Pm124feCntclientFcsErrCntValuePortn_Type = Counter32
_Pm124feCntclientFcsErrCntValuePortn_Object = MibTableColumn
pm124feCntclientFcsErrCntValuePortn = _Pm124feCntclientFcsErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 4, 2, 24, 1, 2),
    _Pm124feCntclientFcsErrCntValuePortn_Type()
)
pm124feCntclientFcsErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feCntclientFcsErrCntValuePortn.setStatus("current")
_Pm124feCntclientFcsErrCntErrorPortn_Type = EkiOnOff
_Pm124feCntclientFcsErrCntErrorPortn_Object = MibTableColumn
pm124feCntclientFcsErrCntErrorPortn = _Pm124feCntclientFcsErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 4, 2, 24, 1, 3),
    _Pm124feCntclientFcsErrCntErrorPortn_Type()
)
pm124feCntclientFcsErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feCntclientFcsErrCntErrorPortn.setStatus("current")
_Pm124feCntclientFcsErrCntOverloadPortn_Type = EkiOnOff
_Pm124feCntclientFcsErrCntOverloadPortn_Object = MibTableColumn
pm124feCntclientFcsErrCntOverloadPortn = _Pm124feCntclientFcsErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 4, 2, 24, 1, 4),
    _Pm124feCntclientFcsErrCntOverloadPortn_Type()
)
pm124feCntclientFcsErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feCntclientFcsErrCntOverloadPortn.setStatus("current")
_Pm124feCntLine_ObjectIdentity = ObjectIdentity
pm124feCntLine = _Pm124feCntLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 4, 3)
)
_Pm124feCntlineDispErrCntTable_Object = MibTable
pm124feCntlineDispErrCntTable = _Pm124feCntlineDispErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 4, 3, 64)
)
if mibBuilder.loadTexts:
    pm124feCntlineDispErrCntTable.setStatus("current")
_Pm124feCntlineDispErrCntEntry_Object = MibTableRow
pm124feCntlineDispErrCntEntry = _Pm124feCntlineDispErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 4, 3, 64, 1)
)
pm124feCntlineDispErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pm124fe-MIB", "pm124feCntlineDispErrCntIndex"),
)
if mibBuilder.loadTexts:
    pm124feCntlineDispErrCntEntry.setStatus("current")


class _Pm124feCntlineDispErrCntIndex_Type(Integer32):
    """Custom type pm124feCntlineDispErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124feCntlineDispErrCntIndex_Type.__name__ = "Integer32"
_Pm124feCntlineDispErrCntIndex_Object = MibTableColumn
pm124feCntlineDispErrCntIndex = _Pm124feCntlineDispErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 4, 3, 64, 1, 1),
    _Pm124feCntlineDispErrCntIndex_Type()
)
pm124feCntlineDispErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feCntlineDispErrCntIndex.setStatus("current")
_Pm124feCntlineDispErrCntValuePortn_Type = Counter32
_Pm124feCntlineDispErrCntValuePortn_Object = MibTableColumn
pm124feCntlineDispErrCntValuePortn = _Pm124feCntlineDispErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 4, 3, 64, 1, 2),
    _Pm124feCntlineDispErrCntValuePortn_Type()
)
pm124feCntlineDispErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feCntlineDispErrCntValuePortn.setStatus("current")
_Pm124feCntlineDispErrCntErrorPortn_Type = EkiOnOff
_Pm124feCntlineDispErrCntErrorPortn_Object = MibTableColumn
pm124feCntlineDispErrCntErrorPortn = _Pm124feCntlineDispErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 4, 3, 64, 1, 3),
    _Pm124feCntlineDispErrCntErrorPortn_Type()
)
pm124feCntlineDispErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feCntlineDispErrCntErrorPortn.setStatus("current")
_Pm124feCntlineDispErrCntOverloadPortn_Type = EkiOnOff
_Pm124feCntlineDispErrCntOverloadPortn_Object = MibTableColumn
pm124feCntlineDispErrCntOverloadPortn = _Pm124feCntlineDispErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 4, 3, 64, 1, 4),
    _Pm124feCntlineDispErrCntOverloadPortn_Type()
)
pm124feCntlineDispErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feCntlineDispErrCntOverloadPortn.setStatus("current")
_Pm124feCntlineCrcErrCntTable_Object = MibTable
pm124feCntlineCrcErrCntTable = _Pm124feCntlineCrcErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 4, 3, 65)
)
if mibBuilder.loadTexts:
    pm124feCntlineCrcErrCntTable.setStatus("current")
_Pm124feCntlineCrcErrCntEntry_Object = MibTableRow
pm124feCntlineCrcErrCntEntry = _Pm124feCntlineCrcErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 4, 3, 65, 1)
)
pm124feCntlineCrcErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pm124fe-MIB", "pm124feCntlineCrcErrCntIndex"),
)
if mibBuilder.loadTexts:
    pm124feCntlineCrcErrCntEntry.setStatus("current")


class _Pm124feCntlineCrcErrCntIndex_Type(Integer32):
    """Custom type pm124feCntlineCrcErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124feCntlineCrcErrCntIndex_Type.__name__ = "Integer32"
_Pm124feCntlineCrcErrCntIndex_Object = MibTableColumn
pm124feCntlineCrcErrCntIndex = _Pm124feCntlineCrcErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 4, 3, 65, 1, 1),
    _Pm124feCntlineCrcErrCntIndex_Type()
)
pm124feCntlineCrcErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feCntlineCrcErrCntIndex.setStatus("current")
_Pm124feCntlineCrcErrCntValuePortn_Type = Counter32
_Pm124feCntlineCrcErrCntValuePortn_Object = MibTableColumn
pm124feCntlineCrcErrCntValuePortn = _Pm124feCntlineCrcErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 4, 3, 65, 1, 2),
    _Pm124feCntlineCrcErrCntValuePortn_Type()
)
pm124feCntlineCrcErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feCntlineCrcErrCntValuePortn.setStatus("current")
_Pm124feCntlineCrcErrCntErrorPortn_Type = EkiOnOff
_Pm124feCntlineCrcErrCntErrorPortn_Object = MibTableColumn
pm124feCntlineCrcErrCntErrorPortn = _Pm124feCntlineCrcErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 4, 3, 65, 1, 3),
    _Pm124feCntlineCrcErrCntErrorPortn_Type()
)
pm124feCntlineCrcErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feCntlineCrcErrCntErrorPortn.setStatus("current")
_Pm124feCntlineCrcErrCntOverloadPortn_Type = EkiOnOff
_Pm124feCntlineCrcErrCntOverloadPortn_Object = MibTableColumn
pm124feCntlineCrcErrCntOverloadPortn = _Pm124feCntlineCrcErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 4, 3, 65, 1, 4),
    _Pm124feCntlineCrcErrCntOverloadPortn_Type()
)
pm124feCntlineCrcErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feCntlineCrcErrCntOverloadPortn.setStatus("current")
_Pm124feCntCountersReset_Type = EkiOnOff
_Pm124feCntCountersReset_Object = MibScalar
pm124feCntCountersReset = _Pm124feCntCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 4, 259),
    _Pm124feCntCountersReset_Type()
)
pm124feCntCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124feCntCountersReset.setStatus("current")
_Pm124feCntCountersStop_Type = EkiOnOff
_Pm124feCntCountersStop_Object = MibScalar
pm124feCntCountersStop = _Pm124feCntCountersStop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 4, 260),
    _Pm124feCntCountersStop_Type()
)
pm124feCntCountersStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124feCntCountersStop.setStatus("current")
_Pm124fecontrolsWrite_ObjectIdentity = ObjectIdentity
pm124fecontrolsWrite = _Pm124fecontrolsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6)
)
_Pm124feCtrlOther_ObjectIdentity = ObjectIdentity
pm124feCtrlOther = _Pm124feCtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 1)
)
_Pm124feCtrlsynth0_ObjectIdentity = ObjectIdentity
pm124feCtrlsynth0 = _Pm124feCtrlsynth0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 1, 0)
)
_Pm124feCtrlConfLoad_Type = EkiOnOff
_Pm124feCtrlConfLoad_Object = MibScalar
pm124feCtrlConfLoad = _Pm124feCtrlConfLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 1, 0, 1),
    _Pm124feCtrlConfLoad_Type()
)
pm124feCtrlConfLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124feCtrlConfLoad.setStatus("current")
_Pm124feCtrlConfFlash_Type = EkiOnOff
_Pm124feCtrlConfFlash_Object = MibScalar
pm124feCtrlConfFlash = _Pm124feCtrlConfFlash_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 1, 0, 9),
    _Pm124feCtrlConfFlash_Type()
)
pm124feCtrlConfFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124feCtrlConfFlash.setStatus("current")
_Pm124feCtrlConfClear_Type = EkiOnOff
_Pm124feCtrlConfClear_Object = MibScalar
pm124feCtrlConfClear = _Pm124feCtrlConfClear_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 1, 0, 13),
    _Pm124feCtrlConfClear_Type()
)
pm124feCtrlConfClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124feCtrlConfClear.setStatus("current")
_Pm124feCtrlsynth4_ObjectIdentity = ObjectIdentity
pm124feCtrlsynth4 = _Pm124feCtrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 1, 4)
)
_Pm124feCtrlCorrelatOn_Type = EkiOnOff
_Pm124feCtrlCorrelatOn_Object = MibScalar
pm124feCtrlCorrelatOn = _Pm124feCtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 1, 4, 1),
    _Pm124feCtrlCorrelatOn_Type()
)
pm124feCtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124feCtrlCorrelatOn.setStatus("current")
_Pm124feCtrlCorrelatOff_Type = EkiOnOff
_Pm124feCtrlCorrelatOff_Object = MibScalar
pm124feCtrlCorrelatOff = _Pm124feCtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 1, 4, 2),
    _Pm124feCtrlCorrelatOff_Type()
)
pm124feCtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124feCtrlCorrelatOff.setStatus("current")
_Pm124feCtrlswMgnt_ObjectIdentity = ObjectIdentity
pm124feCtrlswMgnt = _Pm124feCtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 1, 5)
)
_Pm124feCtrlColdReset_Type = EkiOnOff
_Pm124feCtrlColdReset_Object = MibScalar
pm124feCtrlColdReset = _Pm124feCtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 1, 5, 2),
    _Pm124feCtrlColdReset_Type()
)
pm124feCtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124feCtrlColdReset.setStatus("current")
_Pm124feCtrlWarmReset_Type = EkiOnOff
_Pm124feCtrlWarmReset_Object = MibScalar
pm124feCtrlWarmReset = _Pm124feCtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 1, 5, 3),
    _Pm124feCtrlWarmReset_Type()
)
pm124feCtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124feCtrlWarmReset.setStatus("current")
_Pm124feCtrlledTest_ObjectIdentity = ObjectIdentity
pm124feCtrlledTest = _Pm124feCtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 1, 72)
)
_Pm124feCtrlGreenLed_Type = EkiOnOff
_Pm124feCtrlGreenLed_Object = MibScalar
pm124feCtrlGreenLed = _Pm124feCtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 1, 72, 1),
    _Pm124feCtrlGreenLed_Type()
)
pm124feCtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124feCtrlGreenLed.setStatus("current")
_Pm124feCtrlRedLed_Type = EkiOnOff
_Pm124feCtrlRedLed_Object = MibScalar
pm124feCtrlRedLed = _Pm124feCtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 1, 72, 2),
    _Pm124feCtrlRedLed_Type()
)
pm124feCtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124feCtrlRedLed.setStatus("current")
_Pm124feCtrlLedOff_Type = EkiOnOff
_Pm124feCtrlLedOff_Object = MibScalar
pm124feCtrlLedOff = _Pm124feCtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 1, 72, 3),
    _Pm124feCtrlLedOff_Type()
)
pm124feCtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124feCtrlLedOff.setStatus("current")
_Pm124feCtrlmoduleOosMode_ObjectIdentity = ObjectIdentity
pm124feCtrlmoduleOosMode = _Pm124feCtrlmoduleOosMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 1, 73)
)
_Pm124feCtrlModuleOosMode_Type = EkiOnOff
_Pm124feCtrlModuleOosMode_Object = MibScalar
pm124feCtrlModuleOosMode = _Pm124feCtrlModuleOosMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 1, 73, 1),
    _Pm124feCtrlModuleOosMode_Type()
)
pm124feCtrlModuleOosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124feCtrlModuleOosMode.setStatus("current")
_Pm124feCtrlClient_ObjectIdentity = ObjectIdentity
pm124feCtrlClient = _Pm124feCtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 2)
)
_Pm124feCtrlclientSfpOnoffTable_Object = MibTable
pm124feCtrlclientSfpOnoffTable = _Pm124feCtrlclientSfpOnoffTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 2, 16)
)
if mibBuilder.loadTexts:
    pm124feCtrlclientSfpOnoffTable.setStatus("current")
_Pm124feCtrlclientSfpOnoffEntry_Object = MibTableRow
pm124feCtrlclientSfpOnoffEntry = _Pm124feCtrlclientSfpOnoffEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 2, 16, 1)
)
pm124feCtrlclientSfpOnoffEntry.setIndexNames(
    (0, "EKINOPS-Pm124fe-MIB", "pm124feCtrlclientSfpOnoffIndex"),
)
if mibBuilder.loadTexts:
    pm124feCtrlclientSfpOnoffEntry.setStatus("current")


class _Pm124feCtrlclientSfpOnoffIndex_Type(Integer32):
    """Custom type pm124feCtrlclientSfpOnoffIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124feCtrlclientSfpOnoffIndex_Type.__name__ = "Integer32"
_Pm124feCtrlclientSfpOnoffIndex_Object = MibTableColumn
pm124feCtrlclientSfpOnoffIndex = _Pm124feCtrlclientSfpOnoffIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 2, 16, 1, 1),
    _Pm124feCtrlclientSfpOnoffIndex_Type()
)
pm124feCtrlclientSfpOnoffIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feCtrlclientSfpOnoffIndex.setStatus("current")
_Pm124feCtrlclientSfpOnoffPortn_Type = EkiState
_Pm124feCtrlclientSfpOnoffPortn_Object = MibTableColumn
pm124feCtrlclientSfpOnoffPortn = _Pm124feCtrlclientSfpOnoffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 2, 16, 1, 2),
    _Pm124feCtrlclientSfpOnoffPortn_Type()
)
pm124feCtrlclientSfpOnoffPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124feCtrlclientSfpOnoffPortn.setStatus("current")
_Pm124feCtrlclientLoopTable_Object = MibTable
pm124feCtrlclientLoopTable = _Pm124feCtrlclientLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 2, 17)
)
if mibBuilder.loadTexts:
    pm124feCtrlclientLoopTable.setStatus("current")
_Pm124feCtrlclientLoopEntry_Object = MibTableRow
pm124feCtrlclientLoopEntry = _Pm124feCtrlclientLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 2, 17, 1)
)
pm124feCtrlclientLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm124fe-MIB", "pm124feCtrlclientLoopIndex"),
)
if mibBuilder.loadTexts:
    pm124feCtrlclientLoopEntry.setStatus("current")


class _Pm124feCtrlclientLoopIndex_Type(Integer32):
    """Custom type pm124feCtrlclientLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124feCtrlclientLoopIndex_Type.__name__ = "Integer32"
_Pm124feCtrlclientLoopIndex_Object = MibTableColumn
pm124feCtrlclientLoopIndex = _Pm124feCtrlclientLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 2, 17, 1, 1),
    _Pm124feCtrlclientLoopIndex_Type()
)
pm124feCtrlclientLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feCtrlclientLoopIndex.setStatus("current")
_Pm124feCtrlclientLoopPortn_Type = EkiState
_Pm124feCtrlclientLoopPortn_Object = MibTableColumn
pm124feCtrlclientLoopPortn = _Pm124feCtrlclientLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 2, 17, 1, 2),
    _Pm124feCtrlclientLoopPortn_Type()
)
pm124feCtrlclientLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124feCtrlclientLoopPortn.setStatus("current")
_Pm124feCtrlclientCsfUpInsertTable_Object = MibTable
pm124feCtrlclientCsfUpInsertTable = _Pm124feCtrlclientCsfUpInsertTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 2, 18)
)
if mibBuilder.loadTexts:
    pm124feCtrlclientCsfUpInsertTable.setStatus("current")
_Pm124feCtrlclientCsfUpInsertEntry_Object = MibTableRow
pm124feCtrlclientCsfUpInsertEntry = _Pm124feCtrlclientCsfUpInsertEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 2, 18, 1)
)
pm124feCtrlclientCsfUpInsertEntry.setIndexNames(
    (0, "EKINOPS-Pm124fe-MIB", "pm124feCtrlclientCsfUpInsertIndex"),
)
if mibBuilder.loadTexts:
    pm124feCtrlclientCsfUpInsertEntry.setStatus("current")


class _Pm124feCtrlclientCsfUpInsertIndex_Type(Integer32):
    """Custom type pm124feCtrlclientCsfUpInsertIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124feCtrlclientCsfUpInsertIndex_Type.__name__ = "Integer32"
_Pm124feCtrlclientCsfUpInsertIndex_Object = MibTableColumn
pm124feCtrlclientCsfUpInsertIndex = _Pm124feCtrlclientCsfUpInsertIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 2, 18, 1, 1),
    _Pm124feCtrlclientCsfUpInsertIndex_Type()
)
pm124feCtrlclientCsfUpInsertIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feCtrlclientCsfUpInsertIndex.setStatus("current")
_Pm124feCtrlclientCsfUpInsertPortn_Type = EkiState
_Pm124feCtrlclientCsfUpInsertPortn_Object = MibTableColumn
pm124feCtrlclientCsfUpInsertPortn = _Pm124feCtrlclientCsfUpInsertPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 2, 18, 1, 2),
    _Pm124feCtrlclientCsfUpInsertPortn_Type()
)
pm124feCtrlclientCsfUpInsertPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124feCtrlclientCsfUpInsertPortn.setStatus("current")
_Pm124feCtrlclientCaisDwInsertTable_Object = MibTable
pm124feCtrlclientCaisDwInsertTable = _Pm124feCtrlclientCaisDwInsertTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 2, 19)
)
if mibBuilder.loadTexts:
    pm124feCtrlclientCaisDwInsertTable.setStatus("current")
_Pm124feCtrlclientCaisDwInsertEntry_Object = MibTableRow
pm124feCtrlclientCaisDwInsertEntry = _Pm124feCtrlclientCaisDwInsertEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 2, 19, 1)
)
pm124feCtrlclientCaisDwInsertEntry.setIndexNames(
    (0, "EKINOPS-Pm124fe-MIB", "pm124feCtrlclientCaisDwInsertIndex"),
)
if mibBuilder.loadTexts:
    pm124feCtrlclientCaisDwInsertEntry.setStatus("current")


class _Pm124feCtrlclientCaisDwInsertIndex_Type(Integer32):
    """Custom type pm124feCtrlclientCaisDwInsertIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124feCtrlclientCaisDwInsertIndex_Type.__name__ = "Integer32"
_Pm124feCtrlclientCaisDwInsertIndex_Object = MibTableColumn
pm124feCtrlclientCaisDwInsertIndex = _Pm124feCtrlclientCaisDwInsertIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 2, 19, 1, 1),
    _Pm124feCtrlclientCaisDwInsertIndex_Type()
)
pm124feCtrlclientCaisDwInsertIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feCtrlclientCaisDwInsertIndex.setStatus("current")
_Pm124feCtrlclientCaisDwInsertPortn_Type = EkiState
_Pm124feCtrlclientCaisDwInsertPortn_Object = MibTableColumn
pm124feCtrlclientCaisDwInsertPortn = _Pm124feCtrlclientCaisDwInsertPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 2, 19, 1, 2),
    _Pm124feCtrlclientCaisDwInsertPortn_Type()
)
pm124feCtrlclientCaisDwInsertPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124feCtrlclientCaisDwInsertPortn.setStatus("current")
_Pm124feCtrlclientOosModeTable_Object = MibTable
pm124feCtrlclientOosModeTable = _Pm124feCtrlclientOosModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 2, 20)
)
if mibBuilder.loadTexts:
    pm124feCtrlclientOosModeTable.setStatus("current")
_Pm124feCtrlclientOosModeEntry_Object = MibTableRow
pm124feCtrlclientOosModeEntry = _Pm124feCtrlclientOosModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 2, 20, 1)
)
pm124feCtrlclientOosModeEntry.setIndexNames(
    (0, "EKINOPS-Pm124fe-MIB", "pm124feCtrlclientOosModeIndex"),
)
if mibBuilder.loadTexts:
    pm124feCtrlclientOosModeEntry.setStatus("current")


class _Pm124feCtrlclientOosModeIndex_Type(Integer32):
    """Custom type pm124feCtrlclientOosModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124feCtrlclientOosModeIndex_Type.__name__ = "Integer32"
_Pm124feCtrlclientOosModeIndex_Object = MibTableColumn
pm124feCtrlclientOosModeIndex = _Pm124feCtrlclientOosModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 2, 20, 1, 1),
    _Pm124feCtrlclientOosModeIndex_Type()
)
pm124feCtrlclientOosModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feCtrlclientOosModeIndex.setStatus("current")
_Pm124feCtrlclientOosModePortn_Type = EkiState
_Pm124feCtrlclientOosModePortn_Object = MibTableColumn
pm124feCtrlclientOosModePortn = _Pm124feCtrlclientOosModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 2, 20, 1, 2),
    _Pm124feCtrlclientOosModePortn_Type()
)
pm124feCtrlclientOosModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124feCtrlclientOosModePortn.setStatus("current")
_Pm124feCtrlLine_ObjectIdentity = ObjectIdentity
pm124feCtrlLine = _Pm124feCtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 3)
)
_Pm124feCtrllineSfpOnoffTable_Object = MibTable
pm124feCtrllineSfpOnoffTable = _Pm124feCtrllineSfpOnoffTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 3, 64)
)
if mibBuilder.loadTexts:
    pm124feCtrllineSfpOnoffTable.setStatus("current")
_Pm124feCtrllineSfpOnoffEntry_Object = MibTableRow
pm124feCtrllineSfpOnoffEntry = _Pm124feCtrllineSfpOnoffEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 3, 64, 1)
)
pm124feCtrllineSfpOnoffEntry.setIndexNames(
    (0, "EKINOPS-Pm124fe-MIB", "pm124feCtrllineSfpOnoffIndex"),
)
if mibBuilder.loadTexts:
    pm124feCtrllineSfpOnoffEntry.setStatus("current")


class _Pm124feCtrllineSfpOnoffIndex_Type(Integer32):
    """Custom type pm124feCtrllineSfpOnoffIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124feCtrllineSfpOnoffIndex_Type.__name__ = "Integer32"
_Pm124feCtrllineSfpOnoffIndex_Object = MibTableColumn
pm124feCtrllineSfpOnoffIndex = _Pm124feCtrllineSfpOnoffIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 3, 64, 1, 1),
    _Pm124feCtrllineSfpOnoffIndex_Type()
)
pm124feCtrllineSfpOnoffIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feCtrllineSfpOnoffIndex.setStatus("current")
_Pm124feCtrllineSfpOnoffPortn_Type = EkiState
_Pm124feCtrllineSfpOnoffPortn_Object = MibTableColumn
pm124feCtrllineSfpOnoffPortn = _Pm124feCtrllineSfpOnoffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 3, 64, 1, 2),
    _Pm124feCtrllineSfpOnoffPortn_Type()
)
pm124feCtrllineSfpOnoffPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124feCtrllineSfpOnoffPortn.setStatus("current")
_Pm124feCtrllineOosModeTable_Object = MibTable
pm124feCtrllineOosModeTable = _Pm124feCtrllineOosModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 3, 65)
)
if mibBuilder.loadTexts:
    pm124feCtrllineOosModeTable.setStatus("current")
_Pm124feCtrllineOosModeEntry_Object = MibTableRow
pm124feCtrllineOosModeEntry = _Pm124feCtrllineOosModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 3, 65, 1)
)
pm124feCtrllineOosModeEntry.setIndexNames(
    (0, "EKINOPS-Pm124fe-MIB", "pm124feCtrllineOosModeIndex"),
)
if mibBuilder.loadTexts:
    pm124feCtrllineOosModeEntry.setStatus("current")


class _Pm124feCtrllineOosModeIndex_Type(Integer32):
    """Custom type pm124feCtrllineOosModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124feCtrllineOosModeIndex_Type.__name__ = "Integer32"
_Pm124feCtrllineOosModeIndex_Object = MibTableColumn
pm124feCtrllineOosModeIndex = _Pm124feCtrllineOosModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 3, 65, 1, 1),
    _Pm124feCtrllineOosModeIndex_Type()
)
pm124feCtrllineOosModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feCtrllineOosModeIndex.setStatus("current")
_Pm124feCtrllineOosModePortn_Type = EkiState
_Pm124feCtrllineOosModePortn_Object = MibTableColumn
pm124feCtrllineOosModePortn = _Pm124feCtrllineOosModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 3, 65, 1, 2),
    _Pm124feCtrllineOosModePortn_Type()
)
pm124feCtrllineOosModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124feCtrllineOosModePortn.setStatus("current")
_Pm124feCtrllineLoopTable_Object = MibTable
pm124feCtrllineLoopTable = _Pm124feCtrllineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 3, 66)
)
if mibBuilder.loadTexts:
    pm124feCtrllineLoopTable.setStatus("current")
_Pm124feCtrllineLoopEntry_Object = MibTableRow
pm124feCtrllineLoopEntry = _Pm124feCtrllineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 3, 66, 1)
)
pm124feCtrllineLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm124fe-MIB", "pm124feCtrllineLoopIndex"),
)
if mibBuilder.loadTexts:
    pm124feCtrllineLoopEntry.setStatus("current")


class _Pm124feCtrllineLoopIndex_Type(Integer32):
    """Custom type pm124feCtrllineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124feCtrllineLoopIndex_Type.__name__ = "Integer32"
_Pm124feCtrllineLoopIndex_Object = MibTableColumn
pm124feCtrllineLoopIndex = _Pm124feCtrllineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 3, 66, 1, 1),
    _Pm124feCtrllineLoopIndex_Type()
)
pm124feCtrllineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feCtrllineLoopIndex.setStatus("current")
_Pm124feCtrllineLoopPortn_Type = EkiState
_Pm124feCtrllineLoopPortn_Object = MibTableColumn
pm124feCtrllineLoopPortn = _Pm124feCtrllineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 6, 3, 66, 1, 2),
    _Pm124feCtrllineLoopPortn_Type()
)
pm124feCtrllineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124feCtrllineLoopPortn.setStatus("current")
_Pm124feri_ObjectIdentity = ObjectIdentity
pm124feri = _Pm124feri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 7)
)
_Pm124feriTable_ObjectIdentity = ObjectIdentity
pm124feriTable = _Pm124feriTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 7, 1)
)
_Pm124feRinvClientTable_Object = MibTable
pm124feRinvClientTable = _Pm124feRinvClientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 7, 1, 1)
)
if mibBuilder.loadTexts:
    pm124feRinvClientTable.setStatus("current")
_Pm124feRinvClientEntry_Object = MibTableRow
pm124feRinvClientEntry = _Pm124feRinvClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 7, 1, 1, 1)
)
pm124feRinvClientEntry.setIndexNames(
    (0, "EKINOPS-Pm124fe-MIB", "pm124feRinvClientIndex"),
)
if mibBuilder.loadTexts:
    pm124feRinvClientEntry.setStatus("current")


class _Pm124feRinvClientIndex_Type(Integer32):
    """Custom type pm124feRinvClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm124feRinvClientIndex_Type.__name__ = "Integer32"
_Pm124feRinvClientIndex_Object = MibTableColumn
pm124feRinvClientIndex = _Pm124feRinvClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 7, 1, 1, 1, 1),
    _Pm124feRinvClientIndex_Type()
)
pm124feRinvClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feRinvClientIndex.setStatus("current")
_Pm124feRinvSfpClient_Type = DisplayString
_Pm124feRinvSfpClient_Object = MibTableColumn
pm124feRinvSfpClient = _Pm124feRinvSfpClient_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 7, 1, 1, 1, 2),
    _Pm124feRinvSfpClient_Type()
)
pm124feRinvSfpClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feRinvSfpClient.setStatus("current")
_Pm124feRinvLineTable_Object = MibTable
pm124feRinvLineTable = _Pm124feRinvLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pm124feRinvLineTable.setStatus("current")
_Pm124feRinvLineEntry_Object = MibTableRow
pm124feRinvLineEntry = _Pm124feRinvLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 7, 1, 2, 1)
)
pm124feRinvLineEntry.setIndexNames(
    (0, "EKINOPS-Pm124fe-MIB", "pm124feRinvLineIndex"),
)
if mibBuilder.loadTexts:
    pm124feRinvLineEntry.setStatus("current")


class _Pm124feRinvLineIndex_Type(Integer32):
    """Custom type pm124feRinvLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm124feRinvLineIndex_Type.__name__ = "Integer32"
_Pm124feRinvLineIndex_Object = MibTableColumn
pm124feRinvLineIndex = _Pm124feRinvLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 7, 1, 2, 1, 1),
    _Pm124feRinvLineIndex_Type()
)
pm124feRinvLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feRinvLineIndex.setStatus("current")
_Pm124feRinvsfpLine_Type = DisplayString
_Pm124feRinvsfpLine_Object = MibTableColumn
pm124feRinvsfpLine = _Pm124feRinvsfpLine_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 7, 1, 2, 1, 2),
    _Pm124feRinvsfpLine_Type()
)
pm124feRinvsfpLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feRinvsfpLine.setStatus("current")
_Pm124feRinvReloadInventory_Type = EkiOnOff
_Pm124feRinvReloadInventory_Object = MibScalar
pm124feRinvReloadInventory = _Pm124feRinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 7, 2),
    _Pm124feRinvReloadInventory_Type()
)
pm124feRinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124feRinvReloadInventory.setStatus("current")
_Pm124feRinvHwPlatform_Type = DisplayString
_Pm124feRinvHwPlatform_Object = MibScalar
pm124feRinvHwPlatform = _Pm124feRinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 7, 3),
    _Pm124feRinvHwPlatform_Type()
)
pm124feRinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feRinvHwPlatform.setStatus("current")
_Pm124feRinvModulePlatform_Type = DisplayString
_Pm124feRinvModulePlatform_Object = MibScalar
pm124feRinvModulePlatform = _Pm124feRinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 7, 4),
    _Pm124feRinvModulePlatform_Type()
)
pm124feRinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feRinvModulePlatform.setStatus("current")
_Pm124feRinvSwPlatform_Type = DisplayString
_Pm124feRinvSwPlatform_Object = MibScalar
pm124feRinvSwPlatform = _Pm124feRinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 7, 5),
    _Pm124feRinvSwPlatform_Type()
)
pm124feRinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feRinvSwPlatform.setStatus("current")
_Pm124feRinvGwPlatform_Type = DisplayString
_Pm124feRinvGwPlatform_Object = MibScalar
pm124feRinvGwPlatform = _Pm124feRinvGwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 7, 6),
    _Pm124feRinvGwPlatform_Type()
)
pm124feRinvGwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feRinvGwPlatform.setStatus("current")
_Pm124feConfig_ObjectIdentity = ObjectIdentity
pm124feConfig = _Pm124feConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 9)
)
_Pm124feCfgLsd_ObjectIdentity = ObjectIdentity
pm124feCfgLsd = _Pm124feCfgLsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 9, 1)
)
_Pm124feCfgClientLsdTable_Object = MibTable
pm124feCfgClientLsdTable = _Pm124feCfgClientLsdTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 9, 1, 1)
)
if mibBuilder.loadTexts:
    pm124feCfgClientLsdTable.setStatus("current")
_Pm124feCfgClientLsdEntry_Object = MibTableRow
pm124feCfgClientLsdEntry = _Pm124feCfgClientLsdEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 9, 1, 1, 1)
)
pm124feCfgClientLsdEntry.setIndexNames(
    (0, "EKINOPS-Pm124fe-MIB", "pm124feCfgClientLsdIndex"),
)
if mibBuilder.loadTexts:
    pm124feCfgClientLsdEntry.setStatus("current")


class _Pm124feCfgClientLsdIndex_Type(Integer32):
    """Custom type pm124feCfgClientLsdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124feCfgClientLsdIndex_Type.__name__ = "Integer32"
_Pm124feCfgClientLsdIndex_Object = MibTableColumn
pm124feCfgClientLsdIndex = _Pm124feCfgClientLsdIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 9, 1, 1, 1, 1),
    _Pm124feCfgClientLsdIndex_Type()
)
pm124feCfgClientLsdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feCfgClientLsdIndex.setStatus("current")


class _Pm124feCfgClientLsdModePortn_Type(Unsigned32):
    """Custom type pm124feCfgClientLsdModePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm124feCfgClientLsdModePortn_Type.__name__ = "Unsigned32"
_Pm124feCfgClientLsdModePortn_Object = MibTableColumn
pm124feCfgClientLsdModePortn = _Pm124feCfgClientLsdModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 9, 1, 1, 1, 3),
    _Pm124feCfgClientLsdModePortn_Type()
)
pm124feCfgClientLsdModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124feCfgClientLsdModePortn.setStatus("current")


class _Pm124feCfgClientAccessioCtrbInsPortn_Type(Unsigned32):
    """Custom type pm124feCfgClientAccessioCtrbInsPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm124feCfgClientAccessioCtrbInsPortn_Type.__name__ = "Unsigned32"
_Pm124feCfgClientAccessioCtrbInsPortn_Object = MibTableColumn
pm124feCfgClientAccessioCtrbInsPortn = _Pm124feCfgClientAccessioCtrbInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 9, 1, 1, 1, 4),
    _Pm124feCfgClientAccessioCtrbInsPortn_Type()
)
pm124feCfgClientAccessioCtrbInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124feCfgClientAccessioCtrbInsPortn.setStatus("current")


class _Pm124feCfgClientAccCtrbInsPortn_Type(Unsigned32):
    """Custom type pm124feCfgClientAccCtrbInsPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm124feCfgClientAccCtrbInsPortn_Type.__name__ = "Unsigned32"
_Pm124feCfgClientAccCtrbInsPortn_Object = MibTableColumn
pm124feCfgClientAccCtrbInsPortn = _Pm124feCfgClientAccCtrbInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 9, 1, 1, 1, 5),
    _Pm124feCfgClientAccCtrbInsPortn_Type()
)
pm124feCfgClientAccCtrbInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124feCfgClientAccCtrbInsPortn.setStatus("current")


class _Pm124feCfgLineAccessioCtrbInsPortn_Type(Unsigned32):
    """Custom type pm124feCfgLineAccessioCtrbInsPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm124feCfgLineAccessioCtrbInsPortn_Type.__name__ = "Unsigned32"
_Pm124feCfgLineAccessioCtrbInsPortn_Object = MibTableColumn
pm124feCfgLineAccessioCtrbInsPortn = _Pm124feCfgLineAccessioCtrbInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 9, 1, 1, 1, 6),
    _Pm124feCfgLineAccessioCtrbInsPortn_Type()
)
pm124feCfgLineAccessioCtrbInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124feCfgLineAccessioCtrbInsPortn.setStatus("current")


class _Pm124feCfgClientAccCtrbActPortn_Type(Unsigned32):
    """Custom type pm124feCfgClientAccCtrbActPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm124feCfgClientAccCtrbActPortn_Type.__name__ = "Unsigned32"
_Pm124feCfgClientAccCtrbActPortn_Object = MibTableColumn
pm124feCfgClientAccCtrbActPortn = _Pm124feCfgClientAccCtrbActPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 9, 1, 1, 1, 8),
    _Pm124feCfgClientAccCtrbActPortn_Type()
)
pm124feCfgClientAccCtrbActPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124feCfgClientAccCtrbActPortn.setStatus("current")


class _Pm124feCfgLineAccessioCtrbActPortn_Type(Unsigned32):
    """Custom type pm124feCfgLineAccessioCtrbActPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm124feCfgLineAccessioCtrbActPortn_Type.__name__ = "Unsigned32"
_Pm124feCfgLineAccessioCtrbActPortn_Object = MibTableColumn
pm124feCfgLineAccessioCtrbActPortn = _Pm124feCfgLineAccessioCtrbActPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 9, 1, 1, 1, 9),
    _Pm124feCfgLineAccessioCtrbActPortn_Type()
)
pm124feCfgLineAccessioCtrbActPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124feCfgLineAccessioCtrbActPortn.setStatus("current")
_Pm124feCfgStartUp_ObjectIdentity = ObjectIdentity
pm124feCfgStartUp = _Pm124feCfgStartUp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 9, 2)
)
_Pm124feCfgClientStartupTable_Object = MibTable
pm124feCfgClientStartupTable = _Pm124feCfgClientStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 9, 2, 1)
)
if mibBuilder.loadTexts:
    pm124feCfgClientStartupTable.setStatus("current")
_Pm124feCfgClientStartupEntry_Object = MibTableRow
pm124feCfgClientStartupEntry = _Pm124feCfgClientStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 9, 2, 1, 1)
)
pm124feCfgClientStartupEntry.setIndexNames(
    (0, "EKINOPS-Pm124fe-MIB", "pm124feCfgClientStartupIndex"),
)
if mibBuilder.loadTexts:
    pm124feCfgClientStartupEntry.setStatus("current")


class _Pm124feCfgClientStartupIndex_Type(Integer32):
    """Custom type pm124feCfgClientStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124feCfgClientStartupIndex_Type.__name__ = "Integer32"
_Pm124feCfgClientStartupIndex_Object = MibTableColumn
pm124feCfgClientStartupIndex = _Pm124feCfgClientStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 9, 2, 1, 1, 1),
    _Pm124feCfgClientStartupIndex_Type()
)
pm124feCfgClientStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feCfgClientStartupIndex.setStatus("current")


class _Pm124feCfgClientTrscvCtrlPortn_Type(Unsigned32):
    """Custom type pm124feCfgClientTrscvCtrlPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm124feCfgClientTrscvCtrlPortn_Type.__name__ = "Unsigned32"
_Pm124feCfgClientTrscvCtrlPortn_Object = MibTableColumn
pm124feCfgClientTrscvCtrlPortn = _Pm124feCfgClientTrscvCtrlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 9, 2, 1, 1, 3),
    _Pm124feCfgClientTrscvCtrlPortn_Type()
)
pm124feCfgClientTrscvCtrlPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124feCfgClientTrscvCtrlPortn.setStatus("current")


class _Pm124feCfgClientOosModePortn_Type(Unsigned32):
    """Custom type pm124feCfgClientOosModePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm124feCfgClientOosModePortn_Type.__name__ = "Unsigned32"
_Pm124feCfgClientOosModePortn_Object = MibTableColumn
pm124feCfgClientOosModePortn = _Pm124feCfgClientOosModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 9, 2, 1, 1, 5),
    _Pm124feCfgClientOosModePortn_Type()
)
pm124feCfgClientOosModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124feCfgClientOosModePortn.setStatus("current")
_Pm124fetablelineStartup_ObjectIdentity = ObjectIdentity
pm124fetablelineStartup = _Pm124fetablelineStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 9, 2, 2)
)


class _Pm124feCfglineTrscvCtrl_Type(Unsigned32):
    """Custom type pm124feCfglineTrscvCtrl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm124feCfglineTrscvCtrl_Type.__name__ = "Unsigned32"
_Pm124feCfglineTrscvCtrl_Object = MibScalar
pm124feCfglineTrscvCtrl = _Pm124feCfglineTrscvCtrl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 9, 2, 2, 2),
    _Pm124feCfglineTrscvCtrl_Type()
)
pm124feCfglineTrscvCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124feCfglineTrscvCtrl.setStatus("current")


class _Pm124feCfglineOosMode_Type(Unsigned32):
    """Custom type pm124feCfglineOosMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm124feCfglineOosMode_Type.__name__ = "Unsigned32"
_Pm124feCfglineOosMode_Object = MibScalar
pm124feCfglineOosMode = _Pm124feCfglineOosMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 9, 2, 2, 3),
    _Pm124feCfglineOosMode_Type()
)
pm124feCfglineOosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124feCfglineOosMode.setStatus("current")
_Pm124feCfgLabels_ObjectIdentity = ObjectIdentity
pm124feCfgLabels = _Pm124feCfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 9, 3)
)
_Pm124feCfgLabelclientTable_Object = MibTable
pm124feCfgLabelclientTable = _Pm124feCfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 9, 3, 1)
)
if mibBuilder.loadTexts:
    pm124feCfgLabelclientTable.setStatus("current")
_Pm124feCfgLabelclientEntry_Object = MibTableRow
pm124feCfgLabelclientEntry = _Pm124feCfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 9, 3, 1, 1)
)
pm124feCfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-Pm124fe-MIB", "pm124feCfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pm124feCfgLabelclientEntry.setStatus("current")


class _Pm124feCfgLabelclientIndex_Type(Integer32):
    """Custom type pm124feCfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124feCfgLabelclientIndex_Type.__name__ = "Integer32"
_Pm124feCfgLabelclientIndex_Object = MibTableColumn
pm124feCfgLabelclientIndex = _Pm124feCfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 9, 3, 1, 1, 1),
    _Pm124feCfgLabelclientIndex_Type()
)
pm124feCfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feCfgLabelclientIndex.setStatus("current")


class _Pm124feCfgLabelclientPortn_Type(DisplayString):
    """Custom type pm124feCfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm124feCfgLabelclientPortn_Type.__name__ = "DisplayString"
_Pm124feCfgLabelclientPortn_Object = MibTableColumn
pm124feCfgLabelclientPortn = _Pm124feCfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 9, 3, 1, 1, 3),
    _Pm124feCfgLabelclientPortn_Type()
)
pm124feCfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124feCfgLabelclientPortn.setStatus("current")
_Pm124feCfgLabellineTable_Object = MibTable
pm124feCfgLabellineTable = _Pm124feCfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 9, 3, 2)
)
if mibBuilder.loadTexts:
    pm124feCfgLabellineTable.setStatus("current")
_Pm124feCfgLabellineEntry_Object = MibTableRow
pm124feCfgLabellineEntry = _Pm124feCfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 9, 3, 2, 1)
)
pm124feCfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-Pm124fe-MIB", "pm124feCfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pm124feCfgLabellineEntry.setStatus("current")


class _Pm124feCfgLabellineIndex_Type(Integer32):
    """Custom type pm124feCfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124feCfgLabellineIndex_Type.__name__ = "Integer32"
_Pm124feCfgLabellineIndex_Object = MibTableColumn
pm124feCfgLabellineIndex = _Pm124feCfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 9, 3, 2, 1, 1),
    _Pm124feCfgLabellineIndex_Type()
)
pm124feCfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124feCfgLabellineIndex.setStatus("current")


class _Pm124feCfgLabellinePortn_Type(DisplayString):
    """Custom type pm124feCfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm124feCfgLabellinePortn_Type.__name__ = "DisplayString"
_Pm124feCfgLabellinePortn_Object = MibTableColumn
pm124feCfgLabellinePortn = _Pm124feCfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 9, 3, 2, 1, 3),
    _Pm124feCfgLabellinePortn_Type()
)
pm124feCfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124feCfgLabellinePortn.setStatus("current")
_Pm124feCfgWriteConfiguration_Type = EkiOnOff
_Pm124feCfgWriteConfiguration_Object = MibScalar
pm124feCfgWriteConfiguration = _Pm124feCfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 9, 257),
    _Pm124feCfgWriteConfiguration_Type()
)
pm124feCfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124feCfgWriteConfiguration.setStatus("current")
_Pm124fetraps_ObjectIdentity = ObjectIdentity
pm124fetraps = _Pm124fetraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 44, 10)
)


class _Pm124fetrapPortNumber_Type(Integer32):
    """Custom type pm124fetrapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm124fetrapPortNumber_Type.__name__ = "Integer32"
_Pm124fetrapPortNumber_Object = MibScalar
pm124fetrapPortNumber = _Pm124fetrapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 10, 2),
    _Pm124fetrapPortNumber_Type()
)
pm124fetrapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124fetrapPortNumber.setStatus("current")


class _Pm124fetrapLineNumber_Type(Integer32):
    """Custom type pm124fetrapLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm124fetrapLineNumber_Type.__name__ = "Integer32"
_Pm124fetrapLineNumber_Object = MibScalar
pm124fetrapLineNumber = _Pm124fetrapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 10, 3),
    _Pm124fetrapLineNumber_Type()
)
pm124fetrapLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124fetrapLineNumber.setStatus("current")


class _Pm124fetrapBoardNumber_Type(Integer32):
    """Custom type pm124fetrapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm124fetrapBoardNumber_Type.__name__ = "Integer32"
_Pm124fetrapBoardNumber_Object = MibScalar
pm124fetrapBoardNumber = _Pm124fetrapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 44, 10, 4),
    _Pm124fetrapBoardNumber_Type()
)
pm124fetrapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124fetrapBoardNumber.setStatus("current")

# Managed Objects groups


# Notification objects

pm124feLineTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 44, 10, 30)
)
pm124feLineTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm124fe-MIB", "pm124feAlmLineDdmWarningPortn"),
        ("EKINOPS-Pm124fe-MIB", "pm124fetrapLineNumber"),
        ("EKINOPS-Pm124fe-MIB", "pm124fetrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm124feLineTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm124feLineTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 44, 10, 31)
)
pm124feLineTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm124fe-MIB", "pm124feAlmLineDdmWarningPortn"),
        ("EKINOPS-Pm124fe-MIB", "pm124fetrapLineNumber"),
        ("EKINOPS-Pm124fe-MIB", "pm124fetrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm124feLineTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm124feLineTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 44, 10, 32)
)
pm124feLineTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm124fe-MIB", "pm124feAlmLineDdmAlmPortn"),
        ("EKINOPS-Pm124fe-MIB", "pm124fetrapLineNumber"),
        ("EKINOPS-Pm124fe-MIB", "pm124fetrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm124feLineTrapUrgentGoesOn.setStatus(
        "current"
    )

pm124feLineTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 44, 10, 33)
)
pm124feLineTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm124fe-MIB", "pm124feAlmLineDdmAlmPortn"),
        ("EKINOPS-Pm124fe-MIB", "pm124fetrapLineNumber"),
        ("EKINOPS-Pm124fe-MIB", "pm124fetrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm124feLineTrapUrgentGoesOff.setStatus(
        "current"
    )

pm124feLineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 44, 10, 34)
)
pm124feLineTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm124fe-MIB", "pm124feAlmLineFailPortn"),
        ("EKINOPS-Pm124fe-MIB", "pm124feAlmLineHwFailPortn"),
        ("EKINOPS-Pm124fe-MIB", "pm124fetrapLineNumber"),
        ("EKINOPS-Pm124fe-MIB", "pm124fetrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm124feLineTrapCritGoesOn.setStatus(
        "current"
    )

pm124feLineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 44, 10, 35)
)
pm124feLineTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm124fe-MIB", "pm124feAlmLineFailPortn"),
        ("EKINOPS-Pm124fe-MIB", "pm124feAlmLineHwFailPortn"),
        ("EKINOPS-Pm124fe-MIB", "pm124fetrapLineNumber"),
        ("EKINOPS-Pm124fe-MIB", "pm124fetrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm124feLineTrapCritGoesOff.setStatus(
        "current"
    )

pm124feClientTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 44, 10, 40)
)
pm124feClientTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm124fe-MIB", "pm124feAlmClientSfpDdmWarningPortn"),
        ("EKINOPS-Pm124fe-MIB", "pm124fetrapPortNumber"),
        ("EKINOPS-Pm124fe-MIB", "pm124fetrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm124feClientTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm124feClientTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 44, 10, 41)
)
pm124feClientTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm124fe-MIB", "pm124feAlmClientSfpDdmWarningPortn"),
        ("EKINOPS-Pm124fe-MIB", "pm124fetrapPortNumber"),
        ("EKINOPS-Pm124fe-MIB", "pm124fetrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm124feClientTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm124feClientTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 44, 10, 42)
)
pm124feClientTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm124fe-MIB", "pm124feAlmClientSfpDdmAlmPortn"),
        ("EKINOPS-Pm124fe-MIB", "pm124fetrapPortNumber"),
        ("EKINOPS-Pm124fe-MIB", "pm124fetrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm124feClientTrapUrgentGoesOn.setStatus(
        "current"
    )

pm124feClientTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 44, 10, 43)
)
pm124feClientTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm124fe-MIB", "pm124feAlmClientSfpDdmAlmPortn"),
        ("EKINOPS-Pm124fe-MIB", "pm124fetrapPortNumber"),
        ("EKINOPS-Pm124fe-MIB", "pm124fetrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm124feClientTrapUrgentGoesOff.setStatus(
        "current"
    )

pm124feClientTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 44, 10, 44)
)
pm124feClientTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm124fe-MIB", "pm124feAlmClientFailAccPortn"),
        ("EKINOPS-Pm124fe-MIB", "pm124feAlmClientHwFailAccPortn"),
        ("EKINOPS-Pm124fe-MIB", "pm124fetrapPortNumber"),
        ("EKINOPS-Pm124fe-MIB", "pm124fetrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm124feClientTrapCritGoesOn.setStatus(
        "current"
    )

pm124feClientTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 44, 10, 45)
)
pm124feClientTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm124fe-MIB", "pm124feAlmClientFailAccPortn"),
        ("EKINOPS-Pm124fe-MIB", "pm124feAlmClientHwFailAccPortn"),
        ("EKINOPS-Pm124fe-MIB", "pm124fetrapPortNumber"),
        ("EKINOPS-Pm124fe-MIB", "pm124fetrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm124feClientTrapCritGoesOff.setStatus(
        "current"
    )

pm124fePowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 44, 10, 50)
)
pm124fePowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm124fe-MIB", "pm124feAlmDefFuseB"),
        ("EKINOPS-Pm124fe-MIB", "pm124feAlmDefFuseA"),
        ("EKINOPS-Pm124fe-MIB", "pm124fetrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm124fePowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pm124fePowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 44, 10, 51)
)
pm124fePowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm124fe-MIB", "pm124feAlmDefFuseB"),
        ("EKINOPS-Pm124fe-MIB", "pm124feAlmDefFuseA"),
        ("EKINOPS-Pm124fe-MIB", "pm124fetrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm124fePowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Pm124fe-MIB",
    **{"modulePm124fe": modulePm124fe,
       "pm124fealarms": pm124fealarms,
       "pm124feAlmOther": pm124feAlmOther,
       "pm124feAlmOtherNurg": pm124feAlmOtherNurg,
       "pm124feAlmsynthAlm2": pm124feAlmsynthAlm2,
       "pm124feAlmConfTableSave": pm124feAlmConfTableSave,
       "pm124feAlmInvUpload": pm124feAlmInvUpload,
       "pm124feAlmConfTableLoad": pm124feAlmConfTableLoad,
       "pm124feAlmCorrelatOff": pm124feAlmCorrelatOff,
       "pm124feAlmOtherUrg": pm124feAlmOtherUrg,
       "pm124feAlmOtherCrit": pm124feAlmOtherCrit,
       "pm124feAlmsynthAlm0": pm124feAlmsynthAlm0,
       "pm124feAlmModuleGlobFailure": pm124feAlmModuleGlobFailure,
       "pm124feAlmDefFuseA": pm124feAlmDefFuseA,
       "pm124feAlmDefFuseB": pm124feAlmDefFuseB,
       "pm124feAlmClient": pm124feAlmClient,
       "pm124feAlmClientNurg": pm124feAlmClientNurg,
       "pm124feAlmclientSfpWarnDdmTable": pm124feAlmclientSfpWarnDdmTable,
       "pm124feAlmclientSfpWarnDdmEntry": pm124feAlmclientSfpWarnDdmEntry,
       "pm124feAlmclientSfpWarnDdmIndex": pm124feAlmclientSfpWarnDdmIndex,
       "pm124feAlmClientTxPwLowWngPortn": pm124feAlmClientTxPwLowWngPortn,
       "pm124feAlmClientTxPwrHighWngPortn": pm124feAlmClientTxPwrHighWngPortn,
       "pm124feAlmClientTxBiasLowWngPortn": pm124feAlmClientTxBiasLowWngPortn,
       "pm124feAlmClientTxBiasHighWngPortn": pm124feAlmClientTxBiasHighWngPortn,
       "pm124feAlmClientVccLowWngPortn": pm124feAlmClientVccLowWngPortn,
       "pm124feAlmClientVccHighWngPortn": pm124feAlmClientVccHighWngPortn,
       "pm124feAlmClientTempLowWngPortn": pm124feAlmClientTempLowWngPortn,
       "pm124feAlmClientTempHighWngPortn": pm124feAlmClientTempHighWngPortn,
       "pm124feAlmClientRxPwrLowWngPortn": pm124feAlmClientRxPwrLowWngPortn,
       "pm124feAlmClientRxPwrHighWngPortn": pm124feAlmClientRxPwrHighWngPortn,
       "pm124feAlmClientUrg": pm124feAlmClientUrg,
       "pm124feAlmclientSfpAlmDdmTable": pm124feAlmclientSfpAlmDdmTable,
       "pm124feAlmclientSfpAlmDdmEntry": pm124feAlmclientSfpAlmDdmEntry,
       "pm124feAlmclientSfpAlmDdmIndex": pm124feAlmclientSfpAlmDdmIndex,
       "pm124feAlmClientTxPwrLowAlaPortn": pm124feAlmClientTxPwrLowAlaPortn,
       "pm124feAlmClientClientTxPwrHighAlaPortn": pm124feAlmClientClientTxPwrHighAlaPortn,
       "pm124feAlmClientTxBiasLowAlaPortn": pm124feAlmClientTxBiasLowAlaPortn,
       "pm124feAlmClientTxBiasHighAlaPortn": pm124feAlmClientTxBiasHighAlaPortn,
       "pm124feAlmClientVccLowAlaPortn": pm124feAlmClientVccLowAlaPortn,
       "pm124feAlmClientVccHighAlaPortn": pm124feAlmClientVccHighAlaPortn,
       "pm124feAlmClientTempLowAlaPortn": pm124feAlmClientTempLowAlaPortn,
       "pm124feAlmClientTempHighAlaPortn": pm124feAlmClientTempHighAlaPortn,
       "pm124feAlmClientRxPwrLowAlaPortn": pm124feAlmClientRxPwrLowAlaPortn,
       "pm124feAlmClientRxPwrHighAlaPortn": pm124feAlmClientRxPwrHighAlaPortn,
       "pm124feAlmClientCrit": pm124feAlmClientCrit,
       "pm124feAlmsynthAlmPortTable": pm124feAlmsynthAlmPortTable,
       "pm124feAlmsynthAlmPortEntry": pm124feAlmsynthAlmPortEntry,
       "pm124feAlmsynthAlmPortIndex": pm124feAlmsynthAlmPortIndex,
       "pm124feAlmClientSfpAbsentPortn": pm124feAlmClientSfpAbsentPortn,
       "pm124feAlmClientDdmAbsentPortn": pm124feAlmClientDdmAbsentPortn,
       "pm124feAlmClientHwFailAccPortn": pm124feAlmClientHwFailAccPortn,
       "pm124feAlmClientLsdPortn": pm124feAlmClientLsdPortn,
       "pm124feAlmClientLocalOosPortn": pm124feAlmClientLocalOosPortn,
       "pm124feAlmClientRemoteOosPortn": pm124feAlmClientRemoteOosPortn,
       "pm124feAlmClientDwCaisPortn": pm124feAlmClientDwCaisPortn,
       "pm124feAlmClientSfpDdmWarningPortn": pm124feAlmClientSfpDdmWarningPortn,
       "pm124feAlmClientSfpDdmAlmPortn": pm124feAlmClientSfpDdmAlmPortn,
       "pm124feAlmClientFailAccPortn": pm124feAlmClientFailAccPortn,
       "pm124feAlmClientUpCsfPortn": pm124feAlmClientUpCsfPortn,
       "pm124feAlmclientAccessioAlmTable": pm124feAlmclientAccessioAlmTable,
       "pm124feAlmclientAccessioAlmEntry": pm124feAlmclientAccessioAlmEntry,
       "pm124feAlmclientAccessioAlmIndex": pm124feAlmclientAccessioAlmIndex,
       "pm124feAlmClientLasFailPortn": pm124feAlmClientLasFailPortn,
       "pm124feAlmClientLosPortn": pm124feAlmClientLosPortn,
       "pm124feAlmclientAccAlmTable": pm124feAlmclientAccAlmTable,
       "pm124feAlmclientAccAlmEntry": pm124feAlmclientAccAlmEntry,
       "pm124feAlmclientAccAlmIndex": pm124feAlmclientAccAlmIndex,
       "pm124feAlmClientOosPortn": pm124feAlmClientOosPortn,
       "pm124feAlmClientUpEsOvlPortn": pm124feAlmClientUpEsOvlPortn,
       "pm124feAlmClientCsfDetPortn": pm124feAlmClientCsfDetPortn,
       "pm124feAlmClientDwEsOvlPortn": pm124feAlmClientDwEsOvlPortn,
       "pm124feAlmLine": pm124feAlmLine,
       "pm124feAlmLineNurg": pm124feAlmLineNurg,
       "pm124feAlmlineSfpWarnDdmTable": pm124feAlmlineSfpWarnDdmTable,
       "pm124feAlmlineSfpWarnDdmEntry": pm124feAlmlineSfpWarnDdmEntry,
       "pm124feAlmlineSfpWarnDdmIndex": pm124feAlmlineSfpWarnDdmIndex,
       "pm124feAlmLineTxPwLowWngPortn": pm124feAlmLineTxPwLowWngPortn,
       "pm124feAlmLineTxPwrHighWngPortn": pm124feAlmLineTxPwrHighWngPortn,
       "pm124feAlmLineTxBiasLowWngPortn": pm124feAlmLineTxBiasLowWngPortn,
       "pm124feAlmLineTxBiasHighWngPortn": pm124feAlmLineTxBiasHighWngPortn,
       "pm124feAlmLineVccLowWngPortn": pm124feAlmLineVccLowWngPortn,
       "pm124feAlmLineVccHighWngPortn": pm124feAlmLineVccHighWngPortn,
       "pm124feAlmLineTempLowWngPortn": pm124feAlmLineTempLowWngPortn,
       "pm124feAlmLineTempHighWngPortn": pm124feAlmLineTempHighWngPortn,
       "pm124feAlmLineRxPwrLowWngPortn": pm124feAlmLineRxPwrLowWngPortn,
       "pm124feAlmLineRxPwrHighWngPortn": pm124feAlmLineRxPwrHighWngPortn,
       "pm124feAlmLineUrg": pm124feAlmLineUrg,
       "pm124feAlmlineSfpAlmDdmTable": pm124feAlmlineSfpAlmDdmTable,
       "pm124feAlmlineSfpAlmDdmEntry": pm124feAlmlineSfpAlmDdmEntry,
       "pm124feAlmlineSfpAlmDdmIndex": pm124feAlmlineSfpAlmDdmIndex,
       "pm124feAlmLineTxPwrLowAlaPortn": pm124feAlmLineTxPwrLowAlaPortn,
       "pm124feAlmLineTxPwrHighAlaPortn": pm124feAlmLineTxPwrHighAlaPortn,
       "pm124feAlmLineTxBiasLowAlaPortn": pm124feAlmLineTxBiasLowAlaPortn,
       "pm124feAlmLineTxBiasHighAlaPortn": pm124feAlmLineTxBiasHighAlaPortn,
       "pm124feAlmLineVccLowAlaPortn": pm124feAlmLineVccLowAlaPortn,
       "pm124feAlmLineVccHighAlaPortn": pm124feAlmLineVccHighAlaPortn,
       "pm124feAlmLineTempLowAlaPortn": pm124feAlmLineTempLowAlaPortn,
       "pm124feAlmLineTempHighAlaPortn": pm124feAlmLineTempHighAlaPortn,
       "pm124feAlmLineRxPwrLowAlaPortn": pm124feAlmLineRxPwrLowAlaPortn,
       "pm124feAlmLineRxPwrHighAlaPortn": pm124feAlmLineRxPwrHighAlaPortn,
       "pm124feAlmLineCrit": pm124feAlmLineCrit,
       "pm124feAlmsynthAlmLineTable": pm124feAlmsynthAlmLineTable,
       "pm124feAlmsynthAlmLineEntry": pm124feAlmsynthAlmLineEntry,
       "pm124feAlmsynthAlmLineIndex": pm124feAlmsynthAlmLineIndex,
       "pm124feAlmLineSfpAbsentPortn": pm124feAlmLineSfpAbsentPortn,
       "pm124feAlmLineDdmAbsentPortn": pm124feAlmLineDdmAbsentPortn,
       "pm124feAlmLineHwFailPortn": pm124feAlmLineHwFailPortn,
       "pm124feAlmLineLsdPortn": pm124feAlmLineLsdPortn,
       "pm124feAlmLineLocalOosPortn": pm124feAlmLineLocalOosPortn,
       "pm124feAlmLineDdmWarningPortn": pm124feAlmLineDdmWarningPortn,
       "pm124feAlmLineDdmAlmPortn": pm124feAlmLineDdmAlmPortn,
       "pm124feAlmLineFailPortn": pm124feAlmLineFailPortn,
       "pm124feAlmlineAccessioAlmTable": pm124feAlmlineAccessioAlmTable,
       "pm124feAlmlineAccessioAlmEntry": pm124feAlmlineAccessioAlmEntry,
       "pm124feAlmlineAccessioAlmIndex": pm124feAlmlineAccessioAlmIndex,
       "pm124feAlmLineLasFailPortn": pm124feAlmLineLasFailPortn,
       "pm124feAlmLineLosPortn": pm124feAlmLineLosPortn,
       "pm124feAlmLineLossSyncPortn": pm124feAlmLineLossSyncPortn,
       "pm124femeasures": pm124femeasures,
       "pm124feMesrOther": pm124feMesrOther,
       "pm124feMesrClient": pm124feMesrClient,
       "pm124feMesrclientTemperatureTable": pm124feMesrclientTemperatureTable,
       "pm124feMesrclientTemperatureEntry": pm124feMesrclientTemperatureEntry,
       "pm124feMesrclientTemperatureIndex": pm124feMesrclientTemperatureIndex,
       "pm124feMesrclientTemperaturePortn": pm124feMesrclientTemperaturePortn,
       "pm124feMesrclientVoltTable": pm124feMesrclientVoltTable,
       "pm124feMesrclientVoltEntry": pm124feMesrclientVoltEntry,
       "pm124feMesrclientVoltIndex": pm124feMesrclientVoltIndex,
       "pm124feMesrclientVoltPortn": pm124feMesrclientVoltPortn,
       "pm124feMesrclientTxBiasTable": pm124feMesrclientTxBiasTable,
       "pm124feMesrclientTxBiasEntry": pm124feMesrclientTxBiasEntry,
       "pm124feMesrclientTxBiasIndex": pm124feMesrclientTxBiasIndex,
       "pm124feMesrclientTxBiasPortn": pm124feMesrclientTxBiasPortn,
       "pm124feMesrclientTxPowerTable": pm124feMesrclientTxPowerTable,
       "pm124feMesrclientTxPowerEntry": pm124feMesrclientTxPowerEntry,
       "pm124feMesrclientTxPowerIndex": pm124feMesrclientTxPowerIndex,
       "pm124feMesrclientTxPowerPortn": pm124feMesrclientTxPowerPortn,
       "pm124feMesrclientRxPowerTable": pm124feMesrclientRxPowerTable,
       "pm124feMesrclientRxPowerEntry": pm124feMesrclientRxPowerEntry,
       "pm124feMesrclientRxPowerIndex": pm124feMesrclientRxPowerIndex,
       "pm124feMesrclientRxPowerPortn": pm124feMesrclientRxPowerPortn,
       "pm124feMesrLine": pm124feMesrLine,
       "pm124feMesrlineTemperatureTable": pm124feMesrlineTemperatureTable,
       "pm124feMesrlineTemperatureEntry": pm124feMesrlineTemperatureEntry,
       "pm124feMesrlineTemperatureIndex": pm124feMesrlineTemperatureIndex,
       "pm124feMesrlineTemperaturePortn": pm124feMesrlineTemperaturePortn,
       "pm124feMesrlineVoltTable": pm124feMesrlineVoltTable,
       "pm124feMesrlineVoltEntry": pm124feMesrlineVoltEntry,
       "pm124feMesrlineVoltIndex": pm124feMesrlineVoltIndex,
       "pm124feMesrlineVoltPortn": pm124feMesrlineVoltPortn,
       "pm124feMesrlineTxBiasTable": pm124feMesrlineTxBiasTable,
       "pm124feMesrlineTxBiasEntry": pm124feMesrlineTxBiasEntry,
       "pm124feMesrlineTxBiasIndex": pm124feMesrlineTxBiasIndex,
       "pm124feMesrlineTxBiasPortn": pm124feMesrlineTxBiasPortn,
       "pm124feMesrlineTxPowerTable": pm124feMesrlineTxPowerTable,
       "pm124feMesrlineTxPowerEntry": pm124feMesrlineTxPowerEntry,
       "pm124feMesrlineTxPowerIndex": pm124feMesrlineTxPowerIndex,
       "pm124feMesrlineTxPowerPortn": pm124feMesrlineTxPowerPortn,
       "pm124feMesrlineRxPowerTable": pm124feMesrlineRxPowerTable,
       "pm124feMesrlineRxPowerEntry": pm124feMesrlineRxPowerEntry,
       "pm124feMesrlineRxPowerIndex": pm124feMesrlineRxPowerIndex,
       "pm124feMesrlineRxPowerPortn": pm124feMesrlineRxPowerPortn,
       "pm124fecounters": pm124fecounters,
       "pm124feCntOther": pm124feCntOther,
       "pm124feCntClient": pm124feCntClient,
       "pm124feCntclientCbipErrCntTable": pm124feCntclientCbipErrCntTable,
       "pm124feCntclientCbipErrCntEntry": pm124feCntclientCbipErrCntEntry,
       "pm124feCntclientCbipErrCntIndex": pm124feCntclientCbipErrCntIndex,
       "pm124feCntclientCbipErrCntValuePortn": pm124feCntclientCbipErrCntValuePortn,
       "pm124feCntclientCbipErrCntErrorPortn": pm124feCntclientCbipErrCntErrorPortn,
       "pm124feCntclientCbipErrCntOverloadPortn": pm124feCntclientCbipErrCntOverloadPortn,
       "pm124feCntclientFcsErrCntTable": pm124feCntclientFcsErrCntTable,
       "pm124feCntclientFcsErrCntEntry": pm124feCntclientFcsErrCntEntry,
       "pm124feCntclientFcsErrCntIndex": pm124feCntclientFcsErrCntIndex,
       "pm124feCntclientFcsErrCntValuePortn": pm124feCntclientFcsErrCntValuePortn,
       "pm124feCntclientFcsErrCntErrorPortn": pm124feCntclientFcsErrCntErrorPortn,
       "pm124feCntclientFcsErrCntOverloadPortn": pm124feCntclientFcsErrCntOverloadPortn,
       "pm124feCntLine": pm124feCntLine,
       "pm124feCntlineDispErrCntTable": pm124feCntlineDispErrCntTable,
       "pm124feCntlineDispErrCntEntry": pm124feCntlineDispErrCntEntry,
       "pm124feCntlineDispErrCntIndex": pm124feCntlineDispErrCntIndex,
       "pm124feCntlineDispErrCntValuePortn": pm124feCntlineDispErrCntValuePortn,
       "pm124feCntlineDispErrCntErrorPortn": pm124feCntlineDispErrCntErrorPortn,
       "pm124feCntlineDispErrCntOverloadPortn": pm124feCntlineDispErrCntOverloadPortn,
       "pm124feCntlineCrcErrCntTable": pm124feCntlineCrcErrCntTable,
       "pm124feCntlineCrcErrCntEntry": pm124feCntlineCrcErrCntEntry,
       "pm124feCntlineCrcErrCntIndex": pm124feCntlineCrcErrCntIndex,
       "pm124feCntlineCrcErrCntValuePortn": pm124feCntlineCrcErrCntValuePortn,
       "pm124feCntlineCrcErrCntErrorPortn": pm124feCntlineCrcErrCntErrorPortn,
       "pm124feCntlineCrcErrCntOverloadPortn": pm124feCntlineCrcErrCntOverloadPortn,
       "pm124feCntCountersReset": pm124feCntCountersReset,
       "pm124feCntCountersStop": pm124feCntCountersStop,
       "pm124fecontrolsWrite": pm124fecontrolsWrite,
       "pm124feCtrlOther": pm124feCtrlOther,
       "pm124feCtrlsynth0": pm124feCtrlsynth0,
       "pm124feCtrlConfLoad": pm124feCtrlConfLoad,
       "pm124feCtrlConfFlash": pm124feCtrlConfFlash,
       "pm124feCtrlConfClear": pm124feCtrlConfClear,
       "pm124feCtrlsynth4": pm124feCtrlsynth4,
       "pm124feCtrlCorrelatOn": pm124feCtrlCorrelatOn,
       "pm124feCtrlCorrelatOff": pm124feCtrlCorrelatOff,
       "pm124feCtrlswMgnt": pm124feCtrlswMgnt,
       "pm124feCtrlColdReset": pm124feCtrlColdReset,
       "pm124feCtrlWarmReset": pm124feCtrlWarmReset,
       "pm124feCtrlledTest": pm124feCtrlledTest,
       "pm124feCtrlGreenLed": pm124feCtrlGreenLed,
       "pm124feCtrlRedLed": pm124feCtrlRedLed,
       "pm124feCtrlLedOff": pm124feCtrlLedOff,
       "pm124feCtrlmoduleOosMode": pm124feCtrlmoduleOosMode,
       "pm124feCtrlModuleOosMode": pm124feCtrlModuleOosMode,
       "pm124feCtrlClient": pm124feCtrlClient,
       "pm124feCtrlclientSfpOnoffTable": pm124feCtrlclientSfpOnoffTable,
       "pm124feCtrlclientSfpOnoffEntry": pm124feCtrlclientSfpOnoffEntry,
       "pm124feCtrlclientSfpOnoffIndex": pm124feCtrlclientSfpOnoffIndex,
       "pm124feCtrlclientSfpOnoffPortn": pm124feCtrlclientSfpOnoffPortn,
       "pm124feCtrlclientLoopTable": pm124feCtrlclientLoopTable,
       "pm124feCtrlclientLoopEntry": pm124feCtrlclientLoopEntry,
       "pm124feCtrlclientLoopIndex": pm124feCtrlclientLoopIndex,
       "pm124feCtrlclientLoopPortn": pm124feCtrlclientLoopPortn,
       "pm124feCtrlclientCsfUpInsertTable": pm124feCtrlclientCsfUpInsertTable,
       "pm124feCtrlclientCsfUpInsertEntry": pm124feCtrlclientCsfUpInsertEntry,
       "pm124feCtrlclientCsfUpInsertIndex": pm124feCtrlclientCsfUpInsertIndex,
       "pm124feCtrlclientCsfUpInsertPortn": pm124feCtrlclientCsfUpInsertPortn,
       "pm124feCtrlclientCaisDwInsertTable": pm124feCtrlclientCaisDwInsertTable,
       "pm124feCtrlclientCaisDwInsertEntry": pm124feCtrlclientCaisDwInsertEntry,
       "pm124feCtrlclientCaisDwInsertIndex": pm124feCtrlclientCaisDwInsertIndex,
       "pm124feCtrlclientCaisDwInsertPortn": pm124feCtrlclientCaisDwInsertPortn,
       "pm124feCtrlclientOosModeTable": pm124feCtrlclientOosModeTable,
       "pm124feCtrlclientOosModeEntry": pm124feCtrlclientOosModeEntry,
       "pm124feCtrlclientOosModeIndex": pm124feCtrlclientOosModeIndex,
       "pm124feCtrlclientOosModePortn": pm124feCtrlclientOosModePortn,
       "pm124feCtrlLine": pm124feCtrlLine,
       "pm124feCtrllineSfpOnoffTable": pm124feCtrllineSfpOnoffTable,
       "pm124feCtrllineSfpOnoffEntry": pm124feCtrllineSfpOnoffEntry,
       "pm124feCtrllineSfpOnoffIndex": pm124feCtrllineSfpOnoffIndex,
       "pm124feCtrllineSfpOnoffPortn": pm124feCtrllineSfpOnoffPortn,
       "pm124feCtrllineOosModeTable": pm124feCtrllineOosModeTable,
       "pm124feCtrllineOosModeEntry": pm124feCtrllineOosModeEntry,
       "pm124feCtrllineOosModeIndex": pm124feCtrllineOosModeIndex,
       "pm124feCtrllineOosModePortn": pm124feCtrllineOosModePortn,
       "pm124feCtrllineLoopTable": pm124feCtrllineLoopTable,
       "pm124feCtrllineLoopEntry": pm124feCtrllineLoopEntry,
       "pm124feCtrllineLoopIndex": pm124feCtrllineLoopIndex,
       "pm124feCtrllineLoopPortn": pm124feCtrllineLoopPortn,
       "pm124feri": pm124feri,
       "pm124feriTable": pm124feriTable,
       "pm124feRinvClientTable": pm124feRinvClientTable,
       "pm124feRinvClientEntry": pm124feRinvClientEntry,
       "pm124feRinvClientIndex": pm124feRinvClientIndex,
       "pm124feRinvSfpClient": pm124feRinvSfpClient,
       "pm124feRinvLineTable": pm124feRinvLineTable,
       "pm124feRinvLineEntry": pm124feRinvLineEntry,
       "pm124feRinvLineIndex": pm124feRinvLineIndex,
       "pm124feRinvsfpLine": pm124feRinvsfpLine,
       "pm124feRinvReloadInventory": pm124feRinvReloadInventory,
       "pm124feRinvHwPlatform": pm124feRinvHwPlatform,
       "pm124feRinvModulePlatform": pm124feRinvModulePlatform,
       "pm124feRinvSwPlatform": pm124feRinvSwPlatform,
       "pm124feRinvGwPlatform": pm124feRinvGwPlatform,
       "pm124feConfig": pm124feConfig,
       "pm124feCfgLsd": pm124feCfgLsd,
       "pm124feCfgClientLsdTable": pm124feCfgClientLsdTable,
       "pm124feCfgClientLsdEntry": pm124feCfgClientLsdEntry,
       "pm124feCfgClientLsdIndex": pm124feCfgClientLsdIndex,
       "pm124feCfgClientLsdModePortn": pm124feCfgClientLsdModePortn,
       "pm124feCfgClientAccessioCtrbInsPortn": pm124feCfgClientAccessioCtrbInsPortn,
       "pm124feCfgClientAccCtrbInsPortn": pm124feCfgClientAccCtrbInsPortn,
       "pm124feCfgLineAccessioCtrbInsPortn": pm124feCfgLineAccessioCtrbInsPortn,
       "pm124feCfgClientAccCtrbActPortn": pm124feCfgClientAccCtrbActPortn,
       "pm124feCfgLineAccessioCtrbActPortn": pm124feCfgLineAccessioCtrbActPortn,
       "pm124feCfgStartUp": pm124feCfgStartUp,
       "pm124feCfgClientStartupTable": pm124feCfgClientStartupTable,
       "pm124feCfgClientStartupEntry": pm124feCfgClientStartupEntry,
       "pm124feCfgClientStartupIndex": pm124feCfgClientStartupIndex,
       "pm124feCfgClientTrscvCtrlPortn": pm124feCfgClientTrscvCtrlPortn,
       "pm124feCfgClientOosModePortn": pm124feCfgClientOosModePortn,
       "pm124fetablelineStartup": pm124fetablelineStartup,
       "pm124feCfglineTrscvCtrl": pm124feCfglineTrscvCtrl,
       "pm124feCfglineOosMode": pm124feCfglineOosMode,
       "pm124feCfgLabels": pm124feCfgLabels,
       "pm124feCfgLabelclientTable": pm124feCfgLabelclientTable,
       "pm124feCfgLabelclientEntry": pm124feCfgLabelclientEntry,
       "pm124feCfgLabelclientIndex": pm124feCfgLabelclientIndex,
       "pm124feCfgLabelclientPortn": pm124feCfgLabelclientPortn,
       "pm124feCfgLabellineTable": pm124feCfgLabellineTable,
       "pm124feCfgLabellineEntry": pm124feCfgLabellineEntry,
       "pm124feCfgLabellineIndex": pm124feCfgLabellineIndex,
       "pm124feCfgLabellinePortn": pm124feCfgLabellinePortn,
       "pm124feCfgWriteConfiguration": pm124feCfgWriteConfiguration,
       "pm124fetraps": pm124fetraps,
       "pm124fetrapPortNumber": pm124fetrapPortNumber,
       "pm124fetrapLineNumber": pm124fetrapLineNumber,
       "pm124fetrapBoardNumber": pm124fetrapBoardNumber,
       "pm124feLineTrapNotUrgentGoesOn": pm124feLineTrapNotUrgentGoesOn,
       "pm124feLineTrapNotUrgentGoesOff": pm124feLineTrapNotUrgentGoesOff,
       "pm124feLineTrapUrgentGoesOn": pm124feLineTrapUrgentGoesOn,
       "pm124feLineTrapUrgentGoesOff": pm124feLineTrapUrgentGoesOff,
       "pm124feLineTrapCritGoesOn": pm124feLineTrapCritGoesOn,
       "pm124feLineTrapCritGoesOff": pm124feLineTrapCritGoesOff,
       "pm124feClientTrapNotUrgentGoesOn": pm124feClientTrapNotUrgentGoesOn,
       "pm124feClientTrapNotUrgentGoesOff": pm124feClientTrapNotUrgentGoesOff,
       "pm124feClientTrapUrgentGoesOn": pm124feClientTrapUrgentGoesOn,
       "pm124feClientTrapUrgentGoesOff": pm124feClientTrapUrgentGoesOff,
       "pm124feClientTrapCritGoesOn": pm124feClientTrapCritGoesOn,
       "pm124feClientTrapCritGoesOff": pm124feClientTrapCritGoesOff,
       "pm124fePowerTrapUrgentGoesOn": pm124fePowerTrapUrgentGoesOn,
       "pm124fePowerTrapUrgentGoesOff": pm124fePowerTrapUrgentGoesOff}
)
