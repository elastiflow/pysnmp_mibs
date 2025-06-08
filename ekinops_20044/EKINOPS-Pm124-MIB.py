# SNMP MIB module (EKINOPS-Pm124-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Pm124-MIB.mib
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

modulePm124 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16)
)
if mibBuilder.loadTexts:
    modulePm124.setRevisions(
        ("2007-04-04 00:00",
         "2007-06-08 00:00",
         "2007-06-11 00:00",
         "2007-07-06 00:00",
         "2007-11-21 00:00",
         "2009-08-17 00:00",
         "2010-02-25 00:00",
         "2010-11-05 00:00",
         "2012-07-04 00:00",
         "2014-03-27 00:00",
         "2015-01-14 00:00",
         "2015-01-14 00:00",
         "2016-05-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Pm124alarms_ObjectIdentity = ObjectIdentity
pm124alarms = _Pm124alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2)
)
_Pm124AlmOther_ObjectIdentity = ObjectIdentity
pm124AlmOther = _Pm124AlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 1)
)
_Pm124AlmOtherNurg_ObjectIdentity = ObjectIdentity
pm124AlmOtherNurg = _Pm124AlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 1, 1)
)
_Pm124AlmsynthAlm2_ObjectIdentity = ObjectIdentity
pm124AlmsynthAlm2 = _Pm124AlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 1, 1, 2)
)
_Pm124AlmConfTableSave_Type = EkiOnOff
_Pm124AlmConfTableSave_Object = MibScalar
pm124AlmConfTableSave = _Pm124AlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 1, 1, 2, 1),
    _Pm124AlmConfTableSave_Type()
)
pm124AlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmConfTableSave.setStatus("current")
_Pm124AlmInvUpload_Type = EkiOnOff
_Pm124AlmInvUpload_Object = MibScalar
pm124AlmInvUpload = _Pm124AlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 1, 1, 2, 2),
    _Pm124AlmInvUpload_Type()
)
pm124AlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmInvUpload.setStatus("current")
_Pm124AlmConfTableLoad_Type = EkiOnOff
_Pm124AlmConfTableLoad_Object = MibScalar
pm124AlmConfTableLoad = _Pm124AlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 1, 1, 2, 3),
    _Pm124AlmConfTableLoad_Type()
)
pm124AlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmConfTableLoad.setStatus("current")
_Pm124AlmCorrelatOff_Type = EkiOnOff
_Pm124AlmCorrelatOff_Object = MibScalar
pm124AlmCorrelatOff = _Pm124AlmCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 1, 1, 2, 4),
    _Pm124AlmCorrelatOff_Type()
)
pm124AlmCorrelatOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmCorrelatOff.setStatus("current")
_Pm124AlmOtherUrg_ObjectIdentity = ObjectIdentity
pm124AlmOtherUrg = _Pm124AlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 1, 2)
)
_Pm124AlmOtherCrit_ObjectIdentity = ObjectIdentity
pm124AlmOtherCrit = _Pm124AlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 1, 3)
)
_Pm124AlmsynthAlm0_ObjectIdentity = ObjectIdentity
pm124AlmsynthAlm0 = _Pm124AlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 1, 3, 0)
)
_Pm124AlmModuleGlobFailure_Type = EkiOnOff
_Pm124AlmModuleGlobFailure_Object = MibScalar
pm124AlmModuleGlobFailure = _Pm124AlmModuleGlobFailure_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 1, 3, 0, 9),
    _Pm124AlmModuleGlobFailure_Type()
)
pm124AlmModuleGlobFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmModuleGlobFailure.setStatus("current")
_Pm124AlmDefFuseA_Type = EkiOnOff
_Pm124AlmDefFuseA_Object = MibScalar
pm124AlmDefFuseA = _Pm124AlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 1, 3, 0, 15),
    _Pm124AlmDefFuseA_Type()
)
pm124AlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmDefFuseA.setStatus("current")
_Pm124AlmDefFuseB_Type = EkiOnOff
_Pm124AlmDefFuseB_Object = MibScalar
pm124AlmDefFuseB = _Pm124AlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 1, 3, 0, 16),
    _Pm124AlmDefFuseB_Type()
)
pm124AlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmDefFuseB.setStatus("current")
_Pm124AlmClient_ObjectIdentity = ObjectIdentity
pm124AlmClient = _Pm124AlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2)
)
_Pm124AlmClientNurg_ObjectIdentity = ObjectIdentity
pm124AlmClientNurg = _Pm124AlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 1)
)
_Pm124AlmclientSfpWarnDdmTable_Object = MibTable
pm124AlmclientSfpWarnDdmTable = _Pm124AlmclientSfpWarnDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 1, 32)
)
if mibBuilder.loadTexts:
    pm124AlmclientSfpWarnDdmTable.setStatus("current")
_Pm124AlmclientSfpWarnDdmEntry_Object = MibTableRow
pm124AlmclientSfpWarnDdmEntry = _Pm124AlmclientSfpWarnDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 1, 32, 1)
)
pm124AlmclientSfpWarnDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm124-MIB", "pm124AlmclientSfpWarnDdmIndex"),
)
if mibBuilder.loadTexts:
    pm124AlmclientSfpWarnDdmEntry.setStatus("current")


class _Pm124AlmclientSfpWarnDdmIndex_Type(Integer32):
    """Custom type pm124AlmclientSfpWarnDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124AlmclientSfpWarnDdmIndex_Type.__name__ = "Integer32"
_Pm124AlmclientSfpWarnDdmIndex_Object = MibTableColumn
pm124AlmclientSfpWarnDdmIndex = _Pm124AlmclientSfpWarnDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 1, 32, 1, 1),
    _Pm124AlmclientSfpWarnDdmIndex_Type()
)
pm124AlmclientSfpWarnDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmclientSfpWarnDdmIndex.setStatus("current")
_Pm124AlmClientTxPwLowWngPortn_Type = EkiOnOff
_Pm124AlmClientTxPwLowWngPortn_Object = MibTableColumn
pm124AlmClientTxPwLowWngPortn = _Pm124AlmClientTxPwLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 1, 32, 1, 2),
    _Pm124AlmClientTxPwLowWngPortn_Type()
)
pm124AlmClientTxPwLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmClientTxPwLowWngPortn.setStatus("current")
_Pm124AlmClientTxPwrHighWngPortn_Type = EkiOnOff
_Pm124AlmClientTxPwrHighWngPortn_Object = MibTableColumn
pm124AlmClientTxPwrHighWngPortn = _Pm124AlmClientTxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 1, 32, 1, 3),
    _Pm124AlmClientTxPwrHighWngPortn_Type()
)
pm124AlmClientTxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmClientTxPwrHighWngPortn.setStatus("current")
_Pm124AlmClientTxBiasLowWngPortn_Type = EkiOnOff
_Pm124AlmClientTxBiasLowWngPortn_Object = MibTableColumn
pm124AlmClientTxBiasLowWngPortn = _Pm124AlmClientTxBiasLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 1, 32, 1, 4),
    _Pm124AlmClientTxBiasLowWngPortn_Type()
)
pm124AlmClientTxBiasLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmClientTxBiasLowWngPortn.setStatus("current")
_Pm124AlmClientTxBiasHighWngPortn_Type = EkiOnOff
_Pm124AlmClientTxBiasHighWngPortn_Object = MibTableColumn
pm124AlmClientTxBiasHighWngPortn = _Pm124AlmClientTxBiasHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 1, 32, 1, 5),
    _Pm124AlmClientTxBiasHighWngPortn_Type()
)
pm124AlmClientTxBiasHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmClientTxBiasHighWngPortn.setStatus("current")
_Pm124AlmClientVccLowWngPortn_Type = EkiOnOff
_Pm124AlmClientVccLowWngPortn_Object = MibTableColumn
pm124AlmClientVccLowWngPortn = _Pm124AlmClientVccLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 1, 32, 1, 6),
    _Pm124AlmClientVccLowWngPortn_Type()
)
pm124AlmClientVccLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmClientVccLowWngPortn.setStatus("current")
_Pm124AlmClientVccHighWngPortn_Type = EkiOnOff
_Pm124AlmClientVccHighWngPortn_Object = MibTableColumn
pm124AlmClientVccHighWngPortn = _Pm124AlmClientVccHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 1, 32, 1, 7),
    _Pm124AlmClientVccHighWngPortn_Type()
)
pm124AlmClientVccHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmClientVccHighWngPortn.setStatus("current")
_Pm124AlmClientTempLowWngPortn_Type = EkiOnOff
_Pm124AlmClientTempLowWngPortn_Object = MibTableColumn
pm124AlmClientTempLowWngPortn = _Pm124AlmClientTempLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 1, 32, 1, 8),
    _Pm124AlmClientTempLowWngPortn_Type()
)
pm124AlmClientTempLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmClientTempLowWngPortn.setStatus("current")
_Pm124AlmClientTempHighWngPortn_Type = EkiOnOff
_Pm124AlmClientTempHighWngPortn_Object = MibTableColumn
pm124AlmClientTempHighWngPortn = _Pm124AlmClientTempHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 1, 32, 1, 9),
    _Pm124AlmClientTempHighWngPortn_Type()
)
pm124AlmClientTempHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmClientTempHighWngPortn.setStatus("current")
_Pm124AlmClientRxPwrLowWngPortn_Type = EkiOnOff
_Pm124AlmClientRxPwrLowWngPortn_Object = MibTableColumn
pm124AlmClientRxPwrLowWngPortn = _Pm124AlmClientRxPwrLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 1, 32, 1, 16),
    _Pm124AlmClientRxPwrLowWngPortn_Type()
)
pm124AlmClientRxPwrLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmClientRxPwrLowWngPortn.setStatus("current")
_Pm124AlmClientRxPwrHighWngPortn_Type = EkiOnOff
_Pm124AlmClientRxPwrHighWngPortn_Object = MibTableColumn
pm124AlmClientRxPwrHighWngPortn = _Pm124AlmClientRxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 1, 32, 1, 17),
    _Pm124AlmClientRxPwrHighWngPortn_Type()
)
pm124AlmClientRxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmClientRxPwrHighWngPortn.setStatus("current")
_Pm124AlmClientUrg_ObjectIdentity = ObjectIdentity
pm124AlmClientUrg = _Pm124AlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 2)
)
_Pm124AlmclientSfpAlmDdmTable_Object = MibTable
pm124AlmclientSfpAlmDdmTable = _Pm124AlmclientSfpAlmDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 2, 24)
)
if mibBuilder.loadTexts:
    pm124AlmclientSfpAlmDdmTable.setStatus("current")
_Pm124AlmclientSfpAlmDdmEntry_Object = MibTableRow
pm124AlmclientSfpAlmDdmEntry = _Pm124AlmclientSfpAlmDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 2, 24, 1)
)
pm124AlmclientSfpAlmDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm124-MIB", "pm124AlmclientSfpAlmDdmIndex"),
)
if mibBuilder.loadTexts:
    pm124AlmclientSfpAlmDdmEntry.setStatus("current")


class _Pm124AlmclientSfpAlmDdmIndex_Type(Integer32):
    """Custom type pm124AlmclientSfpAlmDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124AlmclientSfpAlmDdmIndex_Type.__name__ = "Integer32"
_Pm124AlmclientSfpAlmDdmIndex_Object = MibTableColumn
pm124AlmclientSfpAlmDdmIndex = _Pm124AlmclientSfpAlmDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 2, 24, 1, 1),
    _Pm124AlmclientSfpAlmDdmIndex_Type()
)
pm124AlmclientSfpAlmDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmclientSfpAlmDdmIndex.setStatus("current")
_Pm124AlmClientTxPwrLowAlaPortn_Type = EkiOnOff
_Pm124AlmClientTxPwrLowAlaPortn_Object = MibTableColumn
pm124AlmClientTxPwrLowAlaPortn = _Pm124AlmClientTxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 2, 24, 1, 2),
    _Pm124AlmClientTxPwrLowAlaPortn_Type()
)
pm124AlmClientTxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmClientTxPwrLowAlaPortn.setStatus("current")
_Pm124AlmClientClientTxPwrHighAlaPortn_Type = EkiOnOff
_Pm124AlmClientClientTxPwrHighAlaPortn_Object = MibTableColumn
pm124AlmClientClientTxPwrHighAlaPortn = _Pm124AlmClientClientTxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 2, 24, 1, 3),
    _Pm124AlmClientClientTxPwrHighAlaPortn_Type()
)
pm124AlmClientClientTxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmClientClientTxPwrHighAlaPortn.setStatus("current")
_Pm124AlmClientTxBiasLowAlaPortn_Type = EkiOnOff
_Pm124AlmClientTxBiasLowAlaPortn_Object = MibTableColumn
pm124AlmClientTxBiasLowAlaPortn = _Pm124AlmClientTxBiasLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 2, 24, 1, 4),
    _Pm124AlmClientTxBiasLowAlaPortn_Type()
)
pm124AlmClientTxBiasLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmClientTxBiasLowAlaPortn.setStatus("current")
_Pm124AlmClientTxBiasHighAlaPortn_Type = EkiOnOff
_Pm124AlmClientTxBiasHighAlaPortn_Object = MibTableColumn
pm124AlmClientTxBiasHighAlaPortn = _Pm124AlmClientTxBiasHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 2, 24, 1, 5),
    _Pm124AlmClientTxBiasHighAlaPortn_Type()
)
pm124AlmClientTxBiasHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmClientTxBiasHighAlaPortn.setStatus("current")
_Pm124AlmClientVccLowAlaPortn_Type = EkiOnOff
_Pm124AlmClientVccLowAlaPortn_Object = MibTableColumn
pm124AlmClientVccLowAlaPortn = _Pm124AlmClientVccLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 2, 24, 1, 6),
    _Pm124AlmClientVccLowAlaPortn_Type()
)
pm124AlmClientVccLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmClientVccLowAlaPortn.setStatus("current")
_Pm124AlmClientVccHighAlaPortn_Type = EkiOnOff
_Pm124AlmClientVccHighAlaPortn_Object = MibTableColumn
pm124AlmClientVccHighAlaPortn = _Pm124AlmClientVccHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 2, 24, 1, 7),
    _Pm124AlmClientVccHighAlaPortn_Type()
)
pm124AlmClientVccHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmClientVccHighAlaPortn.setStatus("current")
_Pm124AlmClientTempLowAlaPortn_Type = EkiOnOff
_Pm124AlmClientTempLowAlaPortn_Object = MibTableColumn
pm124AlmClientTempLowAlaPortn = _Pm124AlmClientTempLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 2, 24, 1, 8),
    _Pm124AlmClientTempLowAlaPortn_Type()
)
pm124AlmClientTempLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmClientTempLowAlaPortn.setStatus("current")
_Pm124AlmClientTempHighAlaPortn_Type = EkiOnOff
_Pm124AlmClientTempHighAlaPortn_Object = MibTableColumn
pm124AlmClientTempHighAlaPortn = _Pm124AlmClientTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 2, 24, 1, 9),
    _Pm124AlmClientTempHighAlaPortn_Type()
)
pm124AlmClientTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmClientTempHighAlaPortn.setStatus("current")
_Pm124AlmClientRxPwrLowAlaPortn_Type = EkiOnOff
_Pm124AlmClientRxPwrLowAlaPortn_Object = MibTableColumn
pm124AlmClientRxPwrLowAlaPortn = _Pm124AlmClientRxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 2, 24, 1, 16),
    _Pm124AlmClientRxPwrLowAlaPortn_Type()
)
pm124AlmClientRxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmClientRxPwrLowAlaPortn.setStatus("current")
_Pm124AlmClientRxPwrHighAlaPortn_Type = EkiOnOff
_Pm124AlmClientRxPwrHighAlaPortn_Object = MibTableColumn
pm124AlmClientRxPwrHighAlaPortn = _Pm124AlmClientRxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 2, 24, 1, 17),
    _Pm124AlmClientRxPwrHighAlaPortn_Type()
)
pm124AlmClientRxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmClientRxPwrHighAlaPortn.setStatus("current")
_Pm124AlmClientCrit_ObjectIdentity = ObjectIdentity
pm124AlmClientCrit = _Pm124AlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 3)
)
_Pm124AlmsynthAlmPortTable_Object = MibTable
pm124AlmsynthAlmPortTable = _Pm124AlmsynthAlmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    pm124AlmsynthAlmPortTable.setStatus("current")
_Pm124AlmsynthAlmPortEntry_Object = MibTableRow
pm124AlmsynthAlmPortEntry = _Pm124AlmsynthAlmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 3, 8, 1)
)
pm124AlmsynthAlmPortEntry.setIndexNames(
    (0, "EKINOPS-Pm124-MIB", "pm124AlmsynthAlmPortIndex"),
)
if mibBuilder.loadTexts:
    pm124AlmsynthAlmPortEntry.setStatus("current")


