# SNMP MIB module (EKINOPS-Pm404-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Pm404-MIB.mib
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

modulePm404 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25)
)
if mibBuilder.loadTexts:
    modulePm404.setRevisions(
        ("2007-04-04 00:00",
         "2007-09-19 00:00",
         "2007-11-21 00:00",
         "2009-04-21 00:00",
         "2009-08-17 00:00",
         "2009-12-14 00:00",
         "2010-02-24 00:00",
         "2010-11-05 00:00",
         "2010-12-17 00:00",
         "2012-07-04 00:00",
         "2014-03-25 00:00",
         "2014-12-15 00:00",
         "2016-05-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Pm404alarms_ObjectIdentity = ObjectIdentity
pm404alarms = _Pm404alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2)
)
_Pm404AlmOther_ObjectIdentity = ObjectIdentity
pm404AlmOther = _Pm404AlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 1)
)
_Pm404AlmOtherNurg_ObjectIdentity = ObjectIdentity
pm404AlmOtherNurg = _Pm404AlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 1, 1)
)
_Pm404AlmsynthAlm2_ObjectIdentity = ObjectIdentity
pm404AlmsynthAlm2 = _Pm404AlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 1, 1, 2)
)
_Pm404AlmConfTableSave_Type = EkiOnOff
_Pm404AlmConfTableSave_Object = MibScalar
pm404AlmConfTableSave = _Pm404AlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 1, 1, 2, 1),
    _Pm404AlmConfTableSave_Type()
)
pm404AlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmConfTableSave.setStatus("current")
_Pm404AlmInvUpload_Type = EkiOnOff
_Pm404AlmInvUpload_Object = MibScalar
pm404AlmInvUpload = _Pm404AlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 1, 1, 2, 2),
    _Pm404AlmInvUpload_Type()
)
pm404AlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmInvUpload.setStatus("current")
_Pm404AlmConfTableLoad_Type = EkiOnOff
_Pm404AlmConfTableLoad_Object = MibScalar
pm404AlmConfTableLoad = _Pm404AlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 1, 1, 2, 3),
    _Pm404AlmConfTableLoad_Type()
)
pm404AlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmConfTableLoad.setStatus("current")
_Pm404AlmCorrelatOff_Type = EkiOnOff
_Pm404AlmCorrelatOff_Object = MibScalar
pm404AlmCorrelatOff = _Pm404AlmCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 1, 1, 2, 4),
    _Pm404AlmCorrelatOff_Type()
)
pm404AlmCorrelatOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmCorrelatOff.setStatus("current")
_Pm404AlmOtherUrg_ObjectIdentity = ObjectIdentity
pm404AlmOtherUrg = _Pm404AlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 1, 2)
)
_Pm404AlmOtherCrit_ObjectIdentity = ObjectIdentity
pm404AlmOtherCrit = _Pm404AlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 1, 3)
)
_Pm404AlmsynthAlm0_ObjectIdentity = ObjectIdentity
pm404AlmsynthAlm0 = _Pm404AlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 1, 3, 0)
)
_Pm404AlmModuleGlobFailure_Type = EkiOnOff
_Pm404AlmModuleGlobFailure_Object = MibScalar
pm404AlmModuleGlobFailure = _Pm404AlmModuleGlobFailure_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 1, 3, 0, 9),
    _Pm404AlmModuleGlobFailure_Type()
)
pm404AlmModuleGlobFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmModuleGlobFailure.setStatus("current")
_Pm404AlmDefFuseA_Type = EkiOnOff
_Pm404AlmDefFuseA_Object = MibScalar
pm404AlmDefFuseA = _Pm404AlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 1, 3, 0, 15),
    _Pm404AlmDefFuseA_Type()
)
pm404AlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmDefFuseA.setStatus("current")
_Pm404AlmDefFuseB_Type = EkiOnOff
_Pm404AlmDefFuseB_Object = MibScalar
pm404AlmDefFuseB = _Pm404AlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 1, 3, 0, 16),
    _Pm404AlmDefFuseB_Type()
)
pm404AlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmDefFuseB.setStatus("current")
_Pm404AlmClient_ObjectIdentity = ObjectIdentity
pm404AlmClient = _Pm404AlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2)
)
_Pm404AlmClientNurg_ObjectIdentity = ObjectIdentity
pm404AlmClientNurg = _Pm404AlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 1)
)
_Pm404Almline1SfpWarnDdmTable_Object = MibTable
pm404Almline1SfpWarnDdmTable = _Pm404Almline1SfpWarnDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 1, 32)
)
if mibBuilder.loadTexts:
    pm404Almline1SfpWarnDdmTable.setStatus("current")
_Pm404Almline1SfpWarnDdmEntry_Object = MibTableRow
pm404Almline1SfpWarnDdmEntry = _Pm404Almline1SfpWarnDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 1, 32, 1)
)
pm404Almline1SfpWarnDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm404-MIB", "pm404Almline1SfpWarnDdmIndex"),
)
if mibBuilder.loadTexts:
    pm404Almline1SfpWarnDdmEntry.setStatus("current")


class _Pm404Almline1SfpWarnDdmIndex_Type(Integer32):
    """Custom type pm404Almline1SfpWarnDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm404Almline1SfpWarnDdmIndex_Type.__name__ = "Integer32"
_Pm404Almline1SfpWarnDdmIndex_Object = MibTableColumn
pm404Almline1SfpWarnDdmIndex = _Pm404Almline1SfpWarnDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 1, 32, 1, 1),
    _Pm404Almline1SfpWarnDdmIndex_Type()
)
pm404Almline1SfpWarnDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404Almline1SfpWarnDdmIndex.setStatus("current")
_Pm404AlmLine1TxPwLowWngPortn_Type = EkiOnOff
_Pm404AlmLine1TxPwLowWngPortn_Object = MibTableColumn
pm404AlmLine1TxPwLowWngPortn = _Pm404AlmLine1TxPwLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 1, 32, 1, 2),
    _Pm404AlmLine1TxPwLowWngPortn_Type()
)
pm404AlmLine1TxPwLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine1TxPwLowWngPortn.setStatus("current")
_Pm404AlmLine1TxPwrHighWngPortn_Type = EkiOnOff
_Pm404AlmLine1TxPwrHighWngPortn_Object = MibTableColumn
pm404AlmLine1TxPwrHighWngPortn = _Pm404AlmLine1TxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 1, 32, 1, 3),
    _Pm404AlmLine1TxPwrHighWngPortn_Type()
)
pm404AlmLine1TxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine1TxPwrHighWngPortn.setStatus("current")
_Pm404AlmLine1TxBiasLowWngPortn_Type = EkiOnOff
_Pm404AlmLine1TxBiasLowWngPortn_Object = MibTableColumn
pm404AlmLine1TxBiasLowWngPortn = _Pm404AlmLine1TxBiasLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 1, 32, 1, 4),
    _Pm404AlmLine1TxBiasLowWngPortn_Type()
)
pm404AlmLine1TxBiasLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine1TxBiasLowWngPortn.setStatus("current")
_Pm404AlmLine1TxBiasHighWngPortn_Type = EkiOnOff
_Pm404AlmLine1TxBiasHighWngPortn_Object = MibTableColumn
pm404AlmLine1TxBiasHighWngPortn = _Pm404AlmLine1TxBiasHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 1, 32, 1, 5),
    _Pm404AlmLine1TxBiasHighWngPortn_Type()
)
pm404AlmLine1TxBiasHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine1TxBiasHighWngPortn.setStatus("current")
_Pm404AlmLine1VccLowWngPortn_Type = EkiOnOff
_Pm404AlmLine1VccLowWngPortn_Object = MibTableColumn
pm404AlmLine1VccLowWngPortn = _Pm404AlmLine1VccLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 1, 32, 1, 6),
    _Pm404AlmLine1VccLowWngPortn_Type()
)
pm404AlmLine1VccLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine1VccLowWngPortn.setStatus("current")
_Pm404AlmLine1VccHighWngPortn_Type = EkiOnOff
_Pm404AlmLine1VccHighWngPortn_Object = MibTableColumn
pm404AlmLine1VccHighWngPortn = _Pm404AlmLine1VccHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 1, 32, 1, 7),
    _Pm404AlmLine1VccHighWngPortn_Type()
)
pm404AlmLine1VccHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine1VccHighWngPortn.setStatus("current")
_Pm404AlmLine1TempLowWngPortn_Type = EkiOnOff
_Pm404AlmLine1TempLowWngPortn_Object = MibTableColumn
pm404AlmLine1TempLowWngPortn = _Pm404AlmLine1TempLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 1, 32, 1, 8),
    _Pm404AlmLine1TempLowWngPortn_Type()
)
pm404AlmLine1TempLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine1TempLowWngPortn.setStatus("current")
_Pm404AlmLine1TempHighWngPortn_Type = EkiOnOff
_Pm404AlmLine1TempHighWngPortn_Object = MibTableColumn
pm404AlmLine1TempHighWngPortn = _Pm404AlmLine1TempHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 1, 32, 1, 9),
    _Pm404AlmLine1TempHighWngPortn_Type()
)
pm404AlmLine1TempHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine1TempHighWngPortn.setStatus("current")
_Pm404AlmLine1RxPwrLowWngPortn_Type = EkiOnOff
_Pm404AlmLine1RxPwrLowWngPortn_Object = MibTableColumn
pm404AlmLine1RxPwrLowWngPortn = _Pm404AlmLine1RxPwrLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 1, 32, 1, 16),
    _Pm404AlmLine1RxPwrLowWngPortn_Type()
)
pm404AlmLine1RxPwrLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine1RxPwrLowWngPortn.setStatus("current")
_Pm404AlmLine1RxPwrHighWngPortn_Type = EkiOnOff
_Pm404AlmLine1RxPwrHighWngPortn_Object = MibTableColumn
pm404AlmLine1RxPwrHighWngPortn = _Pm404AlmLine1RxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 1, 32, 1, 17),
    _Pm404AlmLine1RxPwrHighWngPortn_Type()
)
pm404AlmLine1RxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine1RxPwrHighWngPortn.setStatus("current")
_Pm404AlmClientUrg_ObjectIdentity = ObjectIdentity
pm404AlmClientUrg = _Pm404AlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 2)
)
_Pm404Almline1SfpAlmDdmTable_Object = MibTable
pm404Almline1SfpAlmDdmTable = _Pm404Almline1SfpAlmDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 2, 24)
)
if mibBuilder.loadTexts:
    pm404Almline1SfpAlmDdmTable.setStatus("current")
_Pm404Almline1SfpAlmDdmEntry_Object = MibTableRow
pm404Almline1SfpAlmDdmEntry = _Pm404Almline1SfpAlmDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 2, 24, 1)
)
pm404Almline1SfpAlmDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm404-MIB", "pm404Almline1SfpAlmDdmIndex"),
)
if mibBuilder.loadTexts:
    pm404Almline1SfpAlmDdmEntry.setStatus("current")


class _Pm404Almline1SfpAlmDdmIndex_Type(Integer32):
    """Custom type pm404Almline1SfpAlmDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm404Almline1SfpAlmDdmIndex_Type.__name__ = "Integer32"
_Pm404Almline1SfpAlmDdmIndex_Object = MibTableColumn
pm404Almline1SfpAlmDdmIndex = _Pm404Almline1SfpAlmDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 2, 24, 1, 1),
    _Pm404Almline1SfpAlmDdmIndex_Type()
)
pm404Almline1SfpAlmDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404Almline1SfpAlmDdmIndex.setStatus("current")
_Pm404AlmLine1TxPwrLowAlaPortn_Type = EkiOnOff
_Pm404AlmLine1TxPwrLowAlaPortn_Object = MibTableColumn
pm404AlmLine1TxPwrLowAlaPortn = _Pm404AlmLine1TxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 2, 24, 1, 2),
    _Pm404AlmLine1TxPwrLowAlaPortn_Type()
)
pm404AlmLine1TxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine1TxPwrLowAlaPortn.setStatus("current")
_Pm404AlmLine1Line1TxPwrHighAlaPortn_Type = EkiOnOff
_Pm404AlmLine1Line1TxPwrHighAlaPortn_Object = MibTableColumn
pm404AlmLine1Line1TxPwrHighAlaPortn = _Pm404AlmLine1Line1TxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 2, 24, 1, 3),
    _Pm404AlmLine1Line1TxPwrHighAlaPortn_Type()
)
pm404AlmLine1Line1TxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine1Line1TxPwrHighAlaPortn.setStatus("current")
_Pm404AlmLine1TxBiasLowAlaPortn_Type = EkiOnOff
_Pm404AlmLine1TxBiasLowAlaPortn_Object = MibTableColumn
pm404AlmLine1TxBiasLowAlaPortn = _Pm404AlmLine1TxBiasLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 2, 24, 1, 4),
    _Pm404AlmLine1TxBiasLowAlaPortn_Type()
)
pm404AlmLine1TxBiasLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine1TxBiasLowAlaPortn.setStatus("current")
_Pm404AlmLine1TxBiasHighAlaPortn_Type = EkiOnOff
_Pm404AlmLine1TxBiasHighAlaPortn_Object = MibTableColumn
pm404AlmLine1TxBiasHighAlaPortn = _Pm404AlmLine1TxBiasHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 2, 24, 1, 5),
    _Pm404AlmLine1TxBiasHighAlaPortn_Type()
)
pm404AlmLine1TxBiasHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine1TxBiasHighAlaPortn.setStatus("current")
_Pm404AlmLine1VccLowAlaPortn_Type = EkiOnOff
_Pm404AlmLine1VccLowAlaPortn_Object = MibTableColumn
pm404AlmLine1VccLowAlaPortn = _Pm404AlmLine1VccLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 2, 24, 1, 6),
    _Pm404AlmLine1VccLowAlaPortn_Type()
)
pm404AlmLine1VccLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine1VccLowAlaPortn.setStatus("current")
_Pm404AlmLine1VccHighAlaPortn_Type = EkiOnOff
_Pm404AlmLine1VccHighAlaPortn_Object = MibTableColumn
pm404AlmLine1VccHighAlaPortn = _Pm404AlmLine1VccHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 2, 24, 1, 7),
    _Pm404AlmLine1VccHighAlaPortn_Type()
)
pm404AlmLine1VccHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine1VccHighAlaPortn.setStatus("current")
_Pm404AlmLine1TempLowAlaPortn_Type = EkiOnOff
_Pm404AlmLine1TempLowAlaPortn_Object = MibTableColumn
pm404AlmLine1TempLowAlaPortn = _Pm404AlmLine1TempLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 2, 24, 1, 8),
    _Pm404AlmLine1TempLowAlaPortn_Type()
)
pm404AlmLine1TempLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine1TempLowAlaPortn.setStatus("current")
_Pm404AlmLine1TempHighAlaPortn_Type = EkiOnOff
_Pm404AlmLine1TempHighAlaPortn_Object = MibTableColumn
pm404AlmLine1TempHighAlaPortn = _Pm404AlmLine1TempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 2, 24, 1, 9),
    _Pm404AlmLine1TempHighAlaPortn_Type()
)
pm404AlmLine1TempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine1TempHighAlaPortn.setStatus("current")
_Pm404AlmLine1RxPwrLowAlaPortn_Type = EkiOnOff
_Pm404AlmLine1RxPwrLowAlaPortn_Object = MibTableColumn
pm404AlmLine1RxPwrLowAlaPortn = _Pm404AlmLine1RxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 2, 24, 1, 16),
    _Pm404AlmLine1RxPwrLowAlaPortn_Type()
)
pm404AlmLine1RxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine1RxPwrLowAlaPortn.setStatus("current")
_Pm404AlmLine1RxPwrHighAlaPortn_Type = EkiOnOff
_Pm404AlmLine1RxPwrHighAlaPortn_Object = MibTableColumn
pm404AlmLine1RxPwrHighAlaPortn = _Pm404AlmLine1RxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 2, 24, 1, 17),
    _Pm404AlmLine1RxPwrHighAlaPortn_Type()
)
pm404AlmLine1RxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine1RxPwrHighAlaPortn.setStatus("current")
_Pm404AlmClientCrit_ObjectIdentity = ObjectIdentity
pm404AlmClientCrit = _Pm404AlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 3)
)
_Pm404AlmsynthAlmLine1Table_Object = MibTable
pm404AlmsynthAlmLine1Table = _Pm404AlmsynthAlmLine1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    pm404AlmsynthAlmLine1Table.setStatus("current")
_Pm404AlmsynthAlmLine1Entry_Object = MibTableRow
pm404AlmsynthAlmLine1Entry = _Pm404AlmsynthAlmLine1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 3, 8, 1)
)
pm404AlmsynthAlmLine1Entry.setIndexNames(
    (0, "EKINOPS-Pm404-MIB", "pm404AlmsynthAlmLine1Index"),
)
if mibBuilder.loadTexts:
    pm404AlmsynthAlmLine1Entry.setStatus("current")


