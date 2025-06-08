# SNMP MIB module (EKINOPS-Pm253-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Pm253-MIB.mib
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

modulePm253 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13)
)
if mibBuilder.loadTexts:
    modulePm253.setRevisions(
        ("2006-03-17 00:00",
         "2006-05-22 00:00",
         "2006-08-18 00:00",
         "2007-07-06 00:00",
         "2007-11-30 00:00",
         "2008-10-27 00:00",
         "2008-11-25 00:00",
         "2009-04-09 00:00",
         "2009-08-25 00:00",
         "2010-02-18 00:00",
         "2010-11-05 00:00",
         "2012-07-02 00:00",
         "2014-03-27 00:00",
         "2015-01-14 00:00",
         "2015-01-14 00:00",
         "2016-05-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Pm253alarms_ObjectIdentity = ObjectIdentity
pm253alarms = _Pm253alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2)
)
_Pm253AlmOther_ObjectIdentity = ObjectIdentity
pm253AlmOther = _Pm253AlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 1)
)
_Pm253AlmOtherNurg_ObjectIdentity = ObjectIdentity
pm253AlmOtherNurg = _Pm253AlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 1, 1)
)
_Pm253AlmsynthAlm0_ObjectIdentity = ObjectIdentity
pm253AlmsynthAlm0 = _Pm253AlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 1, 1, 0)
)
_Pm253AlmModGlobFail_Type = EkiOnOff
_Pm253AlmModGlobFail_Object = MibScalar
pm253AlmModGlobFail = _Pm253AlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 1, 1, 0, 9),
    _Pm253AlmModGlobFail_Type()
)
pm253AlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmModGlobFail.setStatus("current")
_Pm253AlmDefFuseA_Type = EkiOnOff
_Pm253AlmDefFuseA_Object = MibScalar
pm253AlmDefFuseA = _Pm253AlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 1, 1, 0, 15),
    _Pm253AlmDefFuseA_Type()
)
pm253AlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmDefFuseA.setStatus("current")
_Pm253AlmDefFuseB_Type = EkiOnOff
_Pm253AlmDefFuseB_Object = MibScalar
pm253AlmDefFuseB = _Pm253AlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 1, 1, 0, 16),
    _Pm253AlmDefFuseB_Type()
)
pm253AlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmDefFuseB.setStatus("current")
_Pm253AlmsynthAlm2_ObjectIdentity = ObjectIdentity
pm253AlmsynthAlm2 = _Pm253AlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 1, 1, 2)
)
_Pm253AlmConfTableSave_Type = EkiOnOff
_Pm253AlmConfTableSave_Object = MibScalar
pm253AlmConfTableSave = _Pm253AlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 1, 1, 2, 1),
    _Pm253AlmConfTableSave_Type()
)
pm253AlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmConfTableSave.setStatus("current")
_Pm253AlmInvUpload_Type = EkiOnOff
_Pm253AlmInvUpload_Object = MibScalar
pm253AlmInvUpload = _Pm253AlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 1, 1, 2, 2),
    _Pm253AlmInvUpload_Type()
)
pm253AlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmInvUpload.setStatus("current")
_Pm253AlmConfTableLoad_Type = EkiOnOff
_Pm253AlmConfTableLoad_Object = MibScalar
pm253AlmConfTableLoad = _Pm253AlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 1, 1, 2, 3),
    _Pm253AlmConfTableLoad_Type()
)
pm253AlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmConfTableLoad.setStatus("current")
_Pm253AlmCorrelatOff_Type = EkiOnOff
_Pm253AlmCorrelatOff_Object = MibScalar
pm253AlmCorrelatOff = _Pm253AlmCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 1, 1, 2, 4),
    _Pm253AlmCorrelatOff_Type()
)
pm253AlmCorrelatOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmCorrelatOff.setStatus("current")
_Pm253AlmMaintenanceOn_Type = EkiOnOff
_Pm253AlmMaintenanceOn_Object = MibScalar
pm253AlmMaintenanceOn = _Pm253AlmMaintenanceOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 1, 1, 2, 5),
    _Pm253AlmMaintenanceOn_Type()
)
pm253AlmMaintenanceOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmMaintenanceOn.setStatus("current")
_Pm253AlmOtherUrg_ObjectIdentity = ObjectIdentity
pm253AlmOtherUrg = _Pm253AlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 1, 2)
)
_Pm253AlmmodInitFailLevel2_ObjectIdentity = ObjectIdentity
pm253AlmmodInitFailLevel2 = _Pm253AlmmodInitFailLevel2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 1, 2, 194)
)
_Pm253AlmLedFail_Type = EkiOnOff
_Pm253AlmLedFail_Object = MibScalar
pm253AlmLedFail = _Pm253AlmLedFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 1, 2, 194, 1),
    _Pm253AlmLedFail_Type()
)
pm253AlmLedFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLedFail.setStatus("current")
_Pm253AlmNextColdBootForced_Type = EkiOnOff
_Pm253AlmNextColdBootForced_Object = MibScalar
pm253AlmNextColdBootForced = _Pm253AlmNextColdBootForced_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 1, 2, 194, 2),
    _Pm253AlmNextColdBootForced_Type()
)
pm253AlmNextColdBootForced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmNextColdBootForced.setStatus("current")
_Pm253AlmBootUndone_Type = EkiOnOff
_Pm253AlmBootUndone_Object = MibScalar
pm253AlmBootUndone = _Pm253AlmBootUndone_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 1, 2, 194, 3),
    _Pm253AlmBootUndone_Type()
)
pm253AlmBootUndone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmBootUndone.setStatus("current")
_Pm253AlmResetHwInitFail_Type = EkiOnOff
_Pm253AlmResetHwInitFail_Object = MibScalar
pm253AlmResetHwInitFail = _Pm253AlmResetHwInitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 1, 2, 194, 4),
    _Pm253AlmResetHwInitFail_Type()
)
pm253AlmResetHwInitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmResetHwInitFail.setStatus("current")
_Pm253AlmSwInitFail_Type = EkiOnOff
_Pm253AlmSwInitFail_Object = MibScalar
pm253AlmSwInitFail = _Pm253AlmSwInitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 1, 2, 194, 5),
    _Pm253AlmSwInitFail_Type()
)
pm253AlmSwInitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmSwInitFail.setStatus("current")
_Pm253AlmmodInitFailLevel3_ObjectIdentity = ObjectIdentity
pm253AlmmodInitFailLevel3 = _Pm253AlmmodInitFailLevel3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 1, 2, 195)
)
_Pm253AlmGwIdentFail_Type = EkiOnOff
_Pm253AlmGwIdentFail_Object = MibScalar
pm253AlmGwIdentFail = _Pm253AlmGwIdentFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 1, 2, 195, 1),
    _Pm253AlmGwIdentFail_Type()
)
pm253AlmGwIdentFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmGwIdentFail.setStatus("current")
_Pm253AlmObmTypeReadFail_Type = EkiOnOff
_Pm253AlmObmTypeReadFail_Object = MibScalar
pm253AlmObmTypeReadFail = _Pm253AlmObmTypeReadFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 1, 2, 195, 2),
    _Pm253AlmObmTypeReadFail_Type()
)
pm253AlmObmTypeReadFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmObmTypeReadFail.setStatus("current")
_Pm253AlmInitModuleFail_Type = EkiOnOff
_Pm253AlmInitModuleFail_Object = MibScalar
pm253AlmInitModuleFail = _Pm253AlmInitModuleFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 1, 2, 195, 3),
    _Pm253AlmInitModuleFail_Type()
)
pm253AlmInitModuleFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmInitModuleFail.setStatus("current")
_Pm253AlmSfp1InitFail_Type = EkiOnOff
_Pm253AlmSfp1InitFail_Object = MibScalar
pm253AlmSfp1InitFail = _Pm253AlmSfp1InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 1, 2, 195, 5),
    _Pm253AlmSfp1InitFail_Type()
)
pm253AlmSfp1InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmSfp1InitFail.setStatus("current")
_Pm253AlmSfp2InitFail_Type = EkiOnOff
_Pm253AlmSfp2InitFail_Object = MibScalar
pm253AlmSfp2InitFail = _Pm253AlmSfp2InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 1, 2, 195, 6),
    _Pm253AlmSfp2InitFail_Type()
)
pm253AlmSfp2InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmSfp2InitFail.setStatus("current")
_Pm253AlmLine1InitFail_Type = EkiOnOff
_Pm253AlmLine1InitFail_Object = MibScalar
pm253AlmLine1InitFail = _Pm253AlmLine1InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 1, 2, 195, 7),
    _Pm253AlmLine1InitFail_Type()
)
pm253AlmLine1InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLine1InitFail.setStatus("current")
_Pm253AlmLine2InitFail_Type = EkiOnOff
_Pm253AlmLine2InitFail_Object = MibScalar
pm253AlmLine2InitFail = _Pm253AlmLine2InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 1, 2, 195, 8),
    _Pm253AlmLine2InitFail_Type()
)
pm253AlmLine2InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLine2InitFail.setStatus("current")
_Pm253AlmClient1InitFail_Type = EkiOnOff
_Pm253AlmClient1InitFail_Object = MibScalar
pm253AlmClient1InitFail = _Pm253AlmClient1InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 1, 2, 195, 9),
    _Pm253AlmClient1InitFail_Type()
)
pm253AlmClient1InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClient1InitFail.setStatus("current")
_Pm253AlmClient2InitFail_Type = EkiOnOff
_Pm253AlmClient2InitFail_Object = MibScalar
pm253AlmClient2InitFail = _Pm253AlmClient2InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 1, 2, 195, 10),
    _Pm253AlmClient2InitFail_Type()
)
pm253AlmClient2InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClient2InitFail.setStatus("current")
_Pm253AlmClient3InitFail_Type = EkiOnOff
_Pm253AlmClient3InitFail_Object = MibScalar
pm253AlmClient3InitFail = _Pm253AlmClient3InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 1, 2, 195, 11),
    _Pm253AlmClient3InitFail_Type()
)
pm253AlmClient3InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClient3InitFail.setStatus("current")
_Pm253AlmOtherCrit_ObjectIdentity = ObjectIdentity
pm253AlmOtherCrit = _Pm253AlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 1, 3)
)
_Pm253AlmPort_ObjectIdentity = ObjectIdentity
pm253AlmPort = _Pm253AlmPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2)
)
_Pm253AlmPortNurg_ObjectIdentity = ObjectIdentity
pm253AlmPortNurg = _Pm253AlmPortNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 1)
)
_Pm253AlmclientSfpWarnDdmTable_Object = MibTable
pm253AlmclientSfpWarnDdmTable = _Pm253AlmclientSfpWarnDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 1, 48)
)
if mibBuilder.loadTexts:
    pm253AlmclientSfpWarnDdmTable.setStatus("current")
_Pm253AlmclientSfpWarnDdmEntry_Object = MibTableRow
pm253AlmclientSfpWarnDdmEntry = _Pm253AlmclientSfpWarnDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 1, 48, 1)
)
pm253AlmclientSfpWarnDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253AlmclientSfpWarnDdmIndex"),
)
if mibBuilder.loadTexts:
    pm253AlmclientSfpWarnDdmEntry.setStatus("current")


class _Pm253AlmclientSfpWarnDdmIndex_Type(Integer32):
    """Custom type pm253AlmclientSfpWarnDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253AlmclientSfpWarnDdmIndex_Type.__name__ = "Integer32"
_Pm253AlmclientSfpWarnDdmIndex_Object = MibTableColumn
pm253AlmclientSfpWarnDdmIndex = _Pm253AlmclientSfpWarnDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 1, 48, 1, 1),
    _Pm253AlmclientSfpWarnDdmIndex_Type()
)
pm253AlmclientSfpWarnDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmclientSfpWarnDdmIndex.setStatus("current")
_Pm253AlmClientTxPwLowWngPortn_Type = EkiOnOff
_Pm253AlmClientTxPwLowWngPortn_Object = MibTableColumn
pm253AlmClientTxPwLowWngPortn = _Pm253AlmClientTxPwLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 1, 48, 1, 2),
    _Pm253AlmClientTxPwLowWngPortn_Type()
)
pm253AlmClientTxPwLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientTxPwLowWngPortn.setStatus("current")
_Pm253AlmClientTxPwrHighWngPortn_Type = EkiOnOff
_Pm253AlmClientTxPwrHighWngPortn_Object = MibTableColumn
pm253AlmClientTxPwrHighWngPortn = _Pm253AlmClientTxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 1, 48, 1, 3),
    _Pm253AlmClientTxPwrHighWngPortn_Type()
)
pm253AlmClientTxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientTxPwrHighWngPortn.setStatus("current")
_Pm253AlmClientTxBiasLowWngPortn_Type = EkiOnOff
_Pm253AlmClientTxBiasLowWngPortn_Object = MibTableColumn
pm253AlmClientTxBiasLowWngPortn = _Pm253AlmClientTxBiasLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 1, 48, 1, 4),
    _Pm253AlmClientTxBiasLowWngPortn_Type()
)
pm253AlmClientTxBiasLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientTxBiasLowWngPortn.setStatus("current")
_Pm253AlmClientTxBiasHighWngPortn_Type = EkiOnOff
_Pm253AlmClientTxBiasHighWngPortn_Object = MibTableColumn
pm253AlmClientTxBiasHighWngPortn = _Pm253AlmClientTxBiasHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 1, 48, 1, 5),
    _Pm253AlmClientTxBiasHighWngPortn_Type()
)
pm253AlmClientTxBiasHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientTxBiasHighWngPortn.setStatus("current")
_Pm253AlmClientVccLowWngPortn_Type = EkiOnOff
_Pm253AlmClientVccLowWngPortn_Object = MibTableColumn
pm253AlmClientVccLowWngPortn = _Pm253AlmClientVccLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 1, 48, 1, 6),
    _Pm253AlmClientVccLowWngPortn_Type()
)
pm253AlmClientVccLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientVccLowWngPortn.setStatus("current")
_Pm253AlmClientVccHighWngPortn_Type = EkiOnOff
_Pm253AlmClientVccHighWngPortn_Object = MibTableColumn
pm253AlmClientVccHighWngPortn = _Pm253AlmClientVccHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 1, 48, 1, 7),
    _Pm253AlmClientVccHighWngPortn_Type()
)
pm253AlmClientVccHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientVccHighWngPortn.setStatus("current")
_Pm253AlmClientTempLowWngPortn_Type = EkiOnOff
_Pm253AlmClientTempLowWngPortn_Object = MibTableColumn
pm253AlmClientTempLowWngPortn = _Pm253AlmClientTempLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 1, 48, 1, 8),
    _Pm253AlmClientTempLowWngPortn_Type()
)
pm253AlmClientTempLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientTempLowWngPortn.setStatus("current")
_Pm253AlmClientTempHighWngPortn_Type = EkiOnOff
_Pm253AlmClientTempHighWngPortn_Object = MibTableColumn
pm253AlmClientTempHighWngPortn = _Pm253AlmClientTempHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 1, 48, 1, 9),
    _Pm253AlmClientTempHighWngPortn_Type()
)
pm253AlmClientTempHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientTempHighWngPortn.setStatus("current")
_Pm253AlmClientRxPwrLowWngPortn_Type = EkiOnOff
_Pm253AlmClientRxPwrLowWngPortn_Object = MibTableColumn
pm253AlmClientRxPwrLowWngPortn = _Pm253AlmClientRxPwrLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 1, 48, 1, 16),
    _Pm253AlmClientRxPwrLowWngPortn_Type()
)
pm253AlmClientRxPwrLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientRxPwrLowWngPortn.setStatus("current")
_Pm253AlmClientRxPwrHighWngPortn_Type = EkiOnOff
_Pm253AlmClientRxPwrHighWngPortn_Object = MibTableColumn
pm253AlmClientRxPwrHighWngPortn = _Pm253AlmClientRxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 1, 48, 1, 17),
    _Pm253AlmClientRxPwrHighWngPortn_Type()
)
pm253AlmClientRxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientRxPwrHighWngPortn.setStatus("current")
_Pm253AlmPortUrg_ObjectIdentity = ObjectIdentity
pm253AlmPortUrg = _Pm253AlmPortUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 2)
)
_Pm253AlmclientSfpAlmDdmTable_Object = MibTable
pm253AlmclientSfpAlmDdmTable = _Pm253AlmclientSfpAlmDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 2, 32)
)
if mibBuilder.loadTexts:
    pm253AlmclientSfpAlmDdmTable.setStatus("current")
_Pm253AlmclientSfpAlmDdmEntry_Object = MibTableRow
pm253AlmclientSfpAlmDdmEntry = _Pm253AlmclientSfpAlmDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 2, 32, 1)
)
pm253AlmclientSfpAlmDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253AlmclientSfpAlmDdmIndex"),
)
if mibBuilder.loadTexts:
    pm253AlmclientSfpAlmDdmEntry.setStatus("current")


class _Pm253AlmclientSfpAlmDdmIndex_Type(Integer32):
    """Custom type pm253AlmclientSfpAlmDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253AlmclientSfpAlmDdmIndex_Type.__name__ = "Integer32"
_Pm253AlmclientSfpAlmDdmIndex_Object = MibTableColumn
pm253AlmclientSfpAlmDdmIndex = _Pm253AlmclientSfpAlmDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 2, 32, 1, 1),
    _Pm253AlmclientSfpAlmDdmIndex_Type()
)
pm253AlmclientSfpAlmDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmclientSfpAlmDdmIndex.setStatus("current")
_Pm253AlmClientTxPwrLowAlaPortn_Type = EkiOnOff
_Pm253AlmClientTxPwrLowAlaPortn_Object = MibTableColumn
pm253AlmClientTxPwrLowAlaPortn = _Pm253AlmClientTxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 2, 32, 1, 2),
    _Pm253AlmClientTxPwrLowAlaPortn_Type()
)
pm253AlmClientTxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientTxPwrLowAlaPortn.setStatus("current")
_Pm253AlmClientTxPwrHighAlaPortn_Type = EkiOnOff
_Pm253AlmClientTxPwrHighAlaPortn_Object = MibTableColumn
pm253AlmClientTxPwrHighAlaPortn = _Pm253AlmClientTxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 2, 32, 1, 3),
    _Pm253AlmClientTxPwrHighAlaPortn_Type()
)
pm253AlmClientTxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientTxPwrHighAlaPortn.setStatus("current")
_Pm253AlmClientTxBiasLowAlaPortn_Type = EkiOnOff
_Pm253AlmClientTxBiasLowAlaPortn_Object = MibTableColumn
pm253AlmClientTxBiasLowAlaPortn = _Pm253AlmClientTxBiasLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 2, 32, 1, 4),
    _Pm253AlmClientTxBiasLowAlaPortn_Type()
)
pm253AlmClientTxBiasLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientTxBiasLowAlaPortn.setStatus("current")
_Pm253AlmClientTxBiasHighAlaPortn_Type = EkiOnOff
_Pm253AlmClientTxBiasHighAlaPortn_Object = MibTableColumn
pm253AlmClientTxBiasHighAlaPortn = _Pm253AlmClientTxBiasHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 2, 32, 1, 5),
    _Pm253AlmClientTxBiasHighAlaPortn_Type()
)
pm253AlmClientTxBiasHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientTxBiasHighAlaPortn.setStatus("current")
_Pm253AlmClientVccLowAlaPortn_Type = EkiOnOff
_Pm253AlmClientVccLowAlaPortn_Object = MibTableColumn
pm253AlmClientVccLowAlaPortn = _Pm253AlmClientVccLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 2, 32, 1, 6),
    _Pm253AlmClientVccLowAlaPortn_Type()
)
pm253AlmClientVccLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientVccLowAlaPortn.setStatus("current")
_Pm253AlmClientVccHighAlaPortn_Type = EkiOnOff
_Pm253AlmClientVccHighAlaPortn_Object = MibTableColumn
pm253AlmClientVccHighAlaPortn = _Pm253AlmClientVccHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 2, 32, 1, 7),
    _Pm253AlmClientVccHighAlaPortn_Type()
)
pm253AlmClientVccHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientVccHighAlaPortn.setStatus("current")
_Pm253AlmClientTempLowAlaPortn_Type = EkiOnOff
_Pm253AlmClientTempLowAlaPortn_Object = MibTableColumn
pm253AlmClientTempLowAlaPortn = _Pm253AlmClientTempLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 2, 32, 1, 8),
    _Pm253AlmClientTempLowAlaPortn_Type()
)
pm253AlmClientTempLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientTempLowAlaPortn.setStatus("current")
_Pm253AlmClientTempHighAlaPortn_Type = EkiOnOff
_Pm253AlmClientTempHighAlaPortn_Object = MibTableColumn
pm253AlmClientTempHighAlaPortn = _Pm253AlmClientTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 2, 32, 1, 9),
    _Pm253AlmClientTempHighAlaPortn_Type()
)
pm253AlmClientTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientTempHighAlaPortn.setStatus("current")
_Pm253AlmClientRxPwrLowAlaPortn_Type = EkiOnOff
_Pm253AlmClientRxPwrLowAlaPortn_Object = MibTableColumn
pm253AlmClientRxPwrLowAlaPortn = _Pm253AlmClientRxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 2, 32, 1, 16),
    _Pm253AlmClientRxPwrLowAlaPortn_Type()
)
pm253AlmClientRxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientRxPwrLowAlaPortn.setStatus("current")
_Pm253AlmClientRxPwrHighAlaPortn_Type = EkiOnOff
_Pm253AlmClientRxPwrHighAlaPortn_Object = MibTableColumn
pm253AlmClientRxPwrHighAlaPortn = _Pm253AlmClientRxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 2, 32, 1, 17),
    _Pm253AlmClientRxPwrHighAlaPortn_Type()
)
pm253AlmClientRxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientRxPwrHighAlaPortn.setStatus("current")
_Pm253AlmPortCrit_ObjectIdentity = ObjectIdentity
pm253AlmPortCrit = _Pm253AlmPortCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 3)
)
_Pm253AlmsynthAlmClientTable_Object = MibTable
pm253AlmsynthAlmClientTable = _Pm253AlmsynthAlmClientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    pm253AlmsynthAlmClientTable.setStatus("current")
_Pm253AlmsynthAlmClientEntry_Object = MibTableRow
pm253AlmsynthAlmClientEntry = _Pm253AlmsynthAlmClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 3, 8, 1)
)
pm253AlmsynthAlmClientEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253AlmsynthAlmClientIndex"),
)
if mibBuilder.loadTexts:
    pm253AlmsynthAlmClientEntry.setStatus("current")


class _Pm253AlmsynthAlmClientIndex_Type(Integer32):
    """Custom type pm253AlmsynthAlmClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253AlmsynthAlmClientIndex_Type.__name__ = "Integer32"
_Pm253AlmsynthAlmClientIndex_Object = MibTableColumn
pm253AlmsynthAlmClientIndex = _Pm253AlmsynthAlmClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 3, 8, 1, 1),
    _Pm253AlmsynthAlmClientIndex_Type()
)
pm253AlmsynthAlmClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmsynthAlmClientIndex.setStatus("current")
_Pm253AlmClientSfpAbsentPortn_Type = EkiOnOff
_Pm253AlmClientSfpAbsentPortn_Object = MibTableColumn
pm253AlmClientSfpAbsentPortn = _Pm253AlmClientSfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 3, 8, 1, 2),
    _Pm253AlmClientSfpAbsentPortn_Type()
)
pm253AlmClientSfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientSfpAbsentPortn.setStatus("current")
_Pm253AlmClientDdmAbsentPortn_Type = EkiOnOff
_Pm253AlmClientDdmAbsentPortn_Object = MibTableColumn
pm253AlmClientDdmAbsentPortn = _Pm253AlmClientDdmAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 3, 8, 1, 3),
    _Pm253AlmClientDdmAbsentPortn_Type()
)
pm253AlmClientDdmAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientDdmAbsentPortn.setStatus("current")
_Pm253AlmClientHwFailAccPortn_Type = EkiOnOff
_Pm253AlmClientHwFailAccPortn_Object = MibTableColumn
pm253AlmClientHwFailAccPortn = _Pm253AlmClientHwFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 3, 8, 1, 5),
    _Pm253AlmClientHwFailAccPortn_Type()
)
pm253AlmClientHwFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientHwFailAccPortn.setStatus("current")
_Pm253AlmClientLsdPortn_Type = EkiOnOff
_Pm253AlmClientLsdPortn_Object = MibTableColumn
pm253AlmClientLsdPortn = _Pm253AlmClientLsdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 3, 8, 1, 6),
    _Pm253AlmClientLsdPortn_Type()
)
pm253AlmClientLsdPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientLsdPortn.setStatus("current")
_Pm253AlmClientLocalOosPortn_Type = EkiOnOff
_Pm253AlmClientLocalOosPortn_Object = MibTableColumn
pm253AlmClientLocalOosPortn = _Pm253AlmClientLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 3, 8, 1, 7),
    _Pm253AlmClientLocalOosPortn_Type()
)
pm253AlmClientLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientLocalOosPortn.setStatus("current")
_Pm253AlmClientRemoteOosPortn_Type = EkiOnOff
_Pm253AlmClientRemoteOosPortn_Object = MibTableColumn
pm253AlmClientRemoteOosPortn = _Pm253AlmClientRemoteOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 3, 8, 1, 8),
    _Pm253AlmClientRemoteOosPortn_Type()
)
pm253AlmClientRemoteOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientRemoteOosPortn.setStatus("current")
_Pm253AlmClientDwCaisPortn_Type = EkiOnOff
_Pm253AlmClientDwCaisPortn_Object = MibTableColumn
pm253AlmClientDwCaisPortn = _Pm253AlmClientDwCaisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 3, 8, 1, 9),
    _Pm253AlmClientDwCaisPortn_Type()
)
pm253AlmClientDwCaisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientDwCaisPortn.setStatus("current")
_Pm253AlmClientSfpDdmWarningPortn_Type = EkiOnOff
_Pm253AlmClientSfpDdmWarningPortn_Object = MibTableColumn
pm253AlmClientSfpDdmWarningPortn = _Pm253AlmClientSfpDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 3, 8, 1, 10),
    _Pm253AlmClientSfpDdmWarningPortn_Type()
)
pm253AlmClientSfpDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientSfpDdmWarningPortn.setStatus("current")
_Pm253AlmClientSfpDdmAlmPortn_Type = EkiOnOff
_Pm253AlmClientSfpDdmAlmPortn_Object = MibTableColumn
pm253AlmClientSfpDdmAlmPortn = _Pm253AlmClientSfpDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 3, 8, 1, 11),
    _Pm253AlmClientSfpDdmAlmPortn_Type()
)
pm253AlmClientSfpDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientSfpDdmAlmPortn.setStatus("current")
_Pm253AlmClientFailAccPortn_Type = EkiOnOff
_Pm253AlmClientFailAccPortn_Object = MibTableColumn
pm253AlmClientFailAccPortn = _Pm253AlmClientFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 3, 8, 1, 13),
    _Pm253AlmClientFailAccPortn_Type()
)
pm253AlmClientFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientFailAccPortn.setStatus("current")
_Pm253AlmClientUpCsfPortn_Type = EkiOnOff
_Pm253AlmClientUpCsfPortn_Object = MibTableColumn
pm253AlmClientUpCsfPortn = _Pm253AlmClientUpCsfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 3, 8, 1, 17),
    _Pm253AlmClientUpCsfPortn_Type()
)
pm253AlmClientUpCsfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientUpCsfPortn.setStatus("current")
_Pm253AlmaccessioAlmTable_Object = MibTable
pm253AlmaccessioAlmTable = _Pm253AlmaccessioAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 3, 16)
)
if mibBuilder.loadTexts:
    pm253AlmaccessioAlmTable.setStatus("current")
_Pm253AlmaccessioAlmEntry_Object = MibTableRow
pm253AlmaccessioAlmEntry = _Pm253AlmaccessioAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 3, 16, 1)
)
pm253AlmaccessioAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253AlmaccessioAlmIndex"),
)
if mibBuilder.loadTexts:
    pm253AlmaccessioAlmEntry.setStatus("current")


class _Pm253AlmaccessioAlmIndex_Type(Integer32):
    """Custom type pm253AlmaccessioAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253AlmaccessioAlmIndex_Type.__name__ = "Integer32"
_Pm253AlmaccessioAlmIndex_Object = MibTableColumn
pm253AlmaccessioAlmIndex = _Pm253AlmaccessioAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 3, 16, 1, 1),
    _Pm253AlmaccessioAlmIndex_Type()
)
pm253AlmaccessioAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmaccessioAlmIndex.setStatus("current")
_Pm253AlmClientDwLasFailPortn_Type = EkiOnOff
_Pm253AlmClientDwLasFailPortn_Object = MibTableColumn
pm253AlmClientDwLasFailPortn = _Pm253AlmClientDwLasFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 3, 16, 1, 2),
    _Pm253AlmClientDwLasFailPortn_Type()
)
pm253AlmClientDwLasFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientDwLasFailPortn.setStatus("current")
_Pm253AlmClientUpLosPortn_Type = EkiOnOff
_Pm253AlmClientUpLosPortn_Object = MibTableColumn
pm253AlmClientUpLosPortn = _Pm253AlmClientUpLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 3, 16, 1, 5),
    _Pm253AlmClientUpLosPortn_Type()
)
pm253AlmClientUpLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientUpLosPortn.setStatus("current")
_Pm253AlmclientMapperDeAlmTable_Object = MibTable
pm253AlmclientMapperDeAlmTable = _Pm253AlmclientMapperDeAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 3, 72)
)
if mibBuilder.loadTexts:
    pm253AlmclientMapperDeAlmTable.setStatus("current")
_Pm253AlmclientMapperDeAlmEntry_Object = MibTableRow
pm253AlmclientMapperDeAlmEntry = _Pm253AlmclientMapperDeAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 3, 72, 1)
)
pm253AlmclientMapperDeAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253AlmclientMapperDeAlmIndex"),
)
if mibBuilder.loadTexts:
    pm253AlmclientMapperDeAlmEntry.setStatus("current")


class _Pm253AlmclientMapperDeAlmIndex_Type(Integer32):
    """Custom type pm253AlmclientMapperDeAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253AlmclientMapperDeAlmIndex_Type.__name__ = "Integer32"
_Pm253AlmclientMapperDeAlmIndex_Object = MibTableColumn
pm253AlmclientMapperDeAlmIndex = _Pm253AlmclientMapperDeAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 3, 72, 1, 1),
    _Pm253AlmclientMapperDeAlmIndex_Type()
)
pm253AlmclientMapperDeAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmclientMapperDeAlmIndex.setStatus("current")
_Pm253AlmClientUpAccOosPortn_Type = EkiOnOff
_Pm253AlmClientUpAccOosPortn_Object = MibTableColumn
pm253AlmClientUpAccOosPortn = _Pm253AlmClientUpAccOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 3, 72, 1, 2),
    _Pm253AlmClientUpAccOosPortn_Type()
)
pm253AlmClientUpAccOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientUpAccOosPortn.setStatus("current")
_Pm253AlmClientUpBufferOvlPortn_Type = EkiOnOff
_Pm253AlmClientUpBufferOvlPortn_Object = MibTableColumn
pm253AlmClientUpBufferOvlPortn = _Pm253AlmClientUpBufferOvlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 3, 72, 1, 11),
    _Pm253AlmClientUpBufferOvlPortn_Type()
)
pm253AlmClientUpBufferOvlPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientUpBufferOvlPortn.setStatus("current")
_Pm253AlmClientDwCsfDetPortn_Type = EkiOnOff
_Pm253AlmClientDwCsfDetPortn_Object = MibTableColumn
pm253AlmClientDwCsfDetPortn = _Pm253AlmClientDwCsfDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 3, 72, 1, 12),
    _Pm253AlmClientDwCsfDetPortn_Type()
)
pm253AlmClientDwCsfDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientDwCsfDetPortn.setStatus("current")
_Pm253AlmClientDwBufferOvlPortn_Type = EkiOnOff
_Pm253AlmClientDwBufferOvlPortn_Object = MibTableColumn
pm253AlmClientDwBufferOvlPortn = _Pm253AlmClientDwBufferOvlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 3, 72, 1, 15),
    _Pm253AlmClientDwBufferOvlPortn_Type()
)
pm253AlmClientDwBufferOvlPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientDwBufferOvlPortn.setStatus("current")
_Pm253AlmClientLoopAccFifoFailPortn_Type = EkiOnOff
_Pm253AlmClientLoopAccFifoFailPortn_Object = MibTableColumn
pm253AlmClientLoopAccFifoFailPortn = _Pm253AlmClientLoopAccFifoFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 3, 72, 1, 16),
    _Pm253AlmClientLoopAccFifoFailPortn_Type()
)
pm253AlmClientLoopAccFifoFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientLoopAccFifoFailPortn.setStatus("deprecated")
_Pm253AlmaccessioSdhAlarmTable_Object = MibTable
pm253AlmaccessioSdhAlarmTable = _Pm253AlmaccessioSdhAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 3, 104)
)
if mibBuilder.loadTexts:
    pm253AlmaccessioSdhAlarmTable.setStatus("current")
_Pm253AlmaccessioSdhAlarmEntry_Object = MibTableRow
pm253AlmaccessioSdhAlarmEntry = _Pm253AlmaccessioSdhAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 3, 104, 1)
)
pm253AlmaccessioSdhAlarmEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253AlmaccessioSdhAlarmIndex"),
)
if mibBuilder.loadTexts:
    pm253AlmaccessioSdhAlarmEntry.setStatus("current")


class _Pm253AlmaccessioSdhAlarmIndex_Type(Integer32):
    """Custom type pm253AlmaccessioSdhAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253AlmaccessioSdhAlarmIndex_Type.__name__ = "Integer32"
_Pm253AlmaccessioSdhAlarmIndex_Object = MibTableColumn
pm253AlmaccessioSdhAlarmIndex = _Pm253AlmaccessioSdhAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 3, 104, 1, 1),
    _Pm253AlmaccessioSdhAlarmIndex_Type()
)
pm253AlmaccessioSdhAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmaccessioSdhAlarmIndex.setStatus("current")
_Pm253AlmLosTrscPortn_Type = EkiOnOff
_Pm253AlmLosTrscPortn_Object = MibTableColumn
pm253AlmLosTrscPortn = _Pm253AlmLosTrscPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 3, 104, 1, 2),
    _Pm253AlmLosTrscPortn_Type()
)
pm253AlmLosTrscPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLosTrscPortn.setStatus("current")
_Pm253AlmFifoErrPortn_Type = EkiOnOff
_Pm253AlmFifoErrPortn_Object = MibTableColumn
pm253AlmFifoErrPortn = _Pm253AlmFifoErrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 3, 104, 1, 3),
    _Pm253AlmFifoErrPortn_Type()
)
pm253AlmFifoErrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmFifoErrPortn.setStatus("current")
_Pm253AlmRxLossOfLockPortn_Type = EkiOnOff
_Pm253AlmRxLossOfLockPortn_Object = MibTableColumn
pm253AlmRxLossOfLockPortn = _Pm253AlmRxLossOfLockPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 3, 104, 1, 4),
    _Pm253AlmRxLossOfLockPortn_Type()
)
pm253AlmRxLossOfLockPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmRxLossOfLockPortn.setStatus("current")
_Pm253AlmTxLossOfLockPortn_Type = EkiOnOff
_Pm253AlmTxLossOfLockPortn_Object = MibTableColumn
pm253AlmTxLossOfLockPortn = _Pm253AlmTxLossOfLockPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 3, 104, 1, 5),
    _Pm253AlmTxLossOfLockPortn_Type()
)
pm253AlmTxLossOfLockPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmTxLossOfLockPortn.setStatus("current")
_Pm253AlmClientAisDetPortn_Type = EkiOnOff
_Pm253AlmClientAisDetPortn_Object = MibTableColumn
pm253AlmClientAisDetPortn = _Pm253AlmClientAisDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 3, 104, 1, 6),
    _Pm253AlmClientAisDetPortn_Type()
)
pm253AlmClientAisDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientAisDetPortn.setStatus("current")
_Pm253AlmClientRdiDetPortn_Type = EkiOnOff
_Pm253AlmClientRdiDetPortn_Object = MibTableColumn
pm253AlmClientRdiDetPortn = _Pm253AlmClientRdiDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 3, 104, 1, 7),
    _Pm253AlmClientRdiDetPortn_Type()
)
pm253AlmClientRdiDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientRdiDetPortn.setStatus("current")
_Pm253AlmClientOofPortn_Type = EkiOnOff
_Pm253AlmClientOofPortn_Object = MibTableColumn
pm253AlmClientOofPortn = _Pm253AlmClientOofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 2, 3, 104, 1, 8),
    _Pm253AlmClientOofPortn_Type()
)
pm253AlmClientOofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmClientOofPortn.setStatus("current")
_Pm253AlmLine_ObjectIdentity = ObjectIdentity
pm253AlmLine = _Pm253AlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3)
)
_Pm253AlmLineNurg_ObjectIdentity = ObjectIdentity
pm253AlmLineNurg = _Pm253AlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 1)
)
_Pm253AlmlineDownS1Table_Object = MibTable
pm253AlmlineDownS1Table = _Pm253AlmlineDownS1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 1, 130)
)
if mibBuilder.loadTexts:
    pm253AlmlineDownS1Table.setStatus("current")
_Pm253AlmlineDownS1Entry_Object = MibTableRow
pm253AlmlineDownS1Entry = _Pm253AlmlineDownS1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 1, 130, 1)
)
pm253AlmlineDownS1Entry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253AlmlineDownS1Index"),
)
if mibBuilder.loadTexts:
    pm253AlmlineDownS1Entry.setStatus("current")


class _Pm253AlmlineDownS1Index_Type(Integer32):
    """Custom type pm253AlmlineDownS1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253AlmlineDownS1Index_Type.__name__ = "Integer32"
_Pm253AlmlineDownS1Index_Object = MibTableColumn
pm253AlmlineDownS1Index = _Pm253AlmlineDownS1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 1, 130, 1, 1),
    _Pm253AlmlineDownS1Index_Type()
)
pm253AlmlineDownS1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmlineDownS1Index.setStatus("current")


class _Pm253AlmlineDownS1Portn_Type(Integer32):
    """Custom type pm253AlmlineDownS1Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Pm253AlmlineDownS1Portn_Type.__name__ = "Integer32"
_Pm253AlmlineDownS1Portn_Object = MibTableColumn
pm253AlmlineDownS1Portn = _Pm253AlmlineDownS1Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 1, 130, 1, 2),
    _Pm253AlmlineDownS1Portn_Type()
)
pm253AlmlineDownS1Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmlineDownS1Portn.setStatus("current")
_Pm253AlmlineDownK1Table_Object = MibTable
pm253AlmlineDownK1Table = _Pm253AlmlineDownK1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 1, 131)
)
if mibBuilder.loadTexts:
    pm253AlmlineDownK1Table.setStatus("current")
_Pm253AlmlineDownK1Entry_Object = MibTableRow
pm253AlmlineDownK1Entry = _Pm253AlmlineDownK1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 1, 131, 1)
)
pm253AlmlineDownK1Entry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253AlmlineDownK1Index"),
)
if mibBuilder.loadTexts:
    pm253AlmlineDownK1Entry.setStatus("current")


class _Pm253AlmlineDownK1Index_Type(Integer32):
    """Custom type pm253AlmlineDownK1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253AlmlineDownK1Index_Type.__name__ = "Integer32"
_Pm253AlmlineDownK1Index_Object = MibTableColumn
pm253AlmlineDownK1Index = _Pm253AlmlineDownK1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 1, 131, 1, 1),
    _Pm253AlmlineDownK1Index_Type()
)
pm253AlmlineDownK1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmlineDownK1Index.setStatus("current")


class _Pm253AlmlineDownK1Portn_Type(Integer32):
    """Custom type pm253AlmlineDownK1Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Pm253AlmlineDownK1Portn_Type.__name__ = "Integer32"
_Pm253AlmlineDownK1Portn_Object = MibTableColumn
pm253AlmlineDownK1Portn = _Pm253AlmlineDownK1Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 1, 131, 1, 2),
    _Pm253AlmlineDownK1Portn_Type()
)
pm253AlmlineDownK1Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmlineDownK1Portn.setStatus("current")
_Pm253AlmlineDownK2Table_Object = MibTable
pm253AlmlineDownK2Table = _Pm253AlmlineDownK2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 1, 132)
)
if mibBuilder.loadTexts:
    pm253AlmlineDownK2Table.setStatus("current")
_Pm253AlmlineDownK2Entry_Object = MibTableRow
pm253AlmlineDownK2Entry = _Pm253AlmlineDownK2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 1, 132, 1)
)
pm253AlmlineDownK2Entry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253AlmlineDownK2Index"),
)
if mibBuilder.loadTexts:
    pm253AlmlineDownK2Entry.setStatus("current")


class _Pm253AlmlineDownK2Index_Type(Integer32):
    """Custom type pm253AlmlineDownK2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253AlmlineDownK2Index_Type.__name__ = "Integer32"
_Pm253AlmlineDownK2Index_Object = MibTableColumn
pm253AlmlineDownK2Index = _Pm253AlmlineDownK2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 1, 132, 1, 1),
    _Pm253AlmlineDownK2Index_Type()
)
pm253AlmlineDownK2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmlineDownK2Index.setStatus("current")


class _Pm253AlmlineDownK2Portn_Type(Integer32):
    """Custom type pm253AlmlineDownK2Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Pm253AlmlineDownK2Portn_Type.__name__ = "Integer32"
_Pm253AlmlineDownK2Portn_Object = MibTableColumn
pm253AlmlineDownK2Portn = _Pm253AlmlineDownK2Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 1, 132, 1, 2),
    _Pm253AlmlineDownK2Portn_Type()
)
pm253AlmlineDownK2Portn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmlineDownK2Portn.setStatus("current")
_Pm253AlmlineSfpWarnDdmTable_Object = MibTable
pm253AlmlineSfpWarnDdmTable = _Pm253AlmlineSfpWarnDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 1, 164)
)
if mibBuilder.loadTexts:
    pm253AlmlineSfpWarnDdmTable.setStatus("current")
_Pm253AlmlineSfpWarnDdmEntry_Object = MibTableRow
pm253AlmlineSfpWarnDdmEntry = _Pm253AlmlineSfpWarnDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 1, 164, 1)
)
pm253AlmlineSfpWarnDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253AlmlineSfpWarnDdmIndex"),
)
if mibBuilder.loadTexts:
    pm253AlmlineSfpWarnDdmEntry.setStatus("current")


class _Pm253AlmlineSfpWarnDdmIndex_Type(Integer32):
    """Custom type pm253AlmlineSfpWarnDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253AlmlineSfpWarnDdmIndex_Type.__name__ = "Integer32"
_Pm253AlmlineSfpWarnDdmIndex_Object = MibTableColumn
pm253AlmlineSfpWarnDdmIndex = _Pm253AlmlineSfpWarnDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 1, 164, 1, 1),
    _Pm253AlmlineSfpWarnDdmIndex_Type()
)
pm253AlmlineSfpWarnDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmlineSfpWarnDdmIndex.setStatus("current")
_Pm253AlmLineTxPwLowWngPortn_Type = EkiOnOff
_Pm253AlmLineTxPwLowWngPortn_Object = MibTableColumn
pm253AlmLineTxPwLowWngPortn = _Pm253AlmLineTxPwLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 1, 164, 1, 2),
    _Pm253AlmLineTxPwLowWngPortn_Type()
)
pm253AlmLineTxPwLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLineTxPwLowWngPortn.setStatus("current")
_Pm253AlmLineTxPwrHighWngPortn_Type = EkiOnOff
_Pm253AlmLineTxPwrHighWngPortn_Object = MibTableColumn
pm253AlmLineTxPwrHighWngPortn = _Pm253AlmLineTxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 1, 164, 1, 3),
    _Pm253AlmLineTxPwrHighWngPortn_Type()
)
pm253AlmLineTxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLineTxPwrHighWngPortn.setStatus("current")
_Pm253AlmLineTxBiasLowWngPortn_Type = EkiOnOff
_Pm253AlmLineTxBiasLowWngPortn_Object = MibTableColumn
pm253AlmLineTxBiasLowWngPortn = _Pm253AlmLineTxBiasLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 1, 164, 1, 4),
    _Pm253AlmLineTxBiasLowWngPortn_Type()
)
pm253AlmLineTxBiasLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLineTxBiasLowWngPortn.setStatus("current")
_Pm253AlmLineTxBiasHighWngPortn_Type = EkiOnOff
_Pm253AlmLineTxBiasHighWngPortn_Object = MibTableColumn
pm253AlmLineTxBiasHighWngPortn = _Pm253AlmLineTxBiasHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 1, 164, 1, 5),
    _Pm253AlmLineTxBiasHighWngPortn_Type()
)
pm253AlmLineTxBiasHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLineTxBiasHighWngPortn.setStatus("current")
_Pm253AlmLineVccLowWngPortn_Type = EkiOnOff
_Pm253AlmLineVccLowWngPortn_Object = MibTableColumn
pm253AlmLineVccLowWngPortn = _Pm253AlmLineVccLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 1, 164, 1, 6),
    _Pm253AlmLineVccLowWngPortn_Type()
)
pm253AlmLineVccLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLineVccLowWngPortn.setStatus("current")
_Pm253AlmLineVccHighWngPortn_Type = EkiOnOff
_Pm253AlmLineVccHighWngPortn_Object = MibTableColumn
pm253AlmLineVccHighWngPortn = _Pm253AlmLineVccHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 1, 164, 1, 7),
    _Pm253AlmLineVccHighWngPortn_Type()
)
pm253AlmLineVccHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLineVccHighWngPortn.setStatus("current")
_Pm253AlmLineTempLowWngPortn_Type = EkiOnOff
_Pm253AlmLineTempLowWngPortn_Object = MibTableColumn
pm253AlmLineTempLowWngPortn = _Pm253AlmLineTempLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 1, 164, 1, 8),
    _Pm253AlmLineTempLowWngPortn_Type()
)
pm253AlmLineTempLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLineTempLowWngPortn.setStatus("current")
_Pm253AlmLineTempHighWngPortn_Type = EkiOnOff
_Pm253AlmLineTempHighWngPortn_Object = MibTableColumn
pm253AlmLineTempHighWngPortn = _Pm253AlmLineTempHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 1, 164, 1, 9),
    _Pm253AlmLineTempHighWngPortn_Type()
)
pm253AlmLineTempHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLineTempHighWngPortn.setStatus("current")
_Pm253AlmLineRxPwrLowWngPortn_Type = EkiOnOff
_Pm253AlmLineRxPwrLowWngPortn_Object = MibTableColumn
pm253AlmLineRxPwrLowWngPortn = _Pm253AlmLineRxPwrLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 1, 164, 1, 16),
    _Pm253AlmLineRxPwrLowWngPortn_Type()
)
pm253AlmLineRxPwrLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLineRxPwrLowWngPortn.setStatus("current")
_Pm253AlmLineRxPwrHighWngPortn_Type = EkiOnOff
_Pm253AlmLineRxPwrHighWngPortn_Object = MibTableColumn
pm253AlmLineRxPwrHighWngPortn = _Pm253AlmLineRxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 1, 164, 1, 17),
    _Pm253AlmLineRxPwrHighWngPortn_Type()
)
pm253AlmLineRxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLineRxPwrHighWngPortn.setStatus("current")
_Pm253AlmLineUrg_ObjectIdentity = ObjectIdentity
pm253AlmLineUrg = _Pm253AlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 2)
)
_Pm253AlmlineSfpAlaDdmTable_Object = MibTable
pm253AlmlineSfpAlaDdmTable = _Pm253AlmlineSfpAlaDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 2, 162)
)
if mibBuilder.loadTexts:
    pm253AlmlineSfpAlaDdmTable.setStatus("current")
_Pm253AlmlineSfpAlaDdmEntry_Object = MibTableRow
pm253AlmlineSfpAlaDdmEntry = _Pm253AlmlineSfpAlaDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 2, 162, 1)
)
pm253AlmlineSfpAlaDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253AlmlineSfpAlaDdmIndex"),
)
if mibBuilder.loadTexts:
    pm253AlmlineSfpAlaDdmEntry.setStatus("current")


class _Pm253AlmlineSfpAlaDdmIndex_Type(Integer32):
    """Custom type pm253AlmlineSfpAlaDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253AlmlineSfpAlaDdmIndex_Type.__name__ = "Integer32"
_Pm253AlmlineSfpAlaDdmIndex_Object = MibTableColumn
pm253AlmlineSfpAlaDdmIndex = _Pm253AlmlineSfpAlaDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 2, 162, 1, 1),
    _Pm253AlmlineSfpAlaDdmIndex_Type()
)
pm253AlmlineSfpAlaDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmlineSfpAlaDdmIndex.setStatus("current")
_Pm253AlmLineTxPwrLowAlaPortn_Type = EkiOnOff
_Pm253AlmLineTxPwrLowAlaPortn_Object = MibTableColumn
pm253AlmLineTxPwrLowAlaPortn = _Pm253AlmLineTxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 2, 162, 1, 2),
    _Pm253AlmLineTxPwrLowAlaPortn_Type()
)
pm253AlmLineTxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLineTxPwrLowAlaPortn.setStatus("current")
_Pm253AlmLineTxPwrHighAlaPortn_Type = EkiOnOff
_Pm253AlmLineTxPwrHighAlaPortn_Object = MibTableColumn
pm253AlmLineTxPwrHighAlaPortn = _Pm253AlmLineTxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 2, 162, 1, 3),
    _Pm253AlmLineTxPwrHighAlaPortn_Type()
)
pm253AlmLineTxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLineTxPwrHighAlaPortn.setStatus("current")
_Pm253AlmLineTxBiasLowAlaPortn_Type = EkiOnOff
_Pm253AlmLineTxBiasLowAlaPortn_Object = MibTableColumn
pm253AlmLineTxBiasLowAlaPortn = _Pm253AlmLineTxBiasLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 2, 162, 1, 4),
    _Pm253AlmLineTxBiasLowAlaPortn_Type()
)
pm253AlmLineTxBiasLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLineTxBiasLowAlaPortn.setStatus("current")
_Pm253AlmLineTxBiasHighAlaPortn_Type = EkiOnOff
_Pm253AlmLineTxBiasHighAlaPortn_Object = MibTableColumn
pm253AlmLineTxBiasHighAlaPortn = _Pm253AlmLineTxBiasHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 2, 162, 1, 5),
    _Pm253AlmLineTxBiasHighAlaPortn_Type()
)
pm253AlmLineTxBiasHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLineTxBiasHighAlaPortn.setStatus("current")
_Pm253AlmLineVccLowAlaPortn_Type = EkiOnOff
_Pm253AlmLineVccLowAlaPortn_Object = MibTableColumn
pm253AlmLineVccLowAlaPortn = _Pm253AlmLineVccLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 2, 162, 1, 6),
    _Pm253AlmLineVccLowAlaPortn_Type()
)
pm253AlmLineVccLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLineVccLowAlaPortn.setStatus("current")
_Pm253AlmLineVccHighAlaPortn_Type = EkiOnOff
_Pm253AlmLineVccHighAlaPortn_Object = MibTableColumn
pm253AlmLineVccHighAlaPortn = _Pm253AlmLineVccHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 2, 162, 1, 7),
    _Pm253AlmLineVccHighAlaPortn_Type()
)
pm253AlmLineVccHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLineVccHighAlaPortn.setStatus("current")
_Pm253AlmLineTempLowAlaPortn_Type = EkiOnOff
_Pm253AlmLineTempLowAlaPortn_Object = MibTableColumn
pm253AlmLineTempLowAlaPortn = _Pm253AlmLineTempLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 2, 162, 1, 8),
    _Pm253AlmLineTempLowAlaPortn_Type()
)
pm253AlmLineTempLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLineTempLowAlaPortn.setStatus("current")
_Pm253AlmLineTempHighAlaPortn_Type = EkiOnOff
_Pm253AlmLineTempHighAlaPortn_Object = MibTableColumn
pm253AlmLineTempHighAlaPortn = _Pm253AlmLineTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 2, 162, 1, 9),
    _Pm253AlmLineTempHighAlaPortn_Type()
)
pm253AlmLineTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLineTempHighAlaPortn.setStatus("current")
_Pm253AlmLineRxPwrLowAlaPortn_Type = EkiOnOff
_Pm253AlmLineRxPwrLowAlaPortn_Object = MibTableColumn
pm253AlmLineRxPwrLowAlaPortn = _Pm253AlmLineRxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 2, 162, 1, 16),
    _Pm253AlmLineRxPwrLowAlaPortn_Type()
)
pm253AlmLineRxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLineRxPwrLowAlaPortn.setStatus("current")
_Pm253AlmLineRxPwrHighAlaPortn_Type = EkiOnOff
_Pm253AlmLineRxPwrHighAlaPortn_Object = MibTableColumn
pm253AlmLineRxPwrHighAlaPortn = _Pm253AlmLineRxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 2, 162, 1, 17),
    _Pm253AlmLineRxPwrHighAlaPortn_Type()
)
pm253AlmLineRxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLineRxPwrHighAlaPortn.setStatus("current")
_Pm253AlmLineCrit_ObjectIdentity = ObjectIdentity
pm253AlmLineCrit = _Pm253AlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 3)
)
_Pm253AlmsynthAlmLineTable_Object = MibTable
pm253AlmsynthAlmLineTable = _Pm253AlmsynthAlmLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 3, 4)
)
if mibBuilder.loadTexts:
    pm253AlmsynthAlmLineTable.setStatus("current")
_Pm253AlmsynthAlmLineEntry_Object = MibTableRow
pm253AlmsynthAlmLineEntry = _Pm253AlmsynthAlmLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 3, 4, 1)
)
pm253AlmsynthAlmLineEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253AlmsynthAlmLineIndex"),
)
if mibBuilder.loadTexts:
    pm253AlmsynthAlmLineEntry.setStatus("current")


class _Pm253AlmsynthAlmLineIndex_Type(Integer32):
    """Custom type pm253AlmsynthAlmLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253AlmsynthAlmLineIndex_Type.__name__ = "Integer32"
_Pm253AlmsynthAlmLineIndex_Object = MibTableColumn
pm253AlmsynthAlmLineIndex = _Pm253AlmsynthAlmLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 3, 4, 1, 1),
    _Pm253AlmsynthAlmLineIndex_Type()
)
pm253AlmsynthAlmLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmsynthAlmLineIndex.setStatus("current")
_Pm253AlmLineSfpAbsentPortn_Type = EkiOnOff
_Pm253AlmLineSfpAbsentPortn_Object = MibTableColumn
pm253AlmLineSfpAbsentPortn = _Pm253AlmLineSfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 3, 4, 1, 2),
    _Pm253AlmLineSfpAbsentPortn_Type()
)
pm253AlmLineSfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLineSfpAbsentPortn.setStatus("current")
_Pm253AlmLineDdmAbsentPortn_Type = EkiOnOff
_Pm253AlmLineDdmAbsentPortn_Object = MibTableColumn
pm253AlmLineDdmAbsentPortn = _Pm253AlmLineDdmAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 3, 4, 1, 3),
    _Pm253AlmLineDdmAbsentPortn_Type()
)
pm253AlmLineDdmAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLineDdmAbsentPortn.setStatus("current")
_Pm253AlmLineHwFailPortn_Type = EkiOnOff
_Pm253AlmLineHwFailPortn_Object = MibTableColumn
pm253AlmLineHwFailPortn = _Pm253AlmLineHwFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 3, 4, 1, 5),
    _Pm253AlmLineHwFailPortn_Type()
)
pm253AlmLineHwFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLineHwFailPortn.setStatus("current")
_Pm253AlmLineLsdPortn_Type = EkiOnOff
_Pm253AlmLineLsdPortn_Object = MibTableColumn
pm253AlmLineLsdPortn = _Pm253AlmLineLsdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 3, 4, 1, 6),
    _Pm253AlmLineLsdPortn_Type()
)
pm253AlmLineLsdPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLineLsdPortn.setStatus("current")
_Pm253AlmLineLocalOosPortn_Type = EkiOnOff
_Pm253AlmLineLocalOosPortn_Object = MibTableColumn
pm253AlmLineLocalOosPortn = _Pm253AlmLineLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 3, 4, 1, 7),
    _Pm253AlmLineLocalOosPortn_Type()
)
pm253AlmLineLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLineLocalOosPortn.setStatus("current")
_Pm253AlmLineUpRdiInsPortn_Type = EkiOnOff
_Pm253AlmLineUpRdiInsPortn_Object = MibTableColumn
pm253AlmLineUpRdiInsPortn = _Pm253AlmLineUpRdiInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 3, 4, 1, 9),
    _Pm253AlmLineUpRdiInsPortn_Type()
)
pm253AlmLineUpRdiInsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLineUpRdiInsPortn.setStatus("current")
_Pm253AlmLineDdmWarningPortn_Type = EkiOnOff
_Pm253AlmLineDdmWarningPortn_Object = MibTableColumn
pm253AlmLineDdmWarningPortn = _Pm253AlmLineDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 3, 4, 1, 10),
    _Pm253AlmLineDdmWarningPortn_Type()
)
pm253AlmLineDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLineDdmWarningPortn.setStatus("current")
_Pm253AlmLineDdmAlmPortn_Type = EkiOnOff
_Pm253AlmLineDdmAlmPortn_Object = MibTableColumn
pm253AlmLineDdmAlmPortn = _Pm253AlmLineDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 3, 4, 1, 11),
    _Pm253AlmLineDdmAlmPortn_Type()
)
pm253AlmLineDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLineDdmAlmPortn.setStatus("current")
_Pm253AlmLineFailPortn_Type = EkiOnOff
_Pm253AlmLineFailPortn_Object = MibTableColumn
pm253AlmLineFailPortn = _Pm253AlmLineFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 3, 4, 1, 13),
    _Pm253AlmLineFailPortn_Type()
)
pm253AlmLineFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLineFailPortn.setStatus("current")
_Pm253AlmLineActivePortn_Type = EkiOnOff
_Pm253AlmLineActivePortn_Object = MibTableColumn
pm253AlmLineActivePortn = _Pm253AlmLineActivePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 3, 4, 1, 17),
    _Pm253AlmLineActivePortn_Type()
)
pm253AlmLineActivePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLineActivePortn.setStatus("current")
_Pm253AlmlineDfrmAlmTable_Object = MibTable
pm253AlmlineDfrmAlmTable = _Pm253AlmlineDfrmAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 3, 128)
)
if mibBuilder.loadTexts:
    pm253AlmlineDfrmAlmTable.setStatus("current")
_Pm253AlmlineDfrmAlmEntry_Object = MibTableRow
pm253AlmlineDfrmAlmEntry = _Pm253AlmlineDfrmAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 3, 128, 1)
)
pm253AlmlineDfrmAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253AlmlineDfrmAlmIndex"),
)
if mibBuilder.loadTexts:
    pm253AlmlineDfrmAlmEntry.setStatus("current")


class _Pm253AlmlineDfrmAlmIndex_Type(Integer32):
    """Custom type pm253AlmlineDfrmAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253AlmlineDfrmAlmIndex_Type.__name__ = "Integer32"
_Pm253AlmlineDfrmAlmIndex_Object = MibTableColumn
pm253AlmlineDfrmAlmIndex = _Pm253AlmlineDfrmAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 3, 128, 1, 1),
    _Pm253AlmlineDfrmAlmIndex_Type()
)
pm253AlmlineDfrmAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmlineDfrmAlmIndex.setStatus("current")
_Pm253AlmLineDwAisDetPortn_Type = EkiOnOff
_Pm253AlmLineDwAisDetPortn_Object = MibTableColumn
pm253AlmLineDwAisDetPortn = _Pm253AlmLineDwAisDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 3, 128, 1, 2),
    _Pm253AlmLineDwAisDetPortn_Type()
)
pm253AlmLineDwAisDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLineDwAisDetPortn.setStatus("current")
_Pm253AlmLineDwRdiDetPortn_Type = EkiOnOff
_Pm253AlmLineDwRdiDetPortn_Object = MibTableColumn
pm253AlmLineDwRdiDetPortn = _Pm253AlmLineDwRdiDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 3, 128, 1, 3),
    _Pm253AlmLineDwRdiDetPortn_Type()
)
pm253AlmLineDwRdiDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLineDwRdiDetPortn.setStatus("current")
_Pm253AlmLineDwOofPortn_Type = EkiOnOff
_Pm253AlmLineDwOofPortn_Object = MibTableColumn
pm253AlmLineDwOofPortn = _Pm253AlmLineDwOofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 3, 128, 1, 4),
    _Pm253AlmLineDwOofPortn_Type()
)
pm253AlmLineDwOofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLineDwOofPortn.setStatus("current")
_Pm253AlmLineDwLofPortn_Type = EkiOnOff
_Pm253AlmLineDwLofPortn_Object = MibTableColumn
pm253AlmLineDwLofPortn = _Pm253AlmLineDwLofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 3, 128, 1, 5),
    _Pm253AlmLineDwLofPortn_Type()
)
pm253AlmLineDwLofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLineDwLofPortn.setStatus("current")
_Pm253AlmDwLopFirstPortn_Type = EkiOnOff
_Pm253AlmDwLopFirstPortn_Object = MibTableColumn
pm253AlmDwLopFirstPortn = _Pm253AlmDwLopFirstPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 3, 128, 1, 10),
    _Pm253AlmDwLopFirstPortn_Type()
)
pm253AlmDwLopFirstPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmDwLopFirstPortn.setStatus("current")
_Pm253AlmDwAuAisFirstPortn_Type = EkiOnOff
_Pm253AlmDwAuAisFirstPortn_Object = MibTableColumn
pm253AlmDwAuAisFirstPortn = _Pm253AlmDwAuAisFirstPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 3, 128, 1, 11),
    _Pm253AlmDwAuAisFirstPortn_Type()
)
pm253AlmDwAuAisFirstPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmDwAuAisFirstPortn.setStatus("current")
_Pm253AlmDwLopSecondPortn_Type = EkiOnOff
_Pm253AlmDwLopSecondPortn_Object = MibTableColumn
pm253AlmDwLopSecondPortn = _Pm253AlmDwLopSecondPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 3, 128, 1, 12),
    _Pm253AlmDwLopSecondPortn_Type()
)
pm253AlmDwLopSecondPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmDwLopSecondPortn.setStatus("current")
_Pm253AlmDwAuAisSecondPortn_Type = EkiOnOff
_Pm253AlmDwAuAisSecondPortn_Object = MibTableColumn
pm253AlmDwAuAisSecondPortn = _Pm253AlmDwAuAisSecondPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 3, 128, 1, 13),
    _Pm253AlmDwAuAisSecondPortn_Type()
)
pm253AlmDwAuAisSecondPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmDwAuAisSecondPortn.setStatus("current")
_Pm253AlmlineIoAlmTable_Object = MibTable
pm253AlmlineIoAlmTable = _Pm253AlmlineIoAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 3, 160)
)
if mibBuilder.loadTexts:
    pm253AlmlineIoAlmTable.setStatus("current")
_Pm253AlmlineIoAlmEntry_Object = MibTableRow
pm253AlmlineIoAlmEntry = _Pm253AlmlineIoAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 3, 160, 1)
)
pm253AlmlineIoAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253AlmlineIoAlmIndex"),
)
if mibBuilder.loadTexts:
    pm253AlmlineIoAlmEntry.setStatus("current")


class _Pm253AlmlineIoAlmIndex_Type(Integer32):
    """Custom type pm253AlmlineIoAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253AlmlineIoAlmIndex_Type.__name__ = "Integer32"
_Pm253AlmlineIoAlmIndex_Object = MibTableColumn
pm253AlmlineIoAlmIndex = _Pm253AlmlineIoAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 3, 160, 1, 1),
    _Pm253AlmlineIoAlmIndex_Type()
)
pm253AlmlineIoAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmlineIoAlmIndex.setStatus("current")
_Pm253AlmLineUpLasFailPortn_Type = EkiOnOff
_Pm253AlmLineUpLasFailPortn_Object = MibTableColumn
pm253AlmLineUpLasFailPortn = _Pm253AlmLineUpLasFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 3, 160, 1, 2),
    _Pm253AlmLineUpLasFailPortn_Type()
)
pm253AlmLineUpLasFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLineUpLasFailPortn.setStatus("current")
_Pm253AlmLineDwLosPortn_Type = EkiOnOff
_Pm253AlmLineDwLosPortn_Object = MibTableColumn
pm253AlmLineDwLosPortn = _Pm253AlmLineDwLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 2, 3, 3, 160, 1, 5),
    _Pm253AlmLineDwLosPortn_Type()
)
pm253AlmLineDwLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253AlmLineDwLosPortn.setStatus("current")
_Pm253measures_ObjectIdentity = ObjectIdentity
pm253measures = _Pm253measures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3)
)
_Pm253MesrOther_ObjectIdentity = ObjectIdentity
pm253MesrOther = _Pm253MesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 1)
)
_Pm253MesrPort_ObjectIdentity = ObjectIdentity
pm253MesrPort = _Pm253MesrPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 2)
)
_Pm253MesrclientTempMeasTable_Object = MibTable
pm253MesrclientTempMeasTable = _Pm253MesrclientTempMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 2, 16)
)
if mibBuilder.loadTexts:
    pm253MesrclientTempMeasTable.setStatus("current")
_Pm253MesrclientTempMeasEntry_Object = MibTableRow
pm253MesrclientTempMeasEntry = _Pm253MesrclientTempMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 2, 16, 1)
)
pm253MesrclientTempMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253MesrclientTempMeasIndex"),
)
if mibBuilder.loadTexts:
    pm253MesrclientTempMeasEntry.setStatus("current")


class _Pm253MesrclientTempMeasIndex_Type(Integer32):
    """Custom type pm253MesrclientTempMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253MesrclientTempMeasIndex_Type.__name__ = "Integer32"
_Pm253MesrclientTempMeasIndex_Object = MibTableColumn
pm253MesrclientTempMeasIndex = _Pm253MesrclientTempMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 2, 16, 1, 1),
    _Pm253MesrclientTempMeasIndex_Type()
)
pm253MesrclientTempMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MesrclientTempMeasIndex.setStatus("current")


class _Pm253MesrclientTempMeasPortn_Type(Integer32):
    """Custom type pm253MesrclientTempMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm253MesrclientTempMeasPortn_Type.__name__ = "Integer32"
_Pm253MesrclientTempMeasPortn_Object = MibTableColumn
pm253MesrclientTempMeasPortn = _Pm253MesrclientTempMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 2, 16, 1, 2),
    _Pm253MesrclientTempMeasPortn_Type()
)
pm253MesrclientTempMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MesrclientTempMeasPortn.setStatus("current")
_Pm253MesrclientVoltMeasTable_Object = MibTable
pm253MesrclientVoltMeasTable = _Pm253MesrclientVoltMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 2, 24)
)
if mibBuilder.loadTexts:
    pm253MesrclientVoltMeasTable.setStatus("current")
_Pm253MesrclientVoltMeasEntry_Object = MibTableRow
pm253MesrclientVoltMeasEntry = _Pm253MesrclientVoltMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 2, 24, 1)
)
pm253MesrclientVoltMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253MesrclientVoltMeasIndex"),
)
if mibBuilder.loadTexts:
    pm253MesrclientVoltMeasEntry.setStatus("current")


class _Pm253MesrclientVoltMeasIndex_Type(Integer32):
    """Custom type pm253MesrclientVoltMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253MesrclientVoltMeasIndex_Type.__name__ = "Integer32"
_Pm253MesrclientVoltMeasIndex_Object = MibTableColumn
pm253MesrclientVoltMeasIndex = _Pm253MesrclientVoltMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 2, 24, 1, 1),
    _Pm253MesrclientVoltMeasIndex_Type()
)
pm253MesrclientVoltMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MesrclientVoltMeasIndex.setStatus("current")


class _Pm253MesrclientVoltMeasPortn_Type(Integer32):
    """Custom type pm253MesrclientVoltMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm253MesrclientVoltMeasPortn_Type.__name__ = "Integer32"
_Pm253MesrclientVoltMeasPortn_Object = MibTableColumn
pm253MesrclientVoltMeasPortn = _Pm253MesrclientVoltMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 2, 24, 1, 2),
    _Pm253MesrclientVoltMeasPortn_Type()
)
pm253MesrclientVoltMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MesrclientVoltMeasPortn.setStatus("current")
_Pm253MesrclientBiasMeasTable_Object = MibTable
pm253MesrclientBiasMeasTable = _Pm253MesrclientBiasMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 2, 32)
)
if mibBuilder.loadTexts:
    pm253MesrclientBiasMeasTable.setStatus("current")
_Pm253MesrclientBiasMeasEntry_Object = MibTableRow
pm253MesrclientBiasMeasEntry = _Pm253MesrclientBiasMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 2, 32, 1)
)
pm253MesrclientBiasMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253MesrclientBiasMeasIndex"),
)
if mibBuilder.loadTexts:
    pm253MesrclientBiasMeasEntry.setStatus("current")


class _Pm253MesrclientBiasMeasIndex_Type(Integer32):
    """Custom type pm253MesrclientBiasMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253MesrclientBiasMeasIndex_Type.__name__ = "Integer32"
_Pm253MesrclientBiasMeasIndex_Object = MibTableColumn
pm253MesrclientBiasMeasIndex = _Pm253MesrclientBiasMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 2, 32, 1, 1),
    _Pm253MesrclientBiasMeasIndex_Type()
)
pm253MesrclientBiasMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MesrclientBiasMeasIndex.setStatus("current")


class _Pm253MesrclientBiasMeasPortn_Type(Integer32):
    """Custom type pm253MesrclientBiasMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm253MesrclientBiasMeasPortn_Type.__name__ = "Integer32"
_Pm253MesrclientBiasMeasPortn_Object = MibTableColumn
pm253MesrclientBiasMeasPortn = _Pm253MesrclientBiasMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 2, 32, 1, 2),
    _Pm253MesrclientBiasMeasPortn_Type()
)
pm253MesrclientBiasMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MesrclientBiasMeasPortn.setStatus("current")
_Pm253MesrclientTxpwrMeasTable_Object = MibTable
pm253MesrclientTxpwrMeasTable = _Pm253MesrclientTxpwrMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 2, 40)
)
if mibBuilder.loadTexts:
    pm253MesrclientTxpwrMeasTable.setStatus("current")
_Pm253MesrclientTxpwrMeasEntry_Object = MibTableRow
pm253MesrclientTxpwrMeasEntry = _Pm253MesrclientTxpwrMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 2, 40, 1)
)
pm253MesrclientTxpwrMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253MesrclientTxpwrMeasIndex"),
)
if mibBuilder.loadTexts:
    pm253MesrclientTxpwrMeasEntry.setStatus("current")


class _Pm253MesrclientTxpwrMeasIndex_Type(Integer32):
    """Custom type pm253MesrclientTxpwrMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253MesrclientTxpwrMeasIndex_Type.__name__ = "Integer32"
_Pm253MesrclientTxpwrMeasIndex_Object = MibTableColumn
pm253MesrclientTxpwrMeasIndex = _Pm253MesrclientTxpwrMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 2, 40, 1, 1),
    _Pm253MesrclientTxpwrMeasIndex_Type()
)
pm253MesrclientTxpwrMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MesrclientTxpwrMeasIndex.setStatus("current")


class _Pm253MesrclientTxpwrMeasPortn_Type(Integer32):
    """Custom type pm253MesrclientTxpwrMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm253MesrclientTxpwrMeasPortn_Type.__name__ = "Integer32"
_Pm253MesrclientTxpwrMeasPortn_Object = MibTableColumn
pm253MesrclientTxpwrMeasPortn = _Pm253MesrclientTxpwrMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 2, 40, 1, 2),
    _Pm253MesrclientTxpwrMeasPortn_Type()
)
pm253MesrclientTxpwrMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MesrclientTxpwrMeasPortn.setStatus("current")
_Pm253MesrclientRxpwrMeasTable_Object = MibTable
pm253MesrclientRxpwrMeasTable = _Pm253MesrclientRxpwrMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 2, 48)
)
if mibBuilder.loadTexts:
    pm253MesrclientRxpwrMeasTable.setStatus("current")
_Pm253MesrclientRxpwrMeasEntry_Object = MibTableRow
pm253MesrclientRxpwrMeasEntry = _Pm253MesrclientRxpwrMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 2, 48, 1)
)
pm253MesrclientRxpwrMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253MesrclientRxpwrMeasIndex"),
)
if mibBuilder.loadTexts:
    pm253MesrclientRxpwrMeasEntry.setStatus("current")


class _Pm253MesrclientRxpwrMeasIndex_Type(Integer32):
    """Custom type pm253MesrclientRxpwrMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253MesrclientRxpwrMeasIndex_Type.__name__ = "Integer32"
_Pm253MesrclientRxpwrMeasIndex_Object = MibTableColumn
pm253MesrclientRxpwrMeasIndex = _Pm253MesrclientRxpwrMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 2, 48, 1, 1),
    _Pm253MesrclientRxpwrMeasIndex_Type()
)
pm253MesrclientRxpwrMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MesrclientRxpwrMeasIndex.setStatus("current")


class _Pm253MesrclientRxpwrMeasPortn_Type(Integer32):
    """Custom type pm253MesrclientRxpwrMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm253MesrclientRxpwrMeasPortn_Type.__name__ = "Integer32"
_Pm253MesrclientRxpwrMeasPortn_Object = MibTableColumn
pm253MesrclientRxpwrMeasPortn = _Pm253MesrclientRxpwrMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 2, 48, 1, 2),
    _Pm253MesrclientRxpwrMeasPortn_Type()
)
pm253MesrclientRxpwrMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MesrclientRxpwrMeasPortn.setStatus("current")
_Pm253MesrLine_ObjectIdentity = ObjectIdentity
pm253MesrLine = _Pm253MesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 3)
)
_Pm253MesrlineTempMeasTable_Object = MibTable
pm253MesrlineTempMeasTable = _Pm253MesrlineTempMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 3, 160)
)
if mibBuilder.loadTexts:
    pm253MesrlineTempMeasTable.setStatus("current")
_Pm253MesrlineTempMeasEntry_Object = MibTableRow
pm253MesrlineTempMeasEntry = _Pm253MesrlineTempMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 3, 160, 1)
)
pm253MesrlineTempMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253MesrlineTempMeasIndex"),
)
if mibBuilder.loadTexts:
    pm253MesrlineTempMeasEntry.setStatus("current")


class _Pm253MesrlineTempMeasIndex_Type(Integer32):
    """Custom type pm253MesrlineTempMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253MesrlineTempMeasIndex_Type.__name__ = "Integer32"
_Pm253MesrlineTempMeasIndex_Object = MibTableColumn
pm253MesrlineTempMeasIndex = _Pm253MesrlineTempMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 3, 160, 1, 1),
    _Pm253MesrlineTempMeasIndex_Type()
)
pm253MesrlineTempMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MesrlineTempMeasIndex.setStatus("current")


class _Pm253MesrlineTempMeasPortn_Type(Integer32):
    """Custom type pm253MesrlineTempMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm253MesrlineTempMeasPortn_Type.__name__ = "Integer32"
_Pm253MesrlineTempMeasPortn_Object = MibTableColumn
pm253MesrlineTempMeasPortn = _Pm253MesrlineTempMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 3, 160, 1, 2),
    _Pm253MesrlineTempMeasPortn_Type()
)
pm253MesrlineTempMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MesrlineTempMeasPortn.setStatus("current")
_Pm253MesrlineVoltMeasTable_Object = MibTable
pm253MesrlineVoltMeasTable = _Pm253MesrlineVoltMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 3, 161)
)
if mibBuilder.loadTexts:
    pm253MesrlineVoltMeasTable.setStatus("current")
_Pm253MesrlineVoltMeasEntry_Object = MibTableRow
pm253MesrlineVoltMeasEntry = _Pm253MesrlineVoltMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 3, 161, 1)
)
pm253MesrlineVoltMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253MesrlineVoltMeasIndex"),
)
if mibBuilder.loadTexts:
    pm253MesrlineVoltMeasEntry.setStatus("current")


class _Pm253MesrlineVoltMeasIndex_Type(Integer32):
    """Custom type pm253MesrlineVoltMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253MesrlineVoltMeasIndex_Type.__name__ = "Integer32"
_Pm253MesrlineVoltMeasIndex_Object = MibTableColumn
pm253MesrlineVoltMeasIndex = _Pm253MesrlineVoltMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 3, 161, 1, 1),
    _Pm253MesrlineVoltMeasIndex_Type()
)
pm253MesrlineVoltMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MesrlineVoltMeasIndex.setStatus("current")


class _Pm253MesrlineVoltMeasPortn_Type(Integer32):
    """Custom type pm253MesrlineVoltMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm253MesrlineVoltMeasPortn_Type.__name__ = "Integer32"
_Pm253MesrlineVoltMeasPortn_Object = MibTableColumn
pm253MesrlineVoltMeasPortn = _Pm253MesrlineVoltMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 3, 161, 1, 2),
    _Pm253MesrlineVoltMeasPortn_Type()
)
pm253MesrlineVoltMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MesrlineVoltMeasPortn.setStatus("current")
_Pm253MesrlineBiasMeasTable_Object = MibTable
pm253MesrlineBiasMeasTable = _Pm253MesrlineBiasMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 3, 162)
)
if mibBuilder.loadTexts:
    pm253MesrlineBiasMeasTable.setStatus("current")
_Pm253MesrlineBiasMeasEntry_Object = MibTableRow
pm253MesrlineBiasMeasEntry = _Pm253MesrlineBiasMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 3, 162, 1)
)
pm253MesrlineBiasMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253MesrlineBiasMeasIndex"),
)
if mibBuilder.loadTexts:
    pm253MesrlineBiasMeasEntry.setStatus("current")


class _Pm253MesrlineBiasMeasIndex_Type(Integer32):
    """Custom type pm253MesrlineBiasMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253MesrlineBiasMeasIndex_Type.__name__ = "Integer32"
_Pm253MesrlineBiasMeasIndex_Object = MibTableColumn
pm253MesrlineBiasMeasIndex = _Pm253MesrlineBiasMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 3, 162, 1, 1),
    _Pm253MesrlineBiasMeasIndex_Type()
)
pm253MesrlineBiasMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MesrlineBiasMeasIndex.setStatus("current")


class _Pm253MesrlineBiasMeasPortn_Type(Integer32):
    """Custom type pm253MesrlineBiasMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm253MesrlineBiasMeasPortn_Type.__name__ = "Integer32"
_Pm253MesrlineBiasMeasPortn_Object = MibTableColumn
pm253MesrlineBiasMeasPortn = _Pm253MesrlineBiasMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 3, 162, 1, 2),
    _Pm253MesrlineBiasMeasPortn_Type()
)
pm253MesrlineBiasMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MesrlineBiasMeasPortn.setStatus("current")
_Pm253MesrlineTxpwrMeasTable_Object = MibTable
pm253MesrlineTxpwrMeasTable = _Pm253MesrlineTxpwrMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 3, 163)
)
if mibBuilder.loadTexts:
    pm253MesrlineTxpwrMeasTable.setStatus("current")
_Pm253MesrlineTxpwrMeasEntry_Object = MibTableRow
pm253MesrlineTxpwrMeasEntry = _Pm253MesrlineTxpwrMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 3, 163, 1)
)
pm253MesrlineTxpwrMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253MesrlineTxpwrMeasIndex"),
)
if mibBuilder.loadTexts:
    pm253MesrlineTxpwrMeasEntry.setStatus("current")


class _Pm253MesrlineTxpwrMeasIndex_Type(Integer32):
    """Custom type pm253MesrlineTxpwrMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253MesrlineTxpwrMeasIndex_Type.__name__ = "Integer32"
_Pm253MesrlineTxpwrMeasIndex_Object = MibTableColumn
pm253MesrlineTxpwrMeasIndex = _Pm253MesrlineTxpwrMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 3, 163, 1, 1),
    _Pm253MesrlineTxpwrMeasIndex_Type()
)
pm253MesrlineTxpwrMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MesrlineTxpwrMeasIndex.setStatus("current")


class _Pm253MesrlineTxpwrMeasPortn_Type(Integer32):
    """Custom type pm253MesrlineTxpwrMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm253MesrlineTxpwrMeasPortn_Type.__name__ = "Integer32"
_Pm253MesrlineTxpwrMeasPortn_Object = MibTableColumn
pm253MesrlineTxpwrMeasPortn = _Pm253MesrlineTxpwrMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 3, 163, 1, 2),
    _Pm253MesrlineTxpwrMeasPortn_Type()
)
pm253MesrlineTxpwrMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MesrlineTxpwrMeasPortn.setStatus("current")
_Pm253MesrlineRxpwrMeasTable_Object = MibTable
pm253MesrlineRxpwrMeasTable = _Pm253MesrlineRxpwrMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 3, 164)
)
if mibBuilder.loadTexts:
    pm253MesrlineRxpwrMeasTable.setStatus("current")
_Pm253MesrlineRxpwrMeasEntry_Object = MibTableRow
pm253MesrlineRxpwrMeasEntry = _Pm253MesrlineRxpwrMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 3, 164, 1)
)
pm253MesrlineRxpwrMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253MesrlineRxpwrMeasIndex"),
)
if mibBuilder.loadTexts:
    pm253MesrlineRxpwrMeasEntry.setStatus("current")


class _Pm253MesrlineRxpwrMeasIndex_Type(Integer32):
    """Custom type pm253MesrlineRxpwrMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253MesrlineRxpwrMeasIndex_Type.__name__ = "Integer32"
_Pm253MesrlineRxpwrMeasIndex_Object = MibTableColumn
pm253MesrlineRxpwrMeasIndex = _Pm253MesrlineRxpwrMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 3, 164, 1, 1),
    _Pm253MesrlineRxpwrMeasIndex_Type()
)
pm253MesrlineRxpwrMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MesrlineRxpwrMeasIndex.setStatus("current")


class _Pm253MesrlineRxpwrMeasPortn_Type(Integer32):
    """Custom type pm253MesrlineRxpwrMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm253MesrlineRxpwrMeasPortn_Type.__name__ = "Integer32"
_Pm253MesrlineRxpwrMeasPortn_Object = MibTableColumn
pm253MesrlineRxpwrMeasPortn = _Pm253MesrlineRxpwrMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 3, 3, 164, 1, 2),
    _Pm253MesrlineRxpwrMeasPortn_Type()
)
pm253MesrlineRxpwrMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MesrlineRxpwrMeasPortn.setStatus("current")
_Pm253counters_ObjectIdentity = ObjectIdentity
pm253counters = _Pm253counters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4)
)
_Pm253CntOther_ObjectIdentity = ObjectIdentity
pm253CntOther = _Pm253CntOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 1)
)
_Pm253CntPort_ObjectIdentity = ObjectIdentity
pm253CntPort = _Pm253CntPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 2)
)
_Pm253CntclientUpRaRemCntTable_Object = MibTable
pm253CntclientUpRaRemCntTable = _Pm253CntclientUpRaRemCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 2, 16)
)
if mibBuilder.loadTexts:
    pm253CntclientUpRaRemCntTable.setStatus("current")
_Pm253CntclientUpRaRemCntEntry_Object = MibTableRow
pm253CntclientUpRaRemCntEntry = _Pm253CntclientUpRaRemCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 2, 16, 1)
)
pm253CntclientUpRaRemCntEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253CntclientUpRaRemCntIndex"),
)
if mibBuilder.loadTexts:
    pm253CntclientUpRaRemCntEntry.setStatus("current")


class _Pm253CntclientUpRaRemCntIndex_Type(Integer32):
    """Custom type pm253CntclientUpRaRemCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253CntclientUpRaRemCntIndex_Type.__name__ = "Integer32"
_Pm253CntclientUpRaRemCntIndex_Object = MibTableColumn
pm253CntclientUpRaRemCntIndex = _Pm253CntclientUpRaRemCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 2, 16, 1, 1),
    _Pm253CntclientUpRaRemCntIndex_Type()
)
pm253CntclientUpRaRemCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CntclientUpRaRemCntIndex.setStatus("current")
_Pm253CntclientUpRaRemCntValuePortn_Type = Counter32
_Pm253CntclientUpRaRemCntValuePortn_Object = MibTableColumn
pm253CntclientUpRaRemCntValuePortn = _Pm253CntclientUpRaRemCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 2, 16, 1, 2),
    _Pm253CntclientUpRaRemCntValuePortn_Type()
)
pm253CntclientUpRaRemCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CntclientUpRaRemCntValuePortn.setStatus("current")
_Pm253CntclientUpRaRemCntErrorPortn_Type = EkiOnOff
_Pm253CntclientUpRaRemCntErrorPortn_Object = MibTableColumn
pm253CntclientUpRaRemCntErrorPortn = _Pm253CntclientUpRaRemCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 2, 16, 1, 3),
    _Pm253CntclientUpRaRemCntErrorPortn_Type()
)
pm253CntclientUpRaRemCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CntclientUpRaRemCntErrorPortn.setStatus("current")
_Pm253CntclientUpRaRemCntOverloadPortn_Type = EkiOnOff
_Pm253CntclientUpRaRemCntOverloadPortn_Object = MibTableColumn
pm253CntclientUpRaRemCntOverloadPortn = _Pm253CntclientUpRaRemCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 2, 16, 1, 4),
    _Pm253CntclientUpRaRemCntOverloadPortn_Type()
)
pm253CntclientUpRaRemCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CntclientUpRaRemCntOverloadPortn.setStatus("current")
_Pm253CntclientUpRaInsCntTable_Object = MibTable
pm253CntclientUpRaInsCntTable = _Pm253CntclientUpRaInsCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 2, 24)
)
if mibBuilder.loadTexts:
    pm253CntclientUpRaInsCntTable.setStatus("current")
_Pm253CntclientUpRaInsCntEntry_Object = MibTableRow
pm253CntclientUpRaInsCntEntry = _Pm253CntclientUpRaInsCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 2, 24, 1)
)
pm253CntclientUpRaInsCntEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253CntclientUpRaInsCntIndex"),
)
if mibBuilder.loadTexts:
    pm253CntclientUpRaInsCntEntry.setStatus("current")


class _Pm253CntclientUpRaInsCntIndex_Type(Integer32):
    """Custom type pm253CntclientUpRaInsCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253CntclientUpRaInsCntIndex_Type.__name__ = "Integer32"
_Pm253CntclientUpRaInsCntIndex_Object = MibTableColumn
pm253CntclientUpRaInsCntIndex = _Pm253CntclientUpRaInsCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 2, 24, 1, 1),
    _Pm253CntclientUpRaInsCntIndex_Type()
)
pm253CntclientUpRaInsCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CntclientUpRaInsCntIndex.setStatus("current")
_Pm253CntclientUpRaInsCntValuePortn_Type = Counter32
_Pm253CntclientUpRaInsCntValuePortn_Object = MibTableColumn
pm253CntclientUpRaInsCntValuePortn = _Pm253CntclientUpRaInsCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 2, 24, 1, 2),
    _Pm253CntclientUpRaInsCntValuePortn_Type()
)
pm253CntclientUpRaInsCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CntclientUpRaInsCntValuePortn.setStatus("current")
_Pm253CntclientUpRaInsCntErrorPortn_Type = EkiOnOff
_Pm253CntclientUpRaInsCntErrorPortn_Object = MibTableColumn
pm253CntclientUpRaInsCntErrorPortn = _Pm253CntclientUpRaInsCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 2, 24, 1, 3),
    _Pm253CntclientUpRaInsCntErrorPortn_Type()
)
pm253CntclientUpRaInsCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CntclientUpRaInsCntErrorPortn.setStatus("current")
_Pm253CntclientUpRaInsCntOverloadPortn_Type = EkiOnOff
_Pm253CntclientUpRaInsCntOverloadPortn_Object = MibTableColumn
pm253CntclientUpRaInsCntOverloadPortn = _Pm253CntclientUpRaInsCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 2, 24, 1, 4),
    _Pm253CntclientUpRaInsCntOverloadPortn_Type()
)
pm253CntclientUpRaInsCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CntclientUpRaInsCntOverloadPortn.setStatus("current")
_Pm253CntclientUpDispErrCntTable_Object = MibTable
pm253CntclientUpDispErrCntTable = _Pm253CntclientUpDispErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 2, 32)
)
if mibBuilder.loadTexts:
    pm253CntclientUpDispErrCntTable.setStatus("current")
_Pm253CntclientUpDispErrCntEntry_Object = MibTableRow
pm253CntclientUpDispErrCntEntry = _Pm253CntclientUpDispErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 2, 32, 1)
)
pm253CntclientUpDispErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253CntclientUpDispErrCntIndex"),
)
if mibBuilder.loadTexts:
    pm253CntclientUpDispErrCntEntry.setStatus("current")


class _Pm253CntclientUpDispErrCntIndex_Type(Integer32):
    """Custom type pm253CntclientUpDispErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253CntclientUpDispErrCntIndex_Type.__name__ = "Integer32"
_Pm253CntclientUpDispErrCntIndex_Object = MibTableColumn
pm253CntclientUpDispErrCntIndex = _Pm253CntclientUpDispErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 2, 32, 1, 1),
    _Pm253CntclientUpDispErrCntIndex_Type()
)
pm253CntclientUpDispErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CntclientUpDispErrCntIndex.setStatus("current")
_Pm253CntclientUpDispErrCntValuePortn_Type = Counter32
_Pm253CntclientUpDispErrCntValuePortn_Object = MibTableColumn
pm253CntclientUpDispErrCntValuePortn = _Pm253CntclientUpDispErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 2, 32, 1, 2),
    _Pm253CntclientUpDispErrCntValuePortn_Type()
)
pm253CntclientUpDispErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CntclientUpDispErrCntValuePortn.setStatus("current")
_Pm253CntclientUpDispErrCntErrorPortn_Type = EkiOnOff
_Pm253CntclientUpDispErrCntErrorPortn_Object = MibTableColumn
pm253CntclientUpDispErrCntErrorPortn = _Pm253CntclientUpDispErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 2, 32, 1, 3),
    _Pm253CntclientUpDispErrCntErrorPortn_Type()
)
pm253CntclientUpDispErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CntclientUpDispErrCntErrorPortn.setStatus("current")
_Pm253CntclientUpDispErrCntOverloadPortn_Type = EkiOnOff
_Pm253CntclientUpDispErrCntOverloadPortn_Object = MibTableColumn
pm253CntclientUpDispErrCntOverloadPortn = _Pm253CntclientUpDispErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 2, 32, 1, 4),
    _Pm253CntclientUpDispErrCntOverloadPortn_Type()
)
pm253CntclientUpDispErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CntclientUpDispErrCntOverloadPortn.setStatus("current")
_Pm253CntclientUpTimCntTable_Object = MibTable
pm253CntclientUpTimCntTable = _Pm253CntclientUpTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 2, 40)
)
if mibBuilder.loadTexts:
    pm253CntclientUpTimCntTable.setStatus("current")
_Pm253CntclientUpTimCntEntry_Object = MibTableRow
pm253CntclientUpTimCntEntry = _Pm253CntclientUpTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 2, 40, 1)
)
pm253CntclientUpTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253CntclientUpTimCntIndex"),
)
if mibBuilder.loadTexts:
    pm253CntclientUpTimCntEntry.setStatus("current")


class _Pm253CntclientUpTimCntIndex_Type(Integer32):
    """Custom type pm253CntclientUpTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253CntclientUpTimCntIndex_Type.__name__ = "Integer32"
_Pm253CntclientUpTimCntIndex_Object = MibTableColumn
pm253CntclientUpTimCntIndex = _Pm253CntclientUpTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 2, 40, 1, 1),
    _Pm253CntclientUpTimCntIndex_Type()
)
pm253CntclientUpTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CntclientUpTimCntIndex.setStatus("current")
_Pm253CntclientUpTimCntValuePortn_Type = Counter32
_Pm253CntclientUpTimCntValuePortn_Object = MibTableColumn
pm253CntclientUpTimCntValuePortn = _Pm253CntclientUpTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 2, 40, 1, 2),
    _Pm253CntclientUpTimCntValuePortn_Type()
)
pm253CntclientUpTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CntclientUpTimCntValuePortn.setStatus("current")
_Pm253CntclientUpTimCntErrorPortn_Type = EkiOnOff
_Pm253CntclientUpTimCntErrorPortn_Object = MibTableColumn
pm253CntclientUpTimCntErrorPortn = _Pm253CntclientUpTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 2, 40, 1, 3),
    _Pm253CntclientUpTimCntErrorPortn_Type()
)
pm253CntclientUpTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CntclientUpTimCntErrorPortn.setStatus("current")
_Pm253CntclientUpTimCntOverloadPortn_Type = EkiOnOff
_Pm253CntclientUpTimCntOverloadPortn_Object = MibTableColumn
pm253CntclientUpTimCntOverloadPortn = _Pm253CntclientUpTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 2, 40, 1, 4),
    _Pm253CntclientUpTimCntOverloadPortn_Type()
)
pm253CntclientUpTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CntclientUpTimCntOverloadPortn.setStatus("current")
_Pm253CntclientDwCbipCntTable_Object = MibTable
pm253CntclientDwCbipCntTable = _Pm253CntclientDwCbipCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 2, 64)
)
if mibBuilder.loadTexts:
    pm253CntclientDwCbipCntTable.setStatus("current")
_Pm253CntclientDwCbipCntEntry_Object = MibTableRow
pm253CntclientDwCbipCntEntry = _Pm253CntclientDwCbipCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 2, 64, 1)
)
pm253CntclientDwCbipCntEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253CntclientDwCbipCntIndex"),
)
if mibBuilder.loadTexts:
    pm253CntclientDwCbipCntEntry.setStatus("current")


class _Pm253CntclientDwCbipCntIndex_Type(Integer32):
    """Custom type pm253CntclientDwCbipCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253CntclientDwCbipCntIndex_Type.__name__ = "Integer32"
_Pm253CntclientDwCbipCntIndex_Object = MibTableColumn
pm253CntclientDwCbipCntIndex = _Pm253CntclientDwCbipCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 2, 64, 1, 1),
    _Pm253CntclientDwCbipCntIndex_Type()
)
pm253CntclientDwCbipCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CntclientDwCbipCntIndex.setStatus("current")
_Pm253CntclientDwCbipCntValuePortn_Type = Counter32
_Pm253CntclientDwCbipCntValuePortn_Object = MibTableColumn
pm253CntclientDwCbipCntValuePortn = _Pm253CntclientDwCbipCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 2, 64, 1, 2),
    _Pm253CntclientDwCbipCntValuePortn_Type()
)
pm253CntclientDwCbipCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CntclientDwCbipCntValuePortn.setStatus("current")
_Pm253CntclientDwCbipCntErrorPortn_Type = EkiOnOff
_Pm253CntclientDwCbipCntErrorPortn_Object = MibTableColumn
pm253CntclientDwCbipCntErrorPortn = _Pm253CntclientDwCbipCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 2, 64, 1, 3),
    _Pm253CntclientDwCbipCntErrorPortn_Type()
)
pm253CntclientDwCbipCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CntclientDwCbipCntErrorPortn.setStatus("current")
_Pm253CntclientDwCbipCntOverloadPortn_Type = EkiOnOff
_Pm253CntclientDwCbipCntOverloadPortn_Object = MibTableColumn
pm253CntclientDwCbipCntOverloadPortn = _Pm253CntclientDwCbipCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 2, 64, 1, 4),
    _Pm253CntclientDwCbipCntOverloadPortn_Type()
)
pm253CntclientDwCbipCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CntclientDwCbipCntOverloadPortn.setStatus("current")
_Pm253CntclientDwTimCntTable_Object = MibTable
pm253CntclientDwTimCntTable = _Pm253CntclientDwTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 2, 72)
)
if mibBuilder.loadTexts:
    pm253CntclientDwTimCntTable.setStatus("current")
_Pm253CntclientDwTimCntEntry_Object = MibTableRow
pm253CntclientDwTimCntEntry = _Pm253CntclientDwTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 2, 72, 1)
)
pm253CntclientDwTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253CntclientDwTimCntIndex"),
)
if mibBuilder.loadTexts:
    pm253CntclientDwTimCntEntry.setStatus("current")


class _Pm253CntclientDwTimCntIndex_Type(Integer32):
    """Custom type pm253CntclientDwTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253CntclientDwTimCntIndex_Type.__name__ = "Integer32"
_Pm253CntclientDwTimCntIndex_Object = MibTableColumn
pm253CntclientDwTimCntIndex = _Pm253CntclientDwTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 2, 72, 1, 1),
    _Pm253CntclientDwTimCntIndex_Type()
)
pm253CntclientDwTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CntclientDwTimCntIndex.setStatus("current")
_Pm253CntclientDwTimCntValuePortn_Type = Counter32
_Pm253CntclientDwTimCntValuePortn_Object = MibTableColumn
pm253CntclientDwTimCntValuePortn = _Pm253CntclientDwTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 2, 72, 1, 2),
    _Pm253CntclientDwTimCntValuePortn_Type()
)
pm253CntclientDwTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CntclientDwTimCntValuePortn.setStatus("current")
_Pm253CntclientDwTimCntErrorPortn_Type = EkiOnOff
_Pm253CntclientDwTimCntErrorPortn_Object = MibTableColumn
pm253CntclientDwTimCntErrorPortn = _Pm253CntclientDwTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 2, 72, 1, 3),
    _Pm253CntclientDwTimCntErrorPortn_Type()
)
pm253CntclientDwTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CntclientDwTimCntErrorPortn.setStatus("current")
_Pm253CntclientDwTimCntOverloadPortn_Type = EkiOnOff
_Pm253CntclientDwTimCntOverloadPortn_Object = MibTableColumn
pm253CntclientDwTimCntOverloadPortn = _Pm253CntclientDwTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 2, 72, 1, 4),
    _Pm253CntclientDwTimCntOverloadPortn_Type()
)
pm253CntclientDwTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CntclientDwTimCntOverloadPortn.setStatus("current")
_Pm253CntLine_ObjectIdentity = ObjectIdentity
pm253CntLine = _Pm253CntLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 3)
)
_Pm253CntlineDfrmB1ErrCntTable_Object = MibTable
pm253CntlineDfrmB1ErrCntTable = _Pm253CntlineDfrmB1ErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 3, 152)
)
if mibBuilder.loadTexts:
    pm253CntlineDfrmB1ErrCntTable.setStatus("current")
_Pm253CntlineDfrmB1ErrCntEntry_Object = MibTableRow
pm253CntlineDfrmB1ErrCntEntry = _Pm253CntlineDfrmB1ErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 3, 152, 1)
)
pm253CntlineDfrmB1ErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253CntlineDfrmB1ErrCntIndex"),
)
if mibBuilder.loadTexts:
    pm253CntlineDfrmB1ErrCntEntry.setStatus("current")


class _Pm253CntlineDfrmB1ErrCntIndex_Type(Integer32):
    """Custom type pm253CntlineDfrmB1ErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253CntlineDfrmB1ErrCntIndex_Type.__name__ = "Integer32"
_Pm253CntlineDfrmB1ErrCntIndex_Object = MibTableColumn
pm253CntlineDfrmB1ErrCntIndex = _Pm253CntlineDfrmB1ErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 3, 152, 1, 1),
    _Pm253CntlineDfrmB1ErrCntIndex_Type()
)
pm253CntlineDfrmB1ErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CntlineDfrmB1ErrCntIndex.setStatus("current")
_Pm253CntlineDfrmB1ErrCntValuePortn_Type = Counter32
_Pm253CntlineDfrmB1ErrCntValuePortn_Object = MibTableColumn
pm253CntlineDfrmB1ErrCntValuePortn = _Pm253CntlineDfrmB1ErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 3, 152, 1, 2),
    _Pm253CntlineDfrmB1ErrCntValuePortn_Type()
)
pm253CntlineDfrmB1ErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CntlineDfrmB1ErrCntValuePortn.setStatus("current")
_Pm253CntlineDfrmB1ErrCntErrorPortn_Type = EkiOnOff
_Pm253CntlineDfrmB1ErrCntErrorPortn_Object = MibTableColumn
pm253CntlineDfrmB1ErrCntErrorPortn = _Pm253CntlineDfrmB1ErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 3, 152, 1, 3),
    _Pm253CntlineDfrmB1ErrCntErrorPortn_Type()
)
pm253CntlineDfrmB1ErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CntlineDfrmB1ErrCntErrorPortn.setStatus("current")
_Pm253CntlineDfrmB1ErrCntOverloadPortn_Type = EkiOnOff
_Pm253CntlineDfrmB1ErrCntOverloadPortn_Object = MibTableColumn
pm253CntlineDfrmB1ErrCntOverloadPortn = _Pm253CntlineDfrmB1ErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 3, 152, 1, 4),
    _Pm253CntlineDfrmB1ErrCntOverloadPortn_Type()
)
pm253CntlineDfrmB1ErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CntlineDfrmB1ErrCntOverloadPortn.setStatus("current")
_Pm253CntlineDfrmTimCntTable_Object = MibTable
pm253CntlineDfrmTimCntTable = _Pm253CntlineDfrmTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 3, 153)
)
if mibBuilder.loadTexts:
    pm253CntlineDfrmTimCntTable.setStatus("current")
_Pm253CntlineDfrmTimCntEntry_Object = MibTableRow
pm253CntlineDfrmTimCntEntry = _Pm253CntlineDfrmTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 3, 153, 1)
)
pm253CntlineDfrmTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253CntlineDfrmTimCntIndex"),
)
if mibBuilder.loadTexts:
    pm253CntlineDfrmTimCntEntry.setStatus("current")


class _Pm253CntlineDfrmTimCntIndex_Type(Integer32):
    """Custom type pm253CntlineDfrmTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253CntlineDfrmTimCntIndex_Type.__name__ = "Integer32"
_Pm253CntlineDfrmTimCntIndex_Object = MibTableColumn
pm253CntlineDfrmTimCntIndex = _Pm253CntlineDfrmTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 3, 153, 1, 1),
    _Pm253CntlineDfrmTimCntIndex_Type()
)
pm253CntlineDfrmTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CntlineDfrmTimCntIndex.setStatus("current")
_Pm253CntlineDfrmTimCntValuePortn_Type = Counter32
_Pm253CntlineDfrmTimCntValuePortn_Object = MibTableColumn
pm253CntlineDfrmTimCntValuePortn = _Pm253CntlineDfrmTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 3, 153, 1, 2),
    _Pm253CntlineDfrmTimCntValuePortn_Type()
)
pm253CntlineDfrmTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CntlineDfrmTimCntValuePortn.setStatus("current")
_Pm253CntlineDfrmTimCntErrorPortn_Type = EkiOnOff
_Pm253CntlineDfrmTimCntErrorPortn_Object = MibTableColumn
pm253CntlineDfrmTimCntErrorPortn = _Pm253CntlineDfrmTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 3, 153, 1, 3),
    _Pm253CntlineDfrmTimCntErrorPortn_Type()
)
pm253CntlineDfrmTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CntlineDfrmTimCntErrorPortn.setStatus("current")
_Pm253CntlineDfrmTimCntOverloadPortn_Type = EkiOnOff
_Pm253CntlineDfrmTimCntOverloadPortn_Object = MibTableColumn
pm253CntlineDfrmTimCntOverloadPortn = _Pm253CntlineDfrmTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 3, 153, 1, 4),
    _Pm253CntlineDfrmTimCntOverloadPortn_Type()
)
pm253CntlineDfrmTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CntlineDfrmTimCntOverloadPortn.setStatus("current")
_Pm253CntCountersReset_Type = EkiOnOff
_Pm253CntCountersReset_Object = MibScalar
pm253CntCountersReset = _Pm253CntCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 259),
    _Pm253CntCountersReset_Type()
)
pm253CntCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CntCountersReset.setStatus("current")
_Pm253CntCountersStop_Type = EkiOnOff
_Pm253CntCountersStop_Object = MibScalar
pm253CntCountersStop = _Pm253CntCountersStop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 4, 260),
    _Pm253CntCountersStop_Type()
)
pm253CntCountersStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CntCountersStop.setStatus("current")
_Pm253controlsWrite_ObjectIdentity = ObjectIdentity
pm253controlsWrite = _Pm253controlsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6)
)
_Pm253CtrlOther_ObjectIdentity = ObjectIdentity
pm253CtrlOther = _Pm253CtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 1)
)
_Pm253CtrlconfMgnt1_ObjectIdentity = ObjectIdentity
pm253CtrlconfMgnt1 = _Pm253CtrlconfMgnt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 1, 1)
)
_Pm253CtrlConf1Load1_Type = EkiOnOff
_Pm253CtrlConf1Load1_Object = MibScalar
pm253CtrlConf1Load1 = _Pm253CtrlConf1Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 1, 1, 1),
    _Pm253CtrlConf1Load1_Type()
)
pm253CtrlConf1Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlConf1Load1.setStatus("current")
_Pm253CtrlConf2Load1_Type = EkiOnOff
_Pm253CtrlConf2Load1_Object = MibScalar
pm253CtrlConf2Load1 = _Pm253CtrlConf2Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 1, 1, 2),
    _Pm253CtrlConf2Load1_Type()
)
pm253CtrlConf2Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlConf2Load1.setStatus("current")
_Pm253CtrlConf2Flash1_Type = EkiOnOff
_Pm253CtrlConf2Flash1_Object = MibScalar
pm253CtrlConf2Flash1 = _Pm253CtrlConf2Flash1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 1, 1, 10),
    _Pm253CtrlConf2Flash1_Type()
)
pm253CtrlConf2Flash1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlConf2Flash1.setStatus("current")
_Pm253CtrlConf2Clear1_Type = EkiOnOff
_Pm253CtrlConf2Clear1_Object = MibScalar
pm253CtrlConf2Clear1 = _Pm253CtrlConf2Clear1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 1, 1, 14),
    _Pm253CtrlConf2Clear1_Type()
)
pm253CtrlConf2Clear1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlConf2Clear1.setStatus("current")
_Pm253Ctrlsynth4_ObjectIdentity = ObjectIdentity
pm253Ctrlsynth4 = _Pm253Ctrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 1, 4)
)
_Pm253CtrlCorrelatOn_Type = EkiOnOff
_Pm253CtrlCorrelatOn_Object = MibScalar
pm253CtrlCorrelatOn = _Pm253CtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 1, 4, 1),
    _Pm253CtrlCorrelatOn_Type()
)
pm253CtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlCorrelatOn.setStatus("current")
_Pm253CtrlCorrelatOff_Type = EkiOnOff
_Pm253CtrlCorrelatOff_Object = MibScalar
pm253CtrlCorrelatOff = _Pm253CtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 1, 4, 2),
    _Pm253CtrlCorrelatOff_Type()
)
pm253CtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlCorrelatOff.setStatus("current")
_Pm253CtrlswMgnt_ObjectIdentity = ObjectIdentity
pm253CtrlswMgnt = _Pm253CtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 1, 5)
)
_Pm253CtrlColdReset_Type = EkiOnOff
_Pm253CtrlColdReset_Object = MibScalar
pm253CtrlColdReset = _Pm253CtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 1, 5, 2),
    _Pm253CtrlColdReset_Type()
)
pm253CtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlColdReset.setStatus("current")
_Pm253CtrlWarmReset_Type = EkiOnOff
_Pm253CtrlWarmReset_Object = MibScalar
pm253CtrlWarmReset = _Pm253CtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 1, 5, 3),
    _Pm253CtrlWarmReset_Type()
)
pm253CtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlWarmReset.setStatus("current")
_Pm253CtrlLoadSwBank1_Type = EkiOnOff
_Pm253CtrlLoadSwBank1_Object = MibScalar
pm253CtrlLoadSwBank1 = _Pm253CtrlLoadSwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 1, 5, 5),
    _Pm253CtrlLoadSwBank1_Type()
)
pm253CtrlLoadSwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlLoadSwBank1.setStatus("current")
_Pm253CtrlLoadSwBank2_Type = EkiOnOff
_Pm253CtrlLoadSwBank2_Object = MibScalar
pm253CtrlLoadSwBank2 = _Pm253CtrlLoadSwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 1, 5, 6),
    _Pm253CtrlLoadSwBank2_Type()
)
pm253CtrlLoadSwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlLoadSwBank2.setStatus("current")
_Pm253CtrlgwMgnt_ObjectIdentity = ObjectIdentity
pm253CtrlgwMgnt = _Pm253CtrlgwMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 1, 6)
)
_Pm253CtrlCurrentGwReset_Type = EkiOnOff
_Pm253CtrlCurrentGwReset_Object = MibScalar
pm253CtrlCurrentGwReset = _Pm253CtrlCurrentGwReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 1, 6, 1),
    _Pm253CtrlCurrentGwReset_Type()
)
pm253CtrlCurrentGwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlCurrentGwReset.setStatus("current")
_Pm253CtrlLoadGwBank1_Type = EkiOnOff
_Pm253CtrlLoadGwBank1_Object = MibScalar
pm253CtrlLoadGwBank1 = _Pm253CtrlLoadGwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 1, 6, 5),
    _Pm253CtrlLoadGwBank1_Type()
)
pm253CtrlLoadGwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlLoadGwBank1.setStatus("current")
_Pm253CtrlLoadGwBank2_Type = EkiOnOff
_Pm253CtrlLoadGwBank2_Object = MibScalar
pm253CtrlLoadGwBank2 = _Pm253CtrlLoadGwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 1, 6, 6),
    _Pm253CtrlLoadGwBank2_Type()
)
pm253CtrlLoadGwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlLoadGwBank2.setStatus("current")
_Pm253CtrlLoadGwBank3_Type = EkiOnOff
_Pm253CtrlLoadGwBank3_Object = MibScalar
pm253CtrlLoadGwBank3 = _Pm253CtrlLoadGwBank3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 1, 6, 7),
    _Pm253CtrlLoadGwBank3_Type()
)
pm253CtrlLoadGwBank3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlLoadGwBank3.setStatus("current")
_Pm253CtrlLoadGwBank4_Type = EkiOnOff
_Pm253CtrlLoadGwBank4_Object = MibScalar
pm253CtrlLoadGwBank4 = _Pm253CtrlLoadGwBank4_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 1, 6, 8),
    _Pm253CtrlLoadGwBank4_Type()
)
pm253CtrlLoadGwBank4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlLoadGwBank4.setStatus("current")
_Pm253CtrlledTest_ObjectIdentity = ObjectIdentity
pm253CtrlledTest = _Pm253CtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 1, 192)
)
_Pm253CtrlGreenLed_Type = EkiOnOff
_Pm253CtrlGreenLed_Object = MibScalar
pm253CtrlGreenLed = _Pm253CtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 1, 192, 1),
    _Pm253CtrlGreenLed_Type()
)
pm253CtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlGreenLed.setStatus("current")
_Pm253CtrlRedLed_Type = EkiOnOff
_Pm253CtrlRedLed_Object = MibScalar
pm253CtrlRedLed = _Pm253CtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 1, 192, 2),
    _Pm253CtrlRedLed_Type()
)
pm253CtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlRedLed.setStatus("current")
_Pm253CtrlLedOff_Type = EkiOnOff
_Pm253CtrlLedOff_Object = MibScalar
pm253CtrlLedOff = _Pm253CtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 1, 192, 3),
    _Pm253CtrlLedOff_Type()
)
pm253CtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlLedOff.setStatus("current")
_Pm253CtrlmoduleOosMode_ObjectIdentity = ObjectIdentity
pm253CtrlmoduleOosMode = _Pm253CtrlmoduleOosMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 1, 193)
)
_Pm253CtrlModuleOosMode_Type = EkiOnOff
_Pm253CtrlModuleOosMode_Object = MibScalar
pm253CtrlModuleOosMode = _Pm253CtrlModuleOosMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 1, 193, 1),
    _Pm253CtrlModuleOosMode_Type()
)
pm253CtrlModuleOosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlModuleOosMode.setStatus("current")
_Pm253CtrlclientPortMode_ObjectIdentity = ObjectIdentity
pm253CtrlclientPortMode = _Pm253CtrlclientPortMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 1, 194)
)
_Pm253CtrlClientPortMode_Type = EkiOnOff
_Pm253CtrlClientPortMode_Object = MibScalar
pm253CtrlClientPortMode = _Pm253CtrlClientPortMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 1, 194, 1),
    _Pm253CtrlClientPortMode_Type()
)
pm253CtrlClientPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlClientPortMode.setStatus("current")
_Pm253CtrlmaintenanceMode_ObjectIdentity = ObjectIdentity
pm253CtrlmaintenanceMode = _Pm253CtrlmaintenanceMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 1, 197)
)
_Pm253CtrlMaintenanceMode_Type = EkiOnOff
_Pm253CtrlMaintenanceMode_Object = MibScalar
pm253CtrlMaintenanceMode = _Pm253CtrlMaintenanceMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 1, 197, 1),
    _Pm253CtrlMaintenanceMode_Type()
)
pm253CtrlMaintenanceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlMaintenanceMode.setStatus("current")
_Pm253CtrldccEnable_ObjectIdentity = ObjectIdentity
pm253CtrldccEnable = _Pm253CtrldccEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 1, 198)
)
_Pm253CtrlDccEnable_Type = EkiOnOff
_Pm253CtrlDccEnable_Object = MibScalar
pm253CtrlDccEnable = _Pm253CtrlDccEnable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 1, 198, 1),
    _Pm253CtrlDccEnable_Type()
)
pm253CtrlDccEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlDccEnable.setStatus("current")
_Pm253CtrlPort_ObjectIdentity = ObjectIdentity
pm253CtrlPort = _Pm253CtrlPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 2)
)
_Pm253CtrlclientAccessLoopTable_Object = MibTable
pm253CtrlclientAccessLoopTable = _Pm253CtrlclientAccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 2, 16)
)
if mibBuilder.loadTexts:
    pm253CtrlclientAccessLoopTable.setStatus("current")
_Pm253CtrlclientAccessLoopEntry_Object = MibTableRow
pm253CtrlclientAccessLoopEntry = _Pm253CtrlclientAccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 2, 16, 1)
)
pm253CtrlclientAccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253CtrlclientAccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pm253CtrlclientAccessLoopEntry.setStatus("current")


class _Pm253CtrlclientAccessLoopIndex_Type(Integer32):
    """Custom type pm253CtrlclientAccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253CtrlclientAccessLoopIndex_Type.__name__ = "Integer32"
_Pm253CtrlclientAccessLoopIndex_Object = MibTableColumn
pm253CtrlclientAccessLoopIndex = _Pm253CtrlclientAccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 2, 16, 1, 1),
    _Pm253CtrlclientAccessLoopIndex_Type()
)
pm253CtrlclientAccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CtrlclientAccessLoopIndex.setStatus("current")
_Pm253CtrlclientAccessLoopPortn_Type = EkiState
_Pm253CtrlclientAccessLoopPortn_Object = MibTableColumn
pm253CtrlclientAccessLoopPortn = _Pm253CtrlclientAccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 2, 16, 1, 2),
    _Pm253CtrlclientAccessLoopPortn_Type()
)
pm253CtrlclientAccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlclientAccessLoopPortn.setStatus("current")
_Pm253CtrlclientOosModeTable_Object = MibTable
pm253CtrlclientOosModeTable = _Pm253CtrlclientOosModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 2, 18)
)
if mibBuilder.loadTexts:
    pm253CtrlclientOosModeTable.setStatus("current")
_Pm253CtrlclientOosModeEntry_Object = MibTableRow
pm253CtrlclientOosModeEntry = _Pm253CtrlclientOosModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 2, 18, 1)
)
pm253CtrlclientOosModeEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253CtrlclientOosModeIndex"),
)
if mibBuilder.loadTexts:
    pm253CtrlclientOosModeEntry.setStatus("current")


class _Pm253CtrlclientOosModeIndex_Type(Integer32):
    """Custom type pm253CtrlclientOosModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253CtrlclientOosModeIndex_Type.__name__ = "Integer32"
_Pm253CtrlclientOosModeIndex_Object = MibTableColumn
pm253CtrlclientOosModeIndex = _Pm253CtrlclientOosModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 2, 18, 1, 1),
    _Pm253CtrlclientOosModeIndex_Type()
)
pm253CtrlclientOosModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CtrlclientOosModeIndex.setStatus("current")
_Pm253CtrlclientOosModePortn_Type = EkiState
_Pm253CtrlclientOosModePortn_Object = MibTableColumn
pm253CtrlclientOosModePortn = _Pm253CtrlclientOosModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 2, 18, 1, 2),
    _Pm253CtrlclientOosModePortn_Type()
)
pm253CtrlclientOosModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlclientOosModePortn.setStatus("current")
_Pm253CtrlclientSfpOnOffCtrlTable_Object = MibTable
pm253CtrlclientSfpOnOffCtrlTable = _Pm253CtrlclientSfpOnOffCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 2, 20)
)
if mibBuilder.loadTexts:
    pm253CtrlclientSfpOnOffCtrlTable.setStatus("current")
_Pm253CtrlclientSfpOnOffCtrlEntry_Object = MibTableRow
pm253CtrlclientSfpOnOffCtrlEntry = _Pm253CtrlclientSfpOnOffCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 2, 20, 1)
)
pm253CtrlclientSfpOnOffCtrlEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253CtrlclientSfpOnOffCtrlIndex"),
)
if mibBuilder.loadTexts:
    pm253CtrlclientSfpOnOffCtrlEntry.setStatus("current")


class _Pm253CtrlclientSfpOnOffCtrlIndex_Type(Integer32):
    """Custom type pm253CtrlclientSfpOnOffCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253CtrlclientSfpOnOffCtrlIndex_Type.__name__ = "Integer32"
_Pm253CtrlclientSfpOnOffCtrlIndex_Object = MibTableColumn
pm253CtrlclientSfpOnOffCtrlIndex = _Pm253CtrlclientSfpOnOffCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 2, 20, 1, 1),
    _Pm253CtrlclientSfpOnOffCtrlIndex_Type()
)
pm253CtrlclientSfpOnOffCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CtrlclientSfpOnOffCtrlIndex.setStatus("current")
_Pm253CtrlclientSfpOnOffCtrlPortn_Type = EkiState
_Pm253CtrlclientSfpOnOffCtrlPortn_Object = MibTableColumn
pm253CtrlclientSfpOnOffCtrlPortn = _Pm253CtrlclientSfpOnOffCtrlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 2, 20, 1, 2),
    _Pm253CtrlclientSfpOnOffCtrlPortn_Type()
)
pm253CtrlclientSfpOnOffCtrlPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlclientSfpOnOffCtrlPortn.setStatus("current")
_Pm253CtrlclientCsfUpInsTable_Object = MibTable
pm253CtrlclientCsfUpInsTable = _Pm253CtrlclientCsfUpInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 2, 21)
)
if mibBuilder.loadTexts:
    pm253CtrlclientCsfUpInsTable.setStatus("current")
_Pm253CtrlclientCsfUpInsEntry_Object = MibTableRow
pm253CtrlclientCsfUpInsEntry = _Pm253CtrlclientCsfUpInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 2, 21, 1)
)
pm253CtrlclientCsfUpInsEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253CtrlclientCsfUpInsIndex"),
)
if mibBuilder.loadTexts:
    pm253CtrlclientCsfUpInsEntry.setStatus("current")


class _Pm253CtrlclientCsfUpInsIndex_Type(Integer32):
    """Custom type pm253CtrlclientCsfUpInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253CtrlclientCsfUpInsIndex_Type.__name__ = "Integer32"
_Pm253CtrlclientCsfUpInsIndex_Object = MibTableColumn
pm253CtrlclientCsfUpInsIndex = _Pm253CtrlclientCsfUpInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 2, 21, 1, 1),
    _Pm253CtrlclientCsfUpInsIndex_Type()
)
pm253CtrlclientCsfUpInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CtrlclientCsfUpInsIndex.setStatus("current")
_Pm253CtrlclientCsfUpInsPortn_Type = EkiState
_Pm253CtrlclientCsfUpInsPortn_Object = MibTableColumn
pm253CtrlclientCsfUpInsPortn = _Pm253CtrlclientCsfUpInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 2, 21, 1, 2),
    _Pm253CtrlclientCsfUpInsPortn_Type()
)
pm253CtrlclientCsfUpInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlclientCsfUpInsPortn.setStatus("current")
_Pm253CtrlclientCaisDwInsTable_Object = MibTable
pm253CtrlclientCaisDwInsTable = _Pm253CtrlclientCaisDwInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 2, 22)
)
if mibBuilder.loadTexts:
    pm253CtrlclientCaisDwInsTable.setStatus("current")
_Pm253CtrlclientCaisDwInsEntry_Object = MibTableRow
pm253CtrlclientCaisDwInsEntry = _Pm253CtrlclientCaisDwInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 2, 22, 1)
)
pm253CtrlclientCaisDwInsEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253CtrlclientCaisDwInsIndex"),
)
if mibBuilder.loadTexts:
    pm253CtrlclientCaisDwInsEntry.setStatus("current")


class _Pm253CtrlclientCaisDwInsIndex_Type(Integer32):
    """Custom type pm253CtrlclientCaisDwInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253CtrlclientCaisDwInsIndex_Type.__name__ = "Integer32"
_Pm253CtrlclientCaisDwInsIndex_Object = MibTableColumn
pm253CtrlclientCaisDwInsIndex = _Pm253CtrlclientCaisDwInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 2, 22, 1, 1),
    _Pm253CtrlclientCaisDwInsIndex_Type()
)
pm253CtrlclientCaisDwInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CtrlclientCaisDwInsIndex.setStatus("current")
_Pm253CtrlclientCaisDwInsPortn_Type = EkiState
_Pm253CtrlclientCaisDwInsPortn_Object = MibTableColumn
pm253CtrlclientCaisDwInsPortn = _Pm253CtrlclientCaisDwInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 2, 22, 1, 2),
    _Pm253CtrlclientCaisDwInsPortn_Type()
)
pm253CtrlclientCaisDwInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlclientCaisDwInsPortn.setStatus("current")
_Pm253CtrlclientAccessTermLoopTable_Object = MibTable
pm253CtrlclientAccessTermLoopTable = _Pm253CtrlclientAccessTermLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 2, 26)
)
if mibBuilder.loadTexts:
    pm253CtrlclientAccessTermLoopTable.setStatus("current")
_Pm253CtrlclientAccessTermLoopEntry_Object = MibTableRow
pm253CtrlclientAccessTermLoopEntry = _Pm253CtrlclientAccessTermLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 2, 26, 1)
)
pm253CtrlclientAccessTermLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253CtrlclientAccessTermLoopIndex"),
)
if mibBuilder.loadTexts:
    pm253CtrlclientAccessTermLoopEntry.setStatus("current")


class _Pm253CtrlclientAccessTermLoopIndex_Type(Integer32):
    """Custom type pm253CtrlclientAccessTermLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253CtrlclientAccessTermLoopIndex_Type.__name__ = "Integer32"
_Pm253CtrlclientAccessTermLoopIndex_Object = MibTableColumn
pm253CtrlclientAccessTermLoopIndex = _Pm253CtrlclientAccessTermLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 2, 26, 1, 1),
    _Pm253CtrlclientAccessTermLoopIndex_Type()
)
pm253CtrlclientAccessTermLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CtrlclientAccessTermLoopIndex.setStatus("current")
_Pm253CtrlclientAccessTermLoopPortn_Type = EkiState
_Pm253CtrlclientAccessTermLoopPortn_Object = MibTableColumn
pm253CtrlclientAccessTermLoopPortn = _Pm253CtrlclientAccessTermLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 2, 26, 1, 2),
    _Pm253CtrlclientAccessTermLoopPortn_Type()
)
pm253CtrlclientAccessTermLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlclientAccessTermLoopPortn.setStatus("current")
_Pm253CtrlProtocolTable_Object = MibTable
pm253CtrlProtocolTable = _Pm253CtrlProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 2, 48)
)
if mibBuilder.loadTexts:
    pm253CtrlProtocolTable.setStatus("current")
_Pm253CtrlProtocolEntry_Object = MibTableRow
pm253CtrlProtocolEntry = _Pm253CtrlProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 2, 48, 1)
)
pm253CtrlProtocolEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253CtrlProtocolIndex"),
)
if mibBuilder.loadTexts:
    pm253CtrlProtocolEntry.setStatus("current")


class _Pm253CtrlProtocolIndex_Type(Integer32):
    """Custom type pm253CtrlProtocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253CtrlProtocolIndex_Type.__name__ = "Integer32"
_Pm253CtrlProtocolIndex_Object = MibTableColumn
pm253CtrlProtocolIndex = _Pm253CtrlProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 2, 48, 1, 1),
    _Pm253CtrlProtocolIndex_Type()
)
pm253CtrlProtocolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CtrlProtocolIndex.setStatus("current")
_Pm253CtrlProtocolPortn_Type = EkiProtocol
_Pm253CtrlProtocolPortn_Object = MibTableColumn
pm253CtrlProtocolPortn = _Pm253CtrlProtocolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 2, 48, 1, 2),
    _Pm253CtrlProtocolPortn_Type()
)
pm253CtrlProtocolPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlProtocolPortn.setStatus("current")
_Pm253CtrlclientResetAllCountTable_Object = MibTable
pm253CtrlclientResetAllCountTable = _Pm253CtrlclientResetAllCountTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 2, 271)
)
if mibBuilder.loadTexts:
    pm253CtrlclientResetAllCountTable.setStatus("current")
_Pm253CtrlclientResetAllCountEntry_Object = MibTableRow
pm253CtrlclientResetAllCountEntry = _Pm253CtrlclientResetAllCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 2, 271, 1)
)
pm253CtrlclientResetAllCountEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253CtrlclientResetAllCountIndex"),
)
if mibBuilder.loadTexts:
    pm253CtrlclientResetAllCountEntry.setStatus("current")


class _Pm253CtrlclientResetAllCountIndex_Type(Integer32):
    """Custom type pm253CtrlclientResetAllCountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253CtrlclientResetAllCountIndex_Type.__name__ = "Integer32"
_Pm253CtrlclientResetAllCountIndex_Object = MibTableColumn
pm253CtrlclientResetAllCountIndex = _Pm253CtrlclientResetAllCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 2, 271, 1, 1),
    _Pm253CtrlclientResetAllCountIndex_Type()
)
pm253CtrlclientResetAllCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CtrlclientResetAllCountIndex.setStatus("current")
_Pm253CtrlclientResetAllCountsPortn_Type = EkiState
_Pm253CtrlclientResetAllCountsPortn_Object = MibTableColumn
pm253CtrlclientResetAllCountsPortn = _Pm253CtrlclientResetAllCountsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 2, 271, 1, 2),
    _Pm253CtrlclientResetAllCountsPortn_Type()
)
pm253CtrlclientResetAllCountsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlclientResetAllCountsPortn.setStatus("deprecated")
_Pm253CtrlLine_ObjectIdentity = ObjectIdentity
pm253CtrlLine = _Pm253CtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3)
)
_Pm253Ctrlsts48c24c_ObjectIdentity = ObjectIdentity
pm253Ctrlsts48c24c = _Pm253Ctrlsts48c24c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 65)
)
_Pm253CtrlSts24cMode_Type = EkiOnOff
_Pm253CtrlSts24cMode_Object = MibScalar
pm253CtrlSts24cMode = _Pm253CtrlSts24cMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 65, 1),
    _Pm253CtrlSts24cMode_Type()
)
pm253CtrlSts24cMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlSts24cMode.setStatus("current")
_Pm253CtrllineMsAis_ObjectIdentity = ObjectIdentity
pm253CtrllineMsAis = _Pm253CtrllineMsAis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 67)
)
_Pm253CtrlLineMsAis_Type = EkiOnOff
_Pm253CtrlLineMsAis_Object = MibScalar
pm253CtrlLineMsAis = _Pm253CtrlLineMsAis_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 67, 1),
    _Pm253CtrlLineMsAis_Type()
)
pm253CtrlLineMsAis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlLineMsAis.setStatus("current")
_Pm253CtrllineUpS1Table_Object = MibTable
pm253CtrllineUpS1Table = _Pm253CtrllineUpS1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 70)
)
if mibBuilder.loadTexts:
    pm253CtrllineUpS1Table.setStatus("current")
_Pm253CtrllineUpS1Entry_Object = MibTableRow
pm253CtrllineUpS1Entry = _Pm253CtrllineUpS1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 70, 1)
)
pm253CtrllineUpS1Entry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253CtrllineUpS1Index"),
)
if mibBuilder.loadTexts:
    pm253CtrllineUpS1Entry.setStatus("current")


class _Pm253CtrllineUpS1Index_Type(Integer32):
    """Custom type pm253CtrllineUpS1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253CtrllineUpS1Index_Type.__name__ = "Integer32"
_Pm253CtrllineUpS1Index_Object = MibTableColumn
pm253CtrllineUpS1Index = _Pm253CtrllineUpS1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 70, 1, 1),
    _Pm253CtrllineUpS1Index_Type()
)
pm253CtrllineUpS1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CtrllineUpS1Index.setStatus("current")


class _Pm253CtrllineUpS1Portn_Type(Integer32):
    """Custom type pm253CtrllineUpS1Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Pm253CtrllineUpS1Portn_Type.__name__ = "Integer32"
_Pm253CtrllineUpS1Portn_Object = MibTableColumn
pm253CtrllineUpS1Portn = _Pm253CtrllineUpS1Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 70, 1, 2),
    _Pm253CtrllineUpS1Portn_Type()
)
pm253CtrllineUpS1Portn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrllineUpS1Portn.setStatus("current")
_Pm253CtrllineUpK1Table_Object = MibTable
pm253CtrllineUpK1Table = _Pm253CtrllineUpK1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 71)
)
if mibBuilder.loadTexts:
    pm253CtrllineUpK1Table.setStatus("current")
_Pm253CtrllineUpK1Entry_Object = MibTableRow
pm253CtrllineUpK1Entry = _Pm253CtrllineUpK1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 71, 1)
)
pm253CtrllineUpK1Entry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253CtrllineUpK1Index"),
)
if mibBuilder.loadTexts:
    pm253CtrllineUpK1Entry.setStatus("current")


class _Pm253CtrllineUpK1Index_Type(Integer32):
    """Custom type pm253CtrllineUpK1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253CtrllineUpK1Index_Type.__name__ = "Integer32"
_Pm253CtrllineUpK1Index_Object = MibTableColumn
pm253CtrllineUpK1Index = _Pm253CtrllineUpK1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 71, 1, 1),
    _Pm253CtrllineUpK1Index_Type()
)
pm253CtrllineUpK1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CtrllineUpK1Index.setStatus("current")


class _Pm253CtrllineUpK1Portn_Type(Integer32):
    """Custom type pm253CtrllineUpK1Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Pm253CtrllineUpK1Portn_Type.__name__ = "Integer32"
_Pm253CtrllineUpK1Portn_Object = MibTableColumn
pm253CtrllineUpK1Portn = _Pm253CtrllineUpK1Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 71, 1, 2),
    _Pm253CtrllineUpK1Portn_Type()
)
pm253CtrllineUpK1Portn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrllineUpK1Portn.setStatus("current")
_Pm253CtrllineUpK2Table_Object = MibTable
pm253CtrllineUpK2Table = _Pm253CtrllineUpK2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 72)
)
if mibBuilder.loadTexts:
    pm253CtrllineUpK2Table.setStatus("current")
_Pm253CtrllineUpK2Entry_Object = MibTableRow
pm253CtrllineUpK2Entry = _Pm253CtrllineUpK2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 72, 1)
)
pm253CtrllineUpK2Entry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253CtrllineUpK2Index"),
)
if mibBuilder.loadTexts:
    pm253CtrllineUpK2Entry.setStatus("current")


class _Pm253CtrllineUpK2Index_Type(Integer32):
    """Custom type pm253CtrllineUpK2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253CtrllineUpK2Index_Type.__name__ = "Integer32"
_Pm253CtrllineUpK2Index_Object = MibTableColumn
pm253CtrllineUpK2Index = _Pm253CtrllineUpK2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 72, 1, 1),
    _Pm253CtrllineUpK2Index_Type()
)
pm253CtrllineUpK2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CtrllineUpK2Index.setStatus("current")


class _Pm253CtrllineUpK2Portn_Type(Integer32):
    """Custom type pm253CtrllineUpK2Portn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Pm253CtrllineUpK2Portn_Type.__name__ = "Integer32"
_Pm253CtrllineUpK2Portn_Object = MibTableColumn
pm253CtrllineUpK2Portn = _Pm253CtrllineUpK2Portn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 72, 1, 2),
    _Pm253CtrllineUpK2Portn_Type()
)
pm253CtrllineUpK2Portn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrllineUpK2Portn.setStatus("current")
_Pm253CtrlProtMgnt_ObjectIdentity = ObjectIdentity
pm253CtrlProtMgnt = _Pm253CtrlProtMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 73)
)


class _Pm253CtrlLineNumber_Type(Unsigned32):
    """Custom type pm253CtrlLineNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Pm253CtrlLineNumber_Type.__name__ = "Unsigned32"
_Pm253CtrlLineNumber_Object = MibScalar
pm253CtrlLineNumber = _Pm253CtrlLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 73, 1),
    _Pm253CtrlLineNumber_Type()
)
pm253CtrlLineNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlLineNumber.setStatus("current")
_Pm253CtrlProtMode_Type = EkiMode
_Pm253CtrlProtMode_Object = MibScalar
pm253CtrlProtMode = _Pm253CtrlProtMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 73, 2),
    _Pm253CtrlProtMode_Type()
)
pm253CtrlProtMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlProtMode.setStatus("current")
_Pm253CtrllineOosModeTable_Object = MibTable
pm253CtrllineOosModeTable = _Pm253CtrllineOosModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 74)
)
if mibBuilder.loadTexts:
    pm253CtrllineOosModeTable.setStatus("current")
_Pm253CtrllineOosModeEntry_Object = MibTableRow
pm253CtrllineOosModeEntry = _Pm253CtrllineOosModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 74, 1)
)
pm253CtrllineOosModeEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253CtrllineOosModeIndex"),
)
if mibBuilder.loadTexts:
    pm253CtrllineOosModeEntry.setStatus("current")


class _Pm253CtrllineOosModeIndex_Type(Integer32):
    """Custom type pm253CtrllineOosModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253CtrllineOosModeIndex_Type.__name__ = "Integer32"
_Pm253CtrllineOosModeIndex_Object = MibTableColumn
pm253CtrllineOosModeIndex = _Pm253CtrllineOosModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 74, 1, 1),
    _Pm253CtrllineOosModeIndex_Type()
)
pm253CtrllineOosModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CtrllineOosModeIndex.setStatus("current")
_Pm253CtrllineOosModePortn_Type = EkiState
_Pm253CtrllineOosModePortn_Object = MibTableColumn
pm253CtrllineOosModePortn = _Pm253CtrllineOosModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 74, 1, 2),
    _Pm253CtrllineOosModePortn_Type()
)
pm253CtrllineOosModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrllineOosModePortn.setStatus("current")
_Pm253Ctrlk1K2Mgnt_ObjectIdentity = ObjectIdentity
pm253Ctrlk1K2Mgnt = _Pm253Ctrlk1K2Mgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 75)
)
_Pm253CtrlK1K2Transparent_Type = EkiOnOff
_Pm253CtrlK1K2Transparent_Object = MibScalar
pm253CtrlK1K2Transparent = _Pm253CtrlK1K2Transparent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 75, 1),
    _Pm253CtrlK1K2Transparent_Type()
)
pm253CtrlK1K2Transparent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlK1K2Transparent.setStatus("current")
_Pm253CtrlApsForceMode_ObjectIdentity = ObjectIdentity
pm253CtrlApsForceMode = _Pm253CtrlApsForceMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 90)
)
_Pm253CtrlApsForceModeLine1_Type = EkiOnOff
_Pm253CtrlApsForceModeLine1_Object = MibScalar
pm253CtrlApsForceModeLine1 = _Pm253CtrlApsForceModeLine1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 90, 1),
    _Pm253CtrlApsForceModeLine1_Type()
)
pm253CtrlApsForceModeLine1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlApsForceModeLine1.setStatus("current")
_Pm253CtrlApsForceModeLine2_Type = EkiOnOff
_Pm253CtrlApsForceModeLine2_Object = MibScalar
pm253CtrlApsForceModeLine2 = _Pm253CtrlApsForceModeLine2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 90, 2),
    _Pm253CtrlApsForceModeLine2_Type()
)
pm253CtrlApsForceModeLine2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlApsForceModeLine2.setStatus("current")
_Pm253CtrlApsManualMode_ObjectIdentity = ObjectIdentity
pm253CtrlApsManualMode = _Pm253CtrlApsManualMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 91)
)
_Pm253CtrlApsManualModeLine1_Type = EkiOnOff
_Pm253CtrlApsManualModeLine1_Object = MibScalar
pm253CtrlApsManualModeLine1 = _Pm253CtrlApsManualModeLine1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 91, 1),
    _Pm253CtrlApsManualModeLine1_Type()
)
pm253CtrlApsManualModeLine1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlApsManualModeLine1.setStatus("current")
_Pm253CtrlApsManualModeLine2_Type = EkiOnOff
_Pm253CtrlApsManualModeLine2_Object = MibScalar
pm253CtrlApsManualModeLine2 = _Pm253CtrlApsManualModeLine2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 91, 2),
    _Pm253CtrlApsManualModeLine2_Type()
)
pm253CtrlApsManualModeLine2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlApsManualModeLine2.setStatus("current")
_Pm253CtrlapsOtherModes_ObjectIdentity = ObjectIdentity
pm253CtrlapsOtherModes = _Pm253CtrlapsOtherModes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 92)
)
_Pm253CtrlLockout_Type = EkiOnOff
_Pm253CtrlLockout_Object = MibScalar
pm253CtrlLockout = _Pm253CtrlLockout_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 92, 1),
    _Pm253CtrlLockout_Type()
)
pm253CtrlLockout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlLockout.setStatus("current")
_Pm253CtrlClear_Type = EkiOnOff
_Pm253CtrlClear_Object = MibScalar
pm253CtrlClear = _Pm253CtrlClear_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 92, 2),
    _Pm253CtrlClear_Type()
)
pm253CtrlClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrlClear.setStatus("current")
_Pm253CtrllineAccessLoopTable_Object = MibTable
pm253CtrllineAccessLoopTable = _Pm253CtrllineAccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 160)
)
if mibBuilder.loadTexts:
    pm253CtrllineAccessLoopTable.setStatus("current")
_Pm253CtrllineAccessLoopEntry_Object = MibTableRow
pm253CtrllineAccessLoopEntry = _Pm253CtrllineAccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 160, 1)
)
pm253CtrllineAccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253CtrllineAccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pm253CtrllineAccessLoopEntry.setStatus("current")


class _Pm253CtrllineAccessLoopIndex_Type(Integer32):
    """Custom type pm253CtrllineAccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253CtrllineAccessLoopIndex_Type.__name__ = "Integer32"
_Pm253CtrllineAccessLoopIndex_Object = MibTableColumn
pm253CtrllineAccessLoopIndex = _Pm253CtrllineAccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 160, 1, 1),
    _Pm253CtrllineAccessLoopIndex_Type()
)
pm253CtrllineAccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CtrllineAccessLoopIndex.setStatus("current")
_Pm253CtrllineAccessLoopPortn_Type = EkiState
_Pm253CtrllineAccessLoopPortn_Object = MibTableColumn
pm253CtrllineAccessLoopPortn = _Pm253CtrllineAccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 160, 1, 2),
    _Pm253CtrllineAccessLoopPortn_Type()
)
pm253CtrllineAccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrllineAccessLoopPortn.setStatus("current")
_Pm253CtrllineLoopTransceiverTable_Object = MibTable
pm253CtrllineLoopTransceiverTable = _Pm253CtrllineLoopTransceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 161)
)
if mibBuilder.loadTexts:
    pm253CtrllineLoopTransceiverTable.setStatus("current")
_Pm253CtrllineLoopTransceiverEntry_Object = MibTableRow
pm253CtrllineLoopTransceiverEntry = _Pm253CtrllineLoopTransceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 161, 1)
)
pm253CtrllineLoopTransceiverEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253CtrllineLoopTransceiverIndex"),
)
if mibBuilder.loadTexts:
    pm253CtrllineLoopTransceiverEntry.setStatus("current")


class _Pm253CtrllineLoopTransceiverIndex_Type(Integer32):
    """Custom type pm253CtrllineLoopTransceiverIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253CtrllineLoopTransceiverIndex_Type.__name__ = "Integer32"
_Pm253CtrllineLoopTransceiverIndex_Object = MibTableColumn
pm253CtrllineLoopTransceiverIndex = _Pm253CtrllineLoopTransceiverIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 161, 1, 1),
    _Pm253CtrllineLoopTransceiverIndex_Type()
)
pm253CtrllineLoopTransceiverIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CtrllineLoopTransceiverIndex.setStatus("current")
_Pm253CtrllineLoopTransceiverPortn_Type = EkiState
_Pm253CtrllineLoopTransceiverPortn_Object = MibTableColumn
pm253CtrllineLoopTransceiverPortn = _Pm253CtrllineLoopTransceiverPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 161, 1, 2),
    _Pm253CtrllineLoopTransceiverPortn_Type()
)
pm253CtrllineLoopTransceiverPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrllineLoopTransceiverPortn.setStatus("current")
_Pm253CtrllineSfpOnOffCtrlTable_Object = MibTable
pm253CtrllineSfpOnOffCtrlTable = _Pm253CtrllineSfpOnOffCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 162)
)
if mibBuilder.loadTexts:
    pm253CtrllineSfpOnOffCtrlTable.setStatus("current")
_Pm253CtrllineSfpOnOffCtrlEntry_Object = MibTableRow
pm253CtrllineSfpOnOffCtrlEntry = _Pm253CtrllineSfpOnOffCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 162, 1)
)
pm253CtrllineSfpOnOffCtrlEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253CtrllineSfpOnOffCtrlIndex"),
)
if mibBuilder.loadTexts:
    pm253CtrllineSfpOnOffCtrlEntry.setStatus("current")


class _Pm253CtrllineSfpOnOffCtrlIndex_Type(Integer32):
    """Custom type pm253CtrllineSfpOnOffCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253CtrllineSfpOnOffCtrlIndex_Type.__name__ = "Integer32"
_Pm253CtrllineSfpOnOffCtrlIndex_Object = MibTableColumn
pm253CtrllineSfpOnOffCtrlIndex = _Pm253CtrllineSfpOnOffCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 162, 1, 1),
    _Pm253CtrllineSfpOnOffCtrlIndex_Type()
)
pm253CtrllineSfpOnOffCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CtrllineSfpOnOffCtrlIndex.setStatus("current")
_Pm253CtrllineSfpOnOffCtrlPortn_Type = EkiState
_Pm253CtrllineSfpOnOffCtrlPortn_Object = MibTableColumn
pm253CtrllineSfpOnOffCtrlPortn = _Pm253CtrllineSfpOnOffCtrlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 162, 1, 2),
    _Pm253CtrllineSfpOnOffCtrlPortn_Type()
)
pm253CtrllineSfpOnOffCtrlPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrllineSfpOnOffCtrlPortn.setStatus("current")
_Pm253CtrllineResetAllCountTable_Object = MibTable
pm253CtrllineResetAllCountTable = _Pm253CtrllineResetAllCountTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 335)
)
if mibBuilder.loadTexts:
    pm253CtrllineResetAllCountTable.setStatus("current")
_Pm253CtrllineResetAllCountEntry_Object = MibTableRow
pm253CtrllineResetAllCountEntry = _Pm253CtrllineResetAllCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 335, 1)
)
pm253CtrllineResetAllCountEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253CtrllineResetAllCountIndex"),
)
if mibBuilder.loadTexts:
    pm253CtrllineResetAllCountEntry.setStatus("current")


class _Pm253CtrllineResetAllCountIndex_Type(Integer32):
    """Custom type pm253CtrllineResetAllCountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253CtrllineResetAllCountIndex_Type.__name__ = "Integer32"
_Pm253CtrllineResetAllCountIndex_Object = MibTableColumn
pm253CtrllineResetAllCountIndex = _Pm253CtrllineResetAllCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 335, 1, 1),
    _Pm253CtrllineResetAllCountIndex_Type()
)
pm253CtrllineResetAllCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CtrllineResetAllCountIndex.setStatus("current")
_Pm253CtrllineResetAllCountsPortn_Type = EkiState
_Pm253CtrllineResetAllCountsPortn_Object = MibTableColumn
pm253CtrllineResetAllCountsPortn = _Pm253CtrllineResetAllCountsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 6, 3, 335, 1, 2),
    _Pm253CtrllineResetAllCountsPortn_Type()
)
pm253CtrllineResetAllCountsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CtrllineResetAllCountsPortn.setStatus("deprecated")
_Pm253ri_ObjectIdentity = ObjectIdentity
pm253ri = _Pm253ri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 7)
)
_Pm253riTable_ObjectIdentity = ObjectIdentity
pm253riTable = _Pm253riTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 7, 1)
)
_Pm253RinvClientTable_Object = MibTable
pm253RinvClientTable = _Pm253RinvClientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 7, 1, 1)
)
if mibBuilder.loadTexts:
    pm253RinvClientTable.setStatus("current")
_Pm253RinvClientEntry_Object = MibTableRow
pm253RinvClientEntry = _Pm253RinvClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 7, 1, 1, 1)
)
pm253RinvClientEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253RinvClientIndex"),
)
if mibBuilder.loadTexts:
    pm253RinvClientEntry.setStatus("current")


class _Pm253RinvClientIndex_Type(Integer32):
    """Custom type pm253RinvClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm253RinvClientIndex_Type.__name__ = "Integer32"
_Pm253RinvClientIndex_Object = MibTableColumn
pm253RinvClientIndex = _Pm253RinvClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 7, 1, 1, 1, 1),
    _Pm253RinvClientIndex_Type()
)
pm253RinvClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253RinvClientIndex.setStatus("current")
_Pm253RinvSfpClient_Type = DisplayString
_Pm253RinvSfpClient_Object = MibTableColumn
pm253RinvSfpClient = _Pm253RinvSfpClient_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 7, 1, 1, 1, 2),
    _Pm253RinvSfpClient_Type()
)
pm253RinvSfpClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253RinvSfpClient.setStatus("current")
_Pm253RinvLineTable_Object = MibTable
pm253RinvLineTable = _Pm253RinvLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pm253RinvLineTable.setStatus("current")
_Pm253RinvLineEntry_Object = MibTableRow
pm253RinvLineEntry = _Pm253RinvLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 7, 1, 2, 1)
)
pm253RinvLineEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253RinvLineIndex"),
)
if mibBuilder.loadTexts:
    pm253RinvLineEntry.setStatus("current")


class _Pm253RinvLineIndex_Type(Integer32):
    """Custom type pm253RinvLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm253RinvLineIndex_Type.__name__ = "Integer32"
_Pm253RinvLineIndex_Object = MibTableColumn
pm253RinvLineIndex = _Pm253RinvLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 7, 1, 2, 1, 1),
    _Pm253RinvLineIndex_Type()
)
pm253RinvLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253RinvLineIndex.setStatus("current")
_Pm253RinvsfpLine_Type = DisplayString
_Pm253RinvsfpLine_Object = MibTableColumn
pm253RinvsfpLine = _Pm253RinvsfpLine_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 7, 1, 2, 1, 2),
    _Pm253RinvsfpLine_Type()
)
pm253RinvsfpLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253RinvsfpLine.setStatus("current")


class _Pm253RinvReloadInventory_Type(Integer32):
    """Custom type pm253RinvReloadInventory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Pm253RinvReloadInventory_Type.__name__ = "Integer32"
_Pm253RinvReloadInventory_Object = MibScalar
pm253RinvReloadInventory = _Pm253RinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 7, 2),
    _Pm253RinvReloadInventory_Type()
)
pm253RinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253RinvReloadInventory.setStatus("current")
_Pm253RinvHwPlatform_Type = DisplayString
_Pm253RinvHwPlatform_Object = MibScalar
pm253RinvHwPlatform = _Pm253RinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 7, 3),
    _Pm253RinvHwPlatform_Type()
)
pm253RinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253RinvHwPlatform.setStatus("current")
_Pm253RinvModulePlatform_Type = DisplayString
_Pm253RinvModulePlatform_Object = MibScalar
pm253RinvModulePlatform = _Pm253RinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 7, 4),
    _Pm253RinvModulePlatform_Type()
)
pm253RinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253RinvModulePlatform.setStatus("current")
_Pm253RinvSwPlatform_Type = DisplayString
_Pm253RinvSwPlatform_Object = MibScalar
pm253RinvSwPlatform = _Pm253RinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 7, 5),
    _Pm253RinvSwPlatform_Type()
)
pm253RinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253RinvSwPlatform.setStatus("current")
_Pm253RinvGwPlatform_Type = DisplayString
_Pm253RinvGwPlatform_Object = MibScalar
pm253RinvGwPlatform = _Pm253RinvGwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 7, 6),
    _Pm253RinvGwPlatform_Type()
)
pm253RinvGwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253RinvGwPlatform.setStatus("current")
_Pm253download_ObjectIdentity = ObjectIdentity
pm253download = _Pm253download_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 8)
)
_Pm253DwlOther_ObjectIdentity = ObjectIdentity
pm253DwlOther = _Pm253DwlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 8, 1)
)
_Pm253DwlrestartProcess_ObjectIdentity = ObjectIdentity
pm253DwlrestartProcess = _Pm253DwlrestartProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 8, 1, 0)
)
_Pm253DwlWarmRestartProcessed_Type = EkiOnOff
_Pm253DwlWarmRestartProcessed_Object = MibScalar
pm253DwlWarmRestartProcessed = _Pm253DwlWarmRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 8, 1, 0, 1),
    _Pm253DwlWarmRestartProcessed_Type()
)
pm253DwlWarmRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253DwlWarmRestartProcessed.setStatus("current")
_Pm253DwlColdRestartProcessed_Type = EkiOnOff
_Pm253DwlColdRestartProcessed_Object = MibScalar
pm253DwlColdRestartProcessed = _Pm253DwlColdRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 8, 1, 0, 2),
    _Pm253DwlColdRestartProcessed_Type()
)
pm253DwlColdRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253DwlColdRestartProcessed.setStatus("current")
_Pm253DwlswBanksUsed_ObjectIdentity = ObjectIdentity
pm253DwlswBanksUsed = _Pm253DwlswBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 8, 1, 1)
)
_Pm253DwlSwBank1Used_Type = EkiOnOff
_Pm253DwlSwBank1Used_Object = MibScalar
pm253DwlSwBank1Used = _Pm253DwlSwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 8, 1, 1, 1),
    _Pm253DwlSwBank1Used_Type()
)
pm253DwlSwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253DwlSwBank1Used.setStatus("current")
_Pm253DwlSwBank2Used_Type = EkiOnOff
_Pm253DwlSwBank2Used_Object = MibScalar
pm253DwlSwBank2Used = _Pm253DwlSwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 8, 1, 1, 2),
    _Pm253DwlSwBank2Used_Type()
)
pm253DwlSwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253DwlSwBank2Used.setStatus("current")
_Pm253DwlSwBank1Notempty_Type = EkiOnOff
_Pm253DwlSwBank1Notempty_Object = MibScalar
pm253DwlSwBank1Notempty = _Pm253DwlSwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 8, 1, 1, 5),
    _Pm253DwlSwBank1Notempty_Type()
)
pm253DwlSwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253DwlSwBank1Notempty.setStatus("current")
_Pm253DwlSwBank2Notempty_Type = EkiOnOff
_Pm253DwlSwBank2Notempty_Object = MibScalar
pm253DwlSwBank2Notempty = _Pm253DwlSwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 8, 1, 1, 6),
    _Pm253DwlSwBank2Notempty_Type()
)
pm253DwlSwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253DwlSwBank2Notempty.setStatus("current")
_Pm253DwlgwBanksUsed_ObjectIdentity = ObjectIdentity
pm253DwlgwBanksUsed = _Pm253DwlgwBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 8, 1, 2)
)
_Pm253DwlGwBank1Used_Type = EkiOnOff
_Pm253DwlGwBank1Used_Object = MibScalar
pm253DwlGwBank1Used = _Pm253DwlGwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 8, 1, 2, 1),
    _Pm253DwlGwBank1Used_Type()
)
pm253DwlGwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253DwlGwBank1Used.setStatus("current")
_Pm253DwlGwBank2Used_Type = EkiOnOff
_Pm253DwlGwBank2Used_Object = MibScalar
pm253DwlGwBank2Used = _Pm253DwlGwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 8, 1, 2, 2),
    _Pm253DwlGwBank2Used_Type()
)
pm253DwlGwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253DwlGwBank2Used.setStatus("current")
_Pm253DwlGwBank3Used_Type = EkiOnOff
_Pm253DwlGwBank3Used_Object = MibScalar
pm253DwlGwBank3Used = _Pm253DwlGwBank3Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 8, 1, 2, 3),
    _Pm253DwlGwBank3Used_Type()
)
pm253DwlGwBank3Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253DwlGwBank3Used.setStatus("current")
_Pm253DwlGwBank4Used_Type = EkiOnOff
_Pm253DwlGwBank4Used_Object = MibScalar
pm253DwlGwBank4Used = _Pm253DwlGwBank4Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 8, 1, 2, 4),
    _Pm253DwlGwBank4Used_Type()
)
pm253DwlGwBank4Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253DwlGwBank4Used.setStatus("current")
_Pm253DwlGwBank1Notempty_Type = EkiOnOff
_Pm253DwlGwBank1Notempty_Object = MibScalar
pm253DwlGwBank1Notempty = _Pm253DwlGwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 8, 1, 2, 5),
    _Pm253DwlGwBank1Notempty_Type()
)
pm253DwlGwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253DwlGwBank1Notempty.setStatus("current")
_Pm253DwlGwBank2Notempty_Type = EkiOnOff
_Pm253DwlGwBank2Notempty_Object = MibScalar
pm253DwlGwBank2Notempty = _Pm253DwlGwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 8, 1, 2, 6),
    _Pm253DwlGwBank2Notempty_Type()
)
pm253DwlGwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253DwlGwBank2Notempty.setStatus("current")
_Pm253DwlGwBank3Notempty_Type = EkiOnOff
_Pm253DwlGwBank3Notempty_Object = MibScalar
pm253DwlGwBank3Notempty = _Pm253DwlGwBank3Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 8, 1, 2, 7),
    _Pm253DwlGwBank3Notempty_Type()
)
pm253DwlGwBank3Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253DwlGwBank3Notempty.setStatus("current")
_Pm253DwlGwBank4Notempty_Type = EkiOnOff
_Pm253DwlGwBank4Notempty_Object = MibScalar
pm253DwlGwBank4Notempty = _Pm253DwlGwBank4Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 8, 1, 2, 8),
    _Pm253DwlGwBank4Notempty_Type()
)
pm253DwlGwBank4Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253DwlGwBank4Notempty.setStatus("current")
_Pm253DwlPort_ObjectIdentity = ObjectIdentity
pm253DwlPort = _Pm253DwlPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 8, 2)
)
_Pm253DwlLine_ObjectIdentity = ObjectIdentity
pm253DwlLine = _Pm253DwlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 8, 3)
)
_Pm253Config_ObjectIdentity = ObjectIdentity
pm253Config = _Pm253Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 9)
)
_Pm253CfgAccessCAisCsf_ObjectIdentity = ObjectIdentity
pm253CfgAccessCAisCsf = _Pm253CfgAccessCAisCsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 9, 1)
)
_Pm253CfgClientcaiscsfTable_Object = MibTable
pm253CfgClientcaiscsfTable = _Pm253CfgClientcaiscsfTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 9, 1, 1)
)
if mibBuilder.loadTexts:
    pm253CfgClientcaiscsfTable.setStatus("current")
_Pm253CfgClientcaiscsfEntry_Object = MibTableRow
pm253CfgClientcaiscsfEntry = _Pm253CfgClientcaiscsfEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 9, 1, 1, 1)
)
pm253CfgClientcaiscsfEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253CfgClientcaiscsfIndex"),
)
if mibBuilder.loadTexts:
    pm253CfgClientcaiscsfEntry.setStatus("current")


class _Pm253CfgClientcaiscsfIndex_Type(Integer32):
    """Custom type pm253CfgClientcaiscsfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253CfgClientcaiscsfIndex_Type.__name__ = "Integer32"
_Pm253CfgClientcaiscsfIndex_Object = MibTableColumn
pm253CfgClientcaiscsfIndex = _Pm253CfgClientcaiscsfIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 9, 1, 1, 1, 1),
    _Pm253CfgClientcaiscsfIndex_Type()
)
pm253CfgClientcaiscsfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CfgClientcaiscsfIndex.setStatus("current")


class _Pm253CfgCAisModePortn_Type(Unsigned32):
    """Custom type pm253CfgCAisModePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm253CfgCAisModePortn_Type.__name__ = "Unsigned32"
_Pm253CfgCAisModePortn_Object = MibTableColumn
pm253CfgCAisModePortn = _Pm253CfgCAisModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 9, 1, 1, 1, 3),
    _Pm253CfgCAisModePortn_Type()
)
pm253CfgCAisModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CfgCAisModePortn.setStatus("current")


class _Pm253CfgSts24cContribPortn_Type(Unsigned32):
    """Custom type pm253CfgSts24cContribPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm253CfgSts24cContribPortn_Type.__name__ = "Unsigned32"
_Pm253CfgSts24cContribPortn_Object = MibTableColumn
pm253CfgSts24cContribPortn = _Pm253CfgSts24cContribPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 9, 1, 1, 1, 4),
    _Pm253CfgSts24cContribPortn_Type()
)
pm253CfgSts24cContribPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CfgSts24cContribPortn.setStatus("current")


class _Pm253CfgUpAccessioAlmPortn_Type(Unsigned32):
    """Custom type pm253CfgUpAccessioAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm253CfgUpAccessioAlmPortn_Type.__name__ = "Unsigned32"
_Pm253CfgUpAccessioAlmPortn_Object = MibTableColumn
pm253CfgUpAccessioAlmPortn = _Pm253CfgUpAccessioAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 9, 1, 1, 1, 9),
    _Pm253CfgUpAccessioAlmPortn_Type()
)
pm253CfgUpAccessioAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CfgUpAccessioAlmPortn.setStatus("current")


class _Pm253CfgUpMapperDeAlmPortn_Type(Unsigned32):
    """Custom type pm253CfgUpMapperDeAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm253CfgUpMapperDeAlmPortn_Type.__name__ = "Unsigned32"
_Pm253CfgUpMapperDeAlmPortn_Object = MibTableColumn
pm253CfgUpMapperDeAlmPortn = _Pm253CfgUpMapperDeAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 9, 1, 1, 1, 10),
    _Pm253CfgUpMapperDeAlmPortn_Type()
)
pm253CfgUpMapperDeAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CfgUpMapperDeAlmPortn.setStatus("current")


class _Pm253CfgDownMapperDeAlmPortn_Type(Unsigned32):
    """Custom type pm253CfgDownMapperDeAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm253CfgDownMapperDeAlmPortn_Type.__name__ = "Unsigned32"
_Pm253CfgDownMapperDeAlmPortn_Object = MibTableColumn
pm253CfgDownMapperDeAlmPortn = _Pm253CfgDownMapperDeAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 9, 1, 1, 1, 18),
    _Pm253CfgDownMapperDeAlmPortn_Type()
)
pm253CfgDownMapperDeAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CfgDownMapperDeAlmPortn.setStatus("current")


class _Pm253CfgDownDfrmAlmPortn_Type(Unsigned32):
    """Custom type pm253CfgDownDfrmAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm253CfgDownDfrmAlmPortn_Type.__name__ = "Unsigned32"
_Pm253CfgDownDfrmAlmPortn_Object = MibTableColumn
pm253CfgDownDfrmAlmPortn = _Pm253CfgDownDfrmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 9, 1, 1, 1, 19),
    _Pm253CfgDownDfrmAlmPortn_Type()
)
pm253CfgDownDfrmAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CfgDownDfrmAlmPortn.setStatus("current")


class _Pm253CfgDownLineIoAlmPortn_Type(Unsigned32):
    """Custom type pm253CfgDownLineIoAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm253CfgDownLineIoAlmPortn_Type.__name__ = "Unsigned32"
_Pm253CfgDownLineIoAlmPortn_Object = MibTableColumn
pm253CfgDownLineIoAlmPortn = _Pm253CfgDownLineIoAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 9, 1, 1, 1, 22),
    _Pm253CfgDownLineIoAlmPortn_Type()
)
pm253CfgDownLineIoAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CfgDownLineIoAlmPortn.setStatus("deprecated")
_Pm253CfgStartup_ObjectIdentity = ObjectIdentity
pm253CfgStartup = _Pm253CfgStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 9, 2)
)
_Pm253CfgClientStartupTable_Object = MibTable
pm253CfgClientStartupTable = _Pm253CfgClientStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 9, 2, 1)
)
if mibBuilder.loadTexts:
    pm253CfgClientStartupTable.setStatus("current")
_Pm253CfgClientStartupEntry_Object = MibTableRow
pm253CfgClientStartupEntry = _Pm253CfgClientStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 9, 2, 1, 1)
)
pm253CfgClientStartupEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253CfgClientStartupIndex"),
)
if mibBuilder.loadTexts:
    pm253CfgClientStartupEntry.setStatus("current")


class _Pm253CfgClientStartupIndex_Type(Integer32):
    """Custom type pm253CfgClientStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253CfgClientStartupIndex_Type.__name__ = "Integer32"
_Pm253CfgClientStartupIndex_Object = MibTableColumn
pm253CfgClientStartupIndex = _Pm253CfgClientStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 9, 2, 1, 1, 1),
    _Pm253CfgClientStartupIndex_Type()
)
pm253CfgClientStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CfgClientStartupIndex.setStatus("current")


class _Pm253CfgSystConfPortPortn_Type(Unsigned32):
    """Custom type pm253CfgSystConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm253CfgSystConfPortPortn_Type.__name__ = "Unsigned32"
_Pm253CfgSystConfPortPortn_Object = MibTableColumn
pm253CfgSystConfPortPortn = _Pm253CfgSystConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 9, 2, 1, 1, 3),
    _Pm253CfgSystConfPortPortn_Type()
)
pm253CfgSystConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CfgSystConfPortPortn.setStatus("current")


class _Pm253CfgNetConfPortPortn_Type(Unsigned32):
    """Custom type pm253CfgNetConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm253CfgNetConfPortPortn_Type.__name__ = "Unsigned32"
_Pm253CfgNetConfPortPortn_Object = MibTableColumn
pm253CfgNetConfPortPortn = _Pm253CfgNetConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 9, 2, 1, 1, 4),
    _Pm253CfgNetConfPortPortn_Type()
)
pm253CfgNetConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CfgNetConfPortPortn.setStatus("current")


class _Pm253CfgPortsOptionsPortn_Type(Unsigned32):
    """Custom type pm253CfgPortsOptionsPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm253CfgPortsOptionsPortn_Type.__name__ = "Unsigned32"
_Pm253CfgPortsOptionsPortn_Object = MibTableColumn
pm253CfgPortsOptionsPortn = _Pm253CfgPortsOptionsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 9, 2, 1, 1, 6),
    _Pm253CfgPortsOptionsPortn_Type()
)
pm253CfgPortsOptionsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CfgPortsOptionsPortn.setStatus("deprecated")
_Pm253tablelineStartup_ObjectIdentity = ObjectIdentity
pm253tablelineStartup = _Pm253tablelineStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 9, 2, 2)
)


class _Pm253CfgsystConfLine1_Type(Unsigned32):
    """Custom type pm253CfgsystConfLine1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm253CfgsystConfLine1_Type.__name__ = "Unsigned32"
_Pm253CfgsystConfLine1_Object = MibScalar
pm253CfgsystConfLine1 = _Pm253CfgsystConfLine1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 9, 2, 2, 2),
    _Pm253CfgsystConfLine1_Type()
)
pm253CfgsystConfLine1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CfgsystConfLine1.setStatus("current")


class _Pm253CfgsystConfLine2_Type(Unsigned32):
    """Custom type pm253CfgsystConfLine2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm253CfgsystConfLine2_Type.__name__ = "Unsigned32"
_Pm253CfgsystConfLine2_Object = MibScalar
pm253CfgsystConfLine2 = _Pm253CfgsystConfLine2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 9, 2, 2, 6),
    _Pm253CfgsystConfLine2_Type()
)
pm253CfgsystConfLine2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CfgsystConfLine2.setStatus("current")


class _Pm253CfglineSelection_Type(Unsigned32):
    """Custom type pm253CfglineSelection based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm253CfglineSelection_Type.__name__ = "Unsigned32"
_Pm253CfglineSelection_Object = MibScalar
pm253CfglineSelection = _Pm253CfglineSelection_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 9, 2, 2, 7),
    _Pm253CfglineSelection_Type()
)
pm253CfglineSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CfglineSelection.setStatus("current")


class _Pm253CfglineOptions_Type(Unsigned32):
    """Custom type pm253CfglineOptions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm253CfglineOptions_Type.__name__ = "Unsigned32"
_Pm253CfglineOptions_Object = MibScalar
pm253CfglineOptions = _Pm253CfglineOptions_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 9, 2, 2, 9),
    _Pm253CfglineOptions_Type()
)
pm253CfglineOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CfglineOptions.setStatus("current")
_Pm253CfgLabels_ObjectIdentity = ObjectIdentity
pm253CfgLabels = _Pm253CfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 9, 3)
)
_Pm253CfgLabelclientTable_Object = MibTable
pm253CfgLabelclientTable = _Pm253CfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 9, 3, 1)
)
if mibBuilder.loadTexts:
    pm253CfgLabelclientTable.setStatus("current")
_Pm253CfgLabelclientEntry_Object = MibTableRow
pm253CfgLabelclientEntry = _Pm253CfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 9, 3, 1, 1)
)
pm253CfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253CfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pm253CfgLabelclientEntry.setStatus("current")


class _Pm253CfgLabelclientIndex_Type(Integer32):
    """Custom type pm253CfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253CfgLabelclientIndex_Type.__name__ = "Integer32"
_Pm253CfgLabelclientIndex_Object = MibTableColumn
pm253CfgLabelclientIndex = _Pm253CfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 9, 3, 1, 1, 1),
    _Pm253CfgLabelclientIndex_Type()
)
pm253CfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CfgLabelclientIndex.setStatus("current")


class _Pm253CfgLabelclientPortn_Type(DisplayString):
    """Custom type pm253CfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm253CfgLabelclientPortn_Type.__name__ = "DisplayString"
_Pm253CfgLabelclientPortn_Object = MibTableColumn
pm253CfgLabelclientPortn = _Pm253CfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 9, 3, 1, 1, 3),
    _Pm253CfgLabelclientPortn_Type()
)
pm253CfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CfgLabelclientPortn.setStatus("current")
_Pm253CfgLabellineTable_Object = MibTable
pm253CfgLabellineTable = _Pm253CfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 9, 3, 2)
)
if mibBuilder.loadTexts:
    pm253CfgLabellineTable.setStatus("current")
_Pm253CfgLabellineEntry_Object = MibTableRow
pm253CfgLabellineEntry = _Pm253CfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 9, 3, 2, 1)
)
pm253CfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253CfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pm253CfgLabellineEntry.setStatus("current")


class _Pm253CfgLabellineIndex_Type(Integer32):
    """Custom type pm253CfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253CfgLabellineIndex_Type.__name__ = "Integer32"
_Pm253CfgLabellineIndex_Object = MibTableColumn
pm253CfgLabellineIndex = _Pm253CfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 9, 3, 2, 1, 1),
    _Pm253CfgLabellineIndex_Type()
)
pm253CfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253CfgLabellineIndex.setStatus("current")


class _Pm253CfgLabellinePortn_Type(DisplayString):
    """Custom type pm253CfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm253CfgLabellinePortn_Type.__name__ = "DisplayString"
_Pm253CfgLabellinePortn_Object = MibTableColumn
pm253CfgLabellinePortn = _Pm253CfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 9, 3, 2, 1, 3),
    _Pm253CfgLabellinePortn_Type()
)
pm253CfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CfgLabellinePortn.setStatus("current")
_Pm253CfgWriteConfiguration_Type = EkiOnOff
_Pm253CfgWriteConfiguration_Object = MibScalar
pm253CfgWriteConfiguration = _Pm253CfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 9, 257),
    _Pm253CfgWriteConfiguration_Type()
)
pm253CfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253CfgWriteConfiguration.setStatus("current")
_Pm253traps_ObjectIdentity = ObjectIdentity
pm253traps = _Pm253traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 10)
)


class _Pm253TrapPortNumber_Type(Integer32):
    """Custom type pm253TrapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm253TrapPortNumber_Type.__name__ = "Integer32"
_Pm253TrapPortNumber_Object = MibScalar
pm253TrapPortNumber = _Pm253TrapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 10, 2),
    _Pm253TrapPortNumber_Type()
)
pm253TrapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253TrapPortNumber.setStatus("current")


class _Pm253TrapBoardNumber_Type(Integer32):
    """Custom type pm253TrapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm253TrapBoardNumber_Type.__name__ = "Integer32"
_Pm253TrapBoardNumber_Object = MibScalar
pm253TrapBoardNumber = _Pm253TrapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 10, 3),
    _Pm253TrapBoardNumber_Type()
)
pm253TrapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253TrapBoardNumber.setStatus("current")


class _Pm253TrapLineNumber_Type(Integer32):
    """Custom type pm253TrapLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm253TrapLineNumber_Type.__name__ = "Integer32"
_Pm253TrapLineNumber_Object = MibScalar
pm253TrapLineNumber = _Pm253TrapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 10, 4),
    _Pm253TrapLineNumber_Type()
)
pm253TrapLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253TrapLineNumber.setStatus("current")
_Pm253Monitoring_ObjectIdentity = ObjectIdentity
pm253Monitoring = _Pm253Monitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11)
)
_Pm253MonOther_ObjectIdentity = ObjectIdentity
pm253MonOther = _Pm253MonOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 1)
)
_Pm253MonSync_ObjectIdentity = ObjectIdentity
pm253MonSync = _Pm253MonSync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 1, 1)
)
_Pm253PerfEnable_Type = EkiOnOff
_Pm253PerfEnable_Object = MibScalar
pm253PerfEnable = _Pm253PerfEnable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 1, 1, 257),
    _Pm253PerfEnable_Type()
)
pm253PerfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253PerfEnable.setStatus("current")
_Pm253Perf15minSync_Type = EkiOnOff
_Pm253Perf15minSync_Object = MibScalar
pm253Perf15minSync = _Pm253Perf15minSync_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 1, 1, 259),
    _Pm253Perf15minSync_Type()
)
pm253Perf15minSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253Perf15minSync.setStatus("current")
_Pm253Perf24hSync_Type = EkiOnOff
_Pm253Perf24hSync_Object = MibScalar
pm253Perf24hSync = _Pm253Perf24hSync_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 1, 1, 260),
    _Pm253Perf24hSync_Type()
)
pm253Perf24hSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253Perf24hSync.setStatus("current")
_Pm253MonTimeStamp_ObjectIdentity = ObjectIdentity
pm253MonTimeStamp = _Pm253MonTimeStamp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 1, 2)
)
_Pm253Perf15MinShort_Type = EkiOnOff
_Pm253Perf15MinShort_Object = MibScalar
pm253Perf15MinShort = _Pm253Perf15MinShort_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 1, 2, 1),
    _Pm253Perf15MinShort_Type()
)
pm253Perf15MinShort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253Perf15MinShort.setStatus("current")
_Pm253Perf15MinLong_Type = EkiOnOff
_Pm253Perf15MinLong_Object = MibScalar
pm253Perf15MinLong = _Pm253Perf15MinLong_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 1, 2, 2),
    _Pm253Perf15MinLong_Type()
)
pm253Perf15MinLong.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253Perf15MinLong.setStatus("current")
_Pm253Perf24HoursShort_Type = Counter32
_Pm253Perf24HoursShort_Object = MibScalar
pm253Perf24HoursShort = _Pm253Perf24HoursShort_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 1, 2, 5),
    _Pm253Perf24HoursShort_Type()
)
pm253Perf24HoursShort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253Perf24HoursShort.setStatus("current")
_Pm253Perf24HoursLong_Type = Counter32
_Pm253Perf24HoursLong_Object = MibScalar
pm253Perf24HoursLong = _Pm253Perf24HoursLong_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 1, 2, 6),
    _Pm253Perf24HoursLong_Type()
)
pm253Perf24HoursLong.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253Perf24HoursLong.setStatus("current")
_Pm253PerfCurrent15MinElapsedTime_Type = Counter32
_Pm253PerfCurrent15MinElapsedTime_Object = MibScalar
pm253PerfCurrent15MinElapsedTime = _Pm253PerfCurrent15MinElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 1, 2, 7),
    _Pm253PerfCurrent15MinElapsedTime_Type()
)
pm253PerfCurrent15MinElapsedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253PerfCurrent15MinElapsedTime.setStatus("current")
_Pm253PerfCurrent24HoursElapsedTime_Type = Counter32
_Pm253PerfCurrent24HoursElapsedTime_Object = MibScalar
pm253PerfCurrent24HoursElapsedTime = _Pm253PerfCurrent24HoursElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 1, 2, 8),
    _Pm253PerfCurrent24HoursElapsedTime_Type()
)
pm253PerfCurrent24HoursElapsedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253PerfCurrent24HoursElapsedTime.setStatus("current")
_Pm253MonRmon_ObjectIdentity = ObjectIdentity
pm253MonRmon = _Pm253MonRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 1, 3)
)
_Pm253MonCountersReset_Type = EkiOnOff
_Pm253MonCountersReset_Object = MibScalar
pm253MonCountersReset = _Pm253MonCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 1, 3, 359),
    _Pm253MonCountersReset_Type()
)
pm253MonCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253MonCountersReset.setStatus("current")
_Pm253MonCountersStop_Type = EkiOnOff
_Pm253MonCountersStop_Object = MibScalar
pm253MonCountersStop = _Pm253MonCountersStop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 1, 3, 360),
    _Pm253MonCountersStop_Type()
)
pm253MonCountersStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm253MonCountersStop.setStatus("current")
_Pm253MonClient_ObjectIdentity = ObjectIdentity
pm253MonClient = _Pm253MonClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2)
)
_Pm253MonClientRmonCounter_ObjectIdentity = ObjectIdentity
pm253MonClientRmonCounter = _Pm253MonClientRmonCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4)
)
_Pm253MonupRmonByteCntTable_Object = MibTable
pm253MonupRmonByteCntTable = _Pm253MonupRmonByteCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 16)
)
if mibBuilder.loadTexts:
    pm253MonupRmonByteCntTable.setStatus("current")
_Pm253MonupRmonByteCntEntry_Object = MibTableRow
pm253MonupRmonByteCntEntry = _Pm253MonupRmonByteCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 16, 1)
)
pm253MonupRmonByteCntEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253MonupRmonByteCntIndex"),
)
if mibBuilder.loadTexts:
    pm253MonupRmonByteCntEntry.setStatus("current")


class _Pm253MonupRmonByteCntIndex_Type(Integer32):
    """Custom type pm253MonupRmonByteCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253MonupRmonByteCntIndex_Type.__name__ = "Integer32"
_Pm253MonupRmonByteCntIndex_Object = MibTableColumn
pm253MonupRmonByteCntIndex = _Pm253MonupRmonByteCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 16, 1, 1),
    _Pm253MonupRmonByteCntIndex_Type()
)
pm253MonupRmonByteCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonByteCntIndex.setStatus("current")
_Pm253MonupRmonByteCntValuePortn_Type = Counter64
_Pm253MonupRmonByteCntValuePortn_Object = MibTableColumn
pm253MonupRmonByteCntValuePortn = _Pm253MonupRmonByteCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 16, 1, 2),
    _Pm253MonupRmonByteCntValuePortn_Type()
)
pm253MonupRmonByteCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonByteCntValuePortn.setStatus("current")
_Pm253MonupRmonByteCntErrorPortn_Type = EkiOnOff
_Pm253MonupRmonByteCntErrorPortn_Object = MibTableColumn
pm253MonupRmonByteCntErrorPortn = _Pm253MonupRmonByteCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 16, 1, 3),
    _Pm253MonupRmonByteCntErrorPortn_Type()
)
pm253MonupRmonByteCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonByteCntErrorPortn.setStatus("current")
_Pm253MonupRmonByteCntOverloadPortn_Type = EkiOnOff
_Pm253MonupRmonByteCntOverloadPortn_Object = MibTableColumn
pm253MonupRmonByteCntOverloadPortn = _Pm253MonupRmonByteCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 16, 1, 4),
    _Pm253MonupRmonByteCntOverloadPortn_Type()
)
pm253MonupRmonByteCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonByteCntOverloadPortn.setStatus("current")
_Pm253MonupRmonCrcErrorCntTable_Object = MibTable
pm253MonupRmonCrcErrorCntTable = _Pm253MonupRmonCrcErrorCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 24)
)
if mibBuilder.loadTexts:
    pm253MonupRmonCrcErrorCntTable.setStatus("current")
_Pm253MonupRmonCrcErrorCntEntry_Object = MibTableRow
pm253MonupRmonCrcErrorCntEntry = _Pm253MonupRmonCrcErrorCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 24, 1)
)
pm253MonupRmonCrcErrorCntEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253MonupRmonCrcErrorCntIndex"),
)
if mibBuilder.loadTexts:
    pm253MonupRmonCrcErrorCntEntry.setStatus("current")


class _Pm253MonupRmonCrcErrorCntIndex_Type(Integer32):
    """Custom type pm253MonupRmonCrcErrorCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253MonupRmonCrcErrorCntIndex_Type.__name__ = "Integer32"
_Pm253MonupRmonCrcErrorCntIndex_Object = MibTableColumn
pm253MonupRmonCrcErrorCntIndex = _Pm253MonupRmonCrcErrorCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 24, 1, 1),
    _Pm253MonupRmonCrcErrorCntIndex_Type()
)
pm253MonupRmonCrcErrorCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonCrcErrorCntIndex.setStatus("current")
_Pm253MonupRmonCrcErrorCntValuePortn_Type = Counter64
_Pm253MonupRmonCrcErrorCntValuePortn_Object = MibTableColumn
pm253MonupRmonCrcErrorCntValuePortn = _Pm253MonupRmonCrcErrorCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 24, 1, 2),
    _Pm253MonupRmonCrcErrorCntValuePortn_Type()
)
pm253MonupRmonCrcErrorCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonCrcErrorCntValuePortn.setStatus("current")
_Pm253MonupRmonCrcErrorCntErrorPortn_Type = EkiOnOff
_Pm253MonupRmonCrcErrorCntErrorPortn_Object = MibTableColumn
pm253MonupRmonCrcErrorCntErrorPortn = _Pm253MonupRmonCrcErrorCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 24, 1, 3),
    _Pm253MonupRmonCrcErrorCntErrorPortn_Type()
)
pm253MonupRmonCrcErrorCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonCrcErrorCntErrorPortn.setStatus("current")
_Pm253MonupRmonCrcErrorCntOverloadPortn_Type = EkiOnOff
_Pm253MonupRmonCrcErrorCntOverloadPortn_Object = MibTableColumn
pm253MonupRmonCrcErrorCntOverloadPortn = _Pm253MonupRmonCrcErrorCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 24, 1, 4),
    _Pm253MonupRmonCrcErrorCntOverloadPortn_Type()
)
pm253MonupRmonCrcErrorCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonCrcErrorCntOverloadPortn.setStatus("current")
_Pm253MonupRmonPacketsCntTable_Object = MibTable
pm253MonupRmonPacketsCntTable = _Pm253MonupRmonPacketsCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 32)
)
if mibBuilder.loadTexts:
    pm253MonupRmonPacketsCntTable.setStatus("current")
_Pm253MonupRmonPacketsCntEntry_Object = MibTableRow
pm253MonupRmonPacketsCntEntry = _Pm253MonupRmonPacketsCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 32, 1)
)
pm253MonupRmonPacketsCntEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253MonupRmonPacketsCntIndex"),
)
if mibBuilder.loadTexts:
    pm253MonupRmonPacketsCntEntry.setStatus("current")


class _Pm253MonupRmonPacketsCntIndex_Type(Integer32):
    """Custom type pm253MonupRmonPacketsCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253MonupRmonPacketsCntIndex_Type.__name__ = "Integer32"
_Pm253MonupRmonPacketsCntIndex_Object = MibTableColumn
pm253MonupRmonPacketsCntIndex = _Pm253MonupRmonPacketsCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 32, 1, 1),
    _Pm253MonupRmonPacketsCntIndex_Type()
)
pm253MonupRmonPacketsCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonPacketsCntIndex.setStatus("current")
_Pm253MonupRmonPacketsCntValuePortn_Type = Counter64
_Pm253MonupRmonPacketsCntValuePortn_Object = MibTableColumn
pm253MonupRmonPacketsCntValuePortn = _Pm253MonupRmonPacketsCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 32, 1, 2),
    _Pm253MonupRmonPacketsCntValuePortn_Type()
)
pm253MonupRmonPacketsCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonPacketsCntValuePortn.setStatus("current")
_Pm253MonupRmonPacketsCntErrorPortn_Type = EkiOnOff
_Pm253MonupRmonPacketsCntErrorPortn_Object = MibTableColumn
pm253MonupRmonPacketsCntErrorPortn = _Pm253MonupRmonPacketsCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 32, 1, 3),
    _Pm253MonupRmonPacketsCntErrorPortn_Type()
)
pm253MonupRmonPacketsCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonPacketsCntErrorPortn.setStatus("current")
_Pm253MonupRmonPacketsCntOverloadPortn_Type = EkiOnOff
_Pm253MonupRmonPacketsCntOverloadPortn_Object = MibTableColumn
pm253MonupRmonPacketsCntOverloadPortn = _Pm253MonupRmonPacketsCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 32, 1, 4),
    _Pm253MonupRmonPacketsCntOverloadPortn_Type()
)
pm253MonupRmonPacketsCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonPacketsCntOverloadPortn.setStatus("current")
_Pm253MonupRmonBroadcastCntTable_Object = MibTable
pm253MonupRmonBroadcastCntTable = _Pm253MonupRmonBroadcastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 40)
)
if mibBuilder.loadTexts:
    pm253MonupRmonBroadcastCntTable.setStatus("current")
_Pm253MonupRmonBroadcastCntEntry_Object = MibTableRow
pm253MonupRmonBroadcastCntEntry = _Pm253MonupRmonBroadcastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 40, 1)
)
pm253MonupRmonBroadcastCntEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253MonupRmonBroadcastCntIndex"),
)
if mibBuilder.loadTexts:
    pm253MonupRmonBroadcastCntEntry.setStatus("current")


class _Pm253MonupRmonBroadcastCntIndex_Type(Integer32):
    """Custom type pm253MonupRmonBroadcastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253MonupRmonBroadcastCntIndex_Type.__name__ = "Integer32"
_Pm253MonupRmonBroadcastCntIndex_Object = MibTableColumn
pm253MonupRmonBroadcastCntIndex = _Pm253MonupRmonBroadcastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 40, 1, 1),
    _Pm253MonupRmonBroadcastCntIndex_Type()
)
pm253MonupRmonBroadcastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonBroadcastCntIndex.setStatus("current")
_Pm253MonupRmonBroadcastCntValuePortn_Type = Counter64
_Pm253MonupRmonBroadcastCntValuePortn_Object = MibTableColumn
pm253MonupRmonBroadcastCntValuePortn = _Pm253MonupRmonBroadcastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 40, 1, 2),
    _Pm253MonupRmonBroadcastCntValuePortn_Type()
)
pm253MonupRmonBroadcastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonBroadcastCntValuePortn.setStatus("current")
_Pm253MonupRmonBroadcastCntErrorPortn_Type = EkiOnOff
_Pm253MonupRmonBroadcastCntErrorPortn_Object = MibTableColumn
pm253MonupRmonBroadcastCntErrorPortn = _Pm253MonupRmonBroadcastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 40, 1, 3),
    _Pm253MonupRmonBroadcastCntErrorPortn_Type()
)
pm253MonupRmonBroadcastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonBroadcastCntErrorPortn.setStatus("current")
_Pm253MonupRmonBroadcastCntOverloadPortn_Type = EkiOnOff
_Pm253MonupRmonBroadcastCntOverloadPortn_Object = MibTableColumn
pm253MonupRmonBroadcastCntOverloadPortn = _Pm253MonupRmonBroadcastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 40, 1, 4),
    _Pm253MonupRmonBroadcastCntOverloadPortn_Type()
)
pm253MonupRmonBroadcastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonBroadcastCntOverloadPortn.setStatus("current")
_Pm253MonupRmonMulticastCntTable_Object = MibTable
pm253MonupRmonMulticastCntTable = _Pm253MonupRmonMulticastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 48)
)
if mibBuilder.loadTexts:
    pm253MonupRmonMulticastCntTable.setStatus("current")
_Pm253MonupRmonMulticastCntEntry_Object = MibTableRow
pm253MonupRmonMulticastCntEntry = _Pm253MonupRmonMulticastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 48, 1)
)
pm253MonupRmonMulticastCntEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253MonupRmonMulticastCntIndex"),
)
if mibBuilder.loadTexts:
    pm253MonupRmonMulticastCntEntry.setStatus("current")


class _Pm253MonupRmonMulticastCntIndex_Type(Integer32):
    """Custom type pm253MonupRmonMulticastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253MonupRmonMulticastCntIndex_Type.__name__ = "Integer32"
_Pm253MonupRmonMulticastCntIndex_Object = MibTableColumn
pm253MonupRmonMulticastCntIndex = _Pm253MonupRmonMulticastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 48, 1, 1),
    _Pm253MonupRmonMulticastCntIndex_Type()
)
pm253MonupRmonMulticastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonMulticastCntIndex.setStatus("current")
_Pm253MonupRmonMulticastCntValuePortn_Type = Counter64
_Pm253MonupRmonMulticastCntValuePortn_Object = MibTableColumn
pm253MonupRmonMulticastCntValuePortn = _Pm253MonupRmonMulticastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 48, 1, 2),
    _Pm253MonupRmonMulticastCntValuePortn_Type()
)
pm253MonupRmonMulticastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonMulticastCntValuePortn.setStatus("current")
_Pm253MonupRmonMulticastCntErrorPortn_Type = EkiOnOff
_Pm253MonupRmonMulticastCntErrorPortn_Object = MibTableColumn
pm253MonupRmonMulticastCntErrorPortn = _Pm253MonupRmonMulticastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 48, 1, 3),
    _Pm253MonupRmonMulticastCntErrorPortn_Type()
)
pm253MonupRmonMulticastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonMulticastCntErrorPortn.setStatus("current")
_Pm253MonupRmonMulticastCntOverloadPortn_Type = EkiOnOff
_Pm253MonupRmonMulticastCntOverloadPortn_Object = MibTableColumn
pm253MonupRmonMulticastCntOverloadPortn = _Pm253MonupRmonMulticastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 48, 1, 4),
    _Pm253MonupRmonMulticastCntOverloadPortn_Type()
)
pm253MonupRmonMulticastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonMulticastCntOverloadPortn.setStatus("current")
_Pm253MonupRmonTimerCntTable_Object = MibTable
pm253MonupRmonTimerCntTable = _Pm253MonupRmonTimerCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 56)
)
if mibBuilder.loadTexts:
    pm253MonupRmonTimerCntTable.setStatus("current")
_Pm253MonupRmonTimerCntEntry_Object = MibTableRow
pm253MonupRmonTimerCntEntry = _Pm253MonupRmonTimerCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 56, 1)
)
pm253MonupRmonTimerCntEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253MonupRmonTimerCntIndex"),
)
if mibBuilder.loadTexts:
    pm253MonupRmonTimerCntEntry.setStatus("current")


class _Pm253MonupRmonTimerCntIndex_Type(Integer32):
    """Custom type pm253MonupRmonTimerCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253MonupRmonTimerCntIndex_Type.__name__ = "Integer32"
_Pm253MonupRmonTimerCntIndex_Object = MibTableColumn
pm253MonupRmonTimerCntIndex = _Pm253MonupRmonTimerCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 56, 1, 1),
    _Pm253MonupRmonTimerCntIndex_Type()
)
pm253MonupRmonTimerCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonTimerCntIndex.setStatus("current")
_Pm253MonupRmonTimerCntValuePortn_Type = Counter64
_Pm253MonupRmonTimerCntValuePortn_Object = MibTableColumn
pm253MonupRmonTimerCntValuePortn = _Pm253MonupRmonTimerCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 56, 1, 2),
    _Pm253MonupRmonTimerCntValuePortn_Type()
)
pm253MonupRmonTimerCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonTimerCntValuePortn.setStatus("current")
_Pm253MonupRmonTimerCntErrorPortn_Type = EkiOnOff
_Pm253MonupRmonTimerCntErrorPortn_Object = MibTableColumn
pm253MonupRmonTimerCntErrorPortn = _Pm253MonupRmonTimerCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 56, 1, 3),
    _Pm253MonupRmonTimerCntErrorPortn_Type()
)
pm253MonupRmonTimerCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonTimerCntErrorPortn.setStatus("current")
_Pm253MonupRmonTimerCntOverloadPortn_Type = EkiOnOff
_Pm253MonupRmonTimerCntOverloadPortn_Object = MibTableColumn
pm253MonupRmonTimerCntOverloadPortn = _Pm253MonupRmonTimerCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 56, 1, 4),
    _Pm253MonupRmonTimerCntOverloadPortn_Type()
)
pm253MonupRmonTimerCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonTimerCntOverloadPortn.setStatus("current")
_Pm253MonupRmonPauseFrameCntTable_Object = MibTable
pm253MonupRmonPauseFrameCntTable = _Pm253MonupRmonPauseFrameCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 64)
)
if mibBuilder.loadTexts:
    pm253MonupRmonPauseFrameCntTable.setStatus("current")
_Pm253MonupRmonPauseFrameCntEntry_Object = MibTableRow
pm253MonupRmonPauseFrameCntEntry = _Pm253MonupRmonPauseFrameCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 64, 1)
)
pm253MonupRmonPauseFrameCntEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253MonupRmonPauseFrameCntIndex"),
)
if mibBuilder.loadTexts:
    pm253MonupRmonPauseFrameCntEntry.setStatus("current")


class _Pm253MonupRmonPauseFrameCntIndex_Type(Integer32):
    """Custom type pm253MonupRmonPauseFrameCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253MonupRmonPauseFrameCntIndex_Type.__name__ = "Integer32"
_Pm253MonupRmonPauseFrameCntIndex_Object = MibTableColumn
pm253MonupRmonPauseFrameCntIndex = _Pm253MonupRmonPauseFrameCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 64, 1, 1),
    _Pm253MonupRmonPauseFrameCntIndex_Type()
)
pm253MonupRmonPauseFrameCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonPauseFrameCntIndex.setStatus("current")
_Pm253MonupRmonPauseFrameCntValuePortn_Type = Counter64
_Pm253MonupRmonPauseFrameCntValuePortn_Object = MibTableColumn
pm253MonupRmonPauseFrameCntValuePortn = _Pm253MonupRmonPauseFrameCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 64, 1, 2),
    _Pm253MonupRmonPauseFrameCntValuePortn_Type()
)
pm253MonupRmonPauseFrameCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonPauseFrameCntValuePortn.setStatus("current")
_Pm253MonupRmonPauseFrameCntErrorPortn_Type = EkiOnOff
_Pm253MonupRmonPauseFrameCntErrorPortn_Object = MibTableColumn
pm253MonupRmonPauseFrameCntErrorPortn = _Pm253MonupRmonPauseFrameCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 64, 1, 3),
    _Pm253MonupRmonPauseFrameCntErrorPortn_Type()
)
pm253MonupRmonPauseFrameCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonPauseFrameCntErrorPortn.setStatus("current")
_Pm253MonupRmonPauseFrameCntOverloadPortn_Type = EkiOnOff
_Pm253MonupRmonPauseFrameCntOverloadPortn_Object = MibTableColumn
pm253MonupRmonPauseFrameCntOverloadPortn = _Pm253MonupRmonPauseFrameCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 64, 1, 4),
    _Pm253MonupRmonPauseFrameCntOverloadPortn_Type()
)
pm253MonupRmonPauseFrameCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonPauseFrameCntOverloadPortn.setStatus("current")
_Pm253MonupRmonDropFrameCntTable_Object = MibTable
pm253MonupRmonDropFrameCntTable = _Pm253MonupRmonDropFrameCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 72)
)
if mibBuilder.loadTexts:
    pm253MonupRmonDropFrameCntTable.setStatus("current")
_Pm253MonupRmonDropFrameCntEntry_Object = MibTableRow
pm253MonupRmonDropFrameCntEntry = _Pm253MonupRmonDropFrameCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 72, 1)
)
pm253MonupRmonDropFrameCntEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253MonupRmonDropFrameCntIndex"),
)
if mibBuilder.loadTexts:
    pm253MonupRmonDropFrameCntEntry.setStatus("current")


class _Pm253MonupRmonDropFrameCntIndex_Type(Integer32):
    """Custom type pm253MonupRmonDropFrameCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253MonupRmonDropFrameCntIndex_Type.__name__ = "Integer32"
_Pm253MonupRmonDropFrameCntIndex_Object = MibTableColumn
pm253MonupRmonDropFrameCntIndex = _Pm253MonupRmonDropFrameCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 72, 1, 1),
    _Pm253MonupRmonDropFrameCntIndex_Type()
)
pm253MonupRmonDropFrameCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonDropFrameCntIndex.setStatus("current")
_Pm253MonupRmonDropFrameCntValuePortn_Type = Counter64
_Pm253MonupRmonDropFrameCntValuePortn_Object = MibTableColumn
pm253MonupRmonDropFrameCntValuePortn = _Pm253MonupRmonDropFrameCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 72, 1, 2),
    _Pm253MonupRmonDropFrameCntValuePortn_Type()
)
pm253MonupRmonDropFrameCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonDropFrameCntValuePortn.setStatus("current")
_Pm253MonupRmonDropFrameCntErrorPortn_Type = EkiOnOff
_Pm253MonupRmonDropFrameCntErrorPortn_Object = MibTableColumn
pm253MonupRmonDropFrameCntErrorPortn = _Pm253MonupRmonDropFrameCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 72, 1, 3),
    _Pm253MonupRmonDropFrameCntErrorPortn_Type()
)
pm253MonupRmonDropFrameCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonDropFrameCntErrorPortn.setStatus("current")
_Pm253MonupRmonDropFrameCntOverloadPortn_Type = EkiOnOff
_Pm253MonupRmonDropFrameCntOverloadPortn_Object = MibTableColumn
pm253MonupRmonDropFrameCntOverloadPortn = _Pm253MonupRmonDropFrameCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 72, 1, 4),
    _Pm253MonupRmonDropFrameCntOverloadPortn_Type()
)
pm253MonupRmonDropFrameCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonDropFrameCntOverloadPortn.setStatus("current")
_Pm253MonupRmonBitsCntTable_Object = MibTable
pm253MonupRmonBitsCntTable = _Pm253MonupRmonBitsCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 80)
)
if mibBuilder.loadTexts:
    pm253MonupRmonBitsCntTable.setStatus("current")
_Pm253MonupRmonBitsCntEntry_Object = MibTableRow
pm253MonupRmonBitsCntEntry = _Pm253MonupRmonBitsCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 80, 1)
)
pm253MonupRmonBitsCntEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253MonupRmonBitsCntIndex"),
)
if mibBuilder.loadTexts:
    pm253MonupRmonBitsCntEntry.setStatus("current")


class _Pm253MonupRmonBitsCntIndex_Type(Integer32):
    """Custom type pm253MonupRmonBitsCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253MonupRmonBitsCntIndex_Type.__name__ = "Integer32"
_Pm253MonupRmonBitsCntIndex_Object = MibTableColumn
pm253MonupRmonBitsCntIndex = _Pm253MonupRmonBitsCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 80, 1, 1),
    _Pm253MonupRmonBitsCntIndex_Type()
)
pm253MonupRmonBitsCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonBitsCntIndex.setStatus("current")
_Pm253MonupRmonBitsCntValuePortn_Type = Counter64
_Pm253MonupRmonBitsCntValuePortn_Object = MibTableColumn
pm253MonupRmonBitsCntValuePortn = _Pm253MonupRmonBitsCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 80, 1, 2),
    _Pm253MonupRmonBitsCntValuePortn_Type()
)
pm253MonupRmonBitsCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonBitsCntValuePortn.setStatus("current")
_Pm253MonupRmonBitsCntErrorPortn_Type = EkiOnOff
_Pm253MonupRmonBitsCntErrorPortn_Object = MibTableColumn
pm253MonupRmonBitsCntErrorPortn = _Pm253MonupRmonBitsCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 80, 1, 3),
    _Pm253MonupRmonBitsCntErrorPortn_Type()
)
pm253MonupRmonBitsCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonBitsCntErrorPortn.setStatus("current")
_Pm253MonupRmonBitsCntOverloadPortn_Type = EkiOnOff
_Pm253MonupRmonBitsCntOverloadPortn_Object = MibTableColumn
pm253MonupRmonBitsCntOverloadPortn = _Pm253MonupRmonBitsCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 80, 1, 4),
    _Pm253MonupRmonBitsCntOverloadPortn_Type()
)
pm253MonupRmonBitsCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonBitsCntOverloadPortn.setStatus("current")
_Pm253MonupRmonUnicastCntTable_Object = MibTable
pm253MonupRmonUnicastCntTable = _Pm253MonupRmonUnicastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 88)
)
if mibBuilder.loadTexts:
    pm253MonupRmonUnicastCntTable.setStatus("current")
_Pm253MonupRmonUnicastCntEntry_Object = MibTableRow
pm253MonupRmonUnicastCntEntry = _Pm253MonupRmonUnicastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 88, 1)
)
pm253MonupRmonUnicastCntEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253MonupRmonUnicastCntIndex"),
)
if mibBuilder.loadTexts:
    pm253MonupRmonUnicastCntEntry.setStatus("current")


class _Pm253MonupRmonUnicastCntIndex_Type(Integer32):
    """Custom type pm253MonupRmonUnicastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253MonupRmonUnicastCntIndex_Type.__name__ = "Integer32"
_Pm253MonupRmonUnicastCntIndex_Object = MibTableColumn
pm253MonupRmonUnicastCntIndex = _Pm253MonupRmonUnicastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 88, 1, 1),
    _Pm253MonupRmonUnicastCntIndex_Type()
)
pm253MonupRmonUnicastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonUnicastCntIndex.setStatus("current")
_Pm253MonupRmonUnicastCntValuePortn_Type = Counter64
_Pm253MonupRmonUnicastCntValuePortn_Object = MibTableColumn
pm253MonupRmonUnicastCntValuePortn = _Pm253MonupRmonUnicastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 88, 1, 2),
    _Pm253MonupRmonUnicastCntValuePortn_Type()
)
pm253MonupRmonUnicastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonUnicastCntValuePortn.setStatus("current")
_Pm253MonupRmonUnicastCntErrorPortn_Type = EkiOnOff
_Pm253MonupRmonUnicastCntErrorPortn_Object = MibTableColumn
pm253MonupRmonUnicastCntErrorPortn = _Pm253MonupRmonUnicastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 88, 1, 3),
    _Pm253MonupRmonUnicastCntErrorPortn_Type()
)
pm253MonupRmonUnicastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonUnicastCntErrorPortn.setStatus("current")
_Pm253MonupRmonUnicastCntOverloadPortn_Type = EkiOnOff
_Pm253MonupRmonUnicastCntOverloadPortn_Object = MibTableColumn
pm253MonupRmonUnicastCntOverloadPortn = _Pm253MonupRmonUnicastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 88, 1, 4),
    _Pm253MonupRmonUnicastCntOverloadPortn_Type()
)
pm253MonupRmonUnicastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonUnicastCntOverloadPortn.setStatus("current")
_Pm253MonupRmonNonUnicastCntTable_Object = MibTable
pm253MonupRmonNonUnicastCntTable = _Pm253MonupRmonNonUnicastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 96)
)
if mibBuilder.loadTexts:
    pm253MonupRmonNonUnicastCntTable.setStatus("current")
_Pm253MonupRmonNonUnicastCntEntry_Object = MibTableRow
pm253MonupRmonNonUnicastCntEntry = _Pm253MonupRmonNonUnicastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 96, 1)
)
pm253MonupRmonNonUnicastCntEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253MonupRmonNonUnicastCntIndex"),
)
if mibBuilder.loadTexts:
    pm253MonupRmonNonUnicastCntEntry.setStatus("current")


class _Pm253MonupRmonNonUnicastCntIndex_Type(Integer32):
    """Custom type pm253MonupRmonNonUnicastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253MonupRmonNonUnicastCntIndex_Type.__name__ = "Integer32"
_Pm253MonupRmonNonUnicastCntIndex_Object = MibTableColumn
pm253MonupRmonNonUnicastCntIndex = _Pm253MonupRmonNonUnicastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 96, 1, 1),
    _Pm253MonupRmonNonUnicastCntIndex_Type()
)
pm253MonupRmonNonUnicastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonNonUnicastCntIndex.setStatus("current")
_Pm253MonupRmonNonUnicastCntValuePortn_Type = Counter64
_Pm253MonupRmonNonUnicastCntValuePortn_Object = MibTableColumn
pm253MonupRmonNonUnicastCntValuePortn = _Pm253MonupRmonNonUnicastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 96, 1, 2),
    _Pm253MonupRmonNonUnicastCntValuePortn_Type()
)
pm253MonupRmonNonUnicastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonNonUnicastCntValuePortn.setStatus("current")
_Pm253MonupRmonNonUnicastCntErrorPortn_Type = EkiOnOff
_Pm253MonupRmonNonUnicastCntErrorPortn_Object = MibTableColumn
pm253MonupRmonNonUnicastCntErrorPortn = _Pm253MonupRmonNonUnicastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 96, 1, 3),
    _Pm253MonupRmonNonUnicastCntErrorPortn_Type()
)
pm253MonupRmonNonUnicastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonNonUnicastCntErrorPortn.setStatus("current")
_Pm253MonupRmonNonUnicastCntOverloadPortn_Type = EkiOnOff
_Pm253MonupRmonNonUnicastCntOverloadPortn_Object = MibTableColumn
pm253MonupRmonNonUnicastCntOverloadPortn = _Pm253MonupRmonNonUnicastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 96, 1, 4),
    _Pm253MonupRmonNonUnicastCntOverloadPortn_Type()
)
pm253MonupRmonNonUnicastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MonupRmonNonUnicastCntOverloadPortn.setStatus("current")
_Pm253MondwRmonByteCntTable_Object = MibTable
pm253MondwRmonByteCntTable = _Pm253MondwRmonByteCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 112)
)
if mibBuilder.loadTexts:
    pm253MondwRmonByteCntTable.setStatus("current")
_Pm253MondwRmonByteCntEntry_Object = MibTableRow
pm253MondwRmonByteCntEntry = _Pm253MondwRmonByteCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 112, 1)
)
pm253MondwRmonByteCntEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253MondwRmonByteCntIndex"),
)
if mibBuilder.loadTexts:
    pm253MondwRmonByteCntEntry.setStatus("current")


class _Pm253MondwRmonByteCntIndex_Type(Integer32):
    """Custom type pm253MondwRmonByteCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253MondwRmonByteCntIndex_Type.__name__ = "Integer32"
_Pm253MondwRmonByteCntIndex_Object = MibTableColumn
pm253MondwRmonByteCntIndex = _Pm253MondwRmonByteCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 112, 1, 1),
    _Pm253MondwRmonByteCntIndex_Type()
)
pm253MondwRmonByteCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonByteCntIndex.setStatus("current")
_Pm253MondwRmonByteCntValuePortn_Type = Counter64
_Pm253MondwRmonByteCntValuePortn_Object = MibTableColumn
pm253MondwRmonByteCntValuePortn = _Pm253MondwRmonByteCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 112, 1, 2),
    _Pm253MondwRmonByteCntValuePortn_Type()
)
pm253MondwRmonByteCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonByteCntValuePortn.setStatus("current")
_Pm253MondwRmonByteCntErrorPortn_Type = EkiOnOff
_Pm253MondwRmonByteCntErrorPortn_Object = MibTableColumn
pm253MondwRmonByteCntErrorPortn = _Pm253MondwRmonByteCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 112, 1, 3),
    _Pm253MondwRmonByteCntErrorPortn_Type()
)
pm253MondwRmonByteCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonByteCntErrorPortn.setStatus("current")
_Pm253MondwRmonByteCntOverloadPortn_Type = EkiOnOff
_Pm253MondwRmonByteCntOverloadPortn_Object = MibTableColumn
pm253MondwRmonByteCntOverloadPortn = _Pm253MondwRmonByteCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 112, 1, 4),
    _Pm253MondwRmonByteCntOverloadPortn_Type()
)
pm253MondwRmonByteCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonByteCntOverloadPortn.setStatus("current")
_Pm253MondwRmonCrcErrorCntTable_Object = MibTable
pm253MondwRmonCrcErrorCntTable = _Pm253MondwRmonCrcErrorCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 120)
)
if mibBuilder.loadTexts:
    pm253MondwRmonCrcErrorCntTable.setStatus("current")
_Pm253MondwRmonCrcErrorCntEntry_Object = MibTableRow
pm253MondwRmonCrcErrorCntEntry = _Pm253MondwRmonCrcErrorCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 120, 1)
)
pm253MondwRmonCrcErrorCntEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253MondwRmonCrcErrorCntIndex"),
)
if mibBuilder.loadTexts:
    pm253MondwRmonCrcErrorCntEntry.setStatus("current")


class _Pm253MondwRmonCrcErrorCntIndex_Type(Integer32):
    """Custom type pm253MondwRmonCrcErrorCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253MondwRmonCrcErrorCntIndex_Type.__name__ = "Integer32"
_Pm253MondwRmonCrcErrorCntIndex_Object = MibTableColumn
pm253MondwRmonCrcErrorCntIndex = _Pm253MondwRmonCrcErrorCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 120, 1, 1),
    _Pm253MondwRmonCrcErrorCntIndex_Type()
)
pm253MondwRmonCrcErrorCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonCrcErrorCntIndex.setStatus("current")
_Pm253MondwRmonCrcErrorCntValuePortn_Type = Counter64
_Pm253MondwRmonCrcErrorCntValuePortn_Object = MibTableColumn
pm253MondwRmonCrcErrorCntValuePortn = _Pm253MondwRmonCrcErrorCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 120, 1, 2),
    _Pm253MondwRmonCrcErrorCntValuePortn_Type()
)
pm253MondwRmonCrcErrorCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonCrcErrorCntValuePortn.setStatus("current")
_Pm253MondwRmonCrcErrorCntErrorPortn_Type = EkiOnOff
_Pm253MondwRmonCrcErrorCntErrorPortn_Object = MibTableColumn
pm253MondwRmonCrcErrorCntErrorPortn = _Pm253MondwRmonCrcErrorCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 120, 1, 3),
    _Pm253MondwRmonCrcErrorCntErrorPortn_Type()
)
pm253MondwRmonCrcErrorCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonCrcErrorCntErrorPortn.setStatus("current")
_Pm253MondwRmonCrcErrorCntOverloadPortn_Type = EkiOnOff
_Pm253MondwRmonCrcErrorCntOverloadPortn_Object = MibTableColumn
pm253MondwRmonCrcErrorCntOverloadPortn = _Pm253MondwRmonCrcErrorCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 120, 1, 4),
    _Pm253MondwRmonCrcErrorCntOverloadPortn_Type()
)
pm253MondwRmonCrcErrorCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonCrcErrorCntOverloadPortn.setStatus("current")
_Pm253MondwRmonPacketsCntTable_Object = MibTable
pm253MondwRmonPacketsCntTable = _Pm253MondwRmonPacketsCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 128)
)
if mibBuilder.loadTexts:
    pm253MondwRmonPacketsCntTable.setStatus("current")
_Pm253MondwRmonPacketsCntEntry_Object = MibTableRow
pm253MondwRmonPacketsCntEntry = _Pm253MondwRmonPacketsCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 128, 1)
)
pm253MondwRmonPacketsCntEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253MondwRmonPacketsCntIndex"),
)
if mibBuilder.loadTexts:
    pm253MondwRmonPacketsCntEntry.setStatus("current")


class _Pm253MondwRmonPacketsCntIndex_Type(Integer32):
    """Custom type pm253MondwRmonPacketsCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253MondwRmonPacketsCntIndex_Type.__name__ = "Integer32"
_Pm253MondwRmonPacketsCntIndex_Object = MibTableColumn
pm253MondwRmonPacketsCntIndex = _Pm253MondwRmonPacketsCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 128, 1, 1),
    _Pm253MondwRmonPacketsCntIndex_Type()
)
pm253MondwRmonPacketsCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonPacketsCntIndex.setStatus("current")
_Pm253MondwRmonPacketsCntValuePortn_Type = Counter64
_Pm253MondwRmonPacketsCntValuePortn_Object = MibTableColumn
pm253MondwRmonPacketsCntValuePortn = _Pm253MondwRmonPacketsCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 128, 1, 2),
    _Pm253MondwRmonPacketsCntValuePortn_Type()
)
pm253MondwRmonPacketsCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonPacketsCntValuePortn.setStatus("current")
_Pm253MondwRmonPacketsCntErrorPortn_Type = EkiOnOff
_Pm253MondwRmonPacketsCntErrorPortn_Object = MibTableColumn
pm253MondwRmonPacketsCntErrorPortn = _Pm253MondwRmonPacketsCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 128, 1, 3),
    _Pm253MondwRmonPacketsCntErrorPortn_Type()
)
pm253MondwRmonPacketsCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonPacketsCntErrorPortn.setStatus("current")
_Pm253MondwRmonPacketsCntOverloadPortn_Type = EkiOnOff
_Pm253MondwRmonPacketsCntOverloadPortn_Object = MibTableColumn
pm253MondwRmonPacketsCntOverloadPortn = _Pm253MondwRmonPacketsCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 128, 1, 4),
    _Pm253MondwRmonPacketsCntOverloadPortn_Type()
)
pm253MondwRmonPacketsCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonPacketsCntOverloadPortn.setStatus("current")
_Pm253MondwRmonBroadcastCntTable_Object = MibTable
pm253MondwRmonBroadcastCntTable = _Pm253MondwRmonBroadcastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 136)
)
if mibBuilder.loadTexts:
    pm253MondwRmonBroadcastCntTable.setStatus("current")
_Pm253MondwRmonBroadcastCntEntry_Object = MibTableRow
pm253MondwRmonBroadcastCntEntry = _Pm253MondwRmonBroadcastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 136, 1)
)
pm253MondwRmonBroadcastCntEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253MondwRmonBroadcastCntIndex"),
)
if mibBuilder.loadTexts:
    pm253MondwRmonBroadcastCntEntry.setStatus("current")


class _Pm253MondwRmonBroadcastCntIndex_Type(Integer32):
    """Custom type pm253MondwRmonBroadcastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253MondwRmonBroadcastCntIndex_Type.__name__ = "Integer32"
_Pm253MondwRmonBroadcastCntIndex_Object = MibTableColumn
pm253MondwRmonBroadcastCntIndex = _Pm253MondwRmonBroadcastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 136, 1, 1),
    _Pm253MondwRmonBroadcastCntIndex_Type()
)
pm253MondwRmonBroadcastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonBroadcastCntIndex.setStatus("current")
_Pm253MondwRmonBroadcastCntValuePortn_Type = Counter64
_Pm253MondwRmonBroadcastCntValuePortn_Object = MibTableColumn
pm253MondwRmonBroadcastCntValuePortn = _Pm253MondwRmonBroadcastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 136, 1, 2),
    _Pm253MondwRmonBroadcastCntValuePortn_Type()
)
pm253MondwRmonBroadcastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonBroadcastCntValuePortn.setStatus("current")
_Pm253MondwRmonBroadcastCntErrorPortn_Type = EkiOnOff
_Pm253MondwRmonBroadcastCntErrorPortn_Object = MibTableColumn
pm253MondwRmonBroadcastCntErrorPortn = _Pm253MondwRmonBroadcastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 136, 1, 3),
    _Pm253MondwRmonBroadcastCntErrorPortn_Type()
)
pm253MondwRmonBroadcastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonBroadcastCntErrorPortn.setStatus("current")
_Pm253MondwRmonBroadcastCntOverloadPortn_Type = EkiOnOff
_Pm253MondwRmonBroadcastCntOverloadPortn_Object = MibTableColumn
pm253MondwRmonBroadcastCntOverloadPortn = _Pm253MondwRmonBroadcastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 136, 1, 4),
    _Pm253MondwRmonBroadcastCntOverloadPortn_Type()
)
pm253MondwRmonBroadcastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonBroadcastCntOverloadPortn.setStatus("current")
_Pm253MondwRmonMulticastCntTable_Object = MibTable
pm253MondwRmonMulticastCntTable = _Pm253MondwRmonMulticastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 144)
)
if mibBuilder.loadTexts:
    pm253MondwRmonMulticastCntTable.setStatus("current")
_Pm253MondwRmonMulticastCntEntry_Object = MibTableRow
pm253MondwRmonMulticastCntEntry = _Pm253MondwRmonMulticastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 144, 1)
)
pm253MondwRmonMulticastCntEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253MondwRmonMulticastCntIndex"),
)
if mibBuilder.loadTexts:
    pm253MondwRmonMulticastCntEntry.setStatus("current")


class _Pm253MondwRmonMulticastCntIndex_Type(Integer32):
    """Custom type pm253MondwRmonMulticastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253MondwRmonMulticastCntIndex_Type.__name__ = "Integer32"
_Pm253MondwRmonMulticastCntIndex_Object = MibTableColumn
pm253MondwRmonMulticastCntIndex = _Pm253MondwRmonMulticastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 144, 1, 1),
    _Pm253MondwRmonMulticastCntIndex_Type()
)
pm253MondwRmonMulticastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonMulticastCntIndex.setStatus("current")
_Pm253MondwRmonMulticastCntValuePortn_Type = Counter64
_Pm253MondwRmonMulticastCntValuePortn_Object = MibTableColumn
pm253MondwRmonMulticastCntValuePortn = _Pm253MondwRmonMulticastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 144, 1, 2),
    _Pm253MondwRmonMulticastCntValuePortn_Type()
)
pm253MondwRmonMulticastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonMulticastCntValuePortn.setStatus("current")
_Pm253MondwRmonMulticastCntErrorPortn_Type = EkiOnOff
_Pm253MondwRmonMulticastCntErrorPortn_Object = MibTableColumn
pm253MondwRmonMulticastCntErrorPortn = _Pm253MondwRmonMulticastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 144, 1, 3),
    _Pm253MondwRmonMulticastCntErrorPortn_Type()
)
pm253MondwRmonMulticastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonMulticastCntErrorPortn.setStatus("current")
_Pm253MondwRmonMulticastCntOverloadPortn_Type = EkiOnOff
_Pm253MondwRmonMulticastCntOverloadPortn_Object = MibTableColumn
pm253MondwRmonMulticastCntOverloadPortn = _Pm253MondwRmonMulticastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 144, 1, 4),
    _Pm253MondwRmonMulticastCntOverloadPortn_Type()
)
pm253MondwRmonMulticastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonMulticastCntOverloadPortn.setStatus("current")
_Pm253MondwRmonPauseFrameCntTable_Object = MibTable
pm253MondwRmonPauseFrameCntTable = _Pm253MondwRmonPauseFrameCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 152)
)
if mibBuilder.loadTexts:
    pm253MondwRmonPauseFrameCntTable.setStatus("current")
_Pm253MondwRmonPauseFrameCntEntry_Object = MibTableRow
pm253MondwRmonPauseFrameCntEntry = _Pm253MondwRmonPauseFrameCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 152, 1)
)
pm253MondwRmonPauseFrameCntEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253MondwRmonPauseFrameCntIndex"),
)
if mibBuilder.loadTexts:
    pm253MondwRmonPauseFrameCntEntry.setStatus("current")


class _Pm253MondwRmonPauseFrameCntIndex_Type(Integer32):
    """Custom type pm253MondwRmonPauseFrameCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253MondwRmonPauseFrameCntIndex_Type.__name__ = "Integer32"
_Pm253MondwRmonPauseFrameCntIndex_Object = MibTableColumn
pm253MondwRmonPauseFrameCntIndex = _Pm253MondwRmonPauseFrameCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 152, 1, 1),
    _Pm253MondwRmonPauseFrameCntIndex_Type()
)
pm253MondwRmonPauseFrameCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonPauseFrameCntIndex.setStatus("current")
_Pm253MondwRmonPauseFrameCntValuePortn_Type = Counter64
_Pm253MondwRmonPauseFrameCntValuePortn_Object = MibTableColumn
pm253MondwRmonPauseFrameCntValuePortn = _Pm253MondwRmonPauseFrameCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 152, 1, 2),
    _Pm253MondwRmonPauseFrameCntValuePortn_Type()
)
pm253MondwRmonPauseFrameCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonPauseFrameCntValuePortn.setStatus("current")
_Pm253MondwRmonPauseFrameCntErrorPortn_Type = EkiOnOff
_Pm253MondwRmonPauseFrameCntErrorPortn_Object = MibTableColumn
pm253MondwRmonPauseFrameCntErrorPortn = _Pm253MondwRmonPauseFrameCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 152, 1, 3),
    _Pm253MondwRmonPauseFrameCntErrorPortn_Type()
)
pm253MondwRmonPauseFrameCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonPauseFrameCntErrorPortn.setStatus("current")
_Pm253MondwRmonPauseFrameCntOverloadPortn_Type = EkiOnOff
_Pm253MondwRmonPauseFrameCntOverloadPortn_Object = MibTableColumn
pm253MondwRmonPauseFrameCntOverloadPortn = _Pm253MondwRmonPauseFrameCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 152, 1, 4),
    _Pm253MondwRmonPauseFrameCntOverloadPortn_Type()
)
pm253MondwRmonPauseFrameCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonPauseFrameCntOverloadPortn.setStatus("current")
_Pm253MondwRmonTimerCntTable_Object = MibTable
pm253MondwRmonTimerCntTable = _Pm253MondwRmonTimerCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 160)
)
if mibBuilder.loadTexts:
    pm253MondwRmonTimerCntTable.setStatus("current")
_Pm253MondwRmonTimerCntEntry_Object = MibTableRow
pm253MondwRmonTimerCntEntry = _Pm253MondwRmonTimerCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 160, 1)
)
pm253MondwRmonTimerCntEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253MondwRmonTimerCntIndex"),
)
if mibBuilder.loadTexts:
    pm253MondwRmonTimerCntEntry.setStatus("current")


class _Pm253MondwRmonTimerCntIndex_Type(Integer32):
    """Custom type pm253MondwRmonTimerCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253MondwRmonTimerCntIndex_Type.__name__ = "Integer32"
_Pm253MondwRmonTimerCntIndex_Object = MibTableColumn
pm253MondwRmonTimerCntIndex = _Pm253MondwRmonTimerCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 160, 1, 1),
    _Pm253MondwRmonTimerCntIndex_Type()
)
pm253MondwRmonTimerCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonTimerCntIndex.setStatus("current")
_Pm253MondwRmonTimerCntValuePortn_Type = Counter64
_Pm253MondwRmonTimerCntValuePortn_Object = MibTableColumn
pm253MondwRmonTimerCntValuePortn = _Pm253MondwRmonTimerCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 160, 1, 2),
    _Pm253MondwRmonTimerCntValuePortn_Type()
)
pm253MondwRmonTimerCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonTimerCntValuePortn.setStatus("current")
_Pm253MondwRmonTimerCntErrorPortn_Type = EkiOnOff
_Pm253MondwRmonTimerCntErrorPortn_Object = MibTableColumn
pm253MondwRmonTimerCntErrorPortn = _Pm253MondwRmonTimerCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 160, 1, 3),
    _Pm253MondwRmonTimerCntErrorPortn_Type()
)
pm253MondwRmonTimerCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonTimerCntErrorPortn.setStatus("current")
_Pm253MondwRmonTimerCntOverloadPortn_Type = EkiOnOff
_Pm253MondwRmonTimerCntOverloadPortn_Object = MibTableColumn
pm253MondwRmonTimerCntOverloadPortn = _Pm253MondwRmonTimerCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 160, 1, 4),
    _Pm253MondwRmonTimerCntOverloadPortn_Type()
)
pm253MondwRmonTimerCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonTimerCntOverloadPortn.setStatus("current")
_Pm253MondwRmonBitsCntTable_Object = MibTable
pm253MondwRmonBitsCntTable = _Pm253MondwRmonBitsCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 168)
)
if mibBuilder.loadTexts:
    pm253MondwRmonBitsCntTable.setStatus("current")
_Pm253MondwRmonBitsCntEntry_Object = MibTableRow
pm253MondwRmonBitsCntEntry = _Pm253MondwRmonBitsCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 168, 1)
)
pm253MondwRmonBitsCntEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253MondwRmonBitsCntIndex"),
)
if mibBuilder.loadTexts:
    pm253MondwRmonBitsCntEntry.setStatus("current")


class _Pm253MondwRmonBitsCntIndex_Type(Integer32):
    """Custom type pm253MondwRmonBitsCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253MondwRmonBitsCntIndex_Type.__name__ = "Integer32"
_Pm253MondwRmonBitsCntIndex_Object = MibTableColumn
pm253MondwRmonBitsCntIndex = _Pm253MondwRmonBitsCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 168, 1, 1),
    _Pm253MondwRmonBitsCntIndex_Type()
)
pm253MondwRmonBitsCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonBitsCntIndex.setStatus("current")
_Pm253MondwRmonBitsCntValuePortn_Type = Counter64
_Pm253MondwRmonBitsCntValuePortn_Object = MibTableColumn
pm253MondwRmonBitsCntValuePortn = _Pm253MondwRmonBitsCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 168, 1, 2),
    _Pm253MondwRmonBitsCntValuePortn_Type()
)
pm253MondwRmonBitsCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonBitsCntValuePortn.setStatus("current")
_Pm253MondwRmonBitsCntErrorPortn_Type = EkiOnOff
_Pm253MondwRmonBitsCntErrorPortn_Object = MibTableColumn
pm253MondwRmonBitsCntErrorPortn = _Pm253MondwRmonBitsCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 168, 1, 3),
    _Pm253MondwRmonBitsCntErrorPortn_Type()
)
pm253MondwRmonBitsCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonBitsCntErrorPortn.setStatus("current")
_Pm253MondwRmonBitsCntOverloadPortn_Type = EkiOnOff
_Pm253MondwRmonBitsCntOverloadPortn_Object = MibTableColumn
pm253MondwRmonBitsCntOverloadPortn = _Pm253MondwRmonBitsCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 168, 1, 4),
    _Pm253MondwRmonBitsCntOverloadPortn_Type()
)
pm253MondwRmonBitsCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonBitsCntOverloadPortn.setStatus("current")
_Pm253MondwRmonUnicastCntTable_Object = MibTable
pm253MondwRmonUnicastCntTable = _Pm253MondwRmonUnicastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 176)
)
if mibBuilder.loadTexts:
    pm253MondwRmonUnicastCntTable.setStatus("current")
_Pm253MondwRmonUnicastCntEntry_Object = MibTableRow
pm253MondwRmonUnicastCntEntry = _Pm253MondwRmonUnicastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 176, 1)
)
pm253MondwRmonUnicastCntEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253MondwRmonUnicastCntIndex"),
)
if mibBuilder.loadTexts:
    pm253MondwRmonUnicastCntEntry.setStatus("current")


class _Pm253MondwRmonUnicastCntIndex_Type(Integer32):
    """Custom type pm253MondwRmonUnicastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253MondwRmonUnicastCntIndex_Type.__name__ = "Integer32"
_Pm253MondwRmonUnicastCntIndex_Object = MibTableColumn
pm253MondwRmonUnicastCntIndex = _Pm253MondwRmonUnicastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 176, 1, 1),
    _Pm253MondwRmonUnicastCntIndex_Type()
)
pm253MondwRmonUnicastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonUnicastCntIndex.setStatus("current")
_Pm253MondwRmonUnicastCntValuePortn_Type = Counter64
_Pm253MondwRmonUnicastCntValuePortn_Object = MibTableColumn
pm253MondwRmonUnicastCntValuePortn = _Pm253MondwRmonUnicastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 176, 1, 2),
    _Pm253MondwRmonUnicastCntValuePortn_Type()
)
pm253MondwRmonUnicastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonUnicastCntValuePortn.setStatus("current")
_Pm253MondwRmonUnicastCntErrorPortn_Type = EkiOnOff
_Pm253MondwRmonUnicastCntErrorPortn_Object = MibTableColumn
pm253MondwRmonUnicastCntErrorPortn = _Pm253MondwRmonUnicastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 176, 1, 3),
    _Pm253MondwRmonUnicastCntErrorPortn_Type()
)
pm253MondwRmonUnicastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonUnicastCntErrorPortn.setStatus("current")
_Pm253MondwRmonUnicastCntOverloadPortn_Type = EkiOnOff
_Pm253MondwRmonUnicastCntOverloadPortn_Object = MibTableColumn
pm253MondwRmonUnicastCntOverloadPortn = _Pm253MondwRmonUnicastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 176, 1, 4),
    _Pm253MondwRmonUnicastCntOverloadPortn_Type()
)
pm253MondwRmonUnicastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonUnicastCntOverloadPortn.setStatus("current")
_Pm253MondwRmonNonUnicastCntTable_Object = MibTable
pm253MondwRmonNonUnicastCntTable = _Pm253MondwRmonNonUnicastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 184)
)
if mibBuilder.loadTexts:
    pm253MondwRmonNonUnicastCntTable.setStatus("current")
_Pm253MondwRmonNonUnicastCntEntry_Object = MibTableRow
pm253MondwRmonNonUnicastCntEntry = _Pm253MondwRmonNonUnicastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 184, 1)
)
pm253MondwRmonNonUnicastCntEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253MondwRmonNonUnicastCntIndex"),
)
if mibBuilder.loadTexts:
    pm253MondwRmonNonUnicastCntEntry.setStatus("current")


class _Pm253MondwRmonNonUnicastCntIndex_Type(Integer32):
    """Custom type pm253MondwRmonNonUnicastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253MondwRmonNonUnicastCntIndex_Type.__name__ = "Integer32"
_Pm253MondwRmonNonUnicastCntIndex_Object = MibTableColumn
pm253MondwRmonNonUnicastCntIndex = _Pm253MondwRmonNonUnicastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 184, 1, 1),
    _Pm253MondwRmonNonUnicastCntIndex_Type()
)
pm253MondwRmonNonUnicastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonNonUnicastCntIndex.setStatus("current")
_Pm253MondwRmonNonUnicastCntValuePortn_Type = Counter64
_Pm253MondwRmonNonUnicastCntValuePortn_Object = MibTableColumn
pm253MondwRmonNonUnicastCntValuePortn = _Pm253MondwRmonNonUnicastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 184, 1, 2),
    _Pm253MondwRmonNonUnicastCntValuePortn_Type()
)
pm253MondwRmonNonUnicastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonNonUnicastCntValuePortn.setStatus("current")
_Pm253MondwRmonNonUnicastCntErrorPortn_Type = EkiOnOff
_Pm253MondwRmonNonUnicastCntErrorPortn_Object = MibTableColumn
pm253MondwRmonNonUnicastCntErrorPortn = _Pm253MondwRmonNonUnicastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 184, 1, 3),
    _Pm253MondwRmonNonUnicastCntErrorPortn_Type()
)
pm253MondwRmonNonUnicastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonNonUnicastCntErrorPortn.setStatus("current")
_Pm253MondwRmonNonUnicastCntOverloadPortn_Type = EkiOnOff
_Pm253MondwRmonNonUnicastCntOverloadPortn_Object = MibTableColumn
pm253MondwRmonNonUnicastCntOverloadPortn = _Pm253MondwRmonNonUnicastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 4, 184, 1, 4),
    _Pm253MondwRmonNonUnicastCntOverloadPortn_Type()
)
pm253MondwRmonNonUnicastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253MondwRmonNonUnicastCntOverloadPortn.setStatus("current")
_Pm253PerfTelecomClientCurrent15StatTable_Object = MibTable
pm253PerfTelecomClientCurrent15StatTable = _Pm253PerfTelecomClientCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 16)
)
if mibBuilder.loadTexts:
    pm253PerfTelecomClientCurrent15StatTable.setStatus("current")
_Pm253PerfTelecomClientCurrent15StatEntry_Object = MibTableRow
pm253PerfTelecomClientCurrent15StatEntry = _Pm253PerfTelecomClientCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 16, 1)
)
pm253PerfTelecomClientCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253PerfTelecomClientCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pm253PerfTelecomClientCurrent15StatEntry.setStatus("current")


class _Pm253PerfTelecomClientCurrent15StatIndex_Type(Integer32):
    """Custom type pm253PerfTelecomClientCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253PerfTelecomClientCurrent15StatIndex_Type.__name__ = "Integer32"
_Pm253PerfTelecomClientCurrent15StatIndex_Object = MibTableColumn
pm253PerfTelecomClientCurrent15StatIndex = _Pm253PerfTelecomClientCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 16, 1, 1),
    _Pm253PerfTelecomClientCurrent15StatIndex_Type()
)
pm253PerfTelecomClientCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientCurrent15StatIndex.setStatus("current")
_Pm253PerfTelecomClientCurrent15StatInvCvPortn_Type = EkiOnOff
_Pm253PerfTelecomClientCurrent15StatInvCvPortn_Object = MibTableColumn
pm253PerfTelecomClientCurrent15StatInvCvPortn = _Pm253PerfTelecomClientCurrent15StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 16, 1, 2),
    _Pm253PerfTelecomClientCurrent15StatInvCvPortn_Type()
)
pm253PerfTelecomClientCurrent15StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientCurrent15StatInvCvPortn.setStatus("current")
_Pm253PerfTelecomClientCurrent15StatCvValuePortn_Type = Unsigned32
_Pm253PerfTelecomClientCurrent15StatCvValuePortn_Object = MibTableColumn
pm253PerfTelecomClientCurrent15StatCvValuePortn = _Pm253PerfTelecomClientCurrent15StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 16, 1, 3),
    _Pm253PerfTelecomClientCurrent15StatCvValuePortn_Type()
)
pm253PerfTelecomClientCurrent15StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientCurrent15StatCvValuePortn.setStatus("current")
_Pm253PerfTelecomClientCurrent15StatInvEsPortn_Type = EkiOnOff
_Pm253PerfTelecomClientCurrent15StatInvEsPortn_Object = MibTableColumn
pm253PerfTelecomClientCurrent15StatInvEsPortn = _Pm253PerfTelecomClientCurrent15StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 16, 1, 4),
    _Pm253PerfTelecomClientCurrent15StatInvEsPortn_Type()
)
pm253PerfTelecomClientCurrent15StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientCurrent15StatInvEsPortn.setStatus("current")
_Pm253PerfTelecomClientCurrent15StatEsValuePortn_Type = Unsigned32
_Pm253PerfTelecomClientCurrent15StatEsValuePortn_Object = MibTableColumn
pm253PerfTelecomClientCurrent15StatEsValuePortn = _Pm253PerfTelecomClientCurrent15StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 16, 1, 5),
    _Pm253PerfTelecomClientCurrent15StatEsValuePortn_Type()
)
pm253PerfTelecomClientCurrent15StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientCurrent15StatEsValuePortn.setStatus("current")
_Pm253PerfTelecomClientCurrent15StatInvSesPortn_Type = EkiOnOff
_Pm253PerfTelecomClientCurrent15StatInvSesPortn_Object = MibTableColumn
pm253PerfTelecomClientCurrent15StatInvSesPortn = _Pm253PerfTelecomClientCurrent15StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 16, 1, 6),
    _Pm253PerfTelecomClientCurrent15StatInvSesPortn_Type()
)
pm253PerfTelecomClientCurrent15StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientCurrent15StatInvSesPortn.setStatus("current")
_Pm253PerfTelecomClientCurrent15StatSesValuePortn_Type = Unsigned32
_Pm253PerfTelecomClientCurrent15StatSesValuePortn_Object = MibTableColumn
pm253PerfTelecomClientCurrent15StatSesValuePortn = _Pm253PerfTelecomClientCurrent15StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 16, 1, 7),
    _Pm253PerfTelecomClientCurrent15StatSesValuePortn_Type()
)
pm253PerfTelecomClientCurrent15StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientCurrent15StatSesValuePortn.setStatus("current")
_Pm253PerfTelecomClientCurrent15StatInvSefsPortn_Type = EkiOnOff
_Pm253PerfTelecomClientCurrent15StatInvSefsPortn_Object = MibTableColumn
pm253PerfTelecomClientCurrent15StatInvSefsPortn = _Pm253PerfTelecomClientCurrent15StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 16, 1, 8),
    _Pm253PerfTelecomClientCurrent15StatInvSefsPortn_Type()
)
pm253PerfTelecomClientCurrent15StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientCurrent15StatInvSefsPortn.setStatus("current")
_Pm253PerfTelecomClientCurrent15StatSefsValuePortn_Type = Unsigned32
_Pm253PerfTelecomClientCurrent15StatSefsValuePortn_Object = MibTableColumn
pm253PerfTelecomClientCurrent15StatSefsValuePortn = _Pm253PerfTelecomClientCurrent15StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 16, 1, 9),
    _Pm253PerfTelecomClientCurrent15StatSefsValuePortn_Type()
)
pm253PerfTelecomClientCurrent15StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientCurrent15StatSefsValuePortn.setStatus("current")
_Pm253PerfTelecomClientCurrent15StatInvUasPortn_Type = EkiOnOff
_Pm253PerfTelecomClientCurrent15StatInvUasPortn_Object = MibTableColumn
pm253PerfTelecomClientCurrent15StatInvUasPortn = _Pm253PerfTelecomClientCurrent15StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 16, 1, 10),
    _Pm253PerfTelecomClientCurrent15StatInvUasPortn_Type()
)
pm253PerfTelecomClientCurrent15StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientCurrent15StatInvUasPortn.setStatus("current")
_Pm253PerfTelecomClientCurrent15StatUasValuePortn_Type = Unsigned32
_Pm253PerfTelecomClientCurrent15StatUasValuePortn_Object = MibTableColumn
pm253PerfTelecomClientCurrent15StatUasValuePortn = _Pm253PerfTelecomClientCurrent15StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 16, 1, 11),
    _Pm253PerfTelecomClientCurrent15StatUasValuePortn_Type()
)
pm253PerfTelecomClientCurrent15StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientCurrent15StatUasValuePortn.setStatus("current")
_Pm253PerfTelecomClientPast15StatHistoryPort1Table_Object = MibTable
pm253PerfTelecomClientPast15StatHistoryPort1Table = _Pm253PerfTelecomClientPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 24)
)
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast15StatHistoryPort1Table.setStatus("current")
_Pm253PerfTelecomClientPast15StatHistoryPort1Entry_Object = MibTableRow
pm253PerfTelecomClientPast15StatHistoryPort1Entry = _Pm253PerfTelecomClientPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 24, 1)
)
pm253PerfTelecomClientPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253PerfTelecomClientPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast15StatHistoryPort1Entry.setStatus("current")


class _Pm253PerfTelecomClientPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pm253PerfTelecomClientPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253PerfTelecomClientPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm253PerfTelecomClientPast15StatHistoryPort1Index_Object = MibTableColumn
pm253PerfTelecomClientPast15StatHistoryPort1Index = _Pm253PerfTelecomClientPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 24, 1, 1),
    _Pm253PerfTelecomClientPast15StatHistoryPort1Index_Type()
)
pm253PerfTelecomClientPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast15StatHistoryPort1Index.setStatus("current")
_Pm253PerfTelecomClientPast15StatHistoryInvCvPort1_Type = EkiOnOff
_Pm253PerfTelecomClientPast15StatHistoryInvCvPort1_Object = MibTableColumn
pm253PerfTelecomClientPast15StatHistoryInvCvPort1 = _Pm253PerfTelecomClientPast15StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 24, 1, 2),
    _Pm253PerfTelecomClientPast15StatHistoryInvCvPort1_Type()
)
pm253PerfTelecomClientPast15StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast15StatHistoryInvCvPort1.setStatus("current")
_Pm253PerfTelecomClientPast15StatHistoryCvValuePort1_Type = Unsigned32
_Pm253PerfTelecomClientPast15StatHistoryCvValuePort1_Object = MibTableColumn
pm253PerfTelecomClientPast15StatHistoryCvValuePort1 = _Pm253PerfTelecomClientPast15StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 24, 1, 3),
    _Pm253PerfTelecomClientPast15StatHistoryCvValuePort1_Type()
)
pm253PerfTelecomClientPast15StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast15StatHistoryCvValuePort1.setStatus("current")
_Pm253PerfTelecomClientPast15StatHistoryInvEsPort1_Type = EkiOnOff
_Pm253PerfTelecomClientPast15StatHistoryInvEsPort1_Object = MibTableColumn
pm253PerfTelecomClientPast15StatHistoryInvEsPort1 = _Pm253PerfTelecomClientPast15StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 24, 1, 4),
    _Pm253PerfTelecomClientPast15StatHistoryInvEsPort1_Type()
)
pm253PerfTelecomClientPast15StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast15StatHistoryInvEsPort1.setStatus("current")
_Pm253PerfTelecomClientPast15StatHistoryEsValuePort1_Type = Unsigned32
_Pm253PerfTelecomClientPast15StatHistoryEsValuePort1_Object = MibTableColumn
pm253PerfTelecomClientPast15StatHistoryEsValuePort1 = _Pm253PerfTelecomClientPast15StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 24, 1, 5),
    _Pm253PerfTelecomClientPast15StatHistoryEsValuePort1_Type()
)
pm253PerfTelecomClientPast15StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast15StatHistoryEsValuePort1.setStatus("current")
_Pm253PerfTelecomClientPast15StatHistoryInvSesPort1_Type = EkiOnOff
_Pm253PerfTelecomClientPast15StatHistoryInvSesPort1_Object = MibTableColumn
pm253PerfTelecomClientPast15StatHistoryInvSesPort1 = _Pm253PerfTelecomClientPast15StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 24, 1, 6),
    _Pm253PerfTelecomClientPast15StatHistoryInvSesPort1_Type()
)
pm253PerfTelecomClientPast15StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast15StatHistoryInvSesPort1.setStatus("current")
_Pm253PerfTelecomClientPast15StatHistorySesValuePort1_Type = Unsigned32
_Pm253PerfTelecomClientPast15StatHistorySesValuePort1_Object = MibTableColumn
pm253PerfTelecomClientPast15StatHistorySesValuePort1 = _Pm253PerfTelecomClientPast15StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 24, 1, 7),
    _Pm253PerfTelecomClientPast15StatHistorySesValuePort1_Type()
)
pm253PerfTelecomClientPast15StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast15StatHistorySesValuePort1.setStatus("current")
_Pm253PerfTelecomClientPast15StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm253PerfTelecomClientPast15StatHistoryInvSefsPort1_Object = MibTableColumn
pm253PerfTelecomClientPast15StatHistoryInvSefsPort1 = _Pm253PerfTelecomClientPast15StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 24, 1, 8),
    _Pm253PerfTelecomClientPast15StatHistoryInvSefsPort1_Type()
)
pm253PerfTelecomClientPast15StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast15StatHistoryInvSefsPort1.setStatus("current")
_Pm253PerfTelecomClientPast15StatHistorySefsValuePort1_Type = Unsigned32
_Pm253PerfTelecomClientPast15StatHistorySefsValuePort1_Object = MibTableColumn
pm253PerfTelecomClientPast15StatHistorySefsValuePort1 = _Pm253PerfTelecomClientPast15StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 24, 1, 9),
    _Pm253PerfTelecomClientPast15StatHistorySefsValuePort1_Type()
)
pm253PerfTelecomClientPast15StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast15StatHistorySefsValuePort1.setStatus("current")
_Pm253PerfTelecomClientPast15StatHistoryInvUasPort1_Type = EkiOnOff
_Pm253PerfTelecomClientPast15StatHistoryInvUasPort1_Object = MibTableColumn
pm253PerfTelecomClientPast15StatHistoryInvUasPort1 = _Pm253PerfTelecomClientPast15StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 24, 1, 10),
    _Pm253PerfTelecomClientPast15StatHistoryInvUasPort1_Type()
)
pm253PerfTelecomClientPast15StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast15StatHistoryInvUasPort1.setStatus("current")
_Pm253PerfTelecomClientPast15StatHistoryUasValuePort1_Type = Unsigned32
_Pm253PerfTelecomClientPast15StatHistoryUasValuePort1_Object = MibTableColumn
pm253PerfTelecomClientPast15StatHistoryUasValuePort1 = _Pm253PerfTelecomClientPast15StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 24, 1, 11),
    _Pm253PerfTelecomClientPast15StatHistoryUasValuePort1_Type()
)
pm253PerfTelecomClientPast15StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast15StatHistoryUasValuePort1.setStatus("current")
_Pm253PerfTelecomClientPast15StatHistoryPort2Table_Object = MibTable
pm253PerfTelecomClientPast15StatHistoryPort2Table = _Pm253PerfTelecomClientPast15StatHistoryPort2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 25)
)
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast15StatHistoryPort2Table.setStatus("current")
_Pm253PerfTelecomClientPast15StatHistoryPort2Entry_Object = MibTableRow
pm253PerfTelecomClientPast15StatHistoryPort2Entry = _Pm253PerfTelecomClientPast15StatHistoryPort2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 25, 1)
)
pm253PerfTelecomClientPast15StatHistoryPort2Entry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253PerfTelecomClientPast15StatHistoryPort2Index"),
)
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast15StatHistoryPort2Entry.setStatus("current")


class _Pm253PerfTelecomClientPast15StatHistoryPort2Index_Type(Integer32):
    """Custom type pm253PerfTelecomClientPast15StatHistoryPort2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253PerfTelecomClientPast15StatHistoryPort2Index_Type.__name__ = "Integer32"
_Pm253PerfTelecomClientPast15StatHistoryPort2Index_Object = MibTableColumn
pm253PerfTelecomClientPast15StatHistoryPort2Index = _Pm253PerfTelecomClientPast15StatHistoryPort2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 25, 1, 1),
    _Pm253PerfTelecomClientPast15StatHistoryPort2Index_Type()
)
pm253PerfTelecomClientPast15StatHistoryPort2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast15StatHistoryPort2Index.setStatus("current")
_Pm253PerfTelecomClientPast15StatHistoryInvCvPort2_Type = EkiOnOff
_Pm253PerfTelecomClientPast15StatHistoryInvCvPort2_Object = MibTableColumn
pm253PerfTelecomClientPast15StatHistoryInvCvPort2 = _Pm253PerfTelecomClientPast15StatHistoryInvCvPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 25, 1, 2),
    _Pm253PerfTelecomClientPast15StatHistoryInvCvPort2_Type()
)
pm253PerfTelecomClientPast15StatHistoryInvCvPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast15StatHistoryInvCvPort2.setStatus("current")
_Pm253PerfTelecomClientPast15StatHistoryCvValuePort2_Type = Unsigned32
_Pm253PerfTelecomClientPast15StatHistoryCvValuePort2_Object = MibTableColumn
pm253PerfTelecomClientPast15StatHistoryCvValuePort2 = _Pm253PerfTelecomClientPast15StatHistoryCvValuePort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 25, 1, 3),
    _Pm253PerfTelecomClientPast15StatHistoryCvValuePort2_Type()
)
pm253PerfTelecomClientPast15StatHistoryCvValuePort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast15StatHistoryCvValuePort2.setStatus("current")
_Pm253PerfTelecomClientPast15StatHistoryInvEsPort2_Type = EkiOnOff
_Pm253PerfTelecomClientPast15StatHistoryInvEsPort2_Object = MibTableColumn
pm253PerfTelecomClientPast15StatHistoryInvEsPort2 = _Pm253PerfTelecomClientPast15StatHistoryInvEsPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 25, 1, 4),
    _Pm253PerfTelecomClientPast15StatHistoryInvEsPort2_Type()
)
pm253PerfTelecomClientPast15StatHistoryInvEsPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast15StatHistoryInvEsPort2.setStatus("current")
_Pm253PerfTelecomClientPast15StatHistoryEsValuePort2_Type = Unsigned32
_Pm253PerfTelecomClientPast15StatHistoryEsValuePort2_Object = MibTableColumn
pm253PerfTelecomClientPast15StatHistoryEsValuePort2 = _Pm253PerfTelecomClientPast15StatHistoryEsValuePort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 25, 1, 5),
    _Pm253PerfTelecomClientPast15StatHistoryEsValuePort2_Type()
)
pm253PerfTelecomClientPast15StatHistoryEsValuePort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast15StatHistoryEsValuePort2.setStatus("current")
_Pm253PerfTelecomClientPast15StatHistoryInvSesPort2_Type = EkiOnOff
_Pm253PerfTelecomClientPast15StatHistoryInvSesPort2_Object = MibTableColumn
pm253PerfTelecomClientPast15StatHistoryInvSesPort2 = _Pm253PerfTelecomClientPast15StatHistoryInvSesPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 25, 1, 6),
    _Pm253PerfTelecomClientPast15StatHistoryInvSesPort2_Type()
)
pm253PerfTelecomClientPast15StatHistoryInvSesPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast15StatHistoryInvSesPort2.setStatus("current")
_Pm253PerfTelecomClientPast15StatHistorySesValuePort2_Type = Unsigned32
_Pm253PerfTelecomClientPast15StatHistorySesValuePort2_Object = MibTableColumn
pm253PerfTelecomClientPast15StatHistorySesValuePort2 = _Pm253PerfTelecomClientPast15StatHistorySesValuePort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 25, 1, 7),
    _Pm253PerfTelecomClientPast15StatHistorySesValuePort2_Type()
)
pm253PerfTelecomClientPast15StatHistorySesValuePort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast15StatHistorySesValuePort2.setStatus("current")
_Pm253PerfTelecomClientPast15StatHistoryInvSefsPort2_Type = EkiOnOff
_Pm253PerfTelecomClientPast15StatHistoryInvSefsPort2_Object = MibTableColumn
pm253PerfTelecomClientPast15StatHistoryInvSefsPort2 = _Pm253PerfTelecomClientPast15StatHistoryInvSefsPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 25, 1, 8),
    _Pm253PerfTelecomClientPast15StatHistoryInvSefsPort2_Type()
)
pm253PerfTelecomClientPast15StatHistoryInvSefsPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast15StatHistoryInvSefsPort2.setStatus("current")
_Pm253PerfTelecomClientPast15StatHistorySefsValuePort2_Type = Unsigned32
_Pm253PerfTelecomClientPast15StatHistorySefsValuePort2_Object = MibTableColumn
pm253PerfTelecomClientPast15StatHistorySefsValuePort2 = _Pm253PerfTelecomClientPast15StatHistorySefsValuePort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 25, 1, 9),
    _Pm253PerfTelecomClientPast15StatHistorySefsValuePort2_Type()
)
pm253PerfTelecomClientPast15StatHistorySefsValuePort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast15StatHistorySefsValuePort2.setStatus("current")
_Pm253PerfTelecomClientPast15StatHistoryInvUasPort2_Type = EkiOnOff
_Pm253PerfTelecomClientPast15StatHistoryInvUasPort2_Object = MibTableColumn
pm253PerfTelecomClientPast15StatHistoryInvUasPort2 = _Pm253PerfTelecomClientPast15StatHistoryInvUasPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 25, 1, 10),
    _Pm253PerfTelecomClientPast15StatHistoryInvUasPort2_Type()
)
pm253PerfTelecomClientPast15StatHistoryInvUasPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast15StatHistoryInvUasPort2.setStatus("current")
_Pm253PerfTelecomClientPast15StatHistoryUasValuePort2_Type = Unsigned32
_Pm253PerfTelecomClientPast15StatHistoryUasValuePort2_Object = MibTableColumn
pm253PerfTelecomClientPast15StatHistoryUasValuePort2 = _Pm253PerfTelecomClientPast15StatHistoryUasValuePort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 25, 1, 11),
    _Pm253PerfTelecomClientPast15StatHistoryUasValuePort2_Type()
)
pm253PerfTelecomClientPast15StatHistoryUasValuePort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast15StatHistoryUasValuePort2.setStatus("current")
_Pm253PerfTelecomClientPast15StatHistoryPort3Table_Object = MibTable
pm253PerfTelecomClientPast15StatHistoryPort3Table = _Pm253PerfTelecomClientPast15StatHistoryPort3Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 26)
)
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast15StatHistoryPort3Table.setStatus("current")
_Pm253PerfTelecomClientPast15StatHistoryPort3Entry_Object = MibTableRow
pm253PerfTelecomClientPast15StatHistoryPort3Entry = _Pm253PerfTelecomClientPast15StatHistoryPort3Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 26, 1)
)
pm253PerfTelecomClientPast15StatHistoryPort3Entry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253PerfTelecomClientPast15StatHistoryPort3Index"),
)
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast15StatHistoryPort3Entry.setStatus("current")


class _Pm253PerfTelecomClientPast15StatHistoryPort3Index_Type(Integer32):
    """Custom type pm253PerfTelecomClientPast15StatHistoryPort3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253PerfTelecomClientPast15StatHistoryPort3Index_Type.__name__ = "Integer32"
_Pm253PerfTelecomClientPast15StatHistoryPort3Index_Object = MibTableColumn
pm253PerfTelecomClientPast15StatHistoryPort3Index = _Pm253PerfTelecomClientPast15StatHistoryPort3Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 26, 1, 1),
    _Pm253PerfTelecomClientPast15StatHistoryPort3Index_Type()
)
pm253PerfTelecomClientPast15StatHistoryPort3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast15StatHistoryPort3Index.setStatus("current")
_Pm253PerfTelecomClientPast15StatHistoryInvCvPort3_Type = EkiOnOff
_Pm253PerfTelecomClientPast15StatHistoryInvCvPort3_Object = MibTableColumn
pm253PerfTelecomClientPast15StatHistoryInvCvPort3 = _Pm253PerfTelecomClientPast15StatHistoryInvCvPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 26, 1, 2),
    _Pm253PerfTelecomClientPast15StatHistoryInvCvPort3_Type()
)
pm253PerfTelecomClientPast15StatHistoryInvCvPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast15StatHistoryInvCvPort3.setStatus("current")
_Pm253PerfTelecomClientPast15StatHistoryCvValuePort3_Type = Unsigned32
_Pm253PerfTelecomClientPast15StatHistoryCvValuePort3_Object = MibTableColumn
pm253PerfTelecomClientPast15StatHistoryCvValuePort3 = _Pm253PerfTelecomClientPast15StatHistoryCvValuePort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 26, 1, 3),
    _Pm253PerfTelecomClientPast15StatHistoryCvValuePort3_Type()
)
pm253PerfTelecomClientPast15StatHistoryCvValuePort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast15StatHistoryCvValuePort3.setStatus("current")
_Pm253PerfTelecomClientPast15StatHistoryInvEsPort3_Type = EkiOnOff
_Pm253PerfTelecomClientPast15StatHistoryInvEsPort3_Object = MibTableColumn
pm253PerfTelecomClientPast15StatHistoryInvEsPort3 = _Pm253PerfTelecomClientPast15StatHistoryInvEsPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 26, 1, 4),
    _Pm253PerfTelecomClientPast15StatHistoryInvEsPort3_Type()
)
pm253PerfTelecomClientPast15StatHistoryInvEsPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast15StatHistoryInvEsPort3.setStatus("current")
_Pm253PerfTelecomClientPast15StatHistoryEsValuePort3_Type = Unsigned32
_Pm253PerfTelecomClientPast15StatHistoryEsValuePort3_Object = MibTableColumn
pm253PerfTelecomClientPast15StatHistoryEsValuePort3 = _Pm253PerfTelecomClientPast15StatHistoryEsValuePort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 26, 1, 5),
    _Pm253PerfTelecomClientPast15StatHistoryEsValuePort3_Type()
)
pm253PerfTelecomClientPast15StatHistoryEsValuePort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast15StatHistoryEsValuePort3.setStatus("current")
_Pm253PerfTelecomClientPast15StatHistoryInvSesPort3_Type = EkiOnOff
_Pm253PerfTelecomClientPast15StatHistoryInvSesPort3_Object = MibTableColumn
pm253PerfTelecomClientPast15StatHistoryInvSesPort3 = _Pm253PerfTelecomClientPast15StatHistoryInvSesPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 26, 1, 6),
    _Pm253PerfTelecomClientPast15StatHistoryInvSesPort3_Type()
)
pm253PerfTelecomClientPast15StatHistoryInvSesPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast15StatHistoryInvSesPort3.setStatus("current")
_Pm253PerfTelecomClientPast15StatHistorySesValuePort3_Type = Unsigned32
_Pm253PerfTelecomClientPast15StatHistorySesValuePort3_Object = MibTableColumn
pm253PerfTelecomClientPast15StatHistorySesValuePort3 = _Pm253PerfTelecomClientPast15StatHistorySesValuePort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 26, 1, 7),
    _Pm253PerfTelecomClientPast15StatHistorySesValuePort3_Type()
)
pm253PerfTelecomClientPast15StatHistorySesValuePort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast15StatHistorySesValuePort3.setStatus("current")
_Pm253PerfTelecomClientPast15StatHistoryInvSefsPort3_Type = EkiOnOff
_Pm253PerfTelecomClientPast15StatHistoryInvSefsPort3_Object = MibTableColumn
pm253PerfTelecomClientPast15StatHistoryInvSefsPort3 = _Pm253PerfTelecomClientPast15StatHistoryInvSefsPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 26, 1, 8),
    _Pm253PerfTelecomClientPast15StatHistoryInvSefsPort3_Type()
)
pm253PerfTelecomClientPast15StatHistoryInvSefsPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast15StatHistoryInvSefsPort3.setStatus("current")
_Pm253PerfTelecomClientPast15StatHistorySefsValuePort3_Type = Unsigned32
_Pm253PerfTelecomClientPast15StatHistorySefsValuePort3_Object = MibTableColumn
pm253PerfTelecomClientPast15StatHistorySefsValuePort3 = _Pm253PerfTelecomClientPast15StatHistorySefsValuePort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 26, 1, 9),
    _Pm253PerfTelecomClientPast15StatHistorySefsValuePort3_Type()
)
pm253PerfTelecomClientPast15StatHistorySefsValuePort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast15StatHistorySefsValuePort3.setStatus("current")
_Pm253PerfTelecomClientPast15StatHistoryInvUasPort3_Type = EkiOnOff
_Pm253PerfTelecomClientPast15StatHistoryInvUasPort3_Object = MibTableColumn
pm253PerfTelecomClientPast15StatHistoryInvUasPort3 = _Pm253PerfTelecomClientPast15StatHistoryInvUasPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 26, 1, 10),
    _Pm253PerfTelecomClientPast15StatHistoryInvUasPort3_Type()
)
pm253PerfTelecomClientPast15StatHistoryInvUasPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast15StatHistoryInvUasPort3.setStatus("current")
_Pm253PerfTelecomClientPast15StatHistoryUasValuePort3_Type = Unsigned32
_Pm253PerfTelecomClientPast15StatHistoryUasValuePort3_Object = MibTableColumn
pm253PerfTelecomClientPast15StatHistoryUasValuePort3 = _Pm253PerfTelecomClientPast15StatHistoryUasValuePort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 26, 1, 11),
    _Pm253PerfTelecomClientPast15StatHistoryUasValuePort3_Type()
)
pm253PerfTelecomClientPast15StatHistoryUasValuePort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast15StatHistoryUasValuePort3.setStatus("current")
_Pm253PerfTelecomClientCurrent24StatTable_Object = MibTable
pm253PerfTelecomClientCurrent24StatTable = _Pm253PerfTelecomClientCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 32)
)
if mibBuilder.loadTexts:
    pm253PerfTelecomClientCurrent24StatTable.setStatus("current")
_Pm253PerfTelecomClientCurrent24StatEntry_Object = MibTableRow
pm253PerfTelecomClientCurrent24StatEntry = _Pm253PerfTelecomClientCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 32, 1)
)
pm253PerfTelecomClientCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253PerfTelecomClientCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pm253PerfTelecomClientCurrent24StatEntry.setStatus("current")


class _Pm253PerfTelecomClientCurrent24StatIndex_Type(Integer32):
    """Custom type pm253PerfTelecomClientCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253PerfTelecomClientCurrent24StatIndex_Type.__name__ = "Integer32"
_Pm253PerfTelecomClientCurrent24StatIndex_Object = MibTableColumn
pm253PerfTelecomClientCurrent24StatIndex = _Pm253PerfTelecomClientCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 32, 1, 1),
    _Pm253PerfTelecomClientCurrent24StatIndex_Type()
)
pm253PerfTelecomClientCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientCurrent24StatIndex.setStatus("current")
_Pm253PerfTelecomClientCurrent24StatInvCvPortn_Type = EkiOnOff
_Pm253PerfTelecomClientCurrent24StatInvCvPortn_Object = MibTableColumn
pm253PerfTelecomClientCurrent24StatInvCvPortn = _Pm253PerfTelecomClientCurrent24StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 32, 1, 2),
    _Pm253PerfTelecomClientCurrent24StatInvCvPortn_Type()
)
pm253PerfTelecomClientCurrent24StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientCurrent24StatInvCvPortn.setStatus("current")
_Pm253PerfTelecomClientCurrent24StatCvValuePortn_Type = Unsigned32
_Pm253PerfTelecomClientCurrent24StatCvValuePortn_Object = MibTableColumn
pm253PerfTelecomClientCurrent24StatCvValuePortn = _Pm253PerfTelecomClientCurrent24StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 32, 1, 3),
    _Pm253PerfTelecomClientCurrent24StatCvValuePortn_Type()
)
pm253PerfTelecomClientCurrent24StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientCurrent24StatCvValuePortn.setStatus("current")
_Pm253PerfTelecomClientCurrent24StatInvEsPortn_Type = EkiOnOff
_Pm253PerfTelecomClientCurrent24StatInvEsPortn_Object = MibTableColumn
pm253PerfTelecomClientCurrent24StatInvEsPortn = _Pm253PerfTelecomClientCurrent24StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 32, 1, 4),
    _Pm253PerfTelecomClientCurrent24StatInvEsPortn_Type()
)
pm253PerfTelecomClientCurrent24StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientCurrent24StatInvEsPortn.setStatus("current")
_Pm253PerfTelecomClientCurrent24StatEsValuePortn_Type = Unsigned32
_Pm253PerfTelecomClientCurrent24StatEsValuePortn_Object = MibTableColumn
pm253PerfTelecomClientCurrent24StatEsValuePortn = _Pm253PerfTelecomClientCurrent24StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 32, 1, 5),
    _Pm253PerfTelecomClientCurrent24StatEsValuePortn_Type()
)
pm253PerfTelecomClientCurrent24StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientCurrent24StatEsValuePortn.setStatus("current")
_Pm253PerfTelecomClientCurrent24StatInvSesPortn_Type = EkiOnOff
_Pm253PerfTelecomClientCurrent24StatInvSesPortn_Object = MibTableColumn
pm253PerfTelecomClientCurrent24StatInvSesPortn = _Pm253PerfTelecomClientCurrent24StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 32, 1, 6),
    _Pm253PerfTelecomClientCurrent24StatInvSesPortn_Type()
)
pm253PerfTelecomClientCurrent24StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientCurrent24StatInvSesPortn.setStatus("current")
_Pm253PerfTelecomClientCurrent24StatSesValuePortn_Type = Unsigned32
_Pm253PerfTelecomClientCurrent24StatSesValuePortn_Object = MibTableColumn
pm253PerfTelecomClientCurrent24StatSesValuePortn = _Pm253PerfTelecomClientCurrent24StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 32, 1, 7),
    _Pm253PerfTelecomClientCurrent24StatSesValuePortn_Type()
)
pm253PerfTelecomClientCurrent24StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientCurrent24StatSesValuePortn.setStatus("current")
_Pm253PerfTelecomClientCurrent24StatInvSefsPortn_Type = EkiOnOff
_Pm253PerfTelecomClientCurrent24StatInvSefsPortn_Object = MibTableColumn
pm253PerfTelecomClientCurrent24StatInvSefsPortn = _Pm253PerfTelecomClientCurrent24StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 32, 1, 8),
    _Pm253PerfTelecomClientCurrent24StatInvSefsPortn_Type()
)
pm253PerfTelecomClientCurrent24StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientCurrent24StatInvSefsPortn.setStatus("current")
_Pm253PerfTelecomClientCurrent24StatSefsValuePortn_Type = Unsigned32
_Pm253PerfTelecomClientCurrent24StatSefsValuePortn_Object = MibTableColumn
pm253PerfTelecomClientCurrent24StatSefsValuePortn = _Pm253PerfTelecomClientCurrent24StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 32, 1, 9),
    _Pm253PerfTelecomClientCurrent24StatSefsValuePortn_Type()
)
pm253PerfTelecomClientCurrent24StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientCurrent24StatSefsValuePortn.setStatus("current")
_Pm253PerfTelecomClientCurrent24StatInvUasPortn_Type = EkiOnOff
_Pm253PerfTelecomClientCurrent24StatInvUasPortn_Object = MibTableColumn
pm253PerfTelecomClientCurrent24StatInvUasPortn = _Pm253PerfTelecomClientCurrent24StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 32, 1, 10),
    _Pm253PerfTelecomClientCurrent24StatInvUasPortn_Type()
)
pm253PerfTelecomClientCurrent24StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientCurrent24StatInvUasPortn.setStatus("current")
_Pm253PerfTelecomClientCurrent24StatUasValuePortn_Type = Unsigned32
_Pm253PerfTelecomClientCurrent24StatUasValuePortn_Object = MibTableColumn
pm253PerfTelecomClientCurrent24StatUasValuePortn = _Pm253PerfTelecomClientCurrent24StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 32, 1, 11),
    _Pm253PerfTelecomClientCurrent24StatUasValuePortn_Type()
)
pm253PerfTelecomClientCurrent24StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientCurrent24StatUasValuePortn.setStatus("current")
_Pm253PerfTelecomClientPast24StatHistoryPort1Table_Object = MibTable
pm253PerfTelecomClientPast24StatHistoryPort1Table = _Pm253PerfTelecomClientPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 40)
)
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast24StatHistoryPort1Table.setStatus("current")
_Pm253PerfTelecomClientPast24StatHistoryPort1Entry_Object = MibTableRow
pm253PerfTelecomClientPast24StatHistoryPort1Entry = _Pm253PerfTelecomClientPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 40, 1)
)
pm253PerfTelecomClientPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253PerfTelecomClientPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast24StatHistoryPort1Entry.setStatus("current")


class _Pm253PerfTelecomClientPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pm253PerfTelecomClientPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253PerfTelecomClientPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm253PerfTelecomClientPast24StatHistoryPort1Index_Object = MibTableColumn
pm253PerfTelecomClientPast24StatHistoryPort1Index = _Pm253PerfTelecomClientPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 40, 1, 1),
    _Pm253PerfTelecomClientPast24StatHistoryPort1Index_Type()
)
pm253PerfTelecomClientPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast24StatHistoryPort1Index.setStatus("current")
_Pm253PerfTelecomClientPast24StatHistoryInvCvPort1_Type = EkiOnOff
_Pm253PerfTelecomClientPast24StatHistoryInvCvPort1_Object = MibTableColumn
pm253PerfTelecomClientPast24StatHistoryInvCvPort1 = _Pm253PerfTelecomClientPast24StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 40, 1, 2),
    _Pm253PerfTelecomClientPast24StatHistoryInvCvPort1_Type()
)
pm253PerfTelecomClientPast24StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast24StatHistoryInvCvPort1.setStatus("current")
_Pm253PerfTelecomClientPast24StatHistoryCvValuePort1_Type = Unsigned32
_Pm253PerfTelecomClientPast24StatHistoryCvValuePort1_Object = MibTableColumn
pm253PerfTelecomClientPast24StatHistoryCvValuePort1 = _Pm253PerfTelecomClientPast24StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 40, 1, 3),
    _Pm253PerfTelecomClientPast24StatHistoryCvValuePort1_Type()
)
pm253PerfTelecomClientPast24StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast24StatHistoryCvValuePort1.setStatus("current")
_Pm253PerfTelecomClientPast24StatHistoryInvEsPort1_Type = EkiOnOff
_Pm253PerfTelecomClientPast24StatHistoryInvEsPort1_Object = MibTableColumn
pm253PerfTelecomClientPast24StatHistoryInvEsPort1 = _Pm253PerfTelecomClientPast24StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 40, 1, 4),
    _Pm253PerfTelecomClientPast24StatHistoryInvEsPort1_Type()
)
pm253PerfTelecomClientPast24StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast24StatHistoryInvEsPort1.setStatus("current")
_Pm253PerfTelecomClientPast24StatHistoryEsValuePort1_Type = Unsigned32
_Pm253PerfTelecomClientPast24StatHistoryEsValuePort1_Object = MibTableColumn
pm253PerfTelecomClientPast24StatHistoryEsValuePort1 = _Pm253PerfTelecomClientPast24StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 40, 1, 5),
    _Pm253PerfTelecomClientPast24StatHistoryEsValuePort1_Type()
)
pm253PerfTelecomClientPast24StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast24StatHistoryEsValuePort1.setStatus("current")
_Pm253PerfTelecomClientPast24StatHistoryInvSesPort1_Type = EkiOnOff
_Pm253PerfTelecomClientPast24StatHistoryInvSesPort1_Object = MibTableColumn
pm253PerfTelecomClientPast24StatHistoryInvSesPort1 = _Pm253PerfTelecomClientPast24StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 40, 1, 6),
    _Pm253PerfTelecomClientPast24StatHistoryInvSesPort1_Type()
)
pm253PerfTelecomClientPast24StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast24StatHistoryInvSesPort1.setStatus("current")
_Pm253PerfTelecomClientPast24StatHistorySesValuePort1_Type = Unsigned32
_Pm253PerfTelecomClientPast24StatHistorySesValuePort1_Object = MibTableColumn
pm253PerfTelecomClientPast24StatHistorySesValuePort1 = _Pm253PerfTelecomClientPast24StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 40, 1, 7),
    _Pm253PerfTelecomClientPast24StatHistorySesValuePort1_Type()
)
pm253PerfTelecomClientPast24StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast24StatHistorySesValuePort1.setStatus("current")
_Pm253PerfTelecomClientPast24StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm253PerfTelecomClientPast24StatHistoryInvSefsPort1_Object = MibTableColumn
pm253PerfTelecomClientPast24StatHistoryInvSefsPort1 = _Pm253PerfTelecomClientPast24StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 40, 1, 8),
    _Pm253PerfTelecomClientPast24StatHistoryInvSefsPort1_Type()
)
pm253PerfTelecomClientPast24StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast24StatHistoryInvSefsPort1.setStatus("current")
_Pm253PerfTelecomClientPast24StatHistorySefsValuePort1_Type = Unsigned32
_Pm253PerfTelecomClientPast24StatHistorySefsValuePort1_Object = MibTableColumn
pm253PerfTelecomClientPast24StatHistorySefsValuePort1 = _Pm253PerfTelecomClientPast24StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 40, 1, 9),
    _Pm253PerfTelecomClientPast24StatHistorySefsValuePort1_Type()
)
pm253PerfTelecomClientPast24StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast24StatHistorySefsValuePort1.setStatus("current")
_Pm253PerfTelecomClientPast24StatHistoryInvUasPort1_Type = EkiOnOff
_Pm253PerfTelecomClientPast24StatHistoryInvUasPort1_Object = MibTableColumn
pm253PerfTelecomClientPast24StatHistoryInvUasPort1 = _Pm253PerfTelecomClientPast24StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 40, 1, 10),
    _Pm253PerfTelecomClientPast24StatHistoryInvUasPort1_Type()
)
pm253PerfTelecomClientPast24StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast24StatHistoryInvUasPort1.setStatus("current")
_Pm253PerfTelecomClientPast24StatHistoryUasValuePort1_Type = Unsigned32
_Pm253PerfTelecomClientPast24StatHistoryUasValuePort1_Object = MibTableColumn
pm253PerfTelecomClientPast24StatHistoryUasValuePort1 = _Pm253PerfTelecomClientPast24StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 40, 1, 11),
    _Pm253PerfTelecomClientPast24StatHistoryUasValuePort1_Type()
)
pm253PerfTelecomClientPast24StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast24StatHistoryUasValuePort1.setStatus("current")
_Pm253PerfTelecomClientPast24StatHistoryPort2Table_Object = MibTable
pm253PerfTelecomClientPast24StatHistoryPort2Table = _Pm253PerfTelecomClientPast24StatHistoryPort2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 41)
)
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast24StatHistoryPort2Table.setStatus("current")
_Pm253PerfTelecomClientPast24StatHistoryPort2Entry_Object = MibTableRow
pm253PerfTelecomClientPast24StatHistoryPort2Entry = _Pm253PerfTelecomClientPast24StatHistoryPort2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 41, 1)
)
pm253PerfTelecomClientPast24StatHistoryPort2Entry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253PerfTelecomClientPast24StatHistoryPort2Index"),
)
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast24StatHistoryPort2Entry.setStatus("current")


class _Pm253PerfTelecomClientPast24StatHistoryPort2Index_Type(Integer32):
    """Custom type pm253PerfTelecomClientPast24StatHistoryPort2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253PerfTelecomClientPast24StatHistoryPort2Index_Type.__name__ = "Integer32"
_Pm253PerfTelecomClientPast24StatHistoryPort2Index_Object = MibTableColumn
pm253PerfTelecomClientPast24StatHistoryPort2Index = _Pm253PerfTelecomClientPast24StatHistoryPort2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 41, 1, 1),
    _Pm253PerfTelecomClientPast24StatHistoryPort2Index_Type()
)
pm253PerfTelecomClientPast24StatHistoryPort2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast24StatHistoryPort2Index.setStatus("current")
_Pm253PerfTelecomClientPast24StatHistoryInvCvPort2_Type = EkiOnOff
_Pm253PerfTelecomClientPast24StatHistoryInvCvPort2_Object = MibTableColumn
pm253PerfTelecomClientPast24StatHistoryInvCvPort2 = _Pm253PerfTelecomClientPast24StatHistoryInvCvPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 41, 1, 2),
    _Pm253PerfTelecomClientPast24StatHistoryInvCvPort2_Type()
)
pm253PerfTelecomClientPast24StatHistoryInvCvPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast24StatHistoryInvCvPort2.setStatus("current")
_Pm253PerfTelecomClientPast24StatHistoryCvValuePort2_Type = Unsigned32
_Pm253PerfTelecomClientPast24StatHistoryCvValuePort2_Object = MibTableColumn
pm253PerfTelecomClientPast24StatHistoryCvValuePort2 = _Pm253PerfTelecomClientPast24StatHistoryCvValuePort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 41, 1, 3),
    _Pm253PerfTelecomClientPast24StatHistoryCvValuePort2_Type()
)
pm253PerfTelecomClientPast24StatHistoryCvValuePort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast24StatHistoryCvValuePort2.setStatus("current")
_Pm253PerfTelecomClientPast24StatHistoryInvEsPort2_Type = EkiOnOff
_Pm253PerfTelecomClientPast24StatHistoryInvEsPort2_Object = MibTableColumn
pm253PerfTelecomClientPast24StatHistoryInvEsPort2 = _Pm253PerfTelecomClientPast24StatHistoryInvEsPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 41, 1, 4),
    _Pm253PerfTelecomClientPast24StatHistoryInvEsPort2_Type()
)
pm253PerfTelecomClientPast24StatHistoryInvEsPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast24StatHistoryInvEsPort2.setStatus("current")
_Pm253PerfTelecomClientPast24StatHistoryEsValuePort2_Type = Unsigned32
_Pm253PerfTelecomClientPast24StatHistoryEsValuePort2_Object = MibTableColumn
pm253PerfTelecomClientPast24StatHistoryEsValuePort2 = _Pm253PerfTelecomClientPast24StatHistoryEsValuePort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 41, 1, 5),
    _Pm253PerfTelecomClientPast24StatHistoryEsValuePort2_Type()
)
pm253PerfTelecomClientPast24StatHistoryEsValuePort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast24StatHistoryEsValuePort2.setStatus("current")
_Pm253PerfTelecomClientPast24StatHistoryInvSesPort2_Type = EkiOnOff
_Pm253PerfTelecomClientPast24StatHistoryInvSesPort2_Object = MibTableColumn
pm253PerfTelecomClientPast24StatHistoryInvSesPort2 = _Pm253PerfTelecomClientPast24StatHistoryInvSesPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 41, 1, 6),
    _Pm253PerfTelecomClientPast24StatHistoryInvSesPort2_Type()
)
pm253PerfTelecomClientPast24StatHistoryInvSesPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast24StatHistoryInvSesPort2.setStatus("current")
_Pm253PerfTelecomClientPast24StatHistorySesValuePort2_Type = Unsigned32
_Pm253PerfTelecomClientPast24StatHistorySesValuePort2_Object = MibTableColumn
pm253PerfTelecomClientPast24StatHistorySesValuePort2 = _Pm253PerfTelecomClientPast24StatHistorySesValuePort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 41, 1, 7),
    _Pm253PerfTelecomClientPast24StatHistorySesValuePort2_Type()
)
pm253PerfTelecomClientPast24StatHistorySesValuePort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast24StatHistorySesValuePort2.setStatus("current")
_Pm253PerfTelecomClientPast24StatHistoryInvSefsPort2_Type = EkiOnOff
_Pm253PerfTelecomClientPast24StatHistoryInvSefsPort2_Object = MibTableColumn
pm253PerfTelecomClientPast24StatHistoryInvSefsPort2 = _Pm253PerfTelecomClientPast24StatHistoryInvSefsPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 41, 1, 8),
    _Pm253PerfTelecomClientPast24StatHistoryInvSefsPort2_Type()
)
pm253PerfTelecomClientPast24StatHistoryInvSefsPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast24StatHistoryInvSefsPort2.setStatus("current")
_Pm253PerfTelecomClientPast24StatHistorySefsValuePort2_Type = Unsigned32
_Pm253PerfTelecomClientPast24StatHistorySefsValuePort2_Object = MibTableColumn
pm253PerfTelecomClientPast24StatHistorySefsValuePort2 = _Pm253PerfTelecomClientPast24StatHistorySefsValuePort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 41, 1, 9),
    _Pm253PerfTelecomClientPast24StatHistorySefsValuePort2_Type()
)
pm253PerfTelecomClientPast24StatHistorySefsValuePort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast24StatHistorySefsValuePort2.setStatus("current")
_Pm253PerfTelecomClientPast24StatHistoryInvUasPort2_Type = EkiOnOff
_Pm253PerfTelecomClientPast24StatHistoryInvUasPort2_Object = MibTableColumn
pm253PerfTelecomClientPast24StatHistoryInvUasPort2 = _Pm253PerfTelecomClientPast24StatHistoryInvUasPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 41, 1, 10),
    _Pm253PerfTelecomClientPast24StatHistoryInvUasPort2_Type()
)
pm253PerfTelecomClientPast24StatHistoryInvUasPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast24StatHistoryInvUasPort2.setStatus("current")
_Pm253PerfTelecomClientPast24StatHistoryUasValuePort2_Type = Unsigned32
_Pm253PerfTelecomClientPast24StatHistoryUasValuePort2_Object = MibTableColumn
pm253PerfTelecomClientPast24StatHistoryUasValuePort2 = _Pm253PerfTelecomClientPast24StatHistoryUasValuePort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 41, 1, 11),
    _Pm253PerfTelecomClientPast24StatHistoryUasValuePort2_Type()
)
pm253PerfTelecomClientPast24StatHistoryUasValuePort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast24StatHistoryUasValuePort2.setStatus("current")
_Pm253PerfTelecomClientPast24StatHistoryPort3Table_Object = MibTable
pm253PerfTelecomClientPast24StatHistoryPort3Table = _Pm253PerfTelecomClientPast24StatHistoryPort3Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 42)
)
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast24StatHistoryPort3Table.setStatus("current")
_Pm253PerfTelecomClientPast24StatHistoryPort3Entry_Object = MibTableRow
pm253PerfTelecomClientPast24StatHistoryPort3Entry = _Pm253PerfTelecomClientPast24StatHistoryPort3Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 42, 1)
)
pm253PerfTelecomClientPast24StatHistoryPort3Entry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253PerfTelecomClientPast24StatHistoryPort3Index"),
)
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast24StatHistoryPort3Entry.setStatus("current")


class _Pm253PerfTelecomClientPast24StatHistoryPort3Index_Type(Integer32):
    """Custom type pm253PerfTelecomClientPast24StatHistoryPort3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253PerfTelecomClientPast24StatHistoryPort3Index_Type.__name__ = "Integer32"
_Pm253PerfTelecomClientPast24StatHistoryPort3Index_Object = MibTableColumn
pm253PerfTelecomClientPast24StatHistoryPort3Index = _Pm253PerfTelecomClientPast24StatHistoryPort3Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 42, 1, 1),
    _Pm253PerfTelecomClientPast24StatHistoryPort3Index_Type()
)
pm253PerfTelecomClientPast24StatHistoryPort3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast24StatHistoryPort3Index.setStatus("current")
_Pm253PerfTelecomClientPast24StatHistoryInvCvPort3_Type = EkiOnOff
_Pm253PerfTelecomClientPast24StatHistoryInvCvPort3_Object = MibTableColumn
pm253PerfTelecomClientPast24StatHistoryInvCvPort3 = _Pm253PerfTelecomClientPast24StatHistoryInvCvPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 42, 1, 2),
    _Pm253PerfTelecomClientPast24StatHistoryInvCvPort3_Type()
)
pm253PerfTelecomClientPast24StatHistoryInvCvPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast24StatHistoryInvCvPort3.setStatus("current")
_Pm253PerfTelecomClientPast24StatHistoryCvValuePort3_Type = Unsigned32
_Pm253PerfTelecomClientPast24StatHistoryCvValuePort3_Object = MibTableColumn
pm253PerfTelecomClientPast24StatHistoryCvValuePort3 = _Pm253PerfTelecomClientPast24StatHistoryCvValuePort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 42, 1, 3),
    _Pm253PerfTelecomClientPast24StatHistoryCvValuePort3_Type()
)
pm253PerfTelecomClientPast24StatHistoryCvValuePort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast24StatHistoryCvValuePort3.setStatus("current")
_Pm253PerfTelecomClientPast24StatHistoryInvEsPort3_Type = EkiOnOff
_Pm253PerfTelecomClientPast24StatHistoryInvEsPort3_Object = MibTableColumn
pm253PerfTelecomClientPast24StatHistoryInvEsPort3 = _Pm253PerfTelecomClientPast24StatHistoryInvEsPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 42, 1, 4),
    _Pm253PerfTelecomClientPast24StatHistoryInvEsPort3_Type()
)
pm253PerfTelecomClientPast24StatHistoryInvEsPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast24StatHistoryInvEsPort3.setStatus("current")
_Pm253PerfTelecomClientPast24StatHistoryEsValuePort3_Type = Unsigned32
_Pm253PerfTelecomClientPast24StatHistoryEsValuePort3_Object = MibTableColumn
pm253PerfTelecomClientPast24StatHistoryEsValuePort3 = _Pm253PerfTelecomClientPast24StatHistoryEsValuePort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 42, 1, 5),
    _Pm253PerfTelecomClientPast24StatHistoryEsValuePort3_Type()
)
pm253PerfTelecomClientPast24StatHistoryEsValuePort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast24StatHistoryEsValuePort3.setStatus("current")
_Pm253PerfTelecomClientPast24StatHistoryInvSesPort3_Type = EkiOnOff
_Pm253PerfTelecomClientPast24StatHistoryInvSesPort3_Object = MibTableColumn
pm253PerfTelecomClientPast24StatHistoryInvSesPort3 = _Pm253PerfTelecomClientPast24StatHistoryInvSesPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 42, 1, 6),
    _Pm253PerfTelecomClientPast24StatHistoryInvSesPort3_Type()
)
pm253PerfTelecomClientPast24StatHistoryInvSesPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast24StatHistoryInvSesPort3.setStatus("current")
_Pm253PerfTelecomClientPast24StatHistorySesValuePort3_Type = Unsigned32
_Pm253PerfTelecomClientPast24StatHistorySesValuePort3_Object = MibTableColumn
pm253PerfTelecomClientPast24StatHistorySesValuePort3 = _Pm253PerfTelecomClientPast24StatHistorySesValuePort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 42, 1, 7),
    _Pm253PerfTelecomClientPast24StatHistorySesValuePort3_Type()
)
pm253PerfTelecomClientPast24StatHistorySesValuePort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast24StatHistorySesValuePort3.setStatus("current")
_Pm253PerfTelecomClientPast24StatHistoryInvSefsPort3_Type = EkiOnOff
_Pm253PerfTelecomClientPast24StatHistoryInvSefsPort3_Object = MibTableColumn
pm253PerfTelecomClientPast24StatHistoryInvSefsPort3 = _Pm253PerfTelecomClientPast24StatHistoryInvSefsPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 42, 1, 8),
    _Pm253PerfTelecomClientPast24StatHistoryInvSefsPort3_Type()
)
pm253PerfTelecomClientPast24StatHistoryInvSefsPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast24StatHistoryInvSefsPort3.setStatus("current")
_Pm253PerfTelecomClientPast24StatHistorySefsValuePort3_Type = Unsigned32
_Pm253PerfTelecomClientPast24StatHistorySefsValuePort3_Object = MibTableColumn
pm253PerfTelecomClientPast24StatHistorySefsValuePort3 = _Pm253PerfTelecomClientPast24StatHistorySefsValuePort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 42, 1, 9),
    _Pm253PerfTelecomClientPast24StatHistorySefsValuePort3_Type()
)
pm253PerfTelecomClientPast24StatHistorySefsValuePort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast24StatHistorySefsValuePort3.setStatus("current")
_Pm253PerfTelecomClientPast24StatHistoryInvUasPort3_Type = EkiOnOff
_Pm253PerfTelecomClientPast24StatHistoryInvUasPort3_Object = MibTableColumn
pm253PerfTelecomClientPast24StatHistoryInvUasPort3 = _Pm253PerfTelecomClientPast24StatHistoryInvUasPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 42, 1, 10),
    _Pm253PerfTelecomClientPast24StatHistoryInvUasPort3_Type()
)
pm253PerfTelecomClientPast24StatHistoryInvUasPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast24StatHistoryInvUasPort3.setStatus("current")
_Pm253PerfTelecomClientPast24StatHistoryUasValuePort3_Type = Unsigned32
_Pm253PerfTelecomClientPast24StatHistoryUasValuePort3_Object = MibTableColumn
pm253PerfTelecomClientPast24StatHistoryUasValuePort3 = _Pm253PerfTelecomClientPast24StatHistoryUasValuePort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 42, 1, 11),
    _Pm253PerfTelecomClientPast24StatHistoryUasValuePort3_Type()
)
pm253PerfTelecomClientPast24StatHistoryUasValuePort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomClientPast24StatHistoryUasValuePort3.setStatus("current")
_Pm253PerfDatacomClientCurrent15StatTable_Object = MibTable
pm253PerfDatacomClientCurrent15StatTable = _Pm253PerfDatacomClientCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 256)
)
if mibBuilder.loadTexts:
    pm253PerfDatacomClientCurrent15StatTable.setStatus("current")
_Pm253PerfDatacomClientCurrent15StatEntry_Object = MibTableRow
pm253PerfDatacomClientCurrent15StatEntry = _Pm253PerfDatacomClientCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 256, 1)
)
pm253PerfDatacomClientCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253PerfDatacomClientCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pm253PerfDatacomClientCurrent15StatEntry.setStatus("current")


class _Pm253PerfDatacomClientCurrent15StatIndex_Type(Integer32):
    """Custom type pm253PerfDatacomClientCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253PerfDatacomClientCurrent15StatIndex_Type.__name__ = "Integer32"
_Pm253PerfDatacomClientCurrent15StatIndex_Object = MibTableColumn
pm253PerfDatacomClientCurrent15StatIndex = _Pm253PerfDatacomClientCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 256, 1, 1),
    _Pm253PerfDatacomClientCurrent15StatIndex_Type()
)
pm253PerfDatacomClientCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfDatacomClientCurrent15StatIndex.setStatus("current")
_Pm253perfdatacomclientCurrent15StatInBytesCountInvPortn_Type = EkiOnOff
_Pm253perfdatacomclientCurrent15StatInBytesCountInvPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent15StatInBytesCountInvPortn = _Pm253perfdatacomclientCurrent15StatInBytesCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 256, 1, 2),
    _Pm253perfdatacomclientCurrent15StatInBytesCountInvPortn_Type()
)
pm253perfdatacomclientCurrent15StatInBytesCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent15StatInBytesCountInvPortn.setStatus("current")
_Pm253perfdatacomclientCurrent15StatInBytesCountPortn_Type = Counter64
_Pm253perfdatacomclientCurrent15StatInBytesCountPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent15StatInBytesCountPortn = _Pm253perfdatacomclientCurrent15StatInBytesCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 256, 1, 3),
    _Pm253perfdatacomclientCurrent15StatInBytesCountPortn_Type()
)
pm253perfdatacomclientCurrent15StatInBytesCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent15StatInBytesCountPortn.setStatus("current")
_Pm253perfdatacomclientCurrent15StatInCrcCountInvPortn_Type = EkiOnOff
_Pm253perfdatacomclientCurrent15StatInCrcCountInvPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent15StatInCrcCountInvPortn = _Pm253perfdatacomclientCurrent15StatInCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 256, 1, 4),
    _Pm253perfdatacomclientCurrent15StatInCrcCountInvPortn_Type()
)
pm253perfdatacomclientCurrent15StatInCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent15StatInCrcCountInvPortn.setStatus("current")
_Pm253perfdatacomclientCurrent15StatInCrcCountPortn_Type = Counter64
_Pm253perfdatacomclientCurrent15StatInCrcCountPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent15StatInCrcCountPortn = _Pm253perfdatacomclientCurrent15StatInCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 256, 1, 5),
    _Pm253perfdatacomclientCurrent15StatInCrcCountPortn_Type()
)
pm253perfdatacomclientCurrent15StatInCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent15StatInCrcCountPortn.setStatus("current")
_Pm253perfdatacomclientCurrent15StatInBroadcastCountInvPortn_Type = EkiOnOff
_Pm253perfdatacomclientCurrent15StatInBroadcastCountInvPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent15StatInBroadcastCountInvPortn = _Pm253perfdatacomclientCurrent15StatInBroadcastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 256, 1, 8),
    _Pm253perfdatacomclientCurrent15StatInBroadcastCountInvPortn_Type()
)
pm253perfdatacomclientCurrent15StatInBroadcastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent15StatInBroadcastCountInvPortn.setStatus("current")
_Pm253perfdatacomclientCurrent15StatInBroadcastCountPortn_Type = Counter64
_Pm253perfdatacomclientCurrent15StatInBroadcastCountPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent15StatInBroadcastCountPortn = _Pm253perfdatacomclientCurrent15StatInBroadcastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 256, 1, 9),
    _Pm253perfdatacomclientCurrent15StatInBroadcastCountPortn_Type()
)
pm253perfdatacomclientCurrent15StatInBroadcastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent15StatInBroadcastCountPortn.setStatus("current")
_Pm253perfdatacomclientCurrent15StatInMulticastCountInvPortn_Type = EkiOnOff
_Pm253perfdatacomclientCurrent15StatInMulticastCountInvPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent15StatInMulticastCountInvPortn = _Pm253perfdatacomclientCurrent15StatInMulticastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 256, 1, 10),
    _Pm253perfdatacomclientCurrent15StatInMulticastCountInvPortn_Type()
)
pm253perfdatacomclientCurrent15StatInMulticastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent15StatInMulticastCountInvPortn.setStatus("current")
_Pm253perfdatacomclientCurrent15StatInMulticastCountPortn_Type = Counter64
_Pm253perfdatacomclientCurrent15StatInMulticastCountPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent15StatInMulticastCountPortn = _Pm253perfdatacomclientCurrent15StatInMulticastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 256, 1, 11),
    _Pm253perfdatacomclientCurrent15StatInMulticastCountPortn_Type()
)
pm253perfdatacomclientCurrent15StatInMulticastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent15StatInMulticastCountPortn.setStatus("current")
_Pm253perfdatacomclientCurrent15StatInUnicastCountInvPortn_Type = EkiOnOff
_Pm253perfdatacomclientCurrent15StatInUnicastCountInvPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent15StatInUnicastCountInvPortn = _Pm253perfdatacomclientCurrent15StatInUnicastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 256, 1, 20),
    _Pm253perfdatacomclientCurrent15StatInUnicastCountInvPortn_Type()
)
pm253perfdatacomclientCurrent15StatInUnicastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent15StatInUnicastCountInvPortn.setStatus("current")
_Pm253perfdatacomclientCurrent15StatInUnicastCountPortn_Type = Counter64
_Pm253perfdatacomclientCurrent15StatInUnicastCountPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent15StatInUnicastCountPortn = _Pm253perfdatacomclientCurrent15StatInUnicastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 256, 1, 21),
    _Pm253perfdatacomclientCurrent15StatInUnicastCountPortn_Type()
)
pm253perfdatacomclientCurrent15StatInUnicastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent15StatInUnicastCountPortn.setStatus("current")
_Pm253perfdatacomclientCurrent15StatInNonunicastCountInvPortn_Type = EkiOnOff
_Pm253perfdatacomclientCurrent15StatInNonunicastCountInvPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent15StatInNonunicastCountInvPortn = _Pm253perfdatacomclientCurrent15StatInNonunicastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 256, 1, 22),
    _Pm253perfdatacomclientCurrent15StatInNonunicastCountInvPortn_Type()
)
pm253perfdatacomclientCurrent15StatInNonunicastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent15StatInNonunicastCountInvPortn.setStatus("current")
_Pm253perfdatacomclientCurrent15StatInNonunicastCountPortn_Type = Counter64
_Pm253perfdatacomclientCurrent15StatInNonunicastCountPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent15StatInNonunicastCountPortn = _Pm253perfdatacomclientCurrent15StatInNonunicastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 256, 1, 23),
    _Pm253perfdatacomclientCurrent15StatInNonunicastCountPortn_Type()
)
pm253perfdatacomclientCurrent15StatInNonunicastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent15StatInNonunicastCountPortn.setStatus("current")
_Pm253perfdatacomclientCurrent15StatOutBytesCountInvPortn_Type = EkiOnOff
_Pm253perfdatacomclientCurrent15StatOutBytesCountInvPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent15StatOutBytesCountInvPortn = _Pm253perfdatacomclientCurrent15StatOutBytesCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 256, 1, 26),
    _Pm253perfdatacomclientCurrent15StatOutBytesCountInvPortn_Type()
)
pm253perfdatacomclientCurrent15StatOutBytesCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent15StatOutBytesCountInvPortn.setStatus("current")
_Pm253perfdatacomclientCurrent15StatOutBytesCountPortn_Type = Counter64
_Pm253perfdatacomclientCurrent15StatOutBytesCountPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent15StatOutBytesCountPortn = _Pm253perfdatacomclientCurrent15StatOutBytesCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 256, 1, 27),
    _Pm253perfdatacomclientCurrent15StatOutBytesCountPortn_Type()
)
pm253perfdatacomclientCurrent15StatOutBytesCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent15StatOutBytesCountPortn.setStatus("current")
_Pm253perfdatacomclientCurrent15StatOutBroadcastCountInvPortn_Type = EkiOnOff
_Pm253perfdatacomclientCurrent15StatOutBroadcastCountInvPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent15StatOutBroadcastCountInvPortn = _Pm253perfdatacomclientCurrent15StatOutBroadcastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 256, 1, 32),
    _Pm253perfdatacomclientCurrent15StatOutBroadcastCountInvPortn_Type()
)
pm253perfdatacomclientCurrent15StatOutBroadcastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent15StatOutBroadcastCountInvPortn.setStatus("current")
_Pm253perfdatacomclientCurrent15StatOutBroadcastCountPortn_Type = Counter64
_Pm253perfdatacomclientCurrent15StatOutBroadcastCountPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent15StatOutBroadcastCountPortn = _Pm253perfdatacomclientCurrent15StatOutBroadcastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 256, 1, 33),
    _Pm253perfdatacomclientCurrent15StatOutBroadcastCountPortn_Type()
)
pm253perfdatacomclientCurrent15StatOutBroadcastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent15StatOutBroadcastCountPortn.setStatus("current")
_Pm253perfdatacomclientCurrent15StatOutMulticastCountInvPortn_Type = EkiOnOff
_Pm253perfdatacomclientCurrent15StatOutMulticastCountInvPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent15StatOutMulticastCountInvPortn = _Pm253perfdatacomclientCurrent15StatOutMulticastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 256, 1, 34),
    _Pm253perfdatacomclientCurrent15StatOutMulticastCountInvPortn_Type()
)
pm253perfdatacomclientCurrent15StatOutMulticastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent15StatOutMulticastCountInvPortn.setStatus("current")
_Pm253perfdatacomclientCurrent15StatOutMulticastCountPortn_Type = Counter64
_Pm253perfdatacomclientCurrent15StatOutMulticastCountPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent15StatOutMulticastCountPortn = _Pm253perfdatacomclientCurrent15StatOutMulticastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 256, 1, 35),
    _Pm253perfdatacomclientCurrent15StatOutMulticastCountPortn_Type()
)
pm253perfdatacomclientCurrent15StatOutMulticastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent15StatOutMulticastCountPortn.setStatus("current")
_Pm253perfdatacomclientCurrent15StatOutUnicastCountInvPortn_Type = EkiOnOff
_Pm253perfdatacomclientCurrent15StatOutUnicastCountInvPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent15StatOutUnicastCountInvPortn = _Pm253perfdatacomclientCurrent15StatOutUnicastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 256, 1, 42),
    _Pm253perfdatacomclientCurrent15StatOutUnicastCountInvPortn_Type()
)
pm253perfdatacomclientCurrent15StatOutUnicastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent15StatOutUnicastCountInvPortn.setStatus("current")
_Pm253perfdatacomclientCurrent15StatOutUnicastCountPortn_Type = Counter64
_Pm253perfdatacomclientCurrent15StatOutUnicastCountPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent15StatOutUnicastCountPortn = _Pm253perfdatacomclientCurrent15StatOutUnicastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 256, 1, 43),
    _Pm253perfdatacomclientCurrent15StatOutUnicastCountPortn_Type()
)
pm253perfdatacomclientCurrent15StatOutUnicastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent15StatOutUnicastCountPortn.setStatus("current")
_Pm253perfdatacomclientCurrent15StatOutNonunicastCountInvPortn_Type = EkiOnOff
_Pm253perfdatacomclientCurrent15StatOutNonunicastCountInvPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent15StatOutNonunicastCountInvPortn = _Pm253perfdatacomclientCurrent15StatOutNonunicastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 256, 1, 44),
    _Pm253perfdatacomclientCurrent15StatOutNonunicastCountInvPortn_Type()
)
pm253perfdatacomclientCurrent15StatOutNonunicastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent15StatOutNonunicastCountInvPortn.setStatus("current")
_Pm253perfdatacomclientCurrent15StatOutNonunicastCountPortn_Type = Counter64
_Pm253perfdatacomclientCurrent15StatOutNonunicastCountPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent15StatOutNonunicastCountPortn = _Pm253perfdatacomclientCurrent15StatOutNonunicastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 256, 1, 45),
    _Pm253perfdatacomclientCurrent15StatOutNonunicastCountPortn_Type()
)
pm253perfdatacomclientCurrent15StatOutNonunicastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent15StatOutNonunicastCountPortn.setStatus("current")
_Pm253PerfDatacomClientPast15StatHistoryPort1Table_Object = MibTable
pm253PerfDatacomClientPast15StatHistoryPort1Table = _Pm253PerfDatacomClientPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 264)
)
if mibBuilder.loadTexts:
    pm253PerfDatacomClientPast15StatHistoryPort1Table.setStatus("current")
_Pm253PerfDatacomClientPast15StatHistoryPort1Entry_Object = MibTableRow
pm253PerfDatacomClientPast15StatHistoryPort1Entry = _Pm253PerfDatacomClientPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 264, 1)
)
pm253PerfDatacomClientPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253PerfDatacomClientPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm253PerfDatacomClientPast15StatHistoryPort1Entry.setStatus("current")


class _Pm253PerfDatacomClientPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pm253PerfDatacomClientPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253PerfDatacomClientPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm253PerfDatacomClientPast15StatHistoryPort1Index_Object = MibTableColumn
pm253PerfDatacomClientPast15StatHistoryPort1Index = _Pm253PerfDatacomClientPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 264, 1, 1),
    _Pm253PerfDatacomClientPast15StatHistoryPort1Index_Type()
)
pm253PerfDatacomClientPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfDatacomClientPast15StatHistoryPort1Index.setStatus("current")
_Pm253perfdatacomclientPast15StatInBytesCountInvPort1_Type = EkiOnOff
_Pm253perfdatacomclientPast15StatInBytesCountInvPort1_Object = MibTableColumn
pm253perfdatacomclientPast15StatInBytesCountInvPort1 = _Pm253perfdatacomclientPast15StatInBytesCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 264, 1, 2),
    _Pm253perfdatacomclientPast15StatInBytesCountInvPort1_Type()
)
pm253perfdatacomclientPast15StatInBytesCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatInBytesCountInvPort1.setStatus("current")
_Pm253perfdatacomclientPast15StatInBytesCountPort1_Type = Counter64
_Pm253perfdatacomclientPast15StatInBytesCountPort1_Object = MibTableColumn
pm253perfdatacomclientPast15StatInBytesCountPort1 = _Pm253perfdatacomclientPast15StatInBytesCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 264, 1, 3),
    _Pm253perfdatacomclientPast15StatInBytesCountPort1_Type()
)
pm253perfdatacomclientPast15StatInBytesCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatInBytesCountPort1.setStatus("current")
_Pm253perfdatacomclientPast15StatInCrcCountInvPort1_Type = EkiOnOff
_Pm253perfdatacomclientPast15StatInCrcCountInvPort1_Object = MibTableColumn
pm253perfdatacomclientPast15StatInCrcCountInvPort1 = _Pm253perfdatacomclientPast15StatInCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 264, 1, 4),
    _Pm253perfdatacomclientPast15StatInCrcCountInvPort1_Type()
)
pm253perfdatacomclientPast15StatInCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatInCrcCountInvPort1.setStatus("current")
_Pm253perfdatacomclientPast15StatInCrcCountPort1_Type = Counter64
_Pm253perfdatacomclientPast15StatInCrcCountPort1_Object = MibTableColumn
pm253perfdatacomclientPast15StatInCrcCountPort1 = _Pm253perfdatacomclientPast15StatInCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 264, 1, 5),
    _Pm253perfdatacomclientPast15StatInCrcCountPort1_Type()
)
pm253perfdatacomclientPast15StatInCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatInCrcCountPort1.setStatus("current")
_Pm253perfdatacomclientPast15StatInBroadcastCountInvPort1_Type = EkiOnOff
_Pm253perfdatacomclientPast15StatInBroadcastCountInvPort1_Object = MibTableColumn
pm253perfdatacomclientPast15StatInBroadcastCountInvPort1 = _Pm253perfdatacomclientPast15StatInBroadcastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 264, 1, 8),
    _Pm253perfdatacomclientPast15StatInBroadcastCountInvPort1_Type()
)
pm253perfdatacomclientPast15StatInBroadcastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatInBroadcastCountInvPort1.setStatus("current")
_Pm253perfdatacomclientPast15StatInBroadcastCountPort1_Type = Counter64
_Pm253perfdatacomclientPast15StatInBroadcastCountPort1_Object = MibTableColumn
pm253perfdatacomclientPast15StatInBroadcastCountPort1 = _Pm253perfdatacomclientPast15StatInBroadcastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 264, 1, 9),
    _Pm253perfdatacomclientPast15StatInBroadcastCountPort1_Type()
)
pm253perfdatacomclientPast15StatInBroadcastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatInBroadcastCountPort1.setStatus("current")
_Pm253perfdatacomclientPast15StatInMulticastCountInvPort1_Type = EkiOnOff
_Pm253perfdatacomclientPast15StatInMulticastCountInvPort1_Object = MibTableColumn
pm253perfdatacomclientPast15StatInMulticastCountInvPort1 = _Pm253perfdatacomclientPast15StatInMulticastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 264, 1, 10),
    _Pm253perfdatacomclientPast15StatInMulticastCountInvPort1_Type()
)
pm253perfdatacomclientPast15StatInMulticastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatInMulticastCountInvPort1.setStatus("current")
_Pm253perfdatacomclientPast15StatInMulticastCountPort1_Type = Counter64
_Pm253perfdatacomclientPast15StatInMulticastCountPort1_Object = MibTableColumn
pm253perfdatacomclientPast15StatInMulticastCountPort1 = _Pm253perfdatacomclientPast15StatInMulticastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 264, 1, 11),
    _Pm253perfdatacomclientPast15StatInMulticastCountPort1_Type()
)
pm253perfdatacomclientPast15StatInMulticastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatInMulticastCountPort1.setStatus("current")
_Pm253perfdatacomclientPast15StatInUnicastCountInvPort1_Type = EkiOnOff
_Pm253perfdatacomclientPast15StatInUnicastCountInvPort1_Object = MibTableColumn
pm253perfdatacomclientPast15StatInUnicastCountInvPort1 = _Pm253perfdatacomclientPast15StatInUnicastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 264, 1, 20),
    _Pm253perfdatacomclientPast15StatInUnicastCountInvPort1_Type()
)
pm253perfdatacomclientPast15StatInUnicastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatInUnicastCountInvPort1.setStatus("current")
_Pm253perfdatacomclientPast15StatInUnicastCountPort1_Type = Counter64
_Pm253perfdatacomclientPast15StatInUnicastCountPort1_Object = MibTableColumn
pm253perfdatacomclientPast15StatInUnicastCountPort1 = _Pm253perfdatacomclientPast15StatInUnicastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 264, 1, 21),
    _Pm253perfdatacomclientPast15StatInUnicastCountPort1_Type()
)
pm253perfdatacomclientPast15StatInUnicastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatInUnicastCountPort1.setStatus("current")
_Pm253perfdatacomclientPast15StatInNonunicastCountInvPort1_Type = EkiOnOff
_Pm253perfdatacomclientPast15StatInNonunicastCountInvPort1_Object = MibTableColumn
pm253perfdatacomclientPast15StatInNonunicastCountInvPort1 = _Pm253perfdatacomclientPast15StatInNonunicastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 264, 1, 22),
    _Pm253perfdatacomclientPast15StatInNonunicastCountInvPort1_Type()
)
pm253perfdatacomclientPast15StatInNonunicastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatInNonunicastCountInvPort1.setStatus("current")
_Pm253perfdatacomclientPast15StatInNonunicastCountPort1_Type = Counter64
_Pm253perfdatacomclientPast15StatInNonunicastCountPort1_Object = MibTableColumn
pm253perfdatacomclientPast15StatInNonunicastCountPort1 = _Pm253perfdatacomclientPast15StatInNonunicastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 264, 1, 23),
    _Pm253perfdatacomclientPast15StatInNonunicastCountPort1_Type()
)
pm253perfdatacomclientPast15StatInNonunicastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatInNonunicastCountPort1.setStatus("current")
_Pm253perfdatacomclientPast15StatOutBytesCountInvPort1_Type = EkiOnOff
_Pm253perfdatacomclientPast15StatOutBytesCountInvPort1_Object = MibTableColumn
pm253perfdatacomclientPast15StatOutBytesCountInvPort1 = _Pm253perfdatacomclientPast15StatOutBytesCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 264, 1, 26),
    _Pm253perfdatacomclientPast15StatOutBytesCountInvPort1_Type()
)
pm253perfdatacomclientPast15StatOutBytesCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatOutBytesCountInvPort1.setStatus("current")
_Pm253perfdatacomclientPast15StatOutBytesCountPort1_Type = Counter64
_Pm253perfdatacomclientPast15StatOutBytesCountPort1_Object = MibTableColumn
pm253perfdatacomclientPast15StatOutBytesCountPort1 = _Pm253perfdatacomclientPast15StatOutBytesCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 264, 1, 27),
    _Pm253perfdatacomclientPast15StatOutBytesCountPort1_Type()
)
pm253perfdatacomclientPast15StatOutBytesCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatOutBytesCountPort1.setStatus("current")
_Pm253perfdatacomclientPast15StatOutBroadcastCountInvPort1_Type = EkiOnOff
_Pm253perfdatacomclientPast15StatOutBroadcastCountInvPort1_Object = MibTableColumn
pm253perfdatacomclientPast15StatOutBroadcastCountInvPort1 = _Pm253perfdatacomclientPast15StatOutBroadcastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 264, 1, 32),
    _Pm253perfdatacomclientPast15StatOutBroadcastCountInvPort1_Type()
)
pm253perfdatacomclientPast15StatOutBroadcastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatOutBroadcastCountInvPort1.setStatus("current")
_Pm253perfdatacomclientPast15StatOutBroadcastCountPort1_Type = Counter64
_Pm253perfdatacomclientPast15StatOutBroadcastCountPort1_Object = MibTableColumn
pm253perfdatacomclientPast15StatOutBroadcastCountPort1 = _Pm253perfdatacomclientPast15StatOutBroadcastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 264, 1, 33),
    _Pm253perfdatacomclientPast15StatOutBroadcastCountPort1_Type()
)
pm253perfdatacomclientPast15StatOutBroadcastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatOutBroadcastCountPort1.setStatus("current")
_Pm253perfdatacomclientPast15StatOutMulticastCountInvPort1_Type = EkiOnOff
_Pm253perfdatacomclientPast15StatOutMulticastCountInvPort1_Object = MibTableColumn
pm253perfdatacomclientPast15StatOutMulticastCountInvPort1 = _Pm253perfdatacomclientPast15StatOutMulticastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 264, 1, 34),
    _Pm253perfdatacomclientPast15StatOutMulticastCountInvPort1_Type()
)
pm253perfdatacomclientPast15StatOutMulticastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatOutMulticastCountInvPort1.setStatus("current")
_Pm253perfdatacomclientPast15StatOutMulticastCountPort1_Type = Counter64
_Pm253perfdatacomclientPast15StatOutMulticastCountPort1_Object = MibTableColumn
pm253perfdatacomclientPast15StatOutMulticastCountPort1 = _Pm253perfdatacomclientPast15StatOutMulticastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 264, 1, 35),
    _Pm253perfdatacomclientPast15StatOutMulticastCountPort1_Type()
)
pm253perfdatacomclientPast15StatOutMulticastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatOutMulticastCountPort1.setStatus("current")
_Pm253perfdatacomclientPast15StatOutUnicastCountInvPort1_Type = EkiOnOff
_Pm253perfdatacomclientPast15StatOutUnicastCountInvPort1_Object = MibTableColumn
pm253perfdatacomclientPast15StatOutUnicastCountInvPort1 = _Pm253perfdatacomclientPast15StatOutUnicastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 264, 1, 42),
    _Pm253perfdatacomclientPast15StatOutUnicastCountInvPort1_Type()
)
pm253perfdatacomclientPast15StatOutUnicastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatOutUnicastCountInvPort1.setStatus("current")
_Pm253perfdatacomclientPast15StatOutUnicastCountPort1_Type = Counter64
_Pm253perfdatacomclientPast15StatOutUnicastCountPort1_Object = MibTableColumn
pm253perfdatacomclientPast15StatOutUnicastCountPort1 = _Pm253perfdatacomclientPast15StatOutUnicastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 264, 1, 43),
    _Pm253perfdatacomclientPast15StatOutUnicastCountPort1_Type()
)
pm253perfdatacomclientPast15StatOutUnicastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatOutUnicastCountPort1.setStatus("current")
_Pm253perfdatacomclientPast15StatOutNonunicastCountInvPort1_Type = EkiOnOff
_Pm253perfdatacomclientPast15StatOutNonunicastCountInvPort1_Object = MibTableColumn
pm253perfdatacomclientPast15StatOutNonunicastCountInvPort1 = _Pm253perfdatacomclientPast15StatOutNonunicastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 264, 1, 44),
    _Pm253perfdatacomclientPast15StatOutNonunicastCountInvPort1_Type()
)
pm253perfdatacomclientPast15StatOutNonunicastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatOutNonunicastCountInvPort1.setStatus("current")
_Pm253perfdatacomclientPast15StatOutNonunicastCountPort1_Type = Counter64
_Pm253perfdatacomclientPast15StatOutNonunicastCountPort1_Object = MibTableColumn
pm253perfdatacomclientPast15StatOutNonunicastCountPort1 = _Pm253perfdatacomclientPast15StatOutNonunicastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 264, 1, 45),
    _Pm253perfdatacomclientPast15StatOutNonunicastCountPort1_Type()
)
pm253perfdatacomclientPast15StatOutNonunicastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatOutNonunicastCountPort1.setStatus("current")
_Pm253PerfDatacomClientPast15StatHistoryPort2Table_Object = MibTable
pm253PerfDatacomClientPast15StatHistoryPort2Table = _Pm253PerfDatacomClientPast15StatHistoryPort2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 265)
)
if mibBuilder.loadTexts:
    pm253PerfDatacomClientPast15StatHistoryPort2Table.setStatus("current")
_Pm253PerfDatacomClientPast15StatHistoryPort2Entry_Object = MibTableRow
pm253PerfDatacomClientPast15StatHistoryPort2Entry = _Pm253PerfDatacomClientPast15StatHistoryPort2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 265, 1)
)
pm253PerfDatacomClientPast15StatHistoryPort2Entry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253PerfDatacomClientPast15StatHistoryPort2Index"),
)
if mibBuilder.loadTexts:
    pm253PerfDatacomClientPast15StatHistoryPort2Entry.setStatus("current")


class _Pm253PerfDatacomClientPast15StatHistoryPort2Index_Type(Integer32):
    """Custom type pm253PerfDatacomClientPast15StatHistoryPort2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253PerfDatacomClientPast15StatHistoryPort2Index_Type.__name__ = "Integer32"
_Pm253PerfDatacomClientPast15StatHistoryPort2Index_Object = MibTableColumn
pm253PerfDatacomClientPast15StatHistoryPort2Index = _Pm253PerfDatacomClientPast15StatHistoryPort2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 265, 1, 1),
    _Pm253PerfDatacomClientPast15StatHistoryPort2Index_Type()
)
pm253PerfDatacomClientPast15StatHistoryPort2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfDatacomClientPast15StatHistoryPort2Index.setStatus("current")
_Pm253perfdatacomclientPast15StatInBytesCountInvPort2_Type = EkiOnOff
_Pm253perfdatacomclientPast15StatInBytesCountInvPort2_Object = MibTableColumn
pm253perfdatacomclientPast15StatInBytesCountInvPort2 = _Pm253perfdatacomclientPast15StatInBytesCountInvPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 265, 1, 2),
    _Pm253perfdatacomclientPast15StatInBytesCountInvPort2_Type()
)
pm253perfdatacomclientPast15StatInBytesCountInvPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatInBytesCountInvPort2.setStatus("current")
_Pm253perfdatacomclientPast15StatInBytesCountPort2_Type = Counter64
_Pm253perfdatacomclientPast15StatInBytesCountPort2_Object = MibTableColumn
pm253perfdatacomclientPast15StatInBytesCountPort2 = _Pm253perfdatacomclientPast15StatInBytesCountPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 265, 1, 3),
    _Pm253perfdatacomclientPast15StatInBytesCountPort2_Type()
)
pm253perfdatacomclientPast15StatInBytesCountPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatInBytesCountPort2.setStatus("current")
_Pm253perfdatacomclientPast15StatInCrcCountInvPort2_Type = EkiOnOff
_Pm253perfdatacomclientPast15StatInCrcCountInvPort2_Object = MibTableColumn
pm253perfdatacomclientPast15StatInCrcCountInvPort2 = _Pm253perfdatacomclientPast15StatInCrcCountInvPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 265, 1, 4),
    _Pm253perfdatacomclientPast15StatInCrcCountInvPort2_Type()
)
pm253perfdatacomclientPast15StatInCrcCountInvPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatInCrcCountInvPort2.setStatus("current")
_Pm253perfdatacomclientPast15StatInCrcCountPort2_Type = Counter64
_Pm253perfdatacomclientPast15StatInCrcCountPort2_Object = MibTableColumn
pm253perfdatacomclientPast15StatInCrcCountPort2 = _Pm253perfdatacomclientPast15StatInCrcCountPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 265, 1, 5),
    _Pm253perfdatacomclientPast15StatInCrcCountPort2_Type()
)
pm253perfdatacomclientPast15StatInCrcCountPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatInCrcCountPort2.setStatus("current")
_Pm253perfdatacomclientPast15StatInBroadcastCountInvPort2_Type = EkiOnOff
_Pm253perfdatacomclientPast15StatInBroadcastCountInvPort2_Object = MibTableColumn
pm253perfdatacomclientPast15StatInBroadcastCountInvPort2 = _Pm253perfdatacomclientPast15StatInBroadcastCountInvPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 265, 1, 8),
    _Pm253perfdatacomclientPast15StatInBroadcastCountInvPort2_Type()
)
pm253perfdatacomclientPast15StatInBroadcastCountInvPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatInBroadcastCountInvPort2.setStatus("current")
_Pm253perfdatacomclientPast15StatInBroadcastCountPort2_Type = Counter64
_Pm253perfdatacomclientPast15StatInBroadcastCountPort2_Object = MibTableColumn
pm253perfdatacomclientPast15StatInBroadcastCountPort2 = _Pm253perfdatacomclientPast15StatInBroadcastCountPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 265, 1, 9),
    _Pm253perfdatacomclientPast15StatInBroadcastCountPort2_Type()
)
pm253perfdatacomclientPast15StatInBroadcastCountPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatInBroadcastCountPort2.setStatus("current")
_Pm253perfdatacomclientPast15StatInMulticastCountInvPort2_Type = EkiOnOff
_Pm253perfdatacomclientPast15StatInMulticastCountInvPort2_Object = MibTableColumn
pm253perfdatacomclientPast15StatInMulticastCountInvPort2 = _Pm253perfdatacomclientPast15StatInMulticastCountInvPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 265, 1, 10),
    _Pm253perfdatacomclientPast15StatInMulticastCountInvPort2_Type()
)
pm253perfdatacomclientPast15StatInMulticastCountInvPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatInMulticastCountInvPort2.setStatus("current")
_Pm253perfdatacomclientPast15StatInMulticastCountPort2_Type = Counter64
_Pm253perfdatacomclientPast15StatInMulticastCountPort2_Object = MibTableColumn
pm253perfdatacomclientPast15StatInMulticastCountPort2 = _Pm253perfdatacomclientPast15StatInMulticastCountPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 265, 1, 11),
    _Pm253perfdatacomclientPast15StatInMulticastCountPort2_Type()
)
pm253perfdatacomclientPast15StatInMulticastCountPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatInMulticastCountPort2.setStatus("current")
_Pm253perfdatacomclientPast15StatInUnicastCountInvPort2_Type = EkiOnOff
_Pm253perfdatacomclientPast15StatInUnicastCountInvPort2_Object = MibTableColumn
pm253perfdatacomclientPast15StatInUnicastCountInvPort2 = _Pm253perfdatacomclientPast15StatInUnicastCountInvPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 265, 1, 20),
    _Pm253perfdatacomclientPast15StatInUnicastCountInvPort2_Type()
)
pm253perfdatacomclientPast15StatInUnicastCountInvPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatInUnicastCountInvPort2.setStatus("current")
_Pm253perfdatacomclientPast15StatInUnicastCountPort2_Type = Counter64
_Pm253perfdatacomclientPast15StatInUnicastCountPort2_Object = MibTableColumn
pm253perfdatacomclientPast15StatInUnicastCountPort2 = _Pm253perfdatacomclientPast15StatInUnicastCountPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 265, 1, 21),
    _Pm253perfdatacomclientPast15StatInUnicastCountPort2_Type()
)
pm253perfdatacomclientPast15StatInUnicastCountPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatInUnicastCountPort2.setStatus("current")
_Pm253perfdatacomclientPast15StatInNonunicastCountInvPort2_Type = EkiOnOff
_Pm253perfdatacomclientPast15StatInNonunicastCountInvPort2_Object = MibTableColumn
pm253perfdatacomclientPast15StatInNonunicastCountInvPort2 = _Pm253perfdatacomclientPast15StatInNonunicastCountInvPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 265, 1, 22),
    _Pm253perfdatacomclientPast15StatInNonunicastCountInvPort2_Type()
)
pm253perfdatacomclientPast15StatInNonunicastCountInvPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatInNonunicastCountInvPort2.setStatus("current")
_Pm253perfdatacomclientPast15StatInNonunicastCountPort2_Type = Counter64
_Pm253perfdatacomclientPast15StatInNonunicastCountPort2_Object = MibTableColumn
pm253perfdatacomclientPast15StatInNonunicastCountPort2 = _Pm253perfdatacomclientPast15StatInNonunicastCountPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 265, 1, 23),
    _Pm253perfdatacomclientPast15StatInNonunicastCountPort2_Type()
)
pm253perfdatacomclientPast15StatInNonunicastCountPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatInNonunicastCountPort2.setStatus("current")
_Pm253perfdatacomclientPast15StatOutBytesCountInvPort2_Type = EkiOnOff
_Pm253perfdatacomclientPast15StatOutBytesCountInvPort2_Object = MibTableColumn
pm253perfdatacomclientPast15StatOutBytesCountInvPort2 = _Pm253perfdatacomclientPast15StatOutBytesCountInvPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 265, 1, 26),
    _Pm253perfdatacomclientPast15StatOutBytesCountInvPort2_Type()
)
pm253perfdatacomclientPast15StatOutBytesCountInvPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatOutBytesCountInvPort2.setStatus("current")
_Pm253perfdatacomclientPast15StatOutBytesCountPort2_Type = Counter64
_Pm253perfdatacomclientPast15StatOutBytesCountPort2_Object = MibTableColumn
pm253perfdatacomclientPast15StatOutBytesCountPort2 = _Pm253perfdatacomclientPast15StatOutBytesCountPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 265, 1, 27),
    _Pm253perfdatacomclientPast15StatOutBytesCountPort2_Type()
)
pm253perfdatacomclientPast15StatOutBytesCountPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatOutBytesCountPort2.setStatus("current")
_Pm253perfdatacomclientPast15StatOutBroadcastCountInvPort2_Type = EkiOnOff
_Pm253perfdatacomclientPast15StatOutBroadcastCountInvPort2_Object = MibTableColumn
pm253perfdatacomclientPast15StatOutBroadcastCountInvPort2 = _Pm253perfdatacomclientPast15StatOutBroadcastCountInvPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 265, 1, 32),
    _Pm253perfdatacomclientPast15StatOutBroadcastCountInvPort2_Type()
)
pm253perfdatacomclientPast15StatOutBroadcastCountInvPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatOutBroadcastCountInvPort2.setStatus("current")
_Pm253perfdatacomclientPast15StatOutBroadcastCountPort2_Type = Counter64
_Pm253perfdatacomclientPast15StatOutBroadcastCountPort2_Object = MibTableColumn
pm253perfdatacomclientPast15StatOutBroadcastCountPort2 = _Pm253perfdatacomclientPast15StatOutBroadcastCountPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 265, 1, 33),
    _Pm253perfdatacomclientPast15StatOutBroadcastCountPort2_Type()
)
pm253perfdatacomclientPast15StatOutBroadcastCountPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatOutBroadcastCountPort2.setStatus("current")
_Pm253perfdatacomclientPast15StatOutMulticastCountInvPort2_Type = EkiOnOff
_Pm253perfdatacomclientPast15StatOutMulticastCountInvPort2_Object = MibTableColumn
pm253perfdatacomclientPast15StatOutMulticastCountInvPort2 = _Pm253perfdatacomclientPast15StatOutMulticastCountInvPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 265, 1, 34),
    _Pm253perfdatacomclientPast15StatOutMulticastCountInvPort2_Type()
)
pm253perfdatacomclientPast15StatOutMulticastCountInvPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatOutMulticastCountInvPort2.setStatus("current")
_Pm253perfdatacomclientPast15StatOutMulticastCountPort2_Type = Counter64
_Pm253perfdatacomclientPast15StatOutMulticastCountPort2_Object = MibTableColumn
pm253perfdatacomclientPast15StatOutMulticastCountPort2 = _Pm253perfdatacomclientPast15StatOutMulticastCountPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 265, 1, 35),
    _Pm253perfdatacomclientPast15StatOutMulticastCountPort2_Type()
)
pm253perfdatacomclientPast15StatOutMulticastCountPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatOutMulticastCountPort2.setStatus("current")
_Pm253perfdatacomclientPast15StatOutUnicastCountInvPort2_Type = EkiOnOff
_Pm253perfdatacomclientPast15StatOutUnicastCountInvPort2_Object = MibTableColumn
pm253perfdatacomclientPast15StatOutUnicastCountInvPort2 = _Pm253perfdatacomclientPast15StatOutUnicastCountInvPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 265, 1, 42),
    _Pm253perfdatacomclientPast15StatOutUnicastCountInvPort2_Type()
)
pm253perfdatacomclientPast15StatOutUnicastCountInvPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatOutUnicastCountInvPort2.setStatus("current")
_Pm253perfdatacomclientPast15StatOutUnicastCountPort2_Type = Counter64
_Pm253perfdatacomclientPast15StatOutUnicastCountPort2_Object = MibTableColumn
pm253perfdatacomclientPast15StatOutUnicastCountPort2 = _Pm253perfdatacomclientPast15StatOutUnicastCountPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 265, 1, 43),
    _Pm253perfdatacomclientPast15StatOutUnicastCountPort2_Type()
)
pm253perfdatacomclientPast15StatOutUnicastCountPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatOutUnicastCountPort2.setStatus("current")
_Pm253perfdatacomclientPast15StatOutNonunicastCountInvPort2_Type = EkiOnOff
_Pm253perfdatacomclientPast15StatOutNonunicastCountInvPort2_Object = MibTableColumn
pm253perfdatacomclientPast15StatOutNonunicastCountInvPort2 = _Pm253perfdatacomclientPast15StatOutNonunicastCountInvPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 265, 1, 44),
    _Pm253perfdatacomclientPast15StatOutNonunicastCountInvPort2_Type()
)
pm253perfdatacomclientPast15StatOutNonunicastCountInvPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatOutNonunicastCountInvPort2.setStatus("current")
_Pm253perfdatacomclientPast15StatOutNonunicastCountPort2_Type = Counter64
_Pm253perfdatacomclientPast15StatOutNonunicastCountPort2_Object = MibTableColumn
pm253perfdatacomclientPast15StatOutNonunicastCountPort2 = _Pm253perfdatacomclientPast15StatOutNonunicastCountPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 265, 1, 45),
    _Pm253perfdatacomclientPast15StatOutNonunicastCountPort2_Type()
)
pm253perfdatacomclientPast15StatOutNonunicastCountPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatOutNonunicastCountPort2.setStatus("current")
_Pm253PerfDatacomClientPast15StatHistoryPort3Table_Object = MibTable
pm253PerfDatacomClientPast15StatHistoryPort3Table = _Pm253PerfDatacomClientPast15StatHistoryPort3Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 266)
)
if mibBuilder.loadTexts:
    pm253PerfDatacomClientPast15StatHistoryPort3Table.setStatus("current")
_Pm253PerfDatacomClientPast15StatHistoryPort3Entry_Object = MibTableRow
pm253PerfDatacomClientPast15StatHistoryPort3Entry = _Pm253PerfDatacomClientPast15StatHistoryPort3Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 266, 1)
)
pm253PerfDatacomClientPast15StatHistoryPort3Entry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253PerfDatacomClientPast15StatHistoryPort3Index"),
)
if mibBuilder.loadTexts:
    pm253PerfDatacomClientPast15StatHistoryPort3Entry.setStatus("current")


class _Pm253PerfDatacomClientPast15StatHistoryPort3Index_Type(Integer32):
    """Custom type pm253PerfDatacomClientPast15StatHistoryPort3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253PerfDatacomClientPast15StatHistoryPort3Index_Type.__name__ = "Integer32"
_Pm253PerfDatacomClientPast15StatHistoryPort3Index_Object = MibTableColumn
pm253PerfDatacomClientPast15StatHistoryPort3Index = _Pm253PerfDatacomClientPast15StatHistoryPort3Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 266, 1, 1),
    _Pm253PerfDatacomClientPast15StatHistoryPort3Index_Type()
)
pm253PerfDatacomClientPast15StatHistoryPort3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfDatacomClientPast15StatHistoryPort3Index.setStatus("current")
_Pm253perfdatacomclientPast15StatInBytesCountInvPort3_Type = EkiOnOff
_Pm253perfdatacomclientPast15StatInBytesCountInvPort3_Object = MibTableColumn
pm253perfdatacomclientPast15StatInBytesCountInvPort3 = _Pm253perfdatacomclientPast15StatInBytesCountInvPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 266, 1, 2),
    _Pm253perfdatacomclientPast15StatInBytesCountInvPort3_Type()
)
pm253perfdatacomclientPast15StatInBytesCountInvPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatInBytesCountInvPort3.setStatus("current")
_Pm253perfdatacomclientPast15StatInBytesCountPort3_Type = Counter64
_Pm253perfdatacomclientPast15StatInBytesCountPort3_Object = MibTableColumn
pm253perfdatacomclientPast15StatInBytesCountPort3 = _Pm253perfdatacomclientPast15StatInBytesCountPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 266, 1, 3),
    _Pm253perfdatacomclientPast15StatInBytesCountPort3_Type()
)
pm253perfdatacomclientPast15StatInBytesCountPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatInBytesCountPort3.setStatus("current")
_Pm253perfdatacomclientPast15StatInCrcCountInvPort3_Type = EkiOnOff
_Pm253perfdatacomclientPast15StatInCrcCountInvPort3_Object = MibTableColumn
pm253perfdatacomclientPast15StatInCrcCountInvPort3 = _Pm253perfdatacomclientPast15StatInCrcCountInvPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 266, 1, 4),
    _Pm253perfdatacomclientPast15StatInCrcCountInvPort3_Type()
)
pm253perfdatacomclientPast15StatInCrcCountInvPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatInCrcCountInvPort3.setStatus("current")
_Pm253perfdatacomclientPast15StatInCrcCountPort3_Type = Counter64
_Pm253perfdatacomclientPast15StatInCrcCountPort3_Object = MibTableColumn
pm253perfdatacomclientPast15StatInCrcCountPort3 = _Pm253perfdatacomclientPast15StatInCrcCountPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 266, 1, 5),
    _Pm253perfdatacomclientPast15StatInCrcCountPort3_Type()
)
pm253perfdatacomclientPast15StatInCrcCountPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatInCrcCountPort3.setStatus("current")
_Pm253perfdatacomclientPast15StatInBroadcastCountInvPort3_Type = EkiOnOff
_Pm253perfdatacomclientPast15StatInBroadcastCountInvPort3_Object = MibTableColumn
pm253perfdatacomclientPast15StatInBroadcastCountInvPort3 = _Pm253perfdatacomclientPast15StatInBroadcastCountInvPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 266, 1, 8),
    _Pm253perfdatacomclientPast15StatInBroadcastCountInvPort3_Type()
)
pm253perfdatacomclientPast15StatInBroadcastCountInvPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatInBroadcastCountInvPort3.setStatus("current")
_Pm253perfdatacomclientPast15StatInBroadcastCountPort3_Type = Counter64
_Pm253perfdatacomclientPast15StatInBroadcastCountPort3_Object = MibTableColumn
pm253perfdatacomclientPast15StatInBroadcastCountPort3 = _Pm253perfdatacomclientPast15StatInBroadcastCountPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 266, 1, 9),
    _Pm253perfdatacomclientPast15StatInBroadcastCountPort3_Type()
)
pm253perfdatacomclientPast15StatInBroadcastCountPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatInBroadcastCountPort3.setStatus("current")
_Pm253perfdatacomclientPast15StatInMulticastCountInvPort3_Type = EkiOnOff
_Pm253perfdatacomclientPast15StatInMulticastCountInvPort3_Object = MibTableColumn
pm253perfdatacomclientPast15StatInMulticastCountInvPort3 = _Pm253perfdatacomclientPast15StatInMulticastCountInvPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 266, 1, 10),
    _Pm253perfdatacomclientPast15StatInMulticastCountInvPort3_Type()
)
pm253perfdatacomclientPast15StatInMulticastCountInvPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatInMulticastCountInvPort3.setStatus("current")
_Pm253perfdatacomclientPast15StatInMulticastCountPort3_Type = Counter64
_Pm253perfdatacomclientPast15StatInMulticastCountPort3_Object = MibTableColumn
pm253perfdatacomclientPast15StatInMulticastCountPort3 = _Pm253perfdatacomclientPast15StatInMulticastCountPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 266, 1, 11),
    _Pm253perfdatacomclientPast15StatInMulticastCountPort3_Type()
)
pm253perfdatacomclientPast15StatInMulticastCountPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatInMulticastCountPort3.setStatus("current")
_Pm253perfdatacomclientPast15StatInUnicastCountInvPort3_Type = EkiOnOff
_Pm253perfdatacomclientPast15StatInUnicastCountInvPort3_Object = MibTableColumn
pm253perfdatacomclientPast15StatInUnicastCountInvPort3 = _Pm253perfdatacomclientPast15StatInUnicastCountInvPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 266, 1, 20),
    _Pm253perfdatacomclientPast15StatInUnicastCountInvPort3_Type()
)
pm253perfdatacomclientPast15StatInUnicastCountInvPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatInUnicastCountInvPort3.setStatus("current")
_Pm253perfdatacomclientPast15StatInUnicastCountPort3_Type = Counter64
_Pm253perfdatacomclientPast15StatInUnicastCountPort3_Object = MibTableColumn
pm253perfdatacomclientPast15StatInUnicastCountPort3 = _Pm253perfdatacomclientPast15StatInUnicastCountPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 266, 1, 21),
    _Pm253perfdatacomclientPast15StatInUnicastCountPort3_Type()
)
pm253perfdatacomclientPast15StatInUnicastCountPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatInUnicastCountPort3.setStatus("current")
_Pm253perfdatacomclientPast15StatInNonunicastCountInvPort3_Type = EkiOnOff
_Pm253perfdatacomclientPast15StatInNonunicastCountInvPort3_Object = MibTableColumn
pm253perfdatacomclientPast15StatInNonunicastCountInvPort3 = _Pm253perfdatacomclientPast15StatInNonunicastCountInvPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 266, 1, 22),
    _Pm253perfdatacomclientPast15StatInNonunicastCountInvPort3_Type()
)
pm253perfdatacomclientPast15StatInNonunicastCountInvPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatInNonunicastCountInvPort3.setStatus("current")
_Pm253perfdatacomclientPast15StatInNonunicastCountPort3_Type = Counter64
_Pm253perfdatacomclientPast15StatInNonunicastCountPort3_Object = MibTableColumn
pm253perfdatacomclientPast15StatInNonunicastCountPort3 = _Pm253perfdatacomclientPast15StatInNonunicastCountPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 266, 1, 23),
    _Pm253perfdatacomclientPast15StatInNonunicastCountPort3_Type()
)
pm253perfdatacomclientPast15StatInNonunicastCountPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatInNonunicastCountPort3.setStatus("current")
_Pm253perfdatacomclientPast15StatOutBytesCountInvPort3_Type = EkiOnOff
_Pm253perfdatacomclientPast15StatOutBytesCountInvPort3_Object = MibTableColumn
pm253perfdatacomclientPast15StatOutBytesCountInvPort3 = _Pm253perfdatacomclientPast15StatOutBytesCountInvPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 266, 1, 26),
    _Pm253perfdatacomclientPast15StatOutBytesCountInvPort3_Type()
)
pm253perfdatacomclientPast15StatOutBytesCountInvPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatOutBytesCountInvPort3.setStatus("current")
_Pm253perfdatacomclientPast15StatOutBytesCountPort3_Type = Counter64
_Pm253perfdatacomclientPast15StatOutBytesCountPort3_Object = MibTableColumn
pm253perfdatacomclientPast15StatOutBytesCountPort3 = _Pm253perfdatacomclientPast15StatOutBytesCountPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 266, 1, 27),
    _Pm253perfdatacomclientPast15StatOutBytesCountPort3_Type()
)
pm253perfdatacomclientPast15StatOutBytesCountPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatOutBytesCountPort3.setStatus("current")
_Pm253perfdatacomclientPast15StatOutBroadcastCountInvPort3_Type = EkiOnOff
_Pm253perfdatacomclientPast15StatOutBroadcastCountInvPort3_Object = MibTableColumn
pm253perfdatacomclientPast15StatOutBroadcastCountInvPort3 = _Pm253perfdatacomclientPast15StatOutBroadcastCountInvPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 266, 1, 32),
    _Pm253perfdatacomclientPast15StatOutBroadcastCountInvPort3_Type()
)
pm253perfdatacomclientPast15StatOutBroadcastCountInvPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatOutBroadcastCountInvPort3.setStatus("current")
_Pm253perfdatacomclientPast15StatOutBroadcastCountPort3_Type = Counter64
_Pm253perfdatacomclientPast15StatOutBroadcastCountPort3_Object = MibTableColumn
pm253perfdatacomclientPast15StatOutBroadcastCountPort3 = _Pm253perfdatacomclientPast15StatOutBroadcastCountPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 266, 1, 33),
    _Pm253perfdatacomclientPast15StatOutBroadcastCountPort3_Type()
)
pm253perfdatacomclientPast15StatOutBroadcastCountPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatOutBroadcastCountPort3.setStatus("current")
_Pm253perfdatacomclientPast15StatOutMulticastCountInvPort3_Type = EkiOnOff
_Pm253perfdatacomclientPast15StatOutMulticastCountInvPort3_Object = MibTableColumn
pm253perfdatacomclientPast15StatOutMulticastCountInvPort3 = _Pm253perfdatacomclientPast15StatOutMulticastCountInvPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 266, 1, 34),
    _Pm253perfdatacomclientPast15StatOutMulticastCountInvPort3_Type()
)
pm253perfdatacomclientPast15StatOutMulticastCountInvPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatOutMulticastCountInvPort3.setStatus("current")
_Pm253perfdatacomclientPast15StatOutMulticastCountPort3_Type = Counter64
_Pm253perfdatacomclientPast15StatOutMulticastCountPort3_Object = MibTableColumn
pm253perfdatacomclientPast15StatOutMulticastCountPort3 = _Pm253perfdatacomclientPast15StatOutMulticastCountPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 266, 1, 35),
    _Pm253perfdatacomclientPast15StatOutMulticastCountPort3_Type()
)
pm253perfdatacomclientPast15StatOutMulticastCountPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatOutMulticastCountPort3.setStatus("current")
_Pm253perfdatacomclientPast15StatOutUnicastCountInvPort3_Type = EkiOnOff
_Pm253perfdatacomclientPast15StatOutUnicastCountInvPort3_Object = MibTableColumn
pm253perfdatacomclientPast15StatOutUnicastCountInvPort3 = _Pm253perfdatacomclientPast15StatOutUnicastCountInvPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 266, 1, 42),
    _Pm253perfdatacomclientPast15StatOutUnicastCountInvPort3_Type()
)
pm253perfdatacomclientPast15StatOutUnicastCountInvPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatOutUnicastCountInvPort3.setStatus("current")
_Pm253perfdatacomclientPast15StatOutUnicastCountPort3_Type = Counter64
_Pm253perfdatacomclientPast15StatOutUnicastCountPort3_Object = MibTableColumn
pm253perfdatacomclientPast15StatOutUnicastCountPort3 = _Pm253perfdatacomclientPast15StatOutUnicastCountPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 266, 1, 43),
    _Pm253perfdatacomclientPast15StatOutUnicastCountPort3_Type()
)
pm253perfdatacomclientPast15StatOutUnicastCountPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatOutUnicastCountPort3.setStatus("current")
_Pm253perfdatacomclientPast15StatOutNonunicastCountInvPort3_Type = EkiOnOff
_Pm253perfdatacomclientPast15StatOutNonunicastCountInvPort3_Object = MibTableColumn
pm253perfdatacomclientPast15StatOutNonunicastCountInvPort3 = _Pm253perfdatacomclientPast15StatOutNonunicastCountInvPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 266, 1, 44),
    _Pm253perfdatacomclientPast15StatOutNonunicastCountInvPort3_Type()
)
pm253perfdatacomclientPast15StatOutNonunicastCountInvPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatOutNonunicastCountInvPort3.setStatus("current")
_Pm253perfdatacomclientPast15StatOutNonunicastCountPort3_Type = Counter64
_Pm253perfdatacomclientPast15StatOutNonunicastCountPort3_Object = MibTableColumn
pm253perfdatacomclientPast15StatOutNonunicastCountPort3 = _Pm253perfdatacomclientPast15StatOutNonunicastCountPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 266, 1, 45),
    _Pm253perfdatacomclientPast15StatOutNonunicastCountPort3_Type()
)
pm253perfdatacomclientPast15StatOutNonunicastCountPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast15StatOutNonunicastCountPort3.setStatus("current")
_Pm253PerfDatacomClientCurrent24StatTable_Object = MibTable
pm253PerfDatacomClientCurrent24StatTable = _Pm253PerfDatacomClientCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 272)
)
if mibBuilder.loadTexts:
    pm253PerfDatacomClientCurrent24StatTable.setStatus("current")
_Pm253PerfDatacomClientCurrent24StatEntry_Object = MibTableRow
pm253PerfDatacomClientCurrent24StatEntry = _Pm253PerfDatacomClientCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 272, 1)
)
pm253PerfDatacomClientCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253PerfDatacomClientCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pm253PerfDatacomClientCurrent24StatEntry.setStatus("current")


class _Pm253PerfDatacomClientCurrent24StatIndex_Type(Integer32):
    """Custom type pm253PerfDatacomClientCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253PerfDatacomClientCurrent24StatIndex_Type.__name__ = "Integer32"
_Pm253PerfDatacomClientCurrent24StatIndex_Object = MibTableColumn
pm253PerfDatacomClientCurrent24StatIndex = _Pm253PerfDatacomClientCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 272, 1, 1),
    _Pm253PerfDatacomClientCurrent24StatIndex_Type()
)
pm253PerfDatacomClientCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfDatacomClientCurrent24StatIndex.setStatus("current")
_Pm253perfdatacomclientCurrent24StatInBytesCountInvPortn_Type = EkiOnOff
_Pm253perfdatacomclientCurrent24StatInBytesCountInvPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent24StatInBytesCountInvPortn = _Pm253perfdatacomclientCurrent24StatInBytesCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 272, 1, 2),
    _Pm253perfdatacomclientCurrent24StatInBytesCountInvPortn_Type()
)
pm253perfdatacomclientCurrent24StatInBytesCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent24StatInBytesCountInvPortn.setStatus("current")
_Pm253perfdatacomclientCurrent24StatInBytesCountPortn_Type = Counter64
_Pm253perfdatacomclientCurrent24StatInBytesCountPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent24StatInBytesCountPortn = _Pm253perfdatacomclientCurrent24StatInBytesCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 272, 1, 3),
    _Pm253perfdatacomclientCurrent24StatInBytesCountPortn_Type()
)
pm253perfdatacomclientCurrent24StatInBytesCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent24StatInBytesCountPortn.setStatus("current")
_Pm253perfdatacomclientCurrent24StatInCrcCountInvPortn_Type = EkiOnOff
_Pm253perfdatacomclientCurrent24StatInCrcCountInvPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent24StatInCrcCountInvPortn = _Pm253perfdatacomclientCurrent24StatInCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 272, 1, 4),
    _Pm253perfdatacomclientCurrent24StatInCrcCountInvPortn_Type()
)
pm253perfdatacomclientCurrent24StatInCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent24StatInCrcCountInvPortn.setStatus("current")
_Pm253perfdatacomclientCurrent24StatInCrcCountPortn_Type = Counter64
_Pm253perfdatacomclientCurrent24StatInCrcCountPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent24StatInCrcCountPortn = _Pm253perfdatacomclientCurrent24StatInCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 272, 1, 5),
    _Pm253perfdatacomclientCurrent24StatInCrcCountPortn_Type()
)
pm253perfdatacomclientCurrent24StatInCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent24StatInCrcCountPortn.setStatus("current")
_Pm253perfdatacomclientCurrent24StatInBroadcastCountInvPortn_Type = EkiOnOff
_Pm253perfdatacomclientCurrent24StatInBroadcastCountInvPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent24StatInBroadcastCountInvPortn = _Pm253perfdatacomclientCurrent24StatInBroadcastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 272, 1, 8),
    _Pm253perfdatacomclientCurrent24StatInBroadcastCountInvPortn_Type()
)
pm253perfdatacomclientCurrent24StatInBroadcastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent24StatInBroadcastCountInvPortn.setStatus("current")
_Pm253perfdatacomclientCurrent24StatInBroadcastCountPortn_Type = Counter64
_Pm253perfdatacomclientCurrent24StatInBroadcastCountPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent24StatInBroadcastCountPortn = _Pm253perfdatacomclientCurrent24StatInBroadcastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 272, 1, 9),
    _Pm253perfdatacomclientCurrent24StatInBroadcastCountPortn_Type()
)
pm253perfdatacomclientCurrent24StatInBroadcastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent24StatInBroadcastCountPortn.setStatus("current")
_Pm253perfdatacomclientCurrent24StatInMulticastCountInvPortn_Type = EkiOnOff
_Pm253perfdatacomclientCurrent24StatInMulticastCountInvPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent24StatInMulticastCountInvPortn = _Pm253perfdatacomclientCurrent24StatInMulticastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 272, 1, 10),
    _Pm253perfdatacomclientCurrent24StatInMulticastCountInvPortn_Type()
)
pm253perfdatacomclientCurrent24StatInMulticastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent24StatInMulticastCountInvPortn.setStatus("current")
_Pm253perfdatacomclientCurrent24StatInMulticastCountPortn_Type = Counter64
_Pm253perfdatacomclientCurrent24StatInMulticastCountPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent24StatInMulticastCountPortn = _Pm253perfdatacomclientCurrent24StatInMulticastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 272, 1, 11),
    _Pm253perfdatacomclientCurrent24StatInMulticastCountPortn_Type()
)
pm253perfdatacomclientCurrent24StatInMulticastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent24StatInMulticastCountPortn.setStatus("current")
_Pm253perfdatacomclientCurrent24StatInUnicastCountInvPortn_Type = EkiOnOff
_Pm253perfdatacomclientCurrent24StatInUnicastCountInvPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent24StatInUnicastCountInvPortn = _Pm253perfdatacomclientCurrent24StatInUnicastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 272, 1, 20),
    _Pm253perfdatacomclientCurrent24StatInUnicastCountInvPortn_Type()
)
pm253perfdatacomclientCurrent24StatInUnicastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent24StatInUnicastCountInvPortn.setStatus("current")
_Pm253perfdatacomclientCurrent24StatInUnicastCountPortn_Type = Counter64
_Pm253perfdatacomclientCurrent24StatInUnicastCountPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent24StatInUnicastCountPortn = _Pm253perfdatacomclientCurrent24StatInUnicastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 272, 1, 21),
    _Pm253perfdatacomclientCurrent24StatInUnicastCountPortn_Type()
)
pm253perfdatacomclientCurrent24StatInUnicastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent24StatInUnicastCountPortn.setStatus("current")
_Pm253perfdatacomclientCurrent24StatInNonunicastCountInvPortn_Type = EkiOnOff
_Pm253perfdatacomclientCurrent24StatInNonunicastCountInvPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent24StatInNonunicastCountInvPortn = _Pm253perfdatacomclientCurrent24StatInNonunicastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 272, 1, 22),
    _Pm253perfdatacomclientCurrent24StatInNonunicastCountInvPortn_Type()
)
pm253perfdatacomclientCurrent24StatInNonunicastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent24StatInNonunicastCountInvPortn.setStatus("current")
_Pm253perfdatacomclientCurrent24StatInNonunicastCountPortn_Type = Counter64
_Pm253perfdatacomclientCurrent24StatInNonunicastCountPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent24StatInNonunicastCountPortn = _Pm253perfdatacomclientCurrent24StatInNonunicastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 272, 1, 23),
    _Pm253perfdatacomclientCurrent24StatInNonunicastCountPortn_Type()
)
pm253perfdatacomclientCurrent24StatInNonunicastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent24StatInNonunicastCountPortn.setStatus("current")
_Pm253perfdatacomclientCurrent24StatOutBytesCountInvPortn_Type = EkiOnOff
_Pm253perfdatacomclientCurrent24StatOutBytesCountInvPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent24StatOutBytesCountInvPortn = _Pm253perfdatacomclientCurrent24StatOutBytesCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 272, 1, 26),
    _Pm253perfdatacomclientCurrent24StatOutBytesCountInvPortn_Type()
)
pm253perfdatacomclientCurrent24StatOutBytesCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent24StatOutBytesCountInvPortn.setStatus("current")
_Pm253perfdatacomclientCurrent24StatOutBytesCountPortn_Type = Counter64
_Pm253perfdatacomclientCurrent24StatOutBytesCountPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent24StatOutBytesCountPortn = _Pm253perfdatacomclientCurrent24StatOutBytesCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 272, 1, 27),
    _Pm253perfdatacomclientCurrent24StatOutBytesCountPortn_Type()
)
pm253perfdatacomclientCurrent24StatOutBytesCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent24StatOutBytesCountPortn.setStatus("current")
_Pm253perfdatacomclientCurrent24StatOutBroadcastCountInvPortn_Type = EkiOnOff
_Pm253perfdatacomclientCurrent24StatOutBroadcastCountInvPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent24StatOutBroadcastCountInvPortn = _Pm253perfdatacomclientCurrent24StatOutBroadcastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 272, 1, 32),
    _Pm253perfdatacomclientCurrent24StatOutBroadcastCountInvPortn_Type()
)
pm253perfdatacomclientCurrent24StatOutBroadcastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent24StatOutBroadcastCountInvPortn.setStatus("current")
_Pm253perfdatacomclientCurrent24StatOutBroadcastCountPortn_Type = Counter64
_Pm253perfdatacomclientCurrent24StatOutBroadcastCountPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent24StatOutBroadcastCountPortn = _Pm253perfdatacomclientCurrent24StatOutBroadcastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 272, 1, 33),
    _Pm253perfdatacomclientCurrent24StatOutBroadcastCountPortn_Type()
)
pm253perfdatacomclientCurrent24StatOutBroadcastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent24StatOutBroadcastCountPortn.setStatus("current")
_Pm253perfdatacomclientCurrent24StatOutMulticastCountInvPortn_Type = EkiOnOff
_Pm253perfdatacomclientCurrent24StatOutMulticastCountInvPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent24StatOutMulticastCountInvPortn = _Pm253perfdatacomclientCurrent24StatOutMulticastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 272, 1, 34),
    _Pm253perfdatacomclientCurrent24StatOutMulticastCountInvPortn_Type()
)
pm253perfdatacomclientCurrent24StatOutMulticastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent24StatOutMulticastCountInvPortn.setStatus("current")
_Pm253perfdatacomclientCurrent24StatOutMulticastCountPortn_Type = Counter64
_Pm253perfdatacomclientCurrent24StatOutMulticastCountPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent24StatOutMulticastCountPortn = _Pm253perfdatacomclientCurrent24StatOutMulticastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 272, 1, 35),
    _Pm253perfdatacomclientCurrent24StatOutMulticastCountPortn_Type()
)
pm253perfdatacomclientCurrent24StatOutMulticastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent24StatOutMulticastCountPortn.setStatus("current")
_Pm253perfdatacomclientCurrent24StatOutUnicastCountInvPortn_Type = EkiOnOff
_Pm253perfdatacomclientCurrent24StatOutUnicastCountInvPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent24StatOutUnicastCountInvPortn = _Pm253perfdatacomclientCurrent24StatOutUnicastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 272, 1, 42),
    _Pm253perfdatacomclientCurrent24StatOutUnicastCountInvPortn_Type()
)
pm253perfdatacomclientCurrent24StatOutUnicastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent24StatOutUnicastCountInvPortn.setStatus("current")
_Pm253perfdatacomclientCurrent24StatOutUnicastCountPortn_Type = Counter64
_Pm253perfdatacomclientCurrent24StatOutUnicastCountPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent24StatOutUnicastCountPortn = _Pm253perfdatacomclientCurrent24StatOutUnicastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 272, 1, 43),
    _Pm253perfdatacomclientCurrent24StatOutUnicastCountPortn_Type()
)
pm253perfdatacomclientCurrent24StatOutUnicastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent24StatOutUnicastCountPortn.setStatus("current")
_Pm253perfdatacomclientCurrent24StatOutNonunicastCountInvPortn_Type = EkiOnOff
_Pm253perfdatacomclientCurrent24StatOutNonunicastCountInvPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent24StatOutNonunicastCountInvPortn = _Pm253perfdatacomclientCurrent24StatOutNonunicastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 272, 1, 44),
    _Pm253perfdatacomclientCurrent24StatOutNonunicastCountInvPortn_Type()
)
pm253perfdatacomclientCurrent24StatOutNonunicastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent24StatOutNonunicastCountInvPortn.setStatus("current")
_Pm253perfdatacomclientCurrent24StatOutNonunicastCountPortn_Type = Counter64
_Pm253perfdatacomclientCurrent24StatOutNonunicastCountPortn_Object = MibTableColumn
pm253perfdatacomclientCurrent24StatOutNonunicastCountPortn = _Pm253perfdatacomclientCurrent24StatOutNonunicastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 272, 1, 45),
    _Pm253perfdatacomclientCurrent24StatOutNonunicastCountPortn_Type()
)
pm253perfdatacomclientCurrent24StatOutNonunicastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientCurrent24StatOutNonunicastCountPortn.setStatus("current")
_Pm253PerfDatacomClientPast24StatHistoryPort1Table_Object = MibTable
pm253PerfDatacomClientPast24StatHistoryPort1Table = _Pm253PerfDatacomClientPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 280)
)
if mibBuilder.loadTexts:
    pm253PerfDatacomClientPast24StatHistoryPort1Table.setStatus("current")
_Pm253PerfDatacomClientPast24StatHistoryPort1Entry_Object = MibTableRow
pm253PerfDatacomClientPast24StatHistoryPort1Entry = _Pm253PerfDatacomClientPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 280, 1)
)
pm253PerfDatacomClientPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253PerfDatacomClientPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm253PerfDatacomClientPast24StatHistoryPort1Entry.setStatus("current")


class _Pm253PerfDatacomClientPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pm253PerfDatacomClientPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253PerfDatacomClientPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm253PerfDatacomClientPast24StatHistoryPort1Index_Object = MibTableColumn
pm253PerfDatacomClientPast24StatHistoryPort1Index = _Pm253PerfDatacomClientPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 280, 1, 1),
    _Pm253PerfDatacomClientPast24StatHistoryPort1Index_Type()
)
pm253PerfDatacomClientPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfDatacomClientPast24StatHistoryPort1Index.setStatus("current")
_Pm253perfdatacomclientPast24StatInBytesCountInvPort1_Type = EkiOnOff
_Pm253perfdatacomclientPast24StatInBytesCountInvPort1_Object = MibTableColumn
pm253perfdatacomclientPast24StatInBytesCountInvPort1 = _Pm253perfdatacomclientPast24StatInBytesCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 280, 1, 2),
    _Pm253perfdatacomclientPast24StatInBytesCountInvPort1_Type()
)
pm253perfdatacomclientPast24StatInBytesCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatInBytesCountInvPort1.setStatus("current")
_Pm253perfdatacomclientPast24StatInBytesCountPort1_Type = Counter64
_Pm253perfdatacomclientPast24StatInBytesCountPort1_Object = MibTableColumn
pm253perfdatacomclientPast24StatInBytesCountPort1 = _Pm253perfdatacomclientPast24StatInBytesCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 280, 1, 3),
    _Pm253perfdatacomclientPast24StatInBytesCountPort1_Type()
)
pm253perfdatacomclientPast24StatInBytesCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatInBytesCountPort1.setStatus("current")
_Pm253perfdatacomclientPast24StatInCrcCountInvPort1_Type = EkiOnOff
_Pm253perfdatacomclientPast24StatInCrcCountInvPort1_Object = MibTableColumn
pm253perfdatacomclientPast24StatInCrcCountInvPort1 = _Pm253perfdatacomclientPast24StatInCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 280, 1, 4),
    _Pm253perfdatacomclientPast24StatInCrcCountInvPort1_Type()
)
pm253perfdatacomclientPast24StatInCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatInCrcCountInvPort1.setStatus("current")
_Pm253perfdatacomclientPast24StatInCrcCountPort1_Type = Counter64
_Pm253perfdatacomclientPast24StatInCrcCountPort1_Object = MibTableColumn
pm253perfdatacomclientPast24StatInCrcCountPort1 = _Pm253perfdatacomclientPast24StatInCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 280, 1, 5),
    _Pm253perfdatacomclientPast24StatInCrcCountPort1_Type()
)
pm253perfdatacomclientPast24StatInCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatInCrcCountPort1.setStatus("current")
_Pm253perfdatacomclientPast24StatInBroadcastCountInvPort1_Type = EkiOnOff
_Pm253perfdatacomclientPast24StatInBroadcastCountInvPort1_Object = MibTableColumn
pm253perfdatacomclientPast24StatInBroadcastCountInvPort1 = _Pm253perfdatacomclientPast24StatInBroadcastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 280, 1, 8),
    _Pm253perfdatacomclientPast24StatInBroadcastCountInvPort1_Type()
)
pm253perfdatacomclientPast24StatInBroadcastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatInBroadcastCountInvPort1.setStatus("current")
_Pm253perfdatacomclientPast24StatInBroadcastCountPort1_Type = Counter64
_Pm253perfdatacomclientPast24StatInBroadcastCountPort1_Object = MibTableColumn
pm253perfdatacomclientPast24StatInBroadcastCountPort1 = _Pm253perfdatacomclientPast24StatInBroadcastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 280, 1, 9),
    _Pm253perfdatacomclientPast24StatInBroadcastCountPort1_Type()
)
pm253perfdatacomclientPast24StatInBroadcastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatInBroadcastCountPort1.setStatus("current")
_Pm253perfdatacomclientPast24StatInMulticastCountInvPort1_Type = EkiOnOff
_Pm253perfdatacomclientPast24StatInMulticastCountInvPort1_Object = MibTableColumn
pm253perfdatacomclientPast24StatInMulticastCountInvPort1 = _Pm253perfdatacomclientPast24StatInMulticastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 280, 1, 10),
    _Pm253perfdatacomclientPast24StatInMulticastCountInvPort1_Type()
)
pm253perfdatacomclientPast24StatInMulticastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatInMulticastCountInvPort1.setStatus("current")
_Pm253perfdatacomclientPast24StatInMulticastCountPort1_Type = Counter64
_Pm253perfdatacomclientPast24StatInMulticastCountPort1_Object = MibTableColumn
pm253perfdatacomclientPast24StatInMulticastCountPort1 = _Pm253perfdatacomclientPast24StatInMulticastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 280, 1, 11),
    _Pm253perfdatacomclientPast24StatInMulticastCountPort1_Type()
)
pm253perfdatacomclientPast24StatInMulticastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatInMulticastCountPort1.setStatus("current")
_Pm253perfdatacomclientPast24StatInUnicastCountInvPort1_Type = EkiOnOff
_Pm253perfdatacomclientPast24StatInUnicastCountInvPort1_Object = MibTableColumn
pm253perfdatacomclientPast24StatInUnicastCountInvPort1 = _Pm253perfdatacomclientPast24StatInUnicastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 280, 1, 20),
    _Pm253perfdatacomclientPast24StatInUnicastCountInvPort1_Type()
)
pm253perfdatacomclientPast24StatInUnicastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatInUnicastCountInvPort1.setStatus("current")
_Pm253perfdatacomclientPast24StatInUnicastCountPort1_Type = Counter64
_Pm253perfdatacomclientPast24StatInUnicastCountPort1_Object = MibTableColumn
pm253perfdatacomclientPast24StatInUnicastCountPort1 = _Pm253perfdatacomclientPast24StatInUnicastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 280, 1, 21),
    _Pm253perfdatacomclientPast24StatInUnicastCountPort1_Type()
)
pm253perfdatacomclientPast24StatInUnicastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatInUnicastCountPort1.setStatus("current")
_Pm253perfdatacomclientPast24StatInNonunicastCountInvPort1_Type = EkiOnOff
_Pm253perfdatacomclientPast24StatInNonunicastCountInvPort1_Object = MibTableColumn
pm253perfdatacomclientPast24StatInNonunicastCountInvPort1 = _Pm253perfdatacomclientPast24StatInNonunicastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 280, 1, 22),
    _Pm253perfdatacomclientPast24StatInNonunicastCountInvPort1_Type()
)
pm253perfdatacomclientPast24StatInNonunicastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatInNonunicastCountInvPort1.setStatus("current")
_Pm253perfdatacomclientPast24StatInNonunicastCountPort1_Type = Counter64
_Pm253perfdatacomclientPast24StatInNonunicastCountPort1_Object = MibTableColumn
pm253perfdatacomclientPast24StatInNonunicastCountPort1 = _Pm253perfdatacomclientPast24StatInNonunicastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 280, 1, 23),
    _Pm253perfdatacomclientPast24StatInNonunicastCountPort1_Type()
)
pm253perfdatacomclientPast24StatInNonunicastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatInNonunicastCountPort1.setStatus("current")
_Pm253perfdatacomclientPast24StatOutBytesCountInvPort1_Type = EkiOnOff
_Pm253perfdatacomclientPast24StatOutBytesCountInvPort1_Object = MibTableColumn
pm253perfdatacomclientPast24StatOutBytesCountInvPort1 = _Pm253perfdatacomclientPast24StatOutBytesCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 280, 1, 26),
    _Pm253perfdatacomclientPast24StatOutBytesCountInvPort1_Type()
)
pm253perfdatacomclientPast24StatOutBytesCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatOutBytesCountInvPort1.setStatus("current")
_Pm253perfdatacomclientPast24StatOutBytesCountPort1_Type = Counter64
_Pm253perfdatacomclientPast24StatOutBytesCountPort1_Object = MibTableColumn
pm253perfdatacomclientPast24StatOutBytesCountPort1 = _Pm253perfdatacomclientPast24StatOutBytesCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 280, 1, 27),
    _Pm253perfdatacomclientPast24StatOutBytesCountPort1_Type()
)
pm253perfdatacomclientPast24StatOutBytesCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatOutBytesCountPort1.setStatus("current")
_Pm253perfdatacomclientPast24StatOutBroadcastCountInvPort1_Type = EkiOnOff
_Pm253perfdatacomclientPast24StatOutBroadcastCountInvPort1_Object = MibTableColumn
pm253perfdatacomclientPast24StatOutBroadcastCountInvPort1 = _Pm253perfdatacomclientPast24StatOutBroadcastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 280, 1, 32),
    _Pm253perfdatacomclientPast24StatOutBroadcastCountInvPort1_Type()
)
pm253perfdatacomclientPast24StatOutBroadcastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatOutBroadcastCountInvPort1.setStatus("current")
_Pm253perfdatacomclientPast24StatOutBroadcastCountPort1_Type = Counter64
_Pm253perfdatacomclientPast24StatOutBroadcastCountPort1_Object = MibTableColumn
pm253perfdatacomclientPast24StatOutBroadcastCountPort1 = _Pm253perfdatacomclientPast24StatOutBroadcastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 280, 1, 33),
    _Pm253perfdatacomclientPast24StatOutBroadcastCountPort1_Type()
)
pm253perfdatacomclientPast24StatOutBroadcastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatOutBroadcastCountPort1.setStatus("current")
_Pm253perfdatacomclientPast24StatOutMulticastCountInvPort1_Type = EkiOnOff
_Pm253perfdatacomclientPast24StatOutMulticastCountInvPort1_Object = MibTableColumn
pm253perfdatacomclientPast24StatOutMulticastCountInvPort1 = _Pm253perfdatacomclientPast24StatOutMulticastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 280, 1, 34),
    _Pm253perfdatacomclientPast24StatOutMulticastCountInvPort1_Type()
)
pm253perfdatacomclientPast24StatOutMulticastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatOutMulticastCountInvPort1.setStatus("current")
_Pm253perfdatacomclientPast24StatOutMulticastCountPort1_Type = Counter64
_Pm253perfdatacomclientPast24StatOutMulticastCountPort1_Object = MibTableColumn
pm253perfdatacomclientPast24StatOutMulticastCountPort1 = _Pm253perfdatacomclientPast24StatOutMulticastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 280, 1, 35),
    _Pm253perfdatacomclientPast24StatOutMulticastCountPort1_Type()
)
pm253perfdatacomclientPast24StatOutMulticastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatOutMulticastCountPort1.setStatus("current")
_Pm253perfdatacomclientPast24StatOutUnicastCountInvPort1_Type = EkiOnOff
_Pm253perfdatacomclientPast24StatOutUnicastCountInvPort1_Object = MibTableColumn
pm253perfdatacomclientPast24StatOutUnicastCountInvPort1 = _Pm253perfdatacomclientPast24StatOutUnicastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 280, 1, 42),
    _Pm253perfdatacomclientPast24StatOutUnicastCountInvPort1_Type()
)
pm253perfdatacomclientPast24StatOutUnicastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatOutUnicastCountInvPort1.setStatus("current")
_Pm253perfdatacomclientPast24StatOutUnicastCountPort1_Type = Counter64
_Pm253perfdatacomclientPast24StatOutUnicastCountPort1_Object = MibTableColumn
pm253perfdatacomclientPast24StatOutUnicastCountPort1 = _Pm253perfdatacomclientPast24StatOutUnicastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 280, 1, 43),
    _Pm253perfdatacomclientPast24StatOutUnicastCountPort1_Type()
)
pm253perfdatacomclientPast24StatOutUnicastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatOutUnicastCountPort1.setStatus("current")
_Pm253perfdatacomclientPast24StatOutNonunicastCountInvPort1_Type = EkiOnOff
_Pm253perfdatacomclientPast24StatOutNonunicastCountInvPort1_Object = MibTableColumn
pm253perfdatacomclientPast24StatOutNonunicastCountInvPort1 = _Pm253perfdatacomclientPast24StatOutNonunicastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 280, 1, 44),
    _Pm253perfdatacomclientPast24StatOutNonunicastCountInvPort1_Type()
)
pm253perfdatacomclientPast24StatOutNonunicastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatOutNonunicastCountInvPort1.setStatus("current")
_Pm253perfdatacomclientPast24StatOutNonunicastCountPort1_Type = Counter64
_Pm253perfdatacomclientPast24StatOutNonunicastCountPort1_Object = MibTableColumn
pm253perfdatacomclientPast24StatOutNonunicastCountPort1 = _Pm253perfdatacomclientPast24StatOutNonunicastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 280, 1, 45),
    _Pm253perfdatacomclientPast24StatOutNonunicastCountPort1_Type()
)
pm253perfdatacomclientPast24StatOutNonunicastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatOutNonunicastCountPort1.setStatus("current")
_Pm253PerfDatacomClientPast24StatHistoryPort2Table_Object = MibTable
pm253PerfDatacomClientPast24StatHistoryPort2Table = _Pm253PerfDatacomClientPast24StatHistoryPort2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 281)
)
if mibBuilder.loadTexts:
    pm253PerfDatacomClientPast24StatHistoryPort2Table.setStatus("current")
_Pm253PerfDatacomClientPast24StatHistoryPort2Entry_Object = MibTableRow
pm253PerfDatacomClientPast24StatHistoryPort2Entry = _Pm253PerfDatacomClientPast24StatHistoryPort2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 281, 1)
)
pm253PerfDatacomClientPast24StatHistoryPort2Entry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253PerfDatacomClientPast24StatHistoryPort2Index"),
)
if mibBuilder.loadTexts:
    pm253PerfDatacomClientPast24StatHistoryPort2Entry.setStatus("current")


class _Pm253PerfDatacomClientPast24StatHistoryPort2Index_Type(Integer32):
    """Custom type pm253PerfDatacomClientPast24StatHistoryPort2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253PerfDatacomClientPast24StatHistoryPort2Index_Type.__name__ = "Integer32"
_Pm253PerfDatacomClientPast24StatHistoryPort2Index_Object = MibTableColumn
pm253PerfDatacomClientPast24StatHistoryPort2Index = _Pm253PerfDatacomClientPast24StatHistoryPort2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 281, 1, 1),
    _Pm253PerfDatacomClientPast24StatHistoryPort2Index_Type()
)
pm253PerfDatacomClientPast24StatHistoryPort2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfDatacomClientPast24StatHistoryPort2Index.setStatus("current")
_Pm253perfdatacomclientPast24StatInBytesCountInvPort2_Type = EkiOnOff
_Pm253perfdatacomclientPast24StatInBytesCountInvPort2_Object = MibTableColumn
pm253perfdatacomclientPast24StatInBytesCountInvPort2 = _Pm253perfdatacomclientPast24StatInBytesCountInvPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 281, 1, 2),
    _Pm253perfdatacomclientPast24StatInBytesCountInvPort2_Type()
)
pm253perfdatacomclientPast24StatInBytesCountInvPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatInBytesCountInvPort2.setStatus("current")
_Pm253perfdatacomclientPast24StatInBytesCountPort2_Type = Counter64
_Pm253perfdatacomclientPast24StatInBytesCountPort2_Object = MibTableColumn
pm253perfdatacomclientPast24StatInBytesCountPort2 = _Pm253perfdatacomclientPast24StatInBytesCountPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 281, 1, 3),
    _Pm253perfdatacomclientPast24StatInBytesCountPort2_Type()
)
pm253perfdatacomclientPast24StatInBytesCountPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatInBytesCountPort2.setStatus("current")
_Pm253perfdatacomclientPast24StatInCrcCountInvPort2_Type = EkiOnOff
_Pm253perfdatacomclientPast24StatInCrcCountInvPort2_Object = MibTableColumn
pm253perfdatacomclientPast24StatInCrcCountInvPort2 = _Pm253perfdatacomclientPast24StatInCrcCountInvPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 281, 1, 4),
    _Pm253perfdatacomclientPast24StatInCrcCountInvPort2_Type()
)
pm253perfdatacomclientPast24StatInCrcCountInvPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatInCrcCountInvPort2.setStatus("current")
_Pm253perfdatacomclientPast24StatInCrcCountPort2_Type = Counter64
_Pm253perfdatacomclientPast24StatInCrcCountPort2_Object = MibTableColumn
pm253perfdatacomclientPast24StatInCrcCountPort2 = _Pm253perfdatacomclientPast24StatInCrcCountPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 281, 1, 5),
    _Pm253perfdatacomclientPast24StatInCrcCountPort2_Type()
)
pm253perfdatacomclientPast24StatInCrcCountPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatInCrcCountPort2.setStatus("current")
_Pm253perfdatacomclientPast24StatInBroadcastCountInvPort2_Type = EkiOnOff
_Pm253perfdatacomclientPast24StatInBroadcastCountInvPort2_Object = MibTableColumn
pm253perfdatacomclientPast24StatInBroadcastCountInvPort2 = _Pm253perfdatacomclientPast24StatInBroadcastCountInvPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 281, 1, 8),
    _Pm253perfdatacomclientPast24StatInBroadcastCountInvPort2_Type()
)
pm253perfdatacomclientPast24StatInBroadcastCountInvPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatInBroadcastCountInvPort2.setStatus("current")
_Pm253perfdatacomclientPast24StatInBroadcastCountPort2_Type = Counter64
_Pm253perfdatacomclientPast24StatInBroadcastCountPort2_Object = MibTableColumn
pm253perfdatacomclientPast24StatInBroadcastCountPort2 = _Pm253perfdatacomclientPast24StatInBroadcastCountPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 281, 1, 9),
    _Pm253perfdatacomclientPast24StatInBroadcastCountPort2_Type()
)
pm253perfdatacomclientPast24StatInBroadcastCountPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatInBroadcastCountPort2.setStatus("current")
_Pm253perfdatacomclientPast24StatInMulticastCountInvPort2_Type = EkiOnOff
_Pm253perfdatacomclientPast24StatInMulticastCountInvPort2_Object = MibTableColumn
pm253perfdatacomclientPast24StatInMulticastCountInvPort2 = _Pm253perfdatacomclientPast24StatInMulticastCountInvPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 281, 1, 10),
    _Pm253perfdatacomclientPast24StatInMulticastCountInvPort2_Type()
)
pm253perfdatacomclientPast24StatInMulticastCountInvPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatInMulticastCountInvPort2.setStatus("current")
_Pm253perfdatacomclientPast24StatInMulticastCountPort2_Type = Counter64
_Pm253perfdatacomclientPast24StatInMulticastCountPort2_Object = MibTableColumn
pm253perfdatacomclientPast24StatInMulticastCountPort2 = _Pm253perfdatacomclientPast24StatInMulticastCountPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 281, 1, 11),
    _Pm253perfdatacomclientPast24StatInMulticastCountPort2_Type()
)
pm253perfdatacomclientPast24StatInMulticastCountPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatInMulticastCountPort2.setStatus("current")
_Pm253perfdatacomclientPast24StatInUnicastCountInvPort2_Type = EkiOnOff
_Pm253perfdatacomclientPast24StatInUnicastCountInvPort2_Object = MibTableColumn
pm253perfdatacomclientPast24StatInUnicastCountInvPort2 = _Pm253perfdatacomclientPast24StatInUnicastCountInvPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 281, 1, 20),
    _Pm253perfdatacomclientPast24StatInUnicastCountInvPort2_Type()
)
pm253perfdatacomclientPast24StatInUnicastCountInvPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatInUnicastCountInvPort2.setStatus("current")
_Pm253perfdatacomclientPast24StatInUnicastCountPort2_Type = Counter64
_Pm253perfdatacomclientPast24StatInUnicastCountPort2_Object = MibTableColumn
pm253perfdatacomclientPast24StatInUnicastCountPort2 = _Pm253perfdatacomclientPast24StatInUnicastCountPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 281, 1, 21),
    _Pm253perfdatacomclientPast24StatInUnicastCountPort2_Type()
)
pm253perfdatacomclientPast24StatInUnicastCountPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatInUnicastCountPort2.setStatus("current")
_Pm253perfdatacomclientPast24StatInNonunicastCountInvPort2_Type = EkiOnOff
_Pm253perfdatacomclientPast24StatInNonunicastCountInvPort2_Object = MibTableColumn
pm253perfdatacomclientPast24StatInNonunicastCountInvPort2 = _Pm253perfdatacomclientPast24StatInNonunicastCountInvPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 281, 1, 22),
    _Pm253perfdatacomclientPast24StatInNonunicastCountInvPort2_Type()
)
pm253perfdatacomclientPast24StatInNonunicastCountInvPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatInNonunicastCountInvPort2.setStatus("current")
_Pm253perfdatacomclientPast24StatInNonunicastCountPort2_Type = Counter64
_Pm253perfdatacomclientPast24StatInNonunicastCountPort2_Object = MibTableColumn
pm253perfdatacomclientPast24StatInNonunicastCountPort2 = _Pm253perfdatacomclientPast24StatInNonunicastCountPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 281, 1, 23),
    _Pm253perfdatacomclientPast24StatInNonunicastCountPort2_Type()
)
pm253perfdatacomclientPast24StatInNonunicastCountPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatInNonunicastCountPort2.setStatus("current")
_Pm253perfdatacomclientPast24StatOutBytesCountInvPort2_Type = EkiOnOff
_Pm253perfdatacomclientPast24StatOutBytesCountInvPort2_Object = MibTableColumn
pm253perfdatacomclientPast24StatOutBytesCountInvPort2 = _Pm253perfdatacomclientPast24StatOutBytesCountInvPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 281, 1, 26),
    _Pm253perfdatacomclientPast24StatOutBytesCountInvPort2_Type()
)
pm253perfdatacomclientPast24StatOutBytesCountInvPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatOutBytesCountInvPort2.setStatus("current")
_Pm253perfdatacomclientPast24StatOutBytesCountPort2_Type = Counter64
_Pm253perfdatacomclientPast24StatOutBytesCountPort2_Object = MibTableColumn
pm253perfdatacomclientPast24StatOutBytesCountPort2 = _Pm253perfdatacomclientPast24StatOutBytesCountPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 281, 1, 27),
    _Pm253perfdatacomclientPast24StatOutBytesCountPort2_Type()
)
pm253perfdatacomclientPast24StatOutBytesCountPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatOutBytesCountPort2.setStatus("current")
_Pm253perfdatacomclientPast24StatOutBroadcastCountInvPort2_Type = EkiOnOff
_Pm253perfdatacomclientPast24StatOutBroadcastCountInvPort2_Object = MibTableColumn
pm253perfdatacomclientPast24StatOutBroadcastCountInvPort2 = _Pm253perfdatacomclientPast24StatOutBroadcastCountInvPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 281, 1, 32),
    _Pm253perfdatacomclientPast24StatOutBroadcastCountInvPort2_Type()
)
pm253perfdatacomclientPast24StatOutBroadcastCountInvPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatOutBroadcastCountInvPort2.setStatus("current")
_Pm253perfdatacomclientPast24StatOutBroadcastCountPort2_Type = Counter64
_Pm253perfdatacomclientPast24StatOutBroadcastCountPort2_Object = MibTableColumn
pm253perfdatacomclientPast24StatOutBroadcastCountPort2 = _Pm253perfdatacomclientPast24StatOutBroadcastCountPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 281, 1, 33),
    _Pm253perfdatacomclientPast24StatOutBroadcastCountPort2_Type()
)
pm253perfdatacomclientPast24StatOutBroadcastCountPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatOutBroadcastCountPort2.setStatus("current")
_Pm253perfdatacomclientPast24StatOutMulticastCountInvPort2_Type = EkiOnOff
_Pm253perfdatacomclientPast24StatOutMulticastCountInvPort2_Object = MibTableColumn
pm253perfdatacomclientPast24StatOutMulticastCountInvPort2 = _Pm253perfdatacomclientPast24StatOutMulticastCountInvPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 281, 1, 34),
    _Pm253perfdatacomclientPast24StatOutMulticastCountInvPort2_Type()
)
pm253perfdatacomclientPast24StatOutMulticastCountInvPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatOutMulticastCountInvPort2.setStatus("current")
_Pm253perfdatacomclientPast24StatOutMulticastCountPort2_Type = Counter64
_Pm253perfdatacomclientPast24StatOutMulticastCountPort2_Object = MibTableColumn
pm253perfdatacomclientPast24StatOutMulticastCountPort2 = _Pm253perfdatacomclientPast24StatOutMulticastCountPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 281, 1, 35),
    _Pm253perfdatacomclientPast24StatOutMulticastCountPort2_Type()
)
pm253perfdatacomclientPast24StatOutMulticastCountPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatOutMulticastCountPort2.setStatus("current")
_Pm253perfdatacomclientPast24StatOutUnicastCountInvPort2_Type = EkiOnOff
_Pm253perfdatacomclientPast24StatOutUnicastCountInvPort2_Object = MibTableColumn
pm253perfdatacomclientPast24StatOutUnicastCountInvPort2 = _Pm253perfdatacomclientPast24StatOutUnicastCountInvPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 281, 1, 42),
    _Pm253perfdatacomclientPast24StatOutUnicastCountInvPort2_Type()
)
pm253perfdatacomclientPast24StatOutUnicastCountInvPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatOutUnicastCountInvPort2.setStatus("current")
_Pm253perfdatacomclientPast24StatOutUnicastCountPort2_Type = Counter64
_Pm253perfdatacomclientPast24StatOutUnicastCountPort2_Object = MibTableColumn
pm253perfdatacomclientPast24StatOutUnicastCountPort2 = _Pm253perfdatacomclientPast24StatOutUnicastCountPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 281, 1, 43),
    _Pm253perfdatacomclientPast24StatOutUnicastCountPort2_Type()
)
pm253perfdatacomclientPast24StatOutUnicastCountPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatOutUnicastCountPort2.setStatus("current")
_Pm253perfdatacomclientPast24StatOutNonunicastCountInvPort2_Type = EkiOnOff
_Pm253perfdatacomclientPast24StatOutNonunicastCountInvPort2_Object = MibTableColumn
pm253perfdatacomclientPast24StatOutNonunicastCountInvPort2 = _Pm253perfdatacomclientPast24StatOutNonunicastCountInvPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 281, 1, 44),
    _Pm253perfdatacomclientPast24StatOutNonunicastCountInvPort2_Type()
)
pm253perfdatacomclientPast24StatOutNonunicastCountInvPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatOutNonunicastCountInvPort2.setStatus("current")
_Pm253perfdatacomclientPast24StatOutNonunicastCountPort2_Type = Counter64
_Pm253perfdatacomclientPast24StatOutNonunicastCountPort2_Object = MibTableColumn
pm253perfdatacomclientPast24StatOutNonunicastCountPort2 = _Pm253perfdatacomclientPast24StatOutNonunicastCountPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 281, 1, 45),
    _Pm253perfdatacomclientPast24StatOutNonunicastCountPort2_Type()
)
pm253perfdatacomclientPast24StatOutNonunicastCountPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatOutNonunicastCountPort2.setStatus("current")
_Pm253PerfDatacomClientPast24StatHistoryPort3Table_Object = MibTable
pm253PerfDatacomClientPast24StatHistoryPort3Table = _Pm253PerfDatacomClientPast24StatHistoryPort3Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 282)
)
if mibBuilder.loadTexts:
    pm253PerfDatacomClientPast24StatHistoryPort3Table.setStatus("current")
_Pm253PerfDatacomClientPast24StatHistoryPort3Entry_Object = MibTableRow
pm253PerfDatacomClientPast24StatHistoryPort3Entry = _Pm253PerfDatacomClientPast24StatHistoryPort3Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 282, 1)
)
pm253PerfDatacomClientPast24StatHistoryPort3Entry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253PerfDatacomClientPast24StatHistoryPort3Index"),
)
if mibBuilder.loadTexts:
    pm253PerfDatacomClientPast24StatHistoryPort3Entry.setStatus("current")


class _Pm253PerfDatacomClientPast24StatHistoryPort3Index_Type(Integer32):
    """Custom type pm253PerfDatacomClientPast24StatHistoryPort3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253PerfDatacomClientPast24StatHistoryPort3Index_Type.__name__ = "Integer32"
_Pm253PerfDatacomClientPast24StatHistoryPort3Index_Object = MibTableColumn
pm253PerfDatacomClientPast24StatHistoryPort3Index = _Pm253PerfDatacomClientPast24StatHistoryPort3Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 282, 1, 1),
    _Pm253PerfDatacomClientPast24StatHistoryPort3Index_Type()
)
pm253PerfDatacomClientPast24StatHistoryPort3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfDatacomClientPast24StatHistoryPort3Index.setStatus("current")
_Pm253perfdatacomclientPast24StatInBytesCountInvPort3_Type = EkiOnOff
_Pm253perfdatacomclientPast24StatInBytesCountInvPort3_Object = MibTableColumn
pm253perfdatacomclientPast24StatInBytesCountInvPort3 = _Pm253perfdatacomclientPast24StatInBytesCountInvPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 282, 1, 2),
    _Pm253perfdatacomclientPast24StatInBytesCountInvPort3_Type()
)
pm253perfdatacomclientPast24StatInBytesCountInvPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatInBytesCountInvPort3.setStatus("current")
_Pm253perfdatacomclientPast24StatInBytesCountPort3_Type = Counter64
_Pm253perfdatacomclientPast24StatInBytesCountPort3_Object = MibTableColumn
pm253perfdatacomclientPast24StatInBytesCountPort3 = _Pm253perfdatacomclientPast24StatInBytesCountPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 282, 1, 3),
    _Pm253perfdatacomclientPast24StatInBytesCountPort3_Type()
)
pm253perfdatacomclientPast24StatInBytesCountPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatInBytesCountPort3.setStatus("current")
_Pm253perfdatacomclientPast24StatInCrcCountInvPort3_Type = EkiOnOff
_Pm253perfdatacomclientPast24StatInCrcCountInvPort3_Object = MibTableColumn
pm253perfdatacomclientPast24StatInCrcCountInvPort3 = _Pm253perfdatacomclientPast24StatInCrcCountInvPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 282, 1, 4),
    _Pm253perfdatacomclientPast24StatInCrcCountInvPort3_Type()
)
pm253perfdatacomclientPast24StatInCrcCountInvPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatInCrcCountInvPort3.setStatus("current")
_Pm253perfdatacomclientPast24StatInCrcCountPort3_Type = Counter64
_Pm253perfdatacomclientPast24StatInCrcCountPort3_Object = MibTableColumn
pm253perfdatacomclientPast24StatInCrcCountPort3 = _Pm253perfdatacomclientPast24StatInCrcCountPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 282, 1, 5),
    _Pm253perfdatacomclientPast24StatInCrcCountPort3_Type()
)
pm253perfdatacomclientPast24StatInCrcCountPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatInCrcCountPort3.setStatus("current")
_Pm253perfdatacomclientPast24StatInBroadcastCountInvPort3_Type = EkiOnOff
_Pm253perfdatacomclientPast24StatInBroadcastCountInvPort3_Object = MibTableColumn
pm253perfdatacomclientPast24StatInBroadcastCountInvPort3 = _Pm253perfdatacomclientPast24StatInBroadcastCountInvPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 282, 1, 8),
    _Pm253perfdatacomclientPast24StatInBroadcastCountInvPort3_Type()
)
pm253perfdatacomclientPast24StatInBroadcastCountInvPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatInBroadcastCountInvPort3.setStatus("current")
_Pm253perfdatacomclientPast24StatInBroadcastCountPort3_Type = Counter64
_Pm253perfdatacomclientPast24StatInBroadcastCountPort3_Object = MibTableColumn
pm253perfdatacomclientPast24StatInBroadcastCountPort3 = _Pm253perfdatacomclientPast24StatInBroadcastCountPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 282, 1, 9),
    _Pm253perfdatacomclientPast24StatInBroadcastCountPort3_Type()
)
pm253perfdatacomclientPast24StatInBroadcastCountPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatInBroadcastCountPort3.setStatus("current")
_Pm253perfdatacomclientPast24StatInMulticastCountInvPort3_Type = EkiOnOff
_Pm253perfdatacomclientPast24StatInMulticastCountInvPort3_Object = MibTableColumn
pm253perfdatacomclientPast24StatInMulticastCountInvPort3 = _Pm253perfdatacomclientPast24StatInMulticastCountInvPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 282, 1, 10),
    _Pm253perfdatacomclientPast24StatInMulticastCountInvPort3_Type()
)
pm253perfdatacomclientPast24StatInMulticastCountInvPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatInMulticastCountInvPort3.setStatus("current")
_Pm253perfdatacomclientPast24StatInMulticastCountPort3_Type = Counter64
_Pm253perfdatacomclientPast24StatInMulticastCountPort3_Object = MibTableColumn
pm253perfdatacomclientPast24StatInMulticastCountPort3 = _Pm253perfdatacomclientPast24StatInMulticastCountPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 282, 1, 11),
    _Pm253perfdatacomclientPast24StatInMulticastCountPort3_Type()
)
pm253perfdatacomclientPast24StatInMulticastCountPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatInMulticastCountPort3.setStatus("current")
_Pm253perfdatacomclientPast24StatInUnicastCountInvPort3_Type = EkiOnOff
_Pm253perfdatacomclientPast24StatInUnicastCountInvPort3_Object = MibTableColumn
pm253perfdatacomclientPast24StatInUnicastCountInvPort3 = _Pm253perfdatacomclientPast24StatInUnicastCountInvPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 282, 1, 20),
    _Pm253perfdatacomclientPast24StatInUnicastCountInvPort3_Type()
)
pm253perfdatacomclientPast24StatInUnicastCountInvPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatInUnicastCountInvPort3.setStatus("current")
_Pm253perfdatacomclientPast24StatInUnicastCountPort3_Type = Counter64
_Pm253perfdatacomclientPast24StatInUnicastCountPort3_Object = MibTableColumn
pm253perfdatacomclientPast24StatInUnicastCountPort3 = _Pm253perfdatacomclientPast24StatInUnicastCountPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 282, 1, 21),
    _Pm253perfdatacomclientPast24StatInUnicastCountPort3_Type()
)
pm253perfdatacomclientPast24StatInUnicastCountPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatInUnicastCountPort3.setStatus("current")
_Pm253perfdatacomclientPast24StatInNonunicastCountInvPort3_Type = EkiOnOff
_Pm253perfdatacomclientPast24StatInNonunicastCountInvPort3_Object = MibTableColumn
pm253perfdatacomclientPast24StatInNonunicastCountInvPort3 = _Pm253perfdatacomclientPast24StatInNonunicastCountInvPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 282, 1, 22),
    _Pm253perfdatacomclientPast24StatInNonunicastCountInvPort3_Type()
)
pm253perfdatacomclientPast24StatInNonunicastCountInvPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatInNonunicastCountInvPort3.setStatus("current")
_Pm253perfdatacomclientPast24StatInNonunicastCountPort3_Type = Counter64
_Pm253perfdatacomclientPast24StatInNonunicastCountPort3_Object = MibTableColumn
pm253perfdatacomclientPast24StatInNonunicastCountPort3 = _Pm253perfdatacomclientPast24StatInNonunicastCountPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 282, 1, 23),
    _Pm253perfdatacomclientPast24StatInNonunicastCountPort3_Type()
)
pm253perfdatacomclientPast24StatInNonunicastCountPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatInNonunicastCountPort3.setStatus("current")
_Pm253perfdatacomclientPast24StatOutBytesCountInvPort3_Type = EkiOnOff
_Pm253perfdatacomclientPast24StatOutBytesCountInvPort3_Object = MibTableColumn
pm253perfdatacomclientPast24StatOutBytesCountInvPort3 = _Pm253perfdatacomclientPast24StatOutBytesCountInvPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 282, 1, 26),
    _Pm253perfdatacomclientPast24StatOutBytesCountInvPort3_Type()
)
pm253perfdatacomclientPast24StatOutBytesCountInvPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatOutBytesCountInvPort3.setStatus("current")
_Pm253perfdatacomclientPast24StatOutBytesCountPort3_Type = Counter64
_Pm253perfdatacomclientPast24StatOutBytesCountPort3_Object = MibTableColumn
pm253perfdatacomclientPast24StatOutBytesCountPort3 = _Pm253perfdatacomclientPast24StatOutBytesCountPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 282, 1, 27),
    _Pm253perfdatacomclientPast24StatOutBytesCountPort3_Type()
)
pm253perfdatacomclientPast24StatOutBytesCountPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatOutBytesCountPort3.setStatus("current")
_Pm253perfdatacomclientPast24StatOutBroadcastCountInvPort3_Type = EkiOnOff
_Pm253perfdatacomclientPast24StatOutBroadcastCountInvPort3_Object = MibTableColumn
pm253perfdatacomclientPast24StatOutBroadcastCountInvPort3 = _Pm253perfdatacomclientPast24StatOutBroadcastCountInvPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 282, 1, 32),
    _Pm253perfdatacomclientPast24StatOutBroadcastCountInvPort3_Type()
)
pm253perfdatacomclientPast24StatOutBroadcastCountInvPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatOutBroadcastCountInvPort3.setStatus("current")
_Pm253perfdatacomclientPast24StatOutBroadcastCountPort3_Type = Counter64
_Pm253perfdatacomclientPast24StatOutBroadcastCountPort3_Object = MibTableColumn
pm253perfdatacomclientPast24StatOutBroadcastCountPort3 = _Pm253perfdatacomclientPast24StatOutBroadcastCountPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 282, 1, 33),
    _Pm253perfdatacomclientPast24StatOutBroadcastCountPort3_Type()
)
pm253perfdatacomclientPast24StatOutBroadcastCountPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatOutBroadcastCountPort3.setStatus("current")
_Pm253perfdatacomclientPast24StatOutMulticastCountInvPort3_Type = EkiOnOff
_Pm253perfdatacomclientPast24StatOutMulticastCountInvPort3_Object = MibTableColumn
pm253perfdatacomclientPast24StatOutMulticastCountInvPort3 = _Pm253perfdatacomclientPast24StatOutMulticastCountInvPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 282, 1, 34),
    _Pm253perfdatacomclientPast24StatOutMulticastCountInvPort3_Type()
)
pm253perfdatacomclientPast24StatOutMulticastCountInvPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatOutMulticastCountInvPort3.setStatus("current")
_Pm253perfdatacomclientPast24StatOutMulticastCountPort3_Type = Counter64
_Pm253perfdatacomclientPast24StatOutMulticastCountPort3_Object = MibTableColumn
pm253perfdatacomclientPast24StatOutMulticastCountPort3 = _Pm253perfdatacomclientPast24StatOutMulticastCountPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 282, 1, 35),
    _Pm253perfdatacomclientPast24StatOutMulticastCountPort3_Type()
)
pm253perfdatacomclientPast24StatOutMulticastCountPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatOutMulticastCountPort3.setStatus("current")
_Pm253perfdatacomclientPast24StatOutUnicastCountInvPort3_Type = EkiOnOff
_Pm253perfdatacomclientPast24StatOutUnicastCountInvPort3_Object = MibTableColumn
pm253perfdatacomclientPast24StatOutUnicastCountInvPort3 = _Pm253perfdatacomclientPast24StatOutUnicastCountInvPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 282, 1, 42),
    _Pm253perfdatacomclientPast24StatOutUnicastCountInvPort3_Type()
)
pm253perfdatacomclientPast24StatOutUnicastCountInvPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatOutUnicastCountInvPort3.setStatus("current")
_Pm253perfdatacomclientPast24StatOutUnicastCountPort3_Type = Counter64
_Pm253perfdatacomclientPast24StatOutUnicastCountPort3_Object = MibTableColumn
pm253perfdatacomclientPast24StatOutUnicastCountPort3 = _Pm253perfdatacomclientPast24StatOutUnicastCountPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 282, 1, 43),
    _Pm253perfdatacomclientPast24StatOutUnicastCountPort3_Type()
)
pm253perfdatacomclientPast24StatOutUnicastCountPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatOutUnicastCountPort3.setStatus("current")
_Pm253perfdatacomclientPast24StatOutNonunicastCountInvPort3_Type = EkiOnOff
_Pm253perfdatacomclientPast24StatOutNonunicastCountInvPort3_Object = MibTableColumn
pm253perfdatacomclientPast24StatOutNonunicastCountInvPort3 = _Pm253perfdatacomclientPast24StatOutNonunicastCountInvPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 282, 1, 44),
    _Pm253perfdatacomclientPast24StatOutNonunicastCountInvPort3_Type()
)
pm253perfdatacomclientPast24StatOutNonunicastCountInvPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatOutNonunicastCountInvPort3.setStatus("current")
_Pm253perfdatacomclientPast24StatOutNonunicastCountPort3_Type = Counter64
_Pm253perfdatacomclientPast24StatOutNonunicastCountPort3_Object = MibTableColumn
pm253perfdatacomclientPast24StatOutNonunicastCountPort3 = _Pm253perfdatacomclientPast24StatOutNonunicastCountPort3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 2, 282, 1, 45),
    _Pm253perfdatacomclientPast24StatOutNonunicastCountPort3_Type()
)
pm253perfdatacomclientPast24StatOutNonunicastCountPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253perfdatacomclientPast24StatOutNonunicastCountPort3.setStatus("current")
_Pm253MonLine_ObjectIdentity = ObjectIdentity
pm253MonLine = _Pm253MonLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3)
)
_Pm253PerfTelecomLineCurrent15StatTable_Object = MibTable
pm253PerfTelecomLineCurrent15StatTable = _Pm253PerfTelecomLineCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 128)
)
if mibBuilder.loadTexts:
    pm253PerfTelecomLineCurrent15StatTable.setStatus("current")
_Pm253PerfTelecomLineCurrent15StatEntry_Object = MibTableRow
pm253PerfTelecomLineCurrent15StatEntry = _Pm253PerfTelecomLineCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 128, 1)
)
pm253PerfTelecomLineCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253PerfTelecomLineCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pm253PerfTelecomLineCurrent15StatEntry.setStatus("current")


class _Pm253PerfTelecomLineCurrent15StatIndex_Type(Integer32):
    """Custom type pm253PerfTelecomLineCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253PerfTelecomLineCurrent15StatIndex_Type.__name__ = "Integer32"
_Pm253PerfTelecomLineCurrent15StatIndex_Object = MibTableColumn
pm253PerfTelecomLineCurrent15StatIndex = _Pm253PerfTelecomLineCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 128, 1, 1),
    _Pm253PerfTelecomLineCurrent15StatIndex_Type()
)
pm253PerfTelecomLineCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLineCurrent15StatIndex.setStatus("current")
_Pm253PerfTelecomLineCurrent15StatInvCvPortn_Type = EkiOnOff
_Pm253PerfTelecomLineCurrent15StatInvCvPortn_Object = MibTableColumn
pm253PerfTelecomLineCurrent15StatInvCvPortn = _Pm253PerfTelecomLineCurrent15StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 128, 1, 2),
    _Pm253PerfTelecomLineCurrent15StatInvCvPortn_Type()
)
pm253PerfTelecomLineCurrent15StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLineCurrent15StatInvCvPortn.setStatus("current")
_Pm253PerfTelecomLineCurrent15StatCvValuePortn_Type = Unsigned32
_Pm253PerfTelecomLineCurrent15StatCvValuePortn_Object = MibTableColumn
pm253PerfTelecomLineCurrent15StatCvValuePortn = _Pm253PerfTelecomLineCurrent15StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 128, 1, 3),
    _Pm253PerfTelecomLineCurrent15StatCvValuePortn_Type()
)
pm253PerfTelecomLineCurrent15StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLineCurrent15StatCvValuePortn.setStatus("current")
_Pm253PerfTelecomLineCurrent15StatInvEsPortn_Type = EkiOnOff
_Pm253PerfTelecomLineCurrent15StatInvEsPortn_Object = MibTableColumn
pm253PerfTelecomLineCurrent15StatInvEsPortn = _Pm253PerfTelecomLineCurrent15StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 128, 1, 4),
    _Pm253PerfTelecomLineCurrent15StatInvEsPortn_Type()
)
pm253PerfTelecomLineCurrent15StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLineCurrent15StatInvEsPortn.setStatus("current")
_Pm253PerfTelecomLineCurrent15StatEsValuePortn_Type = Unsigned32
_Pm253PerfTelecomLineCurrent15StatEsValuePortn_Object = MibTableColumn
pm253PerfTelecomLineCurrent15StatEsValuePortn = _Pm253PerfTelecomLineCurrent15StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 128, 1, 5),
    _Pm253PerfTelecomLineCurrent15StatEsValuePortn_Type()
)
pm253PerfTelecomLineCurrent15StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLineCurrent15StatEsValuePortn.setStatus("current")
_Pm253PerfTelecomLineCurrent15StatInvSesPortn_Type = EkiOnOff
_Pm253PerfTelecomLineCurrent15StatInvSesPortn_Object = MibTableColumn
pm253PerfTelecomLineCurrent15StatInvSesPortn = _Pm253PerfTelecomLineCurrent15StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 128, 1, 6),
    _Pm253PerfTelecomLineCurrent15StatInvSesPortn_Type()
)
pm253PerfTelecomLineCurrent15StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLineCurrent15StatInvSesPortn.setStatus("current")
_Pm253PerfTelecomLineCurrent15StatSesValuePortn_Type = Unsigned32
_Pm253PerfTelecomLineCurrent15StatSesValuePortn_Object = MibTableColumn
pm253PerfTelecomLineCurrent15StatSesValuePortn = _Pm253PerfTelecomLineCurrent15StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 128, 1, 7),
    _Pm253PerfTelecomLineCurrent15StatSesValuePortn_Type()
)
pm253PerfTelecomLineCurrent15StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLineCurrent15StatSesValuePortn.setStatus("current")
_Pm253PerfTelecomLineCurrent15StatInvSefsPortn_Type = EkiOnOff
_Pm253PerfTelecomLineCurrent15StatInvSefsPortn_Object = MibTableColumn
pm253PerfTelecomLineCurrent15StatInvSefsPortn = _Pm253PerfTelecomLineCurrent15StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 128, 1, 8),
    _Pm253PerfTelecomLineCurrent15StatInvSefsPortn_Type()
)
pm253PerfTelecomLineCurrent15StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLineCurrent15StatInvSefsPortn.setStatus("current")
_Pm253PerfTelecomLineCurrent15StatSefsValuePortn_Type = Unsigned32
_Pm253PerfTelecomLineCurrent15StatSefsValuePortn_Object = MibTableColumn
pm253PerfTelecomLineCurrent15StatSefsValuePortn = _Pm253PerfTelecomLineCurrent15StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 128, 1, 9),
    _Pm253PerfTelecomLineCurrent15StatSefsValuePortn_Type()
)
pm253PerfTelecomLineCurrent15StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLineCurrent15StatSefsValuePortn.setStatus("current")
_Pm253PerfTelecomLineCurrent15StatInvUasPortn_Type = EkiOnOff
_Pm253PerfTelecomLineCurrent15StatInvUasPortn_Object = MibTableColumn
pm253PerfTelecomLineCurrent15StatInvUasPortn = _Pm253PerfTelecomLineCurrent15StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 128, 1, 10),
    _Pm253PerfTelecomLineCurrent15StatInvUasPortn_Type()
)
pm253PerfTelecomLineCurrent15StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLineCurrent15StatInvUasPortn.setStatus("current")
_Pm253PerfTelecomLineCurrent15StatUasValuePortn_Type = Unsigned32
_Pm253PerfTelecomLineCurrent15StatUasValuePortn_Object = MibTableColumn
pm253PerfTelecomLineCurrent15StatUasValuePortn = _Pm253PerfTelecomLineCurrent15StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 128, 1, 11),
    _Pm253PerfTelecomLineCurrent15StatUasValuePortn_Type()
)
pm253PerfTelecomLineCurrent15StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLineCurrent15StatUasValuePortn.setStatus("current")
_Pm253PerfTelecomLinePast15StatHistoryPort1Table_Object = MibTable
pm253PerfTelecomLinePast15StatHistoryPort1Table = _Pm253PerfTelecomLinePast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 129)
)
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast15StatHistoryPort1Table.setStatus("current")
_Pm253PerfTelecomLinePast15StatHistoryPort1Entry_Object = MibTableRow
pm253PerfTelecomLinePast15StatHistoryPort1Entry = _Pm253PerfTelecomLinePast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 129, 1)
)
pm253PerfTelecomLinePast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253PerfTelecomLinePast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast15StatHistoryPort1Entry.setStatus("current")


class _Pm253PerfTelecomLinePast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pm253PerfTelecomLinePast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253PerfTelecomLinePast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm253PerfTelecomLinePast15StatHistoryPort1Index_Object = MibTableColumn
pm253PerfTelecomLinePast15StatHistoryPort1Index = _Pm253PerfTelecomLinePast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 129, 1, 1),
    _Pm253PerfTelecomLinePast15StatHistoryPort1Index_Type()
)
pm253PerfTelecomLinePast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast15StatHistoryPort1Index.setStatus("current")
_Pm253PerfTelecomLinePast15StatHistoryInvCvPort1_Type = EkiOnOff
_Pm253PerfTelecomLinePast15StatHistoryInvCvPort1_Object = MibTableColumn
pm253PerfTelecomLinePast15StatHistoryInvCvPort1 = _Pm253PerfTelecomLinePast15StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 129, 1, 2),
    _Pm253PerfTelecomLinePast15StatHistoryInvCvPort1_Type()
)
pm253PerfTelecomLinePast15StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast15StatHistoryInvCvPort1.setStatus("current")
_Pm253PerfTelecomLinePast15StatHistoryCvValuePort1_Type = Unsigned32
_Pm253PerfTelecomLinePast15StatHistoryCvValuePort1_Object = MibTableColumn
pm253PerfTelecomLinePast15StatHistoryCvValuePort1 = _Pm253PerfTelecomLinePast15StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 129, 1, 3),
    _Pm253PerfTelecomLinePast15StatHistoryCvValuePort1_Type()
)
pm253PerfTelecomLinePast15StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast15StatHistoryCvValuePort1.setStatus("current")
_Pm253PerfTelecomLinePast15StatHistoryInvEsPort1_Type = EkiOnOff
_Pm253PerfTelecomLinePast15StatHistoryInvEsPort1_Object = MibTableColumn
pm253PerfTelecomLinePast15StatHistoryInvEsPort1 = _Pm253PerfTelecomLinePast15StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 129, 1, 4),
    _Pm253PerfTelecomLinePast15StatHistoryInvEsPort1_Type()
)
pm253PerfTelecomLinePast15StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast15StatHistoryInvEsPort1.setStatus("current")
_Pm253PerfTelecomLinePast15StatHistoryEsValuePort1_Type = Unsigned32
_Pm253PerfTelecomLinePast15StatHistoryEsValuePort1_Object = MibTableColumn
pm253PerfTelecomLinePast15StatHistoryEsValuePort1 = _Pm253PerfTelecomLinePast15StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 129, 1, 5),
    _Pm253PerfTelecomLinePast15StatHistoryEsValuePort1_Type()
)
pm253PerfTelecomLinePast15StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast15StatHistoryEsValuePort1.setStatus("current")
_Pm253PerfTelecomLinePast15StatHistoryInvSesPort1_Type = EkiOnOff
_Pm253PerfTelecomLinePast15StatHistoryInvSesPort1_Object = MibTableColumn
pm253PerfTelecomLinePast15StatHistoryInvSesPort1 = _Pm253PerfTelecomLinePast15StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 129, 1, 6),
    _Pm253PerfTelecomLinePast15StatHistoryInvSesPort1_Type()
)
pm253PerfTelecomLinePast15StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast15StatHistoryInvSesPort1.setStatus("current")
_Pm253PerfTelecomLinePast15StatHistorySesValuePort1_Type = Unsigned32
_Pm253PerfTelecomLinePast15StatHistorySesValuePort1_Object = MibTableColumn
pm253PerfTelecomLinePast15StatHistorySesValuePort1 = _Pm253PerfTelecomLinePast15StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 129, 1, 7),
    _Pm253PerfTelecomLinePast15StatHistorySesValuePort1_Type()
)
pm253PerfTelecomLinePast15StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast15StatHistorySesValuePort1.setStatus("current")
_Pm253PerfTelecomLinePast15StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm253PerfTelecomLinePast15StatHistoryInvSefsPort1_Object = MibTableColumn
pm253PerfTelecomLinePast15StatHistoryInvSefsPort1 = _Pm253PerfTelecomLinePast15StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 129, 1, 8),
    _Pm253PerfTelecomLinePast15StatHistoryInvSefsPort1_Type()
)
pm253PerfTelecomLinePast15StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast15StatHistoryInvSefsPort1.setStatus("current")
_Pm253PerfTelecomLinePast15StatHistorySefsValuePort1_Type = Unsigned32
_Pm253PerfTelecomLinePast15StatHistorySefsValuePort1_Object = MibTableColumn
pm253PerfTelecomLinePast15StatHistorySefsValuePort1 = _Pm253PerfTelecomLinePast15StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 129, 1, 9),
    _Pm253PerfTelecomLinePast15StatHistorySefsValuePort1_Type()
)
pm253PerfTelecomLinePast15StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast15StatHistorySefsValuePort1.setStatus("current")
_Pm253PerfTelecomLinePast15StatHistoryInvUasPort1_Type = EkiOnOff
_Pm253PerfTelecomLinePast15StatHistoryInvUasPort1_Object = MibTableColumn
pm253PerfTelecomLinePast15StatHistoryInvUasPort1 = _Pm253PerfTelecomLinePast15StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 129, 1, 10),
    _Pm253PerfTelecomLinePast15StatHistoryInvUasPort1_Type()
)
pm253PerfTelecomLinePast15StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast15StatHistoryInvUasPort1.setStatus("current")
_Pm253PerfTelecomLinePast15StatHistoryUasValuePort1_Type = Unsigned32
_Pm253PerfTelecomLinePast15StatHistoryUasValuePort1_Object = MibTableColumn
pm253PerfTelecomLinePast15StatHistoryUasValuePort1 = _Pm253PerfTelecomLinePast15StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 129, 1, 11),
    _Pm253PerfTelecomLinePast15StatHistoryUasValuePort1_Type()
)
pm253PerfTelecomLinePast15StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast15StatHistoryUasValuePort1.setStatus("current")
_Pm253PerfTelecomLineCurrent24StatTable_Object = MibTable
pm253PerfTelecomLineCurrent24StatTable = _Pm253PerfTelecomLineCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 130)
)
if mibBuilder.loadTexts:
    pm253PerfTelecomLineCurrent24StatTable.setStatus("current")
_Pm253PerfTelecomLineCurrent24StatEntry_Object = MibTableRow
pm253PerfTelecomLineCurrent24StatEntry = _Pm253PerfTelecomLineCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 130, 1)
)
pm253PerfTelecomLineCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253PerfTelecomLineCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pm253PerfTelecomLineCurrent24StatEntry.setStatus("current")


class _Pm253PerfTelecomLineCurrent24StatIndex_Type(Integer32):
    """Custom type pm253PerfTelecomLineCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253PerfTelecomLineCurrent24StatIndex_Type.__name__ = "Integer32"
_Pm253PerfTelecomLineCurrent24StatIndex_Object = MibTableColumn
pm253PerfTelecomLineCurrent24StatIndex = _Pm253PerfTelecomLineCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 130, 1, 1),
    _Pm253PerfTelecomLineCurrent24StatIndex_Type()
)
pm253PerfTelecomLineCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLineCurrent24StatIndex.setStatus("current")
_Pm253PerfTelecomLineCurrent24StatInvCvPortn_Type = EkiOnOff
_Pm253PerfTelecomLineCurrent24StatInvCvPortn_Object = MibTableColumn
pm253PerfTelecomLineCurrent24StatInvCvPortn = _Pm253PerfTelecomLineCurrent24StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 130, 1, 2),
    _Pm253PerfTelecomLineCurrent24StatInvCvPortn_Type()
)
pm253PerfTelecomLineCurrent24StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLineCurrent24StatInvCvPortn.setStatus("current")
_Pm253PerfTelecomLineCurrent24StatCvValuePortn_Type = Unsigned32
_Pm253PerfTelecomLineCurrent24StatCvValuePortn_Object = MibTableColumn
pm253PerfTelecomLineCurrent24StatCvValuePortn = _Pm253PerfTelecomLineCurrent24StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 130, 1, 3),
    _Pm253PerfTelecomLineCurrent24StatCvValuePortn_Type()
)
pm253PerfTelecomLineCurrent24StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLineCurrent24StatCvValuePortn.setStatus("current")
_Pm253PerfTelecomLineCurrent24StatInvEsPortn_Type = EkiOnOff
_Pm253PerfTelecomLineCurrent24StatInvEsPortn_Object = MibTableColumn
pm253PerfTelecomLineCurrent24StatInvEsPortn = _Pm253PerfTelecomLineCurrent24StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 130, 1, 4),
    _Pm253PerfTelecomLineCurrent24StatInvEsPortn_Type()
)
pm253PerfTelecomLineCurrent24StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLineCurrent24StatInvEsPortn.setStatus("current")
_Pm253PerfTelecomLineCurrent24StatEsValuePortn_Type = Unsigned32
_Pm253PerfTelecomLineCurrent24StatEsValuePortn_Object = MibTableColumn
pm253PerfTelecomLineCurrent24StatEsValuePortn = _Pm253PerfTelecomLineCurrent24StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 130, 1, 5),
    _Pm253PerfTelecomLineCurrent24StatEsValuePortn_Type()
)
pm253PerfTelecomLineCurrent24StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLineCurrent24StatEsValuePortn.setStatus("current")
_Pm253PerfTelecomLineCurrent24StatInvSesPortn_Type = EkiOnOff
_Pm253PerfTelecomLineCurrent24StatInvSesPortn_Object = MibTableColumn
pm253PerfTelecomLineCurrent24StatInvSesPortn = _Pm253PerfTelecomLineCurrent24StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 130, 1, 6),
    _Pm253PerfTelecomLineCurrent24StatInvSesPortn_Type()
)
pm253PerfTelecomLineCurrent24StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLineCurrent24StatInvSesPortn.setStatus("current")
_Pm253PerfTelecomLineCurrent24StatSesValuePortn_Type = Unsigned32
_Pm253PerfTelecomLineCurrent24StatSesValuePortn_Object = MibTableColumn
pm253PerfTelecomLineCurrent24StatSesValuePortn = _Pm253PerfTelecomLineCurrent24StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 130, 1, 7),
    _Pm253PerfTelecomLineCurrent24StatSesValuePortn_Type()
)
pm253PerfTelecomLineCurrent24StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLineCurrent24StatSesValuePortn.setStatus("current")
_Pm253PerfTelecomLineCurrent24StatInvSefsPortn_Type = EkiOnOff
_Pm253PerfTelecomLineCurrent24StatInvSefsPortn_Object = MibTableColumn
pm253PerfTelecomLineCurrent24StatInvSefsPortn = _Pm253PerfTelecomLineCurrent24StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 130, 1, 8),
    _Pm253PerfTelecomLineCurrent24StatInvSefsPortn_Type()
)
pm253PerfTelecomLineCurrent24StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLineCurrent24StatInvSefsPortn.setStatus("current")
_Pm253PerfTelecomLineCurrent24StatSefsValuePortn_Type = Unsigned32
_Pm253PerfTelecomLineCurrent24StatSefsValuePortn_Object = MibTableColumn
pm253PerfTelecomLineCurrent24StatSefsValuePortn = _Pm253PerfTelecomLineCurrent24StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 130, 1, 9),
    _Pm253PerfTelecomLineCurrent24StatSefsValuePortn_Type()
)
pm253PerfTelecomLineCurrent24StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLineCurrent24StatSefsValuePortn.setStatus("current")
_Pm253PerfTelecomLineCurrent24StatInvUasPortn_Type = EkiOnOff
_Pm253PerfTelecomLineCurrent24StatInvUasPortn_Object = MibTableColumn
pm253PerfTelecomLineCurrent24StatInvUasPortn = _Pm253PerfTelecomLineCurrent24StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 130, 1, 10),
    _Pm253PerfTelecomLineCurrent24StatInvUasPortn_Type()
)
pm253PerfTelecomLineCurrent24StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLineCurrent24StatInvUasPortn.setStatus("current")
_Pm253PerfTelecomLineCurrent24StatUasValuePortn_Type = Unsigned32
_Pm253PerfTelecomLineCurrent24StatUasValuePortn_Object = MibTableColumn
pm253PerfTelecomLineCurrent24StatUasValuePortn = _Pm253PerfTelecomLineCurrent24StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 130, 1, 11),
    _Pm253PerfTelecomLineCurrent24StatUasValuePortn_Type()
)
pm253PerfTelecomLineCurrent24StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLineCurrent24StatUasValuePortn.setStatus("current")
_Pm253PerfTelecomLinePast24StatHistoryPort1Table_Object = MibTable
pm253PerfTelecomLinePast24StatHistoryPort1Table = _Pm253PerfTelecomLinePast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 131)
)
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast24StatHistoryPort1Table.setStatus("current")
_Pm253PerfTelecomLinePast24StatHistoryPort1Entry_Object = MibTableRow
pm253PerfTelecomLinePast24StatHistoryPort1Entry = _Pm253PerfTelecomLinePast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 131, 1)
)
pm253PerfTelecomLinePast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253PerfTelecomLinePast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast24StatHistoryPort1Entry.setStatus("current")


class _Pm253PerfTelecomLinePast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pm253PerfTelecomLinePast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253PerfTelecomLinePast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm253PerfTelecomLinePast24StatHistoryPort1Index_Object = MibTableColumn
pm253PerfTelecomLinePast24StatHistoryPort1Index = _Pm253PerfTelecomLinePast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 131, 1, 1),
    _Pm253PerfTelecomLinePast24StatHistoryPort1Index_Type()
)
pm253PerfTelecomLinePast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast24StatHistoryPort1Index.setStatus("current")
_Pm253PerfTelecomLinePast24StatHistoryInvCvPort1_Type = EkiOnOff
_Pm253PerfTelecomLinePast24StatHistoryInvCvPort1_Object = MibTableColumn
pm253PerfTelecomLinePast24StatHistoryInvCvPort1 = _Pm253PerfTelecomLinePast24StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 131, 1, 2),
    _Pm253PerfTelecomLinePast24StatHistoryInvCvPort1_Type()
)
pm253PerfTelecomLinePast24StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast24StatHistoryInvCvPort1.setStatus("current")
_Pm253PerfTelecomLinePast24StatHistoryCvValuePort1_Type = Unsigned32
_Pm253PerfTelecomLinePast24StatHistoryCvValuePort1_Object = MibTableColumn
pm253PerfTelecomLinePast24StatHistoryCvValuePort1 = _Pm253PerfTelecomLinePast24StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 131, 1, 3),
    _Pm253PerfTelecomLinePast24StatHistoryCvValuePort1_Type()
)
pm253PerfTelecomLinePast24StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast24StatHistoryCvValuePort1.setStatus("current")
_Pm253PerfTelecomLinePast24StatHistoryInvEsPort1_Type = EkiOnOff
_Pm253PerfTelecomLinePast24StatHistoryInvEsPort1_Object = MibTableColumn
pm253PerfTelecomLinePast24StatHistoryInvEsPort1 = _Pm253PerfTelecomLinePast24StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 131, 1, 4),
    _Pm253PerfTelecomLinePast24StatHistoryInvEsPort1_Type()
)
pm253PerfTelecomLinePast24StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast24StatHistoryInvEsPort1.setStatus("current")
_Pm253PerfTelecomLinePast24StatHistoryEsValuePort1_Type = Unsigned32
_Pm253PerfTelecomLinePast24StatHistoryEsValuePort1_Object = MibTableColumn
pm253PerfTelecomLinePast24StatHistoryEsValuePort1 = _Pm253PerfTelecomLinePast24StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 131, 1, 5),
    _Pm253PerfTelecomLinePast24StatHistoryEsValuePort1_Type()
)
pm253PerfTelecomLinePast24StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast24StatHistoryEsValuePort1.setStatus("current")
_Pm253PerfTelecomLinePast24StatHistoryInvSesPort1_Type = EkiOnOff
_Pm253PerfTelecomLinePast24StatHistoryInvSesPort1_Object = MibTableColumn
pm253PerfTelecomLinePast24StatHistoryInvSesPort1 = _Pm253PerfTelecomLinePast24StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 131, 1, 6),
    _Pm253PerfTelecomLinePast24StatHistoryInvSesPort1_Type()
)
pm253PerfTelecomLinePast24StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast24StatHistoryInvSesPort1.setStatus("current")
_Pm253PerfTelecomLinePast24StatHistorySesValuePort1_Type = Unsigned32
_Pm253PerfTelecomLinePast24StatHistorySesValuePort1_Object = MibTableColumn
pm253PerfTelecomLinePast24StatHistorySesValuePort1 = _Pm253PerfTelecomLinePast24StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 131, 1, 7),
    _Pm253PerfTelecomLinePast24StatHistorySesValuePort1_Type()
)
pm253PerfTelecomLinePast24StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast24StatHistorySesValuePort1.setStatus("current")
_Pm253PerfTelecomLinePast24StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm253PerfTelecomLinePast24StatHistoryInvSefsPort1_Object = MibTableColumn
pm253PerfTelecomLinePast24StatHistoryInvSefsPort1 = _Pm253PerfTelecomLinePast24StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 131, 1, 8),
    _Pm253PerfTelecomLinePast24StatHistoryInvSefsPort1_Type()
)
pm253PerfTelecomLinePast24StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast24StatHistoryInvSefsPort1.setStatus("current")
_Pm253PerfTelecomLinePast24StatHistorySefsValuePort1_Type = Unsigned32
_Pm253PerfTelecomLinePast24StatHistorySefsValuePort1_Object = MibTableColumn
pm253PerfTelecomLinePast24StatHistorySefsValuePort1 = _Pm253PerfTelecomLinePast24StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 131, 1, 9),
    _Pm253PerfTelecomLinePast24StatHistorySefsValuePort1_Type()
)
pm253PerfTelecomLinePast24StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast24StatHistorySefsValuePort1.setStatus("current")
_Pm253PerfTelecomLinePast24StatHistoryInvUasPort1_Type = EkiOnOff
_Pm253PerfTelecomLinePast24StatHistoryInvUasPort1_Object = MibTableColumn
pm253PerfTelecomLinePast24StatHistoryInvUasPort1 = _Pm253PerfTelecomLinePast24StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 131, 1, 10),
    _Pm253PerfTelecomLinePast24StatHistoryInvUasPort1_Type()
)
pm253PerfTelecomLinePast24StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast24StatHistoryInvUasPort1.setStatus("current")
_Pm253PerfTelecomLinePast24StatHistoryUasValuePort1_Type = Unsigned32
_Pm253PerfTelecomLinePast24StatHistoryUasValuePort1_Object = MibTableColumn
pm253PerfTelecomLinePast24StatHistoryUasValuePort1 = _Pm253PerfTelecomLinePast24StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 131, 1, 11),
    _Pm253PerfTelecomLinePast24StatHistoryUasValuePort1_Type()
)
pm253PerfTelecomLinePast24StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast24StatHistoryUasValuePort1.setStatus("current")
_Pm253PerfTelecomLinePast15StatHistoryPort2Table_Object = MibTable
pm253PerfTelecomLinePast15StatHistoryPort2Table = _Pm253PerfTelecomLinePast15StatHistoryPort2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 145)
)
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast15StatHistoryPort2Table.setStatus("current")
_Pm253PerfTelecomLinePast15StatHistoryPort2Entry_Object = MibTableRow
pm253PerfTelecomLinePast15StatHistoryPort2Entry = _Pm253PerfTelecomLinePast15StatHistoryPort2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 145, 1)
)
pm253PerfTelecomLinePast15StatHistoryPort2Entry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253PerfTelecomLinePast15StatHistoryPort2Index"),
)
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast15StatHistoryPort2Entry.setStatus("current")


class _Pm253PerfTelecomLinePast15StatHistoryPort2Index_Type(Integer32):
    """Custom type pm253PerfTelecomLinePast15StatHistoryPort2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253PerfTelecomLinePast15StatHistoryPort2Index_Type.__name__ = "Integer32"
_Pm253PerfTelecomLinePast15StatHistoryPort2Index_Object = MibTableColumn
pm253PerfTelecomLinePast15StatHistoryPort2Index = _Pm253PerfTelecomLinePast15StatHistoryPort2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 145, 1, 1),
    _Pm253PerfTelecomLinePast15StatHistoryPort2Index_Type()
)
pm253PerfTelecomLinePast15StatHistoryPort2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast15StatHistoryPort2Index.setStatus("current")
_Pm253PerfTelecomLinePast15StatHistoryInvCvPort2_Type = EkiOnOff
_Pm253PerfTelecomLinePast15StatHistoryInvCvPort2_Object = MibTableColumn
pm253PerfTelecomLinePast15StatHistoryInvCvPort2 = _Pm253PerfTelecomLinePast15StatHistoryInvCvPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 145, 1, 2),
    _Pm253PerfTelecomLinePast15StatHistoryInvCvPort2_Type()
)
pm253PerfTelecomLinePast15StatHistoryInvCvPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast15StatHistoryInvCvPort2.setStatus("current")
_Pm253PerfTelecomLinePast15StatHistoryCvValuePort2_Type = Unsigned32
_Pm253PerfTelecomLinePast15StatHistoryCvValuePort2_Object = MibTableColumn
pm253PerfTelecomLinePast15StatHistoryCvValuePort2 = _Pm253PerfTelecomLinePast15StatHistoryCvValuePort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 145, 1, 3),
    _Pm253PerfTelecomLinePast15StatHistoryCvValuePort2_Type()
)
pm253PerfTelecomLinePast15StatHistoryCvValuePort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast15StatHistoryCvValuePort2.setStatus("current")
_Pm253PerfTelecomLinePast15StatHistoryInvEsPort2_Type = EkiOnOff
_Pm253PerfTelecomLinePast15StatHistoryInvEsPort2_Object = MibTableColumn
pm253PerfTelecomLinePast15StatHistoryInvEsPort2 = _Pm253PerfTelecomLinePast15StatHistoryInvEsPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 145, 1, 4),
    _Pm253PerfTelecomLinePast15StatHistoryInvEsPort2_Type()
)
pm253PerfTelecomLinePast15StatHistoryInvEsPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast15StatHistoryInvEsPort2.setStatus("current")
_Pm253PerfTelecomLinePast15StatHistoryEsValuePort2_Type = Unsigned32
_Pm253PerfTelecomLinePast15StatHistoryEsValuePort2_Object = MibTableColumn
pm253PerfTelecomLinePast15StatHistoryEsValuePort2 = _Pm253PerfTelecomLinePast15StatHistoryEsValuePort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 145, 1, 5),
    _Pm253PerfTelecomLinePast15StatHistoryEsValuePort2_Type()
)
pm253PerfTelecomLinePast15StatHistoryEsValuePort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast15StatHistoryEsValuePort2.setStatus("current")
_Pm253PerfTelecomLinePast15StatHistoryInvSesPort2_Type = EkiOnOff
_Pm253PerfTelecomLinePast15StatHistoryInvSesPort2_Object = MibTableColumn
pm253PerfTelecomLinePast15StatHistoryInvSesPort2 = _Pm253PerfTelecomLinePast15StatHistoryInvSesPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 145, 1, 6),
    _Pm253PerfTelecomLinePast15StatHistoryInvSesPort2_Type()
)
pm253PerfTelecomLinePast15StatHistoryInvSesPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast15StatHistoryInvSesPort2.setStatus("current")
_Pm253PerfTelecomLinePast15StatHistorySesValuePort2_Type = Unsigned32
_Pm253PerfTelecomLinePast15StatHistorySesValuePort2_Object = MibTableColumn
pm253PerfTelecomLinePast15StatHistorySesValuePort2 = _Pm253PerfTelecomLinePast15StatHistorySesValuePort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 145, 1, 7),
    _Pm253PerfTelecomLinePast15StatHistorySesValuePort2_Type()
)
pm253PerfTelecomLinePast15StatHistorySesValuePort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast15StatHistorySesValuePort2.setStatus("current")
_Pm253PerfTelecomLinePast15StatHistoryInvSefsPort2_Type = EkiOnOff
_Pm253PerfTelecomLinePast15StatHistoryInvSefsPort2_Object = MibTableColumn
pm253PerfTelecomLinePast15StatHistoryInvSefsPort2 = _Pm253PerfTelecomLinePast15StatHistoryInvSefsPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 145, 1, 8),
    _Pm253PerfTelecomLinePast15StatHistoryInvSefsPort2_Type()
)
pm253PerfTelecomLinePast15StatHistoryInvSefsPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast15StatHistoryInvSefsPort2.setStatus("current")
_Pm253PerfTelecomLinePast15StatHistorySefsValuePort2_Type = Unsigned32
_Pm253PerfTelecomLinePast15StatHistorySefsValuePort2_Object = MibTableColumn
pm253PerfTelecomLinePast15StatHistorySefsValuePort2 = _Pm253PerfTelecomLinePast15StatHistorySefsValuePort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 145, 1, 9),
    _Pm253PerfTelecomLinePast15StatHistorySefsValuePort2_Type()
)
pm253PerfTelecomLinePast15StatHistorySefsValuePort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast15StatHistorySefsValuePort2.setStatus("current")
_Pm253PerfTelecomLinePast15StatHistoryInvUasPort2_Type = EkiOnOff
_Pm253PerfTelecomLinePast15StatHistoryInvUasPort2_Object = MibTableColumn
pm253PerfTelecomLinePast15StatHistoryInvUasPort2 = _Pm253PerfTelecomLinePast15StatHistoryInvUasPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 145, 1, 10),
    _Pm253PerfTelecomLinePast15StatHistoryInvUasPort2_Type()
)
pm253PerfTelecomLinePast15StatHistoryInvUasPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast15StatHistoryInvUasPort2.setStatus("current")
_Pm253PerfTelecomLinePast15StatHistoryUasValuePort2_Type = Unsigned32
_Pm253PerfTelecomLinePast15StatHistoryUasValuePort2_Object = MibTableColumn
pm253PerfTelecomLinePast15StatHistoryUasValuePort2 = _Pm253PerfTelecomLinePast15StatHistoryUasValuePort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 145, 1, 11),
    _Pm253PerfTelecomLinePast15StatHistoryUasValuePort2_Type()
)
pm253PerfTelecomLinePast15StatHistoryUasValuePort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast15StatHistoryUasValuePort2.setStatus("current")
_Pm253PerfTelecomLinePast24StatHistoryPort2Table_Object = MibTable
pm253PerfTelecomLinePast24StatHistoryPort2Table = _Pm253PerfTelecomLinePast24StatHistoryPort2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 147)
)
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast24StatHistoryPort2Table.setStatus("current")
_Pm253PerfTelecomLinePast24StatHistoryPort2Entry_Object = MibTableRow
pm253PerfTelecomLinePast24StatHistoryPort2Entry = _Pm253PerfTelecomLinePast24StatHistoryPort2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 147, 1)
)
pm253PerfTelecomLinePast24StatHistoryPort2Entry.setIndexNames(
    (0, "EKINOPS-Pm253-MIB", "pm253PerfTelecomLinePast24StatHistoryPort2Index"),
)
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast24StatHistoryPort2Entry.setStatus("current")


class _Pm253PerfTelecomLinePast24StatHistoryPort2Index_Type(Integer32):
    """Custom type pm253PerfTelecomLinePast24StatHistoryPort2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm253PerfTelecomLinePast24StatHistoryPort2Index_Type.__name__ = "Integer32"
_Pm253PerfTelecomLinePast24StatHistoryPort2Index_Object = MibTableColumn
pm253PerfTelecomLinePast24StatHistoryPort2Index = _Pm253PerfTelecomLinePast24StatHistoryPort2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 147, 1, 1),
    _Pm253PerfTelecomLinePast24StatHistoryPort2Index_Type()
)
pm253PerfTelecomLinePast24StatHistoryPort2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast24StatHistoryPort2Index.setStatus("current")
_Pm253PerfTelecomLinePast24StatHistoryInvCvPort2_Type = EkiOnOff
_Pm253PerfTelecomLinePast24StatHistoryInvCvPort2_Object = MibTableColumn
pm253PerfTelecomLinePast24StatHistoryInvCvPort2 = _Pm253PerfTelecomLinePast24StatHistoryInvCvPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 147, 1, 2),
    _Pm253PerfTelecomLinePast24StatHistoryInvCvPort2_Type()
)
pm253PerfTelecomLinePast24StatHistoryInvCvPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast24StatHistoryInvCvPort2.setStatus("current")
_Pm253PerfTelecomLinePast24StatHistoryCvValuePort2_Type = Unsigned32
_Pm253PerfTelecomLinePast24StatHistoryCvValuePort2_Object = MibTableColumn
pm253PerfTelecomLinePast24StatHistoryCvValuePort2 = _Pm253PerfTelecomLinePast24StatHistoryCvValuePort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 147, 1, 3),
    _Pm253PerfTelecomLinePast24StatHistoryCvValuePort2_Type()
)
pm253PerfTelecomLinePast24StatHistoryCvValuePort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast24StatHistoryCvValuePort2.setStatus("current")
_Pm253PerfTelecomLinePast24StatHistoryInvEsPort2_Type = EkiOnOff
_Pm253PerfTelecomLinePast24StatHistoryInvEsPort2_Object = MibTableColumn
pm253PerfTelecomLinePast24StatHistoryInvEsPort2 = _Pm253PerfTelecomLinePast24StatHistoryInvEsPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 147, 1, 4),
    _Pm253PerfTelecomLinePast24StatHistoryInvEsPort2_Type()
)
pm253PerfTelecomLinePast24StatHistoryInvEsPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast24StatHistoryInvEsPort2.setStatus("current")
_Pm253PerfTelecomLinePast24StatHistoryEsValuePort2_Type = Unsigned32
_Pm253PerfTelecomLinePast24StatHistoryEsValuePort2_Object = MibTableColumn
pm253PerfTelecomLinePast24StatHistoryEsValuePort2 = _Pm253PerfTelecomLinePast24StatHistoryEsValuePort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 147, 1, 5),
    _Pm253PerfTelecomLinePast24StatHistoryEsValuePort2_Type()
)
pm253PerfTelecomLinePast24StatHistoryEsValuePort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast24StatHistoryEsValuePort2.setStatus("current")
_Pm253PerfTelecomLinePast24StatHistoryInvSesPort2_Type = EkiOnOff
_Pm253PerfTelecomLinePast24StatHistoryInvSesPort2_Object = MibTableColumn
pm253PerfTelecomLinePast24StatHistoryInvSesPort2 = _Pm253PerfTelecomLinePast24StatHistoryInvSesPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 147, 1, 6),
    _Pm253PerfTelecomLinePast24StatHistoryInvSesPort2_Type()
)
pm253PerfTelecomLinePast24StatHistoryInvSesPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast24StatHistoryInvSesPort2.setStatus("current")
_Pm253PerfTelecomLinePast24StatHistorySesValuePort2_Type = Unsigned32
_Pm253PerfTelecomLinePast24StatHistorySesValuePort2_Object = MibTableColumn
pm253PerfTelecomLinePast24StatHistorySesValuePort2 = _Pm253PerfTelecomLinePast24StatHistorySesValuePort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 147, 1, 7),
    _Pm253PerfTelecomLinePast24StatHistorySesValuePort2_Type()
)
pm253PerfTelecomLinePast24StatHistorySesValuePort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast24StatHistorySesValuePort2.setStatus("current")
_Pm253PerfTelecomLinePast24StatHistoryInvSefsPort2_Type = EkiOnOff
_Pm253PerfTelecomLinePast24StatHistoryInvSefsPort2_Object = MibTableColumn
pm253PerfTelecomLinePast24StatHistoryInvSefsPort2 = _Pm253PerfTelecomLinePast24StatHistoryInvSefsPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 147, 1, 8),
    _Pm253PerfTelecomLinePast24StatHistoryInvSefsPort2_Type()
)
pm253PerfTelecomLinePast24StatHistoryInvSefsPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast24StatHistoryInvSefsPort2.setStatus("current")
_Pm253PerfTelecomLinePast24StatHistorySefsValuePort2_Type = Unsigned32
_Pm253PerfTelecomLinePast24StatHistorySefsValuePort2_Object = MibTableColumn
pm253PerfTelecomLinePast24StatHistorySefsValuePort2 = _Pm253PerfTelecomLinePast24StatHistorySefsValuePort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 147, 1, 9),
    _Pm253PerfTelecomLinePast24StatHistorySefsValuePort2_Type()
)
pm253PerfTelecomLinePast24StatHistorySefsValuePort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast24StatHistorySefsValuePort2.setStatus("current")
_Pm253PerfTelecomLinePast24StatHistoryInvUasPort2_Type = EkiOnOff
_Pm253PerfTelecomLinePast24StatHistoryInvUasPort2_Object = MibTableColumn
pm253PerfTelecomLinePast24StatHistoryInvUasPort2 = _Pm253PerfTelecomLinePast24StatHistoryInvUasPort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 147, 1, 10),
    _Pm253PerfTelecomLinePast24StatHistoryInvUasPort2_Type()
)
pm253PerfTelecomLinePast24StatHistoryInvUasPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast24StatHistoryInvUasPort2.setStatus("current")
_Pm253PerfTelecomLinePast24StatHistoryUasValuePort2_Type = Unsigned32
_Pm253PerfTelecomLinePast24StatHistoryUasValuePort2_Object = MibTableColumn
pm253PerfTelecomLinePast24StatHistoryUasValuePort2 = _Pm253PerfTelecomLinePast24StatHistoryUasValuePort2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 13, 11, 3, 147, 1, 11),
    _Pm253PerfTelecomLinePast24StatHistoryUasValuePort2_Type()
)
pm253PerfTelecomLinePast24StatHistoryUasValuePort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm253PerfTelecomLinePast24StatHistoryUasValuePort2.setStatus("current")

# Managed Objects groups


# Notification objects

pm253LineTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 13, 10, 30)
)
pm253LineTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm253-MIB", "pm253AlmLineDdmWarningPortn"),
        ("EKINOPS-Pm253-MIB", "pm253TrapLineNumber"),
        ("EKINOPS-Pm253-MIB", "pm253TrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm253LineTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm253LineTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 13, 10, 31)
)
pm253LineTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm253-MIB", "pm253AlmLineDdmWarningPortn"),
        ("EKINOPS-Pm253-MIB", "pm253TrapLineNumber"),
        ("EKINOPS-Pm253-MIB", "pm253TrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm253LineTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm253LineTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 13, 10, 32)
)
pm253LineTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm253-MIB", "pm253AlmLineDdmAlmPortn"),
        ("EKINOPS-Pm253-MIB", "pm253TrapLineNumber"),
        ("EKINOPS-Pm253-MIB", "pm253TrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm253LineTrapUrgentGoesOn.setStatus(
        "current"
    )

pm253LineTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 13, 10, 33)
)
pm253LineTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm253-MIB", "pm253AlmLineDdmAlmPortn"),
        ("EKINOPS-Pm253-MIB", "pm253TrapLineNumber"),
        ("EKINOPS-Pm253-MIB", "pm253TrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm253LineTrapUrgentGoesOff.setStatus(
        "current"
    )

pm253LineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 13, 10, 34)
)
pm253LineTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm253-MIB", "pm253AlmLineFailPortn"),
        ("EKINOPS-Pm253-MIB", "pm253AlmLineHwFailPortn"),
        ("EKINOPS-Pm253-MIB", "pm253AlmLineActivePortn"),
        ("EKINOPS-Pm253-MIB", "pm253TrapLineNumber"),
        ("EKINOPS-Pm253-MIB", "pm253TrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm253LineTrapCritGoesOn.setStatus(
        "current"
    )

pm253LineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 13, 10, 35)
)
pm253LineTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm253-MIB", "pm253AlmLineFailPortn"),
        ("EKINOPS-Pm253-MIB", "pm253AlmLineHwFailPortn"),
        ("EKINOPS-Pm253-MIB", "pm253AlmLineActivePortn"),
        ("EKINOPS-Pm253-MIB", "pm253TrapLineNumber"),
        ("EKINOPS-Pm253-MIB", "pm253TrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm253LineTrapCritGoesOff.setStatus(
        "current"
    )

pm253PortnTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 13, 10, 40)
)
pm253PortnTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm253-MIB", "pm253AlmClientSfpDdmWarningPortn"),
        ("EKINOPS-Pm253-MIB", "pm253TrapPortNumber"),
        ("EKINOPS-Pm253-MIB", "pm253TrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm253PortnTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm253PortnTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 13, 10, 41)
)
pm253PortnTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm253-MIB", "pm253AlmClientSfpDdmWarningPortn"),
        ("EKINOPS-Pm253-MIB", "pm253TrapPortNumber"),
        ("EKINOPS-Pm253-MIB", "pm253TrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm253PortnTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm253PortnTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 13, 10, 42)
)
pm253PortnTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm253-MIB", "pm253AlmClientSfpDdmAlmPortn"),
        ("EKINOPS-Pm253-MIB", "pm253TrapPortNumber"),
        ("EKINOPS-Pm253-MIB", "pm253TrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm253PortnTrapUrgentGoesOn.setStatus(
        "current"
    )

pm253PortnTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 13, 10, 43)
)
pm253PortnTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm253-MIB", "pm253AlmClientSfpDdmAlmPortn"),
        ("EKINOPS-Pm253-MIB", "pm253TrapPortNumber"),
        ("EKINOPS-Pm253-MIB", "pm253TrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm253PortnTrapUrgentGoesOff.setStatus(
        "current"
    )

pm253PortnTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 13, 10, 44)
)
pm253PortnTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm253-MIB", "pm253AlmClientFailAccPortn"),
        ("EKINOPS-Pm253-MIB", "pm253AlmClientHwFailAccPortn"),
        ("EKINOPS-Pm253-MIB", "pm253TrapPortNumber"),
        ("EKINOPS-Pm253-MIB", "pm253TrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm253PortnTrapCritGoesOn.setStatus(
        "current"
    )

pm253PortnTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 13, 10, 45)
)
pm253PortnTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm253-MIB", "pm253AlmClientFailAccPortn"),
        ("EKINOPS-Pm253-MIB", "pm253AlmClientHwFailAccPortn"),
        ("EKINOPS-Pm253-MIB", "pm253TrapPortNumber"),
        ("EKINOPS-Pm253-MIB", "pm253TrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm253PortnTrapCritGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Pm253-MIB",
    **{"modulePm253": modulePm253,
       "pm253alarms": pm253alarms,
       "pm253AlmOther": pm253AlmOther,
       "pm253AlmOtherNurg": pm253AlmOtherNurg,
       "pm253AlmsynthAlm0": pm253AlmsynthAlm0,
       "pm253AlmModGlobFail": pm253AlmModGlobFail,
       "pm253AlmDefFuseA": pm253AlmDefFuseA,
       "pm253AlmDefFuseB": pm253AlmDefFuseB,
       "pm253AlmsynthAlm2": pm253AlmsynthAlm2,
       "pm253AlmConfTableSave": pm253AlmConfTableSave,
       "pm253AlmInvUpload": pm253AlmInvUpload,
       "pm253AlmConfTableLoad": pm253AlmConfTableLoad,
       "pm253AlmCorrelatOff": pm253AlmCorrelatOff,
       "pm253AlmMaintenanceOn": pm253AlmMaintenanceOn,
       "pm253AlmOtherUrg": pm253AlmOtherUrg,
       "pm253AlmmodInitFailLevel2": pm253AlmmodInitFailLevel2,
       "pm253AlmLedFail": pm253AlmLedFail,
       "pm253AlmNextColdBootForced": pm253AlmNextColdBootForced,
       "pm253AlmBootUndone": pm253AlmBootUndone,
       "pm253AlmResetHwInitFail": pm253AlmResetHwInitFail,
       "pm253AlmSwInitFail": pm253AlmSwInitFail,
       "pm253AlmmodInitFailLevel3": pm253AlmmodInitFailLevel3,
       "pm253AlmGwIdentFail": pm253AlmGwIdentFail,
       "pm253AlmObmTypeReadFail": pm253AlmObmTypeReadFail,
       "pm253AlmInitModuleFail": pm253AlmInitModuleFail,
       "pm253AlmSfp1InitFail": pm253AlmSfp1InitFail,
       "pm253AlmSfp2InitFail": pm253AlmSfp2InitFail,
       "pm253AlmLine1InitFail": pm253AlmLine1InitFail,
       "pm253AlmLine2InitFail": pm253AlmLine2InitFail,
       "pm253AlmClient1InitFail": pm253AlmClient1InitFail,
       "pm253AlmClient2InitFail": pm253AlmClient2InitFail,
       "pm253AlmClient3InitFail": pm253AlmClient3InitFail,
       "pm253AlmOtherCrit": pm253AlmOtherCrit,
       "pm253AlmPort": pm253AlmPort,
       "pm253AlmPortNurg": pm253AlmPortNurg,
       "pm253AlmclientSfpWarnDdmTable": pm253AlmclientSfpWarnDdmTable,
       "pm253AlmclientSfpWarnDdmEntry": pm253AlmclientSfpWarnDdmEntry,
       "pm253AlmclientSfpWarnDdmIndex": pm253AlmclientSfpWarnDdmIndex,
       "pm253AlmClientTxPwLowWngPortn": pm253AlmClientTxPwLowWngPortn,
       "pm253AlmClientTxPwrHighWngPortn": pm253AlmClientTxPwrHighWngPortn,
       "pm253AlmClientTxBiasLowWngPortn": pm253AlmClientTxBiasLowWngPortn,
       "pm253AlmClientTxBiasHighWngPortn": pm253AlmClientTxBiasHighWngPortn,
       "pm253AlmClientVccLowWngPortn": pm253AlmClientVccLowWngPortn,
       "pm253AlmClientVccHighWngPortn": pm253AlmClientVccHighWngPortn,
       "pm253AlmClientTempLowWngPortn": pm253AlmClientTempLowWngPortn,
       "pm253AlmClientTempHighWngPortn": pm253AlmClientTempHighWngPortn,
       "pm253AlmClientRxPwrLowWngPortn": pm253AlmClientRxPwrLowWngPortn,
       "pm253AlmClientRxPwrHighWngPortn": pm253AlmClientRxPwrHighWngPortn,
       "pm253AlmPortUrg": pm253AlmPortUrg,
       "pm253AlmclientSfpAlmDdmTable": pm253AlmclientSfpAlmDdmTable,
       "pm253AlmclientSfpAlmDdmEntry": pm253AlmclientSfpAlmDdmEntry,
       "pm253AlmclientSfpAlmDdmIndex": pm253AlmclientSfpAlmDdmIndex,
       "pm253AlmClientTxPwrLowAlaPortn": pm253AlmClientTxPwrLowAlaPortn,
       "pm253AlmClientTxPwrHighAlaPortn": pm253AlmClientTxPwrHighAlaPortn,
       "pm253AlmClientTxBiasLowAlaPortn": pm253AlmClientTxBiasLowAlaPortn,
       "pm253AlmClientTxBiasHighAlaPortn": pm253AlmClientTxBiasHighAlaPortn,
       "pm253AlmClientVccLowAlaPortn": pm253AlmClientVccLowAlaPortn,
       "pm253AlmClientVccHighAlaPortn": pm253AlmClientVccHighAlaPortn,
       "pm253AlmClientTempLowAlaPortn": pm253AlmClientTempLowAlaPortn,
       "pm253AlmClientTempHighAlaPortn": pm253AlmClientTempHighAlaPortn,
       "pm253AlmClientRxPwrLowAlaPortn": pm253AlmClientRxPwrLowAlaPortn,
       "pm253AlmClientRxPwrHighAlaPortn": pm253AlmClientRxPwrHighAlaPortn,
       "pm253AlmPortCrit": pm253AlmPortCrit,
       "pm253AlmsynthAlmClientTable": pm253AlmsynthAlmClientTable,
       "pm253AlmsynthAlmClientEntry": pm253AlmsynthAlmClientEntry,
       "pm253AlmsynthAlmClientIndex": pm253AlmsynthAlmClientIndex,
       "pm253AlmClientSfpAbsentPortn": pm253AlmClientSfpAbsentPortn,
       "pm253AlmClientDdmAbsentPortn": pm253AlmClientDdmAbsentPortn,
       "pm253AlmClientHwFailAccPortn": pm253AlmClientHwFailAccPortn,
       "pm253AlmClientLsdPortn": pm253AlmClientLsdPortn,
       "pm253AlmClientLocalOosPortn": pm253AlmClientLocalOosPortn,
       "pm253AlmClientRemoteOosPortn": pm253AlmClientRemoteOosPortn,
       "pm253AlmClientDwCaisPortn": pm253AlmClientDwCaisPortn,
       "pm253AlmClientSfpDdmWarningPortn": pm253AlmClientSfpDdmWarningPortn,
       "pm253AlmClientSfpDdmAlmPortn": pm253AlmClientSfpDdmAlmPortn,
       "pm253AlmClientFailAccPortn": pm253AlmClientFailAccPortn,
       "pm253AlmClientUpCsfPortn": pm253AlmClientUpCsfPortn,
       "pm253AlmaccessioAlmTable": pm253AlmaccessioAlmTable,
       "pm253AlmaccessioAlmEntry": pm253AlmaccessioAlmEntry,
       "pm253AlmaccessioAlmIndex": pm253AlmaccessioAlmIndex,
       "pm253AlmClientDwLasFailPortn": pm253AlmClientDwLasFailPortn,
       "pm253AlmClientUpLosPortn": pm253AlmClientUpLosPortn,
       "pm253AlmclientMapperDeAlmTable": pm253AlmclientMapperDeAlmTable,
       "pm253AlmclientMapperDeAlmEntry": pm253AlmclientMapperDeAlmEntry,
       "pm253AlmclientMapperDeAlmIndex": pm253AlmclientMapperDeAlmIndex,
       "pm253AlmClientUpAccOosPortn": pm253AlmClientUpAccOosPortn,
       "pm253AlmClientUpBufferOvlPortn": pm253AlmClientUpBufferOvlPortn,
       "pm253AlmClientDwCsfDetPortn": pm253AlmClientDwCsfDetPortn,
       "pm253AlmClientDwBufferOvlPortn": pm253AlmClientDwBufferOvlPortn,
       "pm253AlmClientLoopAccFifoFailPortn": pm253AlmClientLoopAccFifoFailPortn,
       "pm253AlmaccessioSdhAlarmTable": pm253AlmaccessioSdhAlarmTable,
       "pm253AlmaccessioSdhAlarmEntry": pm253AlmaccessioSdhAlarmEntry,
       "pm253AlmaccessioSdhAlarmIndex": pm253AlmaccessioSdhAlarmIndex,
       "pm253AlmLosTrscPortn": pm253AlmLosTrscPortn,
       "pm253AlmFifoErrPortn": pm253AlmFifoErrPortn,
       "pm253AlmRxLossOfLockPortn": pm253AlmRxLossOfLockPortn,
       "pm253AlmTxLossOfLockPortn": pm253AlmTxLossOfLockPortn,
       "pm253AlmClientAisDetPortn": pm253AlmClientAisDetPortn,
       "pm253AlmClientRdiDetPortn": pm253AlmClientRdiDetPortn,
       "pm253AlmClientOofPortn": pm253AlmClientOofPortn,
       "pm253AlmLine": pm253AlmLine,
       "pm253AlmLineNurg": pm253AlmLineNurg,
       "pm253AlmlineDownS1Table": pm253AlmlineDownS1Table,
       "pm253AlmlineDownS1Entry": pm253AlmlineDownS1Entry,
       "pm253AlmlineDownS1Index": pm253AlmlineDownS1Index,
       "pm253AlmlineDownS1Portn": pm253AlmlineDownS1Portn,
       "pm253AlmlineDownK1Table": pm253AlmlineDownK1Table,
       "pm253AlmlineDownK1Entry": pm253AlmlineDownK1Entry,
       "pm253AlmlineDownK1Index": pm253AlmlineDownK1Index,
       "pm253AlmlineDownK1Portn": pm253AlmlineDownK1Portn,
       "pm253AlmlineDownK2Table": pm253AlmlineDownK2Table,
       "pm253AlmlineDownK2Entry": pm253AlmlineDownK2Entry,
       "pm253AlmlineDownK2Index": pm253AlmlineDownK2Index,
       "pm253AlmlineDownK2Portn": pm253AlmlineDownK2Portn,
       "pm253AlmlineSfpWarnDdmTable": pm253AlmlineSfpWarnDdmTable,
       "pm253AlmlineSfpWarnDdmEntry": pm253AlmlineSfpWarnDdmEntry,
       "pm253AlmlineSfpWarnDdmIndex": pm253AlmlineSfpWarnDdmIndex,
       "pm253AlmLineTxPwLowWngPortn": pm253AlmLineTxPwLowWngPortn,
       "pm253AlmLineTxPwrHighWngPortn": pm253AlmLineTxPwrHighWngPortn,
       "pm253AlmLineTxBiasLowWngPortn": pm253AlmLineTxBiasLowWngPortn,
       "pm253AlmLineTxBiasHighWngPortn": pm253AlmLineTxBiasHighWngPortn,
       "pm253AlmLineVccLowWngPortn": pm253AlmLineVccLowWngPortn,
       "pm253AlmLineVccHighWngPortn": pm253AlmLineVccHighWngPortn,
       "pm253AlmLineTempLowWngPortn": pm253AlmLineTempLowWngPortn,
       "pm253AlmLineTempHighWngPortn": pm253AlmLineTempHighWngPortn,
       "pm253AlmLineRxPwrLowWngPortn": pm253AlmLineRxPwrLowWngPortn,
       "pm253AlmLineRxPwrHighWngPortn": pm253AlmLineRxPwrHighWngPortn,
       "pm253AlmLineUrg": pm253AlmLineUrg,
       "pm253AlmlineSfpAlaDdmTable": pm253AlmlineSfpAlaDdmTable,
       "pm253AlmlineSfpAlaDdmEntry": pm253AlmlineSfpAlaDdmEntry,
       "pm253AlmlineSfpAlaDdmIndex": pm253AlmlineSfpAlaDdmIndex,
       "pm253AlmLineTxPwrLowAlaPortn": pm253AlmLineTxPwrLowAlaPortn,
       "pm253AlmLineTxPwrHighAlaPortn": pm253AlmLineTxPwrHighAlaPortn,
       "pm253AlmLineTxBiasLowAlaPortn": pm253AlmLineTxBiasLowAlaPortn,
       "pm253AlmLineTxBiasHighAlaPortn": pm253AlmLineTxBiasHighAlaPortn,
       "pm253AlmLineVccLowAlaPortn": pm253AlmLineVccLowAlaPortn,
       "pm253AlmLineVccHighAlaPortn": pm253AlmLineVccHighAlaPortn,
       "pm253AlmLineTempLowAlaPortn": pm253AlmLineTempLowAlaPortn,
       "pm253AlmLineTempHighAlaPortn": pm253AlmLineTempHighAlaPortn,
       "pm253AlmLineRxPwrLowAlaPortn": pm253AlmLineRxPwrLowAlaPortn,
       "pm253AlmLineRxPwrHighAlaPortn": pm253AlmLineRxPwrHighAlaPortn,
       "pm253AlmLineCrit": pm253AlmLineCrit,
       "pm253AlmsynthAlmLineTable": pm253AlmsynthAlmLineTable,
       "pm253AlmsynthAlmLineEntry": pm253AlmsynthAlmLineEntry,
       "pm253AlmsynthAlmLineIndex": pm253AlmsynthAlmLineIndex,
       "pm253AlmLineSfpAbsentPortn": pm253AlmLineSfpAbsentPortn,
       "pm253AlmLineDdmAbsentPortn": pm253AlmLineDdmAbsentPortn,
       "pm253AlmLineHwFailPortn": pm253AlmLineHwFailPortn,
       "pm253AlmLineLsdPortn": pm253AlmLineLsdPortn,
       "pm253AlmLineLocalOosPortn": pm253AlmLineLocalOosPortn,
       "pm253AlmLineUpRdiInsPortn": pm253AlmLineUpRdiInsPortn,
       "pm253AlmLineDdmWarningPortn": pm253AlmLineDdmWarningPortn,
       "pm253AlmLineDdmAlmPortn": pm253AlmLineDdmAlmPortn,
       "pm253AlmLineFailPortn": pm253AlmLineFailPortn,
       "pm253AlmLineActivePortn": pm253AlmLineActivePortn,
       "pm253AlmlineDfrmAlmTable": pm253AlmlineDfrmAlmTable,
       "pm253AlmlineDfrmAlmEntry": pm253AlmlineDfrmAlmEntry,
       "pm253AlmlineDfrmAlmIndex": pm253AlmlineDfrmAlmIndex,
       "pm253AlmLineDwAisDetPortn": pm253AlmLineDwAisDetPortn,
       "pm253AlmLineDwRdiDetPortn": pm253AlmLineDwRdiDetPortn,
       "pm253AlmLineDwOofPortn": pm253AlmLineDwOofPortn,
       "pm253AlmLineDwLofPortn": pm253AlmLineDwLofPortn,
       "pm253AlmDwLopFirstPortn": pm253AlmDwLopFirstPortn,
       "pm253AlmDwAuAisFirstPortn": pm253AlmDwAuAisFirstPortn,
       "pm253AlmDwLopSecondPortn": pm253AlmDwLopSecondPortn,
       "pm253AlmDwAuAisSecondPortn": pm253AlmDwAuAisSecondPortn,
       "pm253AlmlineIoAlmTable": pm253AlmlineIoAlmTable,
       "pm253AlmlineIoAlmEntry": pm253AlmlineIoAlmEntry,
       "pm253AlmlineIoAlmIndex": pm253AlmlineIoAlmIndex,
       "pm253AlmLineUpLasFailPortn": pm253AlmLineUpLasFailPortn,
       "pm253AlmLineDwLosPortn": pm253AlmLineDwLosPortn,
       "pm253measures": pm253measures,
       "pm253MesrOther": pm253MesrOther,
       "pm253MesrPort": pm253MesrPort,
       "pm253MesrclientTempMeasTable": pm253MesrclientTempMeasTable,
       "pm253MesrclientTempMeasEntry": pm253MesrclientTempMeasEntry,
       "pm253MesrclientTempMeasIndex": pm253MesrclientTempMeasIndex,
       "pm253MesrclientTempMeasPortn": pm253MesrclientTempMeasPortn,
       "pm253MesrclientVoltMeasTable": pm253MesrclientVoltMeasTable,
       "pm253MesrclientVoltMeasEntry": pm253MesrclientVoltMeasEntry,
       "pm253MesrclientVoltMeasIndex": pm253MesrclientVoltMeasIndex,
       "pm253MesrclientVoltMeasPortn": pm253MesrclientVoltMeasPortn,
       "pm253MesrclientBiasMeasTable": pm253MesrclientBiasMeasTable,
       "pm253MesrclientBiasMeasEntry": pm253MesrclientBiasMeasEntry,
       "pm253MesrclientBiasMeasIndex": pm253MesrclientBiasMeasIndex,
       "pm253MesrclientBiasMeasPortn": pm253MesrclientBiasMeasPortn,
       "pm253MesrclientTxpwrMeasTable": pm253MesrclientTxpwrMeasTable,
       "pm253MesrclientTxpwrMeasEntry": pm253MesrclientTxpwrMeasEntry,
       "pm253MesrclientTxpwrMeasIndex": pm253MesrclientTxpwrMeasIndex,
       "pm253MesrclientTxpwrMeasPortn": pm253MesrclientTxpwrMeasPortn,
       "pm253MesrclientRxpwrMeasTable": pm253MesrclientRxpwrMeasTable,
       "pm253MesrclientRxpwrMeasEntry": pm253MesrclientRxpwrMeasEntry,
       "pm253MesrclientRxpwrMeasIndex": pm253MesrclientRxpwrMeasIndex,
       "pm253MesrclientRxpwrMeasPortn": pm253MesrclientRxpwrMeasPortn,
       "pm253MesrLine": pm253MesrLine,
       "pm253MesrlineTempMeasTable": pm253MesrlineTempMeasTable,
       "pm253MesrlineTempMeasEntry": pm253MesrlineTempMeasEntry,
       "pm253MesrlineTempMeasIndex": pm253MesrlineTempMeasIndex,
       "pm253MesrlineTempMeasPortn": pm253MesrlineTempMeasPortn,
       "pm253MesrlineVoltMeasTable": pm253MesrlineVoltMeasTable,
       "pm253MesrlineVoltMeasEntry": pm253MesrlineVoltMeasEntry,
       "pm253MesrlineVoltMeasIndex": pm253MesrlineVoltMeasIndex,
       "pm253MesrlineVoltMeasPortn": pm253MesrlineVoltMeasPortn,
       "pm253MesrlineBiasMeasTable": pm253MesrlineBiasMeasTable,
       "pm253MesrlineBiasMeasEntry": pm253MesrlineBiasMeasEntry,
       "pm253MesrlineBiasMeasIndex": pm253MesrlineBiasMeasIndex,
       "pm253MesrlineBiasMeasPortn": pm253MesrlineBiasMeasPortn,
       "pm253MesrlineTxpwrMeasTable": pm253MesrlineTxpwrMeasTable,
       "pm253MesrlineTxpwrMeasEntry": pm253MesrlineTxpwrMeasEntry,
       "pm253MesrlineTxpwrMeasIndex": pm253MesrlineTxpwrMeasIndex,
       "pm253MesrlineTxpwrMeasPortn": pm253MesrlineTxpwrMeasPortn,
       "pm253MesrlineRxpwrMeasTable": pm253MesrlineRxpwrMeasTable,
       "pm253MesrlineRxpwrMeasEntry": pm253MesrlineRxpwrMeasEntry,
       "pm253MesrlineRxpwrMeasIndex": pm253MesrlineRxpwrMeasIndex,
       "pm253MesrlineRxpwrMeasPortn": pm253MesrlineRxpwrMeasPortn,
       "pm253counters": pm253counters,
       "pm253CntOther": pm253CntOther,
       "pm253CntPort": pm253CntPort,
       "pm253CntclientUpRaRemCntTable": pm253CntclientUpRaRemCntTable,
       "pm253CntclientUpRaRemCntEntry": pm253CntclientUpRaRemCntEntry,
       "pm253CntclientUpRaRemCntIndex": pm253CntclientUpRaRemCntIndex,
       "pm253CntclientUpRaRemCntValuePortn": pm253CntclientUpRaRemCntValuePortn,
       "pm253CntclientUpRaRemCntErrorPortn": pm253CntclientUpRaRemCntErrorPortn,
       "pm253CntclientUpRaRemCntOverloadPortn": pm253CntclientUpRaRemCntOverloadPortn,
       "pm253CntclientUpRaInsCntTable": pm253CntclientUpRaInsCntTable,
       "pm253CntclientUpRaInsCntEntry": pm253CntclientUpRaInsCntEntry,
       "pm253CntclientUpRaInsCntIndex": pm253CntclientUpRaInsCntIndex,
       "pm253CntclientUpRaInsCntValuePortn": pm253CntclientUpRaInsCntValuePortn,
       "pm253CntclientUpRaInsCntErrorPortn": pm253CntclientUpRaInsCntErrorPortn,
       "pm253CntclientUpRaInsCntOverloadPortn": pm253CntclientUpRaInsCntOverloadPortn,
       "pm253CntclientUpDispErrCntTable": pm253CntclientUpDispErrCntTable,
       "pm253CntclientUpDispErrCntEntry": pm253CntclientUpDispErrCntEntry,
       "pm253CntclientUpDispErrCntIndex": pm253CntclientUpDispErrCntIndex,
       "pm253CntclientUpDispErrCntValuePortn": pm253CntclientUpDispErrCntValuePortn,
       "pm253CntclientUpDispErrCntErrorPortn": pm253CntclientUpDispErrCntErrorPortn,
       "pm253CntclientUpDispErrCntOverloadPortn": pm253CntclientUpDispErrCntOverloadPortn,
       "pm253CntclientUpTimCntTable": pm253CntclientUpTimCntTable,
       "pm253CntclientUpTimCntEntry": pm253CntclientUpTimCntEntry,
       "pm253CntclientUpTimCntIndex": pm253CntclientUpTimCntIndex,
       "pm253CntclientUpTimCntValuePortn": pm253CntclientUpTimCntValuePortn,
       "pm253CntclientUpTimCntErrorPortn": pm253CntclientUpTimCntErrorPortn,
       "pm253CntclientUpTimCntOverloadPortn": pm253CntclientUpTimCntOverloadPortn,
       "pm253CntclientDwCbipCntTable": pm253CntclientDwCbipCntTable,
       "pm253CntclientDwCbipCntEntry": pm253CntclientDwCbipCntEntry,
       "pm253CntclientDwCbipCntIndex": pm253CntclientDwCbipCntIndex,
       "pm253CntclientDwCbipCntValuePortn": pm253CntclientDwCbipCntValuePortn,
       "pm253CntclientDwCbipCntErrorPortn": pm253CntclientDwCbipCntErrorPortn,
       "pm253CntclientDwCbipCntOverloadPortn": pm253CntclientDwCbipCntOverloadPortn,
       "pm253CntclientDwTimCntTable": pm253CntclientDwTimCntTable,
       "pm253CntclientDwTimCntEntry": pm253CntclientDwTimCntEntry,
       "pm253CntclientDwTimCntIndex": pm253CntclientDwTimCntIndex,
       "pm253CntclientDwTimCntValuePortn": pm253CntclientDwTimCntValuePortn,
       "pm253CntclientDwTimCntErrorPortn": pm253CntclientDwTimCntErrorPortn,
       "pm253CntclientDwTimCntOverloadPortn": pm253CntclientDwTimCntOverloadPortn,
       "pm253CntLine": pm253CntLine,
       "pm253CntlineDfrmB1ErrCntTable": pm253CntlineDfrmB1ErrCntTable,
       "pm253CntlineDfrmB1ErrCntEntry": pm253CntlineDfrmB1ErrCntEntry,
       "pm253CntlineDfrmB1ErrCntIndex": pm253CntlineDfrmB1ErrCntIndex,
       "pm253CntlineDfrmB1ErrCntValuePortn": pm253CntlineDfrmB1ErrCntValuePortn,
       "pm253CntlineDfrmB1ErrCntErrorPortn": pm253CntlineDfrmB1ErrCntErrorPortn,
       "pm253CntlineDfrmB1ErrCntOverloadPortn": pm253CntlineDfrmB1ErrCntOverloadPortn,
       "pm253CntlineDfrmTimCntTable": pm253CntlineDfrmTimCntTable,
       "pm253CntlineDfrmTimCntEntry": pm253CntlineDfrmTimCntEntry,
       "pm253CntlineDfrmTimCntIndex": pm253CntlineDfrmTimCntIndex,
       "pm253CntlineDfrmTimCntValuePortn": pm253CntlineDfrmTimCntValuePortn,
       "pm253CntlineDfrmTimCntErrorPortn": pm253CntlineDfrmTimCntErrorPortn,
       "pm253CntlineDfrmTimCntOverloadPortn": pm253CntlineDfrmTimCntOverloadPortn,
       "pm253CntCountersReset": pm253CntCountersReset,
       "pm253CntCountersStop": pm253CntCountersStop,
       "pm253controlsWrite": pm253controlsWrite,
       "pm253CtrlOther": pm253CtrlOther,
       "pm253CtrlconfMgnt1": pm253CtrlconfMgnt1,
       "pm253CtrlConf1Load1": pm253CtrlConf1Load1,
       "pm253CtrlConf2Load1": pm253CtrlConf2Load1,
       "pm253CtrlConf2Flash1": pm253CtrlConf2Flash1,
       "pm253CtrlConf2Clear1": pm253CtrlConf2Clear1,
       "pm253Ctrlsynth4": pm253Ctrlsynth4,
       "pm253CtrlCorrelatOn": pm253CtrlCorrelatOn,
       "pm253CtrlCorrelatOff": pm253CtrlCorrelatOff,
       "pm253CtrlswMgnt": pm253CtrlswMgnt,
       "pm253CtrlColdReset": pm253CtrlColdReset,
       "pm253CtrlWarmReset": pm253CtrlWarmReset,
       "pm253CtrlLoadSwBank1": pm253CtrlLoadSwBank1,
       "pm253CtrlLoadSwBank2": pm253CtrlLoadSwBank2,
       "pm253CtrlgwMgnt": pm253CtrlgwMgnt,
       "pm253CtrlCurrentGwReset": pm253CtrlCurrentGwReset,
       "pm253CtrlLoadGwBank1": pm253CtrlLoadGwBank1,
       "pm253CtrlLoadGwBank2": pm253CtrlLoadGwBank2,
       "pm253CtrlLoadGwBank3": pm253CtrlLoadGwBank3,
       "pm253CtrlLoadGwBank4": pm253CtrlLoadGwBank4,
       "pm253CtrlledTest": pm253CtrlledTest,
       "pm253CtrlGreenLed": pm253CtrlGreenLed,
       "pm253CtrlRedLed": pm253CtrlRedLed,
       "pm253CtrlLedOff": pm253CtrlLedOff,
       "pm253CtrlmoduleOosMode": pm253CtrlmoduleOosMode,
       "pm253CtrlModuleOosMode": pm253CtrlModuleOosMode,
       "pm253CtrlclientPortMode": pm253CtrlclientPortMode,
       "pm253CtrlClientPortMode": pm253CtrlClientPortMode,
       "pm253CtrlmaintenanceMode": pm253CtrlmaintenanceMode,
       "pm253CtrlMaintenanceMode": pm253CtrlMaintenanceMode,
       "pm253CtrldccEnable": pm253CtrldccEnable,
       "pm253CtrlDccEnable": pm253CtrlDccEnable,
       "pm253CtrlPort": pm253CtrlPort,
       "pm253CtrlclientAccessLoopTable": pm253CtrlclientAccessLoopTable,
       "pm253CtrlclientAccessLoopEntry": pm253CtrlclientAccessLoopEntry,
       "pm253CtrlclientAccessLoopIndex": pm253CtrlclientAccessLoopIndex,
       "pm253CtrlclientAccessLoopPortn": pm253CtrlclientAccessLoopPortn,
       "pm253CtrlclientOosModeTable": pm253CtrlclientOosModeTable,
       "pm253CtrlclientOosModeEntry": pm253CtrlclientOosModeEntry,
       "pm253CtrlclientOosModeIndex": pm253CtrlclientOosModeIndex,
       "pm253CtrlclientOosModePortn": pm253CtrlclientOosModePortn,
       "pm253CtrlclientSfpOnOffCtrlTable": pm253CtrlclientSfpOnOffCtrlTable,
       "pm253CtrlclientSfpOnOffCtrlEntry": pm253CtrlclientSfpOnOffCtrlEntry,
       "pm253CtrlclientSfpOnOffCtrlIndex": pm253CtrlclientSfpOnOffCtrlIndex,
       "pm253CtrlclientSfpOnOffCtrlPortn": pm253CtrlclientSfpOnOffCtrlPortn,
       "pm253CtrlclientCsfUpInsTable": pm253CtrlclientCsfUpInsTable,
       "pm253CtrlclientCsfUpInsEntry": pm253CtrlclientCsfUpInsEntry,
       "pm253CtrlclientCsfUpInsIndex": pm253CtrlclientCsfUpInsIndex,
       "pm253CtrlclientCsfUpInsPortn": pm253CtrlclientCsfUpInsPortn,
       "pm253CtrlclientCaisDwInsTable": pm253CtrlclientCaisDwInsTable,
       "pm253CtrlclientCaisDwInsEntry": pm253CtrlclientCaisDwInsEntry,
       "pm253CtrlclientCaisDwInsIndex": pm253CtrlclientCaisDwInsIndex,
       "pm253CtrlclientCaisDwInsPortn": pm253CtrlclientCaisDwInsPortn,
       "pm253CtrlclientAccessTermLoopTable": pm253CtrlclientAccessTermLoopTable,
       "pm253CtrlclientAccessTermLoopEntry": pm253CtrlclientAccessTermLoopEntry,
       "pm253CtrlclientAccessTermLoopIndex": pm253CtrlclientAccessTermLoopIndex,
       "pm253CtrlclientAccessTermLoopPortn": pm253CtrlclientAccessTermLoopPortn,
       "pm253CtrlProtocolTable": pm253CtrlProtocolTable,
       "pm253CtrlProtocolEntry": pm253CtrlProtocolEntry,
       "pm253CtrlProtocolIndex": pm253CtrlProtocolIndex,
       "pm253CtrlProtocolPortn": pm253CtrlProtocolPortn,
       "pm253CtrlclientResetAllCountTable": pm253CtrlclientResetAllCountTable,
       "pm253CtrlclientResetAllCountEntry": pm253CtrlclientResetAllCountEntry,
       "pm253CtrlclientResetAllCountIndex": pm253CtrlclientResetAllCountIndex,
       "pm253CtrlclientResetAllCountsPortn": pm253CtrlclientResetAllCountsPortn,
       "pm253CtrlLine": pm253CtrlLine,
       "pm253Ctrlsts48c24c": pm253Ctrlsts48c24c,
       "pm253CtrlSts24cMode": pm253CtrlSts24cMode,
       "pm253CtrllineMsAis": pm253CtrllineMsAis,
       "pm253CtrlLineMsAis": pm253CtrlLineMsAis,
       "pm253CtrllineUpS1Table": pm253CtrllineUpS1Table,
       "pm253CtrllineUpS1Entry": pm253CtrllineUpS1Entry,
       "pm253CtrllineUpS1Index": pm253CtrllineUpS1Index,
       "pm253CtrllineUpS1Portn": pm253CtrllineUpS1Portn,
       "pm253CtrllineUpK1Table": pm253CtrllineUpK1Table,
       "pm253CtrllineUpK1Entry": pm253CtrllineUpK1Entry,
       "pm253CtrllineUpK1Index": pm253CtrllineUpK1Index,
       "pm253CtrllineUpK1Portn": pm253CtrllineUpK1Portn,
       "pm253CtrllineUpK2Table": pm253CtrllineUpK2Table,
       "pm253CtrllineUpK2Entry": pm253CtrllineUpK2Entry,
       "pm253CtrllineUpK2Index": pm253CtrllineUpK2Index,
       "pm253CtrllineUpK2Portn": pm253CtrllineUpK2Portn,
       "pm253CtrlProtMgnt": pm253CtrlProtMgnt,
       "pm253CtrlLineNumber": pm253CtrlLineNumber,
       "pm253CtrlProtMode": pm253CtrlProtMode,
       "pm253CtrllineOosModeTable": pm253CtrllineOosModeTable,
       "pm253CtrllineOosModeEntry": pm253CtrllineOosModeEntry,
       "pm253CtrllineOosModeIndex": pm253CtrllineOosModeIndex,
       "pm253CtrllineOosModePortn": pm253CtrllineOosModePortn,
       "pm253Ctrlk1K2Mgnt": pm253Ctrlk1K2Mgnt,
       "pm253CtrlK1K2Transparent": pm253CtrlK1K2Transparent,
       "pm253CtrlApsForceMode": pm253CtrlApsForceMode,
       "pm253CtrlApsForceModeLine1": pm253CtrlApsForceModeLine1,
       "pm253CtrlApsForceModeLine2": pm253CtrlApsForceModeLine2,
       "pm253CtrlApsManualMode": pm253CtrlApsManualMode,
       "pm253CtrlApsManualModeLine1": pm253CtrlApsManualModeLine1,
       "pm253CtrlApsManualModeLine2": pm253CtrlApsManualModeLine2,
       "pm253CtrlapsOtherModes": pm253CtrlapsOtherModes,
       "pm253CtrlLockout": pm253CtrlLockout,
       "pm253CtrlClear": pm253CtrlClear,
       "pm253CtrllineAccessLoopTable": pm253CtrllineAccessLoopTable,
       "pm253CtrllineAccessLoopEntry": pm253CtrllineAccessLoopEntry,
       "pm253CtrllineAccessLoopIndex": pm253CtrllineAccessLoopIndex,
       "pm253CtrllineAccessLoopPortn": pm253CtrllineAccessLoopPortn,
       "pm253CtrllineLoopTransceiverTable": pm253CtrllineLoopTransceiverTable,
       "pm253CtrllineLoopTransceiverEntry": pm253CtrllineLoopTransceiverEntry,
       "pm253CtrllineLoopTransceiverIndex": pm253CtrllineLoopTransceiverIndex,
       "pm253CtrllineLoopTransceiverPortn": pm253CtrllineLoopTransceiverPortn,
       "pm253CtrllineSfpOnOffCtrlTable": pm253CtrllineSfpOnOffCtrlTable,
       "pm253CtrllineSfpOnOffCtrlEntry": pm253CtrllineSfpOnOffCtrlEntry,
       "pm253CtrllineSfpOnOffCtrlIndex": pm253CtrllineSfpOnOffCtrlIndex,
       "pm253CtrllineSfpOnOffCtrlPortn": pm253CtrllineSfpOnOffCtrlPortn,
       "pm253CtrllineResetAllCountTable": pm253CtrllineResetAllCountTable,
       "pm253CtrllineResetAllCountEntry": pm253CtrllineResetAllCountEntry,
       "pm253CtrllineResetAllCountIndex": pm253CtrllineResetAllCountIndex,
       "pm253CtrllineResetAllCountsPortn": pm253CtrllineResetAllCountsPortn,
       "pm253ri": pm253ri,
       "pm253riTable": pm253riTable,
       "pm253RinvClientTable": pm253RinvClientTable,
       "pm253RinvClientEntry": pm253RinvClientEntry,
       "pm253RinvClientIndex": pm253RinvClientIndex,
       "pm253RinvSfpClient": pm253RinvSfpClient,
       "pm253RinvLineTable": pm253RinvLineTable,
       "pm253RinvLineEntry": pm253RinvLineEntry,
       "pm253RinvLineIndex": pm253RinvLineIndex,
       "pm253RinvsfpLine": pm253RinvsfpLine,
       "pm253RinvReloadInventory": pm253RinvReloadInventory,
       "pm253RinvHwPlatform": pm253RinvHwPlatform,
       "pm253RinvModulePlatform": pm253RinvModulePlatform,
       "pm253RinvSwPlatform": pm253RinvSwPlatform,
       "pm253RinvGwPlatform": pm253RinvGwPlatform,
       "pm253download": pm253download,
       "pm253DwlOther": pm253DwlOther,
       "pm253DwlrestartProcess": pm253DwlrestartProcess,
       "pm253DwlWarmRestartProcessed": pm253DwlWarmRestartProcessed,
       "pm253DwlColdRestartProcessed": pm253DwlColdRestartProcessed,
       "pm253DwlswBanksUsed": pm253DwlswBanksUsed,
       "pm253DwlSwBank1Used": pm253DwlSwBank1Used,
       "pm253DwlSwBank2Used": pm253DwlSwBank2Used,
       "pm253DwlSwBank1Notempty": pm253DwlSwBank1Notempty,
       "pm253DwlSwBank2Notempty": pm253DwlSwBank2Notempty,
       "pm253DwlgwBanksUsed": pm253DwlgwBanksUsed,
       "pm253DwlGwBank1Used": pm253DwlGwBank1Used,
       "pm253DwlGwBank2Used": pm253DwlGwBank2Used,
       "pm253DwlGwBank3Used": pm253DwlGwBank3Used,
       "pm253DwlGwBank4Used": pm253DwlGwBank4Used,
       "pm253DwlGwBank1Notempty": pm253DwlGwBank1Notempty,
       "pm253DwlGwBank2Notempty": pm253DwlGwBank2Notempty,
       "pm253DwlGwBank3Notempty": pm253DwlGwBank3Notempty,
       "pm253DwlGwBank4Notempty": pm253DwlGwBank4Notempty,
       "pm253DwlPort": pm253DwlPort,
       "pm253DwlLine": pm253DwlLine,
       "pm253Config": pm253Config,
       "pm253CfgAccessCAisCsf": pm253CfgAccessCAisCsf,
       "pm253CfgClientcaiscsfTable": pm253CfgClientcaiscsfTable,
       "pm253CfgClientcaiscsfEntry": pm253CfgClientcaiscsfEntry,
       "pm253CfgClientcaiscsfIndex": pm253CfgClientcaiscsfIndex,
       "pm253CfgCAisModePortn": pm253CfgCAisModePortn,
       "pm253CfgSts24cContribPortn": pm253CfgSts24cContribPortn,
       "pm253CfgUpAccessioAlmPortn": pm253CfgUpAccessioAlmPortn,
       "pm253CfgUpMapperDeAlmPortn": pm253CfgUpMapperDeAlmPortn,
       "pm253CfgDownMapperDeAlmPortn": pm253CfgDownMapperDeAlmPortn,
       "pm253CfgDownDfrmAlmPortn": pm253CfgDownDfrmAlmPortn,
       "pm253CfgDownLineIoAlmPortn": pm253CfgDownLineIoAlmPortn,
       "pm253CfgStartup": pm253CfgStartup,
       "pm253CfgClientStartupTable": pm253CfgClientStartupTable,
       "pm253CfgClientStartupEntry": pm253CfgClientStartupEntry,
       "pm253CfgClientStartupIndex": pm253CfgClientStartupIndex,
       "pm253CfgSystConfPortPortn": pm253CfgSystConfPortPortn,
       "pm253CfgNetConfPortPortn": pm253CfgNetConfPortPortn,
       "pm253CfgPortsOptionsPortn": pm253CfgPortsOptionsPortn,
       "pm253tablelineStartup": pm253tablelineStartup,
       "pm253CfgsystConfLine1": pm253CfgsystConfLine1,
       "pm253CfgsystConfLine2": pm253CfgsystConfLine2,
       "pm253CfglineSelection": pm253CfglineSelection,
       "pm253CfglineOptions": pm253CfglineOptions,
       "pm253CfgLabels": pm253CfgLabels,
       "pm253CfgLabelclientTable": pm253CfgLabelclientTable,
       "pm253CfgLabelclientEntry": pm253CfgLabelclientEntry,
       "pm253CfgLabelclientIndex": pm253CfgLabelclientIndex,
       "pm253CfgLabelclientPortn": pm253CfgLabelclientPortn,
       "pm253CfgLabellineTable": pm253CfgLabellineTable,
       "pm253CfgLabellineEntry": pm253CfgLabellineEntry,
       "pm253CfgLabellineIndex": pm253CfgLabellineIndex,
       "pm253CfgLabellinePortn": pm253CfgLabellinePortn,
       "pm253CfgWriteConfiguration": pm253CfgWriteConfiguration,
       "pm253traps": pm253traps,
       "pm253TrapPortNumber": pm253TrapPortNumber,
       "pm253TrapBoardNumber": pm253TrapBoardNumber,
       "pm253TrapLineNumber": pm253TrapLineNumber,
       "pm253LineTrapNotUrgentGoesOn": pm253LineTrapNotUrgentGoesOn,
       "pm253LineTrapNotUrgentGoesOff": pm253LineTrapNotUrgentGoesOff,
       "pm253LineTrapUrgentGoesOn": pm253LineTrapUrgentGoesOn,
       "pm253LineTrapUrgentGoesOff": pm253LineTrapUrgentGoesOff,
       "pm253LineTrapCritGoesOn": pm253LineTrapCritGoesOn,
       "pm253LineTrapCritGoesOff": pm253LineTrapCritGoesOff,
       "pm253PortnTrapNotUrgentGoesOn": pm253PortnTrapNotUrgentGoesOn,
       "pm253PortnTrapNotUrgentGoesOff": pm253PortnTrapNotUrgentGoesOff,
       "pm253PortnTrapUrgentGoesOn": pm253PortnTrapUrgentGoesOn,
       "pm253PortnTrapUrgentGoesOff": pm253PortnTrapUrgentGoesOff,
       "pm253PortnTrapCritGoesOn": pm253PortnTrapCritGoesOn,
       "pm253PortnTrapCritGoesOff": pm253PortnTrapCritGoesOff,
       "pm253Monitoring": pm253Monitoring,
       "pm253MonOther": pm253MonOther,
       "pm253MonSync": pm253MonSync,
       "pm253PerfEnable": pm253PerfEnable,
       "pm253Perf15minSync": pm253Perf15minSync,
       "pm253Perf24hSync": pm253Perf24hSync,
       "pm253MonTimeStamp": pm253MonTimeStamp,
       "pm253Perf15MinShort": pm253Perf15MinShort,
       "pm253Perf15MinLong": pm253Perf15MinLong,
       "pm253Perf24HoursShort": pm253Perf24HoursShort,
       "pm253Perf24HoursLong": pm253Perf24HoursLong,
       "pm253PerfCurrent15MinElapsedTime": pm253PerfCurrent15MinElapsedTime,
       "pm253PerfCurrent24HoursElapsedTime": pm253PerfCurrent24HoursElapsedTime,
       "pm253MonRmon": pm253MonRmon,
       "pm253MonCountersReset": pm253MonCountersReset,
       "pm253MonCountersStop": pm253MonCountersStop,
       "pm253MonClient": pm253MonClient,
       "pm253MonClientRmonCounter": pm253MonClientRmonCounter,
       "pm253MonupRmonByteCntTable": pm253MonupRmonByteCntTable,
       "pm253MonupRmonByteCntEntry": pm253MonupRmonByteCntEntry,
       "pm253MonupRmonByteCntIndex": pm253MonupRmonByteCntIndex,
       "pm253MonupRmonByteCntValuePortn": pm253MonupRmonByteCntValuePortn,
       "pm253MonupRmonByteCntErrorPortn": pm253MonupRmonByteCntErrorPortn,
       "pm253MonupRmonByteCntOverloadPortn": pm253MonupRmonByteCntOverloadPortn,
       "pm253MonupRmonCrcErrorCntTable": pm253MonupRmonCrcErrorCntTable,
       "pm253MonupRmonCrcErrorCntEntry": pm253MonupRmonCrcErrorCntEntry,
       "pm253MonupRmonCrcErrorCntIndex": pm253MonupRmonCrcErrorCntIndex,
       "pm253MonupRmonCrcErrorCntValuePortn": pm253MonupRmonCrcErrorCntValuePortn,
       "pm253MonupRmonCrcErrorCntErrorPortn": pm253MonupRmonCrcErrorCntErrorPortn,
       "pm253MonupRmonCrcErrorCntOverloadPortn": pm253MonupRmonCrcErrorCntOverloadPortn,
       "pm253MonupRmonPacketsCntTable": pm253MonupRmonPacketsCntTable,
       "pm253MonupRmonPacketsCntEntry": pm253MonupRmonPacketsCntEntry,
       "pm253MonupRmonPacketsCntIndex": pm253MonupRmonPacketsCntIndex,
       "pm253MonupRmonPacketsCntValuePortn": pm253MonupRmonPacketsCntValuePortn,
       "pm253MonupRmonPacketsCntErrorPortn": pm253MonupRmonPacketsCntErrorPortn,
       "pm253MonupRmonPacketsCntOverloadPortn": pm253MonupRmonPacketsCntOverloadPortn,
       "pm253MonupRmonBroadcastCntTable": pm253MonupRmonBroadcastCntTable,
       "pm253MonupRmonBroadcastCntEntry": pm253MonupRmonBroadcastCntEntry,
       "pm253MonupRmonBroadcastCntIndex": pm253MonupRmonBroadcastCntIndex,
       "pm253MonupRmonBroadcastCntValuePortn": pm253MonupRmonBroadcastCntValuePortn,
       "pm253MonupRmonBroadcastCntErrorPortn": pm253MonupRmonBroadcastCntErrorPortn,
       "pm253MonupRmonBroadcastCntOverloadPortn": pm253MonupRmonBroadcastCntOverloadPortn,
       "pm253MonupRmonMulticastCntTable": pm253MonupRmonMulticastCntTable,
       "pm253MonupRmonMulticastCntEntry": pm253MonupRmonMulticastCntEntry,
       "pm253MonupRmonMulticastCntIndex": pm253MonupRmonMulticastCntIndex,
       "pm253MonupRmonMulticastCntValuePortn": pm253MonupRmonMulticastCntValuePortn,
       "pm253MonupRmonMulticastCntErrorPortn": pm253MonupRmonMulticastCntErrorPortn,
       "pm253MonupRmonMulticastCntOverloadPortn": pm253MonupRmonMulticastCntOverloadPortn,
       "pm253MonupRmonTimerCntTable": pm253MonupRmonTimerCntTable,
       "pm253MonupRmonTimerCntEntry": pm253MonupRmonTimerCntEntry,
       "pm253MonupRmonTimerCntIndex": pm253MonupRmonTimerCntIndex,
       "pm253MonupRmonTimerCntValuePortn": pm253MonupRmonTimerCntValuePortn,
       "pm253MonupRmonTimerCntErrorPortn": pm253MonupRmonTimerCntErrorPortn,
       "pm253MonupRmonTimerCntOverloadPortn": pm253MonupRmonTimerCntOverloadPortn,
       "pm253MonupRmonPauseFrameCntTable": pm253MonupRmonPauseFrameCntTable,
       "pm253MonupRmonPauseFrameCntEntry": pm253MonupRmonPauseFrameCntEntry,
       "pm253MonupRmonPauseFrameCntIndex": pm253MonupRmonPauseFrameCntIndex,
       "pm253MonupRmonPauseFrameCntValuePortn": pm253MonupRmonPauseFrameCntValuePortn,
       "pm253MonupRmonPauseFrameCntErrorPortn": pm253MonupRmonPauseFrameCntErrorPortn,
       "pm253MonupRmonPauseFrameCntOverloadPortn": pm253MonupRmonPauseFrameCntOverloadPortn,
       "pm253MonupRmonDropFrameCntTable": pm253MonupRmonDropFrameCntTable,
       "pm253MonupRmonDropFrameCntEntry": pm253MonupRmonDropFrameCntEntry,
       "pm253MonupRmonDropFrameCntIndex": pm253MonupRmonDropFrameCntIndex,
       "pm253MonupRmonDropFrameCntValuePortn": pm253MonupRmonDropFrameCntValuePortn,
       "pm253MonupRmonDropFrameCntErrorPortn": pm253MonupRmonDropFrameCntErrorPortn,
       "pm253MonupRmonDropFrameCntOverloadPortn": pm253MonupRmonDropFrameCntOverloadPortn,
       "pm253MonupRmonBitsCntTable": pm253MonupRmonBitsCntTable,
       "pm253MonupRmonBitsCntEntry": pm253MonupRmonBitsCntEntry,
       "pm253MonupRmonBitsCntIndex": pm253MonupRmonBitsCntIndex,
       "pm253MonupRmonBitsCntValuePortn": pm253MonupRmonBitsCntValuePortn,
       "pm253MonupRmonBitsCntErrorPortn": pm253MonupRmonBitsCntErrorPortn,
       "pm253MonupRmonBitsCntOverloadPortn": pm253MonupRmonBitsCntOverloadPortn,
       "pm253MonupRmonUnicastCntTable": pm253MonupRmonUnicastCntTable,
       "pm253MonupRmonUnicastCntEntry": pm253MonupRmonUnicastCntEntry,
       "pm253MonupRmonUnicastCntIndex": pm253MonupRmonUnicastCntIndex,
       "pm253MonupRmonUnicastCntValuePortn": pm253MonupRmonUnicastCntValuePortn,
       "pm253MonupRmonUnicastCntErrorPortn": pm253MonupRmonUnicastCntErrorPortn,
       "pm253MonupRmonUnicastCntOverloadPortn": pm253MonupRmonUnicastCntOverloadPortn,
       "pm253MonupRmonNonUnicastCntTable": pm253MonupRmonNonUnicastCntTable,
       "pm253MonupRmonNonUnicastCntEntry": pm253MonupRmonNonUnicastCntEntry,
       "pm253MonupRmonNonUnicastCntIndex": pm253MonupRmonNonUnicastCntIndex,
       "pm253MonupRmonNonUnicastCntValuePortn": pm253MonupRmonNonUnicastCntValuePortn,
       "pm253MonupRmonNonUnicastCntErrorPortn": pm253MonupRmonNonUnicastCntErrorPortn,
       "pm253MonupRmonNonUnicastCntOverloadPortn": pm253MonupRmonNonUnicastCntOverloadPortn,
       "pm253MondwRmonByteCntTable": pm253MondwRmonByteCntTable,
       "pm253MondwRmonByteCntEntry": pm253MondwRmonByteCntEntry,
       "pm253MondwRmonByteCntIndex": pm253MondwRmonByteCntIndex,
       "pm253MondwRmonByteCntValuePortn": pm253MondwRmonByteCntValuePortn,
       "pm253MondwRmonByteCntErrorPortn": pm253MondwRmonByteCntErrorPortn,
       "pm253MondwRmonByteCntOverloadPortn": pm253MondwRmonByteCntOverloadPortn,
       "pm253MondwRmonCrcErrorCntTable": pm253MondwRmonCrcErrorCntTable,
       "pm253MondwRmonCrcErrorCntEntry": pm253MondwRmonCrcErrorCntEntry,
       "pm253MondwRmonCrcErrorCntIndex": pm253MondwRmonCrcErrorCntIndex,
       "pm253MondwRmonCrcErrorCntValuePortn": pm253MondwRmonCrcErrorCntValuePortn,
       "pm253MondwRmonCrcErrorCntErrorPortn": pm253MondwRmonCrcErrorCntErrorPortn,
       "pm253MondwRmonCrcErrorCntOverloadPortn": pm253MondwRmonCrcErrorCntOverloadPortn,
       "pm253MondwRmonPacketsCntTable": pm253MondwRmonPacketsCntTable,
       "pm253MondwRmonPacketsCntEntry": pm253MondwRmonPacketsCntEntry,
       "pm253MondwRmonPacketsCntIndex": pm253MondwRmonPacketsCntIndex,
       "pm253MondwRmonPacketsCntValuePortn": pm253MondwRmonPacketsCntValuePortn,
       "pm253MondwRmonPacketsCntErrorPortn": pm253MondwRmonPacketsCntErrorPortn,
       "pm253MondwRmonPacketsCntOverloadPortn": pm253MondwRmonPacketsCntOverloadPortn,
       "pm253MondwRmonBroadcastCntTable": pm253MondwRmonBroadcastCntTable,
       "pm253MondwRmonBroadcastCntEntry": pm253MondwRmonBroadcastCntEntry,
       "pm253MondwRmonBroadcastCntIndex": pm253MondwRmonBroadcastCntIndex,
       "pm253MondwRmonBroadcastCntValuePortn": pm253MondwRmonBroadcastCntValuePortn,
       "pm253MondwRmonBroadcastCntErrorPortn": pm253MondwRmonBroadcastCntErrorPortn,
       "pm253MondwRmonBroadcastCntOverloadPortn": pm253MondwRmonBroadcastCntOverloadPortn,
       "pm253MondwRmonMulticastCntTable": pm253MondwRmonMulticastCntTable,
       "pm253MondwRmonMulticastCntEntry": pm253MondwRmonMulticastCntEntry,
       "pm253MondwRmonMulticastCntIndex": pm253MondwRmonMulticastCntIndex,
       "pm253MondwRmonMulticastCntValuePortn": pm253MondwRmonMulticastCntValuePortn,
       "pm253MondwRmonMulticastCntErrorPortn": pm253MondwRmonMulticastCntErrorPortn,
       "pm253MondwRmonMulticastCntOverloadPortn": pm253MondwRmonMulticastCntOverloadPortn,
       "pm253MondwRmonPauseFrameCntTable": pm253MondwRmonPauseFrameCntTable,
       "pm253MondwRmonPauseFrameCntEntry": pm253MondwRmonPauseFrameCntEntry,
       "pm253MondwRmonPauseFrameCntIndex": pm253MondwRmonPauseFrameCntIndex,
       "pm253MondwRmonPauseFrameCntValuePortn": pm253MondwRmonPauseFrameCntValuePortn,
       "pm253MondwRmonPauseFrameCntErrorPortn": pm253MondwRmonPauseFrameCntErrorPortn,
       "pm253MondwRmonPauseFrameCntOverloadPortn": pm253MondwRmonPauseFrameCntOverloadPortn,
       "pm253MondwRmonTimerCntTable": pm253MondwRmonTimerCntTable,
       "pm253MondwRmonTimerCntEntry": pm253MondwRmonTimerCntEntry,
       "pm253MondwRmonTimerCntIndex": pm253MondwRmonTimerCntIndex,
       "pm253MondwRmonTimerCntValuePortn": pm253MondwRmonTimerCntValuePortn,
       "pm253MondwRmonTimerCntErrorPortn": pm253MondwRmonTimerCntErrorPortn,
       "pm253MondwRmonTimerCntOverloadPortn": pm253MondwRmonTimerCntOverloadPortn,
       "pm253MondwRmonBitsCntTable": pm253MondwRmonBitsCntTable,
       "pm253MondwRmonBitsCntEntry": pm253MondwRmonBitsCntEntry,
       "pm253MondwRmonBitsCntIndex": pm253MondwRmonBitsCntIndex,
       "pm253MondwRmonBitsCntValuePortn": pm253MondwRmonBitsCntValuePortn,
       "pm253MondwRmonBitsCntErrorPortn": pm253MondwRmonBitsCntErrorPortn,
       "pm253MondwRmonBitsCntOverloadPortn": pm253MondwRmonBitsCntOverloadPortn,
       "pm253MondwRmonUnicastCntTable": pm253MondwRmonUnicastCntTable,
       "pm253MondwRmonUnicastCntEntry": pm253MondwRmonUnicastCntEntry,
       "pm253MondwRmonUnicastCntIndex": pm253MondwRmonUnicastCntIndex,
       "pm253MondwRmonUnicastCntValuePortn": pm253MondwRmonUnicastCntValuePortn,
       "pm253MondwRmonUnicastCntErrorPortn": pm253MondwRmonUnicastCntErrorPortn,
       "pm253MondwRmonUnicastCntOverloadPortn": pm253MondwRmonUnicastCntOverloadPortn,
       "pm253MondwRmonNonUnicastCntTable": pm253MondwRmonNonUnicastCntTable,
       "pm253MondwRmonNonUnicastCntEntry": pm253MondwRmonNonUnicastCntEntry,
       "pm253MondwRmonNonUnicastCntIndex": pm253MondwRmonNonUnicastCntIndex,
       "pm253MondwRmonNonUnicastCntValuePortn": pm253MondwRmonNonUnicastCntValuePortn,
       "pm253MondwRmonNonUnicastCntErrorPortn": pm253MondwRmonNonUnicastCntErrorPortn,
       "pm253MondwRmonNonUnicastCntOverloadPortn": pm253MondwRmonNonUnicastCntOverloadPortn,
       "pm253PerfTelecomClientCurrent15StatTable": pm253PerfTelecomClientCurrent15StatTable,
       "pm253PerfTelecomClientCurrent15StatEntry": pm253PerfTelecomClientCurrent15StatEntry,
       "pm253PerfTelecomClientCurrent15StatIndex": pm253PerfTelecomClientCurrent15StatIndex,
       "pm253PerfTelecomClientCurrent15StatInvCvPortn": pm253PerfTelecomClientCurrent15StatInvCvPortn,
       "pm253PerfTelecomClientCurrent15StatCvValuePortn": pm253PerfTelecomClientCurrent15StatCvValuePortn,
       "pm253PerfTelecomClientCurrent15StatInvEsPortn": pm253PerfTelecomClientCurrent15StatInvEsPortn,
       "pm253PerfTelecomClientCurrent15StatEsValuePortn": pm253PerfTelecomClientCurrent15StatEsValuePortn,
       "pm253PerfTelecomClientCurrent15StatInvSesPortn": pm253PerfTelecomClientCurrent15StatInvSesPortn,
       "pm253PerfTelecomClientCurrent15StatSesValuePortn": pm253PerfTelecomClientCurrent15StatSesValuePortn,
       "pm253PerfTelecomClientCurrent15StatInvSefsPortn": pm253PerfTelecomClientCurrent15StatInvSefsPortn,
       "pm253PerfTelecomClientCurrent15StatSefsValuePortn": pm253PerfTelecomClientCurrent15StatSefsValuePortn,
       "pm253PerfTelecomClientCurrent15StatInvUasPortn": pm253PerfTelecomClientCurrent15StatInvUasPortn,
       "pm253PerfTelecomClientCurrent15StatUasValuePortn": pm253PerfTelecomClientCurrent15StatUasValuePortn,
       "pm253PerfTelecomClientPast15StatHistoryPort1Table": pm253PerfTelecomClientPast15StatHistoryPort1Table,
       "pm253PerfTelecomClientPast15StatHistoryPort1Entry": pm253PerfTelecomClientPast15StatHistoryPort1Entry,
       "pm253PerfTelecomClientPast15StatHistoryPort1Index": pm253PerfTelecomClientPast15StatHistoryPort1Index,
       "pm253PerfTelecomClientPast15StatHistoryInvCvPort1": pm253PerfTelecomClientPast15StatHistoryInvCvPort1,
       "pm253PerfTelecomClientPast15StatHistoryCvValuePort1": pm253PerfTelecomClientPast15StatHistoryCvValuePort1,
       "pm253PerfTelecomClientPast15StatHistoryInvEsPort1": pm253PerfTelecomClientPast15StatHistoryInvEsPort1,
       "pm253PerfTelecomClientPast15StatHistoryEsValuePort1": pm253PerfTelecomClientPast15StatHistoryEsValuePort1,
       "pm253PerfTelecomClientPast15StatHistoryInvSesPort1": pm253PerfTelecomClientPast15StatHistoryInvSesPort1,
       "pm253PerfTelecomClientPast15StatHistorySesValuePort1": pm253PerfTelecomClientPast15StatHistorySesValuePort1,
       "pm253PerfTelecomClientPast15StatHistoryInvSefsPort1": pm253PerfTelecomClientPast15StatHistoryInvSefsPort1,
       "pm253PerfTelecomClientPast15StatHistorySefsValuePort1": pm253PerfTelecomClientPast15StatHistorySefsValuePort1,
       "pm253PerfTelecomClientPast15StatHistoryInvUasPort1": pm253PerfTelecomClientPast15StatHistoryInvUasPort1,
       "pm253PerfTelecomClientPast15StatHistoryUasValuePort1": pm253PerfTelecomClientPast15StatHistoryUasValuePort1,
       "pm253PerfTelecomClientPast15StatHistoryPort2Table": pm253PerfTelecomClientPast15StatHistoryPort2Table,
       "pm253PerfTelecomClientPast15StatHistoryPort2Entry": pm253PerfTelecomClientPast15StatHistoryPort2Entry,
       "pm253PerfTelecomClientPast15StatHistoryPort2Index": pm253PerfTelecomClientPast15StatHistoryPort2Index,
       "pm253PerfTelecomClientPast15StatHistoryInvCvPort2": pm253PerfTelecomClientPast15StatHistoryInvCvPort2,
       "pm253PerfTelecomClientPast15StatHistoryCvValuePort2": pm253PerfTelecomClientPast15StatHistoryCvValuePort2,
       "pm253PerfTelecomClientPast15StatHistoryInvEsPort2": pm253PerfTelecomClientPast15StatHistoryInvEsPort2,
       "pm253PerfTelecomClientPast15StatHistoryEsValuePort2": pm253PerfTelecomClientPast15StatHistoryEsValuePort2,
       "pm253PerfTelecomClientPast15StatHistoryInvSesPort2": pm253PerfTelecomClientPast15StatHistoryInvSesPort2,
       "pm253PerfTelecomClientPast15StatHistorySesValuePort2": pm253PerfTelecomClientPast15StatHistorySesValuePort2,
       "pm253PerfTelecomClientPast15StatHistoryInvSefsPort2": pm253PerfTelecomClientPast15StatHistoryInvSefsPort2,
       "pm253PerfTelecomClientPast15StatHistorySefsValuePort2": pm253PerfTelecomClientPast15StatHistorySefsValuePort2,
       "pm253PerfTelecomClientPast15StatHistoryInvUasPort2": pm253PerfTelecomClientPast15StatHistoryInvUasPort2,
       "pm253PerfTelecomClientPast15StatHistoryUasValuePort2": pm253PerfTelecomClientPast15StatHistoryUasValuePort2,
       "pm253PerfTelecomClientPast15StatHistoryPort3Table": pm253PerfTelecomClientPast15StatHistoryPort3Table,
       "pm253PerfTelecomClientPast15StatHistoryPort3Entry": pm253PerfTelecomClientPast15StatHistoryPort3Entry,
       "pm253PerfTelecomClientPast15StatHistoryPort3Index": pm253PerfTelecomClientPast15StatHistoryPort3Index,
       "pm253PerfTelecomClientPast15StatHistoryInvCvPort3": pm253PerfTelecomClientPast15StatHistoryInvCvPort3,
       "pm253PerfTelecomClientPast15StatHistoryCvValuePort3": pm253PerfTelecomClientPast15StatHistoryCvValuePort3,
       "pm253PerfTelecomClientPast15StatHistoryInvEsPort3": pm253PerfTelecomClientPast15StatHistoryInvEsPort3,
       "pm253PerfTelecomClientPast15StatHistoryEsValuePort3": pm253PerfTelecomClientPast15StatHistoryEsValuePort3,
       "pm253PerfTelecomClientPast15StatHistoryInvSesPort3": pm253PerfTelecomClientPast15StatHistoryInvSesPort3,
       "pm253PerfTelecomClientPast15StatHistorySesValuePort3": pm253PerfTelecomClientPast15StatHistorySesValuePort3,
       "pm253PerfTelecomClientPast15StatHistoryInvSefsPort3": pm253PerfTelecomClientPast15StatHistoryInvSefsPort3,
       "pm253PerfTelecomClientPast15StatHistorySefsValuePort3": pm253PerfTelecomClientPast15StatHistorySefsValuePort3,
       "pm253PerfTelecomClientPast15StatHistoryInvUasPort3": pm253PerfTelecomClientPast15StatHistoryInvUasPort3,
       "pm253PerfTelecomClientPast15StatHistoryUasValuePort3": pm253PerfTelecomClientPast15StatHistoryUasValuePort3,
       "pm253PerfTelecomClientCurrent24StatTable": pm253PerfTelecomClientCurrent24StatTable,
       "pm253PerfTelecomClientCurrent24StatEntry": pm253PerfTelecomClientCurrent24StatEntry,
       "pm253PerfTelecomClientCurrent24StatIndex": pm253PerfTelecomClientCurrent24StatIndex,
       "pm253PerfTelecomClientCurrent24StatInvCvPortn": pm253PerfTelecomClientCurrent24StatInvCvPortn,
       "pm253PerfTelecomClientCurrent24StatCvValuePortn": pm253PerfTelecomClientCurrent24StatCvValuePortn,
       "pm253PerfTelecomClientCurrent24StatInvEsPortn": pm253PerfTelecomClientCurrent24StatInvEsPortn,
       "pm253PerfTelecomClientCurrent24StatEsValuePortn": pm253PerfTelecomClientCurrent24StatEsValuePortn,
       "pm253PerfTelecomClientCurrent24StatInvSesPortn": pm253PerfTelecomClientCurrent24StatInvSesPortn,
       "pm253PerfTelecomClientCurrent24StatSesValuePortn": pm253PerfTelecomClientCurrent24StatSesValuePortn,
       "pm253PerfTelecomClientCurrent24StatInvSefsPortn": pm253PerfTelecomClientCurrent24StatInvSefsPortn,
       "pm253PerfTelecomClientCurrent24StatSefsValuePortn": pm253PerfTelecomClientCurrent24StatSefsValuePortn,
       "pm253PerfTelecomClientCurrent24StatInvUasPortn": pm253PerfTelecomClientCurrent24StatInvUasPortn,
       "pm253PerfTelecomClientCurrent24StatUasValuePortn": pm253PerfTelecomClientCurrent24StatUasValuePortn,
       "pm253PerfTelecomClientPast24StatHistoryPort1Table": pm253PerfTelecomClientPast24StatHistoryPort1Table,
       "pm253PerfTelecomClientPast24StatHistoryPort1Entry": pm253PerfTelecomClientPast24StatHistoryPort1Entry,
       "pm253PerfTelecomClientPast24StatHistoryPort1Index": pm253PerfTelecomClientPast24StatHistoryPort1Index,
       "pm253PerfTelecomClientPast24StatHistoryInvCvPort1": pm253PerfTelecomClientPast24StatHistoryInvCvPort1,
       "pm253PerfTelecomClientPast24StatHistoryCvValuePort1": pm253PerfTelecomClientPast24StatHistoryCvValuePort1,
       "pm253PerfTelecomClientPast24StatHistoryInvEsPort1": pm253PerfTelecomClientPast24StatHistoryInvEsPort1,
       "pm253PerfTelecomClientPast24StatHistoryEsValuePort1": pm253PerfTelecomClientPast24StatHistoryEsValuePort1,
       "pm253PerfTelecomClientPast24StatHistoryInvSesPort1": pm253PerfTelecomClientPast24StatHistoryInvSesPort1,
       "pm253PerfTelecomClientPast24StatHistorySesValuePort1": pm253PerfTelecomClientPast24StatHistorySesValuePort1,
       "pm253PerfTelecomClientPast24StatHistoryInvSefsPort1": pm253PerfTelecomClientPast24StatHistoryInvSefsPort1,
       "pm253PerfTelecomClientPast24StatHistorySefsValuePort1": pm253PerfTelecomClientPast24StatHistorySefsValuePort1,
       "pm253PerfTelecomClientPast24StatHistoryInvUasPort1": pm253PerfTelecomClientPast24StatHistoryInvUasPort1,
       "pm253PerfTelecomClientPast24StatHistoryUasValuePort1": pm253PerfTelecomClientPast24StatHistoryUasValuePort1,
       "pm253PerfTelecomClientPast24StatHistoryPort2Table": pm253PerfTelecomClientPast24StatHistoryPort2Table,
       "pm253PerfTelecomClientPast24StatHistoryPort2Entry": pm253PerfTelecomClientPast24StatHistoryPort2Entry,
       "pm253PerfTelecomClientPast24StatHistoryPort2Index": pm253PerfTelecomClientPast24StatHistoryPort2Index,
       "pm253PerfTelecomClientPast24StatHistoryInvCvPort2": pm253PerfTelecomClientPast24StatHistoryInvCvPort2,
       "pm253PerfTelecomClientPast24StatHistoryCvValuePort2": pm253PerfTelecomClientPast24StatHistoryCvValuePort2,
       "pm253PerfTelecomClientPast24StatHistoryInvEsPort2": pm253PerfTelecomClientPast24StatHistoryInvEsPort2,
       "pm253PerfTelecomClientPast24StatHistoryEsValuePort2": pm253PerfTelecomClientPast24StatHistoryEsValuePort2,
       "pm253PerfTelecomClientPast24StatHistoryInvSesPort2": pm253PerfTelecomClientPast24StatHistoryInvSesPort2,
       "pm253PerfTelecomClientPast24StatHistorySesValuePort2": pm253PerfTelecomClientPast24StatHistorySesValuePort2,
       "pm253PerfTelecomClientPast24StatHistoryInvSefsPort2": pm253PerfTelecomClientPast24StatHistoryInvSefsPort2,
       "pm253PerfTelecomClientPast24StatHistorySefsValuePort2": pm253PerfTelecomClientPast24StatHistorySefsValuePort2,
       "pm253PerfTelecomClientPast24StatHistoryInvUasPort2": pm253PerfTelecomClientPast24StatHistoryInvUasPort2,
       "pm253PerfTelecomClientPast24StatHistoryUasValuePort2": pm253PerfTelecomClientPast24StatHistoryUasValuePort2,
       "pm253PerfTelecomClientPast24StatHistoryPort3Table": pm253PerfTelecomClientPast24StatHistoryPort3Table,
       "pm253PerfTelecomClientPast24StatHistoryPort3Entry": pm253PerfTelecomClientPast24StatHistoryPort3Entry,
       "pm253PerfTelecomClientPast24StatHistoryPort3Index": pm253PerfTelecomClientPast24StatHistoryPort3Index,
       "pm253PerfTelecomClientPast24StatHistoryInvCvPort3": pm253PerfTelecomClientPast24StatHistoryInvCvPort3,
       "pm253PerfTelecomClientPast24StatHistoryCvValuePort3": pm253PerfTelecomClientPast24StatHistoryCvValuePort3,
       "pm253PerfTelecomClientPast24StatHistoryInvEsPort3": pm253PerfTelecomClientPast24StatHistoryInvEsPort3,
       "pm253PerfTelecomClientPast24StatHistoryEsValuePort3": pm253PerfTelecomClientPast24StatHistoryEsValuePort3,
       "pm253PerfTelecomClientPast24StatHistoryInvSesPort3": pm253PerfTelecomClientPast24StatHistoryInvSesPort3,
       "pm253PerfTelecomClientPast24StatHistorySesValuePort3": pm253PerfTelecomClientPast24StatHistorySesValuePort3,
       "pm253PerfTelecomClientPast24StatHistoryInvSefsPort3": pm253PerfTelecomClientPast24StatHistoryInvSefsPort3,
       "pm253PerfTelecomClientPast24StatHistorySefsValuePort3": pm253PerfTelecomClientPast24StatHistorySefsValuePort3,
       "pm253PerfTelecomClientPast24StatHistoryInvUasPort3": pm253PerfTelecomClientPast24StatHistoryInvUasPort3,
       "pm253PerfTelecomClientPast24StatHistoryUasValuePort3": pm253PerfTelecomClientPast24StatHistoryUasValuePort3,
       "pm253PerfDatacomClientCurrent15StatTable": pm253PerfDatacomClientCurrent15StatTable,
       "pm253PerfDatacomClientCurrent15StatEntry": pm253PerfDatacomClientCurrent15StatEntry,
       "pm253PerfDatacomClientCurrent15StatIndex": pm253PerfDatacomClientCurrent15StatIndex,
       "pm253perfdatacomclientCurrent15StatInBytesCountInvPortn": pm253perfdatacomclientCurrent15StatInBytesCountInvPortn,
       "pm253perfdatacomclientCurrent15StatInBytesCountPortn": pm253perfdatacomclientCurrent15StatInBytesCountPortn,
       "pm253perfdatacomclientCurrent15StatInCrcCountInvPortn": pm253perfdatacomclientCurrent15StatInCrcCountInvPortn,
       "pm253perfdatacomclientCurrent15StatInCrcCountPortn": pm253perfdatacomclientCurrent15StatInCrcCountPortn,
       "pm253perfdatacomclientCurrent15StatInBroadcastCountInvPortn": pm253perfdatacomclientCurrent15StatInBroadcastCountInvPortn,
       "pm253perfdatacomclientCurrent15StatInBroadcastCountPortn": pm253perfdatacomclientCurrent15StatInBroadcastCountPortn,
       "pm253perfdatacomclientCurrent15StatInMulticastCountInvPortn": pm253perfdatacomclientCurrent15StatInMulticastCountInvPortn,
       "pm253perfdatacomclientCurrent15StatInMulticastCountPortn": pm253perfdatacomclientCurrent15StatInMulticastCountPortn,
       "pm253perfdatacomclientCurrent15StatInUnicastCountInvPortn": pm253perfdatacomclientCurrent15StatInUnicastCountInvPortn,
       "pm253perfdatacomclientCurrent15StatInUnicastCountPortn": pm253perfdatacomclientCurrent15StatInUnicastCountPortn,
       "pm253perfdatacomclientCurrent15StatInNonunicastCountInvPortn": pm253perfdatacomclientCurrent15StatInNonunicastCountInvPortn,
       "pm253perfdatacomclientCurrent15StatInNonunicastCountPortn": pm253perfdatacomclientCurrent15StatInNonunicastCountPortn,
       "pm253perfdatacomclientCurrent15StatOutBytesCountInvPortn": pm253perfdatacomclientCurrent15StatOutBytesCountInvPortn,
       "pm253perfdatacomclientCurrent15StatOutBytesCountPortn": pm253perfdatacomclientCurrent15StatOutBytesCountPortn,
       "pm253perfdatacomclientCurrent15StatOutBroadcastCountInvPortn": pm253perfdatacomclientCurrent15StatOutBroadcastCountInvPortn,
       "pm253perfdatacomclientCurrent15StatOutBroadcastCountPortn": pm253perfdatacomclientCurrent15StatOutBroadcastCountPortn,
       "pm253perfdatacomclientCurrent15StatOutMulticastCountInvPortn": pm253perfdatacomclientCurrent15StatOutMulticastCountInvPortn,
       "pm253perfdatacomclientCurrent15StatOutMulticastCountPortn": pm253perfdatacomclientCurrent15StatOutMulticastCountPortn,
       "pm253perfdatacomclientCurrent15StatOutUnicastCountInvPortn": pm253perfdatacomclientCurrent15StatOutUnicastCountInvPortn,
       "pm253perfdatacomclientCurrent15StatOutUnicastCountPortn": pm253perfdatacomclientCurrent15StatOutUnicastCountPortn,
       "pm253perfdatacomclientCurrent15StatOutNonunicastCountInvPortn": pm253perfdatacomclientCurrent15StatOutNonunicastCountInvPortn,
       "pm253perfdatacomclientCurrent15StatOutNonunicastCountPortn": pm253perfdatacomclientCurrent15StatOutNonunicastCountPortn,
       "pm253PerfDatacomClientPast15StatHistoryPort1Table": pm253PerfDatacomClientPast15StatHistoryPort1Table,
       "pm253PerfDatacomClientPast15StatHistoryPort1Entry": pm253PerfDatacomClientPast15StatHistoryPort1Entry,
       "pm253PerfDatacomClientPast15StatHistoryPort1Index": pm253PerfDatacomClientPast15StatHistoryPort1Index,
       "pm253perfdatacomclientPast15StatInBytesCountInvPort1": pm253perfdatacomclientPast15StatInBytesCountInvPort1,
       "pm253perfdatacomclientPast15StatInBytesCountPort1": pm253perfdatacomclientPast15StatInBytesCountPort1,
       "pm253perfdatacomclientPast15StatInCrcCountInvPort1": pm253perfdatacomclientPast15StatInCrcCountInvPort1,
       "pm253perfdatacomclientPast15StatInCrcCountPort1": pm253perfdatacomclientPast15StatInCrcCountPort1,
       "pm253perfdatacomclientPast15StatInBroadcastCountInvPort1": pm253perfdatacomclientPast15StatInBroadcastCountInvPort1,
       "pm253perfdatacomclientPast15StatInBroadcastCountPort1": pm253perfdatacomclientPast15StatInBroadcastCountPort1,
       "pm253perfdatacomclientPast15StatInMulticastCountInvPort1": pm253perfdatacomclientPast15StatInMulticastCountInvPort1,
       "pm253perfdatacomclientPast15StatInMulticastCountPort1": pm253perfdatacomclientPast15StatInMulticastCountPort1,
       "pm253perfdatacomclientPast15StatInUnicastCountInvPort1": pm253perfdatacomclientPast15StatInUnicastCountInvPort1,
       "pm253perfdatacomclientPast15StatInUnicastCountPort1": pm253perfdatacomclientPast15StatInUnicastCountPort1,
       "pm253perfdatacomclientPast15StatInNonunicastCountInvPort1": pm253perfdatacomclientPast15StatInNonunicastCountInvPort1,
       "pm253perfdatacomclientPast15StatInNonunicastCountPort1": pm253perfdatacomclientPast15StatInNonunicastCountPort1,
       "pm253perfdatacomclientPast15StatOutBytesCountInvPort1": pm253perfdatacomclientPast15StatOutBytesCountInvPort1,
       "pm253perfdatacomclientPast15StatOutBytesCountPort1": pm253perfdatacomclientPast15StatOutBytesCountPort1,
       "pm253perfdatacomclientPast15StatOutBroadcastCountInvPort1": pm253perfdatacomclientPast15StatOutBroadcastCountInvPort1,
       "pm253perfdatacomclientPast15StatOutBroadcastCountPort1": pm253perfdatacomclientPast15StatOutBroadcastCountPort1,
       "pm253perfdatacomclientPast15StatOutMulticastCountInvPort1": pm253perfdatacomclientPast15StatOutMulticastCountInvPort1,
       "pm253perfdatacomclientPast15StatOutMulticastCountPort1": pm253perfdatacomclientPast15StatOutMulticastCountPort1,
       "pm253perfdatacomclientPast15StatOutUnicastCountInvPort1": pm253perfdatacomclientPast15StatOutUnicastCountInvPort1,
       "pm253perfdatacomclientPast15StatOutUnicastCountPort1": pm253perfdatacomclientPast15StatOutUnicastCountPort1,
       "pm253perfdatacomclientPast15StatOutNonunicastCountInvPort1": pm253perfdatacomclientPast15StatOutNonunicastCountInvPort1,
       "pm253perfdatacomclientPast15StatOutNonunicastCountPort1": pm253perfdatacomclientPast15StatOutNonunicastCountPort1,
       "pm253PerfDatacomClientPast15StatHistoryPort2Table": pm253PerfDatacomClientPast15StatHistoryPort2Table,
       "pm253PerfDatacomClientPast15StatHistoryPort2Entry": pm253PerfDatacomClientPast15StatHistoryPort2Entry,
       "pm253PerfDatacomClientPast15StatHistoryPort2Index": pm253PerfDatacomClientPast15StatHistoryPort2Index,
       "pm253perfdatacomclientPast15StatInBytesCountInvPort2": pm253perfdatacomclientPast15StatInBytesCountInvPort2,
       "pm253perfdatacomclientPast15StatInBytesCountPort2": pm253perfdatacomclientPast15StatInBytesCountPort2,
       "pm253perfdatacomclientPast15StatInCrcCountInvPort2": pm253perfdatacomclientPast15StatInCrcCountInvPort2,
       "pm253perfdatacomclientPast15StatInCrcCountPort2": pm253perfdatacomclientPast15StatInCrcCountPort2,
       "pm253perfdatacomclientPast15StatInBroadcastCountInvPort2": pm253perfdatacomclientPast15StatInBroadcastCountInvPort2,
       "pm253perfdatacomclientPast15StatInBroadcastCountPort2": pm253perfdatacomclientPast15StatInBroadcastCountPort2,
       "pm253perfdatacomclientPast15StatInMulticastCountInvPort2": pm253perfdatacomclientPast15StatInMulticastCountInvPort2,
       "pm253perfdatacomclientPast15StatInMulticastCountPort2": pm253perfdatacomclientPast15StatInMulticastCountPort2,
       "pm253perfdatacomclientPast15StatInUnicastCountInvPort2": pm253perfdatacomclientPast15StatInUnicastCountInvPort2,
       "pm253perfdatacomclientPast15StatInUnicastCountPort2": pm253perfdatacomclientPast15StatInUnicastCountPort2,
       "pm253perfdatacomclientPast15StatInNonunicastCountInvPort2": pm253perfdatacomclientPast15StatInNonunicastCountInvPort2,
       "pm253perfdatacomclientPast15StatInNonunicastCountPort2": pm253perfdatacomclientPast15StatInNonunicastCountPort2,
       "pm253perfdatacomclientPast15StatOutBytesCountInvPort2": pm253perfdatacomclientPast15StatOutBytesCountInvPort2,
       "pm253perfdatacomclientPast15StatOutBytesCountPort2": pm253perfdatacomclientPast15StatOutBytesCountPort2,
       "pm253perfdatacomclientPast15StatOutBroadcastCountInvPort2": pm253perfdatacomclientPast15StatOutBroadcastCountInvPort2,
       "pm253perfdatacomclientPast15StatOutBroadcastCountPort2": pm253perfdatacomclientPast15StatOutBroadcastCountPort2,
       "pm253perfdatacomclientPast15StatOutMulticastCountInvPort2": pm253perfdatacomclientPast15StatOutMulticastCountInvPort2,
       "pm253perfdatacomclientPast15StatOutMulticastCountPort2": pm253perfdatacomclientPast15StatOutMulticastCountPort2,
       "pm253perfdatacomclientPast15StatOutUnicastCountInvPort2": pm253perfdatacomclientPast15StatOutUnicastCountInvPort2,
       "pm253perfdatacomclientPast15StatOutUnicastCountPort2": pm253perfdatacomclientPast15StatOutUnicastCountPort2,
       "pm253perfdatacomclientPast15StatOutNonunicastCountInvPort2": pm253perfdatacomclientPast15StatOutNonunicastCountInvPort2,
       "pm253perfdatacomclientPast15StatOutNonunicastCountPort2": pm253perfdatacomclientPast15StatOutNonunicastCountPort2,
       "pm253PerfDatacomClientPast15StatHistoryPort3Table": pm253PerfDatacomClientPast15StatHistoryPort3Table,
       "pm253PerfDatacomClientPast15StatHistoryPort3Entry": pm253PerfDatacomClientPast15StatHistoryPort3Entry,
       "pm253PerfDatacomClientPast15StatHistoryPort3Index": pm253PerfDatacomClientPast15StatHistoryPort3Index,
       "pm253perfdatacomclientPast15StatInBytesCountInvPort3": pm253perfdatacomclientPast15StatInBytesCountInvPort3,
       "pm253perfdatacomclientPast15StatInBytesCountPort3": pm253perfdatacomclientPast15StatInBytesCountPort3,
       "pm253perfdatacomclientPast15StatInCrcCountInvPort3": pm253perfdatacomclientPast15StatInCrcCountInvPort3,
       "pm253perfdatacomclientPast15StatInCrcCountPort3": pm253perfdatacomclientPast15StatInCrcCountPort3,
       "pm253perfdatacomclientPast15StatInBroadcastCountInvPort3": pm253perfdatacomclientPast15StatInBroadcastCountInvPort3,
       "pm253perfdatacomclientPast15StatInBroadcastCountPort3": pm253perfdatacomclientPast15StatInBroadcastCountPort3,
       "pm253perfdatacomclientPast15StatInMulticastCountInvPort3": pm253perfdatacomclientPast15StatInMulticastCountInvPort3,
       "pm253perfdatacomclientPast15StatInMulticastCountPort3": pm253perfdatacomclientPast15StatInMulticastCountPort3,
       "pm253perfdatacomclientPast15StatInUnicastCountInvPort3": pm253perfdatacomclientPast15StatInUnicastCountInvPort3,
       "pm253perfdatacomclientPast15StatInUnicastCountPort3": pm253perfdatacomclientPast15StatInUnicastCountPort3,
       "pm253perfdatacomclientPast15StatInNonunicastCountInvPort3": pm253perfdatacomclientPast15StatInNonunicastCountInvPort3,
       "pm253perfdatacomclientPast15StatInNonunicastCountPort3": pm253perfdatacomclientPast15StatInNonunicastCountPort3,
       "pm253perfdatacomclientPast15StatOutBytesCountInvPort3": pm253perfdatacomclientPast15StatOutBytesCountInvPort3,
       "pm253perfdatacomclientPast15StatOutBytesCountPort3": pm253perfdatacomclientPast15StatOutBytesCountPort3,
       "pm253perfdatacomclientPast15StatOutBroadcastCountInvPort3": pm253perfdatacomclientPast15StatOutBroadcastCountInvPort3,
       "pm253perfdatacomclientPast15StatOutBroadcastCountPort3": pm253perfdatacomclientPast15StatOutBroadcastCountPort3,
       "pm253perfdatacomclientPast15StatOutMulticastCountInvPort3": pm253perfdatacomclientPast15StatOutMulticastCountInvPort3,
       "pm253perfdatacomclientPast15StatOutMulticastCountPort3": pm253perfdatacomclientPast15StatOutMulticastCountPort3,
       "pm253perfdatacomclientPast15StatOutUnicastCountInvPort3": pm253perfdatacomclientPast15StatOutUnicastCountInvPort3,
       "pm253perfdatacomclientPast15StatOutUnicastCountPort3": pm253perfdatacomclientPast15StatOutUnicastCountPort3,
       "pm253perfdatacomclientPast15StatOutNonunicastCountInvPort3": pm253perfdatacomclientPast15StatOutNonunicastCountInvPort3,
       "pm253perfdatacomclientPast15StatOutNonunicastCountPort3": pm253perfdatacomclientPast15StatOutNonunicastCountPort3,
       "pm253PerfDatacomClientCurrent24StatTable": pm253PerfDatacomClientCurrent24StatTable,
       "pm253PerfDatacomClientCurrent24StatEntry": pm253PerfDatacomClientCurrent24StatEntry,
       "pm253PerfDatacomClientCurrent24StatIndex": pm253PerfDatacomClientCurrent24StatIndex,
       "pm253perfdatacomclientCurrent24StatInBytesCountInvPortn": pm253perfdatacomclientCurrent24StatInBytesCountInvPortn,
       "pm253perfdatacomclientCurrent24StatInBytesCountPortn": pm253perfdatacomclientCurrent24StatInBytesCountPortn,
       "pm253perfdatacomclientCurrent24StatInCrcCountInvPortn": pm253perfdatacomclientCurrent24StatInCrcCountInvPortn,
       "pm253perfdatacomclientCurrent24StatInCrcCountPortn": pm253perfdatacomclientCurrent24StatInCrcCountPortn,
       "pm253perfdatacomclientCurrent24StatInBroadcastCountInvPortn": pm253perfdatacomclientCurrent24StatInBroadcastCountInvPortn,
       "pm253perfdatacomclientCurrent24StatInBroadcastCountPortn": pm253perfdatacomclientCurrent24StatInBroadcastCountPortn,
       "pm253perfdatacomclientCurrent24StatInMulticastCountInvPortn": pm253perfdatacomclientCurrent24StatInMulticastCountInvPortn,
       "pm253perfdatacomclientCurrent24StatInMulticastCountPortn": pm253perfdatacomclientCurrent24StatInMulticastCountPortn,
       "pm253perfdatacomclientCurrent24StatInUnicastCountInvPortn": pm253perfdatacomclientCurrent24StatInUnicastCountInvPortn,
       "pm253perfdatacomclientCurrent24StatInUnicastCountPortn": pm253perfdatacomclientCurrent24StatInUnicastCountPortn,
       "pm253perfdatacomclientCurrent24StatInNonunicastCountInvPortn": pm253perfdatacomclientCurrent24StatInNonunicastCountInvPortn,
       "pm253perfdatacomclientCurrent24StatInNonunicastCountPortn": pm253perfdatacomclientCurrent24StatInNonunicastCountPortn,
       "pm253perfdatacomclientCurrent24StatOutBytesCountInvPortn": pm253perfdatacomclientCurrent24StatOutBytesCountInvPortn,
       "pm253perfdatacomclientCurrent24StatOutBytesCountPortn": pm253perfdatacomclientCurrent24StatOutBytesCountPortn,
       "pm253perfdatacomclientCurrent24StatOutBroadcastCountInvPortn": pm253perfdatacomclientCurrent24StatOutBroadcastCountInvPortn,
       "pm253perfdatacomclientCurrent24StatOutBroadcastCountPortn": pm253perfdatacomclientCurrent24StatOutBroadcastCountPortn,
       "pm253perfdatacomclientCurrent24StatOutMulticastCountInvPortn": pm253perfdatacomclientCurrent24StatOutMulticastCountInvPortn,
       "pm253perfdatacomclientCurrent24StatOutMulticastCountPortn": pm253perfdatacomclientCurrent24StatOutMulticastCountPortn,
       "pm253perfdatacomclientCurrent24StatOutUnicastCountInvPortn": pm253perfdatacomclientCurrent24StatOutUnicastCountInvPortn,
       "pm253perfdatacomclientCurrent24StatOutUnicastCountPortn": pm253perfdatacomclientCurrent24StatOutUnicastCountPortn,
       "pm253perfdatacomclientCurrent24StatOutNonunicastCountInvPortn": pm253perfdatacomclientCurrent24StatOutNonunicastCountInvPortn,
       "pm253perfdatacomclientCurrent24StatOutNonunicastCountPortn": pm253perfdatacomclientCurrent24StatOutNonunicastCountPortn,
       "pm253PerfDatacomClientPast24StatHistoryPort1Table": pm253PerfDatacomClientPast24StatHistoryPort1Table,
       "pm253PerfDatacomClientPast24StatHistoryPort1Entry": pm253PerfDatacomClientPast24StatHistoryPort1Entry,
       "pm253PerfDatacomClientPast24StatHistoryPort1Index": pm253PerfDatacomClientPast24StatHistoryPort1Index,
       "pm253perfdatacomclientPast24StatInBytesCountInvPort1": pm253perfdatacomclientPast24StatInBytesCountInvPort1,
       "pm253perfdatacomclientPast24StatInBytesCountPort1": pm253perfdatacomclientPast24StatInBytesCountPort1,
       "pm253perfdatacomclientPast24StatInCrcCountInvPort1": pm253perfdatacomclientPast24StatInCrcCountInvPort1,
       "pm253perfdatacomclientPast24StatInCrcCountPort1": pm253perfdatacomclientPast24StatInCrcCountPort1,
       "pm253perfdatacomclientPast24StatInBroadcastCountInvPort1": pm253perfdatacomclientPast24StatInBroadcastCountInvPort1,
       "pm253perfdatacomclientPast24StatInBroadcastCountPort1": pm253perfdatacomclientPast24StatInBroadcastCountPort1,
       "pm253perfdatacomclientPast24StatInMulticastCountInvPort1": pm253perfdatacomclientPast24StatInMulticastCountInvPort1,
       "pm253perfdatacomclientPast24StatInMulticastCountPort1": pm253perfdatacomclientPast24StatInMulticastCountPort1,
       "pm253perfdatacomclientPast24StatInUnicastCountInvPort1": pm253perfdatacomclientPast24StatInUnicastCountInvPort1,
       "pm253perfdatacomclientPast24StatInUnicastCountPort1": pm253perfdatacomclientPast24StatInUnicastCountPort1,
       "pm253perfdatacomclientPast24StatInNonunicastCountInvPort1": pm253perfdatacomclientPast24StatInNonunicastCountInvPort1,
       "pm253perfdatacomclientPast24StatInNonunicastCountPort1": pm253perfdatacomclientPast24StatInNonunicastCountPort1,
       "pm253perfdatacomclientPast24StatOutBytesCountInvPort1": pm253perfdatacomclientPast24StatOutBytesCountInvPort1,
       "pm253perfdatacomclientPast24StatOutBytesCountPort1": pm253perfdatacomclientPast24StatOutBytesCountPort1,
       "pm253perfdatacomclientPast24StatOutBroadcastCountInvPort1": pm253perfdatacomclientPast24StatOutBroadcastCountInvPort1,
       "pm253perfdatacomclientPast24StatOutBroadcastCountPort1": pm253perfdatacomclientPast24StatOutBroadcastCountPort1,
       "pm253perfdatacomclientPast24StatOutMulticastCountInvPort1": pm253perfdatacomclientPast24StatOutMulticastCountInvPort1,
       "pm253perfdatacomclientPast24StatOutMulticastCountPort1": pm253perfdatacomclientPast24StatOutMulticastCountPort1,
       "pm253perfdatacomclientPast24StatOutUnicastCountInvPort1": pm253perfdatacomclientPast24StatOutUnicastCountInvPort1,
       "pm253perfdatacomclientPast24StatOutUnicastCountPort1": pm253perfdatacomclientPast24StatOutUnicastCountPort1,
       "pm253perfdatacomclientPast24StatOutNonunicastCountInvPort1": pm253perfdatacomclientPast24StatOutNonunicastCountInvPort1,
       "pm253perfdatacomclientPast24StatOutNonunicastCountPort1": pm253perfdatacomclientPast24StatOutNonunicastCountPort1,
       "pm253PerfDatacomClientPast24StatHistoryPort2Table": pm253PerfDatacomClientPast24StatHistoryPort2Table,
       "pm253PerfDatacomClientPast24StatHistoryPort2Entry": pm253PerfDatacomClientPast24StatHistoryPort2Entry,
       "pm253PerfDatacomClientPast24StatHistoryPort2Index": pm253PerfDatacomClientPast24StatHistoryPort2Index,
       "pm253perfdatacomclientPast24StatInBytesCountInvPort2": pm253perfdatacomclientPast24StatInBytesCountInvPort2,
       "pm253perfdatacomclientPast24StatInBytesCountPort2": pm253perfdatacomclientPast24StatInBytesCountPort2,
       "pm253perfdatacomclientPast24StatInCrcCountInvPort2": pm253perfdatacomclientPast24StatInCrcCountInvPort2,
       "pm253perfdatacomclientPast24StatInCrcCountPort2": pm253perfdatacomclientPast24StatInCrcCountPort2,
       "pm253perfdatacomclientPast24StatInBroadcastCountInvPort2": pm253perfdatacomclientPast24StatInBroadcastCountInvPort2,
       "pm253perfdatacomclientPast24StatInBroadcastCountPort2": pm253perfdatacomclientPast24StatInBroadcastCountPort2,
       "pm253perfdatacomclientPast24StatInMulticastCountInvPort2": pm253perfdatacomclientPast24StatInMulticastCountInvPort2,
       "pm253perfdatacomclientPast24StatInMulticastCountPort2": pm253perfdatacomclientPast24StatInMulticastCountPort2,
       "pm253perfdatacomclientPast24StatInUnicastCountInvPort2": pm253perfdatacomclientPast24StatInUnicastCountInvPort2,
       "pm253perfdatacomclientPast24StatInUnicastCountPort2": pm253perfdatacomclientPast24StatInUnicastCountPort2,
       "pm253perfdatacomclientPast24StatInNonunicastCountInvPort2": pm253perfdatacomclientPast24StatInNonunicastCountInvPort2,
       "pm253perfdatacomclientPast24StatInNonunicastCountPort2": pm253perfdatacomclientPast24StatInNonunicastCountPort2,
       "pm253perfdatacomclientPast24StatOutBytesCountInvPort2": pm253perfdatacomclientPast24StatOutBytesCountInvPort2,
       "pm253perfdatacomclientPast24StatOutBytesCountPort2": pm253perfdatacomclientPast24StatOutBytesCountPort2,
       "pm253perfdatacomclientPast24StatOutBroadcastCountInvPort2": pm253perfdatacomclientPast24StatOutBroadcastCountInvPort2,
       "pm253perfdatacomclientPast24StatOutBroadcastCountPort2": pm253perfdatacomclientPast24StatOutBroadcastCountPort2,
       "pm253perfdatacomclientPast24StatOutMulticastCountInvPort2": pm253perfdatacomclientPast24StatOutMulticastCountInvPort2,
       "pm253perfdatacomclientPast24StatOutMulticastCountPort2": pm253perfdatacomclientPast24StatOutMulticastCountPort2,
       "pm253perfdatacomclientPast24StatOutUnicastCountInvPort2": pm253perfdatacomclientPast24StatOutUnicastCountInvPort2,
       "pm253perfdatacomclientPast24StatOutUnicastCountPort2": pm253perfdatacomclientPast24StatOutUnicastCountPort2,
       "pm253perfdatacomclientPast24StatOutNonunicastCountInvPort2": pm253perfdatacomclientPast24StatOutNonunicastCountInvPort2,
       "pm253perfdatacomclientPast24StatOutNonunicastCountPort2": pm253perfdatacomclientPast24StatOutNonunicastCountPort2,
       "pm253PerfDatacomClientPast24StatHistoryPort3Table": pm253PerfDatacomClientPast24StatHistoryPort3Table,
       "pm253PerfDatacomClientPast24StatHistoryPort3Entry": pm253PerfDatacomClientPast24StatHistoryPort3Entry,
       "pm253PerfDatacomClientPast24StatHistoryPort3Index": pm253PerfDatacomClientPast24StatHistoryPort3Index,
       "pm253perfdatacomclientPast24StatInBytesCountInvPort3": pm253perfdatacomclientPast24StatInBytesCountInvPort3,
       "pm253perfdatacomclientPast24StatInBytesCountPort3": pm253perfdatacomclientPast24StatInBytesCountPort3,
       "pm253perfdatacomclientPast24StatInCrcCountInvPort3": pm253perfdatacomclientPast24StatInCrcCountInvPort3,
       "pm253perfdatacomclientPast24StatInCrcCountPort3": pm253perfdatacomclientPast24StatInCrcCountPort3,
       "pm253perfdatacomclientPast24StatInBroadcastCountInvPort3": pm253perfdatacomclientPast24StatInBroadcastCountInvPort3,
       "pm253perfdatacomclientPast24StatInBroadcastCountPort3": pm253perfdatacomclientPast24StatInBroadcastCountPort3,
       "pm253perfdatacomclientPast24StatInMulticastCountInvPort3": pm253perfdatacomclientPast24StatInMulticastCountInvPort3,
       "pm253perfdatacomclientPast24StatInMulticastCountPort3": pm253perfdatacomclientPast24StatInMulticastCountPort3,
       "pm253perfdatacomclientPast24StatInUnicastCountInvPort3": pm253perfdatacomclientPast24StatInUnicastCountInvPort3,
       "pm253perfdatacomclientPast24StatInUnicastCountPort3": pm253perfdatacomclientPast24StatInUnicastCountPort3,
       "pm253perfdatacomclientPast24StatInNonunicastCountInvPort3": pm253perfdatacomclientPast24StatInNonunicastCountInvPort3,
       "pm253perfdatacomclientPast24StatInNonunicastCountPort3": pm253perfdatacomclientPast24StatInNonunicastCountPort3,
       "pm253perfdatacomclientPast24StatOutBytesCountInvPort3": pm253perfdatacomclientPast24StatOutBytesCountInvPort3,
       "pm253perfdatacomclientPast24StatOutBytesCountPort3": pm253perfdatacomclientPast24StatOutBytesCountPort3,
       "pm253perfdatacomclientPast24StatOutBroadcastCountInvPort3": pm253perfdatacomclientPast24StatOutBroadcastCountInvPort3,
       "pm253perfdatacomclientPast24StatOutBroadcastCountPort3": pm253perfdatacomclientPast24StatOutBroadcastCountPort3,
       "pm253perfdatacomclientPast24StatOutMulticastCountInvPort3": pm253perfdatacomclientPast24StatOutMulticastCountInvPort3,
       "pm253perfdatacomclientPast24StatOutMulticastCountPort3": pm253perfdatacomclientPast24StatOutMulticastCountPort3,
       "pm253perfdatacomclientPast24StatOutUnicastCountInvPort3": pm253perfdatacomclientPast24StatOutUnicastCountInvPort3,
       "pm253perfdatacomclientPast24StatOutUnicastCountPort3": pm253perfdatacomclientPast24StatOutUnicastCountPort3,
       "pm253perfdatacomclientPast24StatOutNonunicastCountInvPort3": pm253perfdatacomclientPast24StatOutNonunicastCountInvPort3,
       "pm253perfdatacomclientPast24StatOutNonunicastCountPort3": pm253perfdatacomclientPast24StatOutNonunicastCountPort3,
       "pm253MonLine": pm253MonLine,
       "pm253PerfTelecomLineCurrent15StatTable": pm253PerfTelecomLineCurrent15StatTable,
       "pm253PerfTelecomLineCurrent15StatEntry": pm253PerfTelecomLineCurrent15StatEntry,
       "pm253PerfTelecomLineCurrent15StatIndex": pm253PerfTelecomLineCurrent15StatIndex,
       "pm253PerfTelecomLineCurrent15StatInvCvPortn": pm253PerfTelecomLineCurrent15StatInvCvPortn,
       "pm253PerfTelecomLineCurrent15StatCvValuePortn": pm253PerfTelecomLineCurrent15StatCvValuePortn,
       "pm253PerfTelecomLineCurrent15StatInvEsPortn": pm253PerfTelecomLineCurrent15StatInvEsPortn,
       "pm253PerfTelecomLineCurrent15StatEsValuePortn": pm253PerfTelecomLineCurrent15StatEsValuePortn,
       "pm253PerfTelecomLineCurrent15StatInvSesPortn": pm253PerfTelecomLineCurrent15StatInvSesPortn,
       "pm253PerfTelecomLineCurrent15StatSesValuePortn": pm253PerfTelecomLineCurrent15StatSesValuePortn,
       "pm253PerfTelecomLineCurrent15StatInvSefsPortn": pm253PerfTelecomLineCurrent15StatInvSefsPortn,
       "pm253PerfTelecomLineCurrent15StatSefsValuePortn": pm253PerfTelecomLineCurrent15StatSefsValuePortn,
       "pm253PerfTelecomLineCurrent15StatInvUasPortn": pm253PerfTelecomLineCurrent15StatInvUasPortn,
       "pm253PerfTelecomLineCurrent15StatUasValuePortn": pm253PerfTelecomLineCurrent15StatUasValuePortn,
       "pm253PerfTelecomLinePast15StatHistoryPort1Table": pm253PerfTelecomLinePast15StatHistoryPort1Table,
       "pm253PerfTelecomLinePast15StatHistoryPort1Entry": pm253PerfTelecomLinePast15StatHistoryPort1Entry,
       "pm253PerfTelecomLinePast15StatHistoryPort1Index": pm253PerfTelecomLinePast15StatHistoryPort1Index,
       "pm253PerfTelecomLinePast15StatHistoryInvCvPort1": pm253PerfTelecomLinePast15StatHistoryInvCvPort1,
       "pm253PerfTelecomLinePast15StatHistoryCvValuePort1": pm253PerfTelecomLinePast15StatHistoryCvValuePort1,
       "pm253PerfTelecomLinePast15StatHistoryInvEsPort1": pm253PerfTelecomLinePast15StatHistoryInvEsPort1,
       "pm253PerfTelecomLinePast15StatHistoryEsValuePort1": pm253PerfTelecomLinePast15StatHistoryEsValuePort1,
       "pm253PerfTelecomLinePast15StatHistoryInvSesPort1": pm253PerfTelecomLinePast15StatHistoryInvSesPort1,
       "pm253PerfTelecomLinePast15StatHistorySesValuePort1": pm253PerfTelecomLinePast15StatHistorySesValuePort1,
       "pm253PerfTelecomLinePast15StatHistoryInvSefsPort1": pm253PerfTelecomLinePast15StatHistoryInvSefsPort1,
       "pm253PerfTelecomLinePast15StatHistorySefsValuePort1": pm253PerfTelecomLinePast15StatHistorySefsValuePort1,
       "pm253PerfTelecomLinePast15StatHistoryInvUasPort1": pm253PerfTelecomLinePast15StatHistoryInvUasPort1,
       "pm253PerfTelecomLinePast15StatHistoryUasValuePort1": pm253PerfTelecomLinePast15StatHistoryUasValuePort1,
       "pm253PerfTelecomLineCurrent24StatTable": pm253PerfTelecomLineCurrent24StatTable,
       "pm253PerfTelecomLineCurrent24StatEntry": pm253PerfTelecomLineCurrent24StatEntry,
       "pm253PerfTelecomLineCurrent24StatIndex": pm253PerfTelecomLineCurrent24StatIndex,
       "pm253PerfTelecomLineCurrent24StatInvCvPortn": pm253PerfTelecomLineCurrent24StatInvCvPortn,
       "pm253PerfTelecomLineCurrent24StatCvValuePortn": pm253PerfTelecomLineCurrent24StatCvValuePortn,
       "pm253PerfTelecomLineCurrent24StatInvEsPortn": pm253PerfTelecomLineCurrent24StatInvEsPortn,
       "pm253PerfTelecomLineCurrent24StatEsValuePortn": pm253PerfTelecomLineCurrent24StatEsValuePortn,
       "pm253PerfTelecomLineCurrent24StatInvSesPortn": pm253PerfTelecomLineCurrent24StatInvSesPortn,
       "pm253PerfTelecomLineCurrent24StatSesValuePortn": pm253PerfTelecomLineCurrent24StatSesValuePortn,
       "pm253PerfTelecomLineCurrent24StatInvSefsPortn": pm253PerfTelecomLineCurrent24StatInvSefsPortn,
       "pm253PerfTelecomLineCurrent24StatSefsValuePortn": pm253PerfTelecomLineCurrent24StatSefsValuePortn,
       "pm253PerfTelecomLineCurrent24StatInvUasPortn": pm253PerfTelecomLineCurrent24StatInvUasPortn,
       "pm253PerfTelecomLineCurrent24StatUasValuePortn": pm253PerfTelecomLineCurrent24StatUasValuePortn,
       "pm253PerfTelecomLinePast24StatHistoryPort1Table": pm253PerfTelecomLinePast24StatHistoryPort1Table,
       "pm253PerfTelecomLinePast24StatHistoryPort1Entry": pm253PerfTelecomLinePast24StatHistoryPort1Entry,
       "pm253PerfTelecomLinePast24StatHistoryPort1Index": pm253PerfTelecomLinePast24StatHistoryPort1Index,
       "pm253PerfTelecomLinePast24StatHistoryInvCvPort1": pm253PerfTelecomLinePast24StatHistoryInvCvPort1,
       "pm253PerfTelecomLinePast24StatHistoryCvValuePort1": pm253PerfTelecomLinePast24StatHistoryCvValuePort1,
       "pm253PerfTelecomLinePast24StatHistoryInvEsPort1": pm253PerfTelecomLinePast24StatHistoryInvEsPort1,
       "pm253PerfTelecomLinePast24StatHistoryEsValuePort1": pm253PerfTelecomLinePast24StatHistoryEsValuePort1,
       "pm253PerfTelecomLinePast24StatHistoryInvSesPort1": pm253PerfTelecomLinePast24StatHistoryInvSesPort1,
       "pm253PerfTelecomLinePast24StatHistorySesValuePort1": pm253PerfTelecomLinePast24StatHistorySesValuePort1,
       "pm253PerfTelecomLinePast24StatHistoryInvSefsPort1": pm253PerfTelecomLinePast24StatHistoryInvSefsPort1,
       "pm253PerfTelecomLinePast24StatHistorySefsValuePort1": pm253PerfTelecomLinePast24StatHistorySefsValuePort1,
       "pm253PerfTelecomLinePast24StatHistoryInvUasPort1": pm253PerfTelecomLinePast24StatHistoryInvUasPort1,
       "pm253PerfTelecomLinePast24StatHistoryUasValuePort1": pm253PerfTelecomLinePast24StatHistoryUasValuePort1,
       "pm253PerfTelecomLinePast15StatHistoryPort2Table": pm253PerfTelecomLinePast15StatHistoryPort2Table,
       "pm253PerfTelecomLinePast15StatHistoryPort2Entry": pm253PerfTelecomLinePast15StatHistoryPort2Entry,
       "pm253PerfTelecomLinePast15StatHistoryPort2Index": pm253PerfTelecomLinePast15StatHistoryPort2Index,
       "pm253PerfTelecomLinePast15StatHistoryInvCvPort2": pm253PerfTelecomLinePast15StatHistoryInvCvPort2,
       "pm253PerfTelecomLinePast15StatHistoryCvValuePort2": pm253PerfTelecomLinePast15StatHistoryCvValuePort2,
       "pm253PerfTelecomLinePast15StatHistoryInvEsPort2": pm253PerfTelecomLinePast15StatHistoryInvEsPort2,
       "pm253PerfTelecomLinePast15StatHistoryEsValuePort2": pm253PerfTelecomLinePast15StatHistoryEsValuePort2,
       "pm253PerfTelecomLinePast15StatHistoryInvSesPort2": pm253PerfTelecomLinePast15StatHistoryInvSesPort2,
       "pm253PerfTelecomLinePast15StatHistorySesValuePort2": pm253PerfTelecomLinePast15StatHistorySesValuePort2,
       "pm253PerfTelecomLinePast15StatHistoryInvSefsPort2": pm253PerfTelecomLinePast15StatHistoryInvSefsPort2,
       "pm253PerfTelecomLinePast15StatHistorySefsValuePort2": pm253PerfTelecomLinePast15StatHistorySefsValuePort2,
       "pm253PerfTelecomLinePast15StatHistoryInvUasPort2": pm253PerfTelecomLinePast15StatHistoryInvUasPort2,
       "pm253PerfTelecomLinePast15StatHistoryUasValuePort2": pm253PerfTelecomLinePast15StatHistoryUasValuePort2,
       "pm253PerfTelecomLinePast24StatHistoryPort2Table": pm253PerfTelecomLinePast24StatHistoryPort2Table,
       "pm253PerfTelecomLinePast24StatHistoryPort2Entry": pm253PerfTelecomLinePast24StatHistoryPort2Entry,
       "pm253PerfTelecomLinePast24StatHistoryPort2Index": pm253PerfTelecomLinePast24StatHistoryPort2Index,
       "pm253PerfTelecomLinePast24StatHistoryInvCvPort2": pm253PerfTelecomLinePast24StatHistoryInvCvPort2,
       "pm253PerfTelecomLinePast24StatHistoryCvValuePort2": pm253PerfTelecomLinePast24StatHistoryCvValuePort2,
       "pm253PerfTelecomLinePast24StatHistoryInvEsPort2": pm253PerfTelecomLinePast24StatHistoryInvEsPort2,
       "pm253PerfTelecomLinePast24StatHistoryEsValuePort2": pm253PerfTelecomLinePast24StatHistoryEsValuePort2,
       "pm253PerfTelecomLinePast24StatHistoryInvSesPort2": pm253PerfTelecomLinePast24StatHistoryInvSesPort2,
       "pm253PerfTelecomLinePast24StatHistorySesValuePort2": pm253PerfTelecomLinePast24StatHistorySesValuePort2,
       "pm253PerfTelecomLinePast24StatHistoryInvSefsPort2": pm253PerfTelecomLinePast24StatHistoryInvSefsPort2,
       "pm253PerfTelecomLinePast24StatHistorySefsValuePort2": pm253PerfTelecomLinePast24StatHistorySefsValuePort2,
       "pm253PerfTelecomLinePast24StatHistoryInvUasPort2": pm253PerfTelecomLinePast24StatHistoryInvUasPort2,
       "pm253PerfTelecomLinePast24StatHistoryUasValuePort2": pm253PerfTelecomLinePast24StatHistoryUasValuePort2}
)
