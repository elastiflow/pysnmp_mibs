# SNMP MIB module (FSP_I-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/adva_2544/FSP_I-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 00:07:58 2025
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Adva_ObjectIdentity = ObjectIdentity
adva = _Adva_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1)
)
_OptChanMplx_ObjectIdentity = ObjectIdentity
optChanMplx = _OptChanMplx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1)
)
_OcmSys_ObjectIdentity = ObjectIdentity
ocmSys = _OcmSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 1)
)
_OcmSysMan_Type = DisplayString
_OcmSysMan_Object = MibScalar
ocmSysMan = _OcmSysMan_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 1, 1),
    _OcmSysMan_Type()
)
ocmSysMan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmSysMan.setStatus("mandatory")
_OcmSysType_Type = DisplayString
_OcmSysType_Object = MibScalar
ocmSysType = _OcmSysType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 1, 2),
    _OcmSysType_Type()
)
ocmSysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmSysType.setStatus("mandatory")
_OcmSysSerNo_Type = DisplayString
_OcmSysSerNo_Object = MibScalar
ocmSysSerNo = _OcmSysSerNo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 1, 3),
    _OcmSysSerNo_Type()
)
ocmSysSerNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmSysSerNo.setStatus("mandatory")
_OcmSysVer_Type = DisplayString
_OcmSysVer_Object = MibScalar
ocmSysVer = _OcmSysVer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 1, 4),
    _OcmSysVer_Type()
)
ocmSysVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmSysVer.setStatus("mandatory")
_OcmSysTime_Type = TimeTicks
_OcmSysTime_Object = MibScalar
ocmSysTime = _OcmSysTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 1, 5),
    _OcmSysTime_Type()
)
ocmSysTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmSysTime.setStatus("mandatory")
_OcmSysError_Type = Integer32
_OcmSysError_Object = MibScalar
ocmSysError = _OcmSysError_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 1, 6),
    _OcmSysError_Type()
)
ocmSysError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmSysError.setStatus("mandatory")
_OcmSysBusMessages_Type = Integer32
_OcmSysBusMessages_Object = MibScalar
ocmSysBusMessages = _OcmSysBusMessages_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 1, 12),
    _OcmSysBusMessages_Type()
)
ocmSysBusMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmSysBusMessages.setStatus("mandatory")
_OcmSysBusErrors_Type = Integer32
_OcmSysBusErrors_Object = MibScalar
ocmSysBusErrors = _OcmSysBusErrors_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 1, 13),
    _OcmSysBusErrors_Type()
)
ocmSysBusErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmSysBusErrors.setStatus("mandatory")
_OcmSysMotd_Type = DisplayString
_OcmSysMotd_Object = MibScalar
ocmSysMotd = _OcmSysMotd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 1, 14),
    _OcmSysMotd_Type()
)
ocmSysMotd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmSysMotd.setStatus("mandatory")
_OcmSysTrapsinkTable_Object = MibTable
ocmSysTrapsinkTable = _OcmSysTrapsinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 1, 15)
)
if mibBuilder.loadTexts:
    ocmSysTrapsinkTable.setStatus("mandatory")
_OcmSysTrapsinkEntry_Object = MibTableRow
ocmSysTrapsinkEntry = _OcmSysTrapsinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 1, 15, 1)
)
ocmSysTrapsinkEntry.setIndexNames(
    (0, "FSP_I-MIB", "ocmSysTrapsinkNumber"),
)
if mibBuilder.loadTexts:
    ocmSysTrapsinkEntry.setStatus("mandatory")


class _OcmSysTrapsinkNumber_Type(Integer32):
    """Custom type ocmSysTrapsinkNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_OcmSysTrapsinkNumber_Type.__name__ = "Integer32"
_OcmSysTrapsinkNumber_Object = MibTableColumn
ocmSysTrapsinkNumber = _OcmSysTrapsinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 1, 15, 1, 1),
    _OcmSysTrapsinkNumber_Type()
)
ocmSysTrapsinkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmSysTrapsinkNumber.setStatus("mandatory")
_OcmSysTrapsinkAddress_Type = DisplayString
_OcmSysTrapsinkAddress_Object = MibTableColumn
ocmSysTrapsinkAddress = _OcmSysTrapsinkAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 1, 15, 1, 2),
    _OcmSysTrapsinkAddress_Type()
)
ocmSysTrapsinkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmSysTrapsinkAddress.setStatus("mandatory")
_OcmSysTrapsinkCommunity_Type = DisplayString
_OcmSysTrapsinkCommunity_Object = MibTableColumn
ocmSysTrapsinkCommunity = _OcmSysTrapsinkCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 1, 15, 1, 3),
    _OcmSysTrapsinkCommunity_Type()
)
ocmSysTrapsinkCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmSysTrapsinkCommunity.setStatus("mandatory")


class _OcmSysTrapsinkPriority_Type(Integer32):
    """Custom type ocmSysTrapsinkPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_OcmSysTrapsinkPriority_Type.__name__ = "Integer32"
