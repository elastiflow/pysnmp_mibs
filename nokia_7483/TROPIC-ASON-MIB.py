# SNMP MIB module (TROPIC-ASON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TROPIC-ASON-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:06:37 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(tnAsonMIB,
 tnSystemModules) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnAsonMIB",
    "tnSystemModules")

(AluWdmFecMode,
 AluWdmTransferProtocol,
 TnCommand) = mibBuilder.importSymbols(
    "TROPIC-TC",
    "AluWdmFecMode",
    "AluWdmTransferProtocol",
    "TnCommand")


# MODULE-IDENTITY

tnAsonMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 1, 10)
)
if mibBuilder.loadTexts:
    tnAsonMibModule.setRevisions(
        ("2010-10-12 12:00",
         "2011-03-04 12:00",
         "2011-05-05 12:00",
         "2011-05-31 12:00",
         "2011-06-30 12:00",
         "2011-07-25 12:00",
         "2011-08-03 12:00",
         "2011-08-08 12:00",
         "2011-08-12 12:00",
         "2012-01-17 12:00",
         "2012-01-24 12:00",
         "2012-06-25 12:00",
         "2012-08-10 12:00",
         "2012-10-22 12:00",
         "2012-11-05 12:00",
         "2013-09-20 12:00",
         "2013-11-18 12:00",
         "2013-11-22 12:00",
         "2014-02-26 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AluWdmAccessControlDevice(TextualConvention, Integer32):
    status = "current"
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
        *(("null", 1),
          ("cp", 2),
          ("mp", 3),
          ("cpMp", 4))
    )



# MIB Managed Objects in the order of their OIDs

_TnAsonConf_ObjectIdentity = ObjectIdentity
tnAsonConf = _TnAsonConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1)
)
_TnAsonGroups_ObjectIdentity = ObjectIdentity
tnAsonGroups = _TnAsonGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1)
)
_TnAsonCompliances_ObjectIdentity = ObjectIdentity
tnAsonCompliances = _TnAsonCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 2)
)
_TnAsonObjs_ObjectIdentity = ObjectIdentity
tnAsonObjs = _TnAsonObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2)
)
_TnAsonGlobal_ObjectIdentity = ObjectIdentity
tnAsonGlobal = _TnAsonGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 1)
)
_TnGmreNodeIpAddr_Type = IpAddress
_TnGmreNodeIpAddr_Object = MibScalar
tnGmreNodeIpAddr = _TnGmreNodeIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 1, 1),
    _TnGmreNodeIpAddr_Type()
)
tnGmreNodeIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreNodeIpAddr.setStatus("current")
_TnGmreNodeSubMask_Type = IpAddress
_TnGmreNodeSubMask_Object = MibScalar
tnGmreNodeSubMask = _TnGmreNodeSubMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 1, 2),
    _TnGmreNodeSubMask_Type()
)
tnGmreNodeSubMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreNodeSubMask.setStatus("current")
_TnGmreNotifyIpAddr_Type = IpAddress
_TnGmreNotifyIpAddr_Object = MibScalar
tnGmreNotifyIpAddr = _TnGmreNotifyIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 1, 3),
    _TnGmreNotifyIpAddr_Type()
)
tnGmreNotifyIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreNotifyIpAddr.setStatus("current")
_TnGmreNotifySubMask_Type = IpAddress
_TnGmreNotifySubMask_Object = MibScalar
tnGmreNotifySubMask = _TnGmreNotifySubMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 1, 4),
    _TnGmreNotifySubMask_Type()
)
tnGmreNotifySubMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreNotifySubMask.setStatus("current")
_TnAsonIorGlobal_ObjectIdentity = ObjectIdentity
tnAsonIorGlobal = _TnAsonIorGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 2)
)


class _TnGmreCorbaName_Type(SnmpAdminString):
    """Custom type tnGmreCorbaName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnGmreCorbaName_Type.__name__ = "SnmpAdminString"
_TnGmreCorbaName_Object = MibScalar
tnGmreCorbaName = _TnGmreCorbaName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 2, 1),
    _TnGmreCorbaName_Type()
)
tnGmreCorbaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmreCorbaName.setStatus("current")
_TnGmreCorbaHostIpAddress_Type = IpAddress
_TnGmreCorbaHostIpAddress_Object = MibScalar
tnGmreCorbaHostIpAddress = _TnGmreCorbaHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 2, 2),
    _TnGmreCorbaHostIpAddress_Type()
)
tnGmreCorbaHostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmreCorbaHostIpAddress.setStatus("current")


class _TnGmreCorbaIor_Type(SnmpAdminString):
    """Custom type tnGmreCorbaIor based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 265),
    )


_TnGmreCorbaIor_Type.__name__ = "SnmpAdminString"
_TnGmreCorbaIor_Object = MibScalar
tnGmreCorbaIor = _TnGmreCorbaIor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 2, 3),
    _TnGmreCorbaIor_Type()
)
tnGmreCorbaIor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmreCorbaIor.setStatus("current")
_TnAsonOmsLineImp_ObjectIdentity = ObjectIdentity
tnAsonOmsLineImp = _TnAsonOmsLineImp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 3)
)
_TnGmreOmsLineImpAttributeTotal_Type = Integer32
_TnGmreOmsLineImpAttributeTotal_Object = MibScalar
tnGmreOmsLineImpAttributeTotal = _TnGmreOmsLineImpAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 3, 1),
    _TnGmreOmsLineImpAttributeTotal_Type()
)
tnGmreOmsLineImpAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmreOmsLineImpAttributeTotal.setStatus("current")
_TnGmreOmsLineImpTable_Object = MibTable
tnGmreOmsLineImpTable = _TnGmreOmsLineImpTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 3, 2)
)
if mibBuilder.loadTexts:
    tnGmreOmsLineImpTable.setStatus("current")
_TnGmreOmsLineImpEntry_Object = MibTableRow
tnGmreOmsLineImpEntry = _TnGmreOmsLineImpEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 3, 2, 1)
)
tnGmreOmsLineImpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnGmreOmsLineImpEntry.setStatus("current")


class _TnGmreOmsLineImpMaxAlwCh_Type(Unsigned32):
    """Custom type tnGmreOmsLineImpMaxAlwCh based on Unsigned32"""
    defaultValue = 88

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_TnGmreOmsLineImpMaxAlwCh_Type.__name__ = "Unsigned32"
_TnGmreOmsLineImpMaxAlwCh_Object = MibTableColumn
tnGmreOmsLineImpMaxAlwCh = _TnGmreOmsLineImpMaxAlwCh_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 3, 2, 1, 1),
    _TnGmreOmsLineImpMaxAlwCh_Type()
)
tnGmreOmsLineImpMaxAlwCh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOmsLineImpMaxAlwCh.setStatus("current")


