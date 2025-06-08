# SNMP MIB module (EKINOPS-Pm251d-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Pm251d-MIB.mib
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
 ekinops) = mibBuilder.importSymbols(
    "EKINOPS-MIB",
    "EkiApiState",
    "EkiMeasureType",
    "EkiMode",
    "EkiOnOff",
    "EkiProtocol",
    "EkiState",
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

modulePm251d = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31)
)
if mibBuilder.loadTexts:
    modulePm251d.setRevisions(
        ("2006-11-08 00:00",
         "2007-08-30 00:00",
         "2008-01-22 00:00",
         "2008-03-19 00:00",
         "2009-04-09 00:00",
         "2009-10-07 00:00",
         "2010-03-03 00:00",
         "2011-02-03 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Pm251dalarms_ObjectIdentity = ObjectIdentity
pm251dalarms = _Pm251dalarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2)
)
_Pm251dAlmOther_ObjectIdentity = ObjectIdentity
pm251dAlmOther = _Pm251dAlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 1)
)
_Pm251dAlmOtherNurg_ObjectIdentity = ObjectIdentity
pm251dAlmOtherNurg = _Pm251dAlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 1, 1)
)
_Pm251dAlmsynthAlm0_ObjectIdentity = ObjectIdentity
pm251dAlmsynthAlm0 = _Pm251dAlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 1, 1, 0)
)
_Pm251dAlmModGlobFail_Type = EkiOnOff
_Pm251dAlmModGlobFail_Object = MibScalar
pm251dAlmModGlobFail = _Pm251dAlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 1, 1, 0, 9),
    _Pm251dAlmModGlobFail_Type()
)
pm251dAlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmModGlobFail.setStatus("current")
_Pm251dAlmDefFuseA_Type = EkiOnOff
_Pm251dAlmDefFuseA_Object = MibScalar
pm251dAlmDefFuseA = _Pm251dAlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 1, 1, 0, 15),
    _Pm251dAlmDefFuseA_Type()
)
pm251dAlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmDefFuseA.setStatus("current")
_Pm251dAlmDefFuseB_Type = EkiOnOff
_Pm251dAlmDefFuseB_Object = MibScalar
pm251dAlmDefFuseB = _Pm251dAlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 1, 1, 0, 16),
    _Pm251dAlmDefFuseB_Type()
)
pm251dAlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmDefFuseB.setStatus("current")
_Pm251dAlmsynthAlm2_ObjectIdentity = ObjectIdentity
pm251dAlmsynthAlm2 = _Pm251dAlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 1, 1, 2)
)
_Pm251dAlmConfTableSave_Type = EkiOnOff
_Pm251dAlmConfTableSave_Object = MibScalar
pm251dAlmConfTableSave = _Pm251dAlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 1, 1, 2, 1),
    _Pm251dAlmConfTableSave_Type()
)
pm251dAlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmConfTableSave.setStatus("current")
_Pm251dAlmInvUpload_Type = EkiOnOff
_Pm251dAlmInvUpload_Object = MibScalar
pm251dAlmInvUpload = _Pm251dAlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 1, 1, 2, 2),
    _Pm251dAlmInvUpload_Type()
)
pm251dAlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmInvUpload.setStatus("current")
_Pm251dAlmConfTableLoad_Type = EkiOnOff
_Pm251dAlmConfTableLoad_Object = MibScalar
pm251dAlmConfTableLoad = _Pm251dAlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 1, 1, 2, 3),
    _Pm251dAlmConfTableLoad_Type()
)
pm251dAlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmConfTableLoad.setStatus("current")
_Pm251dAlmCorrelatOff_Type = EkiOnOff
_Pm251dAlmCorrelatOff_Object = MibScalar
pm251dAlmCorrelatOff = _Pm251dAlmCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 1, 1, 2, 4),
    _Pm251dAlmCorrelatOff_Type()
)
pm251dAlmCorrelatOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmCorrelatOff.setStatus("current")
_Pm251dAlmMaintenanceOn_Type = EkiOnOff
_Pm251dAlmMaintenanceOn_Object = MibScalar
pm251dAlmMaintenanceOn = _Pm251dAlmMaintenanceOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 1, 1, 2, 5),
    _Pm251dAlmMaintenanceOn_Type()
)
pm251dAlmMaintenanceOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmMaintenanceOn.setStatus("current")
_Pm251dAlmOtherUrg_ObjectIdentity = ObjectIdentity
pm251dAlmOtherUrg = _Pm251dAlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 1, 2)
)
_Pm251dAlmmodInitFailLevel2_ObjectIdentity = ObjectIdentity
pm251dAlmmodInitFailLevel2 = _Pm251dAlmmodInitFailLevel2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 1, 2, 194)
)
_Pm251dAlmLedFail_Type = EkiOnOff
_Pm251dAlmLedFail_Object = MibScalar
pm251dAlmLedFail = _Pm251dAlmLedFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 1, 2, 194, 1),
    _Pm251dAlmLedFail_Type()
)
pm251dAlmLedFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmLedFail.setStatus("current")
_Pm251dAlmNextColdBootForced_Type = EkiOnOff
_Pm251dAlmNextColdBootForced_Object = MibScalar
pm251dAlmNextColdBootForced = _Pm251dAlmNextColdBootForced_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 1, 2, 194, 2),
    _Pm251dAlmNextColdBootForced_Type()
)
pm251dAlmNextColdBootForced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmNextColdBootForced.setStatus("current")
_Pm251dAlmBootUndone_Type = EkiOnOff
_Pm251dAlmBootUndone_Object = MibScalar
pm251dAlmBootUndone = _Pm251dAlmBootUndone_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 1, 2, 194, 3),
    _Pm251dAlmBootUndone_Type()
)
pm251dAlmBootUndone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmBootUndone.setStatus("current")
_Pm251dAlmResetHwInitFail_Type = EkiOnOff
_Pm251dAlmResetHwInitFail_Object = MibScalar
pm251dAlmResetHwInitFail = _Pm251dAlmResetHwInitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 1, 2, 194, 4),
    _Pm251dAlmResetHwInitFail_Type()
)
pm251dAlmResetHwInitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmResetHwInitFail.setStatus("current")
_Pm251dAlmSwInitFail_Type = EkiOnOff
_Pm251dAlmSwInitFail_Object = MibScalar
pm251dAlmSwInitFail = _Pm251dAlmSwInitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 1, 2, 194, 5),
    _Pm251dAlmSwInitFail_Type()
)
pm251dAlmSwInitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmSwInitFail.setStatus("current")
_Pm251dAlmmodInitFailLevel3_ObjectIdentity = ObjectIdentity
pm251dAlmmodInitFailLevel3 = _Pm251dAlmmodInitFailLevel3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 1, 2, 195)
)
_Pm251dAlmGwIdentFail_Type = EkiOnOff
_Pm251dAlmGwIdentFail_Object = MibScalar
pm251dAlmGwIdentFail = _Pm251dAlmGwIdentFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 1, 2, 195, 1),
    _Pm251dAlmGwIdentFail_Type()
)
pm251dAlmGwIdentFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmGwIdentFail.setStatus("current")
_Pm251dAlmObmTypeReadFail_Type = EkiOnOff
_Pm251dAlmObmTypeReadFail_Object = MibScalar
pm251dAlmObmTypeReadFail = _Pm251dAlmObmTypeReadFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 1, 2, 195, 2),
    _Pm251dAlmObmTypeReadFail_Type()
)
pm251dAlmObmTypeReadFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmObmTypeReadFail.setStatus("current")
_Pm251dAlmInitModuleFail_Type = EkiOnOff
_Pm251dAlmInitModuleFail_Object = MibScalar
pm251dAlmInitModuleFail = _Pm251dAlmInitModuleFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 1, 2, 195, 3),
    _Pm251dAlmInitModuleFail_Type()
)
pm251dAlmInitModuleFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmInitModuleFail.setStatus("current")
_Pm251dAlmSfp1InitFail_Type = EkiOnOff
_Pm251dAlmSfp1InitFail_Object = MibScalar
pm251dAlmSfp1InitFail = _Pm251dAlmSfp1InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 1, 2, 195, 5),
    _Pm251dAlmSfp1InitFail_Type()
)
pm251dAlmSfp1InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmSfp1InitFail.setStatus("current")
_Pm251dAlmSfp2InitFail_Type = EkiOnOff
_Pm251dAlmSfp2InitFail_Object = MibScalar
pm251dAlmSfp2InitFail = _Pm251dAlmSfp2InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 1, 2, 195, 6),
    _Pm251dAlmSfp2InitFail_Type()
)
pm251dAlmSfp2InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmSfp2InitFail.setStatus("current")
_Pm251dAlmLine1InitFail_Type = EkiOnOff
_Pm251dAlmLine1InitFail_Object = MibScalar
pm251dAlmLine1InitFail = _Pm251dAlmLine1InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 1, 2, 195, 7),
    _Pm251dAlmLine1InitFail_Type()
)
pm251dAlmLine1InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmLine1InitFail.setStatus("current")
_Pm251dAlmLine2InitFail_Type = EkiOnOff
_Pm251dAlmLine2InitFail_Object = MibScalar
pm251dAlmLine2InitFail = _Pm251dAlmLine2InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 1, 2, 195, 8),
    _Pm251dAlmLine2InitFail_Type()
)
pm251dAlmLine2InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmLine2InitFail.setStatus("current")
_Pm251dAlmClient1InitFail_Type = EkiOnOff
_Pm251dAlmClient1InitFail_Object = MibScalar
pm251dAlmClient1InitFail = _Pm251dAlmClient1InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 1, 2, 195, 9),
    _Pm251dAlmClient1InitFail_Type()
)
pm251dAlmClient1InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClient1InitFail.setStatus("current")
_Pm251dAlmClient2InitFail_Type = EkiOnOff
_Pm251dAlmClient2InitFail_Object = MibScalar
pm251dAlmClient2InitFail = _Pm251dAlmClient2InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 1, 2, 195, 10),
    _Pm251dAlmClient2InitFail_Type()
)
pm251dAlmClient2InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClient2InitFail.setStatus("current")
_Pm251dAlmOtherCrit_ObjectIdentity = ObjectIdentity
pm251dAlmOtherCrit = _Pm251dAlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 1, 3)
)
_Pm251dAlmPort_ObjectIdentity = ObjectIdentity
pm251dAlmPort = _Pm251dAlmPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2)
)
_Pm251dAlmPortNurg_ObjectIdentity = ObjectIdentity
pm251dAlmPortNurg = _Pm251dAlmPortNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 1)
)
_Pm251dAlmclientSfpWarnDdmTable_Object = MibTable
pm251dAlmclientSfpWarnDdmTable = _Pm251dAlmclientSfpWarnDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 1, 48)
)
if mibBuilder.loadTexts:
    pm251dAlmclientSfpWarnDdmTable.setStatus("current")
_Pm251dAlmclientSfpWarnDdmEntry_Object = MibTableRow
pm251dAlmclientSfpWarnDdmEntry = _Pm251dAlmclientSfpWarnDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 1, 48, 1)
)
pm251dAlmclientSfpWarnDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dAlmclientSfpWarnDdmIndex"),
)
if mibBuilder.loadTexts:
    pm251dAlmclientSfpWarnDdmEntry.setStatus("current")


class _Pm251dAlmclientSfpWarnDdmIndex_Type(Integer32):
    """Custom type pm251dAlmclientSfpWarnDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dAlmclientSfpWarnDdmIndex_Type.__name__ = "Integer32"
_Pm251dAlmclientSfpWarnDdmIndex_Object = MibTableColumn
pm251dAlmclientSfpWarnDdmIndex = _Pm251dAlmclientSfpWarnDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 1, 48, 1, 1),
    _Pm251dAlmclientSfpWarnDdmIndex_Type()
)
pm251dAlmclientSfpWarnDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmclientSfpWarnDdmIndex.setStatus("current")
_Pm251dAlmClientTxPwLowWngPortn_Type = EkiOnOff
_Pm251dAlmClientTxPwLowWngPortn_Object = MibTableColumn
pm251dAlmClientTxPwLowWngPortn = _Pm251dAlmClientTxPwLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 1, 48, 1, 2),
    _Pm251dAlmClientTxPwLowWngPortn_Type()
)
pm251dAlmClientTxPwLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientTxPwLowWngPortn.setStatus("current")
_Pm251dAlmClientTxPwrHighWngPortn_Type = EkiOnOff
_Pm251dAlmClientTxPwrHighWngPortn_Object = MibTableColumn
pm251dAlmClientTxPwrHighWngPortn = _Pm251dAlmClientTxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 1, 48, 1, 3),
    _Pm251dAlmClientTxPwrHighWngPortn_Type()
)
pm251dAlmClientTxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientTxPwrHighWngPortn.setStatus("current")
_Pm251dAlmClientTxBiasLowWngPortn_Type = EkiOnOff
_Pm251dAlmClientTxBiasLowWngPortn_Object = MibTableColumn
pm251dAlmClientTxBiasLowWngPortn = _Pm251dAlmClientTxBiasLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 1, 48, 1, 4),
    _Pm251dAlmClientTxBiasLowWngPortn_Type()
)
pm251dAlmClientTxBiasLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientTxBiasLowWngPortn.setStatus("current")
_Pm251dAlmClientTxBiasHighWngPortn_Type = EkiOnOff
_Pm251dAlmClientTxBiasHighWngPortn_Object = MibTableColumn
pm251dAlmClientTxBiasHighWngPortn = _Pm251dAlmClientTxBiasHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 1, 48, 1, 5),
    _Pm251dAlmClientTxBiasHighWngPortn_Type()
)
pm251dAlmClientTxBiasHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientTxBiasHighWngPortn.setStatus("current")
_Pm251dAlmClientVccLowWngPortn_Type = EkiOnOff
_Pm251dAlmClientVccLowWngPortn_Object = MibTableColumn
pm251dAlmClientVccLowWngPortn = _Pm251dAlmClientVccLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 1, 48, 1, 6),
    _Pm251dAlmClientVccLowWngPortn_Type()
)
pm251dAlmClientVccLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientVccLowWngPortn.setStatus("current")
_Pm251dAlmClientVccHighWngPortn_Type = EkiOnOff
_Pm251dAlmClientVccHighWngPortn_Object = MibTableColumn
pm251dAlmClientVccHighWngPortn = _Pm251dAlmClientVccHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 1, 48, 1, 7),
    _Pm251dAlmClientVccHighWngPortn_Type()
)
pm251dAlmClientVccHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientVccHighWngPortn.setStatus("current")
_Pm251dAlmClientTempLowWngPortn_Type = EkiOnOff
_Pm251dAlmClientTempLowWngPortn_Object = MibTableColumn
pm251dAlmClientTempLowWngPortn = _Pm251dAlmClientTempLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 1, 48, 1, 8),
    _Pm251dAlmClientTempLowWngPortn_Type()
)
pm251dAlmClientTempLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientTempLowWngPortn.setStatus("current")
_Pm251dAlmClientTempHighWngPortn_Type = EkiOnOff
_Pm251dAlmClientTempHighWngPortn_Object = MibTableColumn
pm251dAlmClientTempHighWngPortn = _Pm251dAlmClientTempHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 1, 48, 1, 9),
    _Pm251dAlmClientTempHighWngPortn_Type()
)
pm251dAlmClientTempHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientTempHighWngPortn.setStatus("current")
_Pm251dAlmClientRxPwrLowWngPortn_Type = EkiOnOff
_Pm251dAlmClientRxPwrLowWngPortn_Object = MibTableColumn
pm251dAlmClientRxPwrLowWngPortn = _Pm251dAlmClientRxPwrLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 1, 48, 1, 16),
    _Pm251dAlmClientRxPwrLowWngPortn_Type()
)
pm251dAlmClientRxPwrLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientRxPwrLowWngPortn.setStatus("current")
_Pm251dAlmClientRxPwrHighWngPortn_Type = EkiOnOff
_Pm251dAlmClientRxPwrHighWngPortn_Object = MibTableColumn
pm251dAlmClientRxPwrHighWngPortn = _Pm251dAlmClientRxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 1, 48, 1, 17),
    _Pm251dAlmClientRxPwrHighWngPortn_Type()
)
pm251dAlmClientRxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientRxPwrHighWngPortn.setStatus("current")
_Pm251dAlmPortUrg_ObjectIdentity = ObjectIdentity
pm251dAlmPortUrg = _Pm251dAlmPortUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 2)
)
_Pm251dAlmclientSfpAlmDdmTable_Object = MibTable
pm251dAlmclientSfpAlmDdmTable = _Pm251dAlmclientSfpAlmDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 2, 32)
)
if mibBuilder.loadTexts:
    pm251dAlmclientSfpAlmDdmTable.setStatus("current")
_Pm251dAlmclientSfpAlmDdmEntry_Object = MibTableRow
pm251dAlmclientSfpAlmDdmEntry = _Pm251dAlmclientSfpAlmDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 2, 32, 1)
)
pm251dAlmclientSfpAlmDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dAlmclientSfpAlmDdmIndex"),
)
if mibBuilder.loadTexts:
    pm251dAlmclientSfpAlmDdmEntry.setStatus("current")


class _Pm251dAlmclientSfpAlmDdmIndex_Type(Integer32):
    """Custom type pm251dAlmclientSfpAlmDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dAlmclientSfpAlmDdmIndex_Type.__name__ = "Integer32"
_Pm251dAlmclientSfpAlmDdmIndex_Object = MibTableColumn
pm251dAlmclientSfpAlmDdmIndex = _Pm251dAlmclientSfpAlmDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 2, 32, 1, 1),
    _Pm251dAlmclientSfpAlmDdmIndex_Type()
)
pm251dAlmclientSfpAlmDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmclientSfpAlmDdmIndex.setStatus("current")
_Pm251dAlmClientTxPwrLowAlaPortn_Type = EkiOnOff
_Pm251dAlmClientTxPwrLowAlaPortn_Object = MibTableColumn
pm251dAlmClientTxPwrLowAlaPortn = _Pm251dAlmClientTxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 2, 32, 1, 2),
    _Pm251dAlmClientTxPwrLowAlaPortn_Type()
)
pm251dAlmClientTxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientTxPwrLowAlaPortn.setStatus("current")
_Pm251dAlmClientTxPwrHighAlaPortn_Type = EkiOnOff
_Pm251dAlmClientTxPwrHighAlaPortn_Object = MibTableColumn
pm251dAlmClientTxPwrHighAlaPortn = _Pm251dAlmClientTxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 2, 32, 1, 3),
    _Pm251dAlmClientTxPwrHighAlaPortn_Type()
)
pm251dAlmClientTxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientTxPwrHighAlaPortn.setStatus("current")
_Pm251dAlmClientTxBiasLowAlaPortn_Type = EkiOnOff
_Pm251dAlmClientTxBiasLowAlaPortn_Object = MibTableColumn
pm251dAlmClientTxBiasLowAlaPortn = _Pm251dAlmClientTxBiasLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 2, 32, 1, 4),
    _Pm251dAlmClientTxBiasLowAlaPortn_Type()
)
pm251dAlmClientTxBiasLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientTxBiasLowAlaPortn.setStatus("current")
_Pm251dAlmClientTxBiasHighAlaPortn_Type = EkiOnOff
_Pm251dAlmClientTxBiasHighAlaPortn_Object = MibTableColumn
pm251dAlmClientTxBiasHighAlaPortn = _Pm251dAlmClientTxBiasHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 2, 32, 1, 5),
    _Pm251dAlmClientTxBiasHighAlaPortn_Type()
)
pm251dAlmClientTxBiasHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientTxBiasHighAlaPortn.setStatus("current")
_Pm251dAlmClientVccLowAlaPortn_Type = EkiOnOff
_Pm251dAlmClientVccLowAlaPortn_Object = MibTableColumn
pm251dAlmClientVccLowAlaPortn = _Pm251dAlmClientVccLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 2, 32, 1, 6),
    _Pm251dAlmClientVccLowAlaPortn_Type()
)
pm251dAlmClientVccLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientVccLowAlaPortn.setStatus("current")
_Pm251dAlmClientVccHighAlaPortn_Type = EkiOnOff
_Pm251dAlmClientVccHighAlaPortn_Object = MibTableColumn
pm251dAlmClientVccHighAlaPortn = _Pm251dAlmClientVccHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 2, 32, 1, 7),
    _Pm251dAlmClientVccHighAlaPortn_Type()
)
pm251dAlmClientVccHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientVccHighAlaPortn.setStatus("current")
_Pm251dAlmClientTempLowAlaPortn_Type = EkiOnOff
_Pm251dAlmClientTempLowAlaPortn_Object = MibTableColumn
pm251dAlmClientTempLowAlaPortn = _Pm251dAlmClientTempLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 2, 32, 1, 8),
    _Pm251dAlmClientTempLowAlaPortn_Type()
)
pm251dAlmClientTempLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientTempLowAlaPortn.setStatus("current")
_Pm251dAlmClientTempHighAlaPortn_Type = EkiOnOff
_Pm251dAlmClientTempHighAlaPortn_Object = MibTableColumn
pm251dAlmClientTempHighAlaPortn = _Pm251dAlmClientTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 2, 32, 1, 9),
    _Pm251dAlmClientTempHighAlaPortn_Type()
)
pm251dAlmClientTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientTempHighAlaPortn.setStatus("current")
_Pm251dAlmClientRxPwrLowAlaPortn_Type = EkiOnOff
_Pm251dAlmClientRxPwrLowAlaPortn_Object = MibTableColumn
pm251dAlmClientRxPwrLowAlaPortn = _Pm251dAlmClientRxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 2, 32, 1, 16),
    _Pm251dAlmClientRxPwrLowAlaPortn_Type()
)
pm251dAlmClientRxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientRxPwrLowAlaPortn.setStatus("current")
_Pm251dAlmClientRxPwrHighAlaPortn_Type = EkiOnOff
_Pm251dAlmClientRxPwrHighAlaPortn_Object = MibTableColumn
pm251dAlmClientRxPwrHighAlaPortn = _Pm251dAlmClientRxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 2, 32, 1, 17),
    _Pm251dAlmClientRxPwrHighAlaPortn_Type()
)
pm251dAlmClientRxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientRxPwrHighAlaPortn.setStatus("current")
_Pm251dAlmPortCrit_ObjectIdentity = ObjectIdentity
pm251dAlmPortCrit = _Pm251dAlmPortCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 3)
)
_Pm251dAlmsynthAlmClientTable_Object = MibTable
pm251dAlmsynthAlmClientTable = _Pm251dAlmsynthAlmClientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    pm251dAlmsynthAlmClientTable.setStatus("current")
_Pm251dAlmsynthAlmClientEntry_Object = MibTableRow
pm251dAlmsynthAlmClientEntry = _Pm251dAlmsynthAlmClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 3, 8, 1)
)
pm251dAlmsynthAlmClientEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dAlmsynthAlmClientIndex"),
)
if mibBuilder.loadTexts:
    pm251dAlmsynthAlmClientEntry.setStatus("current")


class _Pm251dAlmsynthAlmClientIndex_Type(Integer32):
    """Custom type pm251dAlmsynthAlmClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dAlmsynthAlmClientIndex_Type.__name__ = "Integer32"
_Pm251dAlmsynthAlmClientIndex_Object = MibTableColumn
pm251dAlmsynthAlmClientIndex = _Pm251dAlmsynthAlmClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 3, 8, 1, 1),
    _Pm251dAlmsynthAlmClientIndex_Type()
)
pm251dAlmsynthAlmClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmsynthAlmClientIndex.setStatus("current")
_Pm251dAlmClientSfpAbsentPortn_Type = EkiOnOff
_Pm251dAlmClientSfpAbsentPortn_Object = MibTableColumn
pm251dAlmClientSfpAbsentPortn = _Pm251dAlmClientSfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 3, 8, 1, 2),
    _Pm251dAlmClientSfpAbsentPortn_Type()
)
pm251dAlmClientSfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientSfpAbsentPortn.setStatus("current")
_Pm251dAlmClientDdmAbsentPortn_Type = EkiOnOff
_Pm251dAlmClientDdmAbsentPortn_Object = MibTableColumn
pm251dAlmClientDdmAbsentPortn = _Pm251dAlmClientDdmAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 3, 8, 1, 3),
    _Pm251dAlmClientDdmAbsentPortn_Type()
)
pm251dAlmClientDdmAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientDdmAbsentPortn.setStatus("current")
_Pm251dAlmClientHwFailAccPortn_Type = EkiOnOff
_Pm251dAlmClientHwFailAccPortn_Object = MibTableColumn
pm251dAlmClientHwFailAccPortn = _Pm251dAlmClientHwFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 3, 8, 1, 5),
    _Pm251dAlmClientHwFailAccPortn_Type()
)
pm251dAlmClientHwFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientHwFailAccPortn.setStatus("current")
_Pm251dAlmClientLsdPortn_Type = EkiOnOff
_Pm251dAlmClientLsdPortn_Object = MibTableColumn
pm251dAlmClientLsdPortn = _Pm251dAlmClientLsdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 3, 8, 1, 6),
    _Pm251dAlmClientLsdPortn_Type()
)
pm251dAlmClientLsdPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientLsdPortn.setStatus("current")
_Pm251dAlmClientLocalOosPortn_Type = EkiOnOff
_Pm251dAlmClientLocalOosPortn_Object = MibTableColumn
pm251dAlmClientLocalOosPortn = _Pm251dAlmClientLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 3, 8, 1, 7),
    _Pm251dAlmClientLocalOosPortn_Type()
)
pm251dAlmClientLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientLocalOosPortn.setStatus("current")
_Pm251dAlmClientRemoteOosPortn_Type = EkiOnOff
_Pm251dAlmClientRemoteOosPortn_Object = MibTableColumn
pm251dAlmClientRemoteOosPortn = _Pm251dAlmClientRemoteOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 3, 8, 1, 8),
    _Pm251dAlmClientRemoteOosPortn_Type()
)
pm251dAlmClientRemoteOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientRemoteOosPortn.setStatus("current")
_Pm251dAlmClientDwCaisPortn_Type = EkiOnOff
_Pm251dAlmClientDwCaisPortn_Object = MibTableColumn
pm251dAlmClientDwCaisPortn = _Pm251dAlmClientDwCaisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 3, 8, 1, 9),
    _Pm251dAlmClientDwCaisPortn_Type()
)
pm251dAlmClientDwCaisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientDwCaisPortn.setStatus("current")
_Pm251dAlmClientSfpDdmWarningPortn_Type = EkiOnOff
_Pm251dAlmClientSfpDdmWarningPortn_Object = MibTableColumn
pm251dAlmClientSfpDdmWarningPortn = _Pm251dAlmClientSfpDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 3, 8, 1, 10),
    _Pm251dAlmClientSfpDdmWarningPortn_Type()
)
pm251dAlmClientSfpDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientSfpDdmWarningPortn.setStatus("current")
_Pm251dAlmClientSfpDdmAlmPortn_Type = EkiOnOff
_Pm251dAlmClientSfpDdmAlmPortn_Object = MibTableColumn
pm251dAlmClientSfpDdmAlmPortn = _Pm251dAlmClientSfpDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 3, 8, 1, 11),
    _Pm251dAlmClientSfpDdmAlmPortn_Type()
)
pm251dAlmClientSfpDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientSfpDdmAlmPortn.setStatus("current")
_Pm251dAlmClientFailAccPortn_Type = EkiOnOff
_Pm251dAlmClientFailAccPortn_Object = MibTableColumn
pm251dAlmClientFailAccPortn = _Pm251dAlmClientFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 3, 8, 1, 13),
    _Pm251dAlmClientFailAccPortn_Type()
)
pm251dAlmClientFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientFailAccPortn.setStatus("current")
_Pm251dAlmClientUpCsfPortn_Type = EkiOnOff
_Pm251dAlmClientUpCsfPortn_Object = MibTableColumn
pm251dAlmClientUpCsfPortn = _Pm251dAlmClientUpCsfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 3, 8, 1, 17),
    _Pm251dAlmClientUpCsfPortn_Type()
)
pm251dAlmClientUpCsfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientUpCsfPortn.setStatus("current")
_Pm251dAlmaccessioAlmTable_Object = MibTable
pm251dAlmaccessioAlmTable = _Pm251dAlmaccessioAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 3, 16)
)
if mibBuilder.loadTexts:
    pm251dAlmaccessioAlmTable.setStatus("current")
_Pm251dAlmaccessioAlmEntry_Object = MibTableRow
pm251dAlmaccessioAlmEntry = _Pm251dAlmaccessioAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 3, 16, 1)
)
pm251dAlmaccessioAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dAlmaccessioAlmIndex"),
)
if mibBuilder.loadTexts:
    pm251dAlmaccessioAlmEntry.setStatus("current")


class _Pm251dAlmaccessioAlmIndex_Type(Integer32):
    """Custom type pm251dAlmaccessioAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dAlmaccessioAlmIndex_Type.__name__ = "Integer32"