class _Pm124AlmsynthAlmPortIndex_Type(Integer32):
    """Custom type pm124AlmsynthAlmPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124AlmsynthAlmPortIndex_Type.__name__ = "Integer32"
_Pm124AlmsynthAlmPortIndex_Object = MibTableColumn
pm124AlmsynthAlmPortIndex = _Pm124AlmsynthAlmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 3, 8, 1, 1),
    _Pm124AlmsynthAlmPortIndex_Type()
)
pm124AlmsynthAlmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmsynthAlmPortIndex.setStatus("current")
_Pm124AlmClientSfpAbsentPortn_Type = EkiOnOff
_Pm124AlmClientSfpAbsentPortn_Object = MibTableColumn
pm124AlmClientSfpAbsentPortn = _Pm124AlmClientSfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 3, 8, 1, 2),
    _Pm124AlmClientSfpAbsentPortn_Type()
)
pm124AlmClientSfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmClientSfpAbsentPortn.setStatus("current")
_Pm124AlmClientDdmAbsentPortn_Type = EkiOnOff
_Pm124AlmClientDdmAbsentPortn_Object = MibTableColumn
pm124AlmClientDdmAbsentPortn = _Pm124AlmClientDdmAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 3, 8, 1, 3),
    _Pm124AlmClientDdmAbsentPortn_Type()
)
pm124AlmClientDdmAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmClientDdmAbsentPortn.setStatus("current")
_Pm124AlmClientHwFailAccPortn_Type = EkiOnOff
_Pm124AlmClientHwFailAccPortn_Object = MibTableColumn
pm124AlmClientHwFailAccPortn = _Pm124AlmClientHwFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 3, 8, 1, 5),
    _Pm124AlmClientHwFailAccPortn_Type()
)
pm124AlmClientHwFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmClientHwFailAccPortn.setStatus("current")
_Pm124AlmClientLsdPortn_Type = EkiOnOff
_Pm124AlmClientLsdPortn_Object = MibTableColumn
pm124AlmClientLsdPortn = _Pm124AlmClientLsdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 3, 8, 1, 6),
    _Pm124AlmClientLsdPortn_Type()
)
pm124AlmClientLsdPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmClientLsdPortn.setStatus("current")
_Pm124AlmClientLocalOosPortn_Type = EkiOnOff
_Pm124AlmClientLocalOosPortn_Object = MibTableColumn
pm124AlmClientLocalOosPortn = _Pm124AlmClientLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 3, 8, 1, 7),
    _Pm124AlmClientLocalOosPortn_Type()
)
pm124AlmClientLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmClientLocalOosPortn.setStatus("current")
_Pm124AlmClientRemoteOosPortn_Type = EkiOnOff
_Pm124AlmClientRemoteOosPortn_Object = MibTableColumn
pm124AlmClientRemoteOosPortn = _Pm124AlmClientRemoteOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 3, 8, 1, 8),
    _Pm124AlmClientRemoteOosPortn_Type()
)
pm124AlmClientRemoteOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmClientRemoteOosPortn.setStatus("current")
_Pm124AlmClientDwCaisPortn_Type = EkiOnOff
_Pm124AlmClientDwCaisPortn_Object = MibTableColumn
pm124AlmClientDwCaisPortn = _Pm124AlmClientDwCaisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 3, 8, 1, 9),
    _Pm124AlmClientDwCaisPortn_Type()
)
pm124AlmClientDwCaisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmClientDwCaisPortn.setStatus("current")
_Pm124AlmClientSfpDdmWarningPortn_Type = EkiOnOff
_Pm124AlmClientSfpDdmWarningPortn_Object = MibTableColumn
pm124AlmClientSfpDdmWarningPortn = _Pm124AlmClientSfpDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 3, 8, 1, 10),
    _Pm124AlmClientSfpDdmWarningPortn_Type()
)
pm124AlmClientSfpDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmClientSfpDdmWarningPortn.setStatus("current")
_Pm124AlmClientSfpDdmAlmPortn_Type = EkiOnOff
_Pm124AlmClientSfpDdmAlmPortn_Object = MibTableColumn
pm124AlmClientSfpDdmAlmPortn = _Pm124AlmClientSfpDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 3, 8, 1, 11),
    _Pm124AlmClientSfpDdmAlmPortn_Type()
)
pm124AlmClientSfpDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmClientSfpDdmAlmPortn.setStatus("current")
_Pm124AlmClientFailAccPortn_Type = EkiOnOff
_Pm124AlmClientFailAccPortn_Object = MibTableColumn
pm124AlmClientFailAccPortn = _Pm124AlmClientFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 3, 8, 1, 13),
    _Pm124AlmClientFailAccPortn_Type()
)
pm124AlmClientFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmClientFailAccPortn.setStatus("current")
_Pm124AlmClientUpCsfPortn_Type = EkiOnOff
_Pm124AlmClientUpCsfPortn_Object = MibTableColumn
pm124AlmClientUpCsfPortn = _Pm124AlmClientUpCsfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 3, 8, 1, 17),
    _Pm124AlmClientUpCsfPortn_Type()
)
pm124AlmClientUpCsfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmClientUpCsfPortn.setStatus("current")
_Pm124AlmclientAccessioAlmTable_Object = MibTable
pm124AlmclientAccessioAlmTable = _Pm124AlmclientAccessioAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 3, 16)
)
if mibBuilder.loadTexts:
    pm124AlmclientAccessioAlmTable.setStatus("current")
_Pm124AlmclientAccessioAlmEntry_Object = MibTableRow
pm124AlmclientAccessioAlmEntry = _Pm124AlmclientAccessioAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 3, 16, 1)
)
pm124AlmclientAccessioAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm124-MIB", "pm124AlmclientAccessioAlmIndex"),
)
if mibBuilder.loadTexts:
    pm124AlmclientAccessioAlmEntry.setStatus("current")


class _Pm124AlmclientAccessioAlmIndex_Type(Integer32):
    """Custom type pm124AlmclientAccessioAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124AlmclientAccessioAlmIndex_Type.__name__ = "Integer32"
_Pm124AlmclientAccessioAlmIndex_Object = MibTableColumn
pm124AlmclientAccessioAlmIndex = _Pm124AlmclientAccessioAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 3, 16, 1, 1),
    _Pm124AlmclientAccessioAlmIndex_Type()
)
pm124AlmclientAccessioAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmclientAccessioAlmIndex.setStatus("current")
_Pm124AlmClientLasFailPortn_Type = EkiOnOff
_Pm124AlmClientLasFailPortn_Object = MibTableColumn
pm124AlmClientLasFailPortn = _Pm124AlmClientLasFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 3, 16, 1, 2),
    _Pm124AlmClientLasFailPortn_Type()
)
pm124AlmClientLasFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmClientLasFailPortn.setStatus("current")
_Pm124AlmClientLosPortn_Type = EkiOnOff
_Pm124AlmClientLosPortn_Object = MibTableColumn
pm124AlmClientLosPortn = _Pm124AlmClientLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 3, 16, 1, 5),
    _Pm124AlmClientLosPortn_Type()
)
pm124AlmClientLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmClientLosPortn.setStatus("current")
_Pm124AlmclientAccAlmTable_Object = MibTable
pm124AlmclientAccAlmTable = _Pm124AlmclientAccAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 3, 40)
)
if mibBuilder.loadTexts:
    pm124AlmclientAccAlmTable.setStatus("current")
_Pm124AlmclientAccAlmEntry_Object = MibTableRow
pm124AlmclientAccAlmEntry = _Pm124AlmclientAccAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 3, 40, 1)
)
pm124AlmclientAccAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm124-MIB", "pm124AlmclientAccAlmIndex"),
)
if mibBuilder.loadTexts:
    pm124AlmclientAccAlmEntry.setStatus("current")


class _Pm124AlmclientAccAlmIndex_Type(Integer32):
    """Custom type pm124AlmclientAccAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124AlmclientAccAlmIndex_Type.__name__ = "Integer32"
_Pm124AlmclientAccAlmIndex_Object = MibTableColumn
pm124AlmclientAccAlmIndex = _Pm124AlmclientAccAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 3, 40, 1, 1),
    _Pm124AlmclientAccAlmIndex_Type()
)
pm124AlmclientAccAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmclientAccAlmIndex.setStatus("current")
_Pm124AlmClientOosPortn_Type = EkiOnOff
_Pm124AlmClientOosPortn_Object = MibTableColumn
pm124AlmClientOosPortn = _Pm124AlmClientOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 3, 40, 1, 2),
    _Pm124AlmClientOosPortn_Type()
)
pm124AlmClientOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmClientOosPortn.setStatus("current")
_Pm124AlmClientUpEsOvlPortn_Type = EkiOnOff
_Pm124AlmClientUpEsOvlPortn_Object = MibTableColumn
pm124AlmClientUpEsOvlPortn = _Pm124AlmClientUpEsOvlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 3, 40, 1, 11),
    _Pm124AlmClientUpEsOvlPortn_Type()
)
pm124AlmClientUpEsOvlPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmClientUpEsOvlPortn.setStatus("current")
_Pm124AlmClientCsfDetPortn_Type = EkiOnOff
_Pm124AlmClientCsfDetPortn_Object = MibTableColumn
pm124AlmClientCsfDetPortn = _Pm124AlmClientCsfDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 3, 40, 1, 12),
    _Pm124AlmClientCsfDetPortn_Type()
)
pm124AlmClientCsfDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmClientCsfDetPortn.setStatus("current")
_Pm124AlmClientDwEsOvlPortn_Type = EkiOnOff
_Pm124AlmClientDwEsOvlPortn_Object = MibTableColumn
pm124AlmClientDwEsOvlPortn = _Pm124AlmClientDwEsOvlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 2, 3, 40, 1, 15),
    _Pm124AlmClientDwEsOvlPortn_Type()
)
pm124AlmClientDwEsOvlPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmClientDwEsOvlPortn.setStatus("current")
_Pm124AlmLine_ObjectIdentity = ObjectIdentity
pm124AlmLine = _Pm124AlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3)
)
_Pm124AlmLineNurg_ObjectIdentity = ObjectIdentity
pm124AlmLineNurg = _Pm124AlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 1)
)
_Pm124AlmlineSfpWarnDdmTable_Object = MibTable
pm124AlmlineSfpWarnDdmTable = _Pm124AlmlineSfpWarnDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 1, 66)
)
if mibBuilder.loadTexts:
    pm124AlmlineSfpWarnDdmTable.setStatus("current")
_Pm124AlmlineSfpWarnDdmEntry_Object = MibTableRow
pm124AlmlineSfpWarnDdmEntry = _Pm124AlmlineSfpWarnDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 1, 66, 1)
)
pm124AlmlineSfpWarnDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm124-MIB", "pm124AlmlineSfpWarnDdmIndex"),
)
if mibBuilder.loadTexts:
    pm124AlmlineSfpWarnDdmEntry.setStatus("current")


class _Pm124AlmlineSfpWarnDdmIndex_Type(Integer32):
    """Custom type pm124AlmlineSfpWarnDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124AlmlineSfpWarnDdmIndex_Type.__name__ = "Integer32"
_Pm124AlmlineSfpWarnDdmIndex_Object = MibTableColumn
pm124AlmlineSfpWarnDdmIndex = _Pm124AlmlineSfpWarnDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 1, 66, 1, 1),
    _Pm124AlmlineSfpWarnDdmIndex_Type()
)
pm124AlmlineSfpWarnDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmlineSfpWarnDdmIndex.setStatus("current")
_Pm124AlmLineTxPwLowWngPortn_Type = EkiOnOff
_Pm124AlmLineTxPwLowWngPortn_Object = MibTableColumn
pm124AlmLineTxPwLowWngPortn = _Pm124AlmLineTxPwLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 1, 66, 1, 2),
    _Pm124AlmLineTxPwLowWngPortn_Type()
)
pm124AlmLineTxPwLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmLineTxPwLowWngPortn.setStatus("current")
_Pm124AlmLineTxPwrHighWngPortn_Type = EkiOnOff
_Pm124AlmLineTxPwrHighWngPortn_Object = MibTableColumn
pm124AlmLineTxPwrHighWngPortn = _Pm124AlmLineTxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 1, 66, 1, 3),
    _Pm124AlmLineTxPwrHighWngPortn_Type()
)
pm124AlmLineTxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmLineTxPwrHighWngPortn.setStatus("current")
_Pm124AlmLineTxBiasLowWngPortn_Type = EkiOnOff
_Pm124AlmLineTxBiasLowWngPortn_Object = MibTableColumn
pm124AlmLineTxBiasLowWngPortn = _Pm124AlmLineTxBiasLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 1, 66, 1, 4),
    _Pm124AlmLineTxBiasLowWngPortn_Type()
)
pm124AlmLineTxBiasLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmLineTxBiasLowWngPortn.setStatus("current")
_Pm124AlmLineTxBiasHighWngPortn_Type = EkiOnOff
_Pm124AlmLineTxBiasHighWngPortn_Object = MibTableColumn
pm124AlmLineTxBiasHighWngPortn = _Pm124AlmLineTxBiasHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 1, 66, 1, 5),
    _Pm124AlmLineTxBiasHighWngPortn_Type()
)
pm124AlmLineTxBiasHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmLineTxBiasHighWngPortn.setStatus("current")
_Pm124AlmLineVccLowWngPortn_Type = EkiOnOff
_Pm124AlmLineVccLowWngPortn_Object = MibTableColumn
pm124AlmLineVccLowWngPortn = _Pm124AlmLineVccLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 1, 66, 1, 6),
    _Pm124AlmLineVccLowWngPortn_Type()
)
pm124AlmLineVccLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmLineVccLowWngPortn.setStatus("current")
_Pm124AlmLineVccHighWngPortn_Type = EkiOnOff
_Pm124AlmLineVccHighWngPortn_Object = MibTableColumn
pm124AlmLineVccHighWngPortn = _Pm124AlmLineVccHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 1, 66, 1, 7),
    _Pm124AlmLineVccHighWngPortn_Type()
)
pm124AlmLineVccHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmLineVccHighWngPortn.setStatus("current")
_Pm124AlmLineTempLowWngPortn_Type = EkiOnOff
_Pm124AlmLineTempLowWngPortn_Object = MibTableColumn
pm124AlmLineTempLowWngPortn = _Pm124AlmLineTempLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 1, 66, 1, 8),
    _Pm124AlmLineTempLowWngPortn_Type()
)
pm124AlmLineTempLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmLineTempLowWngPortn.setStatus("current")
_Pm124AlmLineTempHighWngPortn_Type = EkiOnOff
_Pm124AlmLineTempHighWngPortn_Object = MibTableColumn
pm124AlmLineTempHighWngPortn = _Pm124AlmLineTempHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 1, 66, 1, 9),
    _Pm124AlmLineTempHighWngPortn_Type()
)
pm124AlmLineTempHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmLineTempHighWngPortn.setStatus("current")
_Pm124AlmLineRxPwrLowWngPortn_Type = EkiOnOff
_Pm124AlmLineRxPwrLowWngPortn_Object = MibTableColumn
pm124AlmLineRxPwrLowWngPortn = _Pm124AlmLineRxPwrLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 1, 66, 1, 16),
    _Pm124AlmLineRxPwrLowWngPortn_Type()
)
pm124AlmLineRxPwrLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmLineRxPwrLowWngPortn.setStatus("current")
_Pm124AlmLineRxPwrHighWngPortn_Type = EkiOnOff
_Pm124AlmLineRxPwrHighWngPortn_Object = MibTableColumn
pm124AlmLineRxPwrHighWngPortn = _Pm124AlmLineRxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 1, 66, 1, 17),
    _Pm124AlmLineRxPwrHighWngPortn_Type()
)
pm124AlmLineRxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmLineRxPwrHighWngPortn.setStatus("current")
_Pm124AlmLineUrg_ObjectIdentity = ObjectIdentity
pm124AlmLineUrg = _Pm124AlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 2)
)
_Pm124AlmlineSfpAlmDdmTable_Object = MibTable
pm124AlmlineSfpAlmDdmTable = _Pm124AlmlineSfpAlmDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 2, 65)
)
if mibBuilder.loadTexts:
    pm124AlmlineSfpAlmDdmTable.setStatus("current")
_Pm124AlmlineSfpAlmDdmEntry_Object = MibTableRow
pm124AlmlineSfpAlmDdmEntry = _Pm124AlmlineSfpAlmDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 2, 65, 1)
)
pm124AlmlineSfpAlmDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm124-MIB", "pm124AlmlineSfpAlmDdmIndex"),
)
if mibBuilder.loadTexts:
    pm124AlmlineSfpAlmDdmEntry.setStatus("current")


class _Pm124AlmlineSfpAlmDdmIndex_Type(Integer32):
    """Custom type pm124AlmlineSfpAlmDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124AlmlineSfpAlmDdmIndex_Type.__name__ = "Integer32"
_Pm124AlmlineSfpAlmDdmIndex_Object = MibTableColumn
pm124AlmlineSfpAlmDdmIndex = _Pm124AlmlineSfpAlmDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 2, 65, 1, 1),
    _Pm124AlmlineSfpAlmDdmIndex_Type()
)
pm124AlmlineSfpAlmDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmlineSfpAlmDdmIndex.setStatus("current")
_Pm124AlmLineTxPwrLowAlaPortn_Type = EkiOnOff
_Pm124AlmLineTxPwrLowAlaPortn_Object = MibTableColumn
pm124AlmLineTxPwrLowAlaPortn = _Pm124AlmLineTxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 2, 65, 1, 2),
    _Pm124AlmLineTxPwrLowAlaPortn_Type()
)
pm124AlmLineTxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmLineTxPwrLowAlaPortn.setStatus("current")
_Pm124AlmLineTxPwrHighAlaPortn_Type = EkiOnOff
_Pm124AlmLineTxPwrHighAlaPortn_Object = MibTableColumn
pm124AlmLineTxPwrHighAlaPortn = _Pm124AlmLineTxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 2, 65, 1, 3),
    _Pm124AlmLineTxPwrHighAlaPortn_Type()
)
pm124AlmLineTxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmLineTxPwrHighAlaPortn.setStatus("current")
_Pm124AlmLineTxBiasLowAlaPortn_Type = EkiOnOff
_Pm124AlmLineTxBiasLowAlaPortn_Object = MibTableColumn
pm124AlmLineTxBiasLowAlaPortn = _Pm124AlmLineTxBiasLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 2, 65, 1, 4),
    _Pm124AlmLineTxBiasLowAlaPortn_Type()
)
pm124AlmLineTxBiasLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmLineTxBiasLowAlaPortn.setStatus("current")
_Pm124AlmLineTxBiasHighAlaPortn_Type = EkiOnOff
_Pm124AlmLineTxBiasHighAlaPortn_Object = MibTableColumn
pm124AlmLineTxBiasHighAlaPortn = _Pm124AlmLineTxBiasHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 2, 65, 1, 5),
    _Pm124AlmLineTxBiasHighAlaPortn_Type()
)
pm124AlmLineTxBiasHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmLineTxBiasHighAlaPortn.setStatus("current")
_Pm124AlmLineVccLowAlaPortn_Type = EkiOnOff
_Pm124AlmLineVccLowAlaPortn_Object = MibTableColumn
pm124AlmLineVccLowAlaPortn = _Pm124AlmLineVccLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 2, 65, 1, 6),
    _Pm124AlmLineVccLowAlaPortn_Type()
)
pm124AlmLineVccLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmLineVccLowAlaPortn.setStatus("current")
_Pm124AlmLineVccHighAlaPortn_Type = EkiOnOff
_Pm124AlmLineVccHighAlaPortn_Object = MibTableColumn
pm124AlmLineVccHighAlaPortn = _Pm124AlmLineVccHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 2, 65, 1, 7),
    _Pm124AlmLineVccHighAlaPortn_Type()
)
pm124AlmLineVccHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmLineVccHighAlaPortn.setStatus("current")
_Pm124AlmLineTempLowAlaPortn_Type = EkiOnOff
_Pm124AlmLineTempLowAlaPortn_Object = MibTableColumn
pm124AlmLineTempLowAlaPortn = _Pm124AlmLineTempLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 2, 65, 1, 8),
    _Pm124AlmLineTempLowAlaPortn_Type()
)
pm124AlmLineTempLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmLineTempLowAlaPortn.setStatus("current")
_Pm124AlmLineTempHighAlaPortn_Type = EkiOnOff
_Pm124AlmLineTempHighAlaPortn_Object = MibTableColumn
pm124AlmLineTempHighAlaPortn = _Pm124AlmLineTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 2, 65, 1, 9),
    _Pm124AlmLineTempHighAlaPortn_Type()
)
pm124AlmLineTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmLineTempHighAlaPortn.setStatus("current")
_Pm124AlmLineRxPwrLowAlaPortn_Type = EkiOnOff
_Pm124AlmLineRxPwrLowAlaPortn_Object = MibTableColumn
pm124AlmLineRxPwrLowAlaPortn = _Pm124AlmLineRxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 2, 65, 1, 16),
    _Pm124AlmLineRxPwrLowAlaPortn_Type()
)
pm124AlmLineRxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmLineRxPwrLowAlaPortn.setStatus("current")
_Pm124AlmLineRxPwrHighAlaPortn_Type = EkiOnOff
_Pm124AlmLineRxPwrHighAlaPortn_Object = MibTableColumn
pm124AlmLineRxPwrHighAlaPortn = _Pm124AlmLineRxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 2, 65, 1, 17),
    _Pm124AlmLineRxPwrHighAlaPortn_Type()
)
pm124AlmLineRxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmLineRxPwrHighAlaPortn.setStatus("current")
_Pm124AlmLineCrit_ObjectIdentity = ObjectIdentity
pm124AlmLineCrit = _Pm124AlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 3)
)
_Pm124AlmsynthAlmLineTable_Object = MibTable
pm124AlmsynthAlmLineTable = _Pm124AlmsynthAlmLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 3, 7)
)
if mibBuilder.loadTexts:
    pm124AlmsynthAlmLineTable.setStatus("current")
_Pm124AlmsynthAlmLineEntry_Object = MibTableRow
pm124AlmsynthAlmLineEntry = _Pm124AlmsynthAlmLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 3, 7, 1)
)
pm124AlmsynthAlmLineEntry.setIndexNames(
    (0, "EKINOPS-Pm124-MIB", "pm124AlmsynthAlmLineIndex"),
)
if mibBuilder.loadTexts:
    pm124AlmsynthAlmLineEntry.setStatus("current")


class _Pm124AlmsynthAlmLineIndex_Type(Integer32):
    """Custom type pm124AlmsynthAlmLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124AlmsynthAlmLineIndex_Type.__name__ = "Integer32"