class _TnGmreOmsLineImpPMD_Type(Unsigned32):
    """Custom type tnGmreOmsLineImpPMD based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_TnGmreOmsLineImpPMD_Type.__name__ = "Unsigned32"
_TnGmreOmsLineImpPMD_Object = MibTableColumn
tnGmreOmsLineImpPMD = _TnGmreOmsLineImpPMD_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 3, 2, 1, 2),
    _TnGmreOmsLineImpPMD_Type()
)
tnGmreOmsLineImpPMD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOmsLineImpPMD.setStatus("current")
if mibBuilder.loadTexts:
    tnGmreOmsLineImpPMD.setUnits("1/10 picoSecond")


class _TnGmreOmsLineImpAlcMode_Type(Integer32):
    """Custom type tnGmreOmsLineImpAlcMode based on Integer32"""
    defaultValue = 1

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


_TnGmreOmsLineImpAlcMode_Type.__name__ = "Integer32"
_TnGmreOmsLineImpAlcMode_Object = MibTableColumn
tnGmreOmsLineImpAlcMode = _TnGmreOmsLineImpAlcMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 3, 2, 1, 3),
    _TnGmreOmsLineImpAlcMode_Type()
)
tnGmreOmsLineImpAlcMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOmsLineImpAlcMode.setStatus("current")


class _TnGmreOmsLineImpDcuFree_Type(Integer32):
    """Custom type tnGmreOmsLineImpDcuFree based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_TnGmreOmsLineImpDcuFree_Type.__name__ = "Integer32"
_TnGmreOmsLineImpDcuFree_Object = MibTableColumn
tnGmreOmsLineImpDcuFree = _TnGmreOmsLineImpDcuFree_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 3, 2, 1, 4),
    _TnGmreOmsLineImpDcuFree_Type()
)
tnGmreOmsLineImpDcuFree.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOmsLineImpDcuFree.setStatus("current")


class _TnGmreOmsLineImpCD_Type(Integer32):
    """Custom type tnGmreOmsLineImpCD based on Integer32"""
    defaultValue = 17000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40000, 78000),
    )


_TnGmreOmsLineImpCD_Type.__name__ = "Integer32"
_TnGmreOmsLineImpCD_Object = MibTableColumn
tnGmreOmsLineImpCD = _TnGmreOmsLineImpCD_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 3, 2, 1, 5),
    _TnGmreOmsLineImpCD_Type()
)
tnGmreOmsLineImpCD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOmsLineImpCD.setStatus("current")
if mibBuilder.loadTexts:
    tnGmreOmsLineImpCD.setUnits("1/10 ps/nm")


class _TnGmreOmsLineImpFiberType_Type(Integer32):
    """Custom type tnGmreOmsLineImpFiberType based on Integer32"""
    defaultValue = 1

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
        *(("ssmf", 1),
          ("eleaf", 2),
          ("twrs", 3),
          ("twc", 4),
          ("twp", 5),
          ("mixed", 6))
    )


_TnGmreOmsLineImpFiberType_Type.__name__ = "Integer32"
_TnGmreOmsLineImpFiberType_Object = MibTableColumn
tnGmreOmsLineImpFiberType = _TnGmreOmsLineImpFiberType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 3, 2, 1, 6),
    _TnGmreOmsLineImpFiberType_Type()
)
tnGmreOmsLineImpFiberType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOmsLineImpFiberType.setStatus("current")
_TnAsonOptLineImp_ObjectIdentity = ObjectIdentity
tnAsonOptLineImp = _TnAsonOptLineImp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 4)
)
_TnGmreOptLineImpAttributeTotal_Type = Integer32
_TnGmreOptLineImpAttributeTotal_Object = MibScalar
tnGmreOptLineImpAttributeTotal = _TnGmreOptLineImpAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 4, 1),
    _TnGmreOptLineImpAttributeTotal_Type()
)
tnGmreOptLineImpAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmreOptLineImpAttributeTotal.setStatus("current")
_TnGmreOptLineImpTable_Object = MibTable
tnGmreOptLineImpTable = _TnGmreOptLineImpTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 4, 2)
)
if mibBuilder.loadTexts:
    tnGmreOptLineImpTable.setStatus("current")
_TnGmreOptLineImpEntry_Object = MibTableRow
tnGmreOptLineImpEntry = _TnGmreOptLineImpEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 4, 2, 1)
)
tnGmreOptLineImpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-ASON-MIB", "tnGmreOptLineImpIndex"),
)
if mibBuilder.loadTexts:
    tnGmreOptLineImpEntry.setStatus("current")
_TnGmreOptLineImpIndex_Type = Unsigned32
_TnGmreOptLineImpIndex_Object = MibTableColumn
tnGmreOptLineImpIndex = _TnGmreOptLineImpIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 4, 2, 1, 1),
    _TnGmreOptLineImpIndex_Type()
)
tnGmreOptLineImpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGmreOptLineImpIndex.setStatus("current")


class _TnGmreOptLineImpBitRate_Type(Integer32):
    """Custom type tnGmreOptLineImpBitRate based on Integer32"""
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
        *(("rate2G5", 1),
          ("rate10G", 2),
          ("rate40G", 3),
          ("rate100G", 4),
          ("rate260G", 5))
    )


_TnGmreOptLineImpBitRate_Type.__name__ = "Integer32"
_TnGmreOptLineImpBitRate_Object = MibTableColumn
tnGmreOptLineImpBitRate = _TnGmreOptLineImpBitRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 4, 2, 1, 2),
    _TnGmreOptLineImpBitRate_Type()
)
tnGmreOptLineImpBitRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOptLineImpBitRate.setStatus("current")


class _TnGmreOptLineImpEncoding_Type(Integer32):
    """Custom type tnGmreOptLineImpEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("nrz", 1),
          ("pdpsk", 2),
          ("dpsk", 3),
          ("cohpmbpsk", 4),
          ("cohpmqpsk", 5),
          ("icohpmqpsk", 6),
          ("cohpm16qam", 7))
    )


_TnGmreOptLineImpEncoding_Type.__name__ = "Integer32"
_TnGmreOptLineImpEncoding_Object = MibTableColumn
tnGmreOptLineImpEncoding = _TnGmreOptLineImpEncoding_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 4, 2, 1, 3),
    _TnGmreOptLineImpEncoding_Type()
)
tnGmreOptLineImpEncoding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOptLineImpEncoding.setStatus("current")


class _TnGmreOptLineImpCompModule_Type(Integer32):
    """Custom type tnGmreOptLineImpCompModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("null", 1),
          ("pmdc", 2),
          ("mlse", 3),
          ("tdcm", 4),
          ("txfp", 5),
          ("hperf1", 6),
          ("variant1", 7),
          ("variant2", 8),
          ("variant3", 9),
          ("variant4", 10),
          ("variant5", 11),
          ("variant6", 12),
          ("variant7", 13),
          ("variant8", 14),
          ("variant9", 15),
          ("variant10", 16),
          ("tcfp", 17),
          ("cr", 18),
          ("ctxfpwt", 19),
          ("sperf2", 20),
          ("hperf2", 21))
    )