class _Pm404AlmsynthAlmLine1Index_Type(Integer32):
    """Custom type pm404AlmsynthAlmLine1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm404AlmsynthAlmLine1Index_Type.__name__ = "Integer32"
_Pm404AlmsynthAlmLine1Index_Object = MibTableColumn
pm404AlmsynthAlmLine1Index = _Pm404AlmsynthAlmLine1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 3, 8, 1, 1),
    _Pm404AlmsynthAlmLine1Index_Type()
)
pm404AlmsynthAlmLine1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmsynthAlmLine1Index.setStatus("current")
_Pm404AlmLine1SfpAbsentPortn_Type = EkiOnOff
_Pm404AlmLine1SfpAbsentPortn_Object = MibTableColumn
pm404AlmLine1SfpAbsentPortn = _Pm404AlmLine1SfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 3, 8, 1, 2),
    _Pm404AlmLine1SfpAbsentPortn_Type()
)
pm404AlmLine1SfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine1SfpAbsentPortn.setStatus("current")
_Pm404AlmLine1DdmAbsentPortn_Type = EkiOnOff
_Pm404AlmLine1DdmAbsentPortn_Object = MibTableColumn
pm404AlmLine1DdmAbsentPortn = _Pm404AlmLine1DdmAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 3, 8, 1, 3),
    _Pm404AlmLine1DdmAbsentPortn_Type()
)
pm404AlmLine1DdmAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine1DdmAbsentPortn.setStatus("current")
_Pm404AlmLine1HwFailAccPortn_Type = EkiOnOff
_Pm404AlmLine1HwFailAccPortn_Object = MibTableColumn
pm404AlmLine1HwFailAccPortn = _Pm404AlmLine1HwFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 3, 8, 1, 5),
    _Pm404AlmLine1HwFailAccPortn_Type()
)
pm404AlmLine1HwFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine1HwFailAccPortn.setStatus("current")
_Pm404AlmLine1LsdPortn_Type = EkiOnOff
_Pm404AlmLine1LsdPortn_Object = MibTableColumn
pm404AlmLine1LsdPortn = _Pm404AlmLine1LsdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 3, 8, 1, 6),
    _Pm404AlmLine1LsdPortn_Type()
)
pm404AlmLine1LsdPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine1LsdPortn.setStatus("current")
_Pm404AlmLine1LocalOosPortn_Type = EkiOnOff
_Pm404AlmLine1LocalOosPortn_Object = MibTableColumn
pm404AlmLine1LocalOosPortn = _Pm404AlmLine1LocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 3, 8, 1, 7),
    _Pm404AlmLine1LocalOosPortn_Type()
)
pm404AlmLine1LocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine1LocalOosPortn.setStatus("current")
_Pm404AlmLine1DwCaisPortn_Type = EkiOnOff
_Pm404AlmLine1DwCaisPortn_Object = MibTableColumn
pm404AlmLine1DwCaisPortn = _Pm404AlmLine1DwCaisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 3, 8, 1, 9),
    _Pm404AlmLine1DwCaisPortn_Type()
)
pm404AlmLine1DwCaisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine1DwCaisPortn.setStatus("current")
_Pm404AlmLine1SfpDdmWarningPortn_Type = EkiOnOff
_Pm404AlmLine1SfpDdmWarningPortn_Object = MibTableColumn
pm404AlmLine1SfpDdmWarningPortn = _Pm404AlmLine1SfpDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 3, 8, 1, 10),
    _Pm404AlmLine1SfpDdmWarningPortn_Type()
)
pm404AlmLine1SfpDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine1SfpDdmWarningPortn.setStatus("current")
_Pm404AlmLine1SfpDdmAlmPortn_Type = EkiOnOff
_Pm404AlmLine1SfpDdmAlmPortn_Object = MibTableColumn
pm404AlmLine1SfpDdmAlmPortn = _Pm404AlmLine1SfpDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 3, 8, 1, 11),
    _Pm404AlmLine1SfpDdmAlmPortn_Type()
)
pm404AlmLine1SfpDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine1SfpDdmAlmPortn.setStatus("current")
_Pm404AlmLine1FailAccPortn_Type = EkiOnOff
_Pm404AlmLine1FailAccPortn_Object = MibTableColumn
pm404AlmLine1FailAccPortn = _Pm404AlmLine1FailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 3, 8, 1, 13),
    _Pm404AlmLine1FailAccPortn_Type()
)
pm404AlmLine1FailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine1FailAccPortn.setStatus("current")
_Pm404Almline1AccessioAlmTable_Object = MibTable
pm404Almline1AccessioAlmTable = _Pm404Almline1AccessioAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 3, 16)
)
if mibBuilder.loadTexts:
    pm404Almline1AccessioAlmTable.setStatus("current")
_Pm404Almline1AccessioAlmEntry_Object = MibTableRow
pm404Almline1AccessioAlmEntry = _Pm404Almline1AccessioAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 3, 16, 1)
)
pm404Almline1AccessioAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm404-MIB", "pm404Almline1AccessioAlmIndex"),
)
if mibBuilder.loadTexts:
    pm404Almline1AccessioAlmEntry.setStatus("current")


class _Pm404Almline1AccessioAlmIndex_Type(Integer32):
    """Custom type pm404Almline1AccessioAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm404Almline1AccessioAlmIndex_Type.__name__ = "Integer32"
_Pm404Almline1AccessioAlmIndex_Object = MibTableColumn
pm404Almline1AccessioAlmIndex = _Pm404Almline1AccessioAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 3, 16, 1, 1),
    _Pm404Almline1AccessioAlmIndex_Type()
)
pm404Almline1AccessioAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404Almline1AccessioAlmIndex.setStatus("current")
_Pm404AlmLine1LasFailPortn_Type = EkiOnOff
_Pm404AlmLine1LasFailPortn_Object = MibTableColumn
pm404AlmLine1LasFailPortn = _Pm404AlmLine1LasFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 3, 16, 1, 2),
    _Pm404AlmLine1LasFailPortn_Type()
)
pm404AlmLine1LasFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine1LasFailPortn.setStatus("current")
_Pm404AlmLine1LosPortn_Type = EkiOnOff
_Pm404AlmLine1LosPortn_Object = MibTableColumn
pm404AlmLine1LosPortn = _Pm404AlmLine1LosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 3, 16, 1, 5),
    _Pm404AlmLine1LosPortn_Type()
)
pm404AlmLine1LosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine1LosPortn.setStatus("current")
_Pm404AlmLine1LosCdrPortn_Type = EkiOnOff
_Pm404AlmLine1LosCdrPortn_Object = MibTableColumn
pm404AlmLine1LosCdrPortn = _Pm404AlmLine1LosCdrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 3, 16, 1, 7),
    _Pm404AlmLine1LosCdrPortn_Type()
)
pm404AlmLine1LosCdrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine1LosCdrPortn.setStatus("current")
_Pm404AlmLine1ErrSigCdrPortn_Type = EkiOnOff
_Pm404AlmLine1ErrSigCdrPortn_Object = MibTableColumn
pm404AlmLine1ErrSigCdrPortn = _Pm404AlmLine1ErrSigCdrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 2, 3, 16, 1, 8),
    _Pm404AlmLine1ErrSigCdrPortn_Type()
)
pm404AlmLine1ErrSigCdrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine1ErrSigCdrPortn.setStatus("current")
_Pm404AlmLine_ObjectIdentity = ObjectIdentity
pm404AlmLine = _Pm404AlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3)
)
_Pm404AlmLineNurg_ObjectIdentity = ObjectIdentity
pm404AlmLineNurg = _Pm404AlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 1)
)
_Pm404Almline2SfpWarnDdmTable_Object = MibTable
pm404Almline2SfpWarnDdmTable = _Pm404Almline2SfpWarnDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 1, 36)
)
if mibBuilder.loadTexts:
    pm404Almline2SfpWarnDdmTable.setStatus("current")
_Pm404Almline2SfpWarnDdmEntry_Object = MibTableRow
pm404Almline2SfpWarnDdmEntry = _Pm404Almline2SfpWarnDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 1, 36, 1)
)
pm404Almline2SfpWarnDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm404-MIB", "pm404Almline2SfpWarnDdmIndex"),
)
if mibBuilder.loadTexts:
    pm404Almline2SfpWarnDdmEntry.setStatus("current")


class _Pm404Almline2SfpWarnDdmIndex_Type(Integer32):
    """Custom type pm404Almline2SfpWarnDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm404Almline2SfpWarnDdmIndex_Type.__name__ = "Integer32"
_Pm404Almline2SfpWarnDdmIndex_Object = MibTableColumn
pm404Almline2SfpWarnDdmIndex = _Pm404Almline2SfpWarnDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 1, 36, 1, 1),
    _Pm404Almline2SfpWarnDdmIndex_Type()
)
pm404Almline2SfpWarnDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404Almline2SfpWarnDdmIndex.setStatus("current")
_Pm404AlmLine2TxPwLowWngPortn_Type = EkiOnOff
_Pm404AlmLine2TxPwLowWngPortn_Object = MibTableColumn
pm404AlmLine2TxPwLowWngPortn = _Pm404AlmLine2TxPwLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 1, 36, 1, 2),
    _Pm404AlmLine2TxPwLowWngPortn_Type()
)
pm404AlmLine2TxPwLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine2TxPwLowWngPortn.setStatus("current")
_Pm404AlmLine2TxPwrHighWngPortn_Type = EkiOnOff
_Pm404AlmLine2TxPwrHighWngPortn_Object = MibTableColumn
pm404AlmLine2TxPwrHighWngPortn = _Pm404AlmLine2TxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 1, 36, 1, 3),
    _Pm404AlmLine2TxPwrHighWngPortn_Type()
)
pm404AlmLine2TxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine2TxPwrHighWngPortn.setStatus("current")
_Pm404AlmLine2TxBiasLowWngPortn_Type = EkiOnOff
_Pm404AlmLine2TxBiasLowWngPortn_Object = MibTableColumn
pm404AlmLine2TxBiasLowWngPortn = _Pm404AlmLine2TxBiasLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 1, 36, 1, 4),
    _Pm404AlmLine2TxBiasLowWngPortn_Type()
)
pm404AlmLine2TxBiasLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine2TxBiasLowWngPortn.setStatus("current")
_Pm404AlmLine2TxBiasHighWngPortn_Type = EkiOnOff
_Pm404AlmLine2TxBiasHighWngPortn_Object = MibTableColumn
pm404AlmLine2TxBiasHighWngPortn = _Pm404AlmLine2TxBiasHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 1, 36, 1, 5),
    _Pm404AlmLine2TxBiasHighWngPortn_Type()
)
pm404AlmLine2TxBiasHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine2TxBiasHighWngPortn.setStatus("current")
_Pm404AlmLine2VccLowWngPortn_Type = EkiOnOff
_Pm404AlmLine2VccLowWngPortn_Object = MibTableColumn
pm404AlmLine2VccLowWngPortn = _Pm404AlmLine2VccLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 1, 36, 1, 6),
    _Pm404AlmLine2VccLowWngPortn_Type()
)
pm404AlmLine2VccLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine2VccLowWngPortn.setStatus("current")
_Pm404AlmLine2VccHighWngPortn_Type = EkiOnOff
_Pm404AlmLine2VccHighWngPortn_Object = MibTableColumn
pm404AlmLine2VccHighWngPortn = _Pm404AlmLine2VccHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 1, 36, 1, 7),
    _Pm404AlmLine2VccHighWngPortn_Type()
)
pm404AlmLine2VccHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine2VccHighWngPortn.setStatus("current")
_Pm404AlmLine2TempLowWngPortn_Type = EkiOnOff
_Pm404AlmLine2TempLowWngPortn_Object = MibTableColumn
pm404AlmLine2TempLowWngPortn = _Pm404AlmLine2TempLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 1, 36, 1, 8),
    _Pm404AlmLine2TempLowWngPortn_Type()
)
pm404AlmLine2TempLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine2TempLowWngPortn.setStatus("current")
_Pm404AlmLine2TempHighWngPortn_Type = EkiOnOff
_Pm404AlmLine2TempHighWngPortn_Object = MibTableColumn
pm404AlmLine2TempHighWngPortn = _Pm404AlmLine2TempHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 1, 36, 1, 9),
    _Pm404AlmLine2TempHighWngPortn_Type()
)
pm404AlmLine2TempHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine2TempHighWngPortn.setStatus("current")
_Pm404AlmLine2RxPwrLowWngPortn_Type = EkiOnOff
_Pm404AlmLine2RxPwrLowWngPortn_Object = MibTableColumn
pm404AlmLine2RxPwrLowWngPortn = _Pm404AlmLine2RxPwrLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 1, 36, 1, 16),
    _Pm404AlmLine2RxPwrLowWngPortn_Type()
)
pm404AlmLine2RxPwrLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine2RxPwrLowWngPortn.setStatus("current")
_Pm404AlmLine2RxPwrHighWngPortn_Type = EkiOnOff
_Pm404AlmLine2RxPwrHighWngPortn_Object = MibTableColumn
pm404AlmLine2RxPwrHighWngPortn = _Pm404AlmLine2RxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 1, 36, 1, 17),
    _Pm404AlmLine2RxPwrHighWngPortn_Type()
)
pm404AlmLine2RxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine2RxPwrHighWngPortn.setStatus("current")
_Pm404AlmLineUrg_ObjectIdentity = ObjectIdentity
pm404AlmLineUrg = _Pm404AlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 2)
)
_Pm404Almline2SfpAlmDdmTable_Object = MibTable
pm404Almline2SfpAlmDdmTable = _Pm404Almline2SfpAlmDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 2, 28)
)
if mibBuilder.loadTexts:
    pm404Almline2SfpAlmDdmTable.setStatus("current")
_Pm404Almline2SfpAlmDdmEntry_Object = MibTableRow
pm404Almline2SfpAlmDdmEntry = _Pm404Almline2SfpAlmDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 2, 28, 1)
)
pm404Almline2SfpAlmDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm404-MIB", "pm404Almline2SfpAlmDdmIndex"),
)
if mibBuilder.loadTexts:
    pm404Almline2SfpAlmDdmEntry.setStatus("current")


class _Pm404Almline2SfpAlmDdmIndex_Type(Integer32):
    """Custom type pm404Almline2SfpAlmDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm404Almline2SfpAlmDdmIndex_Type.__name__ = "Integer32"