_Pm251dAlmaccessioAlmIndex_Object = MibTableColumn
pm251dAlmaccessioAlmIndex = _Pm251dAlmaccessioAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 3, 16, 1, 1),
    _Pm251dAlmaccessioAlmIndex_Type()
)
pm251dAlmaccessioAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmaccessioAlmIndex.setStatus("current")
_Pm251dAlmClientDwLasFailPortn_Type = EkiOnOff
_Pm251dAlmClientDwLasFailPortn_Object = MibTableColumn
pm251dAlmClientDwLasFailPortn = _Pm251dAlmClientDwLasFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 3, 16, 1, 2),
    _Pm251dAlmClientDwLasFailPortn_Type()
)
pm251dAlmClientDwLasFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientDwLasFailPortn.setStatus("current")
_Pm251dAlmClientUpLosPortn_Type = EkiOnOff
_Pm251dAlmClientUpLosPortn_Object = MibTableColumn
pm251dAlmClientUpLosPortn = _Pm251dAlmClientUpLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 3, 16, 1, 5),
    _Pm251dAlmClientUpLosPortn_Type()
)
pm251dAlmClientUpLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientUpLosPortn.setStatus("current")
_Pm251dAlmclientMapperDeAlmTable_Object = MibTable
pm251dAlmclientMapperDeAlmTable = _Pm251dAlmclientMapperDeAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 3, 72)
)
if mibBuilder.loadTexts:
    pm251dAlmclientMapperDeAlmTable.setStatus("current")
_Pm251dAlmclientMapperDeAlmEntry_Object = MibTableRow
pm251dAlmclientMapperDeAlmEntry = _Pm251dAlmclientMapperDeAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 3, 72, 1)
)
pm251dAlmclientMapperDeAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dAlmclientMapperDeAlmIndex"),
)
if mibBuilder.loadTexts:
    pm251dAlmclientMapperDeAlmEntry.setStatus("current")


class _Pm251dAlmclientMapperDeAlmIndex_Type(Integer32):
    """Custom type pm251dAlmclientMapperDeAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dAlmclientMapperDeAlmIndex_Type.__name__ = "Integer32"
_Pm251dAlmclientMapperDeAlmIndex_Object = MibTableColumn
pm251dAlmclientMapperDeAlmIndex = _Pm251dAlmclientMapperDeAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 3, 72, 1, 1),
    _Pm251dAlmclientMapperDeAlmIndex_Type()
)
pm251dAlmclientMapperDeAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmclientMapperDeAlmIndex.setStatus("current")
_Pm251dAlmClientUpAccOosPortn_Type = EkiOnOff
_Pm251dAlmClientUpAccOosPortn_Object = MibTableColumn
pm251dAlmClientUpAccOosPortn = _Pm251dAlmClientUpAccOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 3, 72, 1, 2),
    _Pm251dAlmClientUpAccOosPortn_Type()
)
pm251dAlmClientUpAccOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientUpAccOosPortn.setStatus("current")
_Pm251dAlmClientUpBufferOvlPortn_Type = EkiOnOff
_Pm251dAlmClientUpBufferOvlPortn_Object = MibTableColumn
pm251dAlmClientUpBufferOvlPortn = _Pm251dAlmClientUpBufferOvlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 3, 72, 1, 11),
    _Pm251dAlmClientUpBufferOvlPortn_Type()
)
pm251dAlmClientUpBufferOvlPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientUpBufferOvlPortn.setStatus("current")
_Pm251dAlmClientDwCsfDetPortn_Type = EkiOnOff
_Pm251dAlmClientDwCsfDetPortn_Object = MibTableColumn
pm251dAlmClientDwCsfDetPortn = _Pm251dAlmClientDwCsfDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 3, 72, 1, 12),
    _Pm251dAlmClientDwCsfDetPortn_Type()
)
pm251dAlmClientDwCsfDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientDwCsfDetPortn.setStatus("current")
_Pm251dAlmClientDwBufferOvlPortn_Type = EkiOnOff
_Pm251dAlmClientDwBufferOvlPortn_Object = MibTableColumn
pm251dAlmClientDwBufferOvlPortn = _Pm251dAlmClientDwBufferOvlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 3, 72, 1, 15),
    _Pm251dAlmClientDwBufferOvlPortn_Type()
)
pm251dAlmClientDwBufferOvlPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientDwBufferOvlPortn.setStatus("current")
_Pm251dAlmClientLoopAccFifoFailPortn_Type = EkiOnOff
_Pm251dAlmClientLoopAccFifoFailPortn_Object = MibTableColumn
pm251dAlmClientLoopAccFifoFailPortn = _Pm251dAlmClientLoopAccFifoFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 3, 72, 1, 16),
    _Pm251dAlmClientLoopAccFifoFailPortn_Type()
)
pm251dAlmClientLoopAccFifoFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientLoopAccFifoFailPortn.setStatus("deprecated")
_Pm251dAlmaccessioSdhAlarmTable_Object = MibTable
pm251dAlmaccessioSdhAlarmTable = _Pm251dAlmaccessioSdhAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 3, 104)
)
if mibBuilder.loadTexts:
    pm251dAlmaccessioSdhAlarmTable.setStatus("current")
_Pm251dAlmaccessioSdhAlarmEntry_Object = MibTableRow
pm251dAlmaccessioSdhAlarmEntry = _Pm251dAlmaccessioSdhAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 3, 104, 1)
)
pm251dAlmaccessioSdhAlarmEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dAlmaccessioSdhAlarmIndex"),
)
if mibBuilder.loadTexts:
    pm251dAlmaccessioSdhAlarmEntry.setStatus("current")


class _Pm251dAlmaccessioSdhAlarmIndex_Type(Integer32):
    """Custom type pm251dAlmaccessioSdhAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dAlmaccessioSdhAlarmIndex_Type.__name__ = "Integer32"
_Pm251dAlmaccessioSdhAlarmIndex_Object = MibTableColumn
pm251dAlmaccessioSdhAlarmIndex = _Pm251dAlmaccessioSdhAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 3, 104, 1, 1),
    _Pm251dAlmaccessioSdhAlarmIndex_Type()
)
pm251dAlmaccessioSdhAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmaccessioSdhAlarmIndex.setStatus("current")
_Pm251dAlmLosTrscPortn_Type = EkiOnOff
_Pm251dAlmLosTrscPortn_Object = MibTableColumn
pm251dAlmLosTrscPortn = _Pm251dAlmLosTrscPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 3, 104, 1, 2),
    _Pm251dAlmLosTrscPortn_Type()
)
pm251dAlmLosTrscPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmLosTrscPortn.setStatus("current")
_Pm251dAlmFifoErrPortn_Type = EkiOnOff
_Pm251dAlmFifoErrPortn_Object = MibTableColumn
pm251dAlmFifoErrPortn = _Pm251dAlmFifoErrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 3, 104, 1, 3),
    _Pm251dAlmFifoErrPortn_Type()
)
pm251dAlmFifoErrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmFifoErrPortn.setStatus("current")
_Pm251dAlmRxLossOfLockPortn_Type = EkiOnOff
_Pm251dAlmRxLossOfLockPortn_Object = MibTableColumn
pm251dAlmRxLossOfLockPortn = _Pm251dAlmRxLossOfLockPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 3, 104, 1, 4),
    _Pm251dAlmRxLossOfLockPortn_Type()
)
pm251dAlmRxLossOfLockPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmRxLossOfLockPortn.setStatus("current")
_Pm251dAlmTxLossOfLockPortn_Type = EkiOnOff
_Pm251dAlmTxLossOfLockPortn_Object = MibTableColumn
pm251dAlmTxLossOfLockPortn = _Pm251dAlmTxLossOfLockPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 3, 104, 1, 5),
    _Pm251dAlmTxLossOfLockPortn_Type()
)
pm251dAlmTxLossOfLockPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmTxLossOfLockPortn.setStatus("current")
_Pm251dAlmClientAisDetPortn_Type = EkiOnOff
_Pm251dAlmClientAisDetPortn_Object = MibTableColumn
pm251dAlmClientAisDetPortn = _Pm251dAlmClientAisDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 3, 104, 1, 6),
    _Pm251dAlmClientAisDetPortn_Type()
)
pm251dAlmClientAisDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientAisDetPortn.setStatus("current")
_Pm251dAlmClientRdiDetPortn_Type = EkiOnOff
_Pm251dAlmClientRdiDetPortn_Object = MibTableColumn
pm251dAlmClientRdiDetPortn = _Pm251dAlmClientRdiDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 3, 104, 1, 7),
    _Pm251dAlmClientRdiDetPortn_Type()
)
pm251dAlmClientRdiDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientRdiDetPortn.setStatus("current")
_Pm251dAlmClientOofPortn_Type = EkiOnOff
_Pm251dAlmClientOofPortn_Object = MibTableColumn
pm251dAlmClientOofPortn = _Pm251dAlmClientOofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 2, 3, 104, 1, 8),
    _Pm251dAlmClientOofPortn_Type()
)
pm251dAlmClientOofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmClientOofPortn.setStatus("current")
_Pm251dAlmLine_ObjectIdentity = ObjectIdentity
pm251dAlmLine = _Pm251dAlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3)
)
_Pm251dAlmLineNurg_ObjectIdentity = ObjectIdentity
pm251dAlmLineNurg = _Pm251dAlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 1)
)
_Pm251dAlmlineDownS1Table_Object = MibTable
pm251dAlmlineDownS1Table = _Pm251dAlmlineDownS1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 1, 130)
)
if mibBuilder.loadTexts:
    pm251dAlmlineDownS1Table.setStatus("current")
_Pm251dAlmlineDownS1Entry_Object = MibTableRow
pm251dAlmlineDownS1Entry = _Pm251dAlmlineDownS1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 1, 130, 1)
)
pm251dAlmlineDownS1Entry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dAlmlineDownS1Index"),
)
if mibBuilder.loadTexts:
    pm251dAlmlineDownS1Entry.setStatus("current")


class _Pm251dAlmlineDownS1Index_Type(Integer32):
    """Custom type pm251dAlmlineDownS1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dAlmlineDownS1Index_Type.__name__ = "Integer32"
_Pm251dAlmlineDownS1Index_Object = MibTableColumn
pm251dAlmlineDownS1Index = _Pm251dAlmlineDownS1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 1, 130, 1, 1),
    _Pm251dAlmlineDownS1Index_Type()
)
pm251dAlmlineDownS1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmlineDownS1Index.setStatus("current")


class _Pm251dAlmlineDownS1Portn_Type(Integer32):
    """Custom type pm251dAlmlineDownS1Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Pm251dAlmlineDownS1Portn_Type.__name__ = "Integer32"
_Pm251dAlmlineDownS1Portn_Object = MibTableColumn
pm251dAlmlineDownS1Portn = _Pm251dAlmlineDownS1Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 1, 130, 1, 2),
    _Pm251dAlmlineDownS1Portn_Type()
)
pm251dAlmlineDownS1Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmlineDownS1Portn.setStatus("current")
_Pm251dAlmlineDownK1Table_Object = MibTable
pm251dAlmlineDownK1Table = _Pm251dAlmlineDownK1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 1, 131)
)
if mibBuilder.loadTexts:
    pm251dAlmlineDownK1Table.setStatus("current")
_Pm251dAlmlineDownK1Entry_Object = MibTableRow
pm251dAlmlineDownK1Entry = _Pm251dAlmlineDownK1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 1, 131, 1)
)
pm251dAlmlineDownK1Entry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dAlmlineDownK1Index"),
)
if mibBuilder.loadTexts:
    pm251dAlmlineDownK1Entry.setStatus("current")


class _Pm251dAlmlineDownK1Index_Type(Integer32):
    """Custom type pm251dAlmlineDownK1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dAlmlineDownK1Index_Type.__name__ = "Integer32"
_Pm251dAlmlineDownK1Index_Object = MibTableColumn
pm251dAlmlineDownK1Index = _Pm251dAlmlineDownK1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 1, 131, 1, 1),
    _Pm251dAlmlineDownK1Index_Type()
)
pm251dAlmlineDownK1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmlineDownK1Index.setStatus("current")


class _Pm251dAlmlineDownK1Portn_Type(Integer32):
    """Custom type pm251dAlmlineDownK1Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Pm251dAlmlineDownK1Portn_Type.__name__ = "Integer32"
_Pm251dAlmlineDownK1Portn_Object = MibTableColumn
pm251dAlmlineDownK1Portn = _Pm251dAlmlineDownK1Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 1, 131, 1, 2),
    _Pm251dAlmlineDownK1Portn_Type()
)
pm251dAlmlineDownK1Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmlineDownK1Portn.setStatus("current")
_Pm251dAlmlineDownK2Table_Object = MibTable
pm251dAlmlineDownK2Table = _Pm251dAlmlineDownK2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 1, 132)
)
if mibBuilder.loadTexts:
    pm251dAlmlineDownK2Table.setStatus("current")
_Pm251dAlmlineDownK2Entry_Object = MibTableRow
pm251dAlmlineDownK2Entry = _Pm251dAlmlineDownK2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 1, 132, 1)
)
pm251dAlmlineDownK2Entry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dAlmlineDownK2Index"),
)
if mibBuilder.loadTexts:
    pm251dAlmlineDownK2Entry.setStatus("current")


class _Pm251dAlmlineDownK2Index_Type(Integer32):
    """Custom type pm251dAlmlineDownK2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dAlmlineDownK2Index_Type.__name__ = "Integer32"
_Pm251dAlmlineDownK2Index_Object = MibTableColumn
pm251dAlmlineDownK2Index = _Pm251dAlmlineDownK2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 1, 132, 1, 1),
    _Pm251dAlmlineDownK2Index_Type()
)
pm251dAlmlineDownK2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmlineDownK2Index.setStatus("current")


class _Pm251dAlmlineDownK2Portn_Type(Integer32):
    """Custom type pm251dAlmlineDownK2Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Pm251dAlmlineDownK2Portn_Type.__name__ = "Integer32"
_Pm251dAlmlineDownK2Portn_Object = MibTableColumn
pm251dAlmlineDownK2Portn = _Pm251dAlmlineDownK2Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 1, 132, 1, 2),
    _Pm251dAlmlineDownK2Portn_Type()
)
pm251dAlmlineDownK2Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmlineDownK2Portn.setStatus("current")
_Pm251dAlmlineSfpWarnDdmTable_Object = MibTable
pm251dAlmlineSfpWarnDdmTable = _Pm251dAlmlineSfpWarnDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 1, 164)
)
if mibBuilder.loadTexts:
    pm251dAlmlineSfpWarnDdmTable.setStatus("current")
_Pm251dAlmlineSfpWarnDdmEntry_Object = MibTableRow
pm251dAlmlineSfpWarnDdmEntry = _Pm251dAlmlineSfpWarnDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 1, 164, 1)
)
pm251dAlmlineSfpWarnDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dAlmlineSfpWarnDdmIndex"),
)
if mibBuilder.loadTexts:
    pm251dAlmlineSfpWarnDdmEntry.setStatus("current")


class _Pm251dAlmlineSfpWarnDdmIndex_Type(Integer32):
    """Custom type pm251dAlmlineSfpWarnDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dAlmlineSfpWarnDdmIndex_Type.__name__ = "Integer32"
_Pm251dAlmlineSfpWarnDdmIndex_Object = MibTableColumn
pm251dAlmlineSfpWarnDdmIndex = _Pm251dAlmlineSfpWarnDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 1, 164, 1, 1),
    _Pm251dAlmlineSfpWarnDdmIndex_Type()
)
pm251dAlmlineSfpWarnDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmlineSfpWarnDdmIndex.setStatus("current")
_Pm251dAlmLineTxPwLowWngPortn_Type = EkiOnOff
_Pm251dAlmLineTxPwLowWngPortn_Object = MibTableColumn
pm251dAlmLineTxPwLowWngPortn = _Pm251dAlmLineTxPwLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 1, 164, 1, 2),
    _Pm251dAlmLineTxPwLowWngPortn_Type()
)
pm251dAlmLineTxPwLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmLineTxPwLowWngPortn.setStatus("current")
_Pm251dAlmLineTxPwrHighWngPortn_Type = EkiOnOff
_Pm251dAlmLineTxPwrHighWngPortn_Object = MibTableColumn
pm251dAlmLineTxPwrHighWngPortn = _Pm251dAlmLineTxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 1, 164, 1, 3),
    _Pm251dAlmLineTxPwrHighWngPortn_Type()
)
pm251dAlmLineTxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmLineTxPwrHighWngPortn.setStatus("current")
_Pm251dAlmLineTxBiasLowWngPortn_Type = EkiOnOff
_Pm251dAlmLineTxBiasLowWngPortn_Object = MibTableColumn
pm251dAlmLineTxBiasLowWngPortn = _Pm251dAlmLineTxBiasLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 1, 164, 1, 4),
    _Pm251dAlmLineTxBiasLowWngPortn_Type()
)
pm251dAlmLineTxBiasLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmLineTxBiasLowWngPortn.setStatus("current")
_Pm251dAlmLineTxBiasHighWngPortn_Type = EkiOnOff
_Pm251dAlmLineTxBiasHighWngPortn_Object = MibTableColumn
pm251dAlmLineTxBiasHighWngPortn = _Pm251dAlmLineTxBiasHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 1, 164, 1, 5),
    _Pm251dAlmLineTxBiasHighWngPortn_Type()
)
pm251dAlmLineTxBiasHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmLineTxBiasHighWngPortn.setStatus("current")
_Pm251dAlmLineVccLowWngPortn_Type = EkiOnOff
_Pm251dAlmLineVccLowWngPortn_Object = MibTableColumn
pm251dAlmLineVccLowWngPortn = _Pm251dAlmLineVccLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 1, 164, 1, 6),
    _Pm251dAlmLineVccLowWngPortn_Type()
)
pm251dAlmLineVccLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmLineVccLowWngPortn.setStatus("current")
_Pm251dAlmLineVccHighWngPortn_Type = EkiOnOff
_Pm251dAlmLineVccHighWngPortn_Object = MibTableColumn
pm251dAlmLineVccHighWngPortn = _Pm251dAlmLineVccHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 1, 164, 1, 7),
    _Pm251dAlmLineVccHighWngPortn_Type()
)
pm251dAlmLineVccHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmLineVccHighWngPortn.setStatus("current")
_Pm251dAlmLineTempLowWngPortn_Type = EkiOnOff
_Pm251dAlmLineTempLowWngPortn_Object = MibTableColumn
pm251dAlmLineTempLowWngPortn = _Pm251dAlmLineTempLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 1, 164, 1, 8),
    _Pm251dAlmLineTempLowWngPortn_Type()
)
pm251dAlmLineTempLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmLineTempLowWngPortn.setStatus("current")
_Pm251dAlmLineTempHighWngPortn_Type = EkiOnOff
_Pm251dAlmLineTempHighWngPortn_Object = MibTableColumn
pm251dAlmLineTempHighWngPortn = _Pm251dAlmLineTempHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 1, 164, 1, 9),
    _Pm251dAlmLineTempHighWngPortn_Type()
)
pm251dAlmLineTempHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmLineTempHighWngPortn.setStatus("current")
_Pm251dAlmLineRxPwrLowWngPortn_Type = EkiOnOff
_Pm251dAlmLineRxPwrLowWngPortn_Object = MibTableColumn
pm251dAlmLineRxPwrLowWngPortn = _Pm251dAlmLineRxPwrLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 1, 164, 1, 16),
    _Pm251dAlmLineRxPwrLowWngPortn_Type()
)
pm251dAlmLineRxPwrLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmLineRxPwrLowWngPortn.setStatus("current")
_Pm251dAlmLineRxPwrHighWngPortn_Type = EkiOnOff
_Pm251dAlmLineRxPwrHighWngPortn_Object = MibTableColumn
pm251dAlmLineRxPwrHighWngPortn = _Pm251dAlmLineRxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 1, 164, 1, 17),
    _Pm251dAlmLineRxPwrHighWngPortn_Type()
)
pm251dAlmLineRxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmLineRxPwrHighWngPortn.setStatus("current")
_Pm251dAlmLineUrg_ObjectIdentity = ObjectIdentity
pm251dAlmLineUrg = _Pm251dAlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 2)
)
_Pm251dAlmlineSfpAlaDdmTable_Object = MibTable
pm251dAlmlineSfpAlaDdmTable = _Pm251dAlmlineSfpAlaDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 2, 162)
)
if mibBuilder.loadTexts:
    pm251dAlmlineSfpAlaDdmTable.setStatus("current")
_Pm251dAlmlineSfpAlaDdmEntry_Object = MibTableRow
pm251dAlmlineSfpAlaDdmEntry = _Pm251dAlmlineSfpAlaDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 2, 162, 1)
)
pm251dAlmlineSfpAlaDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dAlmlineSfpAlaDdmIndex"),
)
if mibBuilder.loadTexts:
    pm251dAlmlineSfpAlaDdmEntry.setStatus("current")


class _Pm251dAlmlineSfpAlaDdmIndex_Type(Integer32):
    """Custom type pm251dAlmlineSfpAlaDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dAlmlineSfpAlaDdmIndex_Type.__name__ = "Integer32"
_Pm251dAlmlineSfpAlaDdmIndex_Object = MibTableColumn
pm251dAlmlineSfpAlaDdmIndex = _Pm251dAlmlineSfpAlaDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 2, 162, 1, 1),
    _Pm251dAlmlineSfpAlaDdmIndex_Type()
)
pm251dAlmlineSfpAlaDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmlineSfpAlaDdmIndex.setStatus("current")
_Pm251dAlmLineTxPwrLowAlaPortn_Type = EkiOnOff
_Pm251dAlmLineTxPwrLowAlaPortn_Object = MibTableColumn
pm251dAlmLineTxPwrLowAlaPortn = _Pm251dAlmLineTxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 2, 162, 1, 2),
    _Pm251dAlmLineTxPwrLowAlaPortn_Type()
)
pm251dAlmLineTxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmLineTxPwrLowAlaPortn.setStatus("current")
_Pm251dAlmLineTxPwrHighAlaPortn_Type = EkiOnOff
_Pm251dAlmLineTxPwrHighAlaPortn_Object = MibTableColumn
pm251dAlmLineTxPwrHighAlaPortn = _Pm251dAlmLineTxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 2, 162, 1, 3),
    _Pm251dAlmLineTxPwrHighAlaPortn_Type()
)
pm251dAlmLineTxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmLineTxPwrHighAlaPortn.setStatus("current")
_Pm251dAlmLineTxBiasLowAlaPortn_Type = EkiOnOff
_Pm251dAlmLineTxBiasLowAlaPortn_Object = MibTableColumn
pm251dAlmLineTxBiasLowAlaPortn = _Pm251dAlmLineTxBiasLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 2, 162, 1, 4),
    _Pm251dAlmLineTxBiasLowAlaPortn_Type()
)
pm251dAlmLineTxBiasLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmLineTxBiasLowAlaPortn.setStatus("current")
_Pm251dAlmLineTxBiasHighAlaPortn_Type = EkiOnOff
_Pm251dAlmLineTxBiasHighAlaPortn_Object = MibTableColumn
pm251dAlmLineTxBiasHighAlaPortn = _Pm251dAlmLineTxBiasHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 2, 162, 1, 5),
    _Pm251dAlmLineTxBiasHighAlaPortn_Type()
)
pm251dAlmLineTxBiasHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmLineTxBiasHighAlaPortn.setStatus("current")
_Pm251dAlmLineVccLowAlaPortn_Type = EkiOnOff
_Pm251dAlmLineVccLowAlaPortn_Object = MibTableColumn
pm251dAlmLineVccLowAlaPortn = _Pm251dAlmLineVccLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 2, 162, 1, 6),
    _Pm251dAlmLineVccLowAlaPortn_Type()
)
pm251dAlmLineVccLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmLineVccLowAlaPortn.setStatus("current")
_Pm251dAlmLineVccHighAlaPortn_Type = EkiOnOff
_Pm251dAlmLineVccHighAlaPortn_Object = MibTableColumn
pm251dAlmLineVccHighAlaPortn = _Pm251dAlmLineVccHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 2, 162, 1, 7),
    _Pm251dAlmLineVccHighAlaPortn_Type()
)
pm251dAlmLineVccHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmLineVccHighAlaPortn.setStatus("current")
_Pm251dAlmLineTempLowAlaPortn_Type = EkiOnOff
_Pm251dAlmLineTempLowAlaPortn_Object = MibTableColumn
pm251dAlmLineTempLowAlaPortn = _Pm251dAlmLineTempLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 2, 162, 1, 8),
    _Pm251dAlmLineTempLowAlaPortn_Type()
)
pm251dAlmLineTempLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmLineTempLowAlaPortn.setStatus("current")
_Pm251dAlmLineTempHighAlaPortn_Type = EkiOnOff
_Pm251dAlmLineTempHighAlaPortn_Object = MibTableColumn
pm251dAlmLineTempHighAlaPortn = _Pm251dAlmLineTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 2, 162, 1, 9),
    _Pm251dAlmLineTempHighAlaPortn_Type()
)
pm251dAlmLineTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmLineTempHighAlaPortn.setStatus("current")
_Pm251dAlmLineRxPwrLowAlaPortn_Type = EkiOnOff
_Pm251dAlmLineRxPwrLowAlaPortn_Object = MibTableColumn
pm251dAlmLineRxPwrLowAlaPortn = _Pm251dAlmLineRxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 2, 162, 1, 16),
    _Pm251dAlmLineRxPwrLowAlaPortn_Type()
)
pm251dAlmLineRxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmLineRxPwrLowAlaPortn.setStatus("current")
_Pm251dAlmLineRxPwrHighAlaPortn_Type = EkiOnOff
_Pm251dAlmLineRxPwrHighAlaPortn_Object = MibTableColumn
pm251dAlmLineRxPwrHighAlaPortn = _Pm251dAlmLineRxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 2, 162, 1, 17),
    _Pm251dAlmLineRxPwrHighAlaPortn_Type()
)
pm251dAlmLineRxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmLineRxPwrHighAlaPortn.setStatus("current")
_Pm251dAlmLineCrit_ObjectIdentity = ObjectIdentity
pm251dAlmLineCrit = _Pm251dAlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 3)
)
_Pm251dAlmsynthAlmLineTable_Object = MibTable
pm251dAlmsynthAlmLineTable = _Pm251dAlmsynthAlmLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 3, 4)
)
if mibBuilder.loadTexts:
    pm251dAlmsynthAlmLineTable.setStatus("current")