_TnGmreOptLineImpCompModule_Type.__name__ = "Integer32"
_TnGmreOptLineImpCompModule_Object = MibTableColumn
tnGmreOptLineImpCompModule = _TnGmreOptLineImpCompModule_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 4, 2, 1, 4),
    _TnGmreOptLineImpCompModule_Type()
)
tnGmreOptLineImpCompModule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOptLineImpCompModule.setStatus("current")
_TnGmreOptLineImpFecMode_Type = AluWdmFecMode
_TnGmreOptLineImpFecMode_Object = MibTableColumn
tnGmreOptLineImpFecMode = _TnGmreOptLineImpFecMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 4, 2, 1, 5),
    _TnGmreOptLineImpFecMode_Type()
)
tnGmreOptLineImpFecMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOptLineImpFecMode.setStatus("current")


class _TnGmreOptLineImpNLP_Type(Unsigned32):
    """Custom type tnGmreOptLineImpNLP based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_TnGmreOptLineImpNLP_Type.__name__ = "Unsigned32"
_TnGmreOptLineImpNLP_Object = MibTableColumn
tnGmreOptLineImpNLP = _TnGmreOptLineImpNLP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 4, 2, 1, 6),
    _TnGmreOptLineImpNLP_Type()
)
tnGmreOptLineImpNLP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOptLineImpNLP.setStatus("current")
if mibBuilder.loadTexts:
    tnGmreOptLineImpNLP.setUnits("percentage")


class _TnGmreOptLineImpOSNR_Type(Unsigned32):
    """Custom type tnGmreOptLineImpOSNR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_TnGmreOptLineImpOSNR_Type.__name__ = "Unsigned32"
_TnGmreOptLineImpOSNR_Object = MibTableColumn
tnGmreOptLineImpOSNR = _TnGmreOptLineImpOSNR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 4, 2, 1, 7),
    _TnGmreOptLineImpOSNR_Type()
)
tnGmreOptLineImpOSNR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOptLineImpOSNR.setStatus("current")


class _TnGmreOptLineImpNLPNP_Type(Unsigned32):
    """Custom type tnGmreOptLineImpNLPNP based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_TnGmreOptLineImpNLPNP_Type.__name__ = "Unsigned32"
_TnGmreOptLineImpNLPNP_Object = MibTableColumn
tnGmreOptLineImpNLPNP = _TnGmreOptLineImpNLPNP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 4, 2, 1, 8),
    _TnGmreOptLineImpNLPNP_Type()
)
tnGmreOptLineImpNLPNP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOptLineImpNLPNP.setStatus("current")
if mibBuilder.loadTexts:
    tnGmreOptLineImpNLPNP.setUnits("percentage")


class _TnGmreOptLineImpOSNRNP_Type(Unsigned32):
    """Custom type tnGmreOptLineImpOSNRNP based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_TnGmreOptLineImpOSNRNP_Type.__name__ = "Unsigned32"
_TnGmreOptLineImpOSNRNP_Object = MibTableColumn
tnGmreOptLineImpOSNRNP = _TnGmreOptLineImpOSNRNP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 4, 2, 1, 9),
    _TnGmreOptLineImpOSNRNP_Type()
)
tnGmreOptLineImpOSNRNP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOptLineImpOSNRNP.setStatus("current")
_TnGmreOptLineImpRowStatus_Type = RowStatus
_TnGmreOptLineImpRowStatus_Object = MibTableColumn
tnGmreOptLineImpRowStatus = _TnGmreOptLineImpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 4, 2, 1, 10),
    _TnGmreOptLineImpRowStatus_Type()
)
tnGmreOptLineImpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOptLineImpRowStatus.setStatus("current")


class _TnGmreOptLineImpPower_Type(Unsigned32):
    """Custom type tnGmreOptLineImpPower based on Unsigned32"""
    defaultValue = 790

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40500),
    )


_TnGmreOptLineImpPower_Type.__name__ = "Unsigned32"
_TnGmreOptLineImpPower_Object = MibTableColumn
tnGmreOptLineImpPower = _TnGmreOptLineImpPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 4, 2, 1, 11),
    _TnGmreOptLineImpPower_Type()
)
tnGmreOptLineImpPower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOptLineImpPower.setStatus("current")
if mibBuilder.loadTexts:
    tnGmreOptLineImpPower.setUnits("micro-Watts")
_TnAsonTopoAlarm_ObjectIdentity = ObjectIdentity
tnAsonTopoAlarm = _TnAsonTopoAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 5)
)
_TnAsonTopoAlarmAttributeTotal_Type = Integer32
_TnAsonTopoAlarmAttributeTotal_Object = MibScalar
tnAsonTopoAlarmAttributeTotal = _TnAsonTopoAlarmAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 5, 1),
    _TnAsonTopoAlarmAttributeTotal_Type()
)
tnAsonTopoAlarmAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAsonTopoAlarmAttributeTotal.setStatus("current")
_TnAsonTopoAlarmTable_Object = MibTable
tnAsonTopoAlarmTable = _TnAsonTopoAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 5, 2)
)
if mibBuilder.loadTexts:
    tnAsonTopoAlarmTable.setStatus("current")
_TnAsonTopoAlarmEntry_Object = MibTableRow
tnAsonTopoAlarmEntry = _TnAsonTopoAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 5, 2, 1)
)
tnAsonTopoAlarmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnAsonTopoAlarmEntry.setStatus("current")


class _TnAsonTopoClearAlarm_Type(TnCommand):
    """Custom type tnAsonTopoClearAlarm based on TnCommand"""
    defaultValue = 1


_TnAsonTopoClearAlarm_Type.__name__ = "TnCommand"
_TnAsonTopoClearAlarm_Object = MibTableColumn
tnAsonTopoClearAlarm = _TnAsonTopoClearAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 5, 2, 1, 1),
    _TnAsonTopoClearAlarm_Type()
)
tnAsonTopoClearAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAsonTopoClearAlarm.setStatus("current")
_TnAsonFeasibility_ObjectIdentity = ObjectIdentity
tnAsonFeasibility = _TnAsonFeasibility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 6)
)