_Pm404Almline2SfpAlmDdmIndex_Object = MibTableColumn
pm404Almline2SfpAlmDdmIndex = _Pm404Almline2SfpAlmDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 2, 28, 1, 1),
    _Pm404Almline2SfpAlmDdmIndex_Type()
)
pm404Almline2SfpAlmDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404Almline2SfpAlmDdmIndex.setStatus("current")
_Pm404AlmLine2TxPwrLowAlaPortn_Type = EkiOnOff
_Pm404AlmLine2TxPwrLowAlaPortn_Object = MibTableColumn
pm404AlmLine2TxPwrLowAlaPortn = _Pm404AlmLine2TxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 2, 28, 1, 2),
    _Pm404AlmLine2TxPwrLowAlaPortn_Type()
)
pm404AlmLine2TxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine2TxPwrLowAlaPortn.setStatus("current")
_Pm404AlmLine2Line2TxPwrHighAlaPortn_Type = EkiOnOff
_Pm404AlmLine2Line2TxPwrHighAlaPortn_Object = MibTableColumn
pm404AlmLine2Line2TxPwrHighAlaPortn = _Pm404AlmLine2Line2TxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 2, 28, 1, 3),
    _Pm404AlmLine2Line2TxPwrHighAlaPortn_Type()
)
pm404AlmLine2Line2TxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine2Line2TxPwrHighAlaPortn.setStatus("current")
_Pm404AlmLine2TxBiasLowAlaPortn_Type = EkiOnOff
_Pm404AlmLine2TxBiasLowAlaPortn_Object = MibTableColumn
pm404AlmLine2TxBiasLowAlaPortn = _Pm404AlmLine2TxBiasLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 2, 28, 1, 4),
    _Pm404AlmLine2TxBiasLowAlaPortn_Type()
)
pm404AlmLine2TxBiasLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine2TxBiasLowAlaPortn.setStatus("current")
_Pm404AlmLine2TxBiasHighAlaPortn_Type = EkiOnOff
_Pm404AlmLine2TxBiasHighAlaPortn_Object = MibTableColumn
pm404AlmLine2TxBiasHighAlaPortn = _Pm404AlmLine2TxBiasHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 2, 28, 1, 5),
    _Pm404AlmLine2TxBiasHighAlaPortn_Type()
)
pm404AlmLine2TxBiasHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine2TxBiasHighAlaPortn.setStatus("current")
_Pm404AlmLine2VccLowAlaPortn_Type = EkiOnOff
_Pm404AlmLine2VccLowAlaPortn_Object = MibTableColumn
pm404AlmLine2VccLowAlaPortn = _Pm404AlmLine2VccLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 2, 28, 1, 6),
    _Pm404AlmLine2VccLowAlaPortn_Type()
)
pm404AlmLine2VccLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine2VccLowAlaPortn.setStatus("current")
_Pm404AlmLine2VccHighAlaPortn_Type = EkiOnOff
_Pm404AlmLine2VccHighAlaPortn_Object = MibTableColumn
pm404AlmLine2VccHighAlaPortn = _Pm404AlmLine2VccHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 2, 28, 1, 7),
    _Pm404AlmLine2VccHighAlaPortn_Type()
)
pm404AlmLine2VccHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine2VccHighAlaPortn.setStatus("current")
_Pm404AlmLine2TempLowAlaPortn_Type = EkiOnOff
_Pm404AlmLine2TempLowAlaPortn_Object = MibTableColumn
pm404AlmLine2TempLowAlaPortn = _Pm404AlmLine2TempLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 2, 28, 1, 8),
    _Pm404AlmLine2TempLowAlaPortn_Type()
)
pm404AlmLine2TempLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine2TempLowAlaPortn.setStatus("current")
_Pm404AlmLine2TempHighAlaPortn_Type = EkiOnOff
_Pm404AlmLine2TempHighAlaPortn_Object = MibTableColumn
pm404AlmLine2TempHighAlaPortn = _Pm404AlmLine2TempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 2, 28, 1, 9),
    _Pm404AlmLine2TempHighAlaPortn_Type()
)
pm404AlmLine2TempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine2TempHighAlaPortn.setStatus("current")
_Pm404AlmLine2RxPwrLowAlaPortn_Type = EkiOnOff
_Pm404AlmLine2RxPwrLowAlaPortn_Object = MibTableColumn
pm404AlmLine2RxPwrLowAlaPortn = _Pm404AlmLine2RxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 2, 28, 1, 16),
    _Pm404AlmLine2RxPwrLowAlaPortn_Type()
)
pm404AlmLine2RxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine2RxPwrLowAlaPortn.setStatus("current")
_Pm404AlmLine2RxPwrHighAlaPortn_Type = EkiOnOff
_Pm404AlmLine2RxPwrHighAlaPortn_Object = MibTableColumn
pm404AlmLine2RxPwrHighAlaPortn = _Pm404AlmLine2RxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 2, 28, 1, 17),
    _Pm404AlmLine2RxPwrHighAlaPortn_Type()
)
pm404AlmLine2RxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine2RxPwrHighAlaPortn.setStatus("current")
_Pm404AlmLineCrit_ObjectIdentity = ObjectIdentity
pm404AlmLineCrit = _Pm404AlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 3)
)
_Pm404AlmsynthAlmLine2Table_Object = MibTable
pm404AlmsynthAlmLine2Table = _Pm404AlmsynthAlmLine2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 3, 12)
)
if mibBuilder.loadTexts:
    pm404AlmsynthAlmLine2Table.setStatus("current")
_Pm404AlmsynthAlmLine2Entry_Object = MibTableRow
pm404AlmsynthAlmLine2Entry = _Pm404AlmsynthAlmLine2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 3, 12, 1)
)
pm404AlmsynthAlmLine2Entry.setIndexNames(
    (0, "EKINOPS-Pm404-MIB", "pm404AlmsynthAlmLine2Index"),
)
if mibBuilder.loadTexts:
    pm404AlmsynthAlmLine2Entry.setStatus("current")


class _Pm404AlmsynthAlmLine2Index_Type(Integer32):
    """Custom type pm404AlmsynthAlmLine2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm404AlmsynthAlmLine2Index_Type.__name__ = "Integer32"
_Pm404AlmsynthAlmLine2Index_Object = MibTableColumn
pm404AlmsynthAlmLine2Index = _Pm404AlmsynthAlmLine2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 3, 12, 1, 1),
    _Pm404AlmsynthAlmLine2Index_Type()
)
pm404AlmsynthAlmLine2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmsynthAlmLine2Index.setStatus("current")
_Pm404AlmLine2SfpAbsentPortn_Type = EkiOnOff
_Pm404AlmLine2SfpAbsentPortn_Object = MibTableColumn
pm404AlmLine2SfpAbsentPortn = _Pm404AlmLine2SfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 3, 12, 1, 2),
    _Pm404AlmLine2SfpAbsentPortn_Type()
)
pm404AlmLine2SfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine2SfpAbsentPortn.setStatus("current")
_Pm404AlmLine2DdmAbsentPortn_Type = EkiOnOff
_Pm404AlmLine2DdmAbsentPortn_Object = MibTableColumn
pm404AlmLine2DdmAbsentPortn = _Pm404AlmLine2DdmAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 3, 12, 1, 3),
    _Pm404AlmLine2DdmAbsentPortn_Type()
)
pm404AlmLine2DdmAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine2DdmAbsentPortn.setStatus("current")
_Pm404AlmLine2HwFailPortn_Type = EkiOnOff
_Pm404AlmLine2HwFailPortn_Object = MibTableColumn
pm404AlmLine2HwFailPortn = _Pm404AlmLine2HwFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 3, 12, 1, 5),
    _Pm404AlmLine2HwFailPortn_Type()
)
pm404AlmLine2HwFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine2HwFailPortn.setStatus("current")
_Pm404AlmLine2LsdPortn_Type = EkiOnOff
_Pm404AlmLine2LsdPortn_Object = MibTableColumn
pm404AlmLine2LsdPortn = _Pm404AlmLine2LsdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 3, 12, 1, 6),
    _Pm404AlmLine2LsdPortn_Type()
)
pm404AlmLine2LsdPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine2LsdPortn.setStatus("current")
_Pm404AlmLine2LocalOosPortn_Type = EkiOnOff
_Pm404AlmLine2LocalOosPortn_Object = MibTableColumn
pm404AlmLine2LocalOosPortn = _Pm404AlmLine2LocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 3, 12, 1, 7),
    _Pm404AlmLine2LocalOosPortn_Type()
)
pm404AlmLine2LocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine2LocalOosPortn.setStatus("current")
_Pm404AlmLine2DwCaisPortn_Type = EkiOnOff
_Pm404AlmLine2DwCaisPortn_Object = MibTableColumn
pm404AlmLine2DwCaisPortn = _Pm404AlmLine2DwCaisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 3, 12, 1, 9),
    _Pm404AlmLine2DwCaisPortn_Type()
)
pm404AlmLine2DwCaisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine2DwCaisPortn.setStatus("current")
_Pm404AlmLine2DdmWarningPortn_Type = EkiOnOff
_Pm404AlmLine2DdmWarningPortn_Object = MibTableColumn
pm404AlmLine2DdmWarningPortn = _Pm404AlmLine2DdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 3, 12, 1, 10),
    _Pm404AlmLine2DdmWarningPortn_Type()
)
pm404AlmLine2DdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine2DdmWarningPortn.setStatus("current")
_Pm404AlmLine2DdmAlmPortn_Type = EkiOnOff
_Pm404AlmLine2DdmAlmPortn_Object = MibTableColumn
pm404AlmLine2DdmAlmPortn = _Pm404AlmLine2DdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 3, 12, 1, 11),
    _Pm404AlmLine2DdmAlmPortn_Type()
)
pm404AlmLine2DdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine2DdmAlmPortn.setStatus("current")
_Pm404AlmLine2FailPortn_Type = EkiOnOff
_Pm404AlmLine2FailPortn_Object = MibTableColumn
pm404AlmLine2FailPortn = _Pm404AlmLine2FailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 3, 12, 1, 13),
    _Pm404AlmLine2FailPortn_Type()
)
pm404AlmLine2FailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine2FailPortn.setStatus("current")
_Pm404Almline2AccessioAlmTable_Object = MibTable
pm404Almline2AccessioAlmTable = _Pm404Almline2AccessioAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 3, 20)
)
if mibBuilder.loadTexts:
    pm404Almline2AccessioAlmTable.setStatus("current")
_Pm404Almline2AccessioAlmEntry_Object = MibTableRow
pm404Almline2AccessioAlmEntry = _Pm404Almline2AccessioAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 3, 20, 1)
)
pm404Almline2AccessioAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm404-MIB", "pm404Almline2AccessioAlmIndex"),
)
if mibBuilder.loadTexts:
    pm404Almline2AccessioAlmEntry.setStatus("current")


class _Pm404Almline2AccessioAlmIndex_Type(Integer32):
    """Custom type pm404Almline2AccessioAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm404Almline2AccessioAlmIndex_Type.__name__ = "Integer32"
_Pm404Almline2AccessioAlmIndex_Object = MibTableColumn
pm404Almline2AccessioAlmIndex = _Pm404Almline2AccessioAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 3, 20, 1, 1),
    _Pm404Almline2AccessioAlmIndex_Type()
)
pm404Almline2AccessioAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404Almline2AccessioAlmIndex.setStatus("current")
_Pm404AlmLine2LasFailPortn_Type = EkiOnOff
_Pm404AlmLine2LasFailPortn_Object = MibTableColumn
pm404AlmLine2LasFailPortn = _Pm404AlmLine2LasFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 3, 20, 1, 2),
    _Pm404AlmLine2LasFailPortn_Type()
)
pm404AlmLine2LasFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine2LasFailPortn.setStatus("current")
_Pm404AlmLine2LosPortn_Type = EkiOnOff
_Pm404AlmLine2LosPortn_Object = MibTableColumn
pm404AlmLine2LosPortn = _Pm404AlmLine2LosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 3, 20, 1, 5),
    _Pm404AlmLine2LosPortn_Type()
)
pm404AlmLine2LosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine2LosPortn.setStatus("current")
_Pm404AlmLine2LosCdrPortn_Type = EkiOnOff
_Pm404AlmLine2LosCdrPortn_Object = MibTableColumn
pm404AlmLine2LosCdrPortn = _Pm404AlmLine2LosCdrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 3, 20, 1, 7),
    _Pm404AlmLine2LosCdrPortn_Type()
)
pm404AlmLine2LosCdrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine2LosCdrPortn.setStatus("current")
_Pm404AlmLine2ErrSigCdrPortn_Type = EkiOnOff
_Pm404AlmLine2ErrSigCdrPortn_Object = MibTableColumn
pm404AlmLine2ErrSigCdrPortn = _Pm404AlmLine2ErrSigCdrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 2, 3, 3, 20, 1, 8),
    _Pm404AlmLine2ErrSigCdrPortn_Type()
)
pm404AlmLine2ErrSigCdrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404AlmLine2ErrSigCdrPortn.setStatus("current")
_Pm404measures_ObjectIdentity = ObjectIdentity
pm404measures = _Pm404measures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3)
)
_Pm404MesrOther_ObjectIdentity = ObjectIdentity
pm404MesrOther = _Pm404MesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 1)
)
_Pm404MesrClient_ObjectIdentity = ObjectIdentity
pm404MesrClient = _Pm404MesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 2)
)
_Pm404Mesrline1TemperatureTable_Object = MibTable
pm404Mesrline1TemperatureTable = _Pm404Mesrline1TemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 2, 16)
)
if mibBuilder.loadTexts:
    pm404Mesrline1TemperatureTable.setStatus("current")
_Pm404Mesrline1TemperatureEntry_Object = MibTableRow
pm404Mesrline1TemperatureEntry = _Pm404Mesrline1TemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 2, 16, 1)
)
pm404Mesrline1TemperatureEntry.setIndexNames(
    (0, "EKINOPS-Pm404-MIB", "pm404Mesrline1TemperatureIndex"),
)
if mibBuilder.loadTexts:
    pm404Mesrline1TemperatureEntry.setStatus("current")


class _Pm404Mesrline1TemperatureIndex_Type(Integer32):
    """Custom type pm404Mesrline1TemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm404Mesrline1TemperatureIndex_Type.__name__ = "Integer32"
_Pm404Mesrline1TemperatureIndex_Object = MibTableColumn
pm404Mesrline1TemperatureIndex = _Pm404Mesrline1TemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 2, 16, 1, 1),
    _Pm404Mesrline1TemperatureIndex_Type()
)
pm404Mesrline1TemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404Mesrline1TemperatureIndex.setStatus("current")


class _Pm404Mesrline1TemperaturePortn_Type(Integer32):
    """Custom type pm404Mesrline1TemperaturePortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm404Mesrline1TemperaturePortn_Type.__name__ = "Integer32"
_Pm404Mesrline1TemperaturePortn_Object = MibTableColumn
pm404Mesrline1TemperaturePortn = _Pm404Mesrline1TemperaturePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 2, 16, 1, 2),
    _Pm404Mesrline1TemperaturePortn_Type()
)
pm404Mesrline1TemperaturePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404Mesrline1TemperaturePortn.setStatus("current")
_Pm404Mesrline1VoltTable_Object = MibTable
pm404Mesrline1VoltTable = _Pm404Mesrline1VoltTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 2, 24)
)
if mibBuilder.loadTexts:
    pm404Mesrline1VoltTable.setStatus("current")
_Pm404Mesrline1VoltEntry_Object = MibTableRow
pm404Mesrline1VoltEntry = _Pm404Mesrline1VoltEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 2, 24, 1)
)
pm404Mesrline1VoltEntry.setIndexNames(
    (0, "EKINOPS-Pm404-MIB", "pm404Mesrline1VoltIndex"),
)
if mibBuilder.loadTexts:
    pm404Mesrline1VoltEntry.setStatus("current")


class _Pm404Mesrline1VoltIndex_Type(Integer32):
    """Custom type pm404Mesrline1VoltIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm404Mesrline1VoltIndex_Type.__name__ = "Integer32"
_Pm404Mesrline1VoltIndex_Object = MibTableColumn
pm404Mesrline1VoltIndex = _Pm404Mesrline1VoltIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 2, 24, 1, 1),
    _Pm404Mesrline1VoltIndex_Type()
)
pm404Mesrline1VoltIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404Mesrline1VoltIndex.setStatus("current")


class _Pm404Mesrline1VoltPortn_Type(Integer32):
    """Custom type pm404Mesrline1VoltPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm404Mesrline1VoltPortn_Type.__name__ = "Integer32"
_Pm404Mesrline1VoltPortn_Object = MibTableColumn
pm404Mesrline1VoltPortn = _Pm404Mesrline1VoltPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 2, 24, 1, 2),
    _Pm404Mesrline1VoltPortn_Type()
)
pm404Mesrline1VoltPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404Mesrline1VoltPortn.setStatus("current")
_Pm404Mesrline1TxBiasTable_Object = MibTable
pm404Mesrline1TxBiasTable = _Pm404Mesrline1TxBiasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 2, 32)
)
if mibBuilder.loadTexts:
    pm404Mesrline1TxBiasTable.setStatus("current")
_Pm404Mesrline1TxBiasEntry_Object = MibTableRow
pm404Mesrline1TxBiasEntry = _Pm404Mesrline1TxBiasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 2, 32, 1)
)
pm404Mesrline1TxBiasEntry.setIndexNames(
    (0, "EKINOPS-Pm404-MIB", "pm404Mesrline1TxBiasIndex"),
)
if mibBuilder.loadTexts:
    pm404Mesrline1TxBiasEntry.setStatus("current")


class _Pm404Mesrline1TxBiasIndex_Type(Integer32):
    """Custom type pm404Mesrline1TxBiasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm404Mesrline1TxBiasIndex_Type.__name__ = "Integer32"
_Pm404Mesrline1TxBiasIndex_Object = MibTableColumn
pm404Mesrline1TxBiasIndex = _Pm404Mesrline1TxBiasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 2, 32, 1, 1),
    _Pm404Mesrline1TxBiasIndex_Type()
)
pm404Mesrline1TxBiasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404Mesrline1TxBiasIndex.setStatus("current")


class _Pm404Mesrline1TxBiasPortn_Type(Integer32):
    """Custom type pm404Mesrline1TxBiasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm404Mesrline1TxBiasPortn_Type.__name__ = "Integer32"