_Pm251dAlmsynthAlmLineEntry_Object = MibTableRow
pm251dAlmsynthAlmLineEntry = _Pm251dAlmsynthAlmLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 3, 4, 1)
)
pm251dAlmsynthAlmLineEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dAlmsynthAlmLineIndex"),
)
if mibBuilder.loadTexts:
    pm251dAlmsynthAlmLineEntry.setStatus("current")


class _Pm251dAlmsynthAlmLineIndex_Type(Integer32):
    """Custom type pm251dAlmsynthAlmLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dAlmsynthAlmLineIndex_Type.__name__ = "Integer32"
_Pm251dAlmsynthAlmLineIndex_Object = MibTableColumn
pm251dAlmsynthAlmLineIndex = _Pm251dAlmsynthAlmLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 3, 4, 1, 1),
    _Pm251dAlmsynthAlmLineIndex_Type()
)
pm251dAlmsynthAlmLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmsynthAlmLineIndex.setStatus("current")
_Pm251dAlmLineSfpAbsentPortn_Type = EkiOnOff
_Pm251dAlmLineSfpAbsentPortn_Object = MibTableColumn
pm251dAlmLineSfpAbsentPortn = _Pm251dAlmLineSfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 3, 4, 1, 2),
    _Pm251dAlmLineSfpAbsentPortn_Type()
)
pm251dAlmLineSfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmLineSfpAbsentPortn.setStatus("current")
_Pm251dAlmLineDdmAbsentPortn_Type = EkiOnOff
_Pm251dAlmLineDdmAbsentPortn_Object = MibTableColumn
pm251dAlmLineDdmAbsentPortn = _Pm251dAlmLineDdmAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 3, 4, 1, 3),
    _Pm251dAlmLineDdmAbsentPortn_Type()
)
pm251dAlmLineDdmAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmLineDdmAbsentPortn.setStatus("current")
_Pm251dAlmLineHwFailPortn_Type = EkiOnOff
_Pm251dAlmLineHwFailPortn_Object = MibTableColumn
pm251dAlmLineHwFailPortn = _Pm251dAlmLineHwFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 3, 4, 1, 5),
    _Pm251dAlmLineHwFailPortn_Type()
)
pm251dAlmLineHwFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmLineHwFailPortn.setStatus("current")
_Pm251dAlmLineLsdPortn_Type = EkiOnOff
_Pm251dAlmLineLsdPortn_Object = MibTableColumn
pm251dAlmLineLsdPortn = _Pm251dAlmLineLsdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 3, 4, 1, 6),
    _Pm251dAlmLineLsdPortn_Type()
)
pm251dAlmLineLsdPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmLineLsdPortn.setStatus("current")
_Pm251dAlmLineLocalOosPortn_Type = EkiOnOff
_Pm251dAlmLineLocalOosPortn_Object = MibTableColumn
pm251dAlmLineLocalOosPortn = _Pm251dAlmLineLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 3, 4, 1, 7),
    _Pm251dAlmLineLocalOosPortn_Type()
)
pm251dAlmLineLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmLineLocalOosPortn.setStatus("current")
_Pm251dAlmLineUpRdiInsPortn_Type = EkiOnOff
_Pm251dAlmLineUpRdiInsPortn_Object = MibTableColumn
pm251dAlmLineUpRdiInsPortn = _Pm251dAlmLineUpRdiInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 3, 4, 1, 9),
    _Pm251dAlmLineUpRdiInsPortn_Type()
)
pm251dAlmLineUpRdiInsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmLineUpRdiInsPortn.setStatus("current")
_Pm251dAlmLineDdmWarningPortn_Type = EkiOnOff
_Pm251dAlmLineDdmWarningPortn_Object = MibTableColumn
pm251dAlmLineDdmWarningPortn = _Pm251dAlmLineDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 3, 4, 1, 10),
    _Pm251dAlmLineDdmWarningPortn_Type()
)
pm251dAlmLineDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmLineDdmWarningPortn.setStatus("current")
_Pm251dAlmLineDdmAlmPortn_Type = EkiOnOff
_Pm251dAlmLineDdmAlmPortn_Object = MibTableColumn
pm251dAlmLineDdmAlmPortn = _Pm251dAlmLineDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 3, 4, 1, 11),
    _Pm251dAlmLineDdmAlmPortn_Type()
)
pm251dAlmLineDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmLineDdmAlmPortn.setStatus("current")
_Pm251dAlmLineFailPortn_Type = EkiOnOff
_Pm251dAlmLineFailPortn_Object = MibTableColumn
pm251dAlmLineFailPortn = _Pm251dAlmLineFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 3, 4, 1, 13),
    _Pm251dAlmLineFailPortn_Type()
)
pm251dAlmLineFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmLineFailPortn.setStatus("current")
_Pm251dAlmlineDfrmAlmTable_Object = MibTable
pm251dAlmlineDfrmAlmTable = _Pm251dAlmlineDfrmAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 3, 128)
)
if mibBuilder.loadTexts:
    pm251dAlmlineDfrmAlmTable.setStatus("current")
_Pm251dAlmlineDfrmAlmEntry_Object = MibTableRow
pm251dAlmlineDfrmAlmEntry = _Pm251dAlmlineDfrmAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 3, 128, 1)
)
pm251dAlmlineDfrmAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dAlmlineDfrmAlmIndex"),
)
if mibBuilder.loadTexts:
    pm251dAlmlineDfrmAlmEntry.setStatus("current")


class _Pm251dAlmlineDfrmAlmIndex_Type(Integer32):
    """Custom type pm251dAlmlineDfrmAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dAlmlineDfrmAlmIndex_Type.__name__ = "Integer32"
_Pm251dAlmlineDfrmAlmIndex_Object = MibTableColumn
pm251dAlmlineDfrmAlmIndex = _Pm251dAlmlineDfrmAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 3, 128, 1, 1),
    _Pm251dAlmlineDfrmAlmIndex_Type()
)
pm251dAlmlineDfrmAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmlineDfrmAlmIndex.setStatus("current")
_Pm251dAlmLineDwAisDetPortn_Type = EkiOnOff
_Pm251dAlmLineDwAisDetPortn_Object = MibTableColumn
pm251dAlmLineDwAisDetPortn = _Pm251dAlmLineDwAisDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 3, 128, 1, 2),
    _Pm251dAlmLineDwAisDetPortn_Type()
)
pm251dAlmLineDwAisDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmLineDwAisDetPortn.setStatus("current")
_Pm251dAlmLineDwRdiDetPortn_Type = EkiOnOff
_Pm251dAlmLineDwRdiDetPortn_Object = MibTableColumn
pm251dAlmLineDwRdiDetPortn = _Pm251dAlmLineDwRdiDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 3, 128, 1, 3),
    _Pm251dAlmLineDwRdiDetPortn_Type()
)
pm251dAlmLineDwRdiDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmLineDwRdiDetPortn.setStatus("current")
_Pm251dAlmLineDwOofPortn_Type = EkiOnOff
_Pm251dAlmLineDwOofPortn_Object = MibTableColumn
pm251dAlmLineDwOofPortn = _Pm251dAlmLineDwOofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 3, 128, 1, 4),
    _Pm251dAlmLineDwOofPortn_Type()
)
pm251dAlmLineDwOofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmLineDwOofPortn.setStatus("current")
_Pm251dAlmLineDwLofPortn_Type = EkiOnOff
_Pm251dAlmLineDwLofPortn_Object = MibTableColumn
pm251dAlmLineDwLofPortn = _Pm251dAlmLineDwLofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 3, 128, 1, 5),
    _Pm251dAlmLineDwLofPortn_Type()
)
pm251dAlmLineDwLofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmLineDwLofPortn.setStatus("current")
_Pm251dAlmlineIoAlmTable_Object = MibTable
pm251dAlmlineIoAlmTable = _Pm251dAlmlineIoAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 3, 160)
)
if mibBuilder.loadTexts:
    pm251dAlmlineIoAlmTable.setStatus("current")
_Pm251dAlmlineIoAlmEntry_Object = MibTableRow
pm251dAlmlineIoAlmEntry = _Pm251dAlmlineIoAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 3, 160, 1)
)
pm251dAlmlineIoAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dAlmlineIoAlmIndex"),
)
if mibBuilder.loadTexts:
    pm251dAlmlineIoAlmEntry.setStatus("current")


class _Pm251dAlmlineIoAlmIndex_Type(Integer32):
    """Custom type pm251dAlmlineIoAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dAlmlineIoAlmIndex_Type.__name__ = "Integer32"
_Pm251dAlmlineIoAlmIndex_Object = MibTableColumn
pm251dAlmlineIoAlmIndex = _Pm251dAlmlineIoAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 3, 160, 1, 1),
    _Pm251dAlmlineIoAlmIndex_Type()
)
pm251dAlmlineIoAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmlineIoAlmIndex.setStatus("current")
_Pm251dAlmLineUpLasFailPortn_Type = EkiOnOff
_Pm251dAlmLineUpLasFailPortn_Object = MibTableColumn
pm251dAlmLineUpLasFailPortn = _Pm251dAlmLineUpLasFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 3, 160, 1, 2),
    _Pm251dAlmLineUpLasFailPortn_Type()
)
pm251dAlmLineUpLasFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmLineUpLasFailPortn.setStatus("current")
_Pm251dAlmLineDwLosPortn_Type = EkiOnOff
_Pm251dAlmLineDwLosPortn_Object = MibTableColumn
pm251dAlmLineDwLosPortn = _Pm251dAlmLineDwLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 2, 3, 3, 160, 1, 5),
    _Pm251dAlmLineDwLosPortn_Type()
)
pm251dAlmLineDwLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dAlmLineDwLosPortn.setStatus("current")
_Pm251dmeasures_ObjectIdentity = ObjectIdentity
pm251dmeasures = _Pm251dmeasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3)
)
_Pm251dMesrOther_ObjectIdentity = ObjectIdentity
pm251dMesrOther = _Pm251dMesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 1)
)
_Pm251dMesrPort_ObjectIdentity = ObjectIdentity
pm251dMesrPort = _Pm251dMesrPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 2)
)
_Pm251dMesrclientTempMeasTable_Object = MibTable
pm251dMesrclientTempMeasTable = _Pm251dMesrclientTempMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 2, 16)
)
if mibBuilder.loadTexts:
    pm251dMesrclientTempMeasTable.setStatus("current")
_Pm251dMesrclientTempMeasEntry_Object = MibTableRow
pm251dMesrclientTempMeasEntry = _Pm251dMesrclientTempMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 2, 16, 1)
)
pm251dMesrclientTempMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dMesrclientTempMeasIndex"),
)
if mibBuilder.loadTexts:
    pm251dMesrclientTempMeasEntry.setStatus("current")


class _Pm251dMesrclientTempMeasIndex_Type(Integer32):
    """Custom type pm251dMesrclientTempMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dMesrclientTempMeasIndex_Type.__name__ = "Integer32"
_Pm251dMesrclientTempMeasIndex_Object = MibTableColumn
pm251dMesrclientTempMeasIndex = _Pm251dMesrclientTempMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 2, 16, 1, 1),
    _Pm251dMesrclientTempMeasIndex_Type()
)
pm251dMesrclientTempMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dMesrclientTempMeasIndex.setStatus("current")


class _Pm251dMesrclientTempMeasPortn_Type(Integer32):
    """Custom type pm251dMesrclientTempMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm251dMesrclientTempMeasPortn_Type.__name__ = "Integer32"
_Pm251dMesrclientTempMeasPortn_Object = MibTableColumn
pm251dMesrclientTempMeasPortn = _Pm251dMesrclientTempMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 2, 16, 1, 2),
    _Pm251dMesrclientTempMeasPortn_Type()
)
pm251dMesrclientTempMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dMesrclientTempMeasPortn.setStatus("current")
_Pm251dMesrclientVoltMeasTable_Object = MibTable
pm251dMesrclientVoltMeasTable = _Pm251dMesrclientVoltMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 2, 24)
)
if mibBuilder.loadTexts:
    pm251dMesrclientVoltMeasTable.setStatus("current")
_Pm251dMesrclientVoltMeasEntry_Object = MibTableRow
pm251dMesrclientVoltMeasEntry = _Pm251dMesrclientVoltMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 2, 24, 1)
)
pm251dMesrclientVoltMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dMesrclientVoltMeasIndex"),
)
if mibBuilder.loadTexts:
    pm251dMesrclientVoltMeasEntry.setStatus("current")


class _Pm251dMesrclientVoltMeasIndex_Type(Integer32):
    """Custom type pm251dMesrclientVoltMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dMesrclientVoltMeasIndex_Type.__name__ = "Integer32"
_Pm251dMesrclientVoltMeasIndex_Object = MibTableColumn
pm251dMesrclientVoltMeasIndex = _Pm251dMesrclientVoltMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 2, 24, 1, 1),
    _Pm251dMesrclientVoltMeasIndex_Type()
)
pm251dMesrclientVoltMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dMesrclientVoltMeasIndex.setStatus("current")


class _Pm251dMesrclientVoltMeasPortn_Type(Integer32):
    """Custom type pm251dMesrclientVoltMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm251dMesrclientVoltMeasPortn_Type.__name__ = "Integer32"
_Pm251dMesrclientVoltMeasPortn_Object = MibTableColumn
pm251dMesrclientVoltMeasPortn = _Pm251dMesrclientVoltMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 2, 24, 1, 2),
    _Pm251dMesrclientVoltMeasPortn_Type()
)
pm251dMesrclientVoltMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dMesrclientVoltMeasPortn.setStatus("current")
_Pm251dMesrclientBiasMeasTable_Object = MibTable
pm251dMesrclientBiasMeasTable = _Pm251dMesrclientBiasMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 2, 32)
)
if mibBuilder.loadTexts:
    pm251dMesrclientBiasMeasTable.setStatus("current")
_Pm251dMesrclientBiasMeasEntry_Object = MibTableRow
pm251dMesrclientBiasMeasEntry = _Pm251dMesrclientBiasMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 2, 32, 1)
)
pm251dMesrclientBiasMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dMesrclientBiasMeasIndex"),
)
if mibBuilder.loadTexts:
    pm251dMesrclientBiasMeasEntry.setStatus("current")


class _Pm251dMesrclientBiasMeasIndex_Type(Integer32):
    """Custom type pm251dMesrclientBiasMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dMesrclientBiasMeasIndex_Type.__name__ = "Integer32"
_Pm251dMesrclientBiasMeasIndex_Object = MibTableColumn
pm251dMesrclientBiasMeasIndex = _Pm251dMesrclientBiasMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 2, 32, 1, 1),
    _Pm251dMesrclientBiasMeasIndex_Type()
)
pm251dMesrclientBiasMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dMesrclientBiasMeasIndex.setStatus("current")


class _Pm251dMesrclientBiasMeasPortn_Type(Integer32):
    """Custom type pm251dMesrclientBiasMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm251dMesrclientBiasMeasPortn_Type.__name__ = "Integer32"
_Pm251dMesrclientBiasMeasPortn_Object = MibTableColumn
pm251dMesrclientBiasMeasPortn = _Pm251dMesrclientBiasMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 2, 32, 1, 2),
    _Pm251dMesrclientBiasMeasPortn_Type()
)
pm251dMesrclientBiasMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dMesrclientBiasMeasPortn.setStatus("current")
_Pm251dMesrclientTxpwrMeasTable_Object = MibTable
pm251dMesrclientTxpwrMeasTable = _Pm251dMesrclientTxpwrMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 2, 40)
)
if mibBuilder.loadTexts:
    pm251dMesrclientTxpwrMeasTable.setStatus("current")
_Pm251dMesrclientTxpwrMeasEntry_Object = MibTableRow
pm251dMesrclientTxpwrMeasEntry = _Pm251dMesrclientTxpwrMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 2, 40, 1)
)
pm251dMesrclientTxpwrMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dMesrclientTxpwrMeasIndex"),
)
if mibBuilder.loadTexts:
    pm251dMesrclientTxpwrMeasEntry.setStatus("current")


class _Pm251dMesrclientTxpwrMeasIndex_Type(Integer32):
    """Custom type pm251dMesrclientTxpwrMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dMesrclientTxpwrMeasIndex_Type.__name__ = "Integer32"
_Pm251dMesrclientTxpwrMeasIndex_Object = MibTableColumn
pm251dMesrclientTxpwrMeasIndex = _Pm251dMesrclientTxpwrMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 2, 40, 1, 1),
    _Pm251dMesrclientTxpwrMeasIndex_Type()
)
pm251dMesrclientTxpwrMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dMesrclientTxpwrMeasIndex.setStatus("current")


class _Pm251dMesrclientTxpwrMeasPortn_Type(Integer32):
    """Custom type pm251dMesrclientTxpwrMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm251dMesrclientTxpwrMeasPortn_Type.__name__ = "Integer32"
_Pm251dMesrclientTxpwrMeasPortn_Object = MibTableColumn
pm251dMesrclientTxpwrMeasPortn = _Pm251dMesrclientTxpwrMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 2, 40, 1, 2),
    _Pm251dMesrclientTxpwrMeasPortn_Type()
)
pm251dMesrclientTxpwrMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dMesrclientTxpwrMeasPortn.setStatus("current")
_Pm251dMesrclientRxpwrMeasTable_Object = MibTable
pm251dMesrclientRxpwrMeasTable = _Pm251dMesrclientRxpwrMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 2, 48)
)
if mibBuilder.loadTexts:
    pm251dMesrclientRxpwrMeasTable.setStatus("current")
_Pm251dMesrclientRxpwrMeasEntry_Object = MibTableRow
pm251dMesrclientRxpwrMeasEntry = _Pm251dMesrclientRxpwrMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 2, 48, 1)
)
pm251dMesrclientRxpwrMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dMesrclientRxpwrMeasIndex"),
)
if mibBuilder.loadTexts:
    pm251dMesrclientRxpwrMeasEntry.setStatus("current")


class _Pm251dMesrclientRxpwrMeasIndex_Type(Integer32):
    """Custom type pm251dMesrclientRxpwrMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dMesrclientRxpwrMeasIndex_Type.__name__ = "Integer32"
_Pm251dMesrclientRxpwrMeasIndex_Object = MibTableColumn
pm251dMesrclientRxpwrMeasIndex = _Pm251dMesrclientRxpwrMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 2, 48, 1, 1),
    _Pm251dMesrclientRxpwrMeasIndex_Type()
)
pm251dMesrclientRxpwrMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dMesrclientRxpwrMeasIndex.setStatus("current")


class _Pm251dMesrclientRxpwrMeasPortn_Type(Integer32):
    """Custom type pm251dMesrclientRxpwrMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm251dMesrclientRxpwrMeasPortn_Type.__name__ = "Integer32"
_Pm251dMesrclientRxpwrMeasPortn_Object = MibTableColumn
pm251dMesrclientRxpwrMeasPortn = _Pm251dMesrclientRxpwrMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 2, 48, 1, 2),
    _Pm251dMesrclientRxpwrMeasPortn_Type()
)
pm251dMesrclientRxpwrMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dMesrclientRxpwrMeasPortn.setStatus("current")
_Pm251dMesrLine_ObjectIdentity = ObjectIdentity
pm251dMesrLine = _Pm251dMesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 3)
)
_Pm251dMesrlineTempMeasTable_Object = MibTable
pm251dMesrlineTempMeasTable = _Pm251dMesrlineTempMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 3, 160)
)
if mibBuilder.loadTexts:
    pm251dMesrlineTempMeasTable.setStatus("current")
_Pm251dMesrlineTempMeasEntry_Object = MibTableRow
pm251dMesrlineTempMeasEntry = _Pm251dMesrlineTempMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 3, 160, 1)
)
pm251dMesrlineTempMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dMesrlineTempMeasIndex"),
)
if mibBuilder.loadTexts:
    pm251dMesrlineTempMeasEntry.setStatus("current")


class _Pm251dMesrlineTempMeasIndex_Type(Integer32):
    """Custom type pm251dMesrlineTempMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dMesrlineTempMeasIndex_Type.__name__ = "Integer32"
_Pm251dMesrlineTempMeasIndex_Object = MibTableColumn
pm251dMesrlineTempMeasIndex = _Pm251dMesrlineTempMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 3, 160, 1, 1),
    _Pm251dMesrlineTempMeasIndex_Type()
)
pm251dMesrlineTempMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dMesrlineTempMeasIndex.setStatus("current")


class _Pm251dMesrlineTempMeasPortn_Type(Integer32):
    """Custom type pm251dMesrlineTempMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm251dMesrlineTempMeasPortn_Type.__name__ = "Integer32"
_Pm251dMesrlineTempMeasPortn_Object = MibTableColumn
pm251dMesrlineTempMeasPortn = _Pm251dMesrlineTempMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 3, 160, 1, 2),
    _Pm251dMesrlineTempMeasPortn_Type()
)
pm251dMesrlineTempMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dMesrlineTempMeasPortn.setStatus("current")
_Pm251dMesrlineVoltMeasTable_Object = MibTable
pm251dMesrlineVoltMeasTable = _Pm251dMesrlineVoltMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 3, 161)
)
if mibBuilder.loadTexts:
    pm251dMesrlineVoltMeasTable.setStatus("current")
_Pm251dMesrlineVoltMeasEntry_Object = MibTableRow
pm251dMesrlineVoltMeasEntry = _Pm251dMesrlineVoltMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 3, 161, 1)
)
pm251dMesrlineVoltMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dMesrlineVoltMeasIndex"),
)
if mibBuilder.loadTexts:
    pm251dMesrlineVoltMeasEntry.setStatus("current")


class _Pm251dMesrlineVoltMeasIndex_Type(Integer32):
    """Custom type pm251dMesrlineVoltMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dMesrlineVoltMeasIndex_Type.__name__ = "Integer32"
_Pm251dMesrlineVoltMeasIndex_Object = MibTableColumn
pm251dMesrlineVoltMeasIndex = _Pm251dMesrlineVoltMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 3, 161, 1, 1),
    _Pm251dMesrlineVoltMeasIndex_Type()
)
pm251dMesrlineVoltMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dMesrlineVoltMeasIndex.setStatus("current")


class _Pm251dMesrlineVoltMeasPortn_Type(Integer32):
    """Custom type pm251dMesrlineVoltMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm251dMesrlineVoltMeasPortn_Type.__name__ = "Integer32"
_Pm251dMesrlineVoltMeasPortn_Object = MibTableColumn
pm251dMesrlineVoltMeasPortn = _Pm251dMesrlineVoltMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 3, 161, 1, 2),
    _Pm251dMesrlineVoltMeasPortn_Type()
)
pm251dMesrlineVoltMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dMesrlineVoltMeasPortn.setStatus("current")
_Pm251dMesrlineBiasMeasTable_Object = MibTable
pm251dMesrlineBiasMeasTable = _Pm251dMesrlineBiasMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 3, 162)
)
if mibBuilder.loadTexts:
    pm251dMesrlineBiasMeasTable.setStatus("current")
_Pm251dMesrlineBiasMeasEntry_Object = MibTableRow
pm251dMesrlineBiasMeasEntry = _Pm251dMesrlineBiasMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 3, 162, 1)
)
pm251dMesrlineBiasMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dMesrlineBiasMeasIndex"),
)
if mibBuilder.loadTexts:
    pm251dMesrlineBiasMeasEntry.setStatus("current")


class _Pm251dMesrlineBiasMeasIndex_Type(Integer32):
    """Custom type pm251dMesrlineBiasMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dMesrlineBiasMeasIndex_Type.__name__ = "Integer32"
_Pm251dMesrlineBiasMeasIndex_Object = MibTableColumn
pm251dMesrlineBiasMeasIndex = _Pm251dMesrlineBiasMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 3, 162, 1, 1),
    _Pm251dMesrlineBiasMeasIndex_Type()
)
pm251dMesrlineBiasMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dMesrlineBiasMeasIndex.setStatus("current")


class _Pm251dMesrlineBiasMeasPortn_Type(Integer32):
    """Custom type pm251dMesrlineBiasMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm251dMesrlineBiasMeasPortn_Type.__name__ = "Integer32"
_Pm251dMesrlineBiasMeasPortn_Object = MibTableColumn
pm251dMesrlineBiasMeasPortn = _Pm251dMesrlineBiasMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 3, 162, 1, 2),
    _Pm251dMesrlineBiasMeasPortn_Type()
)
pm251dMesrlineBiasMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dMesrlineBiasMeasPortn.setStatus("current")
_Pm251dMesrlineTxpwrMeasTable_Object = MibTable
pm251dMesrlineTxpwrMeasTable = _Pm251dMesrlineTxpwrMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 3, 163)
)
if mibBuilder.loadTexts:
    pm251dMesrlineTxpwrMeasTable.setStatus("current")
_Pm251dMesrlineTxpwrMeasEntry_Object = MibTableRow
pm251dMesrlineTxpwrMeasEntry = _Pm251dMesrlineTxpwrMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 3, 163, 1)
)
pm251dMesrlineTxpwrMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dMesrlineTxpwrMeasIndex"),
)
if mibBuilder.loadTexts:
    pm251dMesrlineTxpwrMeasEntry.setStatus("current")


class _Pm251dMesrlineTxpwrMeasIndex_Type(Integer32):
    """Custom type pm251dMesrlineTxpwrMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dMesrlineTxpwrMeasIndex_Type.__name__ = "Integer32"