class _TnAsonFeasibilityCommand_Type(Integer32):
    """Custom type tnAsonFeasibilityCommand based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noCmd", 1),
          ("transferFromRemote", 2))
    )


_TnAsonFeasibilityCommand_Type.__name__ = "Integer32"
_TnAsonFeasibilityCommand_Object = MibScalar
tnAsonFeasibilityCommand = _TnAsonFeasibilityCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 6, 1),
    _TnAsonFeasibilityCommand_Type()
)
tnAsonFeasibilityCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAsonFeasibilityCommand.setStatus("current")
_TnAsonFeasibilityRemoteHostIp_Type = IpAddress
_TnAsonFeasibilityRemoteHostIp_Object = MibScalar
tnAsonFeasibilityRemoteHostIp = _TnAsonFeasibilityRemoteHostIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 6, 2),
    _TnAsonFeasibilityRemoteHostIp_Type()
)
tnAsonFeasibilityRemoteHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAsonFeasibilityRemoteHostIp.setStatus("current")


class _TnAsonFeasibilityRemotePath_Type(SnmpAdminString):
    """Custom type tnAsonFeasibilityRemotePath based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnAsonFeasibilityRemotePath_Type.__name__ = "SnmpAdminString"
_TnAsonFeasibilityRemotePath_Object = MibScalar
tnAsonFeasibilityRemotePath = _TnAsonFeasibilityRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 6, 3),
    _TnAsonFeasibilityRemotePath_Type()
)
tnAsonFeasibilityRemotePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAsonFeasibilityRemotePath.setStatus("current")


class _TnAsonFeasibilityStatus_Type(SnmpAdminString):
    """Custom type tnAsonFeasibilityStatus based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnAsonFeasibilityStatus_Type.__name__ = "SnmpAdminString"
_TnAsonFeasibilityStatus_Object = MibScalar
tnAsonFeasibilityStatus = _TnAsonFeasibilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 6, 4),
    _TnAsonFeasibilityStatus_Type()
)
tnAsonFeasibilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAsonFeasibilityStatus.setStatus("current")


class _TnAsonFeasibilityLastTransferredVersion_Type(SnmpAdminString):
    """Custom type tnAsonFeasibilityLastTransferredVersion based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnAsonFeasibilityLastTransferredVersion_Type.__name__ = "SnmpAdminString"
_TnAsonFeasibilityLastTransferredVersion_Object = MibScalar
tnAsonFeasibilityLastTransferredVersion = _TnAsonFeasibilityLastTransferredVersion_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 6, 5),
    _TnAsonFeasibilityLastTransferredVersion_Type()
)
tnAsonFeasibilityLastTransferredVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAsonFeasibilityLastTransferredVersion.setStatus("current")


class _TnAsonFeasibilityProtocol_Type(AluWdmTransferProtocol):
    """Custom type tnAsonFeasibilityProtocol based on AluWdmTransferProtocol"""
    defaultValue = 3


_TnAsonFeasibilityProtocol_Type.__name__ = "AluWdmTransferProtocol"
_TnAsonFeasibilityProtocol_Object = MibScalar
tnAsonFeasibilityProtocol = _TnAsonFeasibilityProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 6, 6),
    _TnAsonFeasibilityProtocol_Type()
)
tnAsonFeasibilityProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAsonFeasibilityProtocol.setStatus("current")


class _TnAsonFeasibilityUserId_Type(SnmpAdminString):
    """Custom type tnAsonFeasibilityUserId based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnAsonFeasibilityUserId_Type.__name__ = "SnmpAdminString"
_TnAsonFeasibilityUserId_Object = MibScalar
tnAsonFeasibilityUserId = _TnAsonFeasibilityUserId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 6, 7),
    _TnAsonFeasibilityUserId_Type()
)
tnAsonFeasibilityUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAsonFeasibilityUserId.setStatus("current")


class _TnAsonFeasibilityPassword_Type(SnmpAdminString):
    """Custom type tnAsonFeasibilityPassword based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnAsonFeasibilityPassword_Type.__name__ = "SnmpAdminString"
_TnAsonFeasibilityPassword_Object = MibScalar
tnAsonFeasibilityPassword = _TnAsonFeasibilityPassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 6, 8),
    _TnAsonFeasibilityPassword_Type()
)
tnAsonFeasibilityPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAsonFeasibilityPassword.setStatus("current")
_TnAsonMgracdInfo_ObjectIdentity = ObjectIdentity
tnAsonMgracdInfo = _TnAsonMgracdInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 7)
)
_TnAsonMgracdAttributeTotal_Type = Integer32
_TnAsonMgracdAttributeTotal_Object = MibScalar
tnAsonMgracdAttributeTotal = _TnAsonMgracdAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 7, 1),
    _TnAsonMgracdAttributeTotal_Type()
)
tnAsonMgracdAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAsonMgracdAttributeTotal.setStatus("current")
_TnAsonMgracdTable_Object = MibTable
tnAsonMgracdTable = _TnAsonMgracdTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 7, 2)
)
if mibBuilder.loadTexts:
    tnAsonMgracdTable.setStatus("current")
_TnAsonMgracdEntry_Object = MibTableRow
tnAsonMgracdEntry = _TnAsonMgracdEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 7, 2, 1)
)
tnAsonMgracdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnAsonMgracdEntry.setStatus("current")


class _TnAsonOchMgracd_Type(AluWdmAccessControlDevice):
    """Custom type tnAsonOchMgracd based on AluWdmAccessControlDevice"""
    defaultValue = 1


_TnAsonOchMgracd_Type.__name__ = "AluWdmAccessControlDevice"
_TnAsonOchMgracd_Object = MibTableColumn
tnAsonOchMgracd = _TnAsonOchMgracd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 7, 2, 1, 1),
    _TnAsonOchMgracd_Type()
)
tnAsonOchMgracd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAsonOchMgracd.setStatus("current")


class _TnAsonOmsochifMgracd_Type(AluWdmAccessControlDevice):
    """Custom type tnAsonOmsochifMgracd based on AluWdmAccessControlDevice"""
    defaultValue = 1


_TnAsonOmsochifMgracd_Type.__name__ = "AluWdmAccessControlDevice"
_TnAsonOmsochifMgracd_Object = MibTableColumn
tnAsonOmsochifMgracd = _TnAsonOmsochifMgracd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 7, 2, 1, 2),
    _TnAsonOmsochifMgracd_Type()
)
tnAsonOmsochifMgracd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAsonOmsochifMgracd.setStatus("current")