_Pm404Mesrline1TxBiasPortn_Object = MibTableColumn
pm404Mesrline1TxBiasPortn = _Pm404Mesrline1TxBiasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 2, 32, 1, 2),
    _Pm404Mesrline1TxBiasPortn_Type()
)
pm404Mesrline1TxBiasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404Mesrline1TxBiasPortn.setStatus("current")
_Pm404Mesrline1TxPowerTable_Object = MibTable
pm404Mesrline1TxPowerTable = _Pm404Mesrline1TxPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 2, 40)
)
if mibBuilder.loadTexts:
    pm404Mesrline1TxPowerTable.setStatus("current")
_Pm404Mesrline1TxPowerEntry_Object = MibTableRow
pm404Mesrline1TxPowerEntry = _Pm404Mesrline1TxPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 2, 40, 1)
)
pm404Mesrline1TxPowerEntry.setIndexNames(
    (0, "EKINOPS-Pm404-MIB", "pm404Mesrline1TxPowerIndex"),
)
if mibBuilder.loadTexts:
    pm404Mesrline1TxPowerEntry.setStatus("current")


class _Pm404Mesrline1TxPowerIndex_Type(Integer32):
    """Custom type pm404Mesrline1TxPowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm404Mesrline1TxPowerIndex_Type.__name__ = "Integer32"
_Pm404Mesrline1TxPowerIndex_Object = MibTableColumn
pm404Mesrline1TxPowerIndex = _Pm404Mesrline1TxPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 2, 40, 1, 1),
    _Pm404Mesrline1TxPowerIndex_Type()
)
pm404Mesrline1TxPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404Mesrline1TxPowerIndex.setStatus("current")


class _Pm404Mesrline1TxPowerPortn_Type(Integer32):
    """Custom type pm404Mesrline1TxPowerPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm404Mesrline1TxPowerPortn_Type.__name__ = "Integer32"
_Pm404Mesrline1TxPowerPortn_Object = MibTableColumn
pm404Mesrline1TxPowerPortn = _Pm404Mesrline1TxPowerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 2, 40, 1, 2),
    _Pm404Mesrline1TxPowerPortn_Type()
)
pm404Mesrline1TxPowerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404Mesrline1TxPowerPortn.setStatus("current")
_Pm404Mesrline1RxPowerTable_Object = MibTable
pm404Mesrline1RxPowerTable = _Pm404Mesrline1RxPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 2, 48)
)
if mibBuilder.loadTexts:
    pm404Mesrline1RxPowerTable.setStatus("current")
_Pm404Mesrline1RxPowerEntry_Object = MibTableRow
pm404Mesrline1RxPowerEntry = _Pm404Mesrline1RxPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 2, 48, 1)
)
pm404Mesrline1RxPowerEntry.setIndexNames(
    (0, "EKINOPS-Pm404-MIB", "pm404Mesrline1RxPowerIndex"),
)
if mibBuilder.loadTexts:
    pm404Mesrline1RxPowerEntry.setStatus("current")


class _Pm404Mesrline1RxPowerIndex_Type(Integer32):
    """Custom type pm404Mesrline1RxPowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm404Mesrline1RxPowerIndex_Type.__name__ = "Integer32"
_Pm404Mesrline1RxPowerIndex_Object = MibTableColumn
pm404Mesrline1RxPowerIndex = _Pm404Mesrline1RxPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 2, 48, 1, 1),
    _Pm404Mesrline1RxPowerIndex_Type()
)
pm404Mesrline1RxPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404Mesrline1RxPowerIndex.setStatus("current")


class _Pm404Mesrline1RxPowerPortn_Type(Integer32):
    """Custom type pm404Mesrline1RxPowerPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm404Mesrline1RxPowerPortn_Type.__name__ = "Integer32"
_Pm404Mesrline1RxPowerPortn_Object = MibTableColumn
pm404Mesrline1RxPowerPortn = _Pm404Mesrline1RxPowerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 2, 48, 1, 2),
    _Pm404Mesrline1RxPowerPortn_Type()
)
pm404Mesrline1RxPowerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404Mesrline1RxPowerPortn.setStatus("current")
_Pm404MesrLine_ObjectIdentity = ObjectIdentity
pm404MesrLine = _Pm404MesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 3)
)
_Pm404Mesrline2TemperatureTable_Object = MibTable
pm404Mesrline2TemperatureTable = _Pm404Mesrline2TemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 3, 20)
)
if mibBuilder.loadTexts:
    pm404Mesrline2TemperatureTable.setStatus("current")
_Pm404Mesrline2TemperatureEntry_Object = MibTableRow
pm404Mesrline2TemperatureEntry = _Pm404Mesrline2TemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 3, 20, 1)
)
pm404Mesrline2TemperatureEntry.setIndexNames(
    (0, "EKINOPS-Pm404-MIB", "pm404Mesrline2TemperatureIndex"),
)
if mibBuilder.loadTexts:
    pm404Mesrline2TemperatureEntry.setStatus("current")


class _Pm404Mesrline2TemperatureIndex_Type(Integer32):
    """Custom type pm404Mesrline2TemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm404Mesrline2TemperatureIndex_Type.__name__ = "Integer32"
_Pm404Mesrline2TemperatureIndex_Object = MibTableColumn
pm404Mesrline2TemperatureIndex = _Pm404Mesrline2TemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 3, 20, 1, 1),
    _Pm404Mesrline2TemperatureIndex_Type()
)
pm404Mesrline2TemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404Mesrline2TemperatureIndex.setStatus("current")


class _Pm404Mesrline2TemperaturePortn_Type(Integer32):
    """Custom type pm404Mesrline2TemperaturePortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm404Mesrline2TemperaturePortn_Type.__name__ = "Integer32"
_Pm404Mesrline2TemperaturePortn_Object = MibTableColumn
pm404Mesrline2TemperaturePortn = _Pm404Mesrline2TemperaturePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 3, 20, 1, 2),
    _Pm404Mesrline2TemperaturePortn_Type()
)
pm404Mesrline2TemperaturePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404Mesrline2TemperaturePortn.setStatus("current")
_Pm404Mesrline2VoltTable_Object = MibTable
pm404Mesrline2VoltTable = _Pm404Mesrline2VoltTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 3, 28)
)
if mibBuilder.loadTexts:
    pm404Mesrline2VoltTable.setStatus("current")
_Pm404Mesrline2VoltEntry_Object = MibTableRow
pm404Mesrline2VoltEntry = _Pm404Mesrline2VoltEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 3, 28, 1)
)
pm404Mesrline2VoltEntry.setIndexNames(
    (0, "EKINOPS-Pm404-MIB", "pm404Mesrline2VoltIndex"),
)
if mibBuilder.loadTexts:
    pm404Mesrline2VoltEntry.setStatus("current")


class _Pm404Mesrline2VoltIndex_Type(Integer32):
    """Custom type pm404Mesrline2VoltIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm404Mesrline2VoltIndex_Type.__name__ = "Integer32"
_Pm404Mesrline2VoltIndex_Object = MibTableColumn
pm404Mesrline2VoltIndex = _Pm404Mesrline2VoltIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 3, 28, 1, 1),
    _Pm404Mesrline2VoltIndex_Type()
)
pm404Mesrline2VoltIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404Mesrline2VoltIndex.setStatus("current")


class _Pm404Mesrline2VoltPortn_Type(Integer32):
    """Custom type pm404Mesrline2VoltPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm404Mesrline2VoltPortn_Type.__name__ = "Integer32"
_Pm404Mesrline2VoltPortn_Object = MibTableColumn
pm404Mesrline2VoltPortn = _Pm404Mesrline2VoltPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 3, 28, 1, 2),
    _Pm404Mesrline2VoltPortn_Type()
)
pm404Mesrline2VoltPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404Mesrline2VoltPortn.setStatus("current")
_Pm404Mesrline2TxBiasTable_Object = MibTable
pm404Mesrline2TxBiasTable = _Pm404Mesrline2TxBiasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 3, 36)
)
if mibBuilder.loadTexts:
    pm404Mesrline2TxBiasTable.setStatus("current")
_Pm404Mesrline2TxBiasEntry_Object = MibTableRow
pm404Mesrline2TxBiasEntry = _Pm404Mesrline2TxBiasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 3, 36, 1)
)
pm404Mesrline2TxBiasEntry.setIndexNames(
    (0, "EKINOPS-Pm404-MIB", "pm404Mesrline2TxBiasIndex"),
)
if mibBuilder.loadTexts:
    pm404Mesrline2TxBiasEntry.setStatus("current")


class _Pm404Mesrline2TxBiasIndex_Type(Integer32):
    """Custom type pm404Mesrline2TxBiasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm404Mesrline2TxBiasIndex_Type.__name__ = "Integer32"
_Pm404Mesrline2TxBiasIndex_Object = MibTableColumn
pm404Mesrline2TxBiasIndex = _Pm404Mesrline2TxBiasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 3, 36, 1, 1),
    _Pm404Mesrline2TxBiasIndex_Type()
)
pm404Mesrline2TxBiasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404Mesrline2TxBiasIndex.setStatus("current")


class _Pm404Mesrline2TxBiasPortn_Type(Integer32):
    """Custom type pm404Mesrline2TxBiasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm404Mesrline2TxBiasPortn_Type.__name__ = "Integer32"
_Pm404Mesrline2TxBiasPortn_Object = MibTableColumn
pm404Mesrline2TxBiasPortn = _Pm404Mesrline2TxBiasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 3, 36, 1, 2),
    _Pm404Mesrline2TxBiasPortn_Type()
)
pm404Mesrline2TxBiasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404Mesrline2TxBiasPortn.setStatus("current")
_Pm404Mesrline2TxPowerTable_Object = MibTable
pm404Mesrline2TxPowerTable = _Pm404Mesrline2TxPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 3, 44)
)
if mibBuilder.loadTexts:
    pm404Mesrline2TxPowerTable.setStatus("current")
_Pm404Mesrline2TxPowerEntry_Object = MibTableRow
pm404Mesrline2TxPowerEntry = _Pm404Mesrline2TxPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 3, 44, 1)
)
pm404Mesrline2TxPowerEntry.setIndexNames(
    (0, "EKINOPS-Pm404-MIB", "pm404Mesrline2TxPowerIndex"),
)
if mibBuilder.loadTexts:
    pm404Mesrline2TxPowerEntry.setStatus("current")


class _Pm404Mesrline2TxPowerIndex_Type(Integer32):
    """Custom type pm404Mesrline2TxPowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm404Mesrline2TxPowerIndex_Type.__name__ = "Integer32"
_Pm404Mesrline2TxPowerIndex_Object = MibTableColumn
pm404Mesrline2TxPowerIndex = _Pm404Mesrline2TxPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 3, 44, 1, 1),
    _Pm404Mesrline2TxPowerIndex_Type()
)
pm404Mesrline2TxPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404Mesrline2TxPowerIndex.setStatus("current")


class _Pm404Mesrline2TxPowerPortn_Type(Integer32):
    """Custom type pm404Mesrline2TxPowerPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm404Mesrline2TxPowerPortn_Type.__name__ = "Integer32"
_Pm404Mesrline2TxPowerPortn_Object = MibTableColumn
pm404Mesrline2TxPowerPortn = _Pm404Mesrline2TxPowerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 3, 44, 1, 2),
    _Pm404Mesrline2TxPowerPortn_Type()
)
pm404Mesrline2TxPowerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404Mesrline2TxPowerPortn.setStatus("current")
_Pm404Mesrline2RxPowerTable_Object = MibTable
pm404Mesrline2RxPowerTable = _Pm404Mesrline2RxPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 3, 52)
)
if mibBuilder.loadTexts:
    pm404Mesrline2RxPowerTable.setStatus("current")
_Pm404Mesrline2RxPowerEntry_Object = MibTableRow
pm404Mesrline2RxPowerEntry = _Pm404Mesrline2RxPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 3, 52, 1)
)
pm404Mesrline2RxPowerEntry.setIndexNames(
    (0, "EKINOPS-Pm404-MIB", "pm404Mesrline2RxPowerIndex"),
)
if mibBuilder.loadTexts:
    pm404Mesrline2RxPowerEntry.setStatus("current")


class _Pm404Mesrline2RxPowerIndex_Type(Integer32):
    """Custom type pm404Mesrline2RxPowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm404Mesrline2RxPowerIndex_Type.__name__ = "Integer32"
_Pm404Mesrline2RxPowerIndex_Object = MibTableColumn
pm404Mesrline2RxPowerIndex = _Pm404Mesrline2RxPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 3, 52, 1, 1),
    _Pm404Mesrline2RxPowerIndex_Type()
)
pm404Mesrline2RxPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404Mesrline2RxPowerIndex.setStatus("current")


class _Pm404Mesrline2RxPowerPortn_Type(Integer32):
    """Custom type pm404Mesrline2RxPowerPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm404Mesrline2RxPowerPortn_Type.__name__ = "Integer32"
_Pm404Mesrline2RxPowerPortn_Object = MibTableColumn
pm404Mesrline2RxPowerPortn = _Pm404Mesrline2RxPowerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 3, 3, 52, 1, 2),
    _Pm404Mesrline2RxPowerPortn_Type()
)
pm404Mesrline2RxPowerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404Mesrline2RxPowerPortn.setStatus("current")
_Pm404counters_ObjectIdentity = ObjectIdentity
pm404counters = _Pm404counters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25, 4)
)
_Pm404CntOther_ObjectIdentity = ObjectIdentity
pm404CntOther = _Pm404CntOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25, 4, 1)
)
_Pm404CntClient_ObjectIdentity = ObjectIdentity
pm404CntClient = _Pm404CntClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25, 4, 2)
)
_Pm404CntLine_ObjectIdentity = ObjectIdentity
pm404CntLine = _Pm404CntLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25, 4, 3)
)
_Pm404controlsWrite_ObjectIdentity = ObjectIdentity
pm404controlsWrite = _Pm404controlsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6)
)
_Pm404CtrlOther_ObjectIdentity = ObjectIdentity
pm404CtrlOther = _Pm404CtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 1)
)
_Pm404Ctrlsynth0_ObjectIdentity = ObjectIdentity
pm404Ctrlsynth0 = _Pm404Ctrlsynth0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 1, 0)
)
_Pm404CtrlConfLoad_Type = EkiOnOff
_Pm404CtrlConfLoad_Object = MibScalar
pm404CtrlConfLoad = _Pm404CtrlConfLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 1, 0, 1),
    _Pm404CtrlConfLoad_Type()
)
pm404CtrlConfLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm404CtrlConfLoad.setStatus("current")
_Pm404CtrlConfFlash_Type = EkiOnOff
_Pm404CtrlConfFlash_Object = MibScalar
pm404CtrlConfFlash = _Pm404CtrlConfFlash_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 1, 0, 9),
    _Pm404CtrlConfFlash_Type()
)
pm404CtrlConfFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm404CtrlConfFlash.setStatus("current")
_Pm404CtrlConfClear_Type = EkiOnOff
_Pm404CtrlConfClear_Object = MibScalar
pm404CtrlConfClear = _Pm404CtrlConfClear_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 1, 0, 13),
    _Pm404CtrlConfClear_Type()
)
pm404CtrlConfClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm404CtrlConfClear.setStatus("current")
_Pm404Ctrlsynth4_ObjectIdentity = ObjectIdentity
pm404Ctrlsynth4 = _Pm404Ctrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 1, 4)
)
_Pm404CtrlCorrelatOn_Type = EkiOnOff
_Pm404CtrlCorrelatOn_Object = MibScalar
pm404CtrlCorrelatOn = _Pm404CtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 1, 4, 1),
    _Pm404CtrlCorrelatOn_Type()
)
pm404CtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm404CtrlCorrelatOn.setStatus("current")
_Pm404CtrlCorrelatOff_Type = EkiOnOff
_Pm404CtrlCorrelatOff_Object = MibScalar
pm404CtrlCorrelatOff = _Pm404CtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 1, 4, 2),
    _Pm404CtrlCorrelatOff_Type()
)
pm404CtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm404CtrlCorrelatOff.setStatus("current")
_Pm404CtrlswMgnt_ObjectIdentity = ObjectIdentity
pm404CtrlswMgnt = _Pm404CtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 1, 5)
)
_Pm404CtrlColdReset_Type = EkiOnOff
_Pm404CtrlColdReset_Object = MibScalar
pm404CtrlColdReset = _Pm404CtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 1, 5, 2),
    _Pm404CtrlColdReset_Type()
)
pm404CtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm404CtrlColdReset.setStatus("current")
_Pm404CtrlWarmReset_Type = EkiOnOff
_Pm404CtrlWarmReset_Object = MibScalar
pm404CtrlWarmReset = _Pm404CtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 1, 5, 3),
    _Pm404CtrlWarmReset_Type()
)
pm404CtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm404CtrlWarmReset.setStatus("current")
_Pm404CtrlledTest_ObjectIdentity = ObjectIdentity
pm404CtrlledTest = _Pm404CtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 1, 72)
)
_Pm404CtrlGreenLed_Type = EkiOnOff
_Pm404CtrlGreenLed_Object = MibScalar
pm404CtrlGreenLed = _Pm404CtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 1, 72, 1),
    _Pm404CtrlGreenLed_Type()
)
pm404CtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm404CtrlGreenLed.setStatus("current")
_Pm404CtrlRedLed_Type = EkiOnOff
_Pm404CtrlRedLed_Object = MibScalar
pm404CtrlRedLed = _Pm404CtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 1, 72, 2),
    _Pm404CtrlRedLed_Type()
)
pm404CtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm404CtrlRedLed.setStatus("current")
_Pm404CtrlLedOff_Type = EkiOnOff
_Pm404CtrlLedOff_Object = MibScalar
pm404CtrlLedOff = _Pm404CtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 1, 72, 3),
    _Pm404CtrlLedOff_Type()
)
pm404CtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm404CtrlLedOff.setStatus("current")
_Pm404CtrlmoduleOosMode_ObjectIdentity = ObjectIdentity
pm404CtrlmoduleOosMode = _Pm404CtrlmoduleOosMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 1, 73)
)
_Pm404CtrlModuleOosMode_Type = EkiOnOff
_Pm404CtrlModuleOosMode_Object = MibScalar
pm404CtrlModuleOosMode = _Pm404CtrlModuleOosMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 1, 73, 1),
    _Pm404CtrlModuleOosMode_Type()
)
pm404CtrlModuleOosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm404CtrlModuleOosMode.setStatus("current")
_Pm404CtrlClient_ObjectIdentity = ObjectIdentity
pm404CtrlClient = _Pm404CtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 2)
)
_Pm404Ctrlline1SfpOnoffTable_Object = MibTable
pm404Ctrlline1SfpOnoffTable = _Pm404Ctrlline1SfpOnoffTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 2, 16)
)
if mibBuilder.loadTexts:
    pm404Ctrlline1SfpOnoffTable.setStatus("current")