_Pm251dMesrlineTxpwrMeasIndex_Object = MibTableColumn
pm251dMesrlineTxpwrMeasIndex = _Pm251dMesrlineTxpwrMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 3, 163, 1, 1),
    _Pm251dMesrlineTxpwrMeasIndex_Type()
)
pm251dMesrlineTxpwrMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dMesrlineTxpwrMeasIndex.setStatus("current")


class _Pm251dMesrlineTxpwrMeasPortn_Type(Integer32):
    """Custom type pm251dMesrlineTxpwrMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm251dMesrlineTxpwrMeasPortn_Type.__name__ = "Integer32"
_Pm251dMesrlineTxpwrMeasPortn_Object = MibTableColumn
pm251dMesrlineTxpwrMeasPortn = _Pm251dMesrlineTxpwrMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 3, 163, 1, 2),
    _Pm251dMesrlineTxpwrMeasPortn_Type()
)
pm251dMesrlineTxpwrMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dMesrlineTxpwrMeasPortn.setStatus("current")
_Pm251dMesrlineRxpwrMeasTable_Object = MibTable
pm251dMesrlineRxpwrMeasTable = _Pm251dMesrlineRxpwrMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 3, 164)
)
if mibBuilder.loadTexts:
    pm251dMesrlineRxpwrMeasTable.setStatus("current")
_Pm251dMesrlineRxpwrMeasEntry_Object = MibTableRow
pm251dMesrlineRxpwrMeasEntry = _Pm251dMesrlineRxpwrMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 3, 164, 1)
)
pm251dMesrlineRxpwrMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dMesrlineRxpwrMeasIndex"),
)
if mibBuilder.loadTexts:
    pm251dMesrlineRxpwrMeasEntry.setStatus("current")


class _Pm251dMesrlineRxpwrMeasIndex_Type(Integer32):
    """Custom type pm251dMesrlineRxpwrMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dMesrlineRxpwrMeasIndex_Type.__name__ = "Integer32"
_Pm251dMesrlineRxpwrMeasIndex_Object = MibTableColumn
pm251dMesrlineRxpwrMeasIndex = _Pm251dMesrlineRxpwrMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 3, 164, 1, 1),
    _Pm251dMesrlineRxpwrMeasIndex_Type()
)
pm251dMesrlineRxpwrMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dMesrlineRxpwrMeasIndex.setStatus("current")


class _Pm251dMesrlineRxpwrMeasPortn_Type(Integer32):
    """Custom type pm251dMesrlineRxpwrMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm251dMesrlineRxpwrMeasPortn_Type.__name__ = "Integer32"
_Pm251dMesrlineRxpwrMeasPortn_Object = MibTableColumn
pm251dMesrlineRxpwrMeasPortn = _Pm251dMesrlineRxpwrMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 3, 3, 164, 1, 2),
    _Pm251dMesrlineRxpwrMeasPortn_Type()
)
pm251dMesrlineRxpwrMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dMesrlineRxpwrMeasPortn.setStatus("current")
_Pm251dcounters_ObjectIdentity = ObjectIdentity
pm251dcounters = _Pm251dcounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4)
)
_Pm251dCntOther_ObjectIdentity = ObjectIdentity
pm251dCntOther = _Pm251dCntOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 1)
)
_Pm251dCntPort_ObjectIdentity = ObjectIdentity
pm251dCntPort = _Pm251dCntPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 2)
)
_Pm251dCntclientUpRaRemCntTable_Object = MibTable
pm251dCntclientUpRaRemCntTable = _Pm251dCntclientUpRaRemCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 2, 16)
)
if mibBuilder.loadTexts:
    pm251dCntclientUpRaRemCntTable.setStatus("current")
_Pm251dCntclientUpRaRemCntEntry_Object = MibTableRow
pm251dCntclientUpRaRemCntEntry = _Pm251dCntclientUpRaRemCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 2, 16, 1)
)
pm251dCntclientUpRaRemCntEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dCntclientUpRaRemCntIndex"),
)
if mibBuilder.loadTexts:
    pm251dCntclientUpRaRemCntEntry.setStatus("current")


class _Pm251dCntclientUpRaRemCntIndex_Type(Integer32):
    """Custom type pm251dCntclientUpRaRemCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dCntclientUpRaRemCntIndex_Type.__name__ = "Integer32"
_Pm251dCntclientUpRaRemCntIndex_Object = MibTableColumn
pm251dCntclientUpRaRemCntIndex = _Pm251dCntclientUpRaRemCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 2, 16, 1, 1),
    _Pm251dCntclientUpRaRemCntIndex_Type()
)
pm251dCntclientUpRaRemCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCntclientUpRaRemCntIndex.setStatus("current")
_Pm251dCntclientUpRaRemCntValuePortn_Type = Counter32
_Pm251dCntclientUpRaRemCntValuePortn_Object = MibTableColumn
pm251dCntclientUpRaRemCntValuePortn = _Pm251dCntclientUpRaRemCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 2, 16, 1, 2),
    _Pm251dCntclientUpRaRemCntValuePortn_Type()
)
pm251dCntclientUpRaRemCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCntclientUpRaRemCntValuePortn.setStatus("current")
_Pm251dCntclientUpRaRemCntErrorPortn_Type = EkiOnOff
_Pm251dCntclientUpRaRemCntErrorPortn_Object = MibTableColumn
pm251dCntclientUpRaRemCntErrorPortn = _Pm251dCntclientUpRaRemCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 2, 16, 1, 3),
    _Pm251dCntclientUpRaRemCntErrorPortn_Type()
)
pm251dCntclientUpRaRemCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCntclientUpRaRemCntErrorPortn.setStatus("current")
_Pm251dCntclientUpRaRemCntOverloadPortn_Type = EkiOnOff
_Pm251dCntclientUpRaRemCntOverloadPortn_Object = MibTableColumn
pm251dCntclientUpRaRemCntOverloadPortn = _Pm251dCntclientUpRaRemCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 2, 16, 1, 4),
    _Pm251dCntclientUpRaRemCntOverloadPortn_Type()
)
pm251dCntclientUpRaRemCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCntclientUpRaRemCntOverloadPortn.setStatus("current")
_Pm251dCntclientUpRaInsCntTable_Object = MibTable
pm251dCntclientUpRaInsCntTable = _Pm251dCntclientUpRaInsCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 2, 24)
)
if mibBuilder.loadTexts:
    pm251dCntclientUpRaInsCntTable.setStatus("current")
_Pm251dCntclientUpRaInsCntEntry_Object = MibTableRow
pm251dCntclientUpRaInsCntEntry = _Pm251dCntclientUpRaInsCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 2, 24, 1)
)
pm251dCntclientUpRaInsCntEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dCntclientUpRaInsCntIndex"),
)
if mibBuilder.loadTexts:
    pm251dCntclientUpRaInsCntEntry.setStatus("current")


class _Pm251dCntclientUpRaInsCntIndex_Type(Integer32):
    """Custom type pm251dCntclientUpRaInsCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dCntclientUpRaInsCntIndex_Type.__name__ = "Integer32"
_Pm251dCntclientUpRaInsCntIndex_Object = MibTableColumn
pm251dCntclientUpRaInsCntIndex = _Pm251dCntclientUpRaInsCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 2, 24, 1, 1),
    _Pm251dCntclientUpRaInsCntIndex_Type()
)
pm251dCntclientUpRaInsCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCntclientUpRaInsCntIndex.setStatus("current")
_Pm251dCntclientUpRaInsCntValuePortn_Type = Counter32
_Pm251dCntclientUpRaInsCntValuePortn_Object = MibTableColumn
pm251dCntclientUpRaInsCntValuePortn = _Pm251dCntclientUpRaInsCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 2, 24, 1, 2),
    _Pm251dCntclientUpRaInsCntValuePortn_Type()
)
pm251dCntclientUpRaInsCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCntclientUpRaInsCntValuePortn.setStatus("current")
_Pm251dCntclientUpRaInsCntErrorPortn_Type = EkiOnOff
_Pm251dCntclientUpRaInsCntErrorPortn_Object = MibTableColumn
pm251dCntclientUpRaInsCntErrorPortn = _Pm251dCntclientUpRaInsCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 2, 24, 1, 3),
    _Pm251dCntclientUpRaInsCntErrorPortn_Type()
)
pm251dCntclientUpRaInsCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCntclientUpRaInsCntErrorPortn.setStatus("current")
_Pm251dCntclientUpRaInsCntOverloadPortn_Type = EkiOnOff
_Pm251dCntclientUpRaInsCntOverloadPortn_Object = MibTableColumn
pm251dCntclientUpRaInsCntOverloadPortn = _Pm251dCntclientUpRaInsCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 2, 24, 1, 4),
    _Pm251dCntclientUpRaInsCntOverloadPortn_Type()
)
pm251dCntclientUpRaInsCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCntclientUpRaInsCntOverloadPortn.setStatus("current")
_Pm251dCntclientUpDispErrCntTable_Object = MibTable
pm251dCntclientUpDispErrCntTable = _Pm251dCntclientUpDispErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 2, 32)
)
if mibBuilder.loadTexts:
    pm251dCntclientUpDispErrCntTable.setStatus("current")
_Pm251dCntclientUpDispErrCntEntry_Object = MibTableRow
pm251dCntclientUpDispErrCntEntry = _Pm251dCntclientUpDispErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 2, 32, 1)
)
pm251dCntclientUpDispErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dCntclientUpDispErrCntIndex"),
)
if mibBuilder.loadTexts:
    pm251dCntclientUpDispErrCntEntry.setStatus("current")


class _Pm251dCntclientUpDispErrCntIndex_Type(Integer32):
    """Custom type pm251dCntclientUpDispErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dCntclientUpDispErrCntIndex_Type.__name__ = "Integer32"
_Pm251dCntclientUpDispErrCntIndex_Object = MibTableColumn
pm251dCntclientUpDispErrCntIndex = _Pm251dCntclientUpDispErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 2, 32, 1, 1),
    _Pm251dCntclientUpDispErrCntIndex_Type()
)
pm251dCntclientUpDispErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCntclientUpDispErrCntIndex.setStatus("current")
_Pm251dCntclientUpDispErrCntValuePortn_Type = Counter32
_Pm251dCntclientUpDispErrCntValuePortn_Object = MibTableColumn
pm251dCntclientUpDispErrCntValuePortn = _Pm251dCntclientUpDispErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 2, 32, 1, 2),
    _Pm251dCntclientUpDispErrCntValuePortn_Type()
)
pm251dCntclientUpDispErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCntclientUpDispErrCntValuePortn.setStatus("current")
_Pm251dCntclientUpDispErrCntErrorPortn_Type = EkiOnOff
_Pm251dCntclientUpDispErrCntErrorPortn_Object = MibTableColumn
pm251dCntclientUpDispErrCntErrorPortn = _Pm251dCntclientUpDispErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 2, 32, 1, 3),
    _Pm251dCntclientUpDispErrCntErrorPortn_Type()
)
pm251dCntclientUpDispErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCntclientUpDispErrCntErrorPortn.setStatus("current")
_Pm251dCntclientUpDispErrCntOverloadPortn_Type = EkiOnOff
_Pm251dCntclientUpDispErrCntOverloadPortn_Object = MibTableColumn
pm251dCntclientUpDispErrCntOverloadPortn = _Pm251dCntclientUpDispErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 2, 32, 1, 4),
    _Pm251dCntclientUpDispErrCntOverloadPortn_Type()
)
pm251dCntclientUpDispErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCntclientUpDispErrCntOverloadPortn.setStatus("current")
_Pm251dCntclientUpTimCntTable_Object = MibTable
pm251dCntclientUpTimCntTable = _Pm251dCntclientUpTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 2, 40)
)
if mibBuilder.loadTexts:
    pm251dCntclientUpTimCntTable.setStatus("current")
_Pm251dCntclientUpTimCntEntry_Object = MibTableRow
pm251dCntclientUpTimCntEntry = _Pm251dCntclientUpTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 2, 40, 1)
)
pm251dCntclientUpTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dCntclientUpTimCntIndex"),
)
if mibBuilder.loadTexts:
    pm251dCntclientUpTimCntEntry.setStatus("current")


class _Pm251dCntclientUpTimCntIndex_Type(Integer32):
    """Custom type pm251dCntclientUpTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dCntclientUpTimCntIndex_Type.__name__ = "Integer32"
_Pm251dCntclientUpTimCntIndex_Object = MibTableColumn
pm251dCntclientUpTimCntIndex = _Pm251dCntclientUpTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 2, 40, 1, 1),
    _Pm251dCntclientUpTimCntIndex_Type()
)
pm251dCntclientUpTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCntclientUpTimCntIndex.setStatus("current")
_Pm251dCntclientUpTimCntValuePortn_Type = Counter32
_Pm251dCntclientUpTimCntValuePortn_Object = MibTableColumn
pm251dCntclientUpTimCntValuePortn = _Pm251dCntclientUpTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 2, 40, 1, 2),
    _Pm251dCntclientUpTimCntValuePortn_Type()
)
pm251dCntclientUpTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCntclientUpTimCntValuePortn.setStatus("current")
_Pm251dCntclientUpTimCntErrorPortn_Type = EkiOnOff
_Pm251dCntclientUpTimCntErrorPortn_Object = MibTableColumn
pm251dCntclientUpTimCntErrorPortn = _Pm251dCntclientUpTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 2, 40, 1, 3),
    _Pm251dCntclientUpTimCntErrorPortn_Type()
)
pm251dCntclientUpTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCntclientUpTimCntErrorPortn.setStatus("current")
_Pm251dCntclientUpTimCntOverloadPortn_Type = EkiOnOff
_Pm251dCntclientUpTimCntOverloadPortn_Object = MibTableColumn
pm251dCntclientUpTimCntOverloadPortn = _Pm251dCntclientUpTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 2, 40, 1, 4),
    _Pm251dCntclientUpTimCntOverloadPortn_Type()
)
pm251dCntclientUpTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCntclientUpTimCntOverloadPortn.setStatus("current")
_Pm251dCntclientDwCbipCntTable_Object = MibTable
pm251dCntclientDwCbipCntTable = _Pm251dCntclientDwCbipCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 2, 64)
)
if mibBuilder.loadTexts:
    pm251dCntclientDwCbipCntTable.setStatus("current")
_Pm251dCntclientDwCbipCntEntry_Object = MibTableRow
pm251dCntclientDwCbipCntEntry = _Pm251dCntclientDwCbipCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 2, 64, 1)
)
pm251dCntclientDwCbipCntEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dCntclientDwCbipCntIndex"),
)
if mibBuilder.loadTexts:
    pm251dCntclientDwCbipCntEntry.setStatus("current")


class _Pm251dCntclientDwCbipCntIndex_Type(Integer32):
    """Custom type pm251dCntclientDwCbipCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dCntclientDwCbipCntIndex_Type.__name__ = "Integer32"
_Pm251dCntclientDwCbipCntIndex_Object = MibTableColumn
pm251dCntclientDwCbipCntIndex = _Pm251dCntclientDwCbipCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 2, 64, 1, 1),
    _Pm251dCntclientDwCbipCntIndex_Type()
)
pm251dCntclientDwCbipCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCntclientDwCbipCntIndex.setStatus("current")
_Pm251dCntclientDwCbipCntValuePortn_Type = Counter32
_Pm251dCntclientDwCbipCntValuePortn_Object = MibTableColumn
pm251dCntclientDwCbipCntValuePortn = _Pm251dCntclientDwCbipCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 2, 64, 1, 2),
    _Pm251dCntclientDwCbipCntValuePortn_Type()
)
pm251dCntclientDwCbipCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCntclientDwCbipCntValuePortn.setStatus("current")
_Pm251dCntclientDwCbipCntErrorPortn_Type = EkiOnOff
_Pm251dCntclientDwCbipCntErrorPortn_Object = MibTableColumn
pm251dCntclientDwCbipCntErrorPortn = _Pm251dCntclientDwCbipCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 2, 64, 1, 3),
    _Pm251dCntclientDwCbipCntErrorPortn_Type()
)
pm251dCntclientDwCbipCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCntclientDwCbipCntErrorPortn.setStatus("current")
_Pm251dCntclientDwCbipCntOverloadPortn_Type = EkiOnOff
_Pm251dCntclientDwCbipCntOverloadPortn_Object = MibTableColumn
pm251dCntclientDwCbipCntOverloadPortn = _Pm251dCntclientDwCbipCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 2, 64, 1, 4),
    _Pm251dCntclientDwCbipCntOverloadPortn_Type()
)
pm251dCntclientDwCbipCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCntclientDwCbipCntOverloadPortn.setStatus("current")
_Pm251dCntclientDwTimCntTable_Object = MibTable
pm251dCntclientDwTimCntTable = _Pm251dCntclientDwTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 2, 72)
)
if mibBuilder.loadTexts:
    pm251dCntclientDwTimCntTable.setStatus("current")
_Pm251dCntclientDwTimCntEntry_Object = MibTableRow
pm251dCntclientDwTimCntEntry = _Pm251dCntclientDwTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 2, 72, 1)
)
pm251dCntclientDwTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dCntclientDwTimCntIndex"),
)
if mibBuilder.loadTexts:
    pm251dCntclientDwTimCntEntry.setStatus("current")


class _Pm251dCntclientDwTimCntIndex_Type(Integer32):
    """Custom type pm251dCntclientDwTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dCntclientDwTimCntIndex_Type.__name__ = "Integer32"
_Pm251dCntclientDwTimCntIndex_Object = MibTableColumn
pm251dCntclientDwTimCntIndex = _Pm251dCntclientDwTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 2, 72, 1, 1),
    _Pm251dCntclientDwTimCntIndex_Type()
)
pm251dCntclientDwTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCntclientDwTimCntIndex.setStatus("current")
_Pm251dCntclientDwTimCntValuePortn_Type = Counter32
_Pm251dCntclientDwTimCntValuePortn_Object = MibTableColumn
pm251dCntclientDwTimCntValuePortn = _Pm251dCntclientDwTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 2, 72, 1, 2),
    _Pm251dCntclientDwTimCntValuePortn_Type()
)
pm251dCntclientDwTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCntclientDwTimCntValuePortn.setStatus("current")
_Pm251dCntclientDwTimCntErrorPortn_Type = EkiOnOff
_Pm251dCntclientDwTimCntErrorPortn_Object = MibTableColumn
pm251dCntclientDwTimCntErrorPortn = _Pm251dCntclientDwTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 2, 72, 1, 3),
    _Pm251dCntclientDwTimCntErrorPortn_Type()
)
pm251dCntclientDwTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCntclientDwTimCntErrorPortn.setStatus("current")
_Pm251dCntclientDwTimCntOverloadPortn_Type = EkiOnOff
_Pm251dCntclientDwTimCntOverloadPortn_Object = MibTableColumn
pm251dCntclientDwTimCntOverloadPortn = _Pm251dCntclientDwTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 2, 72, 1, 4),
    _Pm251dCntclientDwTimCntOverloadPortn_Type()
)
pm251dCntclientDwTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCntclientDwTimCntOverloadPortn.setStatus("current")
_Pm251dCntLine_ObjectIdentity = ObjectIdentity
pm251dCntLine = _Pm251dCntLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 3)
)
_Pm251dCntlineDfrmB1ErrCntTable_Object = MibTable
pm251dCntlineDfrmB1ErrCntTable = _Pm251dCntlineDfrmB1ErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 3, 152)
)
if mibBuilder.loadTexts:
    pm251dCntlineDfrmB1ErrCntTable.setStatus("current")
_Pm251dCntlineDfrmB1ErrCntEntry_Object = MibTableRow
pm251dCntlineDfrmB1ErrCntEntry = _Pm251dCntlineDfrmB1ErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 3, 152, 1)
)
pm251dCntlineDfrmB1ErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dCntlineDfrmB1ErrCntIndex"),
)
if mibBuilder.loadTexts:
    pm251dCntlineDfrmB1ErrCntEntry.setStatus("current")


class _Pm251dCntlineDfrmB1ErrCntIndex_Type(Integer32):
    """Custom type pm251dCntlineDfrmB1ErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dCntlineDfrmB1ErrCntIndex_Type.__name__ = "Integer32"
_Pm251dCntlineDfrmB1ErrCntIndex_Object = MibTableColumn
pm251dCntlineDfrmB1ErrCntIndex = _Pm251dCntlineDfrmB1ErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 3, 152, 1, 1),
    _Pm251dCntlineDfrmB1ErrCntIndex_Type()
)
pm251dCntlineDfrmB1ErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCntlineDfrmB1ErrCntIndex.setStatus("current")
_Pm251dCntlineDfrmB1ErrCntValuePortn_Type = Counter32
_Pm251dCntlineDfrmB1ErrCntValuePortn_Object = MibTableColumn
pm251dCntlineDfrmB1ErrCntValuePortn = _Pm251dCntlineDfrmB1ErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 3, 152, 1, 2),
    _Pm251dCntlineDfrmB1ErrCntValuePortn_Type()
)
pm251dCntlineDfrmB1ErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCntlineDfrmB1ErrCntValuePortn.setStatus("current")
_Pm251dCntlineDfrmB1ErrCntErrorPortn_Type = EkiOnOff
_Pm251dCntlineDfrmB1ErrCntErrorPortn_Object = MibTableColumn
pm251dCntlineDfrmB1ErrCntErrorPortn = _Pm251dCntlineDfrmB1ErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 3, 152, 1, 3),
    _Pm251dCntlineDfrmB1ErrCntErrorPortn_Type()
)
pm251dCntlineDfrmB1ErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCntlineDfrmB1ErrCntErrorPortn.setStatus("current")
_Pm251dCntlineDfrmB1ErrCntOverloadPortn_Type = EkiOnOff
_Pm251dCntlineDfrmB1ErrCntOverloadPortn_Object = MibTableColumn
pm251dCntlineDfrmB1ErrCntOverloadPortn = _Pm251dCntlineDfrmB1ErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 3, 152, 1, 4),
    _Pm251dCntlineDfrmB1ErrCntOverloadPortn_Type()
)
pm251dCntlineDfrmB1ErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCntlineDfrmB1ErrCntOverloadPortn.setStatus("current")
_Pm251dCntlineDfrmTimCntTable_Object = MibTable
pm251dCntlineDfrmTimCntTable = _Pm251dCntlineDfrmTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 3, 153)
)
if mibBuilder.loadTexts:
    pm251dCntlineDfrmTimCntTable.setStatus("current")
_Pm251dCntlineDfrmTimCntEntry_Object = MibTableRow
pm251dCntlineDfrmTimCntEntry = _Pm251dCntlineDfrmTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 3, 153, 1)
)
pm251dCntlineDfrmTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dCntlineDfrmTimCntIndex"),
)
if mibBuilder.loadTexts:
    pm251dCntlineDfrmTimCntEntry.setStatus("current")


class _Pm251dCntlineDfrmTimCntIndex_Type(Integer32):
    """Custom type pm251dCntlineDfrmTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dCntlineDfrmTimCntIndex_Type.__name__ = "Integer32"
_Pm251dCntlineDfrmTimCntIndex_Object = MibTableColumn
pm251dCntlineDfrmTimCntIndex = _Pm251dCntlineDfrmTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 3, 153, 1, 1),
    _Pm251dCntlineDfrmTimCntIndex_Type()
)
pm251dCntlineDfrmTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCntlineDfrmTimCntIndex.setStatus("current")
_Pm251dCntlineDfrmTimCntValuePortn_Type = Counter32
_Pm251dCntlineDfrmTimCntValuePortn_Object = MibTableColumn
pm251dCntlineDfrmTimCntValuePortn = _Pm251dCntlineDfrmTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 3, 153, 1, 2),
    _Pm251dCntlineDfrmTimCntValuePortn_Type()
)
pm251dCntlineDfrmTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCntlineDfrmTimCntValuePortn.setStatus("current")
_Pm251dCntlineDfrmTimCntErrorPortn_Type = EkiOnOff
_Pm251dCntlineDfrmTimCntErrorPortn_Object = MibTableColumn
pm251dCntlineDfrmTimCntErrorPortn = _Pm251dCntlineDfrmTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 3, 153, 1, 3),
    _Pm251dCntlineDfrmTimCntErrorPortn_Type()
)
pm251dCntlineDfrmTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCntlineDfrmTimCntErrorPortn.setStatus("current")
_Pm251dCntlineDfrmTimCntOverloadPortn_Type = EkiOnOff
_Pm251dCntlineDfrmTimCntOverloadPortn_Object = MibTableColumn
pm251dCntlineDfrmTimCntOverloadPortn = _Pm251dCntlineDfrmTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 3, 153, 1, 4),
    _Pm251dCntlineDfrmTimCntOverloadPortn_Type()
)
pm251dCntlineDfrmTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCntlineDfrmTimCntOverloadPortn.setStatus("current")
_Pm251dCntdfrmPrimLineErrCntTable_Object = MibTable
pm251dCntdfrmPrimLineErrCntTable = _Pm251dCntdfrmPrimLineErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 3, 154)
)
if mibBuilder.loadTexts:
    pm251dCntdfrmPrimLineErrCntTable.setStatus("current")
_Pm251dCntdfrmPrimLineErrCntEntry_Object = MibTableRow
pm251dCntdfrmPrimLineErrCntEntry = _Pm251dCntdfrmPrimLineErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 3, 154, 1)
)
pm251dCntdfrmPrimLineErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dCntdfrmPrimLineErrCntIndex"),
)
if mibBuilder.loadTexts:
    pm251dCntdfrmPrimLineErrCntEntry.setStatus("current")


class _Pm251dCntdfrmPrimLineErrCntIndex_Type(Integer32):
    """Custom type pm251dCntdfrmPrimLineErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dCntdfrmPrimLineErrCntIndex_Type.__name__ = "Integer32"