class _TnAsonOtsMgracd_Type(AluWdmAccessControlDevice):
    """Custom type tnAsonOtsMgracd based on AluWdmAccessControlDevice"""
    defaultValue = 1


_TnAsonOtsMgracd_Type.__name__ = "AluWdmAccessControlDevice"
_TnAsonOtsMgracd_Object = MibTableColumn
tnAsonOtsMgracd = _TnAsonOtsMgracd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 7, 2, 1, 3),
    _TnAsonOtsMgracd_Type()
)
tnAsonOtsMgracd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAsonOtsMgracd.setStatus("current")
_TnAsonOmsWavelengthSet_ObjectIdentity = ObjectIdentity
tnAsonOmsWavelengthSet = _TnAsonOmsWavelengthSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 8)
)
_TnGmreOmsWavelengthSetAttributeTotal_Type = Integer32
_TnGmreOmsWavelengthSetAttributeTotal_Object = MibScalar
tnGmreOmsWavelengthSetAttributeTotal = _TnGmreOmsWavelengthSetAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 8, 1),
    _TnGmreOmsWavelengthSetAttributeTotal_Type()
)
tnGmreOmsWavelengthSetAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmreOmsWavelengthSetAttributeTotal.setStatus("current")
_TnGmreOmsWavelengthSetTable_Object = MibTable
tnGmreOmsWavelengthSetTable = _TnGmreOmsWavelengthSetTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 8, 2)
)
if mibBuilder.loadTexts:
    tnGmreOmsWavelengthSetTable.setStatus("current")
_TnGmreOmsWavelengthSetEntry_Object = MibTableRow
tnGmreOmsWavelengthSetEntry = _TnGmreOmsWavelengthSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 8, 2, 1)
)
tnGmreOmsWavelengthSetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-ASON-MIB", "tnGmreOmsWavelengthEncodingType"),
)
if mibBuilder.loadTexts:
    tnGmreOmsWavelengthSetEntry.setStatus("current")


class _TnGmreOmsWavelengthEncodingType_Type(Integer32):
    """Custom type tnGmreOmsWavelengthEncodingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nrz", 1),
          ("pdpsk", 2),
          ("coherent", 3))
    )


_TnGmreOmsWavelengthEncodingType_Type.__name__ = "Integer32"
_TnGmreOmsWavelengthEncodingType_Object = MibTableColumn
tnGmreOmsWavelengthEncodingType = _TnGmreOmsWavelengthEncodingType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 8, 2, 1, 1),
    _TnGmreOmsWavelengthEncodingType_Type()
)
tnGmreOmsWavelengthEncodingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGmreOmsWavelengthEncodingType.setStatus("current")


class _TnGmreOmsWavelengthEncodingBitMap_Type(OctetString):
    """Custom type tnGmreOmsWavelengthEncodingBitMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TnGmreOmsWavelengthEncodingBitMap_Type.__name__ = "OctetString"
_TnGmreOmsWavelengthEncodingBitMap_Object = MibTableColumn
tnGmreOmsWavelengthEncodingBitMap = _TnGmreOmsWavelengthEncodingBitMap_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 8, 2, 1, 2),
    _TnGmreOmsWavelengthEncodingBitMap_Type()
)
tnGmreOmsWavelengthEncodingBitMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOmsWavelengthEncodingBitMap.setStatus("current")
_TnAsonSnapshot_ObjectIdentity = ObjectIdentity
tnAsonSnapshot = _TnAsonSnapshot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 9)
)
_TnAsonSnapshotRemoteHostIp_Type = IpAddress
_TnAsonSnapshotRemoteHostIp_Object = MibScalar
tnAsonSnapshotRemoteHostIp = _TnAsonSnapshotRemoteHostIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 9, 1),
    _TnAsonSnapshotRemoteHostIp_Type()
)
tnAsonSnapshotRemoteHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAsonSnapshotRemoteHostIp.setStatus("current")
_TnAsonSnapshotProtocol_Type = AluWdmTransferProtocol
_TnAsonSnapshotProtocol_Object = MibScalar
tnAsonSnapshotProtocol = _TnAsonSnapshotProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 9, 2),
    _TnAsonSnapshotProtocol_Type()
)
tnAsonSnapshotProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAsonSnapshotProtocol.setStatus("current")
_TnAsonSnapshotUserId_Type = SnmpAdminString
_TnAsonSnapshotUserId_Object = MibScalar
tnAsonSnapshotUserId = _TnAsonSnapshotUserId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 9, 3),
    _TnAsonSnapshotUserId_Type()
)
tnAsonSnapshotUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAsonSnapshotUserId.setStatus("current")
_TnAsonSnapshotPassword_Type = SnmpAdminString
_TnAsonSnapshotPassword_Object = MibScalar
tnAsonSnapshotPassword = _TnAsonSnapshotPassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 9, 4),
    _TnAsonSnapshotPassword_Type()
)
tnAsonSnapshotPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAsonSnapshotPassword.setStatus("current")


class _TnAsonSnapshotRootRemotePath_Type(SnmpAdminString):
    """Custom type tnAsonSnapshotRootRemotePath based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnAsonSnapshotRootRemotePath_Type.__name__ = "SnmpAdminString"
_TnAsonSnapshotRootRemotePath_Object = MibScalar
tnAsonSnapshotRootRemotePath = _TnAsonSnapshotRootRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 9, 5),
    _TnAsonSnapshotRootRemotePath_Type()
)
tnAsonSnapshotRootRemotePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAsonSnapshotRootRemotePath.setStatus("current")
_TnAsonSnapshotAttributeTotal_Type = Integer32
_TnAsonSnapshotAttributeTotal_Object = MibScalar
tnAsonSnapshotAttributeTotal = _TnAsonSnapshotAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 9, 6),
    _TnAsonSnapshotAttributeTotal_Type()
)
tnAsonSnapshotAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAsonSnapshotAttributeTotal.setStatus("current")
_TnAsonSnapshotTable_Object = MibTable
tnAsonSnapshotTable = _TnAsonSnapshotTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 9, 7)
)
if mibBuilder.loadTexts:
    tnAsonSnapshotTable.setStatus("current")
_TnAsonSnapshotEntry_Object = MibTableRow
tnAsonSnapshotEntry = _TnAsonSnapshotEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 9, 7, 1)
)
tnAsonSnapshotEntry.setIndexNames(
    (0, "TROPIC-ASON-MIB", "tnAsonSnapshotTime"),
)
if mibBuilder.loadTexts:
    tnAsonSnapshotEntry.setStatus("current")
_TnAsonSnapshotTime_Type = Unsigned32
_TnAsonSnapshotTime_Object = MibTableColumn
tnAsonSnapshotTime = _TnAsonSnapshotTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 9, 7, 1, 1),
    _TnAsonSnapshotTime_Type()
)
tnAsonSnapshotTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnAsonSnapshotTime.setStatus("current")


class _TnAsonSnapshotStatus_Type(SnmpAdminString):
    """Custom type tnAsonSnapshotStatus based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnAsonSnapshotStatus_Type.__name__ = "SnmpAdminString"