_Pm404Ctrlline1SfpOnoffEntry_Object = MibTableRow
pm404Ctrlline1SfpOnoffEntry = _Pm404Ctrlline1SfpOnoffEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 2, 16, 1)
)
pm404Ctrlline1SfpOnoffEntry.setIndexNames(
    (0, "EKINOPS-Pm404-MIB", "pm404Ctrlline1SfpOnoffIndex"),
)
if mibBuilder.loadTexts:
    pm404Ctrlline1SfpOnoffEntry.setStatus("current")


class _Pm404Ctrlline1SfpOnoffIndex_Type(Integer32):
    """Custom type pm404Ctrlline1SfpOnoffIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm404Ctrlline1SfpOnoffIndex_Type.__name__ = "Integer32"
_Pm404Ctrlline1SfpOnoffIndex_Object = MibTableColumn
pm404Ctrlline1SfpOnoffIndex = _Pm404Ctrlline1SfpOnoffIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 2, 16, 1, 1),
    _Pm404Ctrlline1SfpOnoffIndex_Type()
)
pm404Ctrlline1SfpOnoffIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404Ctrlline1SfpOnoffIndex.setStatus("current")
_Pm404Ctrlline1SfpOnoffPortn_Type = EkiState
_Pm404Ctrlline1SfpOnoffPortn_Object = MibTableColumn
pm404Ctrlline1SfpOnoffPortn = _Pm404Ctrlline1SfpOnoffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 2, 16, 1, 2),
    _Pm404Ctrlline1SfpOnoffPortn_Type()
)
pm404Ctrlline1SfpOnoffPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm404Ctrlline1SfpOnoffPortn.setStatus("current")
_Pm404Ctrlline1LoopbackTable_Object = MibTable
pm404Ctrlline1LoopbackTable = _Pm404Ctrlline1LoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 2, 17)
)
if mibBuilder.loadTexts:
    pm404Ctrlline1LoopbackTable.setStatus("current")
_Pm404Ctrlline1LoopbackEntry_Object = MibTableRow
pm404Ctrlline1LoopbackEntry = _Pm404Ctrlline1LoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 2, 17, 1)
)
pm404Ctrlline1LoopbackEntry.setIndexNames(
    (0, "EKINOPS-Pm404-MIB", "pm404Ctrlline1LoopbackIndex"),
)
if mibBuilder.loadTexts:
    pm404Ctrlline1LoopbackEntry.setStatus("current")


class _Pm404Ctrlline1LoopbackIndex_Type(Integer32):
    """Custom type pm404Ctrlline1LoopbackIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm404Ctrlline1LoopbackIndex_Type.__name__ = "Integer32"
_Pm404Ctrlline1LoopbackIndex_Object = MibTableColumn
pm404Ctrlline1LoopbackIndex = _Pm404Ctrlline1LoopbackIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 2, 17, 1, 1),
    _Pm404Ctrlline1LoopbackIndex_Type()
)
pm404Ctrlline1LoopbackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404Ctrlline1LoopbackIndex.setStatus("current")
_Pm404Ctrlline1LoopbackPortn_Type = EkiState
_Pm404Ctrlline1LoopbackPortn_Object = MibTableColumn
pm404Ctrlline1LoopbackPortn = _Pm404Ctrlline1LoopbackPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 2, 17, 1, 2),
    _Pm404Ctrlline1LoopbackPortn_Type()
)
pm404Ctrlline1LoopbackPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm404Ctrlline1LoopbackPortn.setStatus("current")
_Pm404Ctrlline1LoopbackTermTable_Object = MibTable
pm404Ctrlline1LoopbackTermTable = _Pm404Ctrlline1LoopbackTermTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 2, 18)
)
if mibBuilder.loadTexts:
    pm404Ctrlline1LoopbackTermTable.setStatus("current")
_Pm404Ctrlline1LoopbackTermEntry_Object = MibTableRow
pm404Ctrlline1LoopbackTermEntry = _Pm404Ctrlline1LoopbackTermEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 2, 18, 1)
)
pm404Ctrlline1LoopbackTermEntry.setIndexNames(
    (0, "EKINOPS-Pm404-MIB", "pm404Ctrlline1LoopbackTermIndex"),
)
if mibBuilder.loadTexts:
    pm404Ctrlline1LoopbackTermEntry.setStatus("current")


class _Pm404Ctrlline1LoopbackTermIndex_Type(Integer32):
    """Custom type pm404Ctrlline1LoopbackTermIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm404Ctrlline1LoopbackTermIndex_Type.__name__ = "Integer32"
_Pm404Ctrlline1LoopbackTermIndex_Object = MibTableColumn
pm404Ctrlline1LoopbackTermIndex = _Pm404Ctrlline1LoopbackTermIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 2, 18, 1, 1),
    _Pm404Ctrlline1LoopbackTermIndex_Type()
)
pm404Ctrlline1LoopbackTermIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404Ctrlline1LoopbackTermIndex.setStatus("current")
_Pm404Ctrlline1LoopbackTermPortn_Type = EkiState
_Pm404Ctrlline1LoopbackTermPortn_Object = MibTableColumn
pm404Ctrlline1LoopbackTermPortn = _Pm404Ctrlline1LoopbackTermPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 2, 18, 1, 2),
    _Pm404Ctrlline1LoopbackTermPortn_Type()
)
pm404Ctrlline1LoopbackTermPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm404Ctrlline1LoopbackTermPortn.setStatus("current")
_Pm404Ctrlline1OosModeTable_Object = MibTable
pm404Ctrlline1OosModeTable = _Pm404Ctrlline1OosModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 2, 20)
)
if mibBuilder.loadTexts:
    pm404Ctrlline1OosModeTable.setStatus("current")
_Pm404Ctrlline1OosModeEntry_Object = MibTableRow
pm404Ctrlline1OosModeEntry = _Pm404Ctrlline1OosModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 2, 20, 1)
)
pm404Ctrlline1OosModeEntry.setIndexNames(
    (0, "EKINOPS-Pm404-MIB", "pm404Ctrlline1OosModeIndex"),
)
if mibBuilder.loadTexts:
    pm404Ctrlline1OosModeEntry.setStatus("current")


class _Pm404Ctrlline1OosModeIndex_Type(Integer32):
    """Custom type pm404Ctrlline1OosModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm404Ctrlline1OosModeIndex_Type.__name__ = "Integer32"
_Pm404Ctrlline1OosModeIndex_Object = MibTableColumn
pm404Ctrlline1OosModeIndex = _Pm404Ctrlline1OosModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 2, 20, 1, 1),
    _Pm404Ctrlline1OosModeIndex_Type()
)
pm404Ctrlline1OosModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404Ctrlline1OosModeIndex.setStatus("current")
_Pm404Ctrlline1OosModePortn_Type = EkiState
_Pm404Ctrlline1OosModePortn_Object = MibTableColumn
pm404Ctrlline1OosModePortn = _Pm404Ctrlline1OosModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 2, 20, 1, 2),
    _Pm404Ctrlline1OosModePortn_Type()
)
pm404Ctrlline1OosModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm404Ctrlline1OosModePortn.setStatus("current")
_Pm404CtrlprotocolTable_Object = MibTable
pm404CtrlprotocolTable = _Pm404CtrlprotocolTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 2, 48)
)
if mibBuilder.loadTexts:
    pm404CtrlprotocolTable.setStatus("current")
_Pm404CtrlprotocolEntry_Object = MibTableRow
pm404CtrlprotocolEntry = _Pm404CtrlprotocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 2, 48, 1)
)
pm404CtrlprotocolEntry.setIndexNames(
    (0, "EKINOPS-Pm404-MIB", "pm404CtrlprotocolIndex"),
)
if mibBuilder.loadTexts:
    pm404CtrlprotocolEntry.setStatus("current")


class _Pm404CtrlprotocolIndex_Type(Integer32):
    """Custom type pm404CtrlprotocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm404CtrlprotocolIndex_Type.__name__ = "Integer32"
_Pm404CtrlprotocolIndex_Object = MibTableColumn
pm404CtrlprotocolIndex = _Pm404CtrlprotocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 2, 48, 1, 1),
    _Pm404CtrlprotocolIndex_Type()
)
pm404CtrlprotocolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404CtrlprotocolIndex.setStatus("current")
_Pm404CtrlprotocolPortn_Type = EkiProtocol
_Pm404CtrlprotocolPortn_Object = MibTableColumn
pm404CtrlprotocolPortn = _Pm404CtrlprotocolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 2, 48, 1, 2),
    _Pm404CtrlprotocolPortn_Type()
)
pm404CtrlprotocolPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm404CtrlprotocolPortn.setStatus("current")
_Pm404CtrlLine_ObjectIdentity = ObjectIdentity
pm404CtrlLine = _Pm404CtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 3)
)
_Pm404Ctrlline2SfpOnoffTable_Object = MibTable
pm404Ctrlline2SfpOnoffTable = _Pm404Ctrlline2SfpOnoffTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 3, 64)
)
if mibBuilder.loadTexts:
    pm404Ctrlline2SfpOnoffTable.setStatus("current")
_Pm404Ctrlline2SfpOnoffEntry_Object = MibTableRow
pm404Ctrlline2SfpOnoffEntry = _Pm404Ctrlline2SfpOnoffEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 3, 64, 1)
)
pm404Ctrlline2SfpOnoffEntry.setIndexNames(
    (0, "EKINOPS-Pm404-MIB", "pm404Ctrlline2SfpOnoffIndex"),
)
if mibBuilder.loadTexts:
    pm404Ctrlline2SfpOnoffEntry.setStatus("current")


class _Pm404Ctrlline2SfpOnoffIndex_Type(Integer32):
    """Custom type pm404Ctrlline2SfpOnoffIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm404Ctrlline2SfpOnoffIndex_Type.__name__ = "Integer32"
_Pm404Ctrlline2SfpOnoffIndex_Object = MibTableColumn
pm404Ctrlline2SfpOnoffIndex = _Pm404Ctrlline2SfpOnoffIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 3, 64, 1, 1),
    _Pm404Ctrlline2SfpOnoffIndex_Type()
)
pm404Ctrlline2SfpOnoffIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404Ctrlline2SfpOnoffIndex.setStatus("current")
_Pm404Ctrlline2SfpOnoffPortn_Type = EkiState
_Pm404Ctrlline2SfpOnoffPortn_Object = MibTableColumn
pm404Ctrlline2SfpOnoffPortn = _Pm404Ctrlline2SfpOnoffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 3, 64, 1, 2),
    _Pm404Ctrlline2SfpOnoffPortn_Type()
)
pm404Ctrlline2SfpOnoffPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm404Ctrlline2SfpOnoffPortn.setStatus("current")
_Pm404Ctrlline2OosModeTable_Object = MibTable
pm404Ctrlline2OosModeTable = _Pm404Ctrlline2OosModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 3, 65)
)
if mibBuilder.loadTexts:
    pm404Ctrlline2OosModeTable.setStatus("current")
_Pm404Ctrlline2OosModeEntry_Object = MibTableRow
pm404Ctrlline2OosModeEntry = _Pm404Ctrlline2OosModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 3, 65, 1)
)
pm404Ctrlline2OosModeEntry.setIndexNames(
    (0, "EKINOPS-Pm404-MIB", "pm404Ctrlline2OosModeIndex"),
)
if mibBuilder.loadTexts:
    pm404Ctrlline2OosModeEntry.setStatus("current")


class _Pm404Ctrlline2OosModeIndex_Type(Integer32):
    """Custom type pm404Ctrlline2OosModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm404Ctrlline2OosModeIndex_Type.__name__ = "Integer32"
_Pm404Ctrlline2OosModeIndex_Object = MibTableColumn
pm404Ctrlline2OosModeIndex = _Pm404Ctrlline2OosModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 3, 65, 1, 1),
    _Pm404Ctrlline2OosModeIndex_Type()
)
pm404Ctrlline2OosModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404Ctrlline2OosModeIndex.setStatus("current")
_Pm404Ctrlline2OosModePortn_Type = EkiState
_Pm404Ctrlline2OosModePortn_Object = MibTableColumn
pm404Ctrlline2OosModePortn = _Pm404Ctrlline2OosModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 3, 65, 1, 2),
    _Pm404Ctrlline2OosModePortn_Type()
)
pm404Ctrlline2OosModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm404Ctrlline2OosModePortn.setStatus("current")
_Pm404Ctrlline2LoopbackTable_Object = MibTable
pm404Ctrlline2LoopbackTable = _Pm404Ctrlline2LoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 3, 66)
)
if mibBuilder.loadTexts:
    pm404Ctrlline2LoopbackTable.setStatus("current")
_Pm404Ctrlline2LoopbackEntry_Object = MibTableRow
pm404Ctrlline2LoopbackEntry = _Pm404Ctrlline2LoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 3, 66, 1)
)
pm404Ctrlline2LoopbackEntry.setIndexNames(
    (0, "EKINOPS-Pm404-MIB", "pm404Ctrlline2LoopbackIndex"),
)
if mibBuilder.loadTexts:
    pm404Ctrlline2LoopbackEntry.setStatus("current")


class _Pm404Ctrlline2LoopbackIndex_Type(Integer32):
    """Custom type pm404Ctrlline2LoopbackIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm404Ctrlline2LoopbackIndex_Type.__name__ = "Integer32"
_Pm404Ctrlline2LoopbackIndex_Object = MibTableColumn
pm404Ctrlline2LoopbackIndex = _Pm404Ctrlline2LoopbackIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 3, 66, 1, 1),
    _Pm404Ctrlline2LoopbackIndex_Type()
)
pm404Ctrlline2LoopbackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404Ctrlline2LoopbackIndex.setStatus("current")
_Pm404Ctrlline2LoopbackPortn_Type = EkiState
_Pm404Ctrlline2LoopbackPortn_Object = MibTableColumn
pm404Ctrlline2LoopbackPortn = _Pm404Ctrlline2LoopbackPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 3, 66, 1, 2),
    _Pm404Ctrlline2LoopbackPortn_Type()
)
pm404Ctrlline2LoopbackPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm404Ctrlline2LoopbackPortn.setStatus("current")
_Pm404Ctrlline2LoopbackTermTable_Object = MibTable
pm404Ctrlline2LoopbackTermTable = _Pm404Ctrlline2LoopbackTermTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 3, 67)
)
if mibBuilder.loadTexts:
    pm404Ctrlline2LoopbackTermTable.setStatus("current")
