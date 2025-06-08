# SNMP MIB module (MPLS-OAM-ID-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/MPLS-OAM-ID-STD-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 14:44:43 2025
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

(IndexIntegerNextFree,) = mibBuilder.importSymbols(
    "DIFFSERV-MIB",
    "IndexIntegerNextFree")

(InterfaceIndexOrZero,
 ifCounterDiscontinuityGroup,
 ifGeneralInformationGroup) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifCounterDiscontinuityGroup",
    "ifGeneralInformationGroup")

(mplsStdMIB,) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "mplsStdMIB")

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
 RowPointer,
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

mplsOamIdStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 21)
)
if mibBuilder.loadTexts:
    mplsOamIdStdMIB.setRevisions(
        ("2016-01-07 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MplsOamIdNotifications_ObjectIdentity = ObjectIdentity
mplsOamIdNotifications = _MplsOamIdNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 0)
)
_MplsOamIdObjects_ObjectIdentity = ObjectIdentity
mplsOamIdObjects = _MplsOamIdObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 1)
)


class _MplsOamIdMegIndexNext_Type(IndexIntegerNextFree):
    """Custom type mplsOamIdMegIndexNext based on IndexIntegerNextFree"""
    subtypeSpec = IndexIntegerNextFree.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MplsOamIdMegIndexNext_Type.__name__ = "IndexIntegerNextFree"
_MplsOamIdMegIndexNext_Object = MibScalar
mplsOamIdMegIndexNext = _MplsOamIdMegIndexNext_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 1, 1),
    _MplsOamIdMegIndexNext_Type()
)
mplsOamIdMegIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOamIdMegIndexNext.setStatus("current")
_MplsOamIdMegTable_Object = MibTable
mplsOamIdMegTable = _MplsOamIdMegTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 1, 2)
)
if mibBuilder.loadTexts:
    mplsOamIdMegTable.setStatus("current")
_MplsOamIdMegEntry_Object = MibTableRow
mplsOamIdMegEntry = _MplsOamIdMegEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 1, 2, 1)
)
mplsOamIdMegEntry.setIndexNames(
    (0, "MPLS-OAM-ID-STD-MIB", "mplsOamIdMegIndex"),
)
if mibBuilder.loadTexts:
    mplsOamIdMegEntry.setStatus("current")


class _MplsOamIdMegIndex_Type(Unsigned32):
    """Custom type mplsOamIdMegIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MplsOamIdMegIndex_Type.__name__ = "Unsigned32"
_MplsOamIdMegIndex_Object = MibTableColumn
mplsOamIdMegIndex = _MplsOamIdMegIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 1, 2, 1, 1),
    _MplsOamIdMegIndex_Type()
)
mplsOamIdMegIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsOamIdMegIndex.setStatus("current")


class _MplsOamIdMegName_Type(SnmpAdminString):
    """Custom type mplsOamIdMegName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_MplsOamIdMegName_Type.__name__ = "SnmpAdminString"
_MplsOamIdMegName_Object = MibTableColumn
mplsOamIdMegName = _MplsOamIdMegName_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 1, 2, 1, 2),
    _MplsOamIdMegName_Type()
)
mplsOamIdMegName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOamIdMegName.setStatus("current")


class _MplsOamIdMegOperatorType_Type(Integer32):
    """Custom type mplsOamIdMegOperatorType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipCompatible", 1),
          ("iccBased", 2))
    )


_MplsOamIdMegOperatorType_Type.__name__ = "Integer32"
_MplsOamIdMegOperatorType_Object = MibTableColumn
mplsOamIdMegOperatorType = _MplsOamIdMegOperatorType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 1, 2, 1, 3),
    _MplsOamIdMegOperatorType_Type()
)
mplsOamIdMegOperatorType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOamIdMegOperatorType.setStatus("current")


class _MplsOamIdMegIdCc_Type(SnmpAdminString):
    """Custom type mplsOamIdMegIdCc based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_MplsOamIdMegIdCc_Type.__name__ = "SnmpAdminString"
_MplsOamIdMegIdCc_Object = MibTableColumn
mplsOamIdMegIdCc = _MplsOamIdMegIdCc_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 1, 2, 1, 4),
    _MplsOamIdMegIdCc_Type()
)
mplsOamIdMegIdCc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOamIdMegIdCc.setStatus("current")