_Pm124AlmsynthAlmLineIndex_Object = MibTableColumn
pm124AlmsynthAlmLineIndex = _Pm124AlmsynthAlmLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 3, 7, 1, 1),
    _Pm124AlmsynthAlmLineIndex_Type()
)
pm124AlmsynthAlmLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmsynthAlmLineIndex.setStatus("current")
_Pm124AlmLineSfpAbsentPortn_Type = EkiOnOff
_Pm124AlmLineSfpAbsentPortn_Object = MibTableColumn
pm124AlmLineSfpAbsentPortn = _Pm124AlmLineSfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 3, 7, 1, 2),
    _Pm124AlmLineSfpAbsentPortn_Type()
)
pm124AlmLineSfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmLineSfpAbsentPortn.setStatus("current")
_Pm124AlmLineDdmAbsentPortn_Type = EkiOnOff
_Pm124AlmLineDdmAbsentPortn_Object = MibTableColumn
pm124AlmLineDdmAbsentPortn = _Pm124AlmLineDdmAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 3, 7, 1, 3),
    _Pm124AlmLineDdmAbsentPortn_Type()
)
pm124AlmLineDdmAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmLineDdmAbsentPortn.setStatus("current")
_Pm124AlmLineHwFailPortn_Type = EkiOnOff
_Pm124AlmLineHwFailPortn_Object = MibTableColumn
pm124AlmLineHwFailPortn = _Pm124AlmLineHwFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 3, 7, 1, 5),
    _Pm124AlmLineHwFailPortn_Type()
)
pm124AlmLineHwFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmLineHwFailPortn.setStatus("current")
_Pm124AlmLineLsdPortn_Type = EkiOnOff
_Pm124AlmLineLsdPortn_Object = MibTableColumn
pm124AlmLineLsdPortn = _Pm124AlmLineLsdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 3, 7, 1, 6),
    _Pm124AlmLineLsdPortn_Type()
)
pm124AlmLineLsdPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmLineLsdPortn.setStatus("current")
_Pm124AlmLineLocalOosPortn_Type = EkiOnOff
_Pm124AlmLineLocalOosPortn_Object = MibTableColumn
pm124AlmLineLocalOosPortn = _Pm124AlmLineLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 3, 7, 1, 7),
    _Pm124AlmLineLocalOosPortn_Type()
)
pm124AlmLineLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmLineLocalOosPortn.setStatus("current")
_Pm124AlmLineDdmWarningPortn_Type = EkiOnOff
_Pm124AlmLineDdmWarningPortn_Object = MibTableColumn
pm124AlmLineDdmWarningPortn = _Pm124AlmLineDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 3, 7, 1, 10),
    _Pm124AlmLineDdmWarningPortn_Type()
)
pm124AlmLineDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmLineDdmWarningPortn.setStatus("current")
_Pm124AlmLineDdmAlmPortn_Type = EkiOnOff
_Pm124AlmLineDdmAlmPortn_Object = MibTableColumn
pm124AlmLineDdmAlmPortn = _Pm124AlmLineDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 3, 7, 1, 11),
    _Pm124AlmLineDdmAlmPortn_Type()
)
pm124AlmLineDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmLineDdmAlmPortn.setStatus("current")
_Pm124AlmLineFailPortn_Type = EkiOnOff
_Pm124AlmLineFailPortn_Object = MibTableColumn
pm124AlmLineFailPortn = _Pm124AlmLineFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 3, 7, 1, 13),
    _Pm124AlmLineFailPortn_Type()
)
pm124AlmLineFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmLineFailPortn.setStatus("current")
_Pm124AlmlineAccessioAlmTable_Object = MibTable
pm124AlmlineAccessioAlmTable = _Pm124AlmlineAccessioAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 3, 64)
)
if mibBuilder.loadTexts:
    pm124AlmlineAccessioAlmTable.setStatus("current")
_Pm124AlmlineAccessioAlmEntry_Object = MibTableRow
pm124AlmlineAccessioAlmEntry = _Pm124AlmlineAccessioAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 3, 64, 1)
)
pm124AlmlineAccessioAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm124-MIB", "pm124AlmlineAccessioAlmIndex"),
)
if mibBuilder.loadTexts:
    pm124AlmlineAccessioAlmEntry.setStatus("current")


class _Pm124AlmlineAccessioAlmIndex_Type(Integer32):
    """Custom type pm124AlmlineAccessioAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124AlmlineAccessioAlmIndex_Type.__name__ = "Integer32"
_Pm124AlmlineAccessioAlmIndex_Object = MibTableColumn
pm124AlmlineAccessioAlmIndex = _Pm124AlmlineAccessioAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 3, 64, 1, 1),
    _Pm124AlmlineAccessioAlmIndex_Type()
)
pm124AlmlineAccessioAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmlineAccessioAlmIndex.setStatus("current")
_Pm124AlmLineLasFailPortn_Type = EkiOnOff
_Pm124AlmLineLasFailPortn_Object = MibTableColumn
pm124AlmLineLasFailPortn = _Pm124AlmLineLasFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 3, 64, 1, 2),
    _Pm124AlmLineLasFailPortn_Type()
)
pm124AlmLineLasFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmLineLasFailPortn.setStatus("current")
_Pm124AlmLineLosPortn_Type = EkiOnOff
_Pm124AlmLineLosPortn_Object = MibTableColumn
pm124AlmLineLosPortn = _Pm124AlmLineLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 3, 64, 1, 5),
    _Pm124AlmLineLosPortn_Type()
)
pm124AlmLineLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmLineLosPortn.setStatus("current")
_Pm124AlmLineLossSyncPortn_Type = EkiOnOff
_Pm124AlmLineLossSyncPortn_Object = MibTableColumn
pm124AlmLineLossSyncPortn = _Pm124AlmLineLossSyncPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 2, 3, 3, 64, 1, 7),
    _Pm124AlmLineLossSyncPortn_Type()
)
pm124AlmLineLossSyncPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124AlmLineLossSyncPortn.setStatus("current")
_Pm124measures_ObjectIdentity = ObjectIdentity
pm124measures = _Pm124measures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3)
)
_Pm124MesrOther_ObjectIdentity = ObjectIdentity
pm124MesrOther = _Pm124MesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 1)
)
_Pm124MesrClient_ObjectIdentity = ObjectIdentity
pm124MesrClient = _Pm124MesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 2)
)
_Pm124MesrclientTemperatureTable_Object = MibTable
pm124MesrclientTemperatureTable = _Pm124MesrclientTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 2, 16)
)
if mibBuilder.loadTexts:
    pm124MesrclientTemperatureTable.setStatus("current")
_Pm124MesrclientTemperatureEntry_Object = MibTableRow
pm124MesrclientTemperatureEntry = _Pm124MesrclientTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 2, 16, 1)
)
pm124MesrclientTemperatureEntry.setIndexNames(
    (0, "EKINOPS-Pm124-MIB", "pm124MesrclientTemperatureIndex"),
)
if mibBuilder.loadTexts:
    pm124MesrclientTemperatureEntry.setStatus("current")


class _Pm124MesrclientTemperatureIndex_Type(Integer32):
    """Custom type pm124MesrclientTemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124MesrclientTemperatureIndex_Type.__name__ = "Integer32"
_Pm124MesrclientTemperatureIndex_Object = MibTableColumn
pm124MesrclientTemperatureIndex = _Pm124MesrclientTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 2, 16, 1, 1),
    _Pm124MesrclientTemperatureIndex_Type()
)
pm124MesrclientTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124MesrclientTemperatureIndex.setStatus("current")


class _Pm124MesrclientTemperaturePortn_Type(Integer32):
    """Custom type pm124MesrclientTemperaturePortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm124MesrclientTemperaturePortn_Type.__name__ = "Integer32"
_Pm124MesrclientTemperaturePortn_Object = MibTableColumn
pm124MesrclientTemperaturePortn = _Pm124MesrclientTemperaturePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 2, 16, 1, 2),
    _Pm124MesrclientTemperaturePortn_Type()
)
pm124MesrclientTemperaturePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124MesrclientTemperaturePortn.setStatus("current")
_Pm124MesrclientVoltTable_Object = MibTable
pm124MesrclientVoltTable = _Pm124MesrclientVoltTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 2, 24)
)
if mibBuilder.loadTexts:
    pm124MesrclientVoltTable.setStatus("current")
_Pm124MesrclientVoltEntry_Object = MibTableRow
pm124MesrclientVoltEntry = _Pm124MesrclientVoltEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 2, 24, 1)
)
pm124MesrclientVoltEntry.setIndexNames(
    (0, "EKINOPS-Pm124-MIB", "pm124MesrclientVoltIndex"),
)
if mibBuilder.loadTexts:
    pm124MesrclientVoltEntry.setStatus("current")


class _Pm124MesrclientVoltIndex_Type(Integer32):
    """Custom type pm124MesrclientVoltIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124MesrclientVoltIndex_Type.__name__ = "Integer32"
_Pm124MesrclientVoltIndex_Object = MibTableColumn
pm124MesrclientVoltIndex = _Pm124MesrclientVoltIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 2, 24, 1, 1),
    _Pm124MesrclientVoltIndex_Type()
)
pm124MesrclientVoltIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124MesrclientVoltIndex.setStatus("current")


class _Pm124MesrclientVoltPortn_Type(Integer32):
    """Custom type pm124MesrclientVoltPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm124MesrclientVoltPortn_Type.__name__ = "Integer32"
_Pm124MesrclientVoltPortn_Object = MibTableColumn
pm124MesrclientVoltPortn = _Pm124MesrclientVoltPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 2, 24, 1, 2),
    _Pm124MesrclientVoltPortn_Type()
)
pm124MesrclientVoltPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124MesrclientVoltPortn.setStatus("current")
_Pm124MesrclientTxBiasTable_Object = MibTable
pm124MesrclientTxBiasTable = _Pm124MesrclientTxBiasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 2, 32)
)
if mibBuilder.loadTexts:
    pm124MesrclientTxBiasTable.setStatus("current")
_Pm124MesrclientTxBiasEntry_Object = MibTableRow
pm124MesrclientTxBiasEntry = _Pm124MesrclientTxBiasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 2, 32, 1)
)
pm124MesrclientTxBiasEntry.setIndexNames(
    (0, "EKINOPS-Pm124-MIB", "pm124MesrclientTxBiasIndex"),
)
if mibBuilder.loadTexts:
    pm124MesrclientTxBiasEntry.setStatus("current")


class _Pm124MesrclientTxBiasIndex_Type(Integer32):
    """Custom type pm124MesrclientTxBiasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124MesrclientTxBiasIndex_Type.__name__ = "Integer32"
_Pm124MesrclientTxBiasIndex_Object = MibTableColumn
pm124MesrclientTxBiasIndex = _Pm124MesrclientTxBiasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 2, 32, 1, 1),
    _Pm124MesrclientTxBiasIndex_Type()
)
pm124MesrclientTxBiasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124MesrclientTxBiasIndex.setStatus("current")


class _Pm124MesrclientTxBiasPortn_Type(Integer32):
    """Custom type pm124MesrclientTxBiasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm124MesrclientTxBiasPortn_Type.__name__ = "Integer32"
_Pm124MesrclientTxBiasPortn_Object = MibTableColumn
pm124MesrclientTxBiasPortn = _Pm124MesrclientTxBiasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 2, 32, 1, 2),
    _Pm124MesrclientTxBiasPortn_Type()
)
pm124MesrclientTxBiasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124MesrclientTxBiasPortn.setStatus("current")
_Pm124MesrclientTxPowerTable_Object = MibTable
pm124MesrclientTxPowerTable = _Pm124MesrclientTxPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 2, 40)
)
if mibBuilder.loadTexts:
    pm124MesrclientTxPowerTable.setStatus("current")
_Pm124MesrclientTxPowerEntry_Object = MibTableRow
pm124MesrclientTxPowerEntry = _Pm124MesrclientTxPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 2, 40, 1)
)
pm124MesrclientTxPowerEntry.setIndexNames(
    (0, "EKINOPS-Pm124-MIB", "pm124MesrclientTxPowerIndex"),
)
if mibBuilder.loadTexts:
    pm124MesrclientTxPowerEntry.setStatus("current")


class _Pm124MesrclientTxPowerIndex_Type(Integer32):
    """Custom type pm124MesrclientTxPowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124MesrclientTxPowerIndex_Type.__name__ = "Integer32"
_Pm124MesrclientTxPowerIndex_Object = MibTableColumn
pm124MesrclientTxPowerIndex = _Pm124MesrclientTxPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 2, 40, 1, 1),
    _Pm124MesrclientTxPowerIndex_Type()
)
pm124MesrclientTxPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124MesrclientTxPowerIndex.setStatus("current")


class _Pm124MesrclientTxPowerPortn_Type(Integer32):
    """Custom type pm124MesrclientTxPowerPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm124MesrclientTxPowerPortn_Type.__name__ = "Integer32"
_Pm124MesrclientTxPowerPortn_Object = MibTableColumn
pm124MesrclientTxPowerPortn = _Pm124MesrclientTxPowerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 2, 40, 1, 2),
    _Pm124MesrclientTxPowerPortn_Type()
)
pm124MesrclientTxPowerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124MesrclientTxPowerPortn.setStatus("current")
_Pm124MesrclientRxPowerTable_Object = MibTable
pm124MesrclientRxPowerTable = _Pm124MesrclientRxPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 2, 48)
)
if mibBuilder.loadTexts:
    pm124MesrclientRxPowerTable.setStatus("current")
_Pm124MesrclientRxPowerEntry_Object = MibTableRow
pm124MesrclientRxPowerEntry = _Pm124MesrclientRxPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 2, 48, 1)
)
pm124MesrclientRxPowerEntry.setIndexNames(
    (0, "EKINOPS-Pm124-MIB", "pm124MesrclientRxPowerIndex"),
)
if mibBuilder.loadTexts:
    pm124MesrclientRxPowerEntry.setStatus("current")


class _Pm124MesrclientRxPowerIndex_Type(Integer32):
    """Custom type pm124MesrclientRxPowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124MesrclientRxPowerIndex_Type.__name__ = "Integer32"
_Pm124MesrclientRxPowerIndex_Object = MibTableColumn
pm124MesrclientRxPowerIndex = _Pm124MesrclientRxPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 2, 48, 1, 1),
    _Pm124MesrclientRxPowerIndex_Type()
)
pm124MesrclientRxPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124MesrclientRxPowerIndex.setStatus("current")


class _Pm124MesrclientRxPowerPortn_Type(Integer32):
    """Custom type pm124MesrclientRxPowerPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm124MesrclientRxPowerPortn_Type.__name__ = "Integer32"
_Pm124MesrclientRxPowerPortn_Object = MibTableColumn
pm124MesrclientRxPowerPortn = _Pm124MesrclientRxPowerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 2, 48, 1, 2),
    _Pm124MesrclientRxPowerPortn_Type()
)
pm124MesrclientRxPowerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124MesrclientRxPowerPortn.setStatus("current")
_Pm124MesrLine_ObjectIdentity = ObjectIdentity
pm124MesrLine = _Pm124MesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 3)
)
_Pm124MesrlineTemperatureTable_Object = MibTable
pm124MesrlineTemperatureTable = _Pm124MesrlineTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 3, 64)
)
if mibBuilder.loadTexts:
    pm124MesrlineTemperatureTable.setStatus("current")
_Pm124MesrlineTemperatureEntry_Object = MibTableRow
pm124MesrlineTemperatureEntry = _Pm124MesrlineTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 3, 64, 1)
)
pm124MesrlineTemperatureEntry.setIndexNames(
    (0, "EKINOPS-Pm124-MIB", "pm124MesrlineTemperatureIndex"),
)
if mibBuilder.loadTexts:
    pm124MesrlineTemperatureEntry.setStatus("current")


class _Pm124MesrlineTemperatureIndex_Type(Integer32):
    """Custom type pm124MesrlineTemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124MesrlineTemperatureIndex_Type.__name__ = "Integer32"
_Pm124MesrlineTemperatureIndex_Object = MibTableColumn
pm124MesrlineTemperatureIndex = _Pm124MesrlineTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 3, 64, 1, 1),
    _Pm124MesrlineTemperatureIndex_Type()
)
pm124MesrlineTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124MesrlineTemperatureIndex.setStatus("current")