_Pm404Ctrlline2LoopbackTermEntry_Object = MibTableRow
pm404Ctrlline2LoopbackTermEntry = _Pm404Ctrlline2LoopbackTermEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 3, 67, 1)
)
pm404Ctrlline2LoopbackTermEntry.setIndexNames(
    (0, "EKINOPS-Pm404-MIB", "pm404Ctrlline2LoopbackTermIndex"),
)
if mibBuilder.loadTexts:
    pm404Ctrlline2LoopbackTermEntry.setStatus("current")


class _Pm404Ctrlline2LoopbackTermIndex_Type(Integer32):
    """Custom type pm404Ctrlline2LoopbackTermIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm404Ctrlline2LoopbackTermIndex_Type.__name__ = "Integer32"
_Pm404Ctrlline2LoopbackTermIndex_Object = MibTableColumn
pm404Ctrlline2LoopbackTermIndex = _Pm404Ctrlline2LoopbackTermIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 3, 67, 1, 1),
    _Pm404Ctrlline2LoopbackTermIndex_Type()
)
pm404Ctrlline2LoopbackTermIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404Ctrlline2LoopbackTermIndex.setStatus("current")
_Pm404Ctrlline2LoopbackTermPortn_Type = EkiState
_Pm404Ctrlline2LoopbackTermPortn_Object = MibTableColumn
pm404Ctrlline2LoopbackTermPortn = _Pm404Ctrlline2LoopbackTermPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 6, 3, 67, 1, 2),
    _Pm404Ctrlline2LoopbackTermPortn_Type()
)
pm404Ctrlline2LoopbackTermPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm404Ctrlline2LoopbackTermPortn.setStatus("current")
_Pm404ri_ObjectIdentity = ObjectIdentity
pm404ri = _Pm404ri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25, 7)
)
_Pm404riTable_ObjectIdentity = ObjectIdentity
pm404riTable = _Pm404riTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25, 7, 1)
)
_Pm404RinvLine1Table_Object = MibTable
pm404RinvLine1Table = _Pm404RinvLine1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 7, 1, 1)
)
if mibBuilder.loadTexts:
    pm404RinvLine1Table.setStatus("current")
_Pm404RinvLine1Entry_Object = MibTableRow
pm404RinvLine1Entry = _Pm404RinvLine1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 7, 1, 1, 1)
)
pm404RinvLine1Entry.setIndexNames(
    (0, "EKINOPS-Pm404-MIB", "pm404RinvLine1Index"),
)
if mibBuilder.loadTexts:
    pm404RinvLine1Entry.setStatus("current")


class _Pm404RinvLine1Index_Type(Integer32):
    """Custom type pm404RinvLine1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm404RinvLine1Index_Type.__name__ = "Integer32"
_Pm404RinvLine1Index_Object = MibTableColumn
pm404RinvLine1Index = _Pm404RinvLine1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 7, 1, 1, 1, 1),
    _Pm404RinvLine1Index_Type()
)
pm404RinvLine1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404RinvLine1Index.setStatus("current")
_Pm404RinvSfpLine1_Type = DisplayString
_Pm404RinvSfpLine1_Object = MibTableColumn
pm404RinvSfpLine1 = _Pm404RinvSfpLine1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 7, 1, 1, 1, 2),
    _Pm404RinvSfpLine1_Type()
)
pm404RinvSfpLine1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404RinvSfpLine1.setStatus("current")
_Pm404RinvLine2Table_Object = MibTable
pm404RinvLine2Table = _Pm404RinvLine2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pm404RinvLine2Table.setStatus("current")
_Pm404RinvLine2Entry_Object = MibTableRow
pm404RinvLine2Entry = _Pm404RinvLine2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 7, 1, 2, 1)
)
pm404RinvLine2Entry.setIndexNames(
    (0, "EKINOPS-Pm404-MIB", "pm404RinvLine2Index"),
)
if mibBuilder.loadTexts:
    pm404RinvLine2Entry.setStatus("current")


class _Pm404RinvLine2Index_Type(Integer32):
    """Custom type pm404RinvLine2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm404RinvLine2Index_Type.__name__ = "Integer32"
_Pm404RinvLine2Index_Object = MibTableColumn
pm404RinvLine2Index = _Pm404RinvLine2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 7, 1, 2, 1, 1),
    _Pm404RinvLine2Index_Type()
)
pm404RinvLine2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404RinvLine2Index.setStatus("current")
_Pm404RinvsfpLine2_Type = DisplayString
_Pm404RinvsfpLine2_Object = MibTableColumn
pm404RinvsfpLine2 = _Pm404RinvsfpLine2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 7, 1, 2, 1, 2),
    _Pm404RinvsfpLine2_Type()
)
pm404RinvsfpLine2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404RinvsfpLine2.setStatus("current")
_Pm404RinvReloadInventory_Type = EkiOnOff
_Pm404RinvReloadInventory_Object = MibScalar
pm404RinvReloadInventory = _Pm404RinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 7, 2),
    _Pm404RinvReloadInventory_Type()
)
pm404RinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm404RinvReloadInventory.setStatus("current")
_Pm404RinvHwPlatform_Type = DisplayString
_Pm404RinvHwPlatform_Object = MibScalar
pm404RinvHwPlatform = _Pm404RinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 7, 3),
    _Pm404RinvHwPlatform_Type()
)
pm404RinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404RinvHwPlatform.setStatus("current")
_Pm404RinvModulePlatform_Type = DisplayString
_Pm404RinvModulePlatform_Object = MibScalar
pm404RinvModulePlatform = _Pm404RinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 7, 4),
    _Pm404RinvModulePlatform_Type()
)
pm404RinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404RinvModulePlatform.setStatus("current")
_Pm404RinvSwPlatform_Type = DisplayString
_Pm404RinvSwPlatform_Object = MibScalar
pm404RinvSwPlatform = _Pm404RinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 7, 5),
    _Pm404RinvSwPlatform_Type()
)
pm404RinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404RinvSwPlatform.setStatus("current")
_Pm404RinvGwPlatform_Type = DisplayString
_Pm404RinvGwPlatform_Object = MibScalar
pm404RinvGwPlatform = _Pm404RinvGwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 7, 6),
    _Pm404RinvGwPlatform_Type()
)
pm404RinvGwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404RinvGwPlatform.setStatus("current")
_Pm404Config_ObjectIdentity = ObjectIdentity
pm404Config = _Pm404Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25, 9)
)
_Pm404CfgLsd_ObjectIdentity = ObjectIdentity
pm404CfgLsd = _Pm404CfgLsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25, 9, 1)
)
_Pm404CfgLine1LsdTable_Object = MibTable
pm404CfgLine1LsdTable = _Pm404CfgLine1LsdTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 9, 1, 1)
)
if mibBuilder.loadTexts:
    pm404CfgLine1LsdTable.setStatus("current")
_Pm404CfgLine1LsdEntry_Object = MibTableRow
pm404CfgLine1LsdEntry = _Pm404CfgLine1LsdEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 9, 1, 1, 1)
)
pm404CfgLine1LsdEntry.setIndexNames(
    (0, "EKINOPS-Pm404-MIB", "pm404CfgLine1LsdIndex"),
)
if mibBuilder.loadTexts:
    pm404CfgLine1LsdEntry.setStatus("current")


class _Pm404CfgLine1LsdIndex_Type(Integer32):
    """Custom type pm404CfgLine1LsdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm404CfgLine1LsdIndex_Type.__name__ = "Integer32"
_Pm404CfgLine1LsdIndex_Object = MibTableColumn
pm404CfgLine1LsdIndex = _Pm404CfgLine1LsdIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 9, 1, 1, 1, 1),
    _Pm404CfgLine1LsdIndex_Type()
)
pm404CfgLine1LsdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404CfgLine1LsdIndex.setStatus("current")


class _Pm404CfgLine1LsdModePortn_Type(Unsigned32):
    """Custom type pm404CfgLine1LsdModePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm404CfgLine1LsdModePortn_Type.__name__ = "Unsigned32"
_Pm404CfgLine1LsdModePortn_Object = MibTableColumn
pm404CfgLine1LsdModePortn = _Pm404CfgLine1LsdModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 9, 1, 1, 1, 3),
    _Pm404CfgLine1LsdModePortn_Type()
)
pm404CfgLine1LsdModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm404CfgLine1LsdModePortn.setStatus("current")


class _Pm404CfgLine1AccessioCtrbInsPortn_Type(Unsigned32):
    """Custom type pm404CfgLine1AccessioCtrbInsPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm404CfgLine1AccessioCtrbInsPortn_Type.__name__ = "Unsigned32"
_Pm404CfgLine1AccessioCtrbInsPortn_Object = MibTableColumn
pm404CfgLine1AccessioCtrbInsPortn = _Pm404CfgLine1AccessioCtrbInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 9, 1, 1, 1, 4),
    _Pm404CfgLine1AccessioCtrbInsPortn_Type()
)
pm404CfgLine1AccessioCtrbInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm404CfgLine1AccessioCtrbInsPortn.setStatus("current")


class _Pm404CfgLine2AccessioCtrbInsPortn_Type(Unsigned32):
    """Custom type pm404CfgLine2AccessioCtrbInsPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm404CfgLine2AccessioCtrbInsPortn_Type.__name__ = "Unsigned32"
_Pm404CfgLine2AccessioCtrbInsPortn_Object = MibTableColumn
pm404CfgLine2AccessioCtrbInsPortn = _Pm404CfgLine2AccessioCtrbInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 9, 1, 1, 1, 7),
    _Pm404CfgLine2AccessioCtrbInsPortn_Type()
)
pm404CfgLine2AccessioCtrbInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm404CfgLine2AccessioCtrbInsPortn.setStatus("current")
_Pm404CfgStartUp_ObjectIdentity = ObjectIdentity
pm404CfgStartUp = _Pm404CfgStartUp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25, 9, 2)
)
_Pm404CfgLine1StartupTable_Object = MibTable
pm404CfgLine1StartupTable = _Pm404CfgLine1StartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 9, 2, 1)
)
if mibBuilder.loadTexts:
    pm404CfgLine1StartupTable.setStatus("current")
_Pm404CfgLine1StartupEntry_Object = MibTableRow
pm404CfgLine1StartupEntry = _Pm404CfgLine1StartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 9, 2, 1, 1)
)
pm404CfgLine1StartupEntry.setIndexNames(
    (0, "EKINOPS-Pm404-MIB", "pm404CfgLine1StartupIndex"),
)
if mibBuilder.loadTexts:
    pm404CfgLine1StartupEntry.setStatus("current")


class _Pm404CfgLine1StartupIndex_Type(Integer32):
    """Custom type pm404CfgLine1StartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm404CfgLine1StartupIndex_Type.__name__ = "Integer32"
_Pm404CfgLine1StartupIndex_Object = MibTableColumn
pm404CfgLine1StartupIndex = _Pm404CfgLine1StartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 9, 2, 1, 1, 1),
    _Pm404CfgLine1StartupIndex_Type()
)
pm404CfgLine1StartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404CfgLine1StartupIndex.setStatus("current")


class _Pm404CfgLine1TrscvCtrlPortn_Type(Unsigned32):
    """Custom type pm404CfgLine1TrscvCtrlPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm404CfgLine1TrscvCtrlPortn_Type.__name__ = "Unsigned32"
_Pm404CfgLine1TrscvCtrlPortn_Object = MibTableColumn
pm404CfgLine1TrscvCtrlPortn = _Pm404CfgLine1TrscvCtrlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 9, 2, 1, 1, 3),
    _Pm404CfgLine1TrscvCtrlPortn_Type()
)
pm404CfgLine1TrscvCtrlPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm404CfgLine1TrscvCtrlPortn.setStatus("current")


class _Pm404CfgLine1ProtocolPortn_Type(Unsigned32):
    """Custom type pm404CfgLine1ProtocolPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm404CfgLine1ProtocolPortn_Type.__name__ = "Unsigned32"
_Pm404CfgLine1ProtocolPortn_Object = MibTableColumn
pm404CfgLine1ProtocolPortn = _Pm404CfgLine1ProtocolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 9, 2, 1, 1, 4),
    _Pm404CfgLine1ProtocolPortn_Type()
)
pm404CfgLine1ProtocolPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm404CfgLine1ProtocolPortn.setStatus("current")


class _Pm404CfgLine1OosModePortn_Type(Unsigned32):
    """Custom type pm404CfgLine1OosModePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm404CfgLine1OosModePortn_Type.__name__ = "Unsigned32"
_Pm404CfgLine1OosModePortn_Object = MibTableColumn
pm404CfgLine1OosModePortn = _Pm404CfgLine1OosModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 9, 2, 1, 1, 5),
    _Pm404CfgLine1OosModePortn_Type()
)
pm404CfgLine1OosModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm404CfgLine1OosModePortn.setStatus("current")
_Pm404CfgLine2StartupTable_Object = MibTable
pm404CfgLine2StartupTable = _Pm404CfgLine2StartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 9, 2, 2)
)
if mibBuilder.loadTexts:
    pm404CfgLine2StartupTable.setStatus("current")
_Pm404CfgLine2StartupEntry_Object = MibTableRow
pm404CfgLine2StartupEntry = _Pm404CfgLine2StartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 9, 2, 2, 1)
)
pm404CfgLine2StartupEntry.setIndexNames(
    (0, "EKINOPS-Pm404-MIB", "pm404CfgLine2StartupIndex"),
)
if mibBuilder.loadTexts:
    pm404CfgLine2StartupEntry.setStatus("current")


class _Pm404CfgLine2StartupIndex_Type(Integer32):
    """Custom type pm404CfgLine2StartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm404CfgLine2StartupIndex_Type.__name__ = "Integer32"
_Pm404CfgLine2StartupIndex_Object = MibTableColumn
pm404CfgLine2StartupIndex = _Pm404CfgLine2StartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 9, 2, 2, 1, 1),
    _Pm404CfgLine2StartupIndex_Type()
)
pm404CfgLine2StartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404CfgLine2StartupIndex.setStatus("current")


class _Pm404CfgLine2TrscvCtrlPortn_Type(Unsigned32):
    """Custom type pm404CfgLine2TrscvCtrlPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm404CfgLine2TrscvCtrlPortn_Type.__name__ = "Unsigned32"
_Pm404CfgLine2TrscvCtrlPortn_Object = MibTableColumn
pm404CfgLine2TrscvCtrlPortn = _Pm404CfgLine2TrscvCtrlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 9, 2, 2, 1, 3),
    _Pm404CfgLine2TrscvCtrlPortn_Type()
)
pm404CfgLine2TrscvCtrlPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm404CfgLine2TrscvCtrlPortn.setStatus("current")


class _Pm404CfgLine2OosModePortn_Type(Unsigned32):
    """Custom type pm404CfgLine2OosModePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm404CfgLine2OosModePortn_Type.__name__ = "Unsigned32"
_Pm404CfgLine2OosModePortn_Object = MibTableColumn
pm404CfgLine2OosModePortn = _Pm404CfgLine2OosModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 9, 2, 2, 1, 4),
    _Pm404CfgLine2OosModePortn_Type()
)
pm404CfgLine2OosModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm404CfgLine2OosModePortn.setStatus("current")
_Pm404CfgLabels_ObjectIdentity = ObjectIdentity
pm404CfgLabels = _Pm404CfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25, 9, 3)
)
_Pm404CfgLabelclientTable_Object = MibTable
pm404CfgLabelclientTable = _Pm404CfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 9, 3, 1)
)
if mibBuilder.loadTexts:
    pm404CfgLabelclientTable.setStatus("current")
_Pm404CfgLabelclientEntry_Object = MibTableRow
pm404CfgLabelclientEntry = _Pm404CfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 9, 3, 1, 1)
)
pm404CfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-Pm404-MIB", "pm404CfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pm404CfgLabelclientEntry.setStatus("current")


class _Pm404CfgLabelclientIndex_Type(Integer32):
    """Custom type pm404CfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm404CfgLabelclientIndex_Type.__name__ = "Integer32"
_Pm404CfgLabelclientIndex_Object = MibTableColumn
pm404CfgLabelclientIndex = _Pm404CfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 9, 3, 1, 1, 1),
    _Pm404CfgLabelclientIndex_Type()
)
pm404CfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404CfgLabelclientIndex.setStatus("current")


class _Pm404CfgLabelclientPortn_Type(DisplayString):
    """Custom type pm404CfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm404CfgLabelclientPortn_Type.__name__ = "DisplayString"