_Pm251dCntdfrmPrimLineErrCntIndex_Object = MibTableColumn
pm251dCntdfrmPrimLineErrCntIndex = _Pm251dCntdfrmPrimLineErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 3, 154, 1, 1),
    _Pm251dCntdfrmPrimLineErrCntIndex_Type()
)
pm251dCntdfrmPrimLineErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCntdfrmPrimLineErrCntIndex.setStatus("current")
_Pm251dCntdfrmPrimLineErrCntValuePortn_Type = Counter32
_Pm251dCntdfrmPrimLineErrCntValuePortn_Object = MibTableColumn
pm251dCntdfrmPrimLineErrCntValuePortn = _Pm251dCntdfrmPrimLineErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 3, 154, 1, 2),
    _Pm251dCntdfrmPrimLineErrCntValuePortn_Type()
)
pm251dCntdfrmPrimLineErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCntdfrmPrimLineErrCntValuePortn.setStatus("current")
_Pm251dCntdfrmPrimLineErrCntErrorPortn_Type = EkiOnOff
_Pm251dCntdfrmPrimLineErrCntErrorPortn_Object = MibTableColumn
pm251dCntdfrmPrimLineErrCntErrorPortn = _Pm251dCntdfrmPrimLineErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 3, 154, 1, 3),
    _Pm251dCntdfrmPrimLineErrCntErrorPortn_Type()
)
pm251dCntdfrmPrimLineErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCntdfrmPrimLineErrCntErrorPortn.setStatus("current")
_Pm251dCntdfrmPrimLineErrCntOverloadPortn_Type = EkiOnOff
_Pm251dCntdfrmPrimLineErrCntOverloadPortn_Object = MibTableColumn
pm251dCntdfrmPrimLineErrCntOverloadPortn = _Pm251dCntdfrmPrimLineErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 3, 154, 1, 4),
    _Pm251dCntdfrmPrimLineErrCntOverloadPortn_Type()
)
pm251dCntdfrmPrimLineErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCntdfrmPrimLineErrCntOverloadPortn.setStatus("current")
_Pm251dCntCountersReset_Type = EkiOnOff
_Pm251dCntCountersReset_Object = MibScalar
pm251dCntCountersReset = _Pm251dCntCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 259),
    _Pm251dCntCountersReset_Type()
)
pm251dCntCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCntCountersReset.setStatus("current")
_Pm251dCntCountersStop_Type = EkiOnOff
_Pm251dCntCountersStop_Object = MibScalar
pm251dCntCountersStop = _Pm251dCntCountersStop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 4, 260),
    _Pm251dCntCountersStop_Type()
)
pm251dCntCountersStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCntCountersStop.setStatus("current")
_Pm251dcontrolsWrite_ObjectIdentity = ObjectIdentity
pm251dcontrolsWrite = _Pm251dcontrolsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6)
)
_Pm251dCtrlOther_ObjectIdentity = ObjectIdentity
pm251dCtrlOther = _Pm251dCtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 1)
)
_Pm251dCtrlconfMgnt1_ObjectIdentity = ObjectIdentity
pm251dCtrlconfMgnt1 = _Pm251dCtrlconfMgnt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 1, 1)
)
_Pm251dCtrlConf1Load1_Type = EkiOnOff
_Pm251dCtrlConf1Load1_Object = MibScalar
pm251dCtrlConf1Load1 = _Pm251dCtrlConf1Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 1, 1, 1),
    _Pm251dCtrlConf1Load1_Type()
)
pm251dCtrlConf1Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCtrlConf1Load1.setStatus("current")
_Pm251dCtrlConf2Load1_Type = EkiOnOff
_Pm251dCtrlConf2Load1_Object = MibScalar
pm251dCtrlConf2Load1 = _Pm251dCtrlConf2Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 1, 1, 2),
    _Pm251dCtrlConf2Load1_Type()
)
pm251dCtrlConf2Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCtrlConf2Load1.setStatus("current")
_Pm251dCtrlConf2Flash1_Type = EkiOnOff
_Pm251dCtrlConf2Flash1_Object = MibScalar
pm251dCtrlConf2Flash1 = _Pm251dCtrlConf2Flash1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 1, 1, 10),
    _Pm251dCtrlConf2Flash1_Type()
)
pm251dCtrlConf2Flash1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCtrlConf2Flash1.setStatus("current")
_Pm251dCtrlConf2Clear1_Type = EkiOnOff
_Pm251dCtrlConf2Clear1_Object = MibScalar
pm251dCtrlConf2Clear1 = _Pm251dCtrlConf2Clear1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 1, 1, 14),
    _Pm251dCtrlConf2Clear1_Type()
)
pm251dCtrlConf2Clear1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCtrlConf2Clear1.setStatus("current")
_Pm251dCtrlsynth4_ObjectIdentity = ObjectIdentity
pm251dCtrlsynth4 = _Pm251dCtrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 1, 4)
)
_Pm251dCtrlCorrelatOn_Type = EkiOnOff
_Pm251dCtrlCorrelatOn_Object = MibScalar
pm251dCtrlCorrelatOn = _Pm251dCtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 1, 4, 1),
    _Pm251dCtrlCorrelatOn_Type()
)
pm251dCtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCtrlCorrelatOn.setStatus("current")
_Pm251dCtrlCorrelatOff_Type = EkiOnOff
_Pm251dCtrlCorrelatOff_Object = MibScalar
pm251dCtrlCorrelatOff = _Pm251dCtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 1, 4, 2),
    _Pm251dCtrlCorrelatOff_Type()
)
pm251dCtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCtrlCorrelatOff.setStatus("current")
_Pm251dCtrlswMgnt_ObjectIdentity = ObjectIdentity
pm251dCtrlswMgnt = _Pm251dCtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 1, 5)
)
_Pm251dCtrlColdReset_Type = EkiOnOff
_Pm251dCtrlColdReset_Object = MibScalar
pm251dCtrlColdReset = _Pm251dCtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 1, 5, 2),
    _Pm251dCtrlColdReset_Type()
)
pm251dCtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCtrlColdReset.setStatus("current")
_Pm251dCtrlWarmReset_Type = EkiOnOff
_Pm251dCtrlWarmReset_Object = MibScalar
pm251dCtrlWarmReset = _Pm251dCtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 1, 5, 3),
    _Pm251dCtrlWarmReset_Type()
)
pm251dCtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCtrlWarmReset.setStatus("current")
_Pm251dCtrlLoadSwBank1_Type = EkiOnOff
_Pm251dCtrlLoadSwBank1_Object = MibScalar
pm251dCtrlLoadSwBank1 = _Pm251dCtrlLoadSwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 1, 5, 5),
    _Pm251dCtrlLoadSwBank1_Type()
)
pm251dCtrlLoadSwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCtrlLoadSwBank1.setStatus("current")
_Pm251dCtrlLoadSwBank2_Type = EkiOnOff
_Pm251dCtrlLoadSwBank2_Object = MibScalar
pm251dCtrlLoadSwBank2 = _Pm251dCtrlLoadSwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 1, 5, 6),
    _Pm251dCtrlLoadSwBank2_Type()
)
pm251dCtrlLoadSwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCtrlLoadSwBank2.setStatus("current")
_Pm251dCtrlgwMgnt_ObjectIdentity = ObjectIdentity
pm251dCtrlgwMgnt = _Pm251dCtrlgwMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 1, 6)
)
_Pm251dCtrlCurrentGwReset_Type = EkiOnOff
_Pm251dCtrlCurrentGwReset_Object = MibScalar
pm251dCtrlCurrentGwReset = _Pm251dCtrlCurrentGwReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 1, 6, 1),
    _Pm251dCtrlCurrentGwReset_Type()
)
pm251dCtrlCurrentGwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCtrlCurrentGwReset.setStatus("current")
_Pm251dCtrlLoadGwBank1_Type = EkiOnOff
_Pm251dCtrlLoadGwBank1_Object = MibScalar
pm251dCtrlLoadGwBank1 = _Pm251dCtrlLoadGwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 1, 6, 5),
    _Pm251dCtrlLoadGwBank1_Type()
)
pm251dCtrlLoadGwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCtrlLoadGwBank1.setStatus("current")
_Pm251dCtrlLoadGwBank2_Type = EkiOnOff
_Pm251dCtrlLoadGwBank2_Object = MibScalar
pm251dCtrlLoadGwBank2 = _Pm251dCtrlLoadGwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 1, 6, 6),
    _Pm251dCtrlLoadGwBank2_Type()
)
pm251dCtrlLoadGwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCtrlLoadGwBank2.setStatus("current")
_Pm251dCtrlLoadGwBank3_Type = EkiOnOff
_Pm251dCtrlLoadGwBank3_Object = MibScalar
pm251dCtrlLoadGwBank3 = _Pm251dCtrlLoadGwBank3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 1, 6, 7),
    _Pm251dCtrlLoadGwBank3_Type()
)
pm251dCtrlLoadGwBank3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCtrlLoadGwBank3.setStatus("current")
_Pm251dCtrlLoadGwBank4_Type = EkiOnOff
_Pm251dCtrlLoadGwBank4_Object = MibScalar
pm251dCtrlLoadGwBank4 = _Pm251dCtrlLoadGwBank4_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 1, 6, 8),
    _Pm251dCtrlLoadGwBank4_Type()
)
pm251dCtrlLoadGwBank4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCtrlLoadGwBank4.setStatus("current")
_Pm251dCtrlledTest_ObjectIdentity = ObjectIdentity
pm251dCtrlledTest = _Pm251dCtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 1, 192)
)
_Pm251dCtrlGreenLed_Type = EkiOnOff
_Pm251dCtrlGreenLed_Object = MibScalar
pm251dCtrlGreenLed = _Pm251dCtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 1, 192, 1),
    _Pm251dCtrlGreenLed_Type()
)
pm251dCtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCtrlGreenLed.setStatus("current")
_Pm251dCtrlRedLed_Type = EkiOnOff
_Pm251dCtrlRedLed_Object = MibScalar
pm251dCtrlRedLed = _Pm251dCtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 1, 192, 2),
    _Pm251dCtrlRedLed_Type()
)
pm251dCtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCtrlRedLed.setStatus("current")
_Pm251dCtrlLedOff_Type = EkiOnOff
_Pm251dCtrlLedOff_Object = MibScalar
pm251dCtrlLedOff = _Pm251dCtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 1, 192, 3),
    _Pm251dCtrlLedOff_Type()
)
pm251dCtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCtrlLedOff.setStatus("current")
_Pm251dCtrlmoduleOosMode_ObjectIdentity = ObjectIdentity
pm251dCtrlmoduleOosMode = _Pm251dCtrlmoduleOosMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 1, 193)
)
_Pm251dCtrlModuleOosMode_Type = EkiOnOff
_Pm251dCtrlModuleOosMode_Object = MibScalar
pm251dCtrlModuleOosMode = _Pm251dCtrlModuleOosMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 1, 193, 1),
    _Pm251dCtrlModuleOosMode_Type()
)
pm251dCtrlModuleOosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCtrlModuleOosMode.setStatus("current")
_Pm251dCtrlmaintenanceMode_ObjectIdentity = ObjectIdentity
pm251dCtrlmaintenanceMode = _Pm251dCtrlmaintenanceMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 1, 197)
)
_Pm251dCtrlMaintenanceMode_Type = EkiOnOff
_Pm251dCtrlMaintenanceMode_Object = MibScalar
pm251dCtrlMaintenanceMode = _Pm251dCtrlMaintenanceMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 1, 197, 1),
    _Pm251dCtrlMaintenanceMode_Type()
)
pm251dCtrlMaintenanceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCtrlMaintenanceMode.setStatus("current")
_Pm251dCtrldccEnable_ObjectIdentity = ObjectIdentity
pm251dCtrldccEnable = _Pm251dCtrldccEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 1, 198)
)
_Pm251dCtrlDccEnable_Type = EkiOnOff
_Pm251dCtrlDccEnable_Object = MibScalar
pm251dCtrlDccEnable = _Pm251dCtrlDccEnable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 1, 198, 1),
    _Pm251dCtrlDccEnable_Type()
)
pm251dCtrlDccEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCtrlDccEnable.setStatus("current")
_Pm251dCtrlPort_ObjectIdentity = ObjectIdentity
pm251dCtrlPort = _Pm251dCtrlPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 2)
)
_Pm251dCtrlclientAccessLoopTable_Object = MibTable
pm251dCtrlclientAccessLoopTable = _Pm251dCtrlclientAccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 2, 16)
)
if mibBuilder.loadTexts:
    pm251dCtrlclientAccessLoopTable.setStatus("current")
_Pm251dCtrlclientAccessLoopEntry_Object = MibTableRow
pm251dCtrlclientAccessLoopEntry = _Pm251dCtrlclientAccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 2, 16, 1)
)
pm251dCtrlclientAccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dCtrlclientAccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pm251dCtrlclientAccessLoopEntry.setStatus("current")


class _Pm251dCtrlclientAccessLoopIndex_Type(Integer32):
    """Custom type pm251dCtrlclientAccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dCtrlclientAccessLoopIndex_Type.__name__ = "Integer32"
_Pm251dCtrlclientAccessLoopIndex_Object = MibTableColumn
pm251dCtrlclientAccessLoopIndex = _Pm251dCtrlclientAccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 2, 16, 1, 1),
    _Pm251dCtrlclientAccessLoopIndex_Type()
)
pm251dCtrlclientAccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCtrlclientAccessLoopIndex.setStatus("current")
_Pm251dCtrlclientAccessLoopPortn_Type = EkiState
_Pm251dCtrlclientAccessLoopPortn_Object = MibTableColumn
pm251dCtrlclientAccessLoopPortn = _Pm251dCtrlclientAccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 2, 16, 1, 2),
    _Pm251dCtrlclientAccessLoopPortn_Type()
)
pm251dCtrlclientAccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCtrlclientAccessLoopPortn.setStatus("current")
_Pm251dCtrlclientOosModeTable_Object = MibTable
pm251dCtrlclientOosModeTable = _Pm251dCtrlclientOosModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 2, 18)
)
if mibBuilder.loadTexts:
    pm251dCtrlclientOosModeTable.setStatus("current")
_Pm251dCtrlclientOosModeEntry_Object = MibTableRow
pm251dCtrlclientOosModeEntry = _Pm251dCtrlclientOosModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 2, 18, 1)
)
pm251dCtrlclientOosModeEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dCtrlclientOosModeIndex"),
)
if mibBuilder.loadTexts:
    pm251dCtrlclientOosModeEntry.setStatus("current")


class _Pm251dCtrlclientOosModeIndex_Type(Integer32):
    """Custom type pm251dCtrlclientOosModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dCtrlclientOosModeIndex_Type.__name__ = "Integer32"
_Pm251dCtrlclientOosModeIndex_Object = MibTableColumn
pm251dCtrlclientOosModeIndex = _Pm251dCtrlclientOosModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 2, 18, 1, 1),
    _Pm251dCtrlclientOosModeIndex_Type()
)
pm251dCtrlclientOosModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCtrlclientOosModeIndex.setStatus("current")
_Pm251dCtrlclientOosModePortn_Type = EkiState
_Pm251dCtrlclientOosModePortn_Object = MibTableColumn
pm251dCtrlclientOosModePortn = _Pm251dCtrlclientOosModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 2, 18, 1, 2),
    _Pm251dCtrlclientOosModePortn_Type()
)
pm251dCtrlclientOosModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCtrlclientOosModePortn.setStatus("current")
_Pm251dCtrlclientSfpOnOffCtrlTable_Object = MibTable
pm251dCtrlclientSfpOnOffCtrlTable = _Pm251dCtrlclientSfpOnOffCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 2, 20)
)
if mibBuilder.loadTexts:
    pm251dCtrlclientSfpOnOffCtrlTable.setStatus("current")
_Pm251dCtrlclientSfpOnOffCtrlEntry_Object = MibTableRow
pm251dCtrlclientSfpOnOffCtrlEntry = _Pm251dCtrlclientSfpOnOffCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 2, 20, 1)
)
pm251dCtrlclientSfpOnOffCtrlEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dCtrlclientSfpOnOffCtrlIndex"),
)
if mibBuilder.loadTexts:
    pm251dCtrlclientSfpOnOffCtrlEntry.setStatus("current")


class _Pm251dCtrlclientSfpOnOffCtrlIndex_Type(Integer32):
    """Custom type pm251dCtrlclientSfpOnOffCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dCtrlclientSfpOnOffCtrlIndex_Type.__name__ = "Integer32"
_Pm251dCtrlclientSfpOnOffCtrlIndex_Object = MibTableColumn
pm251dCtrlclientSfpOnOffCtrlIndex = _Pm251dCtrlclientSfpOnOffCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 2, 20, 1, 1),
    _Pm251dCtrlclientSfpOnOffCtrlIndex_Type()
)
pm251dCtrlclientSfpOnOffCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCtrlclientSfpOnOffCtrlIndex.setStatus("current")
_Pm251dCtrlclientSfpOnOffCtrlPortn_Type = EkiState
_Pm251dCtrlclientSfpOnOffCtrlPortn_Object = MibTableColumn
pm251dCtrlclientSfpOnOffCtrlPortn = _Pm251dCtrlclientSfpOnOffCtrlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 2, 20, 1, 2),
    _Pm251dCtrlclientSfpOnOffCtrlPortn_Type()
)
pm251dCtrlclientSfpOnOffCtrlPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCtrlclientSfpOnOffCtrlPortn.setStatus("current")
_Pm251dCtrlclientCsfUpInsTable_Object = MibTable
pm251dCtrlclientCsfUpInsTable = _Pm251dCtrlclientCsfUpInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 2, 21)
)
if mibBuilder.loadTexts:
    pm251dCtrlclientCsfUpInsTable.setStatus("current")
_Pm251dCtrlclientCsfUpInsEntry_Object = MibTableRow
pm251dCtrlclientCsfUpInsEntry = _Pm251dCtrlclientCsfUpInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 2, 21, 1)
)
pm251dCtrlclientCsfUpInsEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dCtrlclientCsfUpInsIndex"),
)
if mibBuilder.loadTexts:
    pm251dCtrlclientCsfUpInsEntry.setStatus("current")


class _Pm251dCtrlclientCsfUpInsIndex_Type(Integer32):
    """Custom type pm251dCtrlclientCsfUpInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dCtrlclientCsfUpInsIndex_Type.__name__ = "Integer32"
_Pm251dCtrlclientCsfUpInsIndex_Object = MibTableColumn
pm251dCtrlclientCsfUpInsIndex = _Pm251dCtrlclientCsfUpInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 2, 21, 1, 1),
    _Pm251dCtrlclientCsfUpInsIndex_Type()
)
pm251dCtrlclientCsfUpInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCtrlclientCsfUpInsIndex.setStatus("current")
_Pm251dCtrlclientCsfUpInsPortn_Type = EkiState
_Pm251dCtrlclientCsfUpInsPortn_Object = MibTableColumn
pm251dCtrlclientCsfUpInsPortn = _Pm251dCtrlclientCsfUpInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 2, 21, 1, 2),
    _Pm251dCtrlclientCsfUpInsPortn_Type()
)
pm251dCtrlclientCsfUpInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCtrlclientCsfUpInsPortn.setStatus("current")
_Pm251dCtrlclientCaisDwInsTable_Object = MibTable
pm251dCtrlclientCaisDwInsTable = _Pm251dCtrlclientCaisDwInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 2, 22)
)
if mibBuilder.loadTexts:
    pm251dCtrlclientCaisDwInsTable.setStatus("current")
_Pm251dCtrlclientCaisDwInsEntry_Object = MibTableRow
pm251dCtrlclientCaisDwInsEntry = _Pm251dCtrlclientCaisDwInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 2, 22, 1)
)
pm251dCtrlclientCaisDwInsEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dCtrlclientCaisDwInsIndex"),
)
if mibBuilder.loadTexts:
    pm251dCtrlclientCaisDwInsEntry.setStatus("current")


class _Pm251dCtrlclientCaisDwInsIndex_Type(Integer32):
    """Custom type pm251dCtrlclientCaisDwInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dCtrlclientCaisDwInsIndex_Type.__name__ = "Integer32"
_Pm251dCtrlclientCaisDwInsIndex_Object = MibTableColumn
pm251dCtrlclientCaisDwInsIndex = _Pm251dCtrlclientCaisDwInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 2, 22, 1, 1),
    _Pm251dCtrlclientCaisDwInsIndex_Type()
)
pm251dCtrlclientCaisDwInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCtrlclientCaisDwInsIndex.setStatus("current")
_Pm251dCtrlclientCaisDwInsPortn_Type = EkiState
_Pm251dCtrlclientCaisDwInsPortn_Object = MibTableColumn
pm251dCtrlclientCaisDwInsPortn = _Pm251dCtrlclientCaisDwInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 2, 22, 1, 2),
    _Pm251dCtrlclientCaisDwInsPortn_Type()
)
pm251dCtrlclientCaisDwInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCtrlclientCaisDwInsPortn.setStatus("current")
_Pm251dCtrlLine_ObjectIdentity = ObjectIdentity
pm251dCtrlLine = _Pm251dCtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 3)
)
_Pm251dCtrllineMsAis_ObjectIdentity = ObjectIdentity
pm251dCtrllineMsAis = _Pm251dCtrllineMsAis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 3, 67)
)
_Pm251dCtrlLineMsAis_Type = EkiOnOff
_Pm251dCtrlLineMsAis_Object = MibScalar
pm251dCtrlLineMsAis = _Pm251dCtrlLineMsAis_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 3, 67, 1),
    _Pm251dCtrlLineMsAis_Type()
)
pm251dCtrlLineMsAis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCtrlLineMsAis.setStatus("current")
_Pm251dCtrlfecDisableTable_Object = MibTable
pm251dCtrlfecDisableTable = _Pm251dCtrlfecDisableTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 3, 69)
)
if mibBuilder.loadTexts:
    pm251dCtrlfecDisableTable.setStatus("current")
_Pm251dCtrlfecDisableEntry_Object = MibTableRow
pm251dCtrlfecDisableEntry = _Pm251dCtrlfecDisableEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 3, 69, 1)
)
pm251dCtrlfecDisableEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dCtrlfecDisableIndex"),
)
if mibBuilder.loadTexts:
    pm251dCtrlfecDisableEntry.setStatus("current")


class _Pm251dCtrlfecDisableIndex_Type(Integer32):
    """Custom type pm251dCtrlfecDisableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dCtrlfecDisableIndex_Type.__name__ = "Integer32"
_Pm251dCtrlfecDisableIndex_Object = MibTableColumn
pm251dCtrlfecDisableIndex = _Pm251dCtrlfecDisableIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 3, 69, 1, 1),
    _Pm251dCtrlfecDisableIndex_Type()
)
pm251dCtrlfecDisableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCtrlfecDisableIndex.setStatus("current")
_Pm251dCtrlfecDisablePortn_Type = EkiState
_Pm251dCtrlfecDisablePortn_Object = MibTableColumn
pm251dCtrlfecDisablePortn = _Pm251dCtrlfecDisablePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 3, 69, 1, 2),
    _Pm251dCtrlfecDisablePortn_Type()
)
pm251dCtrlfecDisablePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCtrlfecDisablePortn.setStatus("current")
_Pm251dCtrllineUpS1Table_Object = MibTable
pm251dCtrllineUpS1Table = _Pm251dCtrllineUpS1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 3, 70)
)
if mibBuilder.loadTexts:
    pm251dCtrllineUpS1Table.setStatus("current")
_Pm251dCtrllineUpS1Entry_Object = MibTableRow
pm251dCtrllineUpS1Entry = _Pm251dCtrllineUpS1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 3, 70, 1)
)
pm251dCtrllineUpS1Entry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dCtrllineUpS1Index"),
)
if mibBuilder.loadTexts:
    pm251dCtrllineUpS1Entry.setStatus("current")


class _Pm251dCtrllineUpS1Index_Type(Integer32):
    """Custom type pm251dCtrllineUpS1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dCtrllineUpS1Index_Type.__name__ = "Integer32"
_Pm251dCtrllineUpS1Index_Object = MibTableColumn
pm251dCtrllineUpS1Index = _Pm251dCtrllineUpS1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 3, 70, 1, 1),
    _Pm251dCtrllineUpS1Index_Type()
)
pm251dCtrllineUpS1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCtrllineUpS1Index.setStatus("current")


class _Pm251dCtrllineUpS1Portn_Type(Integer32):
    """Custom type pm251dCtrllineUpS1Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Pm251dCtrllineUpS1Portn_Type.__name__ = "Integer32"
_Pm251dCtrllineUpS1Portn_Object = MibTableColumn
pm251dCtrllineUpS1Portn = _Pm251dCtrllineUpS1Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 3, 70, 1, 2),
    _Pm251dCtrllineUpS1Portn_Type()
)
pm251dCtrllineUpS1Portn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCtrllineUpS1Portn.setStatus("current")
_Pm251dCtrllineUpK1Table_Object = MibTable
pm251dCtrllineUpK1Table = _Pm251dCtrllineUpK1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 3, 71)
)
if mibBuilder.loadTexts:
    pm251dCtrllineUpK1Table.setStatus("current")
_Pm251dCtrllineUpK1Entry_Object = MibTableRow
pm251dCtrllineUpK1Entry = _Pm251dCtrllineUpK1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 3, 71, 1)
)
pm251dCtrllineUpK1Entry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dCtrllineUpK1Index"),
)
if mibBuilder.loadTexts:
    pm251dCtrllineUpK1Entry.setStatus("current")


class _Pm251dCtrllineUpK1Index_Type(Integer32):
    """Custom type pm251dCtrllineUpK1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dCtrllineUpK1Index_Type.__name__ = "Integer32"
_Pm251dCtrllineUpK1Index_Object = MibTableColumn
pm251dCtrllineUpK1Index = _Pm251dCtrllineUpK1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 3, 71, 1, 1),
    _Pm251dCtrllineUpK1Index_Type()
)
pm251dCtrllineUpK1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCtrllineUpK1Index.setStatus("current")


class _Pm251dCtrllineUpK1Portn_Type(Integer32):
    """Custom type pm251dCtrllineUpK1Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Pm251dCtrllineUpK1Portn_Type.__name__ = "Integer32"
_Pm251dCtrllineUpK1Portn_Object = MibTableColumn
pm251dCtrllineUpK1Portn = _Pm251dCtrllineUpK1Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 3, 71, 1, 2),
    _Pm251dCtrllineUpK1Portn_Type()
)
pm251dCtrllineUpK1Portn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCtrllineUpK1Portn.setStatus("current")
_Pm251dCtrllineUpK2Table_Object = MibTable
pm251dCtrllineUpK2Table = _Pm251dCtrllineUpK2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 3, 72)
)
if mibBuilder.loadTexts:
    pm251dCtrllineUpK2Table.setStatus("current")