class _MplsOamIdMegIdIcc_Type(SnmpAdminString):
    """Custom type mplsOamIdMegIdIcc based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_MplsOamIdMegIdIcc_Type.__name__ = "SnmpAdminString"
_MplsOamIdMegIdIcc_Object = MibTableColumn
mplsOamIdMegIdIcc = _MplsOamIdMegIdIcc_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 1, 2, 1, 5),
    _MplsOamIdMegIdIcc_Type()
)
mplsOamIdMegIdIcc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOamIdMegIdIcc.setStatus("current")


class _MplsOamIdMegIdUmc_Type(SnmpAdminString):
    """Custom type mplsOamIdMegIdUmc based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_MplsOamIdMegIdUmc_Type.__name__ = "SnmpAdminString"
_MplsOamIdMegIdUmc_Object = MibTableColumn
mplsOamIdMegIdUmc = _MplsOamIdMegIdUmc_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 1, 2, 1, 6),
    _MplsOamIdMegIdUmc_Type()
)
mplsOamIdMegIdUmc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOamIdMegIdUmc.setStatus("current")


class _MplsOamIdMegServicePointerType_Type(Integer32):
    """Custom type mplsOamIdMegServicePointerType based on Integer32"""
    defaultValue = 2

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
        *(("tunnel", 1),
          ("lsp", 2),
          ("pseudowire", 3),
          ("section", 4))
    )


_MplsOamIdMegServicePointerType_Type.__name__ = "Integer32"
_MplsOamIdMegServicePointerType_Object = MibTableColumn
mplsOamIdMegServicePointerType = _MplsOamIdMegServicePointerType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 1, 2, 1, 7),
    _MplsOamIdMegServicePointerType_Type()
)
mplsOamIdMegServicePointerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOamIdMegServicePointerType.setStatus("current")


class _MplsOamIdMegMpLocation_Type(Integer32):
    """Custom type mplsOamIdMegMpLocation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("perNode", 1),
          ("perInterface", 2))
    )


_MplsOamIdMegMpLocation_Type.__name__ = "Integer32"
_MplsOamIdMegMpLocation_Object = MibTableColumn
mplsOamIdMegMpLocation = _MplsOamIdMegMpLocation_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 1, 2, 1, 8),
    _MplsOamIdMegMpLocation_Type()
)
mplsOamIdMegMpLocation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOamIdMegMpLocation.setStatus("current")


class _MplsOamIdMegPathFlow_Type(Integer32):
    """Custom type mplsOamIdMegPathFlow based on Integer32"""
    defaultValue = 2

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
        *(("unidirectionalPointToPoint", 1),
          ("coRoutedBidirectionalPointToPoint", 2),
          ("associatedBidirectionalPointToPoint", 3),
          ("unidirectionalPointToMultiPoint", 4))
    )


_MplsOamIdMegPathFlow_Type.__name__ = "Integer32"
_MplsOamIdMegPathFlow_Object = MibTableColumn
mplsOamIdMegPathFlow = _MplsOamIdMegPathFlow_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 1, 2, 1, 9),
    _MplsOamIdMegPathFlow_Type()
)
mplsOamIdMegPathFlow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOamIdMegPathFlow.setStatus("current")


class _MplsOamIdMegOperStatus_Type(Integer32):
    """Custom type mplsOamIdMegOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_MplsOamIdMegOperStatus_Type.__name__ = "Integer32"
_MplsOamIdMegOperStatus_Object = MibTableColumn
mplsOamIdMegOperStatus = _MplsOamIdMegOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 1, 2, 1, 10),
    _MplsOamIdMegOperStatus_Type()
)
mplsOamIdMegOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOamIdMegOperStatus.setStatus("current")


class _MplsOamIdMegSubOperStatus_Type(Bits):
    """Custom type mplsOamIdMegSubOperStatus based on Bits"""
    namedValues = NamedValues(
        *(("megDown", 0),
          ("meDown", 1),
          ("oamAppDown", 2),
          ("pathDown", 3))
    )

_MplsOamIdMegSubOperStatus_Type.__name__ = "Bits"
_MplsOamIdMegSubOperStatus_Object = MibTableColumn
mplsOamIdMegSubOperStatus = _MplsOamIdMegSubOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 1, 2, 1, 11),
    _MplsOamIdMegSubOperStatus_Type()
)
mplsOamIdMegSubOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOamIdMegSubOperStatus.setStatus("current")
_MplsOamIdMegRowStatus_Type = RowStatus
_MplsOamIdMegRowStatus_Object = MibTableColumn
mplsOamIdMegRowStatus = _MplsOamIdMegRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 1, 2, 1, 12),
    _MplsOamIdMegRowStatus_Type()
)
mplsOamIdMegRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOamIdMegRowStatus.setStatus("current")