_OcmSysTrapsinkPriority_Object = MibTableColumn
ocmSysTrapsinkPriority = _OcmSysTrapsinkPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 1, 15, 1, 4),
    _OcmSysTrapsinkPriority_Type()
)
ocmSysTrapsinkPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmSysTrapsinkPriority.setStatus("mandatory")
_OcmSysLogfileTable_Object = MibTable
ocmSysLogfileTable = _OcmSysLogfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 1, 16)
)
if mibBuilder.loadTexts:
    ocmSysLogfileTable.setStatus("mandatory")
_OcmSysLogfileEntry_Object = MibTableRow
ocmSysLogfileEntry = _OcmSysLogfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 1, 16, 1)
)
ocmSysLogfileEntry.setIndexNames(
    (0, "FSP_I-MIB", "ocmSysLogfileNumber"),
)
if mibBuilder.loadTexts:
    ocmSysLogfileEntry.setStatus("mandatory")


class _OcmSysLogfileNumber_Type(Integer32):
    """Custom type ocmSysLogfileNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_OcmSysLogfileNumber_Type.__name__ = "Integer32"
_OcmSysLogfileNumber_Object = MibTableColumn
ocmSysLogfileNumber = _OcmSysLogfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 1, 16, 1, 1),
    _OcmSysLogfileNumber_Type()
)
ocmSysLogfileNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmSysLogfileNumber.setStatus("mandatory")
_OcmSysLogfileName_Type = DisplayString
_OcmSysLogfileName_Object = MibTableColumn
ocmSysLogfileName = _OcmSysLogfileName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 1, 16, 1, 2),
    _OcmSysLogfileName_Type()
)
ocmSysLogfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmSysLogfileName.setStatus("mandatory")
_OcmSysLogfileSize_Type = Integer32
_OcmSysLogfileSize_Object = MibTableColumn
ocmSysLogfileSize = _OcmSysLogfileSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 1, 16, 1, 3),
    _OcmSysLogfileSize_Type()
)
ocmSysLogfileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmSysLogfileSize.setStatus("mandatory")


class _OcmSysLogfilePriority_Type(Integer32):
    """Custom type ocmSysLogfilePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_OcmSysLogfilePriority_Type.__name__ = "Integer32"
_OcmSysLogfilePriority_Object = MibTableColumn
ocmSysLogfilePriority = _OcmSysLogfilePriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 1, 16, 1, 4),
    _OcmSysLogfilePriority_Type()
)
ocmSysLogfilePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmSysLogfilePriority.setStatus("mandatory")
_OcmSysNEMIType_Type = DisplayString
_OcmSysNEMIType_Object = MibScalar
ocmSysNEMIType = _OcmSysNEMIType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 1, 20),
    _OcmSysNEMIType_Type()
)
ocmSysNEMIType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmSysNEMIType.setStatus("mandatory")
_OcmSysNEMISerNo_Type = DisplayString
_OcmSysNEMISerNo_Object = MibScalar
ocmSysNEMISerNo = _OcmSysNEMISerNo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 1, 21),
    _OcmSysNEMISerNo_Type()
)
ocmSysNEMISerNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmSysNEMISerNo.setStatus("mandatory")
_OcmPs_ObjectIdentity = ObjectIdentity
ocmPs = _OcmPs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 2)
)
_OcmPsTable_Object = MibTable
ocmPsTable = _OcmPsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ocmPsTable.setStatus("mandatory")
_OcmPsEntry_Object = MibTableRow
ocmPsEntry = _OcmPsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 2, 1, 1)
)
ocmPsEntry.setIndexNames(
    (0, "FSP_I-MIB", "ocmPsNumber"),
)
if mibBuilder.loadTexts:
    ocmPsEntry.setStatus("mandatory")
_OcmPsNumber_Type = Integer32
_OcmPsNumber_Object = MibTableColumn
ocmPsNumber = _OcmPsNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 2, 1, 1, 1),
    _OcmPsNumber_Type()
)
ocmPsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmPsNumber.setStatus("mandatory")


class _OcmPsOn_Type(Integer32):
    """Custom type ocmPsOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_OcmPsOn_Type.__name__ = "Integer32"
_OcmPsOn_Object = MibTableColumn
ocmPsOn = _OcmPsOn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 2, 1, 1, 2),
    _OcmPsOn_Type()
)
ocmPsOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmPsOn.setStatus("mandatory")
_OcmFan_ObjectIdentity = ObjectIdentity
ocmFan = _OcmFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 3)
)


class _OcmFan1Inst_Type(Integer32):
    """Custom type ocmFan1Inst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("notInstalled", 2))
    )


_OcmFan1Inst_Type.__name__ = "Integer32"
_OcmFan1Inst_Object = MibScalar
ocmFan1Inst = _OcmFan1Inst_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 3, 1),
    _OcmFan1Inst_Type()
)
ocmFan1Inst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmFan1Inst.setStatus("mandatory")
_OcmFan1_ObjectIdentity = ObjectIdentity
ocmFan1 = _OcmFan1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 3, 2)
)