_Pm251dCtrllineUpK2Entry_Object = MibTableRow
pm251dCtrllineUpK2Entry = _Pm251dCtrllineUpK2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 3, 72, 1)
)
pm251dCtrllineUpK2Entry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dCtrllineUpK2Index"),
)
if mibBuilder.loadTexts:
    pm251dCtrllineUpK2Entry.setStatus("current")


class _Pm251dCtrllineUpK2Index_Type(Integer32):
    """Custom type pm251dCtrllineUpK2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dCtrllineUpK2Index_Type.__name__ = "Integer32"
_Pm251dCtrllineUpK2Index_Object = MibTableColumn
pm251dCtrllineUpK2Index = _Pm251dCtrllineUpK2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 3, 72, 1, 1),
    _Pm251dCtrllineUpK2Index_Type()
)
pm251dCtrllineUpK2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCtrllineUpK2Index.setStatus("current")


class _Pm251dCtrllineUpK2Portn_Type(Integer32):
    """Custom type pm251dCtrllineUpK2Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Pm251dCtrllineUpK2Portn_Type.__name__ = "Integer32"
_Pm251dCtrllineUpK2Portn_Object = MibTableColumn
pm251dCtrllineUpK2Portn = _Pm251dCtrllineUpK2Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 3, 72, 1, 2),
    _Pm251dCtrllineUpK2Portn_Type()
)
pm251dCtrllineUpK2Portn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCtrllineUpK2Portn.setStatus("current")
_Pm251dCtrllineOosModeTable_Object = MibTable
pm251dCtrllineOosModeTable = _Pm251dCtrllineOosModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 3, 74)
)
if mibBuilder.loadTexts:
    pm251dCtrllineOosModeTable.setStatus("current")
_Pm251dCtrllineOosModeEntry_Object = MibTableRow
pm251dCtrllineOosModeEntry = _Pm251dCtrllineOosModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 3, 74, 1)
)
pm251dCtrllineOosModeEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dCtrllineOosModeIndex"),
)
if mibBuilder.loadTexts:
    pm251dCtrllineOosModeEntry.setStatus("current")


class _Pm251dCtrllineOosModeIndex_Type(Integer32):
    """Custom type pm251dCtrllineOosModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dCtrllineOosModeIndex_Type.__name__ = "Integer32"
_Pm251dCtrllineOosModeIndex_Object = MibTableColumn
pm251dCtrllineOosModeIndex = _Pm251dCtrllineOosModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 3, 74, 1, 1),
    _Pm251dCtrllineOosModeIndex_Type()
)
pm251dCtrllineOosModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCtrllineOosModeIndex.setStatus("current")
_Pm251dCtrllineOosModePortn_Type = EkiState
_Pm251dCtrllineOosModePortn_Object = MibTableColumn
pm251dCtrllineOosModePortn = _Pm251dCtrllineOosModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 3, 74, 1, 2),
    _Pm251dCtrllineOosModePortn_Type()
)
pm251dCtrllineOosModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCtrllineOosModePortn.setStatus("current")
_Pm251dCtrllineAccessLoopTable_Object = MibTable
pm251dCtrllineAccessLoopTable = _Pm251dCtrllineAccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 3, 160)
)
if mibBuilder.loadTexts:
    pm251dCtrllineAccessLoopTable.setStatus("current")
_Pm251dCtrllineAccessLoopEntry_Object = MibTableRow
pm251dCtrllineAccessLoopEntry = _Pm251dCtrllineAccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 3, 160, 1)
)
pm251dCtrllineAccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dCtrllineAccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pm251dCtrllineAccessLoopEntry.setStatus("current")


class _Pm251dCtrllineAccessLoopIndex_Type(Integer32):
    """Custom type pm251dCtrllineAccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dCtrllineAccessLoopIndex_Type.__name__ = "Integer32"
_Pm251dCtrllineAccessLoopIndex_Object = MibTableColumn
pm251dCtrllineAccessLoopIndex = _Pm251dCtrllineAccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 3, 160, 1, 1),
    _Pm251dCtrllineAccessLoopIndex_Type()
)
pm251dCtrllineAccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCtrllineAccessLoopIndex.setStatus("current")
_Pm251dCtrllineAccessLoopPortn_Type = EkiState
_Pm251dCtrllineAccessLoopPortn_Object = MibTableColumn
pm251dCtrllineAccessLoopPortn = _Pm251dCtrllineAccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 3, 160, 1, 2),
    _Pm251dCtrllineAccessLoopPortn_Type()
)
pm251dCtrllineAccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCtrllineAccessLoopPortn.setStatus("current")
_Pm251dCtrllineSfpOnOffCtrlTable_Object = MibTable
pm251dCtrllineSfpOnOffCtrlTable = _Pm251dCtrllineSfpOnOffCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 3, 162)
)
if mibBuilder.loadTexts:
    pm251dCtrllineSfpOnOffCtrlTable.setStatus("current")
_Pm251dCtrllineSfpOnOffCtrlEntry_Object = MibTableRow
pm251dCtrllineSfpOnOffCtrlEntry = _Pm251dCtrllineSfpOnOffCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 3, 162, 1)
)
pm251dCtrllineSfpOnOffCtrlEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dCtrllineSfpOnOffCtrlIndex"),
)
if mibBuilder.loadTexts:
    pm251dCtrllineSfpOnOffCtrlEntry.setStatus("current")


class _Pm251dCtrllineSfpOnOffCtrlIndex_Type(Integer32):
    """Custom type pm251dCtrllineSfpOnOffCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dCtrllineSfpOnOffCtrlIndex_Type.__name__ = "Integer32"
_Pm251dCtrllineSfpOnOffCtrlIndex_Object = MibTableColumn
pm251dCtrllineSfpOnOffCtrlIndex = _Pm251dCtrllineSfpOnOffCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 3, 162, 1, 1),
    _Pm251dCtrllineSfpOnOffCtrlIndex_Type()
)
pm251dCtrllineSfpOnOffCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCtrllineSfpOnOffCtrlIndex.setStatus("current")
_Pm251dCtrllineSfpOnOffCtrlPortn_Type = EkiState
_Pm251dCtrllineSfpOnOffCtrlPortn_Object = MibTableColumn
pm251dCtrllineSfpOnOffCtrlPortn = _Pm251dCtrllineSfpOnOffCtrlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 6, 3, 162, 1, 2),
    _Pm251dCtrllineSfpOnOffCtrlPortn_Type()
)
pm251dCtrllineSfpOnOffCtrlPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCtrllineSfpOnOffCtrlPortn.setStatus("current")
_Pm251dri_ObjectIdentity = ObjectIdentity
pm251dri = _Pm251dri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 7)
)
_Pm251driTable_ObjectIdentity = ObjectIdentity
pm251driTable = _Pm251driTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 7, 1)
)
_Pm251dRinvClientTable_Object = MibTable
pm251dRinvClientTable = _Pm251dRinvClientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 7, 1, 1)
)
if mibBuilder.loadTexts:
    pm251dRinvClientTable.setStatus("current")
_Pm251dRinvClientEntry_Object = MibTableRow
pm251dRinvClientEntry = _Pm251dRinvClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 7, 1, 1, 1)
)
pm251dRinvClientEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dRinvClientIndex"),
)
if mibBuilder.loadTexts:
    pm251dRinvClientEntry.setStatus("current")


class _Pm251dRinvClientIndex_Type(Integer32):
    """Custom type pm251dRinvClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm251dRinvClientIndex_Type.__name__ = "Integer32"
_Pm251dRinvClientIndex_Object = MibTableColumn
pm251dRinvClientIndex = _Pm251dRinvClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 7, 1, 1, 1, 1),
    _Pm251dRinvClientIndex_Type()
)
pm251dRinvClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dRinvClientIndex.setStatus("current")
_Pm251dRinvSfpClient_Type = DisplayString
_Pm251dRinvSfpClient_Object = MibTableColumn
pm251dRinvSfpClient = _Pm251dRinvSfpClient_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 7, 1, 1, 1, 2),
    _Pm251dRinvSfpClient_Type()
)
pm251dRinvSfpClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dRinvSfpClient.setStatus("current")
_Pm251dRinvLineTable_Object = MibTable
pm251dRinvLineTable = _Pm251dRinvLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pm251dRinvLineTable.setStatus("current")
_Pm251dRinvLineEntry_Object = MibTableRow
pm251dRinvLineEntry = _Pm251dRinvLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 7, 1, 2, 1)
)
pm251dRinvLineEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dRinvLineIndex"),
)
if mibBuilder.loadTexts:
    pm251dRinvLineEntry.setStatus("current")


class _Pm251dRinvLineIndex_Type(Integer32):
    """Custom type pm251dRinvLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm251dRinvLineIndex_Type.__name__ = "Integer32"
_Pm251dRinvLineIndex_Object = MibTableColumn
pm251dRinvLineIndex = _Pm251dRinvLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 7, 1, 2, 1, 1),
    _Pm251dRinvLineIndex_Type()
)
pm251dRinvLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dRinvLineIndex.setStatus("current")
_Pm251dRinvsfpLine_Type = DisplayString
_Pm251dRinvsfpLine_Object = MibTableColumn
pm251dRinvsfpLine = _Pm251dRinvsfpLine_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 7, 1, 2, 1, 2),
    _Pm251dRinvsfpLine_Type()
)
pm251dRinvsfpLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dRinvsfpLine.setStatus("current")


class _Pm251dRinvReloadInventory_Type(Integer32):
    """Custom type pm251dRinvReloadInventory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Pm251dRinvReloadInventory_Type.__name__ = "Integer32"
_Pm251dRinvReloadInventory_Object = MibScalar
pm251dRinvReloadInventory = _Pm251dRinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 7, 2),
    _Pm251dRinvReloadInventory_Type()
)
pm251dRinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dRinvReloadInventory.setStatus("current")
_Pm251dRinvHwPlatform_Type = DisplayString
_Pm251dRinvHwPlatform_Object = MibScalar
pm251dRinvHwPlatform = _Pm251dRinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 7, 3),
    _Pm251dRinvHwPlatform_Type()
)
pm251dRinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dRinvHwPlatform.setStatus("current")
_Pm251dRinvModulePlatform_Type = DisplayString
_Pm251dRinvModulePlatform_Object = MibScalar
pm251dRinvModulePlatform = _Pm251dRinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 7, 4),
    _Pm251dRinvModulePlatform_Type()
)
pm251dRinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dRinvModulePlatform.setStatus("current")
_Pm251dRinvSwPlatform_Type = DisplayString
_Pm251dRinvSwPlatform_Object = MibScalar
pm251dRinvSwPlatform = _Pm251dRinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 7, 5),
    _Pm251dRinvSwPlatform_Type()
)
pm251dRinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dRinvSwPlatform.setStatus("current")
_Pm251dRinvGwPlatform_Type = DisplayString
_Pm251dRinvGwPlatform_Object = MibScalar
pm251dRinvGwPlatform = _Pm251dRinvGwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 7, 6),
    _Pm251dRinvGwPlatform_Type()
)
pm251dRinvGwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dRinvGwPlatform.setStatus("current")
_Pm251ddownload_ObjectIdentity = ObjectIdentity
pm251ddownload = _Pm251ddownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 8)
)
_Pm251dDwlOther_ObjectIdentity = ObjectIdentity
pm251dDwlOther = _Pm251dDwlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 8, 1)
)
_Pm251dDwlrestartProcess_ObjectIdentity = ObjectIdentity
pm251dDwlrestartProcess = _Pm251dDwlrestartProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 8, 1, 0)
)
_Pm251dDwlWarmRestartProcessed_Type = EkiOnOff
_Pm251dDwlWarmRestartProcessed_Object = MibScalar
pm251dDwlWarmRestartProcessed = _Pm251dDwlWarmRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 8, 1, 0, 1),
    _Pm251dDwlWarmRestartProcessed_Type()
)
pm251dDwlWarmRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dDwlWarmRestartProcessed.setStatus("current")
_Pm251dDwlColdRestartProcessed_Type = EkiOnOff
_Pm251dDwlColdRestartProcessed_Object = MibScalar
pm251dDwlColdRestartProcessed = _Pm251dDwlColdRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 8, 1, 0, 2),
    _Pm251dDwlColdRestartProcessed_Type()
)
pm251dDwlColdRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dDwlColdRestartProcessed.setStatus("current")
_Pm251dDwlswBanksUsed_ObjectIdentity = ObjectIdentity
pm251dDwlswBanksUsed = _Pm251dDwlswBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 8, 1, 1)
)
_Pm251dDwlSwBank1Used_Type = EkiOnOff
_Pm251dDwlSwBank1Used_Object = MibScalar
pm251dDwlSwBank1Used = _Pm251dDwlSwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 8, 1, 1, 1),
    _Pm251dDwlSwBank1Used_Type()
)
pm251dDwlSwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dDwlSwBank1Used.setStatus("current")
_Pm251dDwlSwBank2Used_Type = EkiOnOff
_Pm251dDwlSwBank2Used_Object = MibScalar
pm251dDwlSwBank2Used = _Pm251dDwlSwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 8, 1, 1, 2),
    _Pm251dDwlSwBank2Used_Type()
)
pm251dDwlSwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dDwlSwBank2Used.setStatus("current")
_Pm251dDwlSwBank1Notempty_Type = EkiOnOff
_Pm251dDwlSwBank1Notempty_Object = MibScalar
pm251dDwlSwBank1Notempty = _Pm251dDwlSwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 8, 1, 1, 5),
    _Pm251dDwlSwBank1Notempty_Type()
)
pm251dDwlSwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dDwlSwBank1Notempty.setStatus("current")
_Pm251dDwlSwBank2Notempty_Type = EkiOnOff
_Pm251dDwlSwBank2Notempty_Object = MibScalar
pm251dDwlSwBank2Notempty = _Pm251dDwlSwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 8, 1, 1, 6),
    _Pm251dDwlSwBank2Notempty_Type()
)
pm251dDwlSwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dDwlSwBank2Notempty.setStatus("current")
_Pm251dDwlgwBanksUsed_ObjectIdentity = ObjectIdentity
pm251dDwlgwBanksUsed = _Pm251dDwlgwBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 8, 1, 2)
)
_Pm251dDwlGwBank1Used_Type = EkiOnOff
_Pm251dDwlGwBank1Used_Object = MibScalar
pm251dDwlGwBank1Used = _Pm251dDwlGwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 8, 1, 2, 1),
    _Pm251dDwlGwBank1Used_Type()
)
pm251dDwlGwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dDwlGwBank1Used.setStatus("current")
_Pm251dDwlGwBank2Used_Type = EkiOnOff
_Pm251dDwlGwBank2Used_Object = MibScalar
pm251dDwlGwBank2Used = _Pm251dDwlGwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 8, 1, 2, 2),
    _Pm251dDwlGwBank2Used_Type()
)
pm251dDwlGwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dDwlGwBank2Used.setStatus("current")
_Pm251dDwlGwBank3Used_Type = EkiOnOff
_Pm251dDwlGwBank3Used_Object = MibScalar
pm251dDwlGwBank3Used = _Pm251dDwlGwBank3Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 8, 1, 2, 3),
    _Pm251dDwlGwBank3Used_Type()
)
pm251dDwlGwBank3Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dDwlGwBank3Used.setStatus("current")
_Pm251dDwlGwBank4Used_Type = EkiOnOff
_Pm251dDwlGwBank4Used_Object = MibScalar
pm251dDwlGwBank4Used = _Pm251dDwlGwBank4Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 8, 1, 2, 4),
    _Pm251dDwlGwBank4Used_Type()
)
pm251dDwlGwBank4Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dDwlGwBank4Used.setStatus("current")
_Pm251dDwlGwBank1Notempty_Type = EkiOnOff
_Pm251dDwlGwBank1Notempty_Object = MibScalar
pm251dDwlGwBank1Notempty = _Pm251dDwlGwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 8, 1, 2, 5),
    _Pm251dDwlGwBank1Notempty_Type()
)
pm251dDwlGwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dDwlGwBank1Notempty.setStatus("current")
_Pm251dDwlGwBank2Notempty_Type = EkiOnOff
_Pm251dDwlGwBank2Notempty_Object = MibScalar
pm251dDwlGwBank2Notempty = _Pm251dDwlGwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 8, 1, 2, 6),
    _Pm251dDwlGwBank2Notempty_Type()
)
pm251dDwlGwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dDwlGwBank2Notempty.setStatus("current")
_Pm251dDwlGwBank3Notempty_Type = EkiOnOff
_Pm251dDwlGwBank3Notempty_Object = MibScalar
pm251dDwlGwBank3Notempty = _Pm251dDwlGwBank3Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 8, 1, 2, 7),
    _Pm251dDwlGwBank3Notempty_Type()
)
pm251dDwlGwBank3Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dDwlGwBank3Notempty.setStatus("current")
_Pm251dDwlGwBank4Notempty_Type = EkiOnOff
_Pm251dDwlGwBank4Notempty_Object = MibScalar
pm251dDwlGwBank4Notempty = _Pm251dDwlGwBank4Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 8, 1, 2, 8),
    _Pm251dDwlGwBank4Notempty_Type()
)
pm251dDwlGwBank4Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dDwlGwBank4Notempty.setStatus("current")
_Pm251dDwlPort_ObjectIdentity = ObjectIdentity
pm251dDwlPort = _Pm251dDwlPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 8, 2)
)
_Pm251dDwlLine_ObjectIdentity = ObjectIdentity
pm251dDwlLine = _Pm251dDwlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 8, 3)
)
_Pm251dConfig_ObjectIdentity = ObjectIdentity
pm251dConfig = _Pm251dConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 9)
)
_Pm251dCfgAccessCAisCsf_ObjectIdentity = ObjectIdentity
pm251dCfgAccessCAisCsf = _Pm251dCfgAccessCAisCsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 9, 1)
)
_Pm251dCfgClientcaiscsfTable_Object = MibTable
pm251dCfgClientcaiscsfTable = _Pm251dCfgClientcaiscsfTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 9, 1, 1)
)
if mibBuilder.loadTexts:
    pm251dCfgClientcaiscsfTable.setStatus("current")
_Pm251dCfgClientcaiscsfEntry_Object = MibTableRow
pm251dCfgClientcaiscsfEntry = _Pm251dCfgClientcaiscsfEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 9, 1, 1, 1)
)
pm251dCfgClientcaiscsfEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dCfgClientcaiscsfIndex"),
)
if mibBuilder.loadTexts:
    pm251dCfgClientcaiscsfEntry.setStatus("current")


class _Pm251dCfgClientcaiscsfIndex_Type(Integer32):
    """Custom type pm251dCfgClientcaiscsfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dCfgClientcaiscsfIndex_Type.__name__ = "Integer32"
_Pm251dCfgClientcaiscsfIndex_Object = MibTableColumn
pm251dCfgClientcaiscsfIndex = _Pm251dCfgClientcaiscsfIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 9, 1, 1, 1, 1),
    _Pm251dCfgClientcaiscsfIndex_Type()
)
pm251dCfgClientcaiscsfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCfgClientcaiscsfIndex.setStatus("current")


class _Pm251dCfgCAisModePortn_Type(Unsigned32):
    """Custom type pm251dCfgCAisModePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm251dCfgCAisModePortn_Type.__name__ = "Unsigned32"
_Pm251dCfgCAisModePortn_Object = MibTableColumn
pm251dCfgCAisModePortn = _Pm251dCfgCAisModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 9, 1, 1, 1, 3),
    _Pm251dCfgCAisModePortn_Type()
)
pm251dCfgCAisModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCfgCAisModePortn.setStatus("current")


class _Pm251dCfgSts24cContribPortn_Type(Unsigned32):
    """Custom type pm251dCfgSts24cContribPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm251dCfgSts24cContribPortn_Type.__name__ = "Unsigned32"
_Pm251dCfgSts24cContribPortn_Object = MibTableColumn
pm251dCfgSts24cContribPortn = _Pm251dCfgSts24cContribPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 9, 1, 1, 1, 4),
    _Pm251dCfgSts24cContribPortn_Type()
)
pm251dCfgSts24cContribPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCfgSts24cContribPortn.setStatus("current")


class _Pm251dCfgUpAccessioAlmPortn_Type(Unsigned32):
    """Custom type pm251dCfgUpAccessioAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm251dCfgUpAccessioAlmPortn_Type.__name__ = "Unsigned32"
_Pm251dCfgUpAccessioAlmPortn_Object = MibTableColumn
pm251dCfgUpAccessioAlmPortn = _Pm251dCfgUpAccessioAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 9, 1, 1, 1, 9),
    _Pm251dCfgUpAccessioAlmPortn_Type()
)
pm251dCfgUpAccessioAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCfgUpAccessioAlmPortn.setStatus("current")


class _Pm251dCfgUpMapperDeAlmPortn_Type(Unsigned32):
    """Custom type pm251dCfgUpMapperDeAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm251dCfgUpMapperDeAlmPortn_Type.__name__ = "Unsigned32"
_Pm251dCfgUpMapperDeAlmPortn_Object = MibTableColumn
pm251dCfgUpMapperDeAlmPortn = _Pm251dCfgUpMapperDeAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 9, 1, 1, 1, 10),
    _Pm251dCfgUpMapperDeAlmPortn_Type()
)
pm251dCfgUpMapperDeAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCfgUpMapperDeAlmPortn.setStatus("current")


class _Pm251dCfgDownMapperDeAlmPortn_Type(Unsigned32):
    """Custom type pm251dCfgDownMapperDeAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm251dCfgDownMapperDeAlmPortn_Type.__name__ = "Unsigned32"
_Pm251dCfgDownMapperDeAlmPortn_Object = MibTableColumn
pm251dCfgDownMapperDeAlmPortn = _Pm251dCfgDownMapperDeAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 9, 1, 1, 1, 18),
    _Pm251dCfgDownMapperDeAlmPortn_Type()
)
pm251dCfgDownMapperDeAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCfgDownMapperDeAlmPortn.setStatus("current")


class _Pm251dCfgDownDfrmAlmPortn_Type(Unsigned32):
    """Custom type pm251dCfgDownDfrmAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm251dCfgDownDfrmAlmPortn_Type.__name__ = "Unsigned32"
_Pm251dCfgDownDfrmAlmPortn_Object = MibTableColumn
pm251dCfgDownDfrmAlmPortn = _Pm251dCfgDownDfrmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 9, 1, 1, 1, 19),
    _Pm251dCfgDownDfrmAlmPortn_Type()
)
pm251dCfgDownDfrmAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCfgDownDfrmAlmPortn.setStatus("current")


class _Pm251dCfgDownLineIoAlmPortn_Type(Unsigned32):
    """Custom type pm251dCfgDownLineIoAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm251dCfgDownLineIoAlmPortn_Type.__name__ = "Unsigned32"
_Pm251dCfgDownLineIoAlmPortn_Object = MibTableColumn
pm251dCfgDownLineIoAlmPortn = _Pm251dCfgDownLineIoAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 9, 1, 1, 1, 22),
    _Pm251dCfgDownLineIoAlmPortn_Type()
)
pm251dCfgDownLineIoAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCfgDownLineIoAlmPortn.setStatus("deprecated")
_Pm251dCfgStartup_ObjectIdentity = ObjectIdentity
pm251dCfgStartup = _Pm251dCfgStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 9, 2)
)
_Pm251dCfgClientStartupTable_Object = MibTable
pm251dCfgClientStartupTable = _Pm251dCfgClientStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 9, 2, 1)
)
if mibBuilder.loadTexts:
    pm251dCfgClientStartupTable.setStatus("current")
_Pm251dCfgClientStartupEntry_Object = MibTableRow
pm251dCfgClientStartupEntry = _Pm251dCfgClientStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 9, 2, 1, 1)
)
pm251dCfgClientStartupEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dCfgClientStartupIndex"),
)
if mibBuilder.loadTexts:
    pm251dCfgClientStartupEntry.setStatus("current")


class _Pm251dCfgClientStartupIndex_Type(Integer32):
    """Custom type pm251dCfgClientStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dCfgClientStartupIndex_Type.__name__ = "Integer32"
_Pm251dCfgClientStartupIndex_Object = MibTableColumn
pm251dCfgClientStartupIndex = _Pm251dCfgClientStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 9, 2, 1, 1, 1),
    _Pm251dCfgClientStartupIndex_Type()
)
pm251dCfgClientStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCfgClientStartupIndex.setStatus("current")


class _Pm251dCfgSystConfPortPortn_Type(Unsigned32):
    """Custom type pm251dCfgSystConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm251dCfgSystConfPortPortn_Type.__name__ = "Unsigned32"
_Pm251dCfgSystConfPortPortn_Object = MibTableColumn
pm251dCfgSystConfPortPortn = _Pm251dCfgSystConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 9, 2, 1, 1, 3),
    _Pm251dCfgSystConfPortPortn_Type()
)
pm251dCfgSystConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCfgSystConfPortPortn.setStatus("current")


class _Pm251dCfgNetConfPortPortn_Type(Unsigned32):
    """Custom type pm251dCfgNetConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm251dCfgNetConfPortPortn_Type.__name__ = "Unsigned32"
_Pm251dCfgNetConfPortPortn_Object = MibTableColumn
pm251dCfgNetConfPortPortn = _Pm251dCfgNetConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 9, 2, 1, 1, 4),
    _Pm251dCfgNetConfPortPortn_Type()
)
pm251dCfgNetConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCfgNetConfPortPortn.setStatus("current")


class _Pm251dCfgPortsOptionsPortn_Type(Unsigned32):
    """Custom type pm251dCfgPortsOptionsPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm251dCfgPortsOptionsPortn_Type.__name__ = "Unsigned32"
_Pm251dCfgPortsOptionsPortn_Object = MibTableColumn
pm251dCfgPortsOptionsPortn = _Pm251dCfgPortsOptionsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 9, 2, 1, 1, 6),
    _Pm251dCfgPortsOptionsPortn_Type()
)
pm251dCfgPortsOptionsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCfgPortsOptionsPortn.setStatus("deprecated")
_Pm251dtablelineStartup_ObjectIdentity = ObjectIdentity
pm251dtablelineStartup = _Pm251dtablelineStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 9, 2, 2)
)


class _Pm251dCfgsystConfLine1_Type(Unsigned32):
    """Custom type pm251dCfgsystConfLine1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm251dCfgsystConfLine1_Type.__name__ = "Unsigned32"
_Pm251dCfgsystConfLine1_Object = MibScalar
pm251dCfgsystConfLine1 = _Pm251dCfgsystConfLine1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 9, 2, 2, 2),
    _Pm251dCfgsystConfLine1_Type()
)
pm251dCfgsystConfLine1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCfgsystConfLine1.setStatus("current")


class _Pm251dCfglineOptions1_Type(Unsigned32):
    """Custom type pm251dCfglineOptions1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm251dCfglineOptions1_Type.__name__ = "Unsigned32"