class _Pm124MesrlineTemperaturePortn_Type(Integer32):
    """Custom type pm124MesrlineTemperaturePortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm124MesrlineTemperaturePortn_Type.__name__ = "Integer32"
_Pm124MesrlineTemperaturePortn_Object = MibTableColumn
pm124MesrlineTemperaturePortn = _Pm124MesrlineTemperaturePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 3, 64, 1, 2),
    _Pm124MesrlineTemperaturePortn_Type()
)
pm124MesrlineTemperaturePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124MesrlineTemperaturePortn.setStatus("current")
_Pm124MesrlineVoltTable_Object = MibTable
pm124MesrlineVoltTable = _Pm124MesrlineVoltTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 3, 65)
)
if mibBuilder.loadTexts:
    pm124MesrlineVoltTable.setStatus("current")
_Pm124MesrlineVoltEntry_Object = MibTableRow
pm124MesrlineVoltEntry = _Pm124MesrlineVoltEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 3, 65, 1)
)
pm124MesrlineVoltEntry.setIndexNames(
    (0, "EKINOPS-Pm124-MIB", "pm124MesrlineVoltIndex"),
)
if mibBuilder.loadTexts:
    pm124MesrlineVoltEntry.setStatus("current")


class _Pm124MesrlineVoltIndex_Type(Integer32):
    """Custom type pm124MesrlineVoltIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124MesrlineVoltIndex_Type.__name__ = "Integer32"
_Pm124MesrlineVoltIndex_Object = MibTableColumn
pm124MesrlineVoltIndex = _Pm124MesrlineVoltIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 3, 65, 1, 1),
    _Pm124MesrlineVoltIndex_Type()
)
pm124MesrlineVoltIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124MesrlineVoltIndex.setStatus("current")


class _Pm124MesrlineVoltPortn_Type(Integer32):
    """Custom type pm124MesrlineVoltPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm124MesrlineVoltPortn_Type.__name__ = "Integer32"
_Pm124MesrlineVoltPortn_Object = MibTableColumn
pm124MesrlineVoltPortn = _Pm124MesrlineVoltPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 3, 65, 1, 2),
    _Pm124MesrlineVoltPortn_Type()
)
pm124MesrlineVoltPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124MesrlineVoltPortn.setStatus("current")
_Pm124MesrlineTxBiasTable_Object = MibTable
pm124MesrlineTxBiasTable = _Pm124MesrlineTxBiasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 3, 66)
)
if mibBuilder.loadTexts:
    pm124MesrlineTxBiasTable.setStatus("current")
_Pm124MesrlineTxBiasEntry_Object = MibTableRow
pm124MesrlineTxBiasEntry = _Pm124MesrlineTxBiasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 3, 66, 1)
)
pm124MesrlineTxBiasEntry.setIndexNames(
    (0, "EKINOPS-Pm124-MIB", "pm124MesrlineTxBiasIndex"),
)
if mibBuilder.loadTexts:
    pm124MesrlineTxBiasEntry.setStatus("current")


class _Pm124MesrlineTxBiasIndex_Type(Integer32):
    """Custom type pm124MesrlineTxBiasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124MesrlineTxBiasIndex_Type.__name__ = "Integer32"
_Pm124MesrlineTxBiasIndex_Object = MibTableColumn
pm124MesrlineTxBiasIndex = _Pm124MesrlineTxBiasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 3, 66, 1, 1),
    _Pm124MesrlineTxBiasIndex_Type()
)
pm124MesrlineTxBiasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124MesrlineTxBiasIndex.setStatus("current")


class _Pm124MesrlineTxBiasPortn_Type(Integer32):
    """Custom type pm124MesrlineTxBiasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm124MesrlineTxBiasPortn_Type.__name__ = "Integer32"
_Pm124MesrlineTxBiasPortn_Object = MibTableColumn
pm124MesrlineTxBiasPortn = _Pm124MesrlineTxBiasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 3, 66, 1, 2),
    _Pm124MesrlineTxBiasPortn_Type()
)
pm124MesrlineTxBiasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124MesrlineTxBiasPortn.setStatus("current")
_Pm124MesrlineTxPowerTable_Object = MibTable
pm124MesrlineTxPowerTable = _Pm124MesrlineTxPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 3, 67)
)
if mibBuilder.loadTexts:
    pm124MesrlineTxPowerTable.setStatus("current")
_Pm124MesrlineTxPowerEntry_Object = MibTableRow
pm124MesrlineTxPowerEntry = _Pm124MesrlineTxPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 3, 67, 1)
)
pm124MesrlineTxPowerEntry.setIndexNames(
    (0, "EKINOPS-Pm124-MIB", "pm124MesrlineTxPowerIndex"),
)
if mibBuilder.loadTexts:
    pm124MesrlineTxPowerEntry.setStatus("current")


class _Pm124MesrlineTxPowerIndex_Type(Integer32):
    """Custom type pm124MesrlineTxPowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124MesrlineTxPowerIndex_Type.__name__ = "Integer32"
_Pm124MesrlineTxPowerIndex_Object = MibTableColumn
pm124MesrlineTxPowerIndex = _Pm124MesrlineTxPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 3, 67, 1, 1),
    _Pm124MesrlineTxPowerIndex_Type()
)
pm124MesrlineTxPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124MesrlineTxPowerIndex.setStatus("current")


class _Pm124MesrlineTxPowerPortn_Type(Integer32):
    """Custom type pm124MesrlineTxPowerPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm124MesrlineTxPowerPortn_Type.__name__ = "Integer32"
_Pm124MesrlineTxPowerPortn_Object = MibTableColumn
pm124MesrlineTxPowerPortn = _Pm124MesrlineTxPowerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 3, 67, 1, 2),
    _Pm124MesrlineTxPowerPortn_Type()
)
pm124MesrlineTxPowerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124MesrlineTxPowerPortn.setStatus("current")
_Pm124MesrlineRxPowerTable_Object = MibTable
pm124MesrlineRxPowerTable = _Pm124MesrlineRxPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 3, 68)
)
if mibBuilder.loadTexts:
    pm124MesrlineRxPowerTable.setStatus("current")
_Pm124MesrlineRxPowerEntry_Object = MibTableRow
pm124MesrlineRxPowerEntry = _Pm124MesrlineRxPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 3, 68, 1)
)
pm124MesrlineRxPowerEntry.setIndexNames(
    (0, "EKINOPS-Pm124-MIB", "pm124MesrlineRxPowerIndex"),
)
if mibBuilder.loadTexts:
    pm124MesrlineRxPowerEntry.setStatus("current")


class _Pm124MesrlineRxPowerIndex_Type(Integer32):
    """Custom type pm124MesrlineRxPowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124MesrlineRxPowerIndex_Type.__name__ = "Integer32"
_Pm124MesrlineRxPowerIndex_Object = MibTableColumn
pm124MesrlineRxPowerIndex = _Pm124MesrlineRxPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 3, 68, 1, 1),
    _Pm124MesrlineRxPowerIndex_Type()
)
pm124MesrlineRxPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124MesrlineRxPowerIndex.setStatus("current")


class _Pm124MesrlineRxPowerPortn_Type(Integer32):
    """Custom type pm124MesrlineRxPowerPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm124MesrlineRxPowerPortn_Type.__name__ = "Integer32"
_Pm124MesrlineRxPowerPortn_Object = MibTableColumn
pm124MesrlineRxPowerPortn = _Pm124MesrlineRxPowerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 3, 3, 68, 1, 2),
    _Pm124MesrlineRxPowerPortn_Type()
)
pm124MesrlineRxPowerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124MesrlineRxPowerPortn.setStatus("current")
_Pm124counters_ObjectIdentity = ObjectIdentity
pm124counters = _Pm124counters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 4)
)
_Pm124CntOther_ObjectIdentity = ObjectIdentity
pm124CntOther = _Pm124CntOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 4, 1)
)
_Pm124CntClient_ObjectIdentity = ObjectIdentity
pm124CntClient = _Pm124CntClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 4, 2)
)
_Pm124CntclientCbipErrCntTable_Object = MibTable
pm124CntclientCbipErrCntTable = _Pm124CntclientCbipErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 4, 2, 16)
)
if mibBuilder.loadTexts:
    pm124CntclientCbipErrCntTable.setStatus("current")
_Pm124CntclientCbipErrCntEntry_Object = MibTableRow
pm124CntclientCbipErrCntEntry = _Pm124CntclientCbipErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 4, 2, 16, 1)
)
pm124CntclientCbipErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pm124-MIB", "pm124CntclientCbipErrCntIndex"),
)
if mibBuilder.loadTexts:
    pm124CntclientCbipErrCntEntry.setStatus("current")


class _Pm124CntclientCbipErrCntIndex_Type(Integer32):
    """Custom type pm124CntclientCbipErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124CntclientCbipErrCntIndex_Type.__name__ = "Integer32"
_Pm124CntclientCbipErrCntIndex_Object = MibTableColumn
pm124CntclientCbipErrCntIndex = _Pm124CntclientCbipErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 4, 2, 16, 1, 1),
    _Pm124CntclientCbipErrCntIndex_Type()
)
pm124CntclientCbipErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124CntclientCbipErrCntIndex.setStatus("current")
_Pm124CntclientCbipErrCntValuePortn_Type = Counter32
_Pm124CntclientCbipErrCntValuePortn_Object = MibTableColumn
pm124CntclientCbipErrCntValuePortn = _Pm124CntclientCbipErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 4, 2, 16, 1, 2),
    _Pm124CntclientCbipErrCntValuePortn_Type()
)
pm124CntclientCbipErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124CntclientCbipErrCntValuePortn.setStatus("current")
_Pm124CntclientCbipErrCntErrorPortn_Type = EkiOnOff
_Pm124CntclientCbipErrCntErrorPortn_Object = MibTableColumn
pm124CntclientCbipErrCntErrorPortn = _Pm124CntclientCbipErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 4, 2, 16, 1, 3),
    _Pm124CntclientCbipErrCntErrorPortn_Type()
)
pm124CntclientCbipErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124CntclientCbipErrCntErrorPortn.setStatus("current")
_Pm124CntclientCbipErrCntOverloadPortn_Type = EkiOnOff
_Pm124CntclientCbipErrCntOverloadPortn_Object = MibTableColumn
pm124CntclientCbipErrCntOverloadPortn = _Pm124CntclientCbipErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 4, 2, 16, 1, 4),
    _Pm124CntclientCbipErrCntOverloadPortn_Type()
)
pm124CntclientCbipErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124CntclientCbipErrCntOverloadPortn.setStatus("current")
_Pm124CntclientB1ErrCntTable_Object = MibTable
pm124CntclientB1ErrCntTable = _Pm124CntclientB1ErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 4, 2, 24)
)
if mibBuilder.loadTexts:
    pm124CntclientB1ErrCntTable.setStatus("current")
_Pm124CntclientB1ErrCntEntry_Object = MibTableRow
pm124CntclientB1ErrCntEntry = _Pm124CntclientB1ErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 4, 2, 24, 1)
)
pm124CntclientB1ErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pm124-MIB", "pm124CntclientB1ErrCntIndex"),
)
if mibBuilder.loadTexts:
    pm124CntclientB1ErrCntEntry.setStatus("current")


class _Pm124CntclientB1ErrCntIndex_Type(Integer32):
    """Custom type pm124CntclientB1ErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124CntclientB1ErrCntIndex_Type.__name__ = "Integer32"
_Pm124CntclientB1ErrCntIndex_Object = MibTableColumn
pm124CntclientB1ErrCntIndex = _Pm124CntclientB1ErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 4, 2, 24, 1, 1),
    _Pm124CntclientB1ErrCntIndex_Type()
)
pm124CntclientB1ErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124CntclientB1ErrCntIndex.setStatus("current")
_Pm124CntclientB1ErrCntValuePortn_Type = Counter32
_Pm124CntclientB1ErrCntValuePortn_Object = MibTableColumn
pm124CntclientB1ErrCntValuePortn = _Pm124CntclientB1ErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 4, 2, 24, 1, 2),
    _Pm124CntclientB1ErrCntValuePortn_Type()
)
pm124CntclientB1ErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124CntclientB1ErrCntValuePortn.setStatus("current")
_Pm124CntclientB1ErrCntErrorPortn_Type = EkiOnOff
_Pm124CntclientB1ErrCntErrorPortn_Object = MibTableColumn
pm124CntclientB1ErrCntErrorPortn = _Pm124CntclientB1ErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 4, 2, 24, 1, 3),
    _Pm124CntclientB1ErrCntErrorPortn_Type()
)
pm124CntclientB1ErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124CntclientB1ErrCntErrorPortn.setStatus("current")
_Pm124CntclientB1ErrCntOverloadPortn_Type = EkiOnOff
_Pm124CntclientB1ErrCntOverloadPortn_Object = MibTableColumn
pm124CntclientB1ErrCntOverloadPortn = _Pm124CntclientB1ErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 4, 2, 24, 1, 4),
    _Pm124CntclientB1ErrCntOverloadPortn_Type()
)
pm124CntclientB1ErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124CntclientB1ErrCntOverloadPortn.setStatus("current")
_Pm124CntLine_ObjectIdentity = ObjectIdentity
pm124CntLine = _Pm124CntLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 4, 3)
)
_Pm124CntlineDispErrCntTable_Object = MibTable
pm124CntlineDispErrCntTable = _Pm124CntlineDispErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 4, 3, 64)
)
if mibBuilder.loadTexts:
    pm124CntlineDispErrCntTable.setStatus("current")
_Pm124CntlineDispErrCntEntry_Object = MibTableRow
pm124CntlineDispErrCntEntry = _Pm124CntlineDispErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 4, 3, 64, 1)
)
pm124CntlineDispErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pm124-MIB", "pm124CntlineDispErrCntIndex"),
)
if mibBuilder.loadTexts:
    pm124CntlineDispErrCntEntry.setStatus("current")


class _Pm124CntlineDispErrCntIndex_Type(Integer32):
    """Custom type pm124CntlineDispErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124CntlineDispErrCntIndex_Type.__name__ = "Integer32"
_Pm124CntlineDispErrCntIndex_Object = MibTableColumn
pm124CntlineDispErrCntIndex = _Pm124CntlineDispErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 4, 3, 64, 1, 1),
    _Pm124CntlineDispErrCntIndex_Type()
)
pm124CntlineDispErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124CntlineDispErrCntIndex.setStatus("current")
_Pm124CntlineDispErrCntValuePortn_Type = Counter32
_Pm124CntlineDispErrCntValuePortn_Object = MibTableColumn
pm124CntlineDispErrCntValuePortn = _Pm124CntlineDispErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 4, 3, 64, 1, 2),
    _Pm124CntlineDispErrCntValuePortn_Type()
)
pm124CntlineDispErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124CntlineDispErrCntValuePortn.setStatus("current")
_Pm124CntlineDispErrCntErrorPortn_Type = EkiOnOff
_Pm124CntlineDispErrCntErrorPortn_Object = MibTableColumn
pm124CntlineDispErrCntErrorPortn = _Pm124CntlineDispErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 4, 3, 64, 1, 3),
    _Pm124CntlineDispErrCntErrorPortn_Type()
)
pm124CntlineDispErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124CntlineDispErrCntErrorPortn.setStatus("current")
_Pm124CntlineDispErrCntOverloadPortn_Type = EkiOnOff
_Pm124CntlineDispErrCntOverloadPortn_Object = MibTableColumn
pm124CntlineDispErrCntOverloadPortn = _Pm124CntlineDispErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 4, 3, 64, 1, 4),
    _Pm124CntlineDispErrCntOverloadPortn_Type()
)
pm124CntlineDispErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124CntlineDispErrCntOverloadPortn.setStatus("current")
_Pm124CntlineCrcErrCntTable_Object = MibTable
pm124CntlineCrcErrCntTable = _Pm124CntlineCrcErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 4, 3, 65)
)
if mibBuilder.loadTexts:
    pm124CntlineCrcErrCntTable.setStatus("current")
_Pm124CntlineCrcErrCntEntry_Object = MibTableRow
pm124CntlineCrcErrCntEntry = _Pm124CntlineCrcErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 4, 3, 65, 1)
)
pm124CntlineCrcErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pm124-MIB", "pm124CntlineCrcErrCntIndex"),
)
if mibBuilder.loadTexts:
    pm124CntlineCrcErrCntEntry.setStatus("current")