class _OcmFan1On_Type(Integer32):
    """Custom type ocmFan1On based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_OcmFan1On_Type.__name__ = "Integer32"
_OcmFan1On_Object = MibScalar
ocmFan1On = _OcmFan1On_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 3, 2, 1),
    _OcmFan1On_Type()
)
ocmFan1On.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmFan1On.setStatus("optional")


class _OcmFan2Inst_Type(Integer32):
    """Custom type ocmFan2Inst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("notInstalled", 2))
    )


_OcmFan2Inst_Type.__name__ = "Integer32"
_OcmFan2Inst_Object = MibScalar
ocmFan2Inst = _OcmFan2Inst_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 3, 3),
    _OcmFan2Inst_Type()
)
ocmFan2Inst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmFan2Inst.setStatus("mandatory")
_OcmFan2_ObjectIdentity = ObjectIdentity
ocmFan2 = _OcmFan2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 3, 4)
)


class _OcmFan2On_Type(Integer32):
    """Custom type ocmFan2On based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_OcmFan2On_Type.__name__ = "Integer32"
_OcmFan2On_Object = MibScalar
ocmFan2On = _OcmFan2On_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 3, 4, 1),
    _OcmFan2On_Type()
)
ocmFan2On.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmFan2On.setStatus("optional")
_OcmChan_ObjectIdentity = ObjectIdentity
ocmChan = _OcmChan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 4)
)
_OcmChanTable_Object = MibTable
ocmChanTable = _OcmChanTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ocmChanTable.setStatus("mandatory")
_OcmChanEntry_Object = MibTableRow
ocmChanEntry = _OcmChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 4, 1, 1)
)
ocmChanEntry.setIndexNames(
    (0, "FSP_I-MIB", "ocmChanNumber"),
)
if mibBuilder.loadTexts:
    ocmChanEntry.setStatus("mandatory")
_OcmChanNumber_Type = Integer32
_OcmChanNumber_Object = MibTableColumn
ocmChanNumber = _OcmChanNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 4, 1, 1, 1),
    _OcmChanNumber_Type()
)
ocmChanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmChanNumber.setStatus("optional")
_OcmChanSerNo_Type = DisplayString
_OcmChanSerNo_Object = MibTableColumn
ocmChanSerNo = _OcmChanSerNo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 4, 1, 1, 2),
    _OcmChanSerNo_Type()
)
ocmChanSerNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmChanSerNo.setStatus("optional")


class _OcmChanRecLocOn_Type(Integer32):
    """Custom type ocmChanRecLocOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_OcmChanRecLocOn_Type.__name__ = "Integer32"
_OcmChanRecLocOn_Object = MibTableColumn
ocmChanRecLocOn = _OcmChanRecLocOn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 4, 1, 1, 3),
    _OcmChanRecLocOn_Type()
)
ocmChanRecLocOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmChanRecLocOn.setStatus("optional")


class _OcmChanRecRemOn_Type(Integer32):
    """Custom type ocmChanRecRemOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_OcmChanRecRemOn_Type.__name__ = "Integer32"
_OcmChanRecRemOn_Object = MibTableColumn
ocmChanRecRemOn = _OcmChanRecRemOn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 4, 1, 1, 4),
    _OcmChanRecRemOn_Type()
)
ocmChanRecRemOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmChanRecRemOn.setStatus("optional")


class _OcmChanLasLocOn_Type(Integer32):
    """Custom type ocmChanLasLocOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("alwaysOn", 3),
          ("alwaysOff", 4))
    )


_OcmChanLasLocOn_Type.__name__ = "Integer32"
_OcmChanLasLocOn_Object = MibTableColumn
ocmChanLasLocOn = _OcmChanLasLocOn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 4, 1, 1, 5),
    _OcmChanLasLocOn_Type()
)
ocmChanLasLocOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmChanLasLocOn.setStatus("optional")


class _OcmChanLasLocC_Type(Integer32):
    """Custom type ocmChanLasLocC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_OcmChanLasLocC_Type.__name__ = "Integer32"
_OcmChanLasLocC_Object = MibTableColumn
ocmChanLasLocC = _OcmChanLasLocC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 4, 1, 1, 6),
    _OcmChanLasLocC_Type()
)
ocmChanLasLocC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmChanLasLocC.setStatus("optional")


class _OcmChanLasLocMaxC_Type(Integer32):
    """Custom type ocmChanLasLocMaxC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_OcmChanLasLocMaxC_Type.__name__ = "Integer32"
_OcmChanLasLocMaxC_Object = MibTableColumn
ocmChanLasLocMaxC = _OcmChanLasLocMaxC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 4, 1, 1, 7),
    _OcmChanLasLocMaxC_Type()
)
ocmChanLasLocMaxC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmChanLasLocMaxC.setStatus("optional")