class _MplsOamIdMegStorageType_Type(StorageType):
    """Custom type mplsOamIdMegStorageType based on StorageType"""
    defaultValue = 2


_MplsOamIdMegStorageType_Type.__name__ = "StorageType"
_MplsOamIdMegStorageType_Object = MibTableColumn
mplsOamIdMegStorageType = _MplsOamIdMegStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 1, 2, 1, 13),
    _MplsOamIdMegStorageType_Type()
)
mplsOamIdMegStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOamIdMegStorageType.setStatus("current")


class _MplsOamIdMeIndexNext_Type(IndexIntegerNextFree):
    """Custom type mplsOamIdMeIndexNext based on IndexIntegerNextFree"""
    subtypeSpec = IndexIntegerNextFree.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MplsOamIdMeIndexNext_Type.__name__ = "IndexIntegerNextFree"
_MplsOamIdMeIndexNext_Object = MibScalar
mplsOamIdMeIndexNext = _MplsOamIdMeIndexNext_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 1, 3),
    _MplsOamIdMeIndexNext_Type()
)
mplsOamIdMeIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOamIdMeIndexNext.setStatus("current")


class _MplsOamIdMeMpIndexNext_Type(IndexIntegerNextFree):
    """Custom type mplsOamIdMeMpIndexNext based on IndexIntegerNextFree"""
    subtypeSpec = IndexIntegerNextFree.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MplsOamIdMeMpIndexNext_Type.__name__ = "IndexIntegerNextFree"
_MplsOamIdMeMpIndexNext_Object = MibScalar
mplsOamIdMeMpIndexNext = _MplsOamIdMeMpIndexNext_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 1, 4),
    _MplsOamIdMeMpIndexNext_Type()
)
mplsOamIdMeMpIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOamIdMeMpIndexNext.setStatus("current")
_MplsOamIdMeTable_Object = MibTable
mplsOamIdMeTable = _MplsOamIdMeTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 1, 5)
)
if mibBuilder.loadTexts:
    mplsOamIdMeTable.setStatus("current")
_MplsOamIdMeEntry_Object = MibTableRow
mplsOamIdMeEntry = _MplsOamIdMeEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 1, 5, 1)
)
mplsOamIdMeEntry.setIndexNames(
    (0, "MPLS-OAM-ID-STD-MIB", "mplsOamIdMegIndex"),
    (0, "MPLS-OAM-ID-STD-MIB", "mplsOamIdMeIndex"),
    (0, "MPLS-OAM-ID-STD-MIB", "mplsOamIdMeMpIndex"),
)
if mibBuilder.loadTexts:
    mplsOamIdMeEntry.setStatus("current")


class _MplsOamIdMeIndex_Type(Unsigned32):
    """Custom type mplsOamIdMeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MplsOamIdMeIndex_Type.__name__ = "Unsigned32"
_MplsOamIdMeIndex_Object = MibTableColumn
mplsOamIdMeIndex = _MplsOamIdMeIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 1, 5, 1, 1),
    _MplsOamIdMeIndex_Type()
)
mplsOamIdMeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsOamIdMeIndex.setStatus("current")


class _MplsOamIdMeMpIndex_Type(Unsigned32):
    """Custom type mplsOamIdMeMpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MplsOamIdMeMpIndex_Type.__name__ = "Unsigned32"
_MplsOamIdMeMpIndex_Object = MibTableColumn
mplsOamIdMeMpIndex = _MplsOamIdMeMpIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 1, 5, 1, 2),
    _MplsOamIdMeMpIndex_Type()
)
mplsOamIdMeMpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsOamIdMeMpIndex.setStatus("current")


class _MplsOamIdMeName_Type(SnmpAdminString):
    """Custom type mplsOamIdMeName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_MplsOamIdMeName_Type.__name__ = "SnmpAdminString"
_MplsOamIdMeName_Object = MibTableColumn
mplsOamIdMeName = _MplsOamIdMeName_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 1, 5, 1, 3),
    _MplsOamIdMeName_Type()
)
mplsOamIdMeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOamIdMeName.setStatus("current")


class _MplsOamIdMeMpIfIndex_Type(InterfaceIndexOrZero):
    """Custom type mplsOamIdMeMpIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_MplsOamIdMeMpIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_MplsOamIdMeMpIfIndex_Object = MibTableColumn