class _Pm124CntlineCrcErrCntIndex_Type(Integer32):
    """Custom type pm124CntlineCrcErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124CntlineCrcErrCntIndex_Type.__name__ = "Integer32"
_Pm124CntlineCrcErrCntIndex_Object = MibTableColumn
pm124CntlineCrcErrCntIndex = _Pm124CntlineCrcErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 4, 3, 65, 1, 1),
    _Pm124CntlineCrcErrCntIndex_Type()
)
pm124CntlineCrcErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124CntlineCrcErrCntIndex.setStatus("current")
_Pm124CntlineCrcErrCntValuePortn_Type = Counter32
_Pm124CntlineCrcErrCntValuePortn_Object = MibTableColumn
pm124CntlineCrcErrCntValuePortn = _Pm124CntlineCrcErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 4, 3, 65, 1, 2),
    _Pm124CntlineCrcErrCntValuePortn_Type()
)
pm124CntlineCrcErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124CntlineCrcErrCntValuePortn.setStatus("current")
_Pm124CntlineCrcErrCntErrorPortn_Type = EkiOnOff
_Pm124CntlineCrcErrCntErrorPortn_Object = MibTableColumn
pm124CntlineCrcErrCntErrorPortn = _Pm124CntlineCrcErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 4, 3, 65, 1, 3),
    _Pm124CntlineCrcErrCntErrorPortn_Type()
)
pm124CntlineCrcErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124CntlineCrcErrCntErrorPortn.setStatus("current")
_Pm124CntlineCrcErrCntOverloadPortn_Type = EkiOnOff
_Pm124CntlineCrcErrCntOverloadPortn_Object = MibTableColumn
pm124CntlineCrcErrCntOverloadPortn = _Pm124CntlineCrcErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 4, 3, 65, 1, 4),
    _Pm124CntlineCrcErrCntOverloadPortn_Type()
)
pm124CntlineCrcErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124CntlineCrcErrCntOverloadPortn.setStatus("current")
_Pm124CntCountersReset_Type = EkiOnOff
_Pm124CntCountersReset_Object = MibScalar
pm124CntCountersReset = _Pm124CntCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 4, 259),
    _Pm124CntCountersReset_Type()
)
pm124CntCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124CntCountersReset.setStatus("current")
_Pm124CntCountersStop_Type = EkiOnOff
_Pm124CntCountersStop_Object = MibScalar
pm124CntCountersStop = _Pm124CntCountersStop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 4, 260),
    _Pm124CntCountersStop_Type()
)
pm124CntCountersStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124CntCountersStop.setStatus("current")
_Pm124controlsWrite_ObjectIdentity = ObjectIdentity
pm124controlsWrite = _Pm124controlsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6)
)
_Pm124CtrlOther_ObjectIdentity = ObjectIdentity
pm124CtrlOther = _Pm124CtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 1)
)
_Pm124Ctrlsynth0_ObjectIdentity = ObjectIdentity
pm124Ctrlsynth0 = _Pm124Ctrlsynth0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 1, 0)
)
_Pm124CtrlConfLoad_Type = EkiOnOff
_Pm124CtrlConfLoad_Object = MibScalar
pm124CtrlConfLoad = _Pm124CtrlConfLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 1, 0, 1),
    _Pm124CtrlConfLoad_Type()
)
pm124CtrlConfLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124CtrlConfLoad.setStatus("current")
_Pm124CtrlConfFlash_Type = EkiOnOff
_Pm124CtrlConfFlash_Object = MibScalar
pm124CtrlConfFlash = _Pm124CtrlConfFlash_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 1, 0, 9),
    _Pm124CtrlConfFlash_Type()
)
pm124CtrlConfFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124CtrlConfFlash.setStatus("current")
_Pm124CtrlConfClear_Type = EkiOnOff
_Pm124CtrlConfClear_Object = MibScalar
pm124CtrlConfClear = _Pm124CtrlConfClear_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 1, 0, 13),
    _Pm124CtrlConfClear_Type()
)
pm124CtrlConfClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124CtrlConfClear.setStatus("current")
_Pm124Ctrlsynth4_ObjectIdentity = ObjectIdentity
pm124Ctrlsynth4 = _Pm124Ctrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 1, 4)
)
_Pm124CtrlCorrelatOn_Type = EkiOnOff
_Pm124CtrlCorrelatOn_Object = MibScalar
pm124CtrlCorrelatOn = _Pm124CtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 1, 4, 1),
    _Pm124CtrlCorrelatOn_Type()
)
pm124CtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124CtrlCorrelatOn.setStatus("current")
_Pm124CtrlCorrelatOff_Type = EkiOnOff
_Pm124CtrlCorrelatOff_Object = MibScalar
pm124CtrlCorrelatOff = _Pm124CtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 1, 4, 2),
    _Pm124CtrlCorrelatOff_Type()
)
pm124CtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124CtrlCorrelatOff.setStatus("current")
_Pm124CtrlswMgnt_ObjectIdentity = ObjectIdentity
pm124CtrlswMgnt = _Pm124CtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 1, 5)
)
_Pm124CtrlColdReset_Type = EkiOnOff
_Pm124CtrlColdReset_Object = MibScalar
pm124CtrlColdReset = _Pm124CtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 1, 5, 2),
    _Pm124CtrlColdReset_Type()
)
pm124CtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124CtrlColdReset.setStatus("current")
_Pm124CtrlWarmReset_Type = EkiOnOff
_Pm124CtrlWarmReset_Object = MibScalar
pm124CtrlWarmReset = _Pm124CtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 1, 5, 3),
    _Pm124CtrlWarmReset_Type()
)
pm124CtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124CtrlWarmReset.setStatus("current")
_Pm124Ctrlprotocol_Type = EkiProtocol
_Pm124Ctrlprotocol_Object = MibScalar
pm124Ctrlprotocol = _Pm124Ctrlprotocol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 1, 41),
    _Pm124Ctrlprotocol_Type()
)
pm124Ctrlprotocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124Ctrlprotocol.setStatus("current")
_Pm124CtrlledTest_ObjectIdentity = ObjectIdentity
pm124CtrlledTest = _Pm124CtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 1, 72)
)
_Pm124CtrlGreenLed_Type = EkiOnOff
_Pm124CtrlGreenLed_Object = MibScalar
pm124CtrlGreenLed = _Pm124CtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 1, 72, 1),
    _Pm124CtrlGreenLed_Type()
)
pm124CtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124CtrlGreenLed.setStatus("current")
_Pm124CtrlRedLed_Type = EkiOnOff
_Pm124CtrlRedLed_Object = MibScalar
pm124CtrlRedLed = _Pm124CtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 1, 72, 2),
    _Pm124CtrlRedLed_Type()
)
pm124CtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124CtrlRedLed.setStatus("current")
_Pm124CtrlLedOff_Type = EkiOnOff
_Pm124CtrlLedOff_Object = MibScalar
pm124CtrlLedOff = _Pm124CtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 1, 72, 3),
    _Pm124CtrlLedOff_Type()
)
pm124CtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124CtrlLedOff.setStatus("current")
_Pm124CtrlmoduleOosMode_ObjectIdentity = ObjectIdentity
pm124CtrlmoduleOosMode = _Pm124CtrlmoduleOosMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 1, 73)
)
_Pm124CtrlModuleOosMode_Type = EkiOnOff
_Pm124CtrlModuleOosMode_Object = MibScalar
pm124CtrlModuleOosMode = _Pm124CtrlModuleOosMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 1, 73, 1),
    _Pm124CtrlModuleOosMode_Type()
)
pm124CtrlModuleOosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124CtrlModuleOosMode.setStatus("current")
_Pm124CtrlClient_ObjectIdentity = ObjectIdentity
pm124CtrlClient = _Pm124CtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 2)
)
_Pm124CtrlclientSfpOnoffTable_Object = MibTable
pm124CtrlclientSfpOnoffTable = _Pm124CtrlclientSfpOnoffTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 2, 16)
)
if mibBuilder.loadTexts:
    pm124CtrlclientSfpOnoffTable.setStatus("current")
_Pm124CtrlclientSfpOnoffEntry_Object = MibTableRow
pm124CtrlclientSfpOnoffEntry = _Pm124CtrlclientSfpOnoffEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 2, 16, 1)
)
pm124CtrlclientSfpOnoffEntry.setIndexNames(
    (0, "EKINOPS-Pm124-MIB", "pm124CtrlclientSfpOnoffIndex"),
)
if mibBuilder.loadTexts:
    pm124CtrlclientSfpOnoffEntry.setStatus("current")


class _Pm124CtrlclientSfpOnoffIndex_Type(Integer32):
    """Custom type pm124CtrlclientSfpOnoffIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124CtrlclientSfpOnoffIndex_Type.__name__ = "Integer32"
_Pm124CtrlclientSfpOnoffIndex_Object = MibTableColumn
pm124CtrlclientSfpOnoffIndex = _Pm124CtrlclientSfpOnoffIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 2, 16, 1, 1),
    _Pm124CtrlclientSfpOnoffIndex_Type()
)
pm124CtrlclientSfpOnoffIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124CtrlclientSfpOnoffIndex.setStatus("current")
_Pm124CtrlclientSfpOnoffPortn_Type = EkiState
_Pm124CtrlclientSfpOnoffPortn_Object = MibTableColumn
pm124CtrlclientSfpOnoffPortn = _Pm124CtrlclientSfpOnoffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 2, 16, 1, 2),
    _Pm124CtrlclientSfpOnoffPortn_Type()
)
pm124CtrlclientSfpOnoffPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124CtrlclientSfpOnoffPortn.setStatus("current")
_Pm124CtrlclientLoopTable_Object = MibTable
pm124CtrlclientLoopTable = _Pm124CtrlclientLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 2, 17)
)
if mibBuilder.loadTexts:
    pm124CtrlclientLoopTable.setStatus("current")
_Pm124CtrlclientLoopEntry_Object = MibTableRow
pm124CtrlclientLoopEntry = _Pm124CtrlclientLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 2, 17, 1)
)
pm124CtrlclientLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm124-MIB", "pm124CtrlclientLoopIndex"),
)
if mibBuilder.loadTexts:
    pm124CtrlclientLoopEntry.setStatus("current")


class _Pm124CtrlclientLoopIndex_Type(Integer32):
    """Custom type pm124CtrlclientLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124CtrlclientLoopIndex_Type.__name__ = "Integer32"
_Pm124CtrlclientLoopIndex_Object = MibTableColumn
pm124CtrlclientLoopIndex = _Pm124CtrlclientLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 2, 17, 1, 1),
    _Pm124CtrlclientLoopIndex_Type()
)
pm124CtrlclientLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124CtrlclientLoopIndex.setStatus("current")
_Pm124CtrlclientLoopPortn_Type = EkiState
_Pm124CtrlclientLoopPortn_Object = MibTableColumn
pm124CtrlclientLoopPortn = _Pm124CtrlclientLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 2, 17, 1, 2),
    _Pm124CtrlclientLoopPortn_Type()
)
pm124CtrlclientLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124CtrlclientLoopPortn.setStatus("current")
_Pm124CtrlclientCsfUpInsertTable_Object = MibTable
pm124CtrlclientCsfUpInsertTable = _Pm124CtrlclientCsfUpInsertTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 2, 18)
)
if mibBuilder.loadTexts:
    pm124CtrlclientCsfUpInsertTable.setStatus("current")
_Pm124CtrlclientCsfUpInsertEntry_Object = MibTableRow
pm124CtrlclientCsfUpInsertEntry = _Pm124CtrlclientCsfUpInsertEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 2, 18, 1)
)
pm124CtrlclientCsfUpInsertEntry.setIndexNames(
    (0, "EKINOPS-Pm124-MIB", "pm124CtrlclientCsfUpInsertIndex"),
)
if mibBuilder.loadTexts:
    pm124CtrlclientCsfUpInsertEntry.setStatus("current")


class _Pm124CtrlclientCsfUpInsertIndex_Type(Integer32):
    """Custom type pm124CtrlclientCsfUpInsertIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124CtrlclientCsfUpInsertIndex_Type.__name__ = "Integer32"
_Pm124CtrlclientCsfUpInsertIndex_Object = MibTableColumn
pm124CtrlclientCsfUpInsertIndex = _Pm124CtrlclientCsfUpInsertIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 2, 18, 1, 1),
    _Pm124CtrlclientCsfUpInsertIndex_Type()
)
pm124CtrlclientCsfUpInsertIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124CtrlclientCsfUpInsertIndex.setStatus("current")
_Pm124CtrlclientCsfUpInsertPortn_Type = EkiState
_Pm124CtrlclientCsfUpInsertPortn_Object = MibTableColumn
pm124CtrlclientCsfUpInsertPortn = _Pm124CtrlclientCsfUpInsertPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 2, 18, 1, 2),
    _Pm124CtrlclientCsfUpInsertPortn_Type()
)
pm124CtrlclientCsfUpInsertPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124CtrlclientCsfUpInsertPortn.setStatus("current")
_Pm124CtrlclientCaisDwInsertTable_Object = MibTable
pm124CtrlclientCaisDwInsertTable = _Pm124CtrlclientCaisDwInsertTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 2, 19)
)
if mibBuilder.loadTexts:
    pm124CtrlclientCaisDwInsertTable.setStatus("current")
_Pm124CtrlclientCaisDwInsertEntry_Object = MibTableRow
pm124CtrlclientCaisDwInsertEntry = _Pm124CtrlclientCaisDwInsertEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 2, 19, 1)
)
pm124CtrlclientCaisDwInsertEntry.setIndexNames(
    (0, "EKINOPS-Pm124-MIB", "pm124CtrlclientCaisDwInsertIndex"),
)
if mibBuilder.loadTexts:
    pm124CtrlclientCaisDwInsertEntry.setStatus("current")


class _Pm124CtrlclientCaisDwInsertIndex_Type(Integer32):
    """Custom type pm124CtrlclientCaisDwInsertIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124CtrlclientCaisDwInsertIndex_Type.__name__ = "Integer32"
_Pm124CtrlclientCaisDwInsertIndex_Object = MibTableColumn
pm124CtrlclientCaisDwInsertIndex = _Pm124CtrlclientCaisDwInsertIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 2, 19, 1, 1),
    _Pm124CtrlclientCaisDwInsertIndex_Type()
)
pm124CtrlclientCaisDwInsertIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124CtrlclientCaisDwInsertIndex.setStatus("current")
_Pm124CtrlclientCaisDwInsertPortn_Type = EkiState
_Pm124CtrlclientCaisDwInsertPortn_Object = MibTableColumn
pm124CtrlclientCaisDwInsertPortn = _Pm124CtrlclientCaisDwInsertPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 2, 19, 1, 2),
    _Pm124CtrlclientCaisDwInsertPortn_Type()
)
pm124CtrlclientCaisDwInsertPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124CtrlclientCaisDwInsertPortn.setStatus("current")
_Pm124CtrlclientOosModeTable_Object = MibTable
pm124CtrlclientOosModeTable = _Pm124CtrlclientOosModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 2, 20)
)
if mibBuilder.loadTexts:
    pm124CtrlclientOosModeTable.setStatus("current")
_Pm124CtrlclientOosModeEntry_Object = MibTableRow
pm124CtrlclientOosModeEntry = _Pm124CtrlclientOosModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 2, 20, 1)
)
pm124CtrlclientOosModeEntry.setIndexNames(
    (0, "EKINOPS-Pm124-MIB", "pm124CtrlclientOosModeIndex"),
)
if mibBuilder.loadTexts:
    pm124CtrlclientOosModeEntry.setStatus("current")


class _Pm124CtrlclientOosModeIndex_Type(Integer32):
    """Custom type pm124CtrlclientOosModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124CtrlclientOosModeIndex_Type.__name__ = "Integer32"
_Pm124CtrlclientOosModeIndex_Object = MibTableColumn
pm124CtrlclientOosModeIndex = _Pm124CtrlclientOosModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 2, 20, 1, 1),
    _Pm124CtrlclientOosModeIndex_Type()
)
pm124CtrlclientOosModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124CtrlclientOosModeIndex.setStatus("current")
_Pm124CtrlclientOosModePortn_Type = EkiState
_Pm124CtrlclientOosModePortn_Object = MibTableColumn
pm124CtrlclientOosModePortn = _Pm124CtrlclientOosModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 2, 20, 1, 2),
    _Pm124CtrlclientOosModePortn_Type()
)
pm124CtrlclientOosModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124CtrlclientOosModePortn.setStatus("current")
_Pm124CtrlclientAccessTermLoopTable_Object = MibTable
pm124CtrlclientAccessTermLoopTable = _Pm124CtrlclientAccessTermLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 2, 21)
)
if mibBuilder.loadTexts:
    pm124CtrlclientAccessTermLoopTable.setStatus("current")
_Pm124CtrlclientAccessTermLoopEntry_Object = MibTableRow
pm124CtrlclientAccessTermLoopEntry = _Pm124CtrlclientAccessTermLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 2, 21, 1)
)
pm124CtrlclientAccessTermLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm124-MIB", "pm124CtrlclientAccessTermLoopIndex"),
)
if mibBuilder.loadTexts:
    pm124CtrlclientAccessTermLoopEntry.setStatus("current")


class _Pm124CtrlclientAccessTermLoopIndex_Type(Integer32):
    """Custom type pm124CtrlclientAccessTermLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124CtrlclientAccessTermLoopIndex_Type.__name__ = "Integer32"
_Pm124CtrlclientAccessTermLoopIndex_Object = MibTableColumn
pm124CtrlclientAccessTermLoopIndex = _Pm124CtrlclientAccessTermLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 2, 21, 1, 1),
    _Pm124CtrlclientAccessTermLoopIndex_Type()
)
pm124CtrlclientAccessTermLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124CtrlclientAccessTermLoopIndex.setStatus("current")
_Pm124CtrlclientAccessTermLoopPortn_Type = EkiState
_Pm124CtrlclientAccessTermLoopPortn_Object = MibTableColumn
pm124CtrlclientAccessTermLoopPortn = _Pm124CtrlclientAccessTermLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 2, 21, 1, 2),
    _Pm124CtrlclientAccessTermLoopPortn_Type()
)
pm124CtrlclientAccessTermLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124CtrlclientAccessTermLoopPortn.setStatus("current")
_Pm124CtrlLine_ObjectIdentity = ObjectIdentity
pm124CtrlLine = _Pm124CtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 3)
)
_Pm124CtrllineSfpOnoffTable_Object = MibTable
pm124CtrllineSfpOnoffTable = _Pm124CtrllineSfpOnoffTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 3, 64)
)
if mibBuilder.loadTexts:
    pm124CtrllineSfpOnoffTable.setStatus("current")
_Pm124CtrllineSfpOnoffEntry_Object = MibTableRow
pm124CtrllineSfpOnoffEntry = _Pm124CtrllineSfpOnoffEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 3, 64, 1)
)
pm124CtrllineSfpOnoffEntry.setIndexNames(
    (0, "EKINOPS-Pm124-MIB", "pm124CtrllineSfpOnoffIndex"),
)
if mibBuilder.loadTexts:
    pm124CtrllineSfpOnoffEntry.setStatus("current")


class _Pm124CtrllineSfpOnoffIndex_Type(Integer32):
    """Custom type pm124CtrllineSfpOnoffIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124CtrllineSfpOnoffIndex_Type.__name__ = "Integer32"
_Pm124CtrllineSfpOnoffIndex_Object = MibTableColumn
pm124CtrllineSfpOnoffIndex = _Pm124CtrllineSfpOnoffIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 3, 64, 1, 1),
    _Pm124CtrllineSfpOnoffIndex_Type()
)
pm124CtrllineSfpOnoffIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124CtrllineSfpOnoffIndex.setStatus("current")
_Pm124CtrllineSfpOnoffPortn_Type = EkiState
_Pm124CtrllineSfpOnoffPortn_Object = MibTableColumn
pm124CtrllineSfpOnoffPortn = _Pm124CtrllineSfpOnoffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 3, 64, 1, 2),
    _Pm124CtrllineSfpOnoffPortn_Type()
)
pm124CtrllineSfpOnoffPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124CtrllineSfpOnoffPortn.setStatus("current")
_Pm124CtrllineOosModeTable_Object = MibTable
pm124CtrllineOosModeTable = _Pm124CtrllineOosModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 3, 65)
)
if mibBuilder.loadTexts:
    pm124CtrllineOosModeTable.setStatus("current")