class _OcmChanLasRemOn_Type(Integer32):
    """Custom type ocmChanLasRemOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("alwaysOn", 3),
          ("alwaysOff", 4))
    )


_OcmChanLasRemOn_Type.__name__ = "Integer32"
_OcmChanLasRemOn_Object = MibTableColumn
ocmChanLasRemOn = _OcmChanLasRemOn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 4, 1, 1, 8),
    _OcmChanLasRemOn_Type()
)
ocmChanLasRemOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmChanLasRemOn.setStatus("optional")


class _OcmChanLasRemC_Type(Integer32):
    """Custom type ocmChanLasRemC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_OcmChanLasRemC_Type.__name__ = "Integer32"
_OcmChanLasRemC_Object = MibTableColumn
ocmChanLasRemC = _OcmChanLasRemC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 4, 1, 1, 9),
    _OcmChanLasRemC_Type()
)
ocmChanLasRemC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmChanLasRemC.setStatus("optional")


class _OcmChanLasRemMaxC_Type(Integer32):
    """Custom type ocmChanLasRemMaxC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_OcmChanLasRemMaxC_Type.__name__ = "Integer32"
_OcmChanLasRemMaxC_Object = MibTableColumn
ocmChanLasRemMaxC = _OcmChanLasRemMaxC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 4, 1, 1, 10),
    _OcmChanLasRemMaxC_Type()
)
ocmChanLasRemMaxC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmChanLasRemMaxC.setStatus("optional")


class _OcmChanLRCooledInst_Type(Integer32):
    """Custom type ocmChanLRCooledInst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("notInstalled", 2))
    )


_OcmChanLRCooledInst_Type.__name__ = "Integer32"
_OcmChanLRCooledInst_Object = MibTableColumn
ocmChanLRCooledInst = _OcmChanLRCooledInst_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 4, 1, 1, 11),
    _OcmChanLRCooledInst_Type()
)
ocmChanLRCooledInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmChanLRCooledInst.setStatus("optional")


class _OcmChanLRCooledTemp_Type(Integer32):
    """Custom type ocmChanLRCooledTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_OcmChanLRCooledTemp_Type.__name__ = "Integer32"
_OcmChanLRCooledTemp_Object = MibTableColumn
ocmChanLRCooledTemp = _OcmChanLRCooledTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 4, 1, 1, 12),
    _OcmChanLRCooledTemp_Type()
)
ocmChanLRCooledTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmChanLRCooledTemp.setStatus("optional")


class _OcmChanETemp_Type(Integer32):
    """Custom type ocmChanETemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_OcmChanETemp_Type.__name__ = "Integer32"
_OcmChanETemp_Object = MibTableColumn
ocmChanETemp = _OcmChanETemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 4, 1, 1, 13),
    _OcmChanETemp_Type()
)
ocmChanETemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmChanETemp.setStatus("optional")


class _OcmChanLRCooledOor_Type(Integer32):
    """Custom type ocmChanLRCooledOor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_OcmChanLRCooledOor_Type.__name__ = "Integer32"
_OcmChanLRCooledOor_Object = MibTableColumn
ocmChanLRCooledOor = _OcmChanLRCooledOor_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 4, 1, 1, 14),
    _OcmChanLRCooledOor_Type()
)
ocmChanLRCooledOor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmChanLRCooledOor.setStatus("optional")


class _OcmChanClkInst_Type(Integer32):
    """Custom type ocmChanClkInst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("notInstalled", 2))
    )


_OcmChanClkInst_Type.__name__ = "Integer32"
_OcmChanClkInst_Object = MibTableColumn
ocmChanClkInst = _OcmChanClkInst_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 4, 1, 1, 15),
    _OcmChanClkInst_Type()
)
ocmChanClkInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmChanClkInst.setStatus("optional")


class _OcmChanClkOn_Type(Integer32):
    """Custom type ocmChanClkOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("fixedFrequency1", 3),
          ("fixedFrequency2", 4),
          ("fixedFrequency3", 5),
          ("fixedFrequency4", 6))
    )


_OcmChanClkOn_Type.__name__ = "Integer32"
_OcmChanClkOn_Object = MibTableColumn
ocmChanClkOn = _OcmChanClkOn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 4, 1, 1, 16),
    _OcmChanClkOn_Type()
)
ocmChanClkOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocmChanClkOn.setStatus("optional")


class _OcmChanClkFail_Type(Integer32):
    """Custom type ocmChanClkFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("notFailed", 2))
    )


_OcmChanClkFail_Type.__name__ = "Integer32"
_OcmChanClkFail_Object = MibTableColumn
ocmChanClkFail = _OcmChanClkFail_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 4, 1, 1, 17),
    _OcmChanClkFail_Type()
)
ocmChanClkFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmChanClkFail.setStatus("optional")