_Pm404CfgLabelclientPortn_Object = MibTableColumn
pm404CfgLabelclientPortn = _Pm404CfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 9, 3, 1, 1, 3),
    _Pm404CfgLabelclientPortn_Type()
)
pm404CfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm404CfgLabelclientPortn.setStatus("current")
_Pm404CfgLabellineTable_Object = MibTable
pm404CfgLabellineTable = _Pm404CfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 9, 3, 2)
)
if mibBuilder.loadTexts:
    pm404CfgLabellineTable.setStatus("current")
_Pm404CfgLabellineEntry_Object = MibTableRow
pm404CfgLabellineEntry = _Pm404CfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 9, 3, 2, 1)
)
pm404CfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-Pm404-MIB", "pm404CfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pm404CfgLabellineEntry.setStatus("current")


class _Pm404CfgLabellineIndex_Type(Integer32):
    """Custom type pm404CfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm404CfgLabellineIndex_Type.__name__ = "Integer32"
_Pm404CfgLabellineIndex_Object = MibTableColumn
pm404CfgLabellineIndex = _Pm404CfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 9, 3, 2, 1, 1),
    _Pm404CfgLabellineIndex_Type()
)
pm404CfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404CfgLabellineIndex.setStatus("current")


class _Pm404CfgLabellinePortn_Type(DisplayString):
    """Custom type pm404CfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm404CfgLabellinePortn_Type.__name__ = "DisplayString"
_Pm404CfgLabellinePortn_Object = MibTableColumn
pm404CfgLabellinePortn = _Pm404CfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 9, 3, 2, 1, 3),
    _Pm404CfgLabellinePortn_Type()
)
pm404CfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm404CfgLabellinePortn.setStatus("current")
_Pm404CfgWriteConfiguration_Type = EkiOnOff
_Pm404CfgWriteConfiguration_Object = MibScalar
pm404CfgWriteConfiguration = _Pm404CfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 9, 257),
    _Pm404CfgWriteConfiguration_Type()
)
pm404CfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm404CfgWriteConfiguration.setStatus("current")
_Pm404traps_ObjectIdentity = ObjectIdentity
pm404traps = _Pm404traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 25, 10)
)


class _Pm404trapPortNumber_Type(Integer32):
    """Custom type pm404trapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm404trapPortNumber_Type.__name__ = "Integer32"
_Pm404trapPortNumber_Object = MibScalar
pm404trapPortNumber = _Pm404trapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 10, 2),
    _Pm404trapPortNumber_Type()
)
pm404trapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404trapPortNumber.setStatus("current")


class _Pm404trapLineNumber_Type(Integer32):
    """Custom type pm404trapLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm404trapLineNumber_Type.__name__ = "Integer32"
_Pm404trapLineNumber_Object = MibScalar
pm404trapLineNumber = _Pm404trapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 10, 3),
    _Pm404trapLineNumber_Type()
)
pm404trapLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404trapLineNumber.setStatus("current")