_Pm251dCfglineOptions1_Object = MibScalar
pm251dCfglineOptions1 = _Pm251dCfglineOptions1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 9, 2, 2, 5),
    _Pm251dCfglineOptions1_Type()
)
pm251dCfglineOptions1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCfglineOptions1.setStatus("current")


class _Pm251dCfgsystConfLine2_Type(Unsigned32):
    """Custom type pm251dCfgsystConfLine2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm251dCfgsystConfLine2_Type.__name__ = "Unsigned32"
_Pm251dCfgsystConfLine2_Object = MibScalar
pm251dCfgsystConfLine2 = _Pm251dCfgsystConfLine2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 9, 2, 2, 6),
    _Pm251dCfgsystConfLine2_Type()
)
pm251dCfgsystConfLine2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCfgsystConfLine2.setStatus("current")


class _Pm251dCfglineSelection_Type(Unsigned32):
    """Custom type pm251dCfglineSelection based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm251dCfglineSelection_Type.__name__ = "Unsigned32"
_Pm251dCfglineSelection_Object = MibScalar
pm251dCfglineSelection = _Pm251dCfglineSelection_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 9, 2, 2, 7),
    _Pm251dCfglineSelection_Type()
)
pm251dCfglineSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCfglineSelection.setStatus("current")


class _Pm251dCfglineOptions2_Type(Unsigned32):
    """Custom type pm251dCfglineOptions2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm251dCfglineOptions2_Type.__name__ = "Unsigned32"
_Pm251dCfglineOptions2_Object = MibScalar
pm251dCfglineOptions2 = _Pm251dCfglineOptions2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 9, 2, 2, 9),
    _Pm251dCfglineOptions2_Type()
)
pm251dCfglineOptions2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCfglineOptions2.setStatus("current")
_Pm251dCfgLabels_ObjectIdentity = ObjectIdentity
pm251dCfgLabels = _Pm251dCfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 9, 3)
)
_Pm251dCfgLabelclientTable_Object = MibTable
pm251dCfgLabelclientTable = _Pm251dCfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 9, 3, 1)
)
if mibBuilder.loadTexts:
    pm251dCfgLabelclientTable.setStatus("current")
_Pm251dCfgLabelclientEntry_Object = MibTableRow
pm251dCfgLabelclientEntry = _Pm251dCfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 9, 3, 1, 1)
)
pm251dCfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dCfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pm251dCfgLabelclientEntry.setStatus("current")


class _Pm251dCfgLabelclientIndex_Type(Integer32):
    """Custom type pm251dCfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dCfgLabelclientIndex_Type.__name__ = "Integer32"
_Pm251dCfgLabelclientIndex_Object = MibTableColumn
pm251dCfgLabelclientIndex = _Pm251dCfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 9, 3, 1, 1, 1),
    _Pm251dCfgLabelclientIndex_Type()
)
pm251dCfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCfgLabelclientIndex.setStatus("current")


class _Pm251dCfgLabelclientPortn_Type(DisplayString):
    """Custom type pm251dCfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm251dCfgLabelclientPortn_Type.__name__ = "DisplayString"
_Pm251dCfgLabelclientPortn_Object = MibTableColumn
pm251dCfgLabelclientPortn = _Pm251dCfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 9, 3, 1, 1, 3),
    _Pm251dCfgLabelclientPortn_Type()
)
pm251dCfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCfgLabelclientPortn.setStatus("current")
_Pm251dCfgLabellineTable_Object = MibTable
pm251dCfgLabellineTable = _Pm251dCfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 9, 3, 2)
)
if mibBuilder.loadTexts:
    pm251dCfgLabellineTable.setStatus("current")
_Pm251dCfgLabellineEntry_Object = MibTableRow
pm251dCfgLabellineEntry = _Pm251dCfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 9, 3, 2, 1)
)
pm251dCfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-Pm251d-MIB", "pm251dCfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pm251dCfgLabellineEntry.setStatus("current")


class _Pm251dCfgLabellineIndex_Type(Integer32):
    """Custom type pm251dCfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm251dCfgLabellineIndex_Type.__name__ = "Integer32"
_Pm251dCfgLabellineIndex_Object = MibTableColumn
pm251dCfgLabellineIndex = _Pm251dCfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 9, 3, 2, 1, 1),
    _Pm251dCfgLabellineIndex_Type()
)
pm251dCfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dCfgLabellineIndex.setStatus("current")


class _Pm251dCfgLabellinePortn_Type(DisplayString):
    """Custom type pm251dCfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm251dCfgLabellinePortn_Type.__name__ = "DisplayString"
_Pm251dCfgLabellinePortn_Object = MibTableColumn
pm251dCfgLabellinePortn = _Pm251dCfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 9, 3, 2, 1, 3),
    _Pm251dCfgLabellinePortn_Type()
)
pm251dCfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCfgLabellinePortn.setStatus("current")
_Pm251dCfgWriteConfiguration_Type = EkiOnOff
_Pm251dCfgWriteConfiguration_Object = MibScalar
pm251dCfgWriteConfiguration = _Pm251dCfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 9, 257),
    _Pm251dCfgWriteConfiguration_Type()
)
pm251dCfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm251dCfgWriteConfiguration.setStatus("current")
_Pm251dtraps_ObjectIdentity = ObjectIdentity
pm251dtraps = _Pm251dtraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 10)
)


class _Pm251dTrapPortNumber_Type(Integer32):
    """Custom type pm251dTrapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm251dTrapPortNumber_Type.__name__ = "Integer32"
_Pm251dTrapPortNumber_Object = MibScalar
pm251dTrapPortNumber = _Pm251dTrapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 10, 2),
    _Pm251dTrapPortNumber_Type()
)
pm251dTrapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dTrapPortNumber.setStatus("current")


class _Pm251dTrapBoardNumber_Type(Integer32):
    """Custom type pm251dTrapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm251dTrapBoardNumber_Type.__name__ = "Integer32"
_Pm251dTrapBoardNumber_Object = MibScalar
pm251dTrapBoardNumber = _Pm251dTrapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 10, 3),
    _Pm251dTrapBoardNumber_Type()
)
pm251dTrapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dTrapBoardNumber.setStatus("current")


class _Pm251dTrapLineNumber_Type(Integer32):
    """Custom type pm251dTrapLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm251dTrapLineNumber_Type.__name__ = "Integer32"
_Pm251dTrapLineNumber_Object = MibScalar
pm251dTrapLineNumber = _Pm251dTrapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 31, 10, 4),
    _Pm251dTrapLineNumber_Type()
)
pm251dTrapLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm251dTrapLineNumber.setStatus("current")
_Pm251dMonitoring_ObjectIdentity = ObjectIdentity
pm251dMonitoring = _Pm251dMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 11)
)
_Pm251dMonOther_ObjectIdentity = ObjectIdentity
pm251dMonOther = _Pm251dMonOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 11, 1)
)
_Pm251dMonRmon_ObjectIdentity = ObjectIdentity
pm251dMonRmon = _Pm251dMonRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 11, 1, 3)
)
_Pm251dMonClient_ObjectIdentity = ObjectIdentity
pm251dMonClient = _Pm251dMonClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 11, 2)
)
_Pm251dMonClientRmonCounter_ObjectIdentity = ObjectIdentity
pm251dMonClientRmonCounter = _Pm251dMonClientRmonCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 31, 11, 2, 4)
)

# Managed Objects groups


# Notification objects

pm251dLineTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 31, 10, 30)
)
pm251dLineTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm251d-MIB", "pm251dAlmLineDdmWarningPortn"),
        ("EKINOPS-Pm251d-MIB", "pm251dTrapLineNumber"),
        ("EKINOPS-Pm251d-MIB", "pm251dTrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm251dLineTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm251dLineTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 31, 10, 31)
)
pm251dLineTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm251d-MIB", "pm251dAlmLineDdmWarningPortn"),
        ("EKINOPS-Pm251d-MIB", "pm251dTrapLineNumber"),
        ("EKINOPS-Pm251d-MIB", "pm251dTrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm251dLineTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm251dLineTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 31, 10, 32)
)
pm251dLineTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm251d-MIB", "pm251dAlmLineDdmAlmPortn"),
        ("EKINOPS-Pm251d-MIB", "pm251dTrapLineNumber"),
        ("EKINOPS-Pm251d-MIB", "pm251dTrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm251dLineTrapUrgentGoesOn.setStatus(
        "current"
    )

pm251dLineTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 31, 10, 33)
)
pm251dLineTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm251d-MIB", "pm251dAlmLineDdmAlmPortn"),
        ("EKINOPS-Pm251d-MIB", "pm251dTrapLineNumber"),
        ("EKINOPS-Pm251d-MIB", "pm251dTrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm251dLineTrapUrgentGoesOff.setStatus(
        "current"
    )

pm251dLineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 31, 10, 34)
)
pm251dLineTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm251d-MIB", "pm251dAlmLineFailPortn"),
        ("EKINOPS-Pm251d-MIB", "pm251dAlmLineHwFailPortn"),
        ("EKINOPS-Pm251d-MIB", "pm251dTrapLineNumber"),
        ("EKINOPS-Pm251d-MIB", "pm251dTrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm251dLineTrapCritGoesOn.setStatus(
        "current"
    )

pm251dLineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 31, 10, 35)
)
pm251dLineTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm251d-MIB", "pm251dAlmLineFailPortn"),
        ("EKINOPS-Pm251d-MIB", "pm251dAlmLineHwFailPortn"),
        ("EKINOPS-Pm251d-MIB", "pm251dTrapLineNumber"),
        ("EKINOPS-Pm251d-MIB", "pm251dTrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm251dLineTrapCritGoesOff.setStatus(
        "current"
    )

pm251dClientTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 31, 10, 40)
)
pm251dClientTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm251d-MIB", "pm251dAlmClientSfpDdmWarningPortn"),
        ("EKINOPS-Pm251d-MIB", "pm251dTrapPortNumber"),
        ("EKINOPS-Pm251d-MIB", "pm251dTrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm251dClientTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm251dClientTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 31, 10, 41)
)
pm251dClientTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm251d-MIB", "pm251dAlmClientSfpDdmWarningPortn"),
        ("EKINOPS-Pm251d-MIB", "pm251dTrapPortNumber"),
        ("EKINOPS-Pm251d-MIB", "pm251dTrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm251dClientTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm251dClientTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 31, 10, 42)
)
pm251dClientTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm251d-MIB", "pm251dAlmClientSfpDdmAlmPortn"),
        ("EKINOPS-Pm251d-MIB", "pm251dTrapPortNumber"),
        ("EKINOPS-Pm251d-MIB", "pm251dTrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm251dClientTrapUrgentGoesOn.setStatus(
        "current"
    )

pm251dClientTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 31, 10, 43)
)
pm251dClientTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm251d-MIB", "pm251dAlmClientSfpDdmAlmPortn"),
        ("EKINOPS-Pm251d-MIB", "pm251dTrapPortNumber"),
        ("EKINOPS-Pm251d-MIB", "pm251dTrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm251dClientTrapUrgentGoesOff.setStatus(
        "current"
    )

pm251dClientTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 31, 10, 44)
)
pm251dClientTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm251d-MIB", "pm251dAlmClientFailAccPortn"),
        ("EKINOPS-Pm251d-MIB", "pm251dAlmClientHwFailAccPortn"),
        ("EKINOPS-Pm251d-MIB", "pm251dTrapPortNumber"),
        ("EKINOPS-Pm251d-MIB", "pm251dTrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm251dClientTrapCritGoesOn.setStatus(
        "current"
    )