class _OcmChan2ndRecRemOn_Type(Integer32):
    """Custom type ocmChan2ndRecRemOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("notInstalled", 3))
    )


_OcmChan2ndRecRemOn_Type.__name__ = "Integer32"
_OcmChan2ndRecRemOn_Object = MibTableColumn
ocmChan2ndRecRemOn = _OcmChan2ndRecRemOn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 4, 1, 1, 18),
    _OcmChan2ndRecRemOn_Type()
)
ocmChan2ndRecRemOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmChan2ndRecRemOn.setStatus("optional")


class _OcmChanClockType_Type(Integer32):
    """Custom type ocmChanClockType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5,
              7,
              21,
              22,
              31,
              32,
              41,
              42,
              51,
              52,
              61,
              62,
              71,
              72,
              75,
              76,
              81,
              82,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noClock", 0),
          ("multiClockModule", 1),
          ("multiClock", 2),
          ("multiClockA", 3),
          ("multiClockB", 5),
          ("multiClockC", 7),
          ("fixedClock125MbpsModule", 21),
          ("fixedClock125Mbps", 22),
          ("fixedClock155MbpsModule", 31),
          ("fixedClock155Mbps", 32),
          ("fixedClock200MbpsModule", 41),
          ("fixedClock200Mbps", 42),
          ("fixedClock266MbpsModule", 51),
          ("fixedClock266Mbps", 52),
          ("fixedClock622MbpsModule", 61),
          ("fixedClock622Mbps", 62),
          ("fixedClock1062MbpsModule", 71),
          ("fixedClock1062Mbps", 72),
          ("fixedClock1250MbpsModule", 75),
          ("fixedClock1250Mbps", 76),
          ("fixedClock2500MbpsModule", 81),
          ("fixedClock2500Mbps", 82),
          ("other", 255))
    )


_OcmChanClockType_Type.__name__ = "Integer32"
_OcmChanClockType_Object = MibTableColumn
ocmChanClockType = _OcmChanClockType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 4, 1, 1, 19),
    _OcmChanClockType_Type()
)
ocmChanClockType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmChanClockType.setStatus("mandatory")


class _OcmChanSlotType_Type(Integer32):
    """Custom type ocmChanSlotType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              8,
              9,
              32,
              33,
              64,
              255)
        )
    )
    namedValues = NamedValues(
        *(("hotStandbyConverter", 0),
          ("fsp_II_Converter", 1),
          ("fsp_I_Converter", 2),
          ("fsp_I_EthernetConverter", 3),
          ("hotStandbyEthernetConverter", 4),
          ("fsp_I_Transceiver", 8),
          ("fsp_I_HSTransceiver", 9),
          ("nemi_master", 32),
          ("nemi_slave", 33),
          ("switch", 64),
          ("other", 255))
    )


_OcmChanSlotType_Type.__name__ = "Integer32"
_OcmChanSlotType_Object = MibTableColumn
ocmChanSlotType = _OcmChanSlotType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 4, 1, 1, 20),
    _OcmChanSlotType_Type()
)
ocmChanSlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmChanSlotType.setStatus("mandatory")


class _OcmChanActiveLine_Type(Integer32):
    """Custom type ocmChanActiveLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lineA", 1),
          ("lineB", 2))
    )


_OcmChanActiveLine_Type.__name__ = "Integer32"
_OcmChanActiveLine_Object = MibTableColumn
ocmChanActiveLine = _OcmChanActiveLine_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 4, 1, 1, 21),
    _OcmChanActiveLine_Type()
)
ocmChanActiveLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmChanActiveLine.setStatus("mandatory")


class _OcmChanLineLocked_Type(Integer32):
    """Custom type ocmChanLineLocked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("locked", 2))
    )


_OcmChanLineLocked_Type.__name__ = "Integer32"
_OcmChanLineLocked_Object = MibTableColumn
ocmChanLineLocked = _OcmChanLineLocked_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 4, 1, 1, 22),
    _OcmChanLineLocked_Type()
)
ocmChanLineLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmChanLineLocked.setStatus("mandatory")


class _OcmChanEPLDVersion_Type(Integer32):
    """Custom type ocmChanEPLDVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OcmChanEPLDVersion_Type.__name__ = "Integer32"
_OcmChanEPLDVersion_Object = MibTableColumn
ocmChanEPLDVersion = _OcmChanEPLDVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 4, 1, 1, 23),
    _OcmChanEPLDVersion_Type()
)
ocmChanEPLDVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmChanEPLDVersion.setStatus("mandatory")
_OcmChanHardwareVersion_Type = DisplayString
_OcmChanHardwareVersion_Object = MibTableColumn
ocmChanHardwareVersion = _OcmChanHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 4, 1, 1, 24),
    _OcmChanHardwareVersion_Type()
)
ocmChanHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmChanHardwareVersion.setStatus("mandatory")
_OcmChanSoftwareVersion_Type = DisplayString
_OcmChanSoftwareVersion_Object = MibTableColumn
ocmChanSoftwareVersion = _OcmChanSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 4, 1, 1, 25),
    _OcmChanSoftwareVersion_Type()
)
ocmChanSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmChanSoftwareVersion.setStatus("mandatory")
_OcmChanType_Type = DisplayString
_OcmChanType_Object = MibTableColumn
ocmChanType = _OcmChanType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 4, 1, 1, 26),
    _OcmChanType_Type()
)
ocmChanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmChanType.setStatus("mandatory")
_OcmChanComment_Type = DisplayString
_OcmChanComment_Object = MibTableColumn
ocmChanComment = _OcmChanComment_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 4, 1, 1, 27),
    _OcmChanComment_Type()
)
ocmChanComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmChanComment.setStatus("mandatory")