_Pm124CtrllineOosModeEntry_Object = MibTableRow
pm124CtrllineOosModeEntry = _Pm124CtrllineOosModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 3, 65, 1)
)
pm124CtrllineOosModeEntry.setIndexNames(
    (0, "EKINOPS-Pm124-MIB", "pm124CtrllineOosModeIndex"),
)
if mibBuilder.loadTexts:
    pm124CtrllineOosModeEntry.setStatus("current")


class _Pm124CtrllineOosModeIndex_Type(Integer32):
    """Custom type pm124CtrllineOosModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124CtrllineOosModeIndex_Type.__name__ = "Integer32"
_Pm124CtrllineOosModeIndex_Object = MibTableColumn
pm124CtrllineOosModeIndex = _Pm124CtrllineOosModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 3, 65, 1, 1),
    _Pm124CtrllineOosModeIndex_Type()
)
pm124CtrllineOosModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124CtrllineOosModeIndex.setStatus("current")
_Pm124CtrllineOosModePortn_Type = EkiState
_Pm124CtrllineOosModePortn_Object = MibTableColumn
pm124CtrllineOosModePortn = _Pm124CtrllineOosModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 3, 65, 1, 2),
    _Pm124CtrllineOosModePortn_Type()
)
pm124CtrllineOosModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124CtrllineOosModePortn.setStatus("current")
_Pm124CtrllineLoopTable_Object = MibTable
pm124CtrllineLoopTable = _Pm124CtrllineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 3, 66)
)
if mibBuilder.loadTexts:
    pm124CtrllineLoopTable.setStatus("current")
_Pm124CtrllineLoopEntry_Object = MibTableRow
pm124CtrllineLoopEntry = _Pm124CtrllineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 3, 66, 1)
)
pm124CtrllineLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm124-MIB", "pm124CtrllineLoopIndex"),
)
if mibBuilder.loadTexts:
    pm124CtrllineLoopEntry.setStatus("current")


class _Pm124CtrllineLoopIndex_Type(Integer32):
    """Custom type pm124CtrllineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124CtrllineLoopIndex_Type.__name__ = "Integer32"
_Pm124CtrllineLoopIndex_Object = MibTableColumn
pm124CtrllineLoopIndex = _Pm124CtrllineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 3, 66, 1, 1),
    _Pm124CtrllineLoopIndex_Type()
)
pm124CtrllineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124CtrllineLoopIndex.setStatus("current")
_Pm124CtrllineLoopPortn_Type = EkiState
_Pm124CtrllineLoopPortn_Object = MibTableColumn
pm124CtrllineLoopPortn = _Pm124CtrllineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 3, 66, 1, 2),
    _Pm124CtrllineLoopPortn_Type()
)
pm124CtrllineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124CtrllineLoopPortn.setStatus("current")
_Pm124CtrllineLoopTerminalTable_Object = MibTable
pm124CtrllineLoopTerminalTable = _Pm124CtrllineLoopTerminalTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 3, 67)
)
if mibBuilder.loadTexts:
    pm124CtrllineLoopTerminalTable.setStatus("current")
_Pm124CtrllineLoopTerminalEntry_Object = MibTableRow
pm124CtrllineLoopTerminalEntry = _Pm124CtrllineLoopTerminalEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 3, 67, 1)
)
pm124CtrllineLoopTerminalEntry.setIndexNames(
    (0, "EKINOPS-Pm124-MIB", "pm124CtrllineLoopTerminalIndex"),
)
if mibBuilder.loadTexts:
    pm124CtrllineLoopTerminalEntry.setStatus("current")


class _Pm124CtrllineLoopTerminalIndex_Type(Integer32):
    """Custom type pm124CtrllineLoopTerminalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124CtrllineLoopTerminalIndex_Type.__name__ = "Integer32"
_Pm124CtrllineLoopTerminalIndex_Object = MibTableColumn
pm124CtrllineLoopTerminalIndex = _Pm124CtrllineLoopTerminalIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 3, 67, 1, 1),
    _Pm124CtrllineLoopTerminalIndex_Type()
)
pm124CtrllineLoopTerminalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124CtrllineLoopTerminalIndex.setStatus("current")
_Pm124CtrllineLoopTerminalPortn_Type = EkiState
_Pm124CtrllineLoopTerminalPortn_Object = MibTableColumn
pm124CtrllineLoopTerminalPortn = _Pm124CtrllineLoopTerminalPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 6, 3, 67, 1, 2),
    _Pm124CtrllineLoopTerminalPortn_Type()
)
pm124CtrllineLoopTerminalPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124CtrllineLoopTerminalPortn.setStatus("current")
_Pm124ri_ObjectIdentity = ObjectIdentity
pm124ri = _Pm124ri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 7)
)
_Pm124riTable_ObjectIdentity = ObjectIdentity
pm124riTable = _Pm124riTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 7, 1)
)
_Pm124RinvClientTable_Object = MibTable
pm124RinvClientTable = _Pm124RinvClientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 7, 1, 1)
)
if mibBuilder.loadTexts:
    pm124RinvClientTable.setStatus("current")
_Pm124RinvClientEntry_Object = MibTableRow
pm124RinvClientEntry = _Pm124RinvClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 7, 1, 1, 1)
)
pm124RinvClientEntry.setIndexNames(
    (0, "EKINOPS-Pm124-MIB", "pm124RinvClientIndex"),
)
if mibBuilder.loadTexts:
    pm124RinvClientEntry.setStatus("current")


class _Pm124RinvClientIndex_Type(Integer32):
    """Custom type pm124RinvClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm124RinvClientIndex_Type.__name__ = "Integer32"
_Pm124RinvClientIndex_Object = MibTableColumn
pm124RinvClientIndex = _Pm124RinvClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 7, 1, 1, 1, 1),
    _Pm124RinvClientIndex_Type()
)
pm124RinvClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124RinvClientIndex.setStatus("current")
_Pm124RinvSfpClient_Type = DisplayString
_Pm124RinvSfpClient_Object = MibTableColumn
pm124RinvSfpClient = _Pm124RinvSfpClient_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 7, 1, 1, 1, 2),
    _Pm124RinvSfpClient_Type()
)
pm124RinvSfpClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124RinvSfpClient.setStatus("current")
_Pm124RinvLineTable_Object = MibTable
pm124RinvLineTable = _Pm124RinvLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pm124RinvLineTable.setStatus("current")
_Pm124RinvLineEntry_Object = MibTableRow
pm124RinvLineEntry = _Pm124RinvLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 7, 1, 2, 1)
)
pm124RinvLineEntry.setIndexNames(
    (0, "EKINOPS-Pm124-MIB", "pm124RinvLineIndex"),
)
if mibBuilder.loadTexts:
    pm124RinvLineEntry.setStatus("current")


class _Pm124RinvLineIndex_Type(Integer32):
    """Custom type pm124RinvLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm124RinvLineIndex_Type.__name__ = "Integer32"
_Pm124RinvLineIndex_Object = MibTableColumn
pm124RinvLineIndex = _Pm124RinvLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 7, 1, 2, 1, 1),
    _Pm124RinvLineIndex_Type()
)
pm124RinvLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124RinvLineIndex.setStatus("current")
_Pm124RinvsfpLine_Type = DisplayString
_Pm124RinvsfpLine_Object = MibTableColumn
pm124RinvsfpLine = _Pm124RinvsfpLine_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 7, 1, 2, 1, 2),
    _Pm124RinvsfpLine_Type()
)
pm124RinvsfpLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124RinvsfpLine.setStatus("current")
_Pm124RinvReloadInventory_Type = EkiOnOff
_Pm124RinvReloadInventory_Object = MibScalar
pm124RinvReloadInventory = _Pm124RinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 7, 2),
    _Pm124RinvReloadInventory_Type()
)
pm124RinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124RinvReloadInventory.setStatus("current")
_Pm124RinvHwPlatform_Type = DisplayString
_Pm124RinvHwPlatform_Object = MibScalar
pm124RinvHwPlatform = _Pm124RinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 7, 3),
    _Pm124RinvHwPlatform_Type()
)
pm124RinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124RinvHwPlatform.setStatus("current")
_Pm124RinvModulePlatform_Type = DisplayString
_Pm124RinvModulePlatform_Object = MibScalar
pm124RinvModulePlatform = _Pm124RinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 7, 4),
    _Pm124RinvModulePlatform_Type()
)
pm124RinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124RinvModulePlatform.setStatus("current")
_Pm124RinvSwPlatform_Type = DisplayString
_Pm124RinvSwPlatform_Object = MibScalar
pm124RinvSwPlatform = _Pm124RinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 7, 5),
    _Pm124RinvSwPlatform_Type()
)
pm124RinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124RinvSwPlatform.setStatus("current")
_Pm124RinvGwPlatform_Type = DisplayString
_Pm124RinvGwPlatform_Object = MibScalar
pm124RinvGwPlatform = _Pm124RinvGwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 7, 6),
    _Pm124RinvGwPlatform_Type()
)
pm124RinvGwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124RinvGwPlatform.setStatus("current")
_Pm124Config_ObjectIdentity = ObjectIdentity
pm124Config = _Pm124Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 9)
)
_Pm124CfgLsd_ObjectIdentity = ObjectIdentity
pm124CfgLsd = _Pm124CfgLsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 9, 1)
)
_Pm124CfgClientLsdTable_Object = MibTable
pm124CfgClientLsdTable = _Pm124CfgClientLsdTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 9, 1, 1)
)
if mibBuilder.loadTexts:
    pm124CfgClientLsdTable.setStatus("current")
_Pm124CfgClientLsdEntry_Object = MibTableRow
pm124CfgClientLsdEntry = _Pm124CfgClientLsdEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 9, 1, 1, 1)
)
pm124CfgClientLsdEntry.setIndexNames(
    (0, "EKINOPS-Pm124-MIB", "pm124CfgClientLsdIndex"),
)
if mibBuilder.loadTexts:
    pm124CfgClientLsdEntry.setStatus("current")


class _Pm124CfgClientLsdIndex_Type(Integer32):
    """Custom type pm124CfgClientLsdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124CfgClientLsdIndex_Type.__name__ = "Integer32"
_Pm124CfgClientLsdIndex_Object = MibTableColumn
pm124CfgClientLsdIndex = _Pm124CfgClientLsdIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 9, 1, 1, 1, 1),
    _Pm124CfgClientLsdIndex_Type()
)
pm124CfgClientLsdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124CfgClientLsdIndex.setStatus("current")


class _Pm124CfgClientLsdModePortn_Type(Unsigned32):
    """Custom type pm124CfgClientLsdModePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm124CfgClientLsdModePortn_Type.__name__ = "Unsigned32"
_Pm124CfgClientLsdModePortn_Object = MibTableColumn
pm124CfgClientLsdModePortn = _Pm124CfgClientLsdModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 9, 1, 1, 1, 3),
    _Pm124CfgClientLsdModePortn_Type()
)
pm124CfgClientLsdModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124CfgClientLsdModePortn.setStatus("current")


class _Pm124CfgClientAccessioCtrbInsPortn_Type(Unsigned32):
    """Custom type pm124CfgClientAccessioCtrbInsPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm124CfgClientAccessioCtrbInsPortn_Type.__name__ = "Unsigned32"
_Pm124CfgClientAccessioCtrbInsPortn_Object = MibTableColumn
pm124CfgClientAccessioCtrbInsPortn = _Pm124CfgClientAccessioCtrbInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 9, 1, 1, 1, 4),
    _Pm124CfgClientAccessioCtrbInsPortn_Type()
)
pm124CfgClientAccessioCtrbInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124CfgClientAccessioCtrbInsPortn.setStatus("current")


class _Pm124CfgClientAccCtrbInsPortn_Type(Unsigned32):
    """Custom type pm124CfgClientAccCtrbInsPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm124CfgClientAccCtrbInsPortn_Type.__name__ = "Unsigned32"
_Pm124CfgClientAccCtrbInsPortn_Object = MibTableColumn
pm124CfgClientAccCtrbInsPortn = _Pm124CfgClientAccCtrbInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 9, 1, 1, 1, 5),
    _Pm124CfgClientAccCtrbInsPortn_Type()
)
pm124CfgClientAccCtrbInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124CfgClientAccCtrbInsPortn.setStatus("current")


class _Pm124CfgLineAccessioCtrbInsPortn_Type(Unsigned32):
    """Custom type pm124CfgLineAccessioCtrbInsPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm124CfgLineAccessioCtrbInsPortn_Type.__name__ = "Unsigned32"
_Pm124CfgLineAccessioCtrbInsPortn_Object = MibTableColumn
pm124CfgLineAccessioCtrbInsPortn = _Pm124CfgLineAccessioCtrbInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 9, 1, 1, 1, 6),
    _Pm124CfgLineAccessioCtrbInsPortn_Type()
)
pm124CfgLineAccessioCtrbInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124CfgLineAccessioCtrbInsPortn.setStatus("current")


class _Pm124CfgClientAccCtrbActPortn_Type(Unsigned32):
    """Custom type pm124CfgClientAccCtrbActPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm124CfgClientAccCtrbActPortn_Type.__name__ = "Unsigned32"
_Pm124CfgClientAccCtrbActPortn_Object = MibTableColumn
pm124CfgClientAccCtrbActPortn = _Pm124CfgClientAccCtrbActPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 9, 1, 1, 1, 8),
    _Pm124CfgClientAccCtrbActPortn_Type()
)
pm124CfgClientAccCtrbActPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124CfgClientAccCtrbActPortn.setStatus("current")


class _Pm124CfgLineAccessioCtrbActPortn_Type(Unsigned32):
    """Custom type pm124CfgLineAccessioCtrbActPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm124CfgLineAccessioCtrbActPortn_Type.__name__ = "Unsigned32"
_Pm124CfgLineAccessioCtrbActPortn_Object = MibTableColumn
pm124CfgLineAccessioCtrbActPortn = _Pm124CfgLineAccessioCtrbActPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 9, 1, 1, 1, 9),
    _Pm124CfgLineAccessioCtrbActPortn_Type()
)
pm124CfgLineAccessioCtrbActPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124CfgLineAccessioCtrbActPortn.setStatus("current")
_Pm124CfgStartUp_ObjectIdentity = ObjectIdentity
pm124CfgStartUp = _Pm124CfgStartUp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 9, 2)
)
_Pm124CfgClientStartupTable_Object = MibTable
pm124CfgClientStartupTable = _Pm124CfgClientStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 9, 2, 1)
)
if mibBuilder.loadTexts:
    pm124CfgClientStartupTable.setStatus("current")
_Pm124CfgClientStartupEntry_Object = MibTableRow
pm124CfgClientStartupEntry = _Pm124CfgClientStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 9, 2, 1, 1)
)
pm124CfgClientStartupEntry.setIndexNames(
    (0, "EKINOPS-Pm124-MIB", "pm124CfgClientStartupIndex"),
)
if mibBuilder.loadTexts:
    pm124CfgClientStartupEntry.setStatus("current")


class _Pm124CfgClientStartupIndex_Type(Integer32):
    """Custom type pm124CfgClientStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124CfgClientStartupIndex_Type.__name__ = "Integer32"
_Pm124CfgClientStartupIndex_Object = MibTableColumn
pm124CfgClientStartupIndex = _Pm124CfgClientStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 9, 2, 1, 1, 1),
    _Pm124CfgClientStartupIndex_Type()
)
pm124CfgClientStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124CfgClientStartupIndex.setStatus("current")


class _Pm124CfgClientTrscvCtrlPortn_Type(Unsigned32):
    """Custom type pm124CfgClientTrscvCtrlPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm124CfgClientTrscvCtrlPortn_Type.__name__ = "Unsigned32"
_Pm124CfgClientTrscvCtrlPortn_Object = MibTableColumn
pm124CfgClientTrscvCtrlPortn = _Pm124CfgClientTrscvCtrlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 9, 2, 1, 1, 3),
    _Pm124CfgClientTrscvCtrlPortn_Type()
)
pm124CfgClientTrscvCtrlPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124CfgClientTrscvCtrlPortn.setStatus("current")


class _Pm124CfgClientOosModePortn_Type(Unsigned32):
    """Custom type pm124CfgClientOosModePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm124CfgClientOosModePortn_Type.__name__ = "Unsigned32"
_Pm124CfgClientOosModePortn_Object = MibTableColumn
pm124CfgClientOosModePortn = _Pm124CfgClientOosModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 9, 2, 1, 1, 5),
    _Pm124CfgClientOosModePortn_Type()
)
pm124CfgClientOosModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124CfgClientOosModePortn.setStatus("current")
_Pm124tablelineStartup_ObjectIdentity = ObjectIdentity
pm124tablelineStartup = _Pm124tablelineStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 9, 2, 2)
)


class _Pm124CfglineTrscvCtrl_Type(Unsigned32):
    """Custom type pm124CfglineTrscvCtrl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm124CfglineTrscvCtrl_Type.__name__ = "Unsigned32"
_Pm124CfglineTrscvCtrl_Object = MibScalar
pm124CfglineTrscvCtrl = _Pm124CfglineTrscvCtrl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 9, 2, 2, 2),
    _Pm124CfglineTrscvCtrl_Type()
)
pm124CfglineTrscvCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124CfglineTrscvCtrl.setStatus("current")


class _Pm124CfglineOosMode_Type(Unsigned32):
    """Custom type pm124CfglineOosMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm124CfglineOosMode_Type.__name__ = "Unsigned32"
_Pm124CfglineOosMode_Object = MibScalar
pm124CfglineOosMode = _Pm124CfglineOosMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 9, 2, 2, 3),
    _Pm124CfglineOosMode_Type()
)
pm124CfglineOosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124CfglineOosMode.setStatus("current")


class _Pm124CfgmodProtSelect_Type(Unsigned32):
    """Custom type pm124CfgmodProtSelect based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm124CfgmodProtSelect_Type.__name__ = "Unsigned32"
_Pm124CfgmodProtSelect_Object = MibScalar
pm124CfgmodProtSelect = _Pm124CfgmodProtSelect_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 9, 2, 2, 18),
    _Pm124CfgmodProtSelect_Type()
)
pm124CfgmodProtSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124CfgmodProtSelect.setStatus("current")
_Pm124CfgLabels_ObjectIdentity = ObjectIdentity
pm124CfgLabels = _Pm124CfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 9, 3)
)
_Pm124CfgLabelclientTable_Object = MibTable
pm124CfgLabelclientTable = _Pm124CfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 9, 3, 1)
)
if mibBuilder.loadTexts:
    pm124CfgLabelclientTable.setStatus("current")