pm251dClientTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 31, 10, 45)
)
pm251dClientTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm251d-MIB", "pm251dAlmClientFailAccPortn"),
        ("EKINOPS-Pm251d-MIB", "pm251dAlmClientHwFailAccPortn"),
        ("EKINOPS-Pm251d-MIB", "pm251dTrapPortNumber"),
        ("EKINOPS-Pm251d-MIB", "pm251dTrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm251dClientTrapCritGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Pm251d-MIB",
    **{"modulePm251d": modulePm251d,
       "pm251dalarms": pm251dalarms,
       "pm251dAlmOther": pm251dAlmOther,
       "pm251dAlmOtherNurg": pm251dAlmOtherNurg,
       "pm251dAlmsynthAlm0": pm251dAlmsynthAlm0,
       "pm251dAlmModGlobFail": pm251dAlmModGlobFail,
       "pm251dAlmDefFuseA": pm251dAlmDefFuseA,
       "pm251dAlmDefFuseB": pm251dAlmDefFuseB,
       "pm251dAlmsynthAlm2": pm251dAlmsynthAlm2,
       "pm251dAlmConfTableSave": pm251dAlmConfTableSave,
       "pm251dAlmInvUpload": pm251dAlmInvUpload,
       "pm251dAlmConfTableLoad": pm251dAlmConfTableLoad,
       "pm251dAlmCorrelatOff": pm251dAlmCorrelatOff,
       "pm251dAlmMaintenanceOn": pm251dAlmMaintenanceOn,
       "pm251dAlmOtherUrg": pm251dAlmOtherUrg,
       "pm251dAlmmodInitFailLevel2": pm251dAlmmodInitFailLevel2,
       "pm251dAlmLedFail": pm251dAlmLedFail,
       "pm251dAlmNextColdBootForced": pm251dAlmNextColdBootForced,
       "pm251dAlmBootUndone": pm251dAlmBootUndone,
       "pm251dAlmResetHwInitFail": pm251dAlmResetHwInitFail,
       "pm251dAlmSwInitFail": pm251dAlmSwInitFail,
       "pm251dAlmmodInitFailLevel3": pm251dAlmmodInitFailLevel3,
       "pm251dAlmGwIdentFail": pm251dAlmGwIdentFail,
       "pm251dAlmObmTypeReadFail": pm251dAlmObmTypeReadFail,
       "pm251dAlmInitModuleFail": pm251dAlmInitModuleFail,
       "pm251dAlmSfp1InitFail": pm251dAlmSfp1InitFail,
       "pm251dAlmSfp2InitFail": pm251dAlmSfp2InitFail,
       "pm251dAlmLine1InitFail": pm251dAlmLine1InitFail,
       "pm251dAlmLine2InitFail": pm251dAlmLine2InitFail,
       "pm251dAlmClient1InitFail": pm251dAlmClient1InitFail,
       "pm251dAlmClient2InitFail": pm251dAlmClient2InitFail,
       "pm251dAlmOtherCrit": pm251dAlmOtherCrit,
       "pm251dAlmPort": pm251dAlmPort,
       "pm251dAlmPortNurg": pm251dAlmPortNurg,
       "pm251dAlmclientSfpWarnDdmTable": pm251dAlmclientSfpWarnDdmTable,
       "pm251dAlmclientSfpWarnDdmEntry": pm251dAlmclientSfpWarnDdmEntry,
       "pm251dAlmclientSfpWarnDdmIndex": pm251dAlmclientSfpWarnDdmIndex,
       "pm251dAlmClientTxPwLowWngPortn": pm251dAlmClientTxPwLowWngPortn,
       "pm251dAlmClientTxPwrHighWngPortn": pm251dAlmClientTxPwrHighWngPortn,
       "pm251dAlmClientTxBiasLowWngPortn": pm251dAlmClientTxBiasLowWngPortn,
       "pm251dAlmClientTxBiasHighWngPortn": pm251dAlmClientTxBiasHighWngPortn,
       "pm251dAlmClientVccLowWngPortn": pm251dAlmClientVccLowWngPortn,
       "pm251dAlmClientVccHighWngPortn": pm251dAlmClientVccHighWngPortn,
       "pm251dAlmClientTempLowWngPortn": pm251dAlmClientTempLowWngPortn,
       "pm251dAlmClientTempHighWngPortn": pm251dAlmClientTempHighWngPortn,
       "pm251dAlmClientRxPwrLowWngPortn": pm251dAlmClientRxPwrLowWngPortn,
       "pm251dAlmClientRxPwrHighWngPortn": pm251dAlmClientRxPwrHighWngPortn,
       "pm251dAlmPortUrg": pm251dAlmPortUrg,
       "pm251dAlmclientSfpAlmDdmTable": pm251dAlmclientSfpAlmDdmTable,
       "pm251dAlmclientSfpAlmDdmEntry": pm251dAlmclientSfpAlmDdmEntry,
       "pm251dAlmclientSfpAlmDdmIndex": pm251dAlmclientSfpAlmDdmIndex,
       "pm251dAlmClientTxPwrLowAlaPortn": pm251dAlmClientTxPwrLowAlaPortn,
       "pm251dAlmClientTxPwrHighAlaPortn": pm251dAlmClientTxPwrHighAlaPortn,
       "pm251dAlmClientTxBiasLowAlaPortn": pm251dAlmClientTxBiasLowAlaPortn,
       "pm251dAlmClientTxBiasHighAlaPortn": pm251dAlmClientTxBiasHighAlaPortn,
       "pm251dAlmClientVccLowAlaPortn": pm251dAlmClientVccLowAlaPortn,
       "pm251dAlmClientVccHighAlaPortn": pm251dAlmClientVccHighAlaPortn,
       "pm251dAlmClientTempLowAlaPortn": pm251dAlmClientTempLowAlaPortn,
       "pm251dAlmClientTempHighAlaPortn": pm251dAlmClientTempHighAlaPortn,
       "pm251dAlmClientRxPwrLowAlaPortn": pm251dAlmClientRxPwrLowAlaPortn,
       "pm251dAlmClientRxPwrHighAlaPortn": pm251dAlmClientRxPwrHighAlaPortn,
       "pm251dAlmPortCrit": pm251dAlmPortCrit,
       "pm251dAlmsynthAlmClientTable": pm251dAlmsynthAlmClientTable,
       "pm251dAlmsynthAlmClientEntry": pm251dAlmsynthAlmClientEntry,
       "pm251dAlmsynthAlmClientIndex": pm251dAlmsynthAlmClientIndex,
       "pm251dAlmClientSfpAbsentPortn": pm251dAlmClientSfpAbsentPortn,
       "pm251dAlmClientDdmAbsentPortn": pm251dAlmClientDdmAbsentPortn,
       "pm251dAlmClientHwFailAccPortn": pm251dAlmClientHwFailAccPortn,
       "pm251dAlmClientLsdPortn": pm251dAlmClientLsdPortn,
       "pm251dAlmClientLocalOosPortn": pm251dAlmClientLocalOosPortn,
       "pm251dAlmClientRemoteOosPortn": pm251dAlmClientRemoteOosPortn,
       "pm251dAlmClientDwCaisPortn": pm251dAlmClientDwCaisPortn,
       "pm251dAlmClientSfpDdmWarningPortn": pm251dAlmClientSfpDdmWarningPortn,
       "pm251dAlmClientSfpDdmAlmPortn": pm251dAlmClientSfpDdmAlmPortn,
       "pm251dAlmClientFailAccPortn": pm251dAlmClientFailAccPortn,
       "pm251dAlmClientUpCsfPortn": pm251dAlmClientUpCsfPortn,
       "pm251dAlmaccessioAlmTable": pm251dAlmaccessioAlmTable,
       "pm251dAlmaccessioAlmEntry": pm251dAlmaccessioAlmEntry,
       "pm251dAlmaccessioAlmIndex": pm251dAlmaccessioAlmIndex,
       "pm251dAlmClientDwLasFailPortn": pm251dAlmClientDwLasFailPortn,
       "pm251dAlmClientUpLosPortn": pm251dAlmClientUpLosPortn,
       "pm251dAlmclientMapperDeAlmTable": pm251dAlmclientMapperDeAlmTable,
       "pm251dAlmclientMapperDeAlmEntry": pm251dAlmclientMapperDeAlmEntry,
       "pm251dAlmclientMapperDeAlmIndex": pm251dAlmclientMapperDeAlmIndex,
       "pm251dAlmClientUpAccOosPortn": pm251dAlmClientUpAccOosPortn,
       "pm251dAlmClientUpBufferOvlPortn": pm251dAlmClientUpBufferOvlPortn,
       "pm251dAlmClientDwCsfDetPortn": pm251dAlmClientDwCsfDetPortn,
       "pm251dAlmClientDwBufferOvlPortn": pm251dAlmClientDwBufferOvlPortn,
       "pm251dAlmClientLoopAccFifoFailPortn": pm251dAlmClientLoopAccFifoFailPortn,
       "pm251dAlmaccessioSdhAlarmTable": pm251dAlmaccessioSdhAlarmTable,
       "pm251dAlmaccessioSdhAlarmEntry": pm251dAlmaccessioSdhAlarmEntry,
       "pm251dAlmaccessioSdhAlarmIndex": pm251dAlmaccessioSdhAlarmIndex,
       "pm251dAlmLosTrscPortn": pm251dAlmLosTrscPortn,
       "pm251dAlmFifoErrPortn": pm251dAlmFifoErrPortn,
       "pm251dAlmRxLossOfLockPortn": pm251dAlmRxLossOfLockPortn,
       "pm251dAlmTxLossOfLockPortn": pm251dAlmTxLossOfLockPortn,
       "pm251dAlmClientAisDetPortn": pm251dAlmClientAisDetPortn,
       "pm251dAlmClientRdiDetPortn": pm251dAlmClientRdiDetPortn,
       "pm251dAlmClientOofPortn": pm251dAlmClientOofPortn,
       "pm251dAlmLine": pm251dAlmLine,
       "pm251dAlmLineNurg": pm251dAlmLineNurg,
       "pm251dAlmlineDownS1Table": pm251dAlmlineDownS1Table,
       "pm251dAlmlineDownS1Entry": pm251dAlmlineDownS1Entry,
       "pm251dAlmlineDownS1Index": pm251dAlmlineDownS1Index,
       "pm251dAlmlineDownS1Portn": pm251dAlmlineDownS1Portn,
       "pm251dAlmlineDownK1Table": pm251dAlmlineDownK1Table,
       "pm251dAlmlineDownK1Entry": pm251dAlmlineDownK1Entry,
       "pm251dAlmlineDownK1Index": pm251dAlmlineDownK1Index,
       "pm251dAlmlineDownK1Portn": pm251dAlmlineDownK1Portn,
       "pm251dAlmlineDownK2Table": pm251dAlmlineDownK2Table,
       "pm251dAlmlineDownK2Entry": pm251dAlmlineDownK2Entry,
       "pm251dAlmlineDownK2Index": pm251dAlmlineDownK2Index,
       "pm251dAlmlineDownK2Portn": pm251dAlmlineDownK2Portn,
       "pm251dAlmlineSfpWarnDdmTable": pm251dAlmlineSfpWarnDdmTable,
       "pm251dAlmlineSfpWarnDdmEntry": pm251dAlmlineSfpWarnDdmEntry,
       "pm251dAlmlineSfpWarnDdmIndex": pm251dAlmlineSfpWarnDdmIndex,
       "pm251dAlmLineTxPwLowWngPortn": pm251dAlmLineTxPwLowWngPortn,
       "pm251dAlmLineTxPwrHighWngPortn": pm251dAlmLineTxPwrHighWngPortn,
       "pm251dAlmLineTxBiasLowWngPortn": pm251dAlmLineTxBiasLowWngPortn,
       "pm251dAlmLineTxBiasHighWngPortn": pm251dAlmLineTxBiasHighWngPortn,
       "pm251dAlmLineVccLowWngPortn": pm251dAlmLineVccLowWngPortn,
       "pm251dAlmLineVccHighWngPortn": pm251dAlmLineVccHighWngPortn,
       "pm251dAlmLineTempLowWngPortn": pm251dAlmLineTempLowWngPortn,
       "pm251dAlmLineTempHighWngPortn": pm251dAlmLineTempHighWngPortn,
       "pm251dAlmLineRxPwrLowWngPortn": pm251dAlmLineRxPwrLowWngPortn,
       "pm251dAlmLineRxPwrHighWngPortn": pm251dAlmLineRxPwrHighWngPortn,
       "pm251dAlmLineUrg": pm251dAlmLineUrg,
       "pm251dAlmlineSfpAlaDdmTable": pm251dAlmlineSfpAlaDdmTable,
       "pm251dAlmlineSfpAlaDdmEntry": pm251dAlmlineSfpAlaDdmEntry,
       "pm251dAlmlineSfpAlaDdmIndex": pm251dAlmlineSfpAlaDdmIndex,
       "pm251dAlmLineTxPwrLowAlaPortn": pm251dAlmLineTxPwrLowAlaPortn,
       "pm251dAlmLineTxPwrHighAlaPortn": pm251dAlmLineTxPwrHighAlaPortn,
       "pm251dAlmLineTxBiasLowAlaPortn": pm251dAlmLineTxBiasLowAlaPortn,
       "pm251dAlmLineTxBiasHighAlaPortn": pm251dAlmLineTxBiasHighAlaPortn,
       "pm251dAlmLineVccLowAlaPortn": pm251dAlmLineVccLowAlaPortn,
       "pm251dAlmLineVccHighAlaPortn": pm251dAlmLineVccHighAlaPortn,
       "pm251dAlmLineTempLowAlaPortn": pm251dAlmLineTempLowAlaPortn,
       "pm251dAlmLineTempHighAlaPortn": pm251dAlmLineTempHighAlaPortn,
       "pm251dAlmLineRxPwrLowAlaPortn": pm251dAlmLineRxPwrLowAlaPortn,
       "pm251dAlmLineRxPwrHighAlaPortn": pm251dAlmLineRxPwrHighAlaPortn,
       "pm251dAlmLineCrit": pm251dAlmLineCrit,
       "pm251dAlmsynthAlmLineTable": pm251dAlmsynthAlmLineTable,
       "pm251dAlmsynthAlmLineEntry": pm251dAlmsynthAlmLineEntry,
       "pm251dAlmsynthAlmLineIndex": pm251dAlmsynthAlmLineIndex,
       "pm251dAlmLineSfpAbsentPortn": pm251dAlmLineSfpAbsentPortn,
       "pm251dAlmLineDdmAbsentPortn": pm251dAlmLineDdmAbsentPortn,
       "pm251dAlmLineHwFailPortn": pm251dAlmLineHwFailPortn,
       "pm251dAlmLineLsdPortn": pm251dAlmLineLsdPortn,
       "pm251dAlmLineLocalOosPortn": pm251dAlmLineLocalOosPortn,
       "pm251dAlmLineUpRdiInsPortn": pm251dAlmLineUpRdiInsPortn,
       "pm251dAlmLineDdmWarningPortn": pm251dAlmLineDdmWarningPortn,
       "pm251dAlmLineDdmAlmPortn": pm251dAlmLineDdmAlmPortn,
       "pm251dAlmLineFailPortn": pm251dAlmLineFailPortn,
       "pm251dAlmlineDfrmAlmTable": pm251dAlmlineDfrmAlmTable,
       "pm251dAlmlineDfrmAlmEntry": pm251dAlmlineDfrmAlmEntry,
       "pm251dAlmlineDfrmAlmIndex": pm251dAlmlineDfrmAlmIndex,
       "pm251dAlmLineDwAisDetPortn": pm251dAlmLineDwAisDetPortn,
       "pm251dAlmLineDwRdiDetPortn": pm251dAlmLineDwRdiDetPortn,
       "pm251dAlmLineDwOofPortn": pm251dAlmLineDwOofPortn,
       "pm251dAlmLineDwLofPortn": pm251dAlmLineDwLofPortn,
       "pm251dAlmlineIoAlmTable": pm251dAlmlineIoAlmTable,
       "pm251dAlmlineIoAlmEntry": pm251dAlmlineIoAlmEntry,
       "pm251dAlmlineIoAlmIndex": pm251dAlmlineIoAlmIndex,
       "pm251dAlmLineUpLasFailPortn": pm251dAlmLineUpLasFailPortn,
       "pm251dAlmLineDwLosPortn": pm251dAlmLineDwLosPortn,
       "pm251dmeasures": pm251dmeasures,
       "pm251dMesrOther": pm251dMesrOther,
       "pm251dMesrPort": pm251dMesrPort,
       "pm251dMesrclientTempMeasTable": pm251dMesrclientTempMeasTable,
       "pm251dMesrclientTempMeasEntry": pm251dMesrclientTempMeasEntry,
       "pm251dMesrclientTempMeasIndex": pm251dMesrclientTempMeasIndex,
       "pm251dMesrclientTempMeasPortn": pm251dMesrclientTempMeasPortn,
       "pm251dMesrclientVoltMeasTable": pm251dMesrclientVoltMeasTable,
       "pm251dMesrclientVoltMeasEntry": pm251dMesrclientVoltMeasEntry,
       "pm251dMesrclientVoltMeasIndex": pm251dMesrclientVoltMeasIndex,
       "pm251dMesrclientVoltMeasPortn": pm251dMesrclientVoltMeasPortn,
       "pm251dMesrclientBiasMeasTable": pm251dMesrclientBiasMeasTable,
       "pm251dMesrclientBiasMeasEntry": pm251dMesrclientBiasMeasEntry,
       "pm251dMesrclientBiasMeasIndex": pm251dMesrclientBiasMeasIndex,
       "pm251dMesrclientBiasMeasPortn": pm251dMesrclientBiasMeasPortn,
       "pm251dMesrclientTxpwrMeasTable": pm251dMesrclientTxpwrMeasTable,
       "pm251dMesrclientTxpwrMeasEntry": pm251dMesrclientTxpwrMeasEntry,
       "pm251dMesrclientTxpwrMeasIndex": pm251dMesrclientTxpwrMeasIndex,
       "pm251dMesrclientTxpwrMeasPortn": pm251dMesrclientTxpwrMeasPortn,
       "pm251dMesrclientRxpwrMeasTable": pm251dMesrclientRxpwrMeasTable,
       "pm251dMesrclientRxpwrMeasEntry": pm251dMesrclientRxpwrMeasEntry,
       "pm251dMesrclientRxpwrMeasIndex": pm251dMesrclientRxpwrMeasIndex,
       "pm251dMesrclientRxpwrMeasPortn": pm251dMesrclientRxpwrMeasPortn,
       "pm251dMesrLine": pm251dMesrLine,
       "pm251dMesrlineTempMeasTable": pm251dMesrlineTempMeasTable,
       "pm251dMesrlineTempMeasEntry": pm251dMesrlineTempMeasEntry,
       "pm251dMesrlineTempMeasIndex": pm251dMesrlineTempMeasIndex,
       "pm251dMesrlineTempMeasPortn": pm251dMesrlineTempMeasPortn,
       "pm251dMesrlineVoltMeasTable": pm251dMesrlineVoltMeasTable,
       "pm251dMesrlineVoltMeasEntry": pm251dMesrlineVoltMeasEntry,
       "pm251dMesrlineVoltMeasIndex": pm251dMesrlineVoltMeasIndex,
       "pm251dMesrlineVoltMeasPortn": pm251dMesrlineVoltMeasPortn,
       "pm251dMesrlineBiasMeasTable": pm251dMesrlineBiasMeasTable,
       "pm251dMesrlineBiasMeasEntry": pm251dMesrlineBiasMeasEntry,
       "pm251dMesrlineBiasMeasIndex": pm251dMesrlineBiasMeasIndex,
       "pm251dMesrlineBiasMeasPortn": pm251dMesrlineBiasMeasPortn,
       "pm251dMesrlineTxpwrMeasTable": pm251dMesrlineTxpwrMeasTable,
       "pm251dMesrlineTxpwrMeasEntry": pm251dMesrlineTxpwrMeasEntry,
       "pm251dMesrlineTxpwrMeasIndex": pm251dMesrlineTxpwrMeasIndex,
       "pm251dMesrlineTxpwrMeasPortn": pm251dMesrlineTxpwrMeasPortn,
       "pm251dMesrlineRxpwrMeasTable": pm251dMesrlineRxpwrMeasTable,
       "pm251dMesrlineRxpwrMeasEntry": pm251dMesrlineRxpwrMeasEntry,
       "pm251dMesrlineRxpwrMeasIndex": pm251dMesrlineRxpwrMeasIndex,
       "pm251dMesrlineRxpwrMeasPortn": pm251dMesrlineRxpwrMeasPortn,
       "pm251dcounters": pm251dcounters,
       "pm251dCntOther": pm251dCntOther,
       "pm251dCntPort": pm251dCntPort,
       "pm251dCntclientUpRaRemCntTable": pm251dCntclientUpRaRemCntTable,
       "pm251dCntclientUpRaRemCntEntry": pm251dCntclientUpRaRemCntEntry,
       "pm251dCntclientUpRaRemCntIndex": pm251dCntclientUpRaRemCntIndex,
       "pm251dCntclientUpRaRemCntValuePortn": pm251dCntclientUpRaRemCntValuePortn,
       "pm251dCntclientUpRaRemCntErrorPortn": pm251dCntclientUpRaRemCntErrorPortn,
       "pm251dCntclientUpRaRemCntOverloadPortn": pm251dCntclientUpRaRemCntOverloadPortn,
       "pm251dCntclientUpRaInsCntTable": pm251dCntclientUpRaInsCntTable,
       "pm251dCntclientUpRaInsCntEntry": pm251dCntclientUpRaInsCntEntry,
       "pm251dCntclientUpRaInsCntIndex": pm251dCntclientUpRaInsCntIndex,
       "pm251dCntclientUpRaInsCntValuePortn": pm251dCntclientUpRaInsCntValuePortn,
       "pm251dCntclientUpRaInsCntErrorPortn": pm251dCntclientUpRaInsCntErrorPortn,
       "pm251dCntclientUpRaInsCntOverloadPortn": pm251dCntclientUpRaInsCntOverloadPortn,
       "pm251dCntclientUpDispErrCntTable": pm251dCntclientUpDispErrCntTable,
       "pm251dCntclientUpDispErrCntEntry": pm251dCntclientUpDispErrCntEntry,
       "pm251dCntclientUpDispErrCntIndex": pm251dCntclientUpDispErrCntIndex,
       "pm251dCntclientUpDispErrCntValuePortn": pm251dCntclientUpDispErrCntValuePortn,
       "pm251dCntclientUpDispErrCntErrorPortn": pm251dCntclientUpDispErrCntErrorPortn,
       "pm251dCntclientUpDispErrCntOverloadPortn": pm251dCntclientUpDispErrCntOverloadPortn,
       "pm251dCntclientUpTimCntTable": pm251dCntclientUpTimCntTable,
       "pm251dCntclientUpTimCntEntry": pm251dCntclientUpTimCntEntry,
       "pm251dCntclientUpTimCntIndex": pm251dCntclientUpTimCntIndex,
       "pm251dCntclientUpTimCntValuePortn": pm251dCntclientUpTimCntValuePortn,
       "pm251dCntclientUpTimCntErrorPortn": pm251dCntclientUpTimCntErrorPortn,
       "pm251dCntclientUpTimCntOverloadPortn": pm251dCntclientUpTimCntOverloadPortn,
       "pm251dCntclientDwCbipCntTable": pm251dCntclientDwCbipCntTable,
       "pm251dCntclientDwCbipCntEntry": pm251dCntclientDwCbipCntEntry,
       "pm251dCntclientDwCbipCntIndex": pm251dCntclientDwCbipCntIndex,
       "pm251dCntclientDwCbipCntValuePortn": pm251dCntclientDwCbipCntValuePortn,
       "pm251dCntclientDwCbipCntErrorPortn": pm251dCntclientDwCbipCntErrorPortn,
       "pm251dCntclientDwCbipCntOverloadPortn": pm251dCntclientDwCbipCntOverloadPortn,
       "pm251dCntclientDwTimCntTable": pm251dCntclientDwTimCntTable,
       "pm251dCntclientDwTimCntEntry": pm251dCntclientDwTimCntEntry,
       "pm251dCntclientDwTimCntIndex": pm251dCntclientDwTimCntIndex,
       "pm251dCntclientDwTimCntValuePortn": pm251dCntclientDwTimCntValuePortn,
       "pm251dCntclientDwTimCntErrorPortn": pm251dCntclientDwTimCntErrorPortn,
       "pm251dCntclientDwTimCntOverloadPortn": pm251dCntclientDwTimCntOverloadPortn,
       "pm251dCntLine": pm251dCntLine,
       "pm251dCntlineDfrmB1ErrCntTable": pm251dCntlineDfrmB1ErrCntTable,
       "pm251dCntlineDfrmB1ErrCntEntry": pm251dCntlineDfrmB1ErrCntEntry,
       "pm251dCntlineDfrmB1ErrCntIndex": pm251dCntlineDfrmB1ErrCntIndex,
       "pm251dCntlineDfrmB1ErrCntValuePortn": pm251dCntlineDfrmB1ErrCntValuePortn,
       "pm251dCntlineDfrmB1ErrCntErrorPortn": pm251dCntlineDfrmB1ErrCntErrorPortn,
       "pm251dCntlineDfrmB1ErrCntOverloadPortn": pm251dCntlineDfrmB1ErrCntOverloadPortn,
       "pm251dCntlineDfrmTimCntTable": pm251dCntlineDfrmTimCntTable,
       "pm251dCntlineDfrmTimCntEntry": pm251dCntlineDfrmTimCntEntry,
       "pm251dCntlineDfrmTimCntIndex": pm251dCntlineDfrmTimCntIndex,
       "pm251dCntlineDfrmTimCntValuePortn": pm251dCntlineDfrmTimCntValuePortn,
       "pm251dCntlineDfrmTimCntErrorPortn": pm251dCntlineDfrmTimCntErrorPortn,
       "pm251dCntlineDfrmTimCntOverloadPortn": pm251dCntlineDfrmTimCntOverloadPortn,
       "pm251dCntdfrmPrimLineErrCntTable": pm251dCntdfrmPrimLineErrCntTable,
       "pm251dCntdfrmPrimLineErrCntEntry": pm251dCntdfrmPrimLineErrCntEntry,
       "pm251dCntdfrmPrimLineErrCntIndex": pm251dCntdfrmPrimLineErrCntIndex,
       "pm251dCntdfrmPrimLineErrCntValuePortn": pm251dCntdfrmPrimLineErrCntValuePortn,
       "pm251dCntdfrmPrimLineErrCntErrorPortn": pm251dCntdfrmPrimLineErrCntErrorPortn,
       "pm251dCntdfrmPrimLineErrCntOverloadPortn": pm251dCntdfrmPrimLineErrCntOverloadPortn,
       "pm251dCntCountersReset": pm251dCntCountersReset,
       "pm251dCntCountersStop": pm251dCntCountersStop,
       "pm251dcontrolsWrite": pm251dcontrolsWrite,
       "pm251dCtrlOther": pm251dCtrlOther,
       "pm251dCtrlconfMgnt1": pm251dCtrlconfMgnt1,
       "pm251dCtrlConf1Load1": pm251dCtrlConf1Load1,
       "pm251dCtrlConf2Load1": pm251dCtrlConf2Load1,
       "pm251dCtrlConf2Flash1": pm251dCtrlConf2Flash1,
       "pm251dCtrlConf2Clear1": pm251dCtrlConf2Clear1,
       "pm251dCtrlsynth4": pm251dCtrlsynth4,
       "pm251dCtrlCorrelatOn": pm251dCtrlCorrelatOn,
       "pm251dCtrlCorrelatOff": pm251dCtrlCorrelatOff,
       "pm251dCtrlswMgnt": pm251dCtrlswMgnt,
       "pm251dCtrlColdReset": pm251dCtrlColdReset,
       "pm251dCtrlWarmReset": pm251dCtrlWarmReset,
       "pm251dCtrlLoadSwBank1": pm251dCtrlLoadSwBank1,
       "pm251dCtrlLoadSwBank2": pm251dCtrlLoadSwBank2,
       "pm251dCtrlgwMgnt": pm251dCtrlgwMgnt,
       "pm251dCtrlCurrentGwReset": pm251dCtrlCurrentGwReset,
       "pm251dCtrlLoadGwBank1": pm251dCtrlLoadGwBank1,
       "pm251dCtrlLoadGwBank2": pm251dCtrlLoadGwBank2,
       "pm251dCtrlLoadGwBank3": pm251dCtrlLoadGwBank3,
       "pm251dCtrlLoadGwBank4": pm251dCtrlLoadGwBank4,
       "pm251dCtrlledTest": pm251dCtrlledTest,
       "pm251dCtrlGreenLed": pm251dCtrlGreenLed,
       "pm251dCtrlRedLed": pm251dCtrlRedLed,
       "pm251dCtrlLedOff": pm251dCtrlLedOff,
       "pm251dCtrlmoduleOosMode": pm251dCtrlmoduleOosMode,
       "pm251dCtrlModuleOosMode": pm251dCtrlModuleOosMode,
       "pm251dCtrlmaintenanceMode": pm251dCtrlmaintenanceMode,
       "pm251dCtrlMaintenanceMode": pm251dCtrlMaintenanceMode,
       "pm251dCtrldccEnable": pm251dCtrldccEnable,
       "pm251dCtrlDccEnable": pm251dCtrlDccEnable,
       "pm251dCtrlPort": pm251dCtrlPort,
       "pm251dCtrlclientAccessLoopTable": pm251dCtrlclientAccessLoopTable,
       "pm251dCtrlclientAccessLoopEntry": pm251dCtrlclientAccessLoopEntry,
       "pm251dCtrlclientAccessLoopIndex": pm251dCtrlclientAccessLoopIndex,
       "pm251dCtrlclientAccessLoopPortn": pm251dCtrlclientAccessLoopPortn,
       "pm251dCtrlclientOosModeTable": pm251dCtrlclientOosModeTable,
       "pm251dCtrlclientOosModeEntry": pm251dCtrlclientOosModeEntry,
       "pm251dCtrlclientOosModeIndex": pm251dCtrlclientOosModeIndex,
       "pm251dCtrlclientOosModePortn": pm251dCtrlclientOosModePortn,
       "pm251dCtrlclientSfpOnOffCtrlTable": pm251dCtrlclientSfpOnOffCtrlTable,
       "pm251dCtrlclientSfpOnOffCtrlEntry": pm251dCtrlclientSfpOnOffCtrlEntry,
       "pm251dCtrlclientSfpOnOffCtrlIndex": pm251dCtrlclientSfpOnOffCtrlIndex,
       "pm251dCtrlclientSfpOnOffCtrlPortn": pm251dCtrlclientSfpOnOffCtrlPortn,
       "pm251dCtrlclientCsfUpInsTable": pm251dCtrlclientCsfUpInsTable,
       "pm251dCtrlclientCsfUpInsEntry": pm251dCtrlclientCsfUpInsEntry,
       "pm251dCtrlclientCsfUpInsIndex": pm251dCtrlclientCsfUpInsIndex,
       "pm251dCtrlclientCsfUpInsPortn": pm251dCtrlclientCsfUpInsPortn,
       "pm251dCtrlclientCaisDwInsTable": pm251dCtrlclientCaisDwInsTable,
       "pm251dCtrlclientCaisDwInsEntry": pm251dCtrlclientCaisDwInsEntry,
       "pm251dCtrlclientCaisDwInsIndex": pm251dCtrlclientCaisDwInsIndex,
       "pm251dCtrlclientCaisDwInsPortn": pm251dCtrlclientCaisDwInsPortn,
       "pm251dCtrlLine": pm251dCtrlLine,
       "pm251dCtrllineMsAis": pm251dCtrllineMsAis,
       "pm251dCtrlLineMsAis": pm251dCtrlLineMsAis,
       "pm251dCtrlfecDisableTable": pm251dCtrlfecDisableTable,
       "pm251dCtrlfecDisableEntry": pm251dCtrlfecDisableEntry,
       "pm251dCtrlfecDisableIndex": pm251dCtrlfecDisableIndex,
       "pm251dCtrlfecDisablePortn": pm251dCtrlfecDisablePortn,
       "pm251dCtrllineUpS1Table": pm251dCtrllineUpS1Table,
       "pm251dCtrllineUpS1Entry": pm251dCtrllineUpS1Entry,
       "pm251dCtrllineUpS1Index": pm251dCtrllineUpS1Index,
       "pm251dCtrllineUpS1Portn": pm251dCtrllineUpS1Portn,
       "pm251dCtrllineUpK1Table": pm251dCtrllineUpK1Table,
       "pm251dCtrllineUpK1Entry": pm251dCtrllineUpK1Entry,
       "pm251dCtrllineUpK1Index": pm251dCtrllineUpK1Index,
       "pm251dCtrllineUpK1Portn": pm251dCtrllineUpK1Portn,
       "pm251dCtrllineUpK2Table": pm251dCtrllineUpK2Table,
       "pm251dCtrllineUpK2Entry": pm251dCtrllineUpK2Entry,
       "pm251dCtrllineUpK2Index": pm251dCtrllineUpK2Index,
       "pm251dCtrllineUpK2Portn": pm251dCtrllineUpK2Portn,
       "pm251dCtrllineOosModeTable": pm251dCtrllineOosModeTable,
       "pm251dCtrllineOosModeEntry": pm251dCtrllineOosModeEntry,
       "pm251dCtrllineOosModeIndex": pm251dCtrllineOosModeIndex,
       "pm251dCtrllineOosModePortn": pm251dCtrllineOosModePortn,
       "pm251dCtrllineAccessLoopTable": pm251dCtrllineAccessLoopTable,
       "pm251dCtrllineAccessLoopEntry": pm251dCtrllineAccessLoopEntry,
       "pm251dCtrllineAccessLoopIndex": pm251dCtrllineAccessLoopIndex,
       "pm251dCtrllineAccessLoopPortn": pm251dCtrllineAccessLoopPortn,
       "pm251dCtrllineSfpOnOffCtrlTable": pm251dCtrllineSfpOnOffCtrlTable,
       "pm251dCtrllineSfpOnOffCtrlEntry": pm251dCtrllineSfpOnOffCtrlEntry,
       "pm251dCtrllineSfpOnOffCtrlIndex": pm251dCtrllineSfpOnOffCtrlIndex,
       "pm251dCtrllineSfpOnOffCtrlPortn": pm251dCtrllineSfpOnOffCtrlPortn,
       "pm251dri": pm251dri,
       "pm251driTable": pm251driTable,
       "pm251dRinvClientTable": pm251dRinvClientTable,
       "pm251dRinvClientEntry": pm251dRinvClientEntry,
       "pm251dRinvClientIndex": pm251dRinvClientIndex,
       "pm251dRinvSfpClient": pm251dRinvSfpClient,
       "pm251dRinvLineTable": pm251dRinvLineTable,
       "pm251dRinvLineEntry": pm251dRinvLineEntry,
       "pm251dRinvLineIndex": pm251dRinvLineIndex,
       "pm251dRinvsfpLine": pm251dRinvsfpLine,
       "pm251dRinvReloadInventory": pm251dRinvReloadInventory,
       "pm251dRinvHwPlatform": pm251dRinvHwPlatform,
       "pm251dRinvModulePlatform": pm251dRinvModulePlatform,
       "pm251dRinvSwPlatform": pm251dRinvSwPlatform,
       "pm251dRinvGwPlatform": pm251dRinvGwPlatform,
       "pm251ddownload": pm251ddownload,
       "pm251dDwlOther": pm251dDwlOther,
       "pm251dDwlrestartProcess": pm251dDwlrestartProcess,
       "pm251dDwlWarmRestartProcessed": pm251dDwlWarmRestartProcessed,
       "pm251dDwlColdRestartProcessed": pm251dDwlColdRestartProcessed,
       "pm251dDwlswBanksUsed": pm251dDwlswBanksUsed,
       "pm251dDwlSwBank1Used": pm251dDwlSwBank1Used,
       "pm251dDwlSwBank2Used": pm251dDwlSwBank2Used,
       "pm251dDwlSwBank1Notempty": pm251dDwlSwBank1Notempty,
       "pm251dDwlSwBank2Notempty": pm251dDwlSwBank2Notempty,
       "pm251dDwlgwBanksUsed": pm251dDwlgwBanksUsed,
       "pm251dDwlGwBank1Used": pm251dDwlGwBank1Used,
       "pm251dDwlGwBank2Used": pm251dDwlGwBank2Used,
       "pm251dDwlGwBank3Used": pm251dDwlGwBank3Used,
       "pm251dDwlGwBank4Used": pm251dDwlGwBank4Used,
       "pm251dDwlGwBank1Notempty": pm251dDwlGwBank1Notempty,
       "pm251dDwlGwBank2Notempty": pm251dDwlGwBank2Notempty,
       "pm251dDwlGwBank3Notempty": pm251dDwlGwBank3Notempty,
       "pm251dDwlGwBank4Notempty": pm251dDwlGwBank4Notempty,
       "pm251dDwlPort": pm251dDwlPort,
       "pm251dDwlLine": pm251dDwlLine,
       "pm251dConfig": pm251dConfig,
       "pm251dCfgAccessCAisCsf": pm251dCfgAccessCAisCsf,
       "pm251dCfgClientcaiscsfTable": pm251dCfgClientcaiscsfTable,
       "pm251dCfgClientcaiscsfEntry": pm251dCfgClientcaiscsfEntry,
       "pm251dCfgClientcaiscsfIndex": pm251dCfgClientcaiscsfIndex,
       "pm251dCfgCAisModePortn": pm251dCfgCAisModePortn,
       "pm251dCfgSts24cContribPortn": pm251dCfgSts24cContribPortn,
       "pm251dCfgUpAccessioAlmPortn": pm251dCfgUpAccessioAlmPortn,
       "pm251dCfgUpMapperDeAlmPortn": pm251dCfgUpMapperDeAlmPortn,
       "pm251dCfgDownMapperDeAlmPortn": pm251dCfgDownMapperDeAlmPortn,
       "pm251dCfgDownDfrmAlmPortn": pm251dCfgDownDfrmAlmPortn,
       "pm251dCfgDownLineIoAlmPortn": pm251dCfgDownLineIoAlmPortn,
       "pm251dCfgStartup": pm251dCfgStartup,
       "pm251dCfgClientStartupTable": pm251dCfgClientStartupTable,
       "pm251dCfgClientStartupEntry": pm251dCfgClientStartupEntry,
       "pm251dCfgClientStartupIndex": pm251dCfgClientStartupIndex,
       "pm251dCfgSystConfPortPortn": pm251dCfgSystConfPortPortn,
       "pm251dCfgNetConfPortPortn": pm251dCfgNetConfPortPortn,
       "pm251dCfgPortsOptionsPortn": pm251dCfgPortsOptionsPortn,
       "pm251dtablelineStartup": pm251dtablelineStartup,
       "pm251dCfgsystConfLine1": pm251dCfgsystConfLine1,
       "pm251dCfglineOptions1": pm251dCfglineOptions1,
       "pm251dCfgsystConfLine2": pm251dCfgsystConfLine2,
       "pm251dCfglineSelection": pm251dCfglineSelection,
       "pm251dCfglineOptions2": pm251dCfglineOptions2,
       "pm251dCfgLabels": pm251dCfgLabels,
       "pm251dCfgLabelclientTable": pm251dCfgLabelclientTable,
       "pm251dCfgLabelclientEntry": pm251dCfgLabelclientEntry,
       "pm251dCfgLabelclientIndex": pm251dCfgLabelclientIndex,
       "pm251dCfgLabelclientPortn": pm251dCfgLabelclientPortn,
       "pm251dCfgLabellineTable": pm251dCfgLabellineTable,
       "pm251dCfgLabellineEntry": pm251dCfgLabellineEntry,
       "pm251dCfgLabellineIndex": pm251dCfgLabellineIndex,
       "pm251dCfgLabellinePortn": pm251dCfgLabellinePortn,
       "pm251dCfgWriteConfiguration": pm251dCfgWriteConfiguration,
       "pm251dtraps": pm251dtraps,
       "pm251dTrapPortNumber": pm251dTrapPortNumber,
       "pm251dTrapBoardNumber": pm251dTrapBoardNumber,
       "pm251dTrapLineNumber": pm251dTrapLineNumber,
       "pm251dLineTrapNotUrgentGoesOn": pm251dLineTrapNotUrgentGoesOn,
       "pm251dLineTrapNotUrgentGoesOff": pm251dLineTrapNotUrgentGoesOff,
       "pm251dLineTrapUrgentGoesOn": pm251dLineTrapUrgentGoesOn,
       "pm251dLineTrapUrgentGoesOff": pm251dLineTrapUrgentGoesOff,
       "pm251dLineTrapCritGoesOn": pm251dLineTrapCritGoesOn,
       "pm251dLineTrapCritGoesOff": pm251dLineTrapCritGoesOff,
       "pm251dClientTrapNotUrgentGoesOn": pm251dClientTrapNotUrgentGoesOn,
       "pm251dClientTrapNotUrgentGoesOff": pm251dClientTrapNotUrgentGoesOff,
       "pm251dClientTrapUrgentGoesOn": pm251dClientTrapUrgentGoesOn,
       "pm251dClientTrapUrgentGoesOff": pm251dClientTrapUrgentGoesOff,
       "pm251dClientTrapCritGoesOn": pm251dClientTrapCritGoesOn,
       "pm251dClientTrapCritGoesOff": pm251dClientTrapCritGoesOff,
       "pm251dMonitoring": pm251dMonitoring,
       "pm251dMonOther": pm251dMonOther,
       "pm251dMonRmon": pm251dMonRmon,
       "pm251dMonClient": pm251dMonClient,
       "pm251dMonClientRmonCounter": pm251dMonClientRmonCounter}
)