class _Pm404trapBoardNumber_Type(Integer32):
    """Custom type pm404trapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm404trapBoardNumber_Type.__name__ = "Integer32"
_Pm404trapBoardNumber_Object = MibScalar
pm404trapBoardNumber = _Pm404trapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 25, 10, 4),
    _Pm404trapBoardNumber_Type()
)
pm404trapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm404trapBoardNumber.setStatus("current")

# Managed Objects groups


# Notification objects

pm404Line2TrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 25, 10, 30)
)
pm404Line2TrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm404-MIB", "pm404AlmLine2DdmWarningPortn"),
        ("EKINOPS-Pm404-MIB", "pm404trapLineNumber"),
        ("EKINOPS-Pm404-MIB", "pm404trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm404Line2TrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm404Line2TrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 25, 10, 31)
)
pm404Line2TrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm404-MIB", "pm404AlmLine2DdmWarningPortn"),
        ("EKINOPS-Pm404-MIB", "pm404trapLineNumber"),
        ("EKINOPS-Pm404-MIB", "pm404trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm404Line2TrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm404Line2TrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 25, 10, 32)
)
pm404Line2TrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm404-MIB", "pm404AlmLine2DdmAlmPortn"),
        ("EKINOPS-Pm404-MIB", "pm404trapLineNumber"),
        ("EKINOPS-Pm404-MIB", "pm404trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm404Line2TrapUrgentGoesOn.setStatus(
        "current"
    )

pm404Line2TrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 25, 10, 33)
)
pm404Line2TrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm404-MIB", "pm404AlmLine2DdmAlmPortn"),
        ("EKINOPS-Pm404-MIB", "pm404trapLineNumber"),
        ("EKINOPS-Pm404-MIB", "pm404trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm404Line2TrapUrgentGoesOff.setStatus(
        "current"
    )

pm404Line2TrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 25, 10, 34)
)
pm404Line2TrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm404-MIB", "pm404AlmLine2FailPortn"),
        ("EKINOPS-Pm404-MIB", "pm404AlmLine2HwFailPortn"),
        ("EKINOPS-Pm404-MIB", "pm404trapLineNumber"),
        ("EKINOPS-Pm404-MIB", "pm404trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm404Line2TrapCritGoesOn.setStatus(
        "current"
    )

pm404Line2TrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 25, 10, 35)
)
pm404Line2TrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm404-MIB", "pm404AlmLine2FailPortn"),
        ("EKINOPS-Pm404-MIB", "pm404AlmLine2HwFailPortn"),
        ("EKINOPS-Pm404-MIB", "pm404trapLineNumber"),
        ("EKINOPS-Pm404-MIB", "pm404trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm404Line2TrapCritGoesOff.setStatus(
        "current"
    )

pm404Line1TrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 25, 10, 40)
)
pm404Line1TrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm404-MIB", "pm404AlmLine1SfpDdmWarningPortn"),
        ("EKINOPS-Pm404-MIB", "pm404trapPortNumber"),
        ("EKINOPS-Pm404-MIB", "pm404trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm404Line1TrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm404Line1TrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 25, 10, 41)
)
pm404Line1TrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm404-MIB", "pm404AlmLine1SfpDdmWarningPortn"),
        ("EKINOPS-Pm404-MIB", "pm404trapPortNumber"),
        ("EKINOPS-Pm404-MIB", "pm404trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm404Line1TrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm404Line1TrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 25, 10, 42)
)
pm404Line1TrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm404-MIB", "pm404AlmLine1SfpDdmAlmPortn"),
        ("EKINOPS-Pm404-MIB", "pm404trapPortNumber"),
        ("EKINOPS-Pm404-MIB", "pm404trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm404Line1TrapUrgentGoesOn.setStatus(
        "current"
    )

pm404Line1TrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 25, 10, 43)
)
pm404Line1TrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm404-MIB", "pm404AlmLine1SfpDdmAlmPortn"),
        ("EKINOPS-Pm404-MIB", "pm404trapPortNumber"),
        ("EKINOPS-Pm404-MIB", "pm404trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm404Line1TrapUrgentGoesOff.setStatus(
        "current"
    )

pm404Line1TrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 25, 10, 44)
)
pm404Line1TrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm404-MIB", "pm404AlmLine1FailAccPortn"),
        ("EKINOPS-Pm404-MIB", "pm404AlmLine1HwFailAccPortn"),
        ("EKINOPS-Pm404-MIB", "pm404trapPortNumber"),
        ("EKINOPS-Pm404-MIB", "pm404trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm404Line1TrapCritGoesOn.setStatus(
        "current"
    )

pm404Line1TrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 25, 10, 45)
)
pm404Line1TrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm404-MIB", "pm404AlmLine1FailAccPortn"),
        ("EKINOPS-Pm404-MIB", "pm404AlmLine1HwFailAccPortn"),
        ("EKINOPS-Pm404-MIB", "pm404trapPortNumber"),
        ("EKINOPS-Pm404-MIB", "pm404trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm404Line1TrapCritGoesOff.setStatus(
        "current"
    )

pm404PowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 25, 10, 50)
)
pm404PowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm404-MIB", "pm404AlmDefFuseB"),
        ("EKINOPS-Pm404-MIB", "pm404AlmDefFuseA"),
        ("EKINOPS-Pm404-MIB", "pm404trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm404PowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pm404PowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 25, 10, 51)
)
pm404PowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm404-MIB", "pm404AlmDefFuseB"),
        ("EKINOPS-Pm404-MIB", "pm404AlmDefFuseA"),
        ("EKINOPS-Pm404-MIB", "pm404trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm404PowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Pm404-MIB",
    **{"modulePm404": modulePm404,
       "pm404alarms": pm404alarms,
       "pm404AlmOther": pm404AlmOther,
       "pm404AlmOtherNurg": pm404AlmOtherNurg,
       "pm404AlmsynthAlm2": pm404AlmsynthAlm2,
       "pm404AlmConfTableSave": pm404AlmConfTableSave,
       "pm404AlmInvUpload": pm404AlmInvUpload,
       "pm404AlmConfTableLoad": pm404AlmConfTableLoad,
       "pm404AlmCorrelatOff": pm404AlmCorrelatOff,
       "pm404AlmOtherUrg": pm404AlmOtherUrg,
       "pm404AlmOtherCrit": pm404AlmOtherCrit,
       "pm404AlmsynthAlm0": pm404AlmsynthAlm0,
       "pm404AlmModuleGlobFailure": pm404AlmModuleGlobFailure,
       "pm404AlmDefFuseA": pm404AlmDefFuseA,
       "pm404AlmDefFuseB": pm404AlmDefFuseB,
       "pm404AlmClient": pm404AlmClient,
       "pm404AlmClientNurg": pm404AlmClientNurg,
       "pm404Almline1SfpWarnDdmTable": pm404Almline1SfpWarnDdmTable,
       "pm404Almline1SfpWarnDdmEntry": pm404Almline1SfpWarnDdmEntry,
       "pm404Almline1SfpWarnDdmIndex": pm404Almline1SfpWarnDdmIndex,
       "pm404AlmLine1TxPwLowWngPortn": pm404AlmLine1TxPwLowWngPortn,
       "pm404AlmLine1TxPwrHighWngPortn": pm404AlmLine1TxPwrHighWngPortn,
       "pm404AlmLine1TxBiasLowWngPortn": pm404AlmLine1TxBiasLowWngPortn,
       "pm404AlmLine1TxBiasHighWngPortn": pm404AlmLine1TxBiasHighWngPortn,
       "pm404AlmLine1VccLowWngPortn": pm404AlmLine1VccLowWngPortn,
       "pm404AlmLine1VccHighWngPortn": pm404AlmLine1VccHighWngPortn,
       "pm404AlmLine1TempLowWngPortn": pm404AlmLine1TempLowWngPortn,
       "pm404AlmLine1TempHighWngPortn": pm404AlmLine1TempHighWngPortn,
       "pm404AlmLine1RxPwrLowWngPortn": pm404AlmLine1RxPwrLowWngPortn,
       "pm404AlmLine1RxPwrHighWngPortn": pm404AlmLine1RxPwrHighWngPortn,
       "pm404AlmClientUrg": pm404AlmClientUrg,
       "pm404Almline1SfpAlmDdmTable": pm404Almline1SfpAlmDdmTable,
       "pm404Almline1SfpAlmDdmEntry": pm404Almline1SfpAlmDdmEntry,
       "pm404Almline1SfpAlmDdmIndex": pm404Almline1SfpAlmDdmIndex,
       "pm404AlmLine1TxPwrLowAlaPortn": pm404AlmLine1TxPwrLowAlaPortn,
       "pm404AlmLine1Line1TxPwrHighAlaPortn": pm404AlmLine1Line1TxPwrHighAlaPortn,
       "pm404AlmLine1TxBiasLowAlaPortn": pm404AlmLine1TxBiasLowAlaPortn,
       "pm404AlmLine1TxBiasHighAlaPortn": pm404AlmLine1TxBiasHighAlaPortn,
       "pm404AlmLine1VccLowAlaPortn": pm404AlmLine1VccLowAlaPortn,
       "pm404AlmLine1VccHighAlaPortn": pm404AlmLine1VccHighAlaPortn,
       "pm404AlmLine1TempLowAlaPortn": pm404AlmLine1TempLowAlaPortn,
       "pm404AlmLine1TempHighAlaPortn": pm404AlmLine1TempHighAlaPortn,
       "pm404AlmLine1RxPwrLowAlaPortn": pm404AlmLine1RxPwrLowAlaPortn,
       "pm404AlmLine1RxPwrHighAlaPortn": pm404AlmLine1RxPwrHighAlaPortn,
       "pm404AlmClientCrit": pm404AlmClientCrit,
       "pm404AlmsynthAlmLine1Table": pm404AlmsynthAlmLine1Table,
       "pm404AlmsynthAlmLine1Entry": pm404AlmsynthAlmLine1Entry,
       "pm404AlmsynthAlmLine1Index": pm404AlmsynthAlmLine1Index,
       "pm404AlmLine1SfpAbsentPortn": pm404AlmLine1SfpAbsentPortn,
       "pm404AlmLine1DdmAbsentPortn": pm404AlmLine1DdmAbsentPortn,
       "pm404AlmLine1HwFailAccPortn": pm404AlmLine1HwFailAccPortn,
       "pm404AlmLine1LsdPortn": pm404AlmLine1LsdPortn,
       "pm404AlmLine1LocalOosPortn": pm404AlmLine1LocalOosPortn,
       "pm404AlmLine1DwCaisPortn": pm404AlmLine1DwCaisPortn,
       "pm404AlmLine1SfpDdmWarningPortn": pm404AlmLine1SfpDdmWarningPortn,
       "pm404AlmLine1SfpDdmAlmPortn": pm404AlmLine1SfpDdmAlmPortn,
       "pm404AlmLine1FailAccPortn": pm404AlmLine1FailAccPortn,
       "pm404Almline1AccessioAlmTable": pm404Almline1AccessioAlmTable,
       "pm404Almline1AccessioAlmEntry": pm404Almline1AccessioAlmEntry,
       "pm404Almline1AccessioAlmIndex": pm404Almline1AccessioAlmIndex,
       "pm404AlmLine1LasFailPortn": pm404AlmLine1LasFailPortn,
       "pm404AlmLine1LosPortn": pm404AlmLine1LosPortn,
       "pm404AlmLine1LosCdrPortn": pm404AlmLine1LosCdrPortn,
       "pm404AlmLine1ErrSigCdrPortn": pm404AlmLine1ErrSigCdrPortn,
       "pm404AlmLine": pm404AlmLine,
       "pm404AlmLineNurg": pm404AlmLineNurg,
       "pm404Almline2SfpWarnDdmTable": pm404Almline2SfpWarnDdmTable,
       "pm404Almline2SfpWarnDdmEntry": pm404Almline2SfpWarnDdmEntry,
       "pm404Almline2SfpWarnDdmIndex": pm404Almline2SfpWarnDdmIndex,
       "pm404AlmLine2TxPwLowWngPortn": pm404AlmLine2TxPwLowWngPortn,
       "pm404AlmLine2TxPwrHighWngPortn": pm404AlmLine2TxPwrHighWngPortn,
       "pm404AlmLine2TxBiasLowWngPortn": pm404AlmLine2TxBiasLowWngPortn,
       "pm404AlmLine2TxBiasHighWngPortn": pm404AlmLine2TxBiasHighWngPortn,
       "pm404AlmLine2VccLowWngPortn": pm404AlmLine2VccLowWngPortn,
       "pm404AlmLine2VccHighWngPortn": pm404AlmLine2VccHighWngPortn,
       "pm404AlmLine2TempLowWngPortn": pm404AlmLine2TempLowWngPortn,
       "pm404AlmLine2TempHighWngPortn": pm404AlmLine2TempHighWngPortn,
       "pm404AlmLine2RxPwrLowWngPortn": pm404AlmLine2RxPwrLowWngPortn,
       "pm404AlmLine2RxPwrHighWngPortn": pm404AlmLine2RxPwrHighWngPortn,
       "pm404AlmLineUrg": pm404AlmLineUrg,
       "pm404Almline2SfpAlmDdmTable": pm404Almline2SfpAlmDdmTable,
       "pm404Almline2SfpAlmDdmEntry": pm404Almline2SfpAlmDdmEntry,
       "pm404Almline2SfpAlmDdmIndex": pm404Almline2SfpAlmDdmIndex,
       "pm404AlmLine2TxPwrLowAlaPortn": pm404AlmLine2TxPwrLowAlaPortn,
       "pm404AlmLine2Line2TxPwrHighAlaPortn": pm404AlmLine2Line2TxPwrHighAlaPortn,
       "pm404AlmLine2TxBiasLowAlaPortn": pm404AlmLine2TxBiasLowAlaPortn,
       "pm404AlmLine2TxBiasHighAlaPortn": pm404AlmLine2TxBiasHighAlaPortn,
       "pm404AlmLine2VccLowAlaPortn": pm404AlmLine2VccLowAlaPortn,
       "pm404AlmLine2VccHighAlaPortn": pm404AlmLine2VccHighAlaPortn,
       "pm404AlmLine2TempLowAlaPortn": pm404AlmLine2TempLowAlaPortn,
       "pm404AlmLine2TempHighAlaPortn": pm404AlmLine2TempHighAlaPortn,
       "pm404AlmLine2RxPwrLowAlaPortn": pm404AlmLine2RxPwrLowAlaPortn,
       "pm404AlmLine2RxPwrHighAlaPortn": pm404AlmLine2RxPwrHighAlaPortn,
       "pm404AlmLineCrit": pm404AlmLineCrit,
       "pm404AlmsynthAlmLine2Table": pm404AlmsynthAlmLine2Table,
       "pm404AlmsynthAlmLine2Entry": pm404AlmsynthAlmLine2Entry,
       "pm404AlmsynthAlmLine2Index": pm404AlmsynthAlmLine2Index,
       "pm404AlmLine2SfpAbsentPortn": pm404AlmLine2SfpAbsentPortn,
       "pm404AlmLine2DdmAbsentPortn": pm404AlmLine2DdmAbsentPortn,
       "pm404AlmLine2HwFailPortn": pm404AlmLine2HwFailPortn,
       "pm404AlmLine2LsdPortn": pm404AlmLine2LsdPortn,
       "pm404AlmLine2LocalOosPortn": pm404AlmLine2LocalOosPortn,
       "pm404AlmLine2DwCaisPortn": pm404AlmLine2DwCaisPortn,
       "pm404AlmLine2DdmWarningPortn": pm404AlmLine2DdmWarningPortn,
       "pm404AlmLine2DdmAlmPortn": pm404AlmLine2DdmAlmPortn,
       "pm404AlmLine2FailPortn": pm404AlmLine2FailPortn,
       "pm404Almline2AccessioAlmTable": pm404Almline2AccessioAlmTable,
       "pm404Almline2AccessioAlmEntry": pm404Almline2AccessioAlmEntry,
       "pm404Almline2AccessioAlmIndex": pm404Almline2AccessioAlmIndex,
       "pm404AlmLine2LasFailPortn": pm404AlmLine2LasFailPortn,
       "pm404AlmLine2LosPortn": pm404AlmLine2LosPortn,
       "pm404AlmLine2LosCdrPortn": pm404AlmLine2LosCdrPortn,
       "pm404AlmLine2ErrSigCdrPortn": pm404AlmLine2ErrSigCdrPortn,
       "pm404measures": pm404measures,
       "pm404MesrOther": pm404MesrOther,
       "pm404MesrClient": pm404MesrClient,
       "pm404Mesrline1TemperatureTable": pm404Mesrline1TemperatureTable,
       "pm404Mesrline1TemperatureEntry": pm404Mesrline1TemperatureEntry,
       "pm404Mesrline1TemperatureIndex": pm404Mesrline1TemperatureIndex,
       "pm404Mesrline1TemperaturePortn": pm404Mesrline1TemperaturePortn,
       "pm404Mesrline1VoltTable": pm404Mesrline1VoltTable,
       "pm404Mesrline1VoltEntry": pm404Mesrline1VoltEntry,
       "pm404Mesrline1VoltIndex": pm404Mesrline1VoltIndex,
       "pm404Mesrline1VoltPortn": pm404Mesrline1VoltPortn,
       "pm404Mesrline1TxBiasTable": pm404Mesrline1TxBiasTable,
       "pm404Mesrline1TxBiasEntry": pm404Mesrline1TxBiasEntry,
       "pm404Mesrline1TxBiasIndex": pm404Mesrline1TxBiasIndex,
       "pm404Mesrline1TxBiasPortn": pm404Mesrline1TxBiasPortn,
       "pm404Mesrline1TxPowerTable": pm404Mesrline1TxPowerTable,
       "pm404Mesrline1TxPowerEntry": pm404Mesrline1TxPowerEntry,
       "pm404Mesrline1TxPowerIndex": pm404Mesrline1TxPowerIndex,
       "pm404Mesrline1TxPowerPortn": pm404Mesrline1TxPowerPortn,
       "pm404Mesrline1RxPowerTable": pm404Mesrline1RxPowerTable,
       "pm404Mesrline1RxPowerEntry": pm404Mesrline1RxPowerEntry,
       "pm404Mesrline1RxPowerIndex": pm404Mesrline1RxPowerIndex,
       "pm404Mesrline1RxPowerPortn": pm404Mesrline1RxPowerPortn,
       "pm404MesrLine": pm404MesrLine,
       "pm404Mesrline2TemperatureTable": pm404Mesrline2TemperatureTable,
       "pm404Mesrline2TemperatureEntry": pm404Mesrline2TemperatureEntry,
       "pm404Mesrline2TemperatureIndex": pm404Mesrline2TemperatureIndex,
       "pm404Mesrline2TemperaturePortn": pm404Mesrline2TemperaturePortn,
       "pm404Mesrline2VoltTable": pm404Mesrline2VoltTable,
       "pm404Mesrline2VoltEntry": pm404Mesrline2VoltEntry,
       "pm404Mesrline2VoltIndex": pm404Mesrline2VoltIndex,
       "pm404Mesrline2VoltPortn": pm404Mesrline2VoltPortn,
       "pm404Mesrline2TxBiasTable": pm404Mesrline2TxBiasTable,
       "pm404Mesrline2TxBiasEntry": pm404Mesrline2TxBiasEntry,
       "pm404Mesrline2TxBiasIndex": pm404Mesrline2TxBiasIndex,
       "pm404Mesrline2TxBiasPortn": pm404Mesrline2TxBiasPortn,
       "pm404Mesrline2TxPowerTable": pm404Mesrline2TxPowerTable,
       "pm404Mesrline2TxPowerEntry": pm404Mesrline2TxPowerEntry,
       "pm404Mesrline2TxPowerIndex": pm404Mesrline2TxPowerIndex,
       "pm404Mesrline2TxPowerPortn": pm404Mesrline2TxPowerPortn,
       "pm404Mesrline2RxPowerTable": pm404Mesrline2RxPowerTable,
       "pm404Mesrline2RxPowerEntry": pm404Mesrline2RxPowerEntry,
       "pm404Mesrline2RxPowerIndex": pm404Mesrline2RxPowerIndex,
       "pm404Mesrline2RxPowerPortn": pm404Mesrline2RxPowerPortn,
       "pm404counters": pm404counters,
       "pm404CntOther": pm404CntOther,
       "pm404CntClient": pm404CntClient,
       "pm404CntLine": pm404CntLine,
       "pm404controlsWrite": pm404controlsWrite,
       "pm404CtrlOther": pm404CtrlOther,
       "pm404Ctrlsynth0": pm404Ctrlsynth0,
       "pm404CtrlConfLoad": pm404CtrlConfLoad,
       "pm404CtrlConfFlash": pm404CtrlConfFlash,
       "pm404CtrlConfClear": pm404CtrlConfClear,
       "pm404Ctrlsynth4": pm404Ctrlsynth4,
       "pm404CtrlCorrelatOn": pm404CtrlCorrelatOn,
       "pm404CtrlCorrelatOff": pm404CtrlCorrelatOff,
       "pm404CtrlswMgnt": pm404CtrlswMgnt,
       "pm404CtrlColdReset": pm404CtrlColdReset,
       "pm404CtrlWarmReset": pm404CtrlWarmReset,
       "pm404CtrlledTest": pm404CtrlledTest,
       "pm404CtrlGreenLed": pm404CtrlGreenLed,
       "pm404CtrlRedLed": pm404CtrlRedLed,
       "pm404CtrlLedOff": pm404CtrlLedOff,
       "pm404CtrlmoduleOosMode": pm404CtrlmoduleOosMode,
       "pm404CtrlModuleOosMode": pm404CtrlModuleOosMode,
       "pm404CtrlClient": pm404CtrlClient,
       "pm404Ctrlline1SfpOnoffTable": pm404Ctrlline1SfpOnoffTable,
       "pm404Ctrlline1SfpOnoffEntry": pm404Ctrlline1SfpOnoffEntry,
       "pm404Ctrlline1SfpOnoffIndex": pm404Ctrlline1SfpOnoffIndex,
       "pm404Ctrlline1SfpOnoffPortn": pm404Ctrlline1SfpOnoffPortn,
       "pm404Ctrlline1LoopbackTable": pm404Ctrlline1LoopbackTable,
       "pm404Ctrlline1LoopbackEntry": pm404Ctrlline1LoopbackEntry,
       "pm404Ctrlline1LoopbackIndex": pm404Ctrlline1LoopbackIndex,
       "pm404Ctrlline1LoopbackPortn": pm404Ctrlline1LoopbackPortn,
       "pm404Ctrlline1LoopbackTermTable": pm404Ctrlline1LoopbackTermTable,
       "pm404Ctrlline1LoopbackTermEntry": pm404Ctrlline1LoopbackTermEntry,
       "pm404Ctrlline1LoopbackTermIndex": pm404Ctrlline1LoopbackTermIndex,
       "pm404Ctrlline1LoopbackTermPortn": pm404Ctrlline1LoopbackTermPortn,
       "pm404Ctrlline1OosModeTable": pm404Ctrlline1OosModeTable,
       "pm404Ctrlline1OosModeEntry": pm404Ctrlline1OosModeEntry,
       "pm404Ctrlline1OosModeIndex": pm404Ctrlline1OosModeIndex,
       "pm404Ctrlline1OosModePortn": pm404Ctrlline1OosModePortn,
       "pm404CtrlprotocolTable": pm404CtrlprotocolTable,
       "pm404CtrlprotocolEntry": pm404CtrlprotocolEntry,
       "pm404CtrlprotocolIndex": pm404CtrlprotocolIndex,
       "pm404CtrlprotocolPortn": pm404CtrlprotocolPortn,
       "pm404CtrlLine": pm404CtrlLine,
       "pm404Ctrlline2SfpOnoffTable": pm404Ctrlline2SfpOnoffTable,
       "pm404Ctrlline2SfpOnoffEntry": pm404Ctrlline2SfpOnoffEntry,
       "pm404Ctrlline2SfpOnoffIndex": pm404Ctrlline2SfpOnoffIndex,
       "pm404Ctrlline2SfpOnoffPortn": pm404Ctrlline2SfpOnoffPortn,
       "pm404Ctrlline2OosModeTable": pm404Ctrlline2OosModeTable,
       "pm404Ctrlline2OosModeEntry": pm404Ctrlline2OosModeEntry,
       "pm404Ctrlline2OosModeIndex": pm404Ctrlline2OosModeIndex,
       "pm404Ctrlline2OosModePortn": pm404Ctrlline2OosModePortn,
       "pm404Ctrlline2LoopbackTable": pm404Ctrlline2LoopbackTable,
       "pm404Ctrlline2LoopbackEntry": pm404Ctrlline2LoopbackEntry,
       "pm404Ctrlline2LoopbackIndex": pm404Ctrlline2LoopbackIndex,
       "pm404Ctrlline2LoopbackPortn": pm404Ctrlline2LoopbackPortn,
       "pm404Ctrlline2LoopbackTermTable": pm404Ctrlline2LoopbackTermTable,
       "pm404Ctrlline2LoopbackTermEntry": pm404Ctrlline2LoopbackTermEntry,
       "pm404Ctrlline2LoopbackTermIndex": pm404Ctrlline2LoopbackTermIndex,
       "pm404Ctrlline2LoopbackTermPortn": pm404Ctrlline2LoopbackTermPortn,
       "pm404ri": pm404ri,
       "pm404riTable": pm404riTable,
       "pm404RinvLine1Table": pm404RinvLine1Table,
       "pm404RinvLine1Entry": pm404RinvLine1Entry,
       "pm404RinvLine1Index": pm404RinvLine1Index,
       "pm404RinvSfpLine1": pm404RinvSfpLine1,
       "pm404RinvLine2Table": pm404RinvLine2Table,
       "pm404RinvLine2Entry": pm404RinvLine2Entry,
       "pm404RinvLine2Index": pm404RinvLine2Index,
       "pm404RinvsfpLine2": pm404RinvsfpLine2,
       "pm404RinvReloadInventory": pm404RinvReloadInventory,
       "pm404RinvHwPlatform": pm404RinvHwPlatform,
       "pm404RinvModulePlatform": pm404RinvModulePlatform,
       "pm404RinvSwPlatform": pm404RinvSwPlatform,
       "pm404RinvGwPlatform": pm404RinvGwPlatform,
       "pm404Config": pm404Config,
       "pm404CfgLsd": pm404CfgLsd,
       "pm404CfgLine1LsdTable": pm404CfgLine1LsdTable,
       "pm404CfgLine1LsdEntry": pm404CfgLine1LsdEntry,
       "pm404CfgLine1LsdIndex": pm404CfgLine1LsdIndex,
       "pm404CfgLine1LsdModePortn": pm404CfgLine1LsdModePortn,
       "pm404CfgLine1AccessioCtrbInsPortn": pm404CfgLine1AccessioCtrbInsPortn,
       "pm404CfgLine2AccessioCtrbInsPortn": pm404CfgLine2AccessioCtrbInsPortn,
       "pm404CfgStartUp": pm404CfgStartUp,
       "pm404CfgLine1StartupTable": pm404CfgLine1StartupTable,
       "pm404CfgLine1StartupEntry": pm404CfgLine1StartupEntry,
       "pm404CfgLine1StartupIndex": pm404CfgLine1StartupIndex,
       "pm404CfgLine1TrscvCtrlPortn": pm404CfgLine1TrscvCtrlPortn,
       "pm404CfgLine1ProtocolPortn": pm404CfgLine1ProtocolPortn,
       "pm404CfgLine1OosModePortn": pm404CfgLine1OosModePortn,
       "pm404CfgLine2StartupTable": pm404CfgLine2StartupTable,
       "pm404CfgLine2StartupEntry": pm404CfgLine2StartupEntry,
       "pm404CfgLine2StartupIndex": pm404CfgLine2StartupIndex,
       "pm404CfgLine2TrscvCtrlPortn": pm404CfgLine2TrscvCtrlPortn,
       "pm404CfgLine2OosModePortn": pm404CfgLine2OosModePortn,
       "pm404CfgLabels": pm404CfgLabels,
       "pm404CfgLabelclientTable": pm404CfgLabelclientTable,
       "pm404CfgLabelclientEntry": pm404CfgLabelclientEntry,
       "pm404CfgLabelclientIndex": pm404CfgLabelclientIndex,
       "pm404CfgLabelclientPortn": pm404CfgLabelclientPortn,
       "pm404CfgLabellineTable": pm404CfgLabellineTable,
       "pm404CfgLabellineEntry": pm404CfgLabellineEntry,
       "pm404CfgLabellineIndex": pm404CfgLabellineIndex,
       "pm404CfgLabellinePortn": pm404CfgLabellinePortn,
       "pm404CfgWriteConfiguration": pm404CfgWriteConfiguration,
       "pm404traps": pm404traps,
       "pm404trapPortNumber": pm404trapPortNumber,
       "pm404trapLineNumber": pm404trapLineNumber,
       "pm404trapBoardNumber": pm404trapBoardNumber,
       "pm404Line2TrapNotUrgentGoesOn": pm404Line2TrapNotUrgentGoesOn,
       "pm404Line2TrapNotUrgentGoesOff": pm404Line2TrapNotUrgentGoesOff,
       "pm404Line2TrapUrgentGoesOn": pm404Line2TrapUrgentGoesOn,
       "pm404Line2TrapUrgentGoesOff": pm404Line2TrapUrgentGoesOff,
       "pm404Line2TrapCritGoesOn": pm404Line2TrapCritGoesOn,
       "pm404Line2TrapCritGoesOff": pm404Line2TrapCritGoesOff,
       "pm404Line1TrapNotUrgentGoesOn": pm404Line1TrapNotUrgentGoesOn,
       "pm404Line1TrapNotUrgentGoesOff": pm404Line1TrapNotUrgentGoesOff,
       "pm404Line1TrapUrgentGoesOn": pm404Line1TrapUrgentGoesOn,
       "pm404Line1TrapUrgentGoesOff": pm404Line1TrapUrgentGoesOff,
       "pm404Line1TrapCritGoesOn": pm404Line1TrapCritGoesOn,
       "pm404Line1TrapCritGoesOff": pm404Line1TrapCritGoesOff,
       "pm404PowerTrapUrgentGoesOn": pm404PowerTrapUrgentGoesOn,
       "pm404PowerTrapUrgentGoesOff": pm404PowerTrapUrgentGoesOff}
)