_Pm124CfgLabelclientEntry_Object = MibTableRow
pm124CfgLabelclientEntry = _Pm124CfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 9, 3, 1, 1)
)
pm124CfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-Pm124-MIB", "pm124CfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pm124CfgLabelclientEntry.setStatus("current")


class _Pm124CfgLabelclientIndex_Type(Integer32):
    """Custom type pm124CfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124CfgLabelclientIndex_Type.__name__ = "Integer32"
_Pm124CfgLabelclientIndex_Object = MibTableColumn
pm124CfgLabelclientIndex = _Pm124CfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 9, 3, 1, 1, 1),
    _Pm124CfgLabelclientIndex_Type()
)
pm124CfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124CfgLabelclientIndex.setStatus("current")


class _Pm124CfgLabelclientPortn_Type(DisplayString):
    """Custom type pm124CfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm124CfgLabelclientPortn_Type.__name__ = "DisplayString"
_Pm124CfgLabelclientPortn_Object = MibTableColumn
pm124CfgLabelclientPortn = _Pm124CfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 9, 3, 1, 1, 3),
    _Pm124CfgLabelclientPortn_Type()
)
pm124CfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124CfgLabelclientPortn.setStatus("current")
_Pm124CfgLabellineTable_Object = MibTable
pm124CfgLabellineTable = _Pm124CfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 9, 3, 2)
)
if mibBuilder.loadTexts:
    pm124CfgLabellineTable.setStatus("current")
_Pm124CfgLabellineEntry_Object = MibTableRow
pm124CfgLabellineEntry = _Pm124CfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 9, 3, 2, 1)
)
pm124CfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-Pm124-MIB", "pm124CfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pm124CfgLabellineEntry.setStatus("current")


class _Pm124CfgLabellineIndex_Type(Integer32):
    """Custom type pm124CfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm124CfgLabellineIndex_Type.__name__ = "Integer32"
_Pm124CfgLabellineIndex_Object = MibTableColumn
pm124CfgLabellineIndex = _Pm124CfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 9, 3, 2, 1, 1),
    _Pm124CfgLabellineIndex_Type()
)
pm124CfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124CfgLabellineIndex.setStatus("current")


class _Pm124CfgLabellinePortn_Type(DisplayString):
    """Custom type pm124CfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm124CfgLabellinePortn_Type.__name__ = "DisplayString"
_Pm124CfgLabellinePortn_Object = MibTableColumn
pm124CfgLabellinePortn = _Pm124CfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 9, 3, 2, 1, 3),
    _Pm124CfgLabellinePortn_Type()
)
pm124CfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124CfgLabellinePortn.setStatus("current")
_Pm124CfgWriteConfiguration_Type = EkiOnOff
_Pm124CfgWriteConfiguration_Object = MibScalar
pm124CfgWriteConfiguration = _Pm124CfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 9, 257),
    _Pm124CfgWriteConfiguration_Type()
)
pm124CfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm124CfgWriteConfiguration.setStatus("current")
_Pm124traps_ObjectIdentity = ObjectIdentity
pm124traps = _Pm124traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 16, 10)
)


class _Pm124trapPortNumber_Type(Integer32):
    """Custom type pm124trapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm124trapPortNumber_Type.__name__ = "Integer32"
_Pm124trapPortNumber_Object = MibScalar
pm124trapPortNumber = _Pm124trapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 10, 2),
    _Pm124trapPortNumber_Type()
)
pm124trapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124trapPortNumber.setStatus("current")


class _Pm124trapLineNumber_Type(Integer32):
    """Custom type pm124trapLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm124trapLineNumber_Type.__name__ = "Integer32"
_Pm124trapLineNumber_Object = MibScalar
pm124trapLineNumber = _Pm124trapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 10, 3),
    _Pm124trapLineNumber_Type()
)
pm124trapLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124trapLineNumber.setStatus("current")