_TnAsonSnapshotStatus_Object = MibTableColumn
tnAsonSnapshotStatus = _TnAsonSnapshotStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 9, 7, 1, 2),
    _TnAsonSnapshotStatus_Type()
)
tnAsonSnapshotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAsonSnapshotStatus.setStatus("current")


class _TnAsonSnapshotRemotePath_Type(SnmpAdminString):
    """Custom type tnAsonSnapshotRemotePath based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnAsonSnapshotRemotePath_Type.__name__ = "SnmpAdminString"
_TnAsonSnapshotRemotePath_Object = MibTableColumn
tnAsonSnapshotRemotePath = _TnAsonSnapshotRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 9, 7, 1, 3),
    _TnAsonSnapshotRemotePath_Type()
)
tnAsonSnapshotRemotePath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAsonSnapshotRemotePath.setStatus("current")
_TnAsonSnapshotRowStatus_Type = RowStatus
_TnAsonSnapshotRowStatus_Object = MibTableColumn
tnAsonSnapshotRowStatus = _TnAsonSnapshotRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 9, 7, 1, 4),
    _TnAsonSnapshotRowStatus_Type()
)
tnAsonSnapshotRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAsonSnapshotRowStatus.setStatus("current")


class _TnAsonSnapshotFilename_Type(SnmpAdminString):
    """Custom type tnAsonSnapshotFilename based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnAsonSnapshotFilename_Type.__name__ = "SnmpAdminString"
_TnAsonSnapshotFilename_Object = MibTableColumn
tnAsonSnapshotFilename = _TnAsonSnapshotFilename_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 9, 7, 1, 5),
    _TnAsonSnapshotFilename_Type()
)
tnAsonSnapshotFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAsonSnapshotFilename.setStatus("current")

# Managed Objects groups

tnAsonGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 1)
)
tnAsonGlobalGroup.setObjects(
      *(("TROPIC-ASON-MIB", "tnGmreNodeIpAddr"),
        ("TROPIC-ASON-MIB", "tnGmreNodeSubMask"),
        ("TROPIC-ASON-MIB", "tnGmreNotifyIpAddr"),
        ("TROPIC-ASON-MIB", "tnGmreNotifySubMask"))
)
if mibBuilder.loadTexts:
    tnAsonGlobalGroup.setStatus("current")

tnAsonIorGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 2)
)
tnAsonIorGlobalGroup.setObjects(
      *(("TROPIC-ASON-MIB", "tnGmreCorbaName"),
        ("TROPIC-ASON-MIB", "tnGmreCorbaHostIpAddress"),
        ("TROPIC-ASON-MIB", "tnGmreCorbaIor"))
)
if mibBuilder.loadTexts:
    tnAsonIorGlobalGroup.setStatus("current")

tnAsonOmsLineImpScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 3)
)
tnAsonOmsLineImpScalarsGroup.setObjects(
    ("TROPIC-ASON-MIB", "tnGmreOmsLineImpAttributeTotal")
)
if mibBuilder.loadTexts:
    tnAsonOmsLineImpScalarsGroup.setStatus("current")

tnAsonOmsLineImpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 4)
)
tnAsonOmsLineImpGroup.setObjects(
      *(("TROPIC-ASON-MIB", "tnGmreOmsLineImpMaxAlwCh"),
        ("TROPIC-ASON-MIB", "tnGmreOmsLineImpPMD"),
        ("TROPIC-ASON-MIB", "tnGmreOmsLineImpAlcMode"),
        ("TROPIC-ASON-MIB", "tnGmreOmsLineImpDcuFree"),
        ("TROPIC-ASON-MIB", "tnGmreOmsLineImpCD"),
        ("TROPIC-ASON-MIB", "tnGmreOmsLineImpFiberType"))
)
if mibBuilder.loadTexts:
    tnAsonOmsLineImpGroup.setStatus("current")

tnAsonOptLineImpScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 5)
)
tnAsonOptLineImpScalarsGroup.setObjects(
    ("TROPIC-ASON-MIB", "tnGmreOptLineImpAttributeTotal")
)
if mibBuilder.loadTexts:
    tnAsonOptLineImpScalarsGroup.setStatus("current")

tnAsonOptLineImpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 6)
)
tnAsonOptLineImpGroup.setObjects(
      *(("TROPIC-ASON-MIB", "tnGmreOptLineImpBitRate"),
        ("TROPIC-ASON-MIB", "tnGmreOptLineImpEncoding"),
        ("TROPIC-ASON-MIB", "tnGmreOptLineImpCompModule"),
        ("TROPIC-ASON-MIB", "tnGmreOptLineImpFecMode"),
        ("TROPIC-ASON-MIB", "tnGmreOptLineImpNLP"),
        ("TROPIC-ASON-MIB", "tnGmreOptLineImpOSNR"),
        ("TROPIC-ASON-MIB", "tnGmreOptLineImpNLPNP"),
        ("TROPIC-ASON-MIB", "tnGmreOptLineImpOSNRNP"),
        ("TROPIC-ASON-MIB", "tnGmreOptLineImpRowStatus"),
        ("TROPIC-ASON-MIB", "tnGmreOptLineImpPower"))
)
if mibBuilder.loadTexts:
    tnAsonOptLineImpGroup.setStatus("current")

tnAsonTopoAlarmScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 7)
)
tnAsonTopoAlarmScalarsGroup.setObjects(
    ("TROPIC-ASON-MIB", "tnAsonTopoAlarmAttributeTotal")
)
if mibBuilder.loadTexts:
    tnAsonTopoAlarmScalarsGroup.setStatus("current")

tnAsonTopoAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 8)
)
tnAsonTopoAlarmGroup.setObjects(
    ("TROPIC-ASON-MIB", "tnAsonTopoClearAlarm")
)
if mibBuilder.loadTexts:
    tnAsonTopoAlarmGroup.setStatus("current")

tnAsonFeasibilityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 9)
)
tnAsonFeasibilityGroup.setObjects(
      *(("TROPIC-ASON-MIB", "tnAsonFeasibilityCommand"),
        ("TROPIC-ASON-MIB", "tnAsonFeasibilityRemoteHostIp"),
        ("TROPIC-ASON-MIB", "tnAsonFeasibilityRemotePath"),
        ("TROPIC-ASON-MIB", "tnAsonFeasibilityStatus"),
        ("TROPIC-ASON-MIB", "tnAsonFeasibilityLastTransferredVersion"),
        ("TROPIC-ASON-MIB", "tnAsonFeasibilityProtocol"),
        ("TROPIC-ASON-MIB", "tnAsonFeasibilityUserId"),
        ("TROPIC-ASON-MIB", "tnAsonFeasibilityPassword"))
)
if mibBuilder.loadTexts:
    tnAsonFeasibilityGroup.setStatus("current")

tnAsonMgracdScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 10)
)
tnAsonMgracdScalarsGroup.setObjects(
    ("TROPIC-ASON-MIB", "tnAsonMgracdAttributeTotal")
)
if mibBuilder.loadTexts:
    tnAsonMgracdScalarsGroup.setStatus("current")

tnAsonMgracdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 11)
)
tnAsonMgracdGroup.setObjects(
      *(("TROPIC-ASON-MIB", "tnAsonOchMgracd"),
        ("TROPIC-ASON-MIB", "tnAsonOmsochifMgracd"),
        ("TROPIC-ASON-MIB", "tnAsonOtsMgracd"))
)
if mibBuilder.loadTexts:
    tnAsonMgracdGroup.setStatus("current")

tnAsonOmsWavelengthSetScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 12)
)
tnAsonOmsWavelengthSetScalarsGroup.setObjects(
    ("TROPIC-ASON-MIB", "tnGmreOmsWavelengthSetAttributeTotal")
)
if mibBuilder.loadTexts:
    tnAsonOmsWavelengthSetScalarsGroup.setStatus("current")

tnAsonOmsWavelengthSetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 13)
)
tnAsonOmsWavelengthSetGroup.setObjects(
    ("TROPIC-ASON-MIB", "tnGmreOmsWavelengthEncodingBitMap")
)
if mibBuilder.loadTexts:
    tnAsonOmsWavelengthSetGroup.setStatus("current")

tnAsonSnapshotScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 14)
)
tnAsonSnapshotScalarsGroup.setObjects(
      *(("TROPIC-ASON-MIB", "tnAsonSnapshotRemoteHostIp"),
        ("TROPIC-ASON-MIB", "tnAsonSnapshotProtocol"),
        ("TROPIC-ASON-MIB", "tnAsonSnapshotUserId"),
        ("TROPIC-ASON-MIB", "tnAsonSnapshotPassword"),
        ("TROPIC-ASON-MIB", "tnAsonSnapshotRootRemotePath"),
        ("TROPIC-ASON-MIB", "tnAsonSnapshotAttributeTotal"))
)
if mibBuilder.loadTexts:
    tnAsonSnapshotScalarsGroup.setStatus("current")

tnAsonSnapshotGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 15)
)
tnAsonSnapshotGroup.setObjects(
      *(("TROPIC-ASON-MIB", "tnAsonSnapshotStatus"),
        ("TROPIC-ASON-MIB", "tnAsonSnapshotRemotePath"),
        ("TROPIC-ASON-MIB", "tnAsonSnapshotRowStatus"),
        ("TROPIC-ASON-MIB", "tnAsonSnapshotFilename"))
)
if mibBuilder.loadTexts:
    tnAsonSnapshotGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnAsonCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 2, 1)
)
tnAsonCompliance.setObjects(
      *(("TROPIC-ASON-MIB", "tnAsonGlobalGroup"),
        ("TROPIC-ASON-MIB", "tnAsonIorGlobalGroup"),
        ("TROPIC-ASON-MIB", "tnAsonOmsLineImpScalarsGroup"),
        ("TROPIC-ASON-MIB", "tnAsonOmsLineImpGroup"),
        ("TROPIC-ASON-MIB", "tnAsonOptLineImpScalarsGroup"),
        ("TROPIC-ASON-MIB", "tnAsonOptLineImpGroup"),
        ("TROPIC-ASON-MIB", "tnAsonTopoAlarmScalarsGroup"),
        ("TROPIC-ASON-MIB", "tnAsonTopoAlarmGroup"),
        ("TROPIC-ASON-MIB", "tnAsonFeasibilityGroup"),
        ("TROPIC-ASON-MIB", "tnAsonMgracdScalarsGroup"),
        ("TROPIC-ASON-MIB", "tnAsonMgracdGroup"),
        ("TROPIC-ASON-MIB", "tnAsonOmsWavelengthSetScalarsGroup"),
        ("TROPIC-ASON-MIB", "tnAsonOmsWavelengthSetGroup"),
        ("TROPIC-ASON-MIB", "tnAsonSnapshotScalarsGroup"),
        ("TROPIC-ASON-MIB", "tnAsonSnapshotGroup"))
)
if mibBuilder.loadTexts:
    tnAsonCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-ASON-MIB",
    **{"AluWdmAccessControlDevice": AluWdmAccessControlDevice,
       "tnAsonMibModule": tnAsonMibModule,
       "tnAsonConf": tnAsonConf,
       "tnAsonGroups": tnAsonGroups,
       "tnAsonGlobalGroup": tnAsonGlobalGroup,
       "tnAsonIorGlobalGroup": tnAsonIorGlobalGroup,
       "tnAsonOmsLineImpScalarsGroup": tnAsonOmsLineImpScalarsGroup,
       "tnAsonOmsLineImpGroup": tnAsonOmsLineImpGroup,
       "tnAsonOptLineImpScalarsGroup": tnAsonOptLineImpScalarsGroup,
       "tnAsonOptLineImpGroup": tnAsonOptLineImpGroup,
       "tnAsonTopoAlarmScalarsGroup": tnAsonTopoAlarmScalarsGroup,
       "tnAsonTopoAlarmGroup": tnAsonTopoAlarmGroup,
       "tnAsonFeasibilityGroup": tnAsonFeasibilityGroup,
       "tnAsonMgracdScalarsGroup": tnAsonMgracdScalarsGroup,
       "tnAsonMgracdGroup": tnAsonMgracdGroup,
       "tnAsonOmsWavelengthSetScalarsGroup": tnAsonOmsWavelengthSetScalarsGroup,
       "tnAsonOmsWavelengthSetGroup": tnAsonOmsWavelengthSetGroup,
       "tnAsonSnapshotScalarsGroup": tnAsonSnapshotScalarsGroup,
       "tnAsonSnapshotGroup": tnAsonSnapshotGroup,
       "tnAsonCompliances": tnAsonCompliances,
       "tnAsonCompliance": tnAsonCompliance,
       "tnAsonObjs": tnAsonObjs,
       "tnAsonGlobal": tnAsonGlobal,
       "tnGmreNodeIpAddr": tnGmreNodeIpAddr,
       "tnGmreNodeSubMask": tnGmreNodeSubMask,
       "tnGmreNotifyIpAddr": tnGmreNotifyIpAddr,
       "tnGmreNotifySubMask": tnGmreNotifySubMask,
       "tnAsonIorGlobal": tnAsonIorGlobal,
       "tnGmreCorbaName": tnGmreCorbaName,
       "tnGmreCorbaHostIpAddress": tnGmreCorbaHostIpAddress,
       "tnGmreCorbaIor": tnGmreCorbaIor,
       "tnAsonOmsLineImp": tnAsonOmsLineImp,
       "tnGmreOmsLineImpAttributeTotal": tnGmreOmsLineImpAttributeTotal,
       "tnGmreOmsLineImpTable": tnGmreOmsLineImpTable,
       "tnGmreOmsLineImpEntry": tnGmreOmsLineImpEntry,
       "tnGmreOmsLineImpMaxAlwCh": tnGmreOmsLineImpMaxAlwCh,
       "tnGmreOmsLineImpPMD": tnGmreOmsLineImpPMD,
       "tnGmreOmsLineImpAlcMode": tnGmreOmsLineImpAlcMode,
       "tnGmreOmsLineImpDcuFree": tnGmreOmsLineImpDcuFree,
       "tnGmreOmsLineImpCD": tnGmreOmsLineImpCD,
       "tnGmreOmsLineImpFiberType": tnGmreOmsLineImpFiberType,
       "tnAsonOptLineImp": tnAsonOptLineImp,
       "tnGmreOptLineImpAttributeTotal": tnGmreOptLineImpAttributeTotal,
       "tnGmreOptLineImpTable": tnGmreOptLineImpTable,
       "tnGmreOptLineImpEntry": tnGmreOptLineImpEntry,
       "tnGmreOptLineImpIndex": tnGmreOptLineImpIndex,
       "tnGmreOptLineImpBitRate": tnGmreOptLineImpBitRate,
       "tnGmreOptLineImpEncoding": tnGmreOptLineImpEncoding,
       "tnGmreOptLineImpCompModule": tnGmreOptLineImpCompModule,
       "tnGmreOptLineImpFecMode": tnGmreOptLineImpFecMode,
       "tnGmreOptLineImpNLP": tnGmreOptLineImpNLP,
       "tnGmreOptLineImpOSNR": tnGmreOptLineImpOSNR,
       "tnGmreOptLineImpNLPNP": tnGmreOptLineImpNLPNP,
       "tnGmreOptLineImpOSNRNP": tnGmreOptLineImpOSNRNP,
       "tnGmreOptLineImpRowStatus": tnGmreOptLineImpRowStatus,
       "tnGmreOptLineImpPower": tnGmreOptLineImpPower,
       "tnAsonTopoAlarm": tnAsonTopoAlarm,
       "tnAsonTopoAlarmAttributeTotal": tnAsonTopoAlarmAttributeTotal,
       "tnAsonTopoAlarmTable": tnAsonTopoAlarmTable,
       "tnAsonTopoAlarmEntry": tnAsonTopoAlarmEntry,
       "tnAsonTopoClearAlarm": tnAsonTopoClearAlarm,
       "tnAsonFeasibility": tnAsonFeasibility,
       "tnAsonFeasibilityCommand": tnAsonFeasibilityCommand,
       "tnAsonFeasibilityRemoteHostIp": tnAsonFeasibilityRemoteHostIp,
       "tnAsonFeasibilityRemotePath": tnAsonFeasibilityRemotePath,
       "tnAsonFeasibilityStatus": tnAsonFeasibilityStatus,
       "tnAsonFeasibilityLastTransferredVersion": tnAsonFeasibilityLastTransferredVersion,
       "tnAsonFeasibilityProtocol": tnAsonFeasibilityProtocol,
       "tnAsonFeasibilityUserId": tnAsonFeasibilityUserId,
       "tnAsonFeasibilityPassword": tnAsonFeasibilityPassword,
       "tnAsonMgracdInfo": tnAsonMgracdInfo,
       "tnAsonMgracdAttributeTotal": tnAsonMgracdAttributeTotal,
       "tnAsonMgracdTable": tnAsonMgracdTable,
       "tnAsonMgracdEntry": tnAsonMgracdEntry,
       "tnAsonOchMgracd": tnAsonOchMgracd,
       "tnAsonOmsochifMgracd": tnAsonOmsochifMgracd,
       "tnAsonOtsMgracd": tnAsonOtsMgracd,
       "tnAsonOmsWavelengthSet": tnAsonOmsWavelengthSet,
       "tnGmreOmsWavelengthSetAttributeTotal": tnGmreOmsWavelengthSetAttributeTotal,
       "tnGmreOmsWavelengthSetTable": tnGmreOmsWavelengthSetTable,
       "tnGmreOmsWavelengthSetEntry": tnGmreOmsWavelengthSetEntry,
       "tnGmreOmsWavelengthEncodingType": tnGmreOmsWavelengthEncodingType,
       "tnGmreOmsWavelengthEncodingBitMap": tnGmreOmsWavelengthEncodingBitMap,
       "tnAsonSnapshot": tnAsonSnapshot,
       "tnAsonSnapshotRemoteHostIp": tnAsonSnapshotRemoteHostIp,
       "tnAsonSnapshotProtocol": tnAsonSnapshotProtocol,
       "tnAsonSnapshotUserId": tnAsonSnapshotUserId,
       "tnAsonSnapshotPassword": tnAsonSnapshotPassword,
       "tnAsonSnapshotRootRemotePath": tnAsonSnapshotRootRemotePath,
       "tnAsonSnapshotAttributeTotal": tnAsonSnapshotAttributeTotal,
       "tnAsonSnapshotTable": tnAsonSnapshotTable,
       "tnAsonSnapshotEntry": tnAsonSnapshotEntry,
       "tnAsonSnapshotTime": tnAsonSnapshotTime,
       "tnAsonSnapshotStatus": tnAsonSnapshotStatus,
       "tnAsonSnapshotRemotePath": tnAsonSnapshotRemotePath,
       "tnAsonSnapshotRowStatus": tnAsonSnapshotRowStatus,
       "tnAsonSnapshotFilename": tnAsonSnapshotFilename}
)