mplsOamIdMeMpIfIndex = _MplsOamIdMeMpIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 1, 5, 1, 4),
    _MplsOamIdMeMpIfIndex_Type()
)
mplsOamIdMeMpIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOamIdMeMpIfIndex.setStatus("current")


class _MplsOamIdMeSourceMepIndex_Type(Unsigned32):
    """Custom type mplsOamIdMeSourceMepIndex based on Unsigned32"""
    defaultValue = 0


_MplsOamIdMeSourceMepIndex_Type.__name__ = "Unsigned32"
_MplsOamIdMeSourceMepIndex_Object = MibTableColumn
mplsOamIdMeSourceMepIndex = _MplsOamIdMeSourceMepIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 1, 5, 1, 5),
    _MplsOamIdMeSourceMepIndex_Type()
)
mplsOamIdMeSourceMepIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOamIdMeSourceMepIndex.setStatus("current")


class _MplsOamIdMeSinkMepIndex_Type(Unsigned32):
    """Custom type mplsOamIdMeSinkMepIndex based on Unsigned32"""
    defaultValue = 0


_MplsOamIdMeSinkMepIndex_Type.__name__ = "Unsigned32"
_MplsOamIdMeSinkMepIndex_Object = MibTableColumn
mplsOamIdMeSinkMepIndex = _MplsOamIdMeSinkMepIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 1, 5, 1, 6),
    _MplsOamIdMeSinkMepIndex_Type()
)
mplsOamIdMeSinkMepIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOamIdMeSinkMepIndex.setStatus("current")


class _MplsOamIdMeMpType_Type(Integer32):
    """Custom type mplsOamIdMeMpType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mep", 1),
          ("mip", 2))
    )


_MplsOamIdMeMpType_Type.__name__ = "Integer32"
_MplsOamIdMeMpType_Object = MibTableColumn
mplsOamIdMeMpType = _MplsOamIdMeMpType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 1, 5, 1, 7),
    _MplsOamIdMeMpType_Type()
)
mplsOamIdMeMpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOamIdMeMpType.setStatus("current")


class _MplsOamIdMeMepDirection_Type(Integer32):
    """Custom type mplsOamIdMeMepDirection based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("notApplicable", 3))
    )


_MplsOamIdMeMepDirection_Type.__name__ = "Integer32"
_MplsOamIdMeMepDirection_Object = MibTableColumn
mplsOamIdMeMepDirection = _MplsOamIdMeMepDirection_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 1, 5, 1, 8),
    _MplsOamIdMeMepDirection_Type()
)
mplsOamIdMeMepDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOamIdMeMepDirection.setStatus("current")
_MplsOamIdMeServicePointer_Type = RowPointer
_MplsOamIdMeServicePointer_Object = MibTableColumn
mplsOamIdMeServicePointer = _MplsOamIdMeServicePointer_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 1, 5, 1, 9),
    _MplsOamIdMeServicePointer_Type()
)
mplsOamIdMeServicePointer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOamIdMeServicePointer.setStatus("current")
_MplsOamIdMeRowStatus_Type = RowStatus
_MplsOamIdMeRowStatus_Object = MibTableColumn
mplsOamIdMeRowStatus = _MplsOamIdMeRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 1, 5, 1, 10),
    _MplsOamIdMeRowStatus_Type()
)
mplsOamIdMeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOamIdMeRowStatus.setStatus("current")


class _MplsOamIdMeStorageType_Type(StorageType):
    """Custom type mplsOamIdMeStorageType based on StorageType"""
    defaultValue = 2


_MplsOamIdMeStorageType_Type.__name__ = "StorageType"
_MplsOamIdMeStorageType_Object = MibTableColumn
mplsOamIdMeStorageType = _MplsOamIdMeStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 1, 5, 1, 11),
    _MplsOamIdMeStorageType_Type()
)
mplsOamIdMeStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOamIdMeStorageType.setStatus("current")
_MplsOamIdConformance_ObjectIdentity = ObjectIdentity
mplsOamIdConformance = _MplsOamIdConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 2)
)
_MplsOamIdCompliances_ObjectIdentity = ObjectIdentity
mplsOamIdCompliances = _MplsOamIdCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 2, 1)
)
_MplsOamIdGroups_ObjectIdentity = ObjectIdentity
mplsOamIdGroups = _MplsOamIdGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 2, 2)
)

# Managed Objects groups

mplsOamIdMegGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 2, 2, 1)
)
mplsOamIdMegGroup.setObjects(
      *(("MPLS-OAM-ID-STD-MIB", "mplsOamIdMegIndexNext"),
        ("MPLS-OAM-ID-STD-MIB", "mplsOamIdMegName"),
        ("MPLS-OAM-ID-STD-MIB", "mplsOamIdMegOperatorType"),
        ("MPLS-OAM-ID-STD-MIB", "mplsOamIdMegIdCc"),
        ("MPLS-OAM-ID-STD-MIB", "mplsOamIdMegIdIcc"),
        ("MPLS-OAM-ID-STD-MIB", "mplsOamIdMegIdUmc"),
        ("MPLS-OAM-ID-STD-MIB", "mplsOamIdMegServicePointerType"),
        ("MPLS-OAM-ID-STD-MIB", "mplsOamIdMegMpLocation"),
        ("MPLS-OAM-ID-STD-MIB", "mplsOamIdMegOperStatus"),
        ("MPLS-OAM-ID-STD-MIB", "mplsOamIdMegSubOperStatus"),
        ("MPLS-OAM-ID-STD-MIB", "mplsOamIdMegPathFlow"),
        ("MPLS-OAM-ID-STD-MIB", "mplsOamIdMegRowStatus"),
        ("MPLS-OAM-ID-STD-MIB", "mplsOamIdMegStorageType"))
)
if mibBuilder.loadTexts:
    mplsOamIdMegGroup.setStatus("current")

mplsOamIdMeGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 2, 2, 2)
)
mplsOamIdMeGroup.setObjects(
      *(("MPLS-OAM-ID-STD-MIB", "mplsOamIdMeIndexNext"),
        ("MPLS-OAM-ID-STD-MIB", "mplsOamIdMeMpIndexNext"),
        ("MPLS-OAM-ID-STD-MIB", "mplsOamIdMeName"),
        ("MPLS-OAM-ID-STD-MIB", "mplsOamIdMeMpIfIndex"),
        ("MPLS-OAM-ID-STD-MIB", "mplsOamIdMeSourceMepIndex"),
        ("MPLS-OAM-ID-STD-MIB", "mplsOamIdMeSinkMepIndex"),
        ("MPLS-OAM-ID-STD-MIB", "mplsOamIdMeMpType"),
        ("MPLS-OAM-ID-STD-MIB", "mplsOamIdMeMepDirection"),
        ("MPLS-OAM-ID-STD-MIB", "mplsOamIdMeServicePointer"),
        ("MPLS-OAM-ID-STD-MIB", "mplsOamIdMeRowStatus"),
        ("MPLS-OAM-ID-STD-MIB", "mplsOamIdMeStorageType"))
)
if mibBuilder.loadTexts:
    mplsOamIdMeGroup.setStatus("current")

mplsOamIdNotificationObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 2, 2, 3)
)
mplsOamIdNotificationObjectsGroup.setObjects(
      *(("MPLS-OAM-ID-STD-MIB", "mplsOamIdMegOperStatus"),
        ("MPLS-OAM-ID-STD-MIB", "mplsOamIdMegSubOperStatus"))
)
if mibBuilder.loadTexts:
    mplsOamIdNotificationObjectsGroup.setStatus("current")


# Notification objects

mplsOamIdDefectCondition = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 0, 1)
)
mplsOamIdDefectCondition.setObjects(
      *(("MPLS-OAM-ID-STD-MIB", "mplsOamIdMegName"),
        ("MPLS-OAM-ID-STD-MIB", "mplsOamIdMeName"),
        ("MPLS-OAM-ID-STD-MIB", "mplsOamIdMegOperStatus"),
        ("MPLS-OAM-ID-STD-MIB", "mplsOamIdMegSubOperStatus"))
)
if mibBuilder.loadTexts:
    mplsOamIdDefectCondition.setStatus(
        "current"
    )


# Notifications groups

mplsOamIdNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 2, 2, 4)
)
mplsOamIdNotificationGroup.setObjects(
    ("MPLS-OAM-ID-STD-MIB", "mplsOamIdDefectCondition")
)
if mibBuilder.loadTexts:
    mplsOamIdNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

mplsOamIdModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 2, 1, 1)
)
mplsOamIdModuleFullCompliance.setObjects(
      *(("IF-MIB", "ifGeneralInformationGroup"),
        ("IF-MIB", "ifCounterDiscontinuityGroup"),
        ("MPLS-OAM-ID-STD-MIB", "mplsOamIdMegGroup"),
        ("MPLS-OAM-ID-STD-MIB", "mplsOamIdMeGroup"),
        ("MPLS-OAM-ID-STD-MIB", "mplsOamIdNotificationObjectsGroup"),
        ("MPLS-OAM-ID-STD-MIB", "mplsOamIdNotificationGroup"))
)
if mibBuilder.loadTexts:
    mplsOamIdModuleFullCompliance.setStatus(
        "current"
    )

mplsOamIdModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 166, 21, 2, 1, 2)
)
mplsOamIdModuleReadOnlyCompliance.setObjects(
      *(("MPLS-OAM-ID-STD-MIB", "mplsOamIdMegGroup"),
        ("MPLS-OAM-ID-STD-MIB", "mplsOamIdMeGroup"),
        ("MPLS-OAM-ID-STD-MIB", "mplsOamIdNotificationObjectsGroup"),
        ("MPLS-OAM-ID-STD-MIB", "mplsOamIdNotificationGroup"))
)
if mibBuilder.loadTexts:
    mplsOamIdModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPLS-OAM-ID-STD-MIB",
    **{"mplsOamIdStdMIB": mplsOamIdStdMIB,
       "mplsOamIdNotifications": mplsOamIdNotifications,
       "mplsOamIdDefectCondition": mplsOamIdDefectCondition,
       "mplsOamIdObjects": mplsOamIdObjects,
       "mplsOamIdMegIndexNext": mplsOamIdMegIndexNext,
       "mplsOamIdMegTable": mplsOamIdMegTable,
       "mplsOamIdMegEntry": mplsOamIdMegEntry,
       "mplsOamIdMegIndex": mplsOamIdMegIndex,
       "mplsOamIdMegName": mplsOamIdMegName,
       "mplsOamIdMegOperatorType": mplsOamIdMegOperatorType,
       "mplsOamIdMegIdCc": mplsOamIdMegIdCc,
       "mplsOamIdMegIdIcc": mplsOamIdMegIdIcc,
       "mplsOamIdMegIdUmc": mplsOamIdMegIdUmc,
       "mplsOamIdMegServicePointerType": mplsOamIdMegServicePointerType,
       "mplsOamIdMegMpLocation": mplsOamIdMegMpLocation,
       "mplsOamIdMegPathFlow": mplsOamIdMegPathFlow,
       "mplsOamIdMegOperStatus": mplsOamIdMegOperStatus,
       "mplsOamIdMegSubOperStatus": mplsOamIdMegSubOperStatus,
       "mplsOamIdMegRowStatus": mplsOamIdMegRowStatus,
       "mplsOamIdMegStorageType": mplsOamIdMegStorageType,
       "mplsOamIdMeIndexNext": mplsOamIdMeIndexNext,
       "mplsOamIdMeMpIndexNext": mplsOamIdMeMpIndexNext,
       "mplsOamIdMeTable": mplsOamIdMeTable,
       "mplsOamIdMeEntry": mplsOamIdMeEntry,
       "mplsOamIdMeIndex": mplsOamIdMeIndex,
       "mplsOamIdMeMpIndex": mplsOamIdMeMpIndex,
       "mplsOamIdMeName": mplsOamIdMeName,
       "mplsOamIdMeMpIfIndex": mplsOamIdMeMpIfIndex,
       "mplsOamIdMeSourceMepIndex": mplsOamIdMeSourceMepIndex,
       "mplsOamIdMeSinkMepIndex": mplsOamIdMeSinkMepIndex,
       "mplsOamIdMeMpType": mplsOamIdMeMpType,
       "mplsOamIdMeMepDirection": mplsOamIdMeMepDirection,
       "mplsOamIdMeServicePointer": mplsOamIdMeServicePointer,
       "mplsOamIdMeRowStatus": mplsOamIdMeRowStatus,
       "mplsOamIdMeStorageType": mplsOamIdMeStorageType,
       "mplsOamIdConformance": mplsOamIdConformance,
       "mplsOamIdCompliances": mplsOamIdCompliances,
       "mplsOamIdModuleFullCompliance": mplsOamIdModuleFullCompliance,
       "mplsOamIdModuleReadOnlyCompliance": mplsOamIdModuleReadOnlyCompliance,
       "mplsOamIdGroups": mplsOamIdGroups,
       "mplsOamIdMegGroup": mplsOamIdMegGroup,
       "mplsOamIdMeGroup": mplsOamIdMeGroup,
       "mplsOamIdNotificationObjectsGroup": mplsOamIdNotificationObjectsGroup,
       "mplsOamIdNotificationGroup": mplsOamIdNotificationGroup}
)