class _Pm124trapBoardNumber_Type(Integer32):
    """Custom type pm124trapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm124trapBoardNumber_Type.__name__ = "Integer32"
_Pm124trapBoardNumber_Object = MibScalar
pm124trapBoardNumber = _Pm124trapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 16, 10, 4),
    _Pm124trapBoardNumber_Type()
)
pm124trapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm124trapBoardNumber.setStatus("current")

# Managed Objects groups


# Notification objects

pm124LineTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 16, 10, 30)
)
pm124LineTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm124-MIB", "pm124AlmLineDdmWarningPortn"),
        ("EKINOPS-Pm124-MIB", "pm124trapLineNumber"),
        ("EKINOPS-Pm124-MIB", "pm124trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm124LineTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm124LineTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 16, 10, 31)
)
pm124LineTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm124-MIB", "pm124AlmLineDdmWarningPortn"),
        ("EKINOPS-Pm124-MIB", "pm124trapLineNumber"),
        ("EKINOPS-Pm124-MIB", "pm124trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm124LineTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm124LineTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 16, 10, 32)
)
pm124LineTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm124-MIB", "pm124AlmLineDdmAlmPortn"),
        ("EKINOPS-Pm124-MIB", "pm124trapLineNumber"),
        ("EKINOPS-Pm124-MIB", "pm124trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm124LineTrapUrgentGoesOn.setStatus(
        "current"
    )

pm124LineTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 16, 10, 33)
)
pm124LineTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm124-MIB", "pm124AlmLineDdmAlmPortn"),
        ("EKINOPS-Pm124-MIB", "pm124trapLineNumber"),
        ("EKINOPS-Pm124-MIB", "pm124trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm124LineTrapUrgentGoesOff.setStatus(
        "current"
    )

pm124LineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 16, 10, 34)
)
pm124LineTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm124-MIB", "pm124AlmLineFailPortn"),
        ("EKINOPS-Pm124-MIB", "pm124AlmLineHwFailPortn"),
        ("EKINOPS-Pm124-MIB", "pm124trapLineNumber"),
        ("EKINOPS-Pm124-MIB", "pm124trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm124LineTrapCritGoesOn.setStatus(
        "current"
    )

pm124LineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 16, 10, 35)
)
pm124LineTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm124-MIB", "pm124AlmLineFailPortn"),
        ("EKINOPS-Pm124-MIB", "pm124AlmLineHwFailPortn"),
        ("EKINOPS-Pm124-MIB", "pm124trapLineNumber"),
        ("EKINOPS-Pm124-MIB", "pm124trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm124LineTrapCritGoesOff.setStatus(
        "current"
    )

pm124ClientTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 16, 10, 40)
)
pm124ClientTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm124-MIB", "pm124AlmClientSfpDdmWarningPortn"),
        ("EKINOPS-Pm124-MIB", "pm124trapPortNumber"),
        ("EKINOPS-Pm124-MIB", "pm124trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm124ClientTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm124ClientTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 16, 10, 41)
)
pm124ClientTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm124-MIB", "pm124AlmClientSfpDdmWarningPortn"),
        ("EKINOPS-Pm124-MIB", "pm124trapPortNumber"),
        ("EKINOPS-Pm124-MIB", "pm124trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm124ClientTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm124ClientTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 16, 10, 42)
)
pm124ClientTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm124-MIB", "pm124AlmClientSfpDdmAlmPortn"),
        ("EKINOPS-Pm124-MIB", "pm124trapPortNumber"),
        ("EKINOPS-Pm124-MIB", "pm124trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm124ClientTrapUrgentGoesOn.setStatus(
        "current"
    )

pm124ClientTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 16, 10, 43)
)
pm124ClientTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm124-MIB", "pm124AlmClientSfpDdmAlmPortn"),
        ("EKINOPS-Pm124-MIB", "pm124trapPortNumber"),
        ("EKINOPS-Pm124-MIB", "pm124trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm124ClientTrapUrgentGoesOff.setStatus(
        "current"
    )

pm124ClientTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 16, 10, 44)
)
pm124ClientTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm124-MIB", "pm124AlmClientFailAccPortn"),
        ("EKINOPS-Pm124-MIB", "pm124AlmClientHwFailAccPortn"),
        ("EKINOPS-Pm124-MIB", "pm124trapPortNumber"),
        ("EKINOPS-Pm124-MIB", "pm124trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm124ClientTrapCritGoesOn.setStatus(
        "current"
    )

pm124ClientTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 16, 10, 45)
)
pm124ClientTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm124-MIB", "pm124AlmClientFailAccPortn"),
        ("EKINOPS-Pm124-MIB", "pm124AlmClientHwFailAccPortn"),
        ("EKINOPS-Pm124-MIB", "pm124trapPortNumber"),
        ("EKINOPS-Pm124-MIB", "pm124trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm124ClientTrapCritGoesOff.setStatus(
        "current"
    )

pm124PowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 16, 10, 50)
)
pm124PowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm124-MIB", "pm124AlmDefFuseB"),
        ("EKINOPS-Pm124-MIB", "pm124AlmDefFuseA"),
        ("EKINOPS-Pm124-MIB", "pm124trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm124PowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pm124PowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 16, 10, 51)
)
pm124PowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm124-MIB", "pm124AlmDefFuseB"),
        ("EKINOPS-Pm124-MIB", "pm124AlmDefFuseA"),
        ("EKINOPS-Pm124-MIB", "pm124trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm124PowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Pm124-MIB",
    **{"modulePm124": modulePm124,
       "pm124alarms": pm124alarms,
       "pm124AlmOther": pm124AlmOther,
       "pm124AlmOtherNurg": pm124AlmOtherNurg,
       "pm124AlmsynthAlm2": pm124AlmsynthAlm2,
       "pm124AlmConfTableSave": pm124AlmConfTableSave,
       "pm124AlmInvUpload": pm124AlmInvUpload,
       "pm124AlmConfTableLoad": pm124AlmConfTableLoad,
       "pm124AlmCorrelatOff": pm124AlmCorrelatOff,
       "pm124AlmOtherUrg": pm124AlmOtherUrg,
       "pm124AlmOtherCrit": pm124AlmOtherCrit,
       "pm124AlmsynthAlm0": pm124AlmsynthAlm0,
       "pm124AlmModuleGlobFailure": pm124AlmModuleGlobFailure,
       "pm124AlmDefFuseA": pm124AlmDefFuseA,
       "pm124AlmDefFuseB": pm124AlmDefFuseB,
       "pm124AlmClient": pm124AlmClient,
       "pm124AlmClientNurg": pm124AlmClientNurg,
       "pm124AlmclientSfpWarnDdmTable": pm124AlmclientSfpWarnDdmTable,
       "pm124AlmclientSfpWarnDdmEntry": pm124AlmclientSfpWarnDdmEntry,
       "pm124AlmclientSfpWarnDdmIndex": pm124AlmclientSfpWarnDdmIndex,
       "pm124AlmClientTxPwLowWngPortn": pm124AlmClientTxPwLowWngPortn,
       "pm124AlmClientTxPwrHighWngPortn": pm124AlmClientTxPwrHighWngPortn,
       "pm124AlmClientTxBiasLowWngPortn": pm124AlmClientTxBiasLowWngPortn,
       "pm124AlmClientTxBiasHighWngPortn": pm124AlmClientTxBiasHighWngPortn,
       "pm124AlmClientVccLowWngPortn": pm124AlmClientVccLowWngPortn,
       "pm124AlmClientVccHighWngPortn": pm124AlmClientVccHighWngPortn,
       "pm124AlmClientTempLowWngPortn": pm124AlmClientTempLowWngPortn,
       "pm124AlmClientTempHighWngPortn": pm124AlmClientTempHighWngPortn,
       "pm124AlmClientRxPwrLowWngPortn": pm124AlmClientRxPwrLowWngPortn,
       "pm124AlmClientRxPwrHighWngPortn": pm124AlmClientRxPwrHighWngPortn,
       "pm124AlmClientUrg": pm124AlmClientUrg,
       "pm124AlmclientSfpAlmDdmTable": pm124AlmclientSfpAlmDdmTable,
       "pm124AlmclientSfpAlmDdmEntry": pm124AlmclientSfpAlmDdmEntry,
       "pm124AlmclientSfpAlmDdmIndex": pm124AlmclientSfpAlmDdmIndex,
       "pm124AlmClientTxPwrLowAlaPortn": pm124AlmClientTxPwrLowAlaPortn,
       "pm124AlmClientClientTxPwrHighAlaPortn": pm124AlmClientClientTxPwrHighAlaPortn,
       "pm124AlmClientTxBiasLowAlaPortn": pm124AlmClientTxBiasLowAlaPortn,
       "pm124AlmClientTxBiasHighAlaPortn": pm124AlmClientTxBiasHighAlaPortn,
       "pm124AlmClientVccLowAlaPortn": pm124AlmClientVccLowAlaPortn,
       "pm124AlmClientVccHighAlaPortn": pm124AlmClientVccHighAlaPortn,
       "pm124AlmClientTempLowAlaPortn": pm124AlmClientTempLowAlaPortn,
       "pm124AlmClientTempHighAlaPortn": pm124AlmClientTempHighAlaPortn,
       "pm124AlmClientRxPwrLowAlaPortn": pm124AlmClientRxPwrLowAlaPortn,
       "pm124AlmClientRxPwrHighAlaPortn": pm124AlmClientRxPwrHighAlaPortn,
       "pm124AlmClientCrit": pm124AlmClientCrit,
       "pm124AlmsynthAlmPortTable": pm124AlmsynthAlmPortTable,
       "pm124AlmsynthAlmPortEntry": pm124AlmsynthAlmPortEntry,
       "pm124AlmsynthAlmPortIndex": pm124AlmsynthAlmPortIndex,
       "pm124AlmClientSfpAbsentPortn": pm124AlmClientSfpAbsentPortn,
       "pm124AlmClientDdmAbsentPortn": pm124AlmClientDdmAbsentPortn,
       "pm124AlmClientHwFailAccPortn": pm124AlmClientHwFailAccPortn,
       "pm124AlmClientLsdPortn": pm124AlmClientLsdPortn,
       "pm124AlmClientLocalOosPortn": pm124AlmClientLocalOosPortn,
       "pm124AlmClientRemoteOosPortn": pm124AlmClientRemoteOosPortn,
       "pm124AlmClientDwCaisPortn": pm124AlmClientDwCaisPortn,
       "pm124AlmClientSfpDdmWarningPortn": pm124AlmClientSfpDdmWarningPortn,
       "pm124AlmClientSfpDdmAlmPortn": pm124AlmClientSfpDdmAlmPortn,
       "pm124AlmClientFailAccPortn": pm124AlmClientFailAccPortn,
       "pm124AlmClientUpCsfPortn": pm124AlmClientUpCsfPortn,
       "pm124AlmclientAccessioAlmTable": pm124AlmclientAccessioAlmTable,
       "pm124AlmclientAccessioAlmEntry": pm124AlmclientAccessioAlmEntry,
       "pm124AlmclientAccessioAlmIndex": pm124AlmclientAccessioAlmIndex,
       "pm124AlmClientLasFailPortn": pm124AlmClientLasFailPortn,
       "pm124AlmClientLosPortn": pm124AlmClientLosPortn,
       "pm124AlmclientAccAlmTable": pm124AlmclientAccAlmTable,
       "pm124AlmclientAccAlmEntry": pm124AlmclientAccAlmEntry,
       "pm124AlmclientAccAlmIndex": pm124AlmclientAccAlmIndex,
       "pm124AlmClientOosPortn": pm124AlmClientOosPortn,
       "pm124AlmClientUpEsOvlPortn": pm124AlmClientUpEsOvlPortn,
       "pm124AlmClientCsfDetPortn": pm124AlmClientCsfDetPortn,
       "pm124AlmClientDwEsOvlPortn": pm124AlmClientDwEsOvlPortn,
       "pm124AlmLine": pm124AlmLine,
       "pm124AlmLineNurg": pm124AlmLineNurg,
       "pm124AlmlineSfpWarnDdmTable": pm124AlmlineSfpWarnDdmTable,
       "pm124AlmlineSfpWarnDdmEntry": pm124AlmlineSfpWarnDdmEntry,
       "pm124AlmlineSfpWarnDdmIndex": pm124AlmlineSfpWarnDdmIndex,
       "pm124AlmLineTxPwLowWngPortn": pm124AlmLineTxPwLowWngPortn,
       "pm124AlmLineTxPwrHighWngPortn": pm124AlmLineTxPwrHighWngPortn,
       "pm124AlmLineTxBiasLowWngPortn": pm124AlmLineTxBiasLowWngPortn,
       "pm124AlmLineTxBiasHighWngPortn": pm124AlmLineTxBiasHighWngPortn,
       "pm124AlmLineVccLowWngPortn": pm124AlmLineVccLowWngPortn,
       "pm124AlmLineVccHighWngPortn": pm124AlmLineVccHighWngPortn,
       "pm124AlmLineTempLowWngPortn": pm124AlmLineTempLowWngPortn,
       "pm124AlmLineTempHighWngPortn": pm124AlmLineTempHighWngPortn,
       "pm124AlmLineRxPwrLowWngPortn": pm124AlmLineRxPwrLowWngPortn,
       "pm124AlmLineRxPwrHighWngPortn": pm124AlmLineRxPwrHighWngPortn,
       "pm124AlmLineUrg": pm124AlmLineUrg,
       "pm124AlmlineSfpAlmDdmTable": pm124AlmlineSfpAlmDdmTable,
       "pm124AlmlineSfpAlmDdmEntry": pm124AlmlineSfpAlmDdmEntry,
       "pm124AlmlineSfpAlmDdmIndex": pm124AlmlineSfpAlmDdmIndex,
       "pm124AlmLineTxPwrLowAlaPortn": pm124AlmLineTxPwrLowAlaPortn,
       "pm124AlmLineTxPwrHighAlaPortn": pm124AlmLineTxPwrHighAlaPortn,
       "pm124AlmLineTxBiasLowAlaPortn": pm124AlmLineTxBiasLowAlaPortn,
       "pm124AlmLineTxBiasHighAlaPortn": pm124AlmLineTxBiasHighAlaPortn,
       "pm124AlmLineVccLowAlaPortn": pm124AlmLineVccLowAlaPortn,
       "pm124AlmLineVccHighAlaPortn": pm124AlmLineVccHighAlaPortn,
       "pm124AlmLineTempLowAlaPortn": pm124AlmLineTempLowAlaPortn,
       "pm124AlmLineTempHighAlaPortn": pm124AlmLineTempHighAlaPortn,
       "pm124AlmLineRxPwrLowAlaPortn": pm124AlmLineRxPwrLowAlaPortn,
       "pm124AlmLineRxPwrHighAlaPortn": pm124AlmLineRxPwrHighAlaPortn,
       "pm124AlmLineCrit": pm124AlmLineCrit,
       "pm124AlmsynthAlmLineTable": pm124AlmsynthAlmLineTable,
       "pm124AlmsynthAlmLineEntry": pm124AlmsynthAlmLineEntry,
       "pm124AlmsynthAlmLineIndex": pm124AlmsynthAlmLineIndex,
       "pm124AlmLineSfpAbsentPortn": pm124AlmLineSfpAbsentPortn,
       "pm124AlmLineDdmAbsentPortn": pm124AlmLineDdmAbsentPortn,
       "pm124AlmLineHwFailPortn": pm124AlmLineHwFailPortn,
       "pm124AlmLineLsdPortn": pm124AlmLineLsdPortn,
       "pm124AlmLineLocalOosPortn": pm124AlmLineLocalOosPortn,
       "pm124AlmLineDdmWarningPortn": pm124AlmLineDdmWarningPortn,
       "pm124AlmLineDdmAlmPortn": pm124AlmLineDdmAlmPortn,
       "pm124AlmLineFailPortn": pm124AlmLineFailPortn,
       "pm124AlmlineAccessioAlmTable": pm124AlmlineAccessioAlmTable,
       "pm124AlmlineAccessioAlmEntry": pm124AlmlineAccessioAlmEntry,
       "pm124AlmlineAccessioAlmIndex": pm124AlmlineAccessioAlmIndex,
       "pm124AlmLineLasFailPortn": pm124AlmLineLasFailPortn,
       "pm124AlmLineLosPortn": pm124AlmLineLosPortn,
       "pm124AlmLineLossSyncPortn": pm124AlmLineLossSyncPortn,
       "pm124measures": pm124measures,
       "pm124MesrOther": pm124MesrOther,
       "pm124MesrClient": pm124MesrClient,
       "pm124MesrclientTemperatureTable": pm124MesrclientTemperatureTable,
       "pm124MesrclientTemperatureEntry": pm124MesrclientTemperatureEntry,
       "pm124MesrclientTemperatureIndex": pm124MesrclientTemperatureIndex,
       "pm124MesrclientTemperaturePortn": pm124MesrclientTemperaturePortn,
       "pm124MesrclientVoltTable": pm124MesrclientVoltTable,
       "pm124MesrclientVoltEntry": pm124MesrclientVoltEntry,
       "pm124MesrclientVoltIndex": pm124MesrclientVoltIndex,
       "pm124MesrclientVoltPortn": pm124MesrclientVoltPortn,
       "pm124MesrclientTxBiasTable": pm124MesrclientTxBiasTable,
       "pm124MesrclientTxBiasEntry": pm124MesrclientTxBiasEntry,
       "pm124MesrclientTxBiasIndex": pm124MesrclientTxBiasIndex,
       "pm124MesrclientTxBiasPortn": pm124MesrclientTxBiasPortn,
       "pm124MesrclientTxPowerTable": pm124MesrclientTxPowerTable,
       "pm124MesrclientTxPowerEntry": pm124MesrclientTxPowerEntry,
       "pm124MesrclientTxPowerIndex": pm124MesrclientTxPowerIndex,
       "pm124MesrclientTxPowerPortn": pm124MesrclientTxPowerPortn,
       "pm124MesrclientRxPowerTable": pm124MesrclientRxPowerTable,
       "pm124MesrclientRxPowerEntry": pm124MesrclientRxPowerEntry,
       "pm124MesrclientRxPowerIndex": pm124MesrclientRxPowerIndex,
       "pm124MesrclientRxPowerPortn": pm124MesrclientRxPowerPortn,
       "pm124MesrLine": pm124MesrLine,
       "pm124MesrlineTemperatureTable": pm124MesrlineTemperatureTable,
       "pm124MesrlineTemperatureEntry": pm124MesrlineTemperatureEntry,
       "pm124MesrlineTemperatureIndex": pm124MesrlineTemperatureIndex,
       "pm124MesrlineTemperaturePortn": pm124MesrlineTemperaturePortn,
       "pm124MesrlineVoltTable": pm124MesrlineVoltTable,
       "pm124MesrlineVoltEntry": pm124MesrlineVoltEntry,
       "pm124MesrlineVoltIndex": pm124MesrlineVoltIndex,
       "pm124MesrlineVoltPortn": pm124MesrlineVoltPortn,
       "pm124MesrlineTxBiasTable": pm124MesrlineTxBiasTable,
       "pm124MesrlineTxBiasEntry": pm124MesrlineTxBiasEntry,
       "pm124MesrlineTxBiasIndex": pm124MesrlineTxBiasIndex,
       "pm124MesrlineTxBiasPortn": pm124MesrlineTxBiasPortn,
       "pm124MesrlineTxPowerTable": pm124MesrlineTxPowerTable,
       "pm124MesrlineTxPowerEntry": pm124MesrlineTxPowerEntry,
       "pm124MesrlineTxPowerIndex": pm124MesrlineTxPowerIndex,
       "pm124MesrlineTxPowerPortn": pm124MesrlineTxPowerPortn,
       "pm124MesrlineRxPowerTable": pm124MesrlineRxPowerTable,
       "pm124MesrlineRxPowerEntry": pm124MesrlineRxPowerEntry,
       "pm124MesrlineRxPowerIndex": pm124MesrlineRxPowerIndex,
       "pm124MesrlineRxPowerPortn": pm124MesrlineRxPowerPortn,
       "pm124counters": pm124counters,
       "pm124CntOther": pm124CntOther,
       "pm124CntClient": pm124CntClient,
       "pm124CntclientCbipErrCntTable": pm124CntclientCbipErrCntTable,
       "pm124CntclientCbipErrCntEntry": pm124CntclientCbipErrCntEntry,
       "pm124CntclientCbipErrCntIndex": pm124CntclientCbipErrCntIndex,
       "pm124CntclientCbipErrCntValuePortn": pm124CntclientCbipErrCntValuePortn,
       "pm124CntclientCbipErrCntErrorPortn": pm124CntclientCbipErrCntErrorPortn,
       "pm124CntclientCbipErrCntOverloadPortn": pm124CntclientCbipErrCntOverloadPortn,
       "pm124CntclientB1ErrCntTable": pm124CntclientB1ErrCntTable,
       "pm124CntclientB1ErrCntEntry": pm124CntclientB1ErrCntEntry,
       "pm124CntclientB1ErrCntIndex": pm124CntclientB1ErrCntIndex,
       "pm124CntclientB1ErrCntValuePortn": pm124CntclientB1ErrCntValuePortn,
       "pm124CntclientB1ErrCntErrorPortn": pm124CntclientB1ErrCntErrorPortn,
       "pm124CntclientB1ErrCntOverloadPortn": pm124CntclientB1ErrCntOverloadPortn,
       "pm124CntLine": pm124CntLine,
       "pm124CntlineDispErrCntTable": pm124CntlineDispErrCntTable,
       "pm124CntlineDispErrCntEntry": pm124CntlineDispErrCntEntry,
       "pm124CntlineDispErrCntIndex": pm124CntlineDispErrCntIndex,
       "pm124CntlineDispErrCntValuePortn": pm124CntlineDispErrCntValuePortn,
       "pm124CntlineDispErrCntErrorPortn": pm124CntlineDispErrCntErrorPortn,
       "pm124CntlineDispErrCntOverloadPortn": pm124CntlineDispErrCntOverloadPortn,
       "pm124CntlineCrcErrCntTable": pm124CntlineCrcErrCntTable,
       "pm124CntlineCrcErrCntEntry": pm124CntlineCrcErrCntEntry,
       "pm124CntlineCrcErrCntIndex": pm124CntlineCrcErrCntIndex,
       "pm124CntlineCrcErrCntValuePortn": pm124CntlineCrcErrCntValuePortn,
       "pm124CntlineCrcErrCntErrorPortn": pm124CntlineCrcErrCntErrorPortn,
       "pm124CntlineCrcErrCntOverloadPortn": pm124CntlineCrcErrCntOverloadPortn,
       "pm124CntCountersReset": pm124CntCountersReset,
       "pm124CntCountersStop": pm124CntCountersStop,
       "pm124controlsWrite": pm124controlsWrite,
       "pm124CtrlOther": pm124CtrlOther,
       "pm124Ctrlsynth0": pm124Ctrlsynth0,
       "pm124CtrlConfLoad": pm124CtrlConfLoad,
       "pm124CtrlConfFlash": pm124CtrlConfFlash,
       "pm124CtrlConfClear": pm124CtrlConfClear,
       "pm124Ctrlsynth4": pm124Ctrlsynth4,
       "pm124CtrlCorrelatOn": pm124CtrlCorrelatOn,
       "pm124CtrlCorrelatOff": pm124CtrlCorrelatOff,
       "pm124CtrlswMgnt": pm124CtrlswMgnt,
       "pm124CtrlColdReset": pm124CtrlColdReset,
       "pm124CtrlWarmReset": pm124CtrlWarmReset,
       "pm124Ctrlprotocol": pm124Ctrlprotocol,
       "pm124CtrlledTest": pm124CtrlledTest,
       "pm124CtrlGreenLed": pm124CtrlGreenLed,
       "pm124CtrlRedLed": pm124CtrlRedLed,
       "pm124CtrlLedOff": pm124CtrlLedOff,
       "pm124CtrlmoduleOosMode": pm124CtrlmoduleOosMode,
       "pm124CtrlModuleOosMode": pm124CtrlModuleOosMode,
       "pm124CtrlClient": pm124CtrlClient,
       "pm124CtrlclientSfpOnoffTable": pm124CtrlclientSfpOnoffTable,
       "pm124CtrlclientSfpOnoffEntry": pm124CtrlclientSfpOnoffEntry,
       "pm124CtrlclientSfpOnoffIndex": pm124CtrlclientSfpOnoffIndex,
       "pm124CtrlclientSfpOnoffPortn": pm124CtrlclientSfpOnoffPortn,
       "pm124CtrlclientLoopTable": pm124CtrlclientLoopTable,
       "pm124CtrlclientLoopEntry": pm124CtrlclientLoopEntry,
       "pm124CtrlclientLoopIndex": pm124CtrlclientLoopIndex,
       "pm124CtrlclientLoopPortn": pm124CtrlclientLoopPortn,
       "pm124CtrlclientCsfUpInsertTable": pm124CtrlclientCsfUpInsertTable,
       "pm124CtrlclientCsfUpInsertEntry": pm124CtrlclientCsfUpInsertEntry,
       "pm124CtrlclientCsfUpInsertIndex": pm124CtrlclientCsfUpInsertIndex,
       "pm124CtrlclientCsfUpInsertPortn": pm124CtrlclientCsfUpInsertPortn,
       "pm124CtrlclientCaisDwInsertTable": pm124CtrlclientCaisDwInsertTable,
       "pm124CtrlclientCaisDwInsertEntry": pm124CtrlclientCaisDwInsertEntry,
       "pm124CtrlclientCaisDwInsertIndex": pm124CtrlclientCaisDwInsertIndex,
       "pm124CtrlclientCaisDwInsertPortn": pm124CtrlclientCaisDwInsertPortn,
       "pm124CtrlclientOosModeTable": pm124CtrlclientOosModeTable,
       "pm124CtrlclientOosModeEntry": pm124CtrlclientOosModeEntry,
       "pm124CtrlclientOosModeIndex": pm124CtrlclientOosModeIndex,
       "pm124CtrlclientOosModePortn": pm124CtrlclientOosModePortn,
       "pm124CtrlclientAccessTermLoopTable": pm124CtrlclientAccessTermLoopTable,
       "pm124CtrlclientAccessTermLoopEntry": pm124CtrlclientAccessTermLoopEntry,
       "pm124CtrlclientAccessTermLoopIndex": pm124CtrlclientAccessTermLoopIndex,
       "pm124CtrlclientAccessTermLoopPortn": pm124CtrlclientAccessTermLoopPortn,
       "pm124CtrlLine": pm124CtrlLine,
       "pm124CtrllineSfpOnoffTable": pm124CtrllineSfpOnoffTable,
       "pm124CtrllineSfpOnoffEntry": pm124CtrllineSfpOnoffEntry,
       "pm124CtrllineSfpOnoffIndex": pm124CtrllineSfpOnoffIndex,
       "pm124CtrllineSfpOnoffPortn": pm124CtrllineSfpOnoffPortn,
       "pm124CtrllineOosModeTable": pm124CtrllineOosModeTable,
       "pm124CtrllineOosModeEntry": pm124CtrllineOosModeEntry,
       "pm124CtrllineOosModeIndex": pm124CtrllineOosModeIndex,
       "pm124CtrllineOosModePortn": pm124CtrllineOosModePortn,
       "pm124CtrllineLoopTable": pm124CtrllineLoopTable,
       "pm124CtrllineLoopEntry": pm124CtrllineLoopEntry,
       "pm124CtrllineLoopIndex": pm124CtrllineLoopIndex,
       "pm124CtrllineLoopPortn": pm124CtrllineLoopPortn,
       "pm124CtrllineLoopTerminalTable": pm124CtrllineLoopTerminalTable,
       "pm124CtrllineLoopTerminalEntry": pm124CtrllineLoopTerminalEntry,
       "pm124CtrllineLoopTerminalIndex": pm124CtrllineLoopTerminalIndex,
       "pm124CtrllineLoopTerminalPortn": pm124CtrllineLoopTerminalPortn,
       "pm124ri": pm124ri,
       "pm124riTable": pm124riTable,
       "pm124RinvClientTable": pm124RinvClientTable,
       "pm124RinvClientEntry": pm124RinvClientEntry,
       "pm124RinvClientIndex": pm124RinvClientIndex,
       "pm124RinvSfpClient": pm124RinvSfpClient,
       "pm124RinvLineTable": pm124RinvLineTable,
       "pm124RinvLineEntry": pm124RinvLineEntry,
       "pm124RinvLineIndex": pm124RinvLineIndex,
       "pm124RinvsfpLine": pm124RinvsfpLine,
       "pm124RinvReloadInventory": pm124RinvReloadInventory,
       "pm124RinvHwPlatform": pm124RinvHwPlatform,
       "pm124RinvModulePlatform": pm124RinvModulePlatform,
       "pm124RinvSwPlatform": pm124RinvSwPlatform,
       "pm124RinvGwPlatform": pm124RinvGwPlatform,
       "pm124Config": pm124Config,
       "pm124CfgLsd": pm124CfgLsd,
       "pm124CfgClientLsdTable": pm124CfgClientLsdTable,
       "pm124CfgClientLsdEntry": pm124CfgClientLsdEntry,
       "pm124CfgClientLsdIndex": pm124CfgClientLsdIndex,
       "pm124CfgClientLsdModePortn": pm124CfgClientLsdModePortn,
       "pm124CfgClientAccessioCtrbInsPortn": pm124CfgClientAccessioCtrbInsPortn,
       "pm124CfgClientAccCtrbInsPortn": pm124CfgClientAccCtrbInsPortn,
       "pm124CfgLineAccessioCtrbInsPortn": pm124CfgLineAccessioCtrbInsPortn,
       "pm124CfgClientAccCtrbActPortn": pm124CfgClientAccCtrbActPortn,
       "pm124CfgLineAccessioCtrbActPortn": pm124CfgLineAccessioCtrbActPortn,
       "pm124CfgStartUp": pm124CfgStartUp,
       "pm124CfgClientStartupTable": pm124CfgClientStartupTable,
       "pm124CfgClientStartupEntry": pm124CfgClientStartupEntry,
       "pm124CfgClientStartupIndex": pm124CfgClientStartupIndex,
       "pm124CfgClientTrscvCtrlPortn": pm124CfgClientTrscvCtrlPortn,
       "pm124CfgClientOosModePortn": pm124CfgClientOosModePortn,
       "pm124tablelineStartup": pm124tablelineStartup,
       "pm124CfglineTrscvCtrl": pm124CfglineTrscvCtrl,
       "pm124CfglineOosMode": pm124CfglineOosMode,
       "pm124CfgmodProtSelect": pm124CfgmodProtSelect,
       "pm124CfgLabels": pm124CfgLabels,
       "pm124CfgLabelclientTable": pm124CfgLabelclientTable,
       "pm124CfgLabelclientEntry": pm124CfgLabelclientEntry,
       "pm124CfgLabelclientIndex": pm124CfgLabelclientIndex,
       "pm124CfgLabelclientPortn": pm124CfgLabelclientPortn,
       "pm124CfgLabellineTable": pm124CfgLabellineTable,
       "pm124CfgLabellineEntry": pm124CfgLabellineEntry,
       "pm124CfgLabellineIndex": pm124CfgLabellineIndex,
       "pm124CfgLabellinePortn": pm124CfgLabellinePortn,
       "pm124CfgWriteConfiguration": pm124CfgWriteConfiguration,
       "pm124traps": pm124traps,
       "pm124trapPortNumber": pm124trapPortNumber,
       "pm124trapLineNumber": pm124trapLineNumber,
       "pm124trapBoardNumber": pm124trapBoardNumber,
       "pm124LineTrapNotUrgentGoesOn": pm124LineTrapNotUrgentGoesOn,
       "pm124LineTrapNotUrgentGoesOff": pm124LineTrapNotUrgentGoesOff,
       "pm124LineTrapUrgentGoesOn": pm124LineTrapUrgentGoesOn,
       "pm124LineTrapUrgentGoesOff": pm124LineTrapUrgentGoesOff,
       "pm124LineTrapCritGoesOn": pm124LineTrapCritGoesOn,
       "pm124LineTrapCritGoesOff": pm124LineTrapCritGoesOff,
       "pm124ClientTrapNotUrgentGoesOn": pm124ClientTrapNotUrgentGoesOn,
       "pm124ClientTrapNotUrgentGoesOff": pm124ClientTrapNotUrgentGoesOff,
       "pm124ClientTrapUrgentGoesOn": pm124ClientTrapUrgentGoesOn,
       "pm124ClientTrapUrgentGoesOff": pm124ClientTrapUrgentGoesOff,
       "pm124ClientTrapCritGoesOn": pm124ClientTrapCritGoesOn,
       "pm124ClientTrapCritGoesOff": pm124ClientTrapCritGoesOff,
       "pm124PowerTrapUrgentGoesOn": pm124PowerTrapUrgentGoesOn,
       "pm124PowerTrapUrgentGoesOff": pm124PowerTrapUrgentGoesOff}
)