class _OcmChanBoardVoltage_Type(Integer32):
    """Custom type ocmChanBoardVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5500),
    )


_OcmChanBoardVoltage_Type.__name__ = "Integer32"
_OcmChanBoardVoltage_Object = MibTableColumn
ocmChanBoardVoltage = _OcmChanBoardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 4, 1, 1, 28),
    _OcmChanBoardVoltage_Type()
)
ocmChanBoardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmChanBoardVoltage.setStatus("mandatory")
_OcmChanDatarate_Type = Integer32
_OcmChanDatarate_Object = MibTableColumn
ocmChanDatarate = _OcmChanDatarate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 4, 1, 1, 29),
    _OcmChanDatarate_Type()
)
ocmChanDatarate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmChanDatarate.setStatus("optional")


class _OcmChanRemLoop_Type(Integer32):
    """Custom type ocmChanRemLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("notApplicable", 3))
    )


_OcmChanRemLoop_Type.__name__ = "Integer32"
_OcmChanRemLoop_Object = MibTableColumn
ocmChanRemLoop = _OcmChanRemLoop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 4, 1, 1, 30),
    _OcmChanRemLoop_Type()
)
ocmChanRemLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocmChanRemLoop.setStatus("optional")


class _OcmChanLocLoop_Type(Integer32):
    """Custom type ocmChanLocLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("notApplicable", 3))
    )


_OcmChanLocLoop_Type.__name__ = "Integer32"
_OcmChanLocLoop_Object = MibTableColumn
ocmChanLocLoop = _OcmChanLocLoop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 4, 1, 1, 31),
    _OcmChanLocLoop_Type()
)
ocmChanLocLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocmChanLocLoop.setStatus("optional")
_OcmTrap_ObjectIdentity = ObjectIdentity
ocmTrap = _OcmTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 7)
)
_OcmTrapText_Type = DisplayString
_OcmTrapText_Object = MibScalar
ocmTrapText = _OcmTrapText_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 99),
    _OcmTrapText_Type()
)
ocmTrapText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocmTrapText.setStatus("mandatory")

# Managed Objects groups


# Notification objects

chanClockrecFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 7, 0, 12)
)
chanClockrecFail.setObjects(
      *(("FSP_I-MIB", "ocmChanNumber"),
        ("FSP_I-MIB", "ocmTrapText"))
)
if mibBuilder.loadTexts:
    chanClockrecFail.setStatus(
        ""
    )

chanRecRemLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 7, 0, 14)
)
chanRecRemLOS.setObjects(
      *(("FSP_I-MIB", "ocmChanNumber"),
        ("FSP_I-MIB", "ocmTrapText"))
)
if mibBuilder.loadTexts:
    chanRecRemLOS.setStatus(
        ""
    )

chanRecLocLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 7, 0, 15)
)
chanRecLocLOS.setObjects(
      *(("FSP_I-MIB", "ocmChanNumber"),
        ("FSP_I-MIB", "ocmTrapText"))
)
if mibBuilder.loadTexts:
    chanRecLocLOS.setStatus(
        ""
    )

fanFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 7, 0, 16)
)
fanFail.setObjects(
      *(("FSP_I-MIB", "ocmSysError"),
        ("FSP_I-MIB", "ocmTrapText"))
)
if mibBuilder.loadTexts:
    fanFail.setStatus(
        ""
    )

psFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 7, 0, 18)
)
psFail.setObjects(
      *(("FSP_I-MIB", "ocmPsNumber"),
        ("FSP_I-MIB", "ocmTrapText"))
)
if mibBuilder.loadTexts:
    psFail.setStatus(
        ""
    )

psOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 7, 0, 19)
)
psOk.setObjects(
      *(("FSP_I-MIB", "ocmPsNumber"),
        ("FSP_I-MIB", "ocmTrapText"))
)
if mibBuilder.loadTexts:
    psOk.setStatus(
        ""
    )

chanRecRemNoLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 7, 0, 20)
)
chanRecRemNoLOS.setObjects(
      *(("FSP_I-MIB", "ocmChanNumber"),
        ("FSP_I-MIB", "ocmTrapText"))
)
if mibBuilder.loadTexts:
    chanRecRemNoLOS.setStatus(
        ""
    )

chanRecLocNoLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 7, 0, 21)
)
chanRecLocNoLOS.setObjects(
      *(("FSP_I-MIB", "ocmChanNumber"),
        ("FSP_I-MIB", "ocmTrapText"))
)
if mibBuilder.loadTexts:
    chanRecLocNoLOS.setStatus(
        ""
    )

chanHardwareAdd = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 7, 0, 22)
)
chanHardwareAdd.setObjects(
      *(("FSP_I-MIB", "ocmChanNumber"),
        ("FSP_I-MIB", "ocmTrapText"))
)
if mibBuilder.loadTexts:
    chanHardwareAdd.setStatus(
        ""
    )

chanHardwareDel = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 7, 0, 23)
)
chanHardwareDel.setObjects(
      *(("FSP_I-MIB", "ocmChanNumber"),
        ("FSP_I-MIB", "ocmTrapText"))
)
if mibBuilder.loadTexts:
    chanHardwareDel.setStatus(
        ""
    )

chanClockrecNoFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 7, 0, 24)
)
chanClockrecNoFail.setObjects(
      *(("FSP_I-MIB", "ocmChanNumber"),
        ("FSP_I-MIB", "ocmTrapText"))
)
if mibBuilder.loadTexts:
    chanClockrecNoFail.setStatus(
        ""
    )

fanOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 7, 0, 25)
)
fanOk.setObjects(
      *(("FSP_I-MIB", "ocmSysError"),
        ("FSP_I-MIB", "ocmTrapText"))
)
if mibBuilder.loadTexts:
    fanOk.setStatus(
        ""
    )

chan2ndRecRemLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 7, 0, 26)
)
chan2ndRecRemLOS.setObjects(
      *(("FSP_I-MIB", "ocmChanNumber"),
        ("FSP_I-MIB", "ocmTrapText"))
)
if mibBuilder.loadTexts:
    chan2ndRecRemLOS.setStatus(
        ""
    )

chan2ndRecRemNoLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 7, 0, 27)
)
chan2ndRecRemNoLOS.setObjects(
      *(("FSP_I-MIB", "ocmChanNumber"),
        ("FSP_I-MIB", "ocmTrapText"))
)
if mibBuilder.loadTexts:
    chan2ndRecRemNoLOS.setStatus(
        ""
    )

chanChangeLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 7, 0, 28)
)
chanChangeLine.setObjects(
      *(("FSP_I-MIB", "ocmChanNumber"),
        ("FSP_I-MIB", "ocmChanActiveLine"),
        ("FSP_I-MIB", "ocmTrapText"))
)
if mibBuilder.loadTexts:
    chanChangeLine.setStatus(
        ""
    )

chanChangeState = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 7, 0, 29)
)
chanChangeState.setObjects(
      *(("FSP_I-MIB", "ocmChanNumber"),
        ("FSP_I-MIB", "ocmChanLineLocked"),
        ("FSP_I-MIB", "ocmTrapText"))
)
if mibBuilder.loadTexts:
    chanChangeState.setStatus(
        ""
    )

chanRepeatedMessage = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 7, 0, 30)
)
chanRepeatedMessage.setObjects(
      *(("FSP_I-MIB", "ocmChanNumber"),
        ("FSP_I-MIB", "ocmSysError"),
        ("FSP_I-MIB", "ocmPsNumber"),
        ("FSP_I-MIB", "ocmTrapText"))
)
if mibBuilder.loadTexts:
    chanRepeatedMessage.setStatus(
        ""
    )

chanLocLoopOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 7, 0, 35)
)
chanLocLoopOn.setObjects(
      *(("FSP_I-MIB", "ocmChanNumber"),
        ("FSP_I-MIB", "ocmTrapText"))
)
if mibBuilder.loadTexts:
    chanLocLoopOn.setStatus(
        ""
    )

chanLocLoopOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 7, 0, 36)
)
chanLocLoopOff.setObjects(
      *(("FSP_I-MIB", "ocmChanNumber"),
        ("FSP_I-MIB", "ocmTrapText"))
)
if mibBuilder.loadTexts:
    chanLocLoopOff.setStatus(
        ""
    )

chanRemLoopOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 7, 0, 37)
)
chanRemLoopOn.setObjects(
      *(("FSP_I-MIB", "ocmChanNumber"),
        ("FSP_I-MIB", "ocmTrapText"))
)
if mibBuilder.loadTexts:
    chanRemLoopOn.setStatus(
        ""
    )

chanRemLoopOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 1, 7, 0, 38)
)
chanRemLoopOff.setObjects(
      *(("FSP_I-MIB", "ocmChanNumber"),
        ("FSP_I-MIB", "ocmTrapText"))
)
if mibBuilder.loadTexts:
    chanRemLoopOff.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FSP_I-MIB",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "adva": adva,
       "products": products,
       "optChanMplx": optChanMplx,
       "ocmSys": ocmSys,
       "ocmSysMan": ocmSysMan,
       "ocmSysType": ocmSysType,
       "ocmSysSerNo": ocmSysSerNo,
       "ocmSysVer": ocmSysVer,
       "ocmSysTime": ocmSysTime,
       "ocmSysError": ocmSysError,
       "ocmSysBusMessages": ocmSysBusMessages,
       "ocmSysBusErrors": ocmSysBusErrors,
       "ocmSysMotd": ocmSysMotd,
       "ocmSysTrapsinkTable": ocmSysTrapsinkTable,
       "ocmSysTrapsinkEntry": ocmSysTrapsinkEntry,
       "ocmSysTrapsinkNumber": ocmSysTrapsinkNumber,
       "ocmSysTrapsinkAddress": ocmSysTrapsinkAddress,
       "ocmSysTrapsinkCommunity": ocmSysTrapsinkCommunity,
       "ocmSysTrapsinkPriority": ocmSysTrapsinkPriority,
       "ocmSysLogfileTable": ocmSysLogfileTable,
       "ocmSysLogfileEntry": ocmSysLogfileEntry,
       "ocmSysLogfileNumber": ocmSysLogfileNumber,
       "ocmSysLogfileName": ocmSysLogfileName,
       "ocmSysLogfileSize": ocmSysLogfileSize,
       "ocmSysLogfilePriority": ocmSysLogfilePriority,
       "ocmSysNEMIType": ocmSysNEMIType,
       "ocmSysNEMISerNo": ocmSysNEMISerNo,
       "ocmPs": ocmPs,
       "ocmPsTable": ocmPsTable,
       "ocmPsEntry": ocmPsEntry,
       "ocmPsNumber": ocmPsNumber,
       "ocmPsOn": ocmPsOn,
       "ocmFan": ocmFan,
       "ocmFan1Inst": ocmFan1Inst,
       "ocmFan1": ocmFan1,
       "ocmFan1On": ocmFan1On,
       "ocmFan2Inst": ocmFan2Inst,
       "ocmFan2": ocmFan2,
       "ocmFan2On": ocmFan2On,
       "ocmChan": ocmChan,
       "ocmChanTable": ocmChanTable,
       "ocmChanEntry": ocmChanEntry,
       "ocmChanNumber": ocmChanNumber,
       "ocmChanSerNo": ocmChanSerNo,
       "ocmChanRecLocOn": ocmChanRecLocOn,
       "ocmChanRecRemOn": ocmChanRecRemOn,
       "ocmChanLasLocOn": ocmChanLasLocOn,
       "ocmChanLasLocC": ocmChanLasLocC,
       "ocmChanLasLocMaxC": ocmChanLasLocMaxC,
       "ocmChanLasRemOn": ocmChanLasRemOn,
       "ocmChanLasRemC": ocmChanLasRemC,
       "ocmChanLasRemMaxC": ocmChanLasRemMaxC,
       "ocmChanLRCooledInst": ocmChanLRCooledInst,
       "ocmChanLRCooledTemp": ocmChanLRCooledTemp,
       "ocmChanETemp": ocmChanETemp,
       "ocmChanLRCooledOor": ocmChanLRCooledOor,
       "ocmChanClkInst": ocmChanClkInst,
       "ocmChanClkOn": ocmChanClkOn,
       "ocmChanClkFail": ocmChanClkFail,
       "ocmChan2ndRecRemOn": ocmChan2ndRecRemOn,
       "ocmChanClockType": ocmChanClockType,
       "ocmChanSlotType": ocmChanSlotType,
       "ocmChanActiveLine": ocmChanActiveLine,
       "ocmChanLineLocked": ocmChanLineLocked,
       "ocmChanEPLDVersion": ocmChanEPLDVersion,
       "ocmChanHardwareVersion": ocmChanHardwareVersion,
       "ocmChanSoftwareVersion": ocmChanSoftwareVersion,
       "ocmChanType": ocmChanType,
       "ocmChanComment": ocmChanComment,
       "ocmChanBoardVoltage": ocmChanBoardVoltage,
       "ocmChanDatarate": ocmChanDatarate,
       "ocmChanRemLoop": ocmChanRemLoop,
       "ocmChanLocLoop": ocmChanLocLoop,
       "ocmTrap": ocmTrap,
       "chanClockrecFail": chanClockrecFail,
       "chanRecRemLOS": chanRecRemLOS,
       "chanRecLocLOS": chanRecLocLOS,
       "fanFail": fanFail,
       "psFail": psFail,
       "psOk": psOk,
       "chanRecRemNoLOS": chanRecRemNoLOS,
       "chanRecLocNoLOS": chanRecLocNoLOS,
       "chanHardwareAdd": chanHardwareAdd,
       "chanHardwareDel": chanHardwareDel,
       "chanClockrecNoFail": chanClockrecNoFail,
       "fanOk": fanOk,
       "chan2ndRecRemLOS": chan2ndRecRemLOS,
       "chan2ndRecRemNoLOS": chan2ndRecRemNoLOS,
       "chanChangeLine": chanChangeLine,
       "chanChangeState": chanChangeState,
       "chanRepeatedMessage": chanRepeatedMessage,
       "chanLocLoopOn": chanLocLoopOn,
       "chanLocLoopOff": chanLocLoopOff,
       "chanRemLoopOn": chanRemLoopOn,
       "chanRemLoopOff": chanRemLoopOff,
       "ocmTrapText": ocmTrapText}
)
