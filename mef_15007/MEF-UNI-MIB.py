# SNMP MIB module (MEF-UNI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/mef_15007/MEF-UNI-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:23:56 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

mefUniMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2)
)
if mibBuilder.loadTexts:
    mefUniMib.setRevisions(
        ("2012-03-15 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MefServiceNotifications_ObjectIdentity = ObjectIdentity
mefServiceNotifications = _MefServiceNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 0)
)
_MefServiceInterfaceObjects_ObjectIdentity = ObjectIdentity
mefServiceInterfaceObjects = _MefServiceInterfaceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1)
)
_MefServiceInterface_ObjectIdentity = ObjectIdentity
mefServiceInterface = _MefServiceInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1)
)
_MefServiceInterfaceCfgTable_Object = MibTable
mefServiceInterfaceCfgTable = _MefServiceInterfaceCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mefServiceInterfaceCfgTable.setStatus("current")
_MefServiceInterfaceCfgEntry_Object = MibTableRow
mefServiceInterfaceCfgEntry = _MefServiceInterfaceCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 1, 1)
)
mefServiceInterfaceCfgEntry.setIndexNames(
    (0, "MEF-UNI-MIB", "mefServiceInterfaceCfgNumber"),
)
if mibBuilder.loadTexts:
    mefServiceInterfaceCfgEntry.setStatus("current")
_MefServiceInterfaceCfgNumber_Type = Unsigned32
_MefServiceInterfaceCfgNumber_Object = MibTableColumn
mefServiceInterfaceCfgNumber = _MefServiceInterfaceCfgNumber_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 1, 1, 1),
    _MefServiceInterfaceCfgNumber_Type()
)
mefServiceInterfaceCfgNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mefServiceInterfaceCfgNumber.setStatus("current")


class _MefServiceInterfaceCfgType_Type(Integer32):
    """Custom type mefServiceInterfaceCfgType based on Integer32"""
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
        *(("uni1d1", 1),
          ("uni1d2", 2),
          ("uni2d1", 3),
          ("uni2d2", 4),
          ("enni", 5),
          ("enniVuni", 6))
    )


_MefServiceInterfaceCfgType_Type.__name__ = "Integer32"
_MefServiceInterfaceCfgType_Object = MibTableColumn
mefServiceInterfaceCfgType = _MefServiceInterfaceCfgType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 1, 1, 2),
    _MefServiceInterfaceCfgType_Type()
)
mefServiceInterfaceCfgType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceInterfaceCfgType.setStatus("current")


class _MefServiceInterfaceCfgIdentifier_Type(OctetString):
    """Custom type mefServiceInterfaceCfgIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_MefServiceInterfaceCfgIdentifier_Type.__name__ = "OctetString"
_MefServiceInterfaceCfgIdentifier_Object = MibTableColumn
mefServiceInterfaceCfgIdentifier = _MefServiceInterfaceCfgIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 1, 1, 3),
    _MefServiceInterfaceCfgIdentifier_Type()
)
mefServiceInterfaceCfgIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceInterfaceCfgIdentifier.setStatus("current")


class _MefServiceInterfaceCfgSpeed_Type(Integer32):
    """Custom type mefServiceInterfaceCfgSpeed based on Integer32"""
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
        *(("auto", 1),
          ("speed10M", 2),
          ("speed100M", 3),
          ("speed1G", 4),
          ("speed10G", 5))
    )


_MefServiceInterfaceCfgSpeed_Type.__name__ = "Integer32"
_MefServiceInterfaceCfgSpeed_Object = MibTableColumn
mefServiceInterfaceCfgSpeed = _MefServiceInterfaceCfgSpeed_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 1, 1, 4),
    _MefServiceInterfaceCfgSpeed_Type()
)
mefServiceInterfaceCfgSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceInterfaceCfgSpeed.setStatus("current")


class _MefServiceInterfaceCfgMode_Type(Integer32):
    """Custom type mefServiceInterfaceCfgMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 1),
          ("halfDuplex", 2))
    )


_MefServiceInterfaceCfgMode_Type.__name__ = "Integer32"
_MefServiceInterfaceCfgMode_Object = MibTableColumn
mefServiceInterfaceCfgMode = _MefServiceInterfaceCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 1, 1, 5),
    _MefServiceInterfaceCfgMode_Type()
)
mefServiceInterfaceCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceInterfaceCfgMode.setStatus("current")


class _MefServiceInterfaceCfgNegotiate_Type(Integer32):
    """Custom type mefServiceInterfaceCfgNegotiate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("force", 1),
          ("auto", 2))
    )


_MefServiceInterfaceCfgNegotiate_Type.__name__ = "Integer32"
_MefServiceInterfaceCfgNegotiate_Object = MibTableColumn
mefServiceInterfaceCfgNegotiate = _MefServiceInterfaceCfgNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 1, 1, 6),
    _MefServiceInterfaceCfgNegotiate_Type()
)
mefServiceInterfaceCfgNegotiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceInterfaceCfgNegotiate.setStatus("current")


class _MefServiceInterfaceCfgFrameFormat_Type(Integer32):
    """Custom type mefServiceInterfaceCfgFrameFormat based on Integer32"""
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
        *(("noTag", 1),
          ("ctag", 2),
          ("stag", 3),
          ("stagCtag", 4))
    )


_MefServiceInterfaceCfgFrameFormat_Type.__name__ = "Integer32"
_MefServiceInterfaceCfgFrameFormat_Object = MibTableColumn
mefServiceInterfaceCfgFrameFormat = _MefServiceInterfaceCfgFrameFormat_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 1, 1, 7),
    _MefServiceInterfaceCfgFrameFormat_Type()
)
mefServiceInterfaceCfgFrameFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceInterfaceCfgFrameFormat.setStatus("current")


class _MefServiceInterfaceCfgMtuSize_Type(Unsigned32):
    """Custom type mefServiceInterfaceCfgMtuSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1522, 16384),
    )


_MefServiceInterfaceCfgMtuSize_Type.__name__ = "Unsigned32"
_MefServiceInterfaceCfgMtuSize_Object = MibTableColumn
mefServiceInterfaceCfgMtuSize = _MefServiceInterfaceCfgMtuSize_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 1, 1, 8),
    _MefServiceInterfaceCfgMtuSize_Type()
)
mefServiceInterfaceCfgMtuSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceInterfaceCfgMtuSize.setStatus("current")


class _MefServiceInterfaceCfgIngressBwpIndex_Type(Unsigned32):
    """Custom type mefServiceInterfaceCfgIngressBwpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_MefServiceInterfaceCfgIngressBwpIndex_Type.__name__ = "Unsigned32"
_MefServiceInterfaceCfgIngressBwpIndex_Object = MibTableColumn
mefServiceInterfaceCfgIngressBwpIndex = _MefServiceInterfaceCfgIngressBwpIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 1, 1, 9),
    _MefServiceInterfaceCfgIngressBwpIndex_Type()
)
mefServiceInterfaceCfgIngressBwpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceInterfaceCfgIngressBwpIndex.setStatus("current")


class _MefServiceInterfaceCfgEgressBwpIndex_Type(Unsigned32):
    """Custom type mefServiceInterfaceCfgEgressBwpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_MefServiceInterfaceCfgEgressBwpIndex_Type.__name__ = "Unsigned32"
_MefServiceInterfaceCfgEgressBwpIndex_Object = MibTableColumn
mefServiceInterfaceCfgEgressBwpIndex = _MefServiceInterfaceCfgEgressBwpIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 1, 1, 10),
    _MefServiceInterfaceCfgEgressBwpIndex_Type()
)
mefServiceInterfaceCfgEgressBwpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceInterfaceCfgEgressBwpIndex.setStatus("current")
_MefServiceInterfaceStatusTable_Object = MibTable
mefServiceInterfaceStatusTable = _MefServiceInterfaceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mefServiceInterfaceStatusTable.setStatus("current")
_MefServiceInterfaceStatusEntry_Object = MibTableRow
mefServiceInterfaceStatusEntry = _MefServiceInterfaceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 2, 1)
)
mefServiceInterfaceStatusEntry.setIndexNames(
    (0, "MEF-UNI-MIB", "mefServiceInterfaceStatusNumber"),
)
if mibBuilder.loadTexts:
    mefServiceInterfaceStatusEntry.setStatus("current")
_MefServiceInterfaceStatusNumber_Type = Unsigned32
_MefServiceInterfaceStatusNumber_Object = MibTableColumn
mefServiceInterfaceStatusNumber = _MefServiceInterfaceStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 2, 1, 1),
    _MefServiceInterfaceStatusNumber_Type()
)
mefServiceInterfaceStatusNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mefServiceInterfaceStatusNumber.setStatus("current")


class _MefServiceInterfaceStatusType_Type(Bits):
    """Custom type mefServiceInterfaceStatusType based on Bits"""
    namedValues = NamedValues(
        *(("bUni1d1", 0),
          ("bUni1d2", 1),
          ("bUni2d1", 2),
          ("bUni2d2", 3),
          ("bEnni", 4),
          ("bEnniVuni", 5))
    )

_MefServiceInterfaceStatusType_Type.__name__ = "Bits"
_MefServiceInterfaceStatusType_Object = MibTableColumn
mefServiceInterfaceStatusType = _MefServiceInterfaceStatusType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 2, 1, 2),
    _MefServiceInterfaceStatusType_Type()
)
mefServiceInterfaceStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceInterfaceStatusType.setStatus("current")


class _MefServiceInterfaceStatusPhysicalLayer_Type(Integer32):
    """Custom type mefServiceInterfaceStatusPhysicalLayer based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("p10BaseT", 1),
          ("p100BaseTx", 2),
          ("p100BaseFx", 3),
          ("p1000BaseSx", 4),
          ("p1000BaseLx", 5),
          ("p1000BaseT", 6),
          ("p10GBaseSr", 7),
          ("p10gBaseLx4", 8),
          ("p10gBaseLr", 9),
          ("p10gBaseEr", 10),
          ("p10gBaseSw", 11),
          ("p10gBaseLw", 12),
          ("p10GbaseEw", 13))
    )


_MefServiceInterfaceStatusPhysicalLayer_Type.__name__ = "Integer32"
_MefServiceInterfaceStatusPhysicalLayer_Object = MibTableColumn
mefServiceInterfaceStatusPhysicalLayer = _MefServiceInterfaceStatusPhysicalLayer_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 2, 1, 3),
    _MefServiceInterfaceStatusPhysicalLayer_Type()
)
mefServiceInterfaceStatusPhysicalLayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceInterfaceStatusPhysicalLayer.setStatus("current")


class _MefServiceInterfaceStatusSpeed_Type(Integer32):
    """Custom type mefServiceInterfaceStatusSpeed based on Integer32"""
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
        *(("speed10M", 1),
          ("speed100M", 2),
          ("speed1G", 3),
          ("speed10G", 4))
    )


_MefServiceInterfaceStatusSpeed_Type.__name__ = "Integer32"
_MefServiceInterfaceStatusSpeed_Object = MibTableColumn
mefServiceInterfaceStatusSpeed = _MefServiceInterfaceStatusSpeed_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 2, 1, 4),
    _MefServiceInterfaceStatusSpeed_Type()
)
mefServiceInterfaceStatusSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceInterfaceStatusSpeed.setStatus("current")


class _MefServiceInterfaceStatusMode_Type(Integer32):
    """Custom type mefServiceInterfaceStatusMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 1),
          ("halfDuplex", 2))
    )


_MefServiceInterfaceStatusMode_Type.__name__ = "Integer32"
_MefServiceInterfaceStatusMode_Object = MibTableColumn
mefServiceInterfaceStatusMode = _MefServiceInterfaceStatusMode_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 2, 1, 5),
    _MefServiceInterfaceStatusMode_Type()
)
mefServiceInterfaceStatusMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceInterfaceStatusMode.setStatus("current")


class _MefServiceInterfaceStatusMaxMtuSize_Type(Unsigned32):
    """Custom type mefServiceInterfaceStatusMaxMtuSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1522, 16384),
    )


_MefServiceInterfaceStatusMaxMtuSize_Type.__name__ = "Unsigned32"
_MefServiceInterfaceStatusMaxMtuSize_Object = MibTableColumn
mefServiceInterfaceStatusMaxMtuSize = _MefServiceInterfaceStatusMaxMtuSize_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 2, 1, 6),
    _MefServiceInterfaceStatusMaxMtuSize_Type()
)
mefServiceInterfaceStatusMaxMtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceInterfaceStatusMaxMtuSize.setStatus("current")


class _MefServiceInterfaceStatusMaxVc_Type(Unsigned32):
    """Custom type mefServiceInterfaceStatusMaxVc based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_MefServiceInterfaceStatusMaxVc_Type.__name__ = "Unsigned32"
_MefServiceInterfaceStatusMaxVc_Object = MibTableColumn
mefServiceInterfaceStatusMaxVc = _MefServiceInterfaceStatusMaxVc_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 2, 1, 7),
    _MefServiceInterfaceStatusMaxVc_Type()
)
mefServiceInterfaceStatusMaxVc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceInterfaceStatusMaxVc.setStatus("current")


class _MefServiceInterfaceStatusMaxEndPointPerVc_Type(Unsigned32):
    """Custom type mefServiceInterfaceStatusMaxEndPointPerVc based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MefServiceInterfaceStatusMaxEndPointPerVc_Type.__name__ = "Unsigned32"
_MefServiceInterfaceStatusMaxEndPointPerVc_Object = MibTableColumn
mefServiceInterfaceStatusMaxEndPointPerVc = _MefServiceInterfaceStatusMaxEndPointPerVc_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 1, 2, 1, 8),
    _MefServiceInterfaceStatusMaxEndPointPerVc_Type()
)
mefServiceInterfaceStatusMaxEndPointPerVc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceInterfaceStatusMaxEndPointPerVc.setStatus("current")
_MefServiceInterfaceL2cp_ObjectIdentity = ObjectIdentity
mefServiceInterfaceL2cp = _MefServiceInterfaceL2cp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 2)
)
_MefServiceL2cpCfgTable_Object = MibTable
mefServiceL2cpCfgTable = _MefServiceL2cpCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mefServiceL2cpCfgTable.setStatus("current")
_MefServiceL2cpCfgEntry_Object = MibTableRow
mefServiceL2cpCfgEntry = _MefServiceL2cpCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 2, 1, 1)
)
mefServiceL2cpCfgEntry.setIndexNames(
    (0, "MEF-UNI-MIB", "mefServiceL2cpCfgInterfaceNumber"),
    (0, "MEF-UNI-MIB", "mefServiceL2cpCfgIndex"),
)
if mibBuilder.loadTexts:
    mefServiceL2cpCfgEntry.setStatus("current")
_MefServiceL2cpCfgInterfaceNumber_Type = Unsigned32
_MefServiceL2cpCfgInterfaceNumber_Object = MibTableColumn
mefServiceL2cpCfgInterfaceNumber = _MefServiceL2cpCfgInterfaceNumber_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 2, 1, 1, 1),
    _MefServiceL2cpCfgInterfaceNumber_Type()
)
mefServiceL2cpCfgInterfaceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mefServiceL2cpCfgInterfaceNumber.setStatus("current")
_MefServiceL2cpCfgIndex_Type = Unsigned32
_MefServiceL2cpCfgIndex_Object = MibTableColumn
mefServiceL2cpCfgIndex = _MefServiceL2cpCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 2, 1, 1, 2),
    _MefServiceL2cpCfgIndex_Type()
)
mefServiceL2cpCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mefServiceL2cpCfgIndex.setStatus("current")


class _MefServiceL2cpCfgType_Type(Integer32):
    """Custom type mefServiceL2cpCfgType based on Integer32"""
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
        *(("discard", 1),
          ("tunnel", 2),
          ("peer", 3),
          ("passToEvc", 4),
          ("peerToEvc", 5))
    )


_MefServiceL2cpCfgType_Type.__name__ = "Integer32"
_MefServiceL2cpCfgType_Object = MibTableColumn
mefServiceL2cpCfgType = _MefServiceL2cpCfgType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 2, 1, 1, 3),
    _MefServiceL2cpCfgType_Type()
)
mefServiceL2cpCfgType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceL2cpCfgType.setStatus("current")


class _MefServiceL2cpCfgMatchScope_Type(Integer32):
    """Custom type mefServiceL2cpCfgMatchScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("destationAddressOnly", 1),
          ("daPlusProtocol", 2),
          ("daPlusProtocolPlusSubtype", 3))
    )


_MefServiceL2cpCfgMatchScope_Type.__name__ = "Integer32"
_MefServiceL2cpCfgMatchScope_Object = MibTableColumn
mefServiceL2cpCfgMatchScope = _MefServiceL2cpCfgMatchScope_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 2, 1, 1, 4),
    _MefServiceL2cpCfgMatchScope_Type()
)
mefServiceL2cpCfgMatchScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceL2cpCfgMatchScope.setStatus("current")
_MefServiceL2cpCfgMacAddress_Type = MacAddress
_MefServiceL2cpCfgMacAddress_Object = MibTableColumn
mefServiceL2cpCfgMacAddress = _MefServiceL2cpCfgMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 2, 1, 1, 5),
    _MefServiceL2cpCfgMacAddress_Type()
)
mefServiceL2cpCfgMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceL2cpCfgMacAddress.setStatus("current")
_MefServiceL2cpCfgProtocol_Type = Unsigned32
_MefServiceL2cpCfgProtocol_Object = MibTableColumn
mefServiceL2cpCfgProtocol = _MefServiceL2cpCfgProtocol_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 2, 1, 1, 6),
    _MefServiceL2cpCfgProtocol_Type()
)
mefServiceL2cpCfgProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceL2cpCfgProtocol.setStatus("current")
_MefServiceL2cpCfgSubType_Type = Unsigned32
_MefServiceL2cpCfgSubType_Object = MibTableColumn
mefServiceL2cpCfgSubType = _MefServiceL2cpCfgSubType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 2, 1, 1, 7),
    _MefServiceL2cpCfgSubType_Type()
)
mefServiceL2cpCfgSubType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceL2cpCfgSubType.setStatus("current")


class _MefServiceL2cpCfgEvcName_Type(OctetString):
    """Custom type mefServiceL2cpCfgEvcName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_MefServiceL2cpCfgEvcName_Type.__name__ = "OctetString"
_MefServiceL2cpCfgEvcName_Object = MibTableColumn
mefServiceL2cpCfgEvcName = _MefServiceL2cpCfgEvcName_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 2, 1, 1, 8),
    _MefServiceL2cpCfgEvcName_Type()
)
mefServiceL2cpCfgEvcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceL2cpCfgEvcName.setStatus("current")


class _MefServiceL2cpCfgValid_Type(Integer32):
    """Custom type mefServiceL2cpCfgValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_MefServiceL2cpCfgValid_Type.__name__ = "Integer32"
_MefServiceL2cpCfgValid_Object = MibTableColumn
mefServiceL2cpCfgValid = _MefServiceL2cpCfgValid_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 2, 1, 1, 9),
    _MefServiceL2cpCfgValid_Type()
)
mefServiceL2cpCfgValid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceL2cpCfgValid.setStatus("current")
_MefServiceL2cpCfgRowStatus_Type = RowStatus
_MefServiceL2cpCfgRowStatus_Object = MibTableColumn
mefServiceL2cpCfgRowStatus = _MefServiceL2cpCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 2, 1, 1, 10),
    _MefServiceL2cpCfgRowStatus_Type()
)
mefServiceL2cpCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceL2cpCfgRowStatus.setStatus("current")
_MefServiceUniAttributes_ObjectIdentity = ObjectIdentity
mefServiceUniAttributes = _MefServiceUniAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3)
)
_MefServiceUniCfgTable_Object = MibTable
mefServiceUniCfgTable = _MefServiceUniCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    mefServiceUniCfgTable.setStatus("current")
_MefServiceUniCfgEntry_Object = MibTableRow
mefServiceUniCfgEntry = _MefServiceUniCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 1, 1)
)
mefServiceUniCfgEntry.setIndexNames(
    (0, "MEF-UNI-MIB", "mefServiceUniCfgNumber"),
)
if mibBuilder.loadTexts:
    mefServiceUniCfgEntry.setStatus("current")
_MefServiceUniCfgNumber_Type = Unsigned32
_MefServiceUniCfgNumber_Object = MibTableColumn
mefServiceUniCfgNumber = _MefServiceUniCfgNumber_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 1, 1, 1),
    _MefServiceUniCfgNumber_Type()
)
mefServiceUniCfgNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mefServiceUniCfgNumber.setStatus("current")


class _MefServiceUniCfgIdentifier_Type(OctetString):
    """Custom type mefServiceUniCfgIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_MefServiceUniCfgIdentifier_Type.__name__ = "OctetString"
_MefServiceUniCfgIdentifier_Object = MibTableColumn
mefServiceUniCfgIdentifier = _MefServiceUniCfgIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 1, 1, 2),
    _MefServiceUniCfgIdentifier_Type()
)
mefServiceUniCfgIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceUniCfgIdentifier.setStatus("current")


class _MefServiceUniCfgBundlingMultiplex_Type(Integer32):
    """Custom type mefServiceUniCfgBundlingMultiplex based on Integer32"""
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
        *(("allToOne", 1),
          ("bundling", 2),
          ("multiplex", 3),
          ("bundlingMultiplex", 4))
    )


_MefServiceUniCfgBundlingMultiplex_Type.__name__ = "Integer32"
_MefServiceUniCfgBundlingMultiplex_Object = MibTableColumn
mefServiceUniCfgBundlingMultiplex = _MefServiceUniCfgBundlingMultiplex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 1, 1, 3),
    _MefServiceUniCfgBundlingMultiplex_Type()
)
mefServiceUniCfgBundlingMultiplex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceUniCfgBundlingMultiplex.setStatus("current")


class _MefServiceUniCfgCeVidUntagged_Type(Unsigned32):
    """Custom type mefServiceUniCfgCeVidUntagged based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_MefServiceUniCfgCeVidUntagged_Type.__name__ = "Unsigned32"
_MefServiceUniCfgCeVidUntagged_Object = MibTableColumn
mefServiceUniCfgCeVidUntagged = _MefServiceUniCfgCeVidUntagged_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 1, 1, 4),
    _MefServiceUniCfgCeVidUntagged_Type()
)
mefServiceUniCfgCeVidUntagged.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceUniCfgCeVidUntagged.setStatus("current")
_MefServiceEvcPerUniCfgTable_Object = MibTable
mefServiceEvcPerUniCfgTable = _MefServiceEvcPerUniCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    mefServiceEvcPerUniCfgTable.setStatus("current")
_MefServiceEvcPerUniCfgEntry_Object = MibTableRow
mefServiceEvcPerUniCfgEntry = _MefServiceEvcPerUniCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 2, 1)
)
mefServiceEvcPerUniCfgEntry.setIndexNames(
    (0, "MEF-UNI-MIB", "mefServiceUniCfgNumber"),
)
if mibBuilder.loadTexts:
    mefServiceEvcPerUniCfgEntry.setStatus("current")


class _MefServiceEvcPerUniCfgServiceType_Type(Integer32):
    """Custom type mefServiceEvcPerUniCfgServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eLine", 1),
          ("eLan", 2),
          ("eTree", 3))
    )


_MefServiceEvcPerUniCfgServiceType_Type.__name__ = "Integer32"
_MefServiceEvcPerUniCfgServiceType_Object = MibTableColumn
mefServiceEvcPerUniCfgServiceType = _MefServiceEvcPerUniCfgServiceType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 2, 1, 1),
    _MefServiceEvcPerUniCfgServiceType_Type()
)
mefServiceEvcPerUniCfgServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceEvcPerUniCfgServiceType.setStatus("current")


class _MefServiceEvcPerUniCfgServiceSpecific_Type(Integer32):
    """Custom type mefServiceEvcPerUniCfgServiceSpecific based on Integer32"""
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
        *(("epl", 1),
          ("epLan", 2),
          ("epTree", 3),
          ("evpl", 4),
          ("evpLan", 5),
          ("evpTree", 6))
    )


_MefServiceEvcPerUniCfgServiceSpecific_Type.__name__ = "Integer32"
_MefServiceEvcPerUniCfgServiceSpecific_Object = MibTableColumn
mefServiceEvcPerUniCfgServiceSpecific = _MefServiceEvcPerUniCfgServiceSpecific_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 2, 1, 2),
    _MefServiceEvcPerUniCfgServiceSpecific_Type()
)
mefServiceEvcPerUniCfgServiceSpecific.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceEvcPerUniCfgServiceSpecific.setStatus("current")


class _MefServiceEvcPerUniCfgIdentifier_Type(OctetString):
    """Custom type mefServiceEvcPerUniCfgIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 90),
    )


_MefServiceEvcPerUniCfgIdentifier_Type.__name__ = "OctetString"
_MefServiceEvcPerUniCfgIdentifier_Object = MibTableColumn
mefServiceEvcPerUniCfgIdentifier = _MefServiceEvcPerUniCfgIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 2, 1, 3),
    _MefServiceEvcPerUniCfgIdentifier_Type()
)
mefServiceEvcPerUniCfgIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceEvcPerUniCfgIdentifier.setStatus("current")


class _MefServiceEvcPerUniCfgCeVlanMap_Type(OctetString):
    """Custom type mefServiceEvcPerUniCfgCeVlanMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_MefServiceEvcPerUniCfgCeVlanMap_Type.__name__ = "OctetString"
_MefServiceEvcPerUniCfgCeVlanMap_Object = MibTableColumn
mefServiceEvcPerUniCfgCeVlanMap = _MefServiceEvcPerUniCfgCeVlanMap_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 2, 1, 4),
    _MefServiceEvcPerUniCfgCeVlanMap_Type()
)
mefServiceEvcPerUniCfgCeVlanMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceEvcPerUniCfgCeVlanMap.setStatus("current")


class _MefServiceEvcPerUniCfgIngressBwpIndex_Type(Unsigned32):
    """Custom type mefServiceEvcPerUniCfgIngressBwpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_MefServiceEvcPerUniCfgIngressBwpIndex_Type.__name__ = "Unsigned32"
_MefServiceEvcPerUniCfgIngressBwpIndex_Object = MibTableColumn
mefServiceEvcPerUniCfgIngressBwpIndex = _MefServiceEvcPerUniCfgIngressBwpIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 2, 1, 5),
    _MefServiceEvcPerUniCfgIngressBwpIndex_Type()
)
mefServiceEvcPerUniCfgIngressBwpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceEvcPerUniCfgIngressBwpIndex.setStatus("current")


class _MefServiceEvcPerUniCfgIngressCosIndex_Type(Unsigned32):
    """Custom type mefServiceEvcPerUniCfgIngressCosIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_MefServiceEvcPerUniCfgIngressCosIndex_Type.__name__ = "Unsigned32"
_MefServiceEvcPerUniCfgIngressCosIndex_Object = MibTableColumn
mefServiceEvcPerUniCfgIngressCosIndex = _MefServiceEvcPerUniCfgIngressCosIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 2, 1, 6),
    _MefServiceEvcPerUniCfgIngressCosIndex_Type()
)
mefServiceEvcPerUniCfgIngressCosIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceEvcPerUniCfgIngressCosIndex.setStatus("current")


class _MefServiceEvcPerUniCfgEgressBwpIndex_Type(Unsigned32):
    """Custom type mefServiceEvcPerUniCfgEgressBwpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_MefServiceEvcPerUniCfgEgressBwpIndex_Type.__name__ = "Unsigned32"
_MefServiceEvcPerUniCfgEgressBwpIndex_Object = MibTableColumn
mefServiceEvcPerUniCfgEgressBwpIndex = _MefServiceEvcPerUniCfgEgressBwpIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 2, 1, 7),
    _MefServiceEvcPerUniCfgEgressBwpIndex_Type()
)
mefServiceEvcPerUniCfgEgressBwpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceEvcPerUniCfgEgressBwpIndex.setStatus("current")


class _MefServiceEvcPerUniCfgEgressCosIndex_Type(Unsigned32):
    """Custom type mefServiceEvcPerUniCfgEgressCosIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_MefServiceEvcPerUniCfgEgressCosIndex_Type.__name__ = "Unsigned32"
_MefServiceEvcPerUniCfgEgressCosIndex_Object = MibTableColumn
mefServiceEvcPerUniCfgEgressCosIndex = _MefServiceEvcPerUniCfgEgressCosIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 3, 2, 1, 8),
    _MefServiceEvcPerUniCfgEgressCosIndex_Type()
)
mefServiceEvcPerUniCfgEgressCosIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceEvcPerUniCfgEgressCosIndex.setStatus("current")
_MefServiceBwpAttributes_ObjectIdentity = ObjectIdentity
mefServiceBwpAttributes = _MefServiceBwpAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4)
)
_MefServiceBwpNextIndex_Type = Unsigned32
_MefServiceBwpNextIndex_Object = MibScalar
mefServiceBwpNextIndex = _MefServiceBwpNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 1),
    _MefServiceBwpNextIndex_Type()
)
mefServiceBwpNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceBwpNextIndex.setStatus("current")
_MefServiceBwpCfgTable_Object = MibTable
mefServiceBwpCfgTable = _MefServiceBwpCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    mefServiceBwpCfgTable.setStatus("current")
_MefServiceBwpCfgEntry_Object = MibTableRow
mefServiceBwpCfgEntry = _MefServiceBwpCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 2, 1)
)
mefServiceBwpCfgEntry.setIndexNames(
    (0, "MEF-UNI-MIB", "mefServiceBwpCfgIndex"),
)
if mibBuilder.loadTexts:
    mefServiceBwpCfgEntry.setStatus("current")
_MefServiceBwpCfgIndex_Type = Unsigned32
_MefServiceBwpCfgIndex_Object = MibTableColumn
mefServiceBwpCfgIndex = _MefServiceBwpCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 2, 1, 1),
    _MefServiceBwpCfgIndex_Type()
)
mefServiceBwpCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mefServiceBwpCfgIndex.setStatus("current")


class _MefServiceBwpCfgIdentifier_Type(OctetString):
    """Custom type mefServiceBwpCfgIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 45),
    )


_MefServiceBwpCfgIdentifier_Type.__name__ = "OctetString"
_MefServiceBwpCfgIdentifier_Object = MibTableColumn
mefServiceBwpCfgIdentifier = _MefServiceBwpCfgIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 2, 1, 2),
    _MefServiceBwpCfgIdentifier_Type()
)
mefServiceBwpCfgIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceBwpCfgIdentifier.setStatus("current")


class _MefServiceBwpCfgType_Type(Integer32):
    """Custom type mefServiceBwpCfgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 1),
          ("egress", 2))
    )


_MefServiceBwpCfgType_Type.__name__ = "Integer32"
_MefServiceBwpCfgType_Object = MibTableColumn
mefServiceBwpCfgType = _MefServiceBwpCfgType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 2, 1, 3),
    _MefServiceBwpCfgType_Type()
)
mefServiceBwpCfgType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceBwpCfgType.setStatus("current")


class _MefServiceBwpCfgRateType_Type(Integer32):
    """Custom type mefServiceBwpCfgRateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("l1", 1),
          ("l2", 2))
    )


_MefServiceBwpCfgRateType_Type.__name__ = "Integer32"
_MefServiceBwpCfgRateType_Object = MibTableColumn
mefServiceBwpCfgRateType = _MefServiceBwpCfgRateType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 2, 1, 4),
    _MefServiceBwpCfgRateType_Type()
)
mefServiceBwpCfgRateType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceBwpCfgRateType.setStatus("current")


class _MefServiceBwpCfgCir_Type(Unsigned32):
    """Custom type mefServiceBwpCfgCir based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000000),
    )


_MefServiceBwpCfgCir_Type.__name__ = "Unsigned32"
_MefServiceBwpCfgCir_Object = MibTableColumn
mefServiceBwpCfgCir = _MefServiceBwpCfgCir_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 2, 1, 5),
    _MefServiceBwpCfgCir_Type()
)
mefServiceBwpCfgCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceBwpCfgCir.setStatus("current")


class _MefServiceBwpCfgCbs_Type(Unsigned32):
    """Custom type mefServiceBwpCfgCbs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_MefServiceBwpCfgCbs_Type.__name__ = "Unsigned32"
_MefServiceBwpCfgCbs_Object = MibTableColumn
mefServiceBwpCfgCbs = _MefServiceBwpCfgCbs_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 2, 1, 6),
    _MefServiceBwpCfgCbs_Type()
)
mefServiceBwpCfgCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceBwpCfgCbs.setStatus("current")


class _MefServiceBwpCfgEir_Type(Unsigned32):
    """Custom type mefServiceBwpCfgEir based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000000),
    )


_MefServiceBwpCfgEir_Type.__name__ = "Unsigned32"
_MefServiceBwpCfgEir_Object = MibTableColumn
mefServiceBwpCfgEir = _MefServiceBwpCfgEir_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 2, 1, 7),
    _MefServiceBwpCfgEir_Type()
)
mefServiceBwpCfgEir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceBwpCfgEir.setStatus("current")


class _MefServiceBwpCfgEbs_Type(Unsigned32):
    """Custom type mefServiceBwpCfgEbs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_MefServiceBwpCfgEbs_Type.__name__ = "Unsigned32"
_MefServiceBwpCfgEbs_Object = MibTableColumn
mefServiceBwpCfgEbs = _MefServiceBwpCfgEbs_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 2, 1, 8),
    _MefServiceBwpCfgEbs_Type()
)
mefServiceBwpCfgEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceBwpCfgEbs.setStatus("current")


class _MefServiceBwpCfgCm_Type(Integer32):
    """Custom type mefServiceBwpCfgCm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("colorBlind", 1),
          ("colorAware", 2))
    )


_MefServiceBwpCfgCm_Type.__name__ = "Integer32"
_MefServiceBwpCfgCm_Object = MibTableColumn
mefServiceBwpCfgCm = _MefServiceBwpCfgCm_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 2, 1, 9),
    _MefServiceBwpCfgCm_Type()
)
mefServiceBwpCfgCm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceBwpCfgCm.setStatus("current")


class _MefServiceBwpCfgCf_Type(Integer32):
    """Custom type mefServiceBwpCfgCf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("couplingYellowEirOnly", 1),
          ("couplingYellowEirPlusCir", 2))
    )


_MefServiceBwpCfgCf_Type.__name__ = "Integer32"
_MefServiceBwpCfgCf_Object = MibTableColumn
mefServiceBwpCfgCf = _MefServiceBwpCfgCf_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 2, 1, 10),
    _MefServiceBwpCfgCf_Type()
)
mefServiceBwpCfgCf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceBwpCfgCf.setStatus("current")
_MefServiceBwpCfgRowStatus_Type = RowStatus
_MefServiceBwpCfgRowStatus_Object = MibTableColumn
mefServiceBwpCfgRowStatus = _MefServiceBwpCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 4, 2, 1, 11),
    _MefServiceBwpCfgRowStatus_Type()
)
mefServiceBwpCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceBwpCfgRowStatus.setStatus("current")
_MefServiceCosAttributes_ObjectIdentity = ObjectIdentity
mefServiceCosAttributes = _MefServiceCosAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 5)
)
_MefServiceCosNextIndex_Type = Unsigned32
_MefServiceCosNextIndex_Object = MibScalar
mefServiceCosNextIndex = _MefServiceCosNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 5, 1),
    _MefServiceCosNextIndex_Type()
)
mefServiceCosNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceCosNextIndex.setStatus("current")
_MefServiceCosCfgTable_Object = MibTable
mefServiceCosCfgTable = _MefServiceCosCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 5, 2)
)
if mibBuilder.loadTexts:
    mefServiceCosCfgTable.setStatus("current")
_MefServiceCosCfgEntry_Object = MibTableRow
mefServiceCosCfgEntry = _MefServiceCosCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 5, 2, 1)
)
mefServiceCosCfgEntry.setIndexNames(
    (0, "MEF-UNI-MIB", "mefServiceCosCfgIndex"),
)
if mibBuilder.loadTexts:
    mefServiceCosCfgEntry.setStatus("current")
_MefServiceCosCfgIndex_Type = Unsigned32
_MefServiceCosCfgIndex_Object = MibTableColumn
mefServiceCosCfgIndex = _MefServiceCosCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 5, 2, 1, 1),
    _MefServiceCosCfgIndex_Type()
)
mefServiceCosCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mefServiceCosCfgIndex.setStatus("current")


class _MefServiceCosCfgIdentifier_Type(OctetString):
    """Custom type mefServiceCosCfgIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 45),
    )


_MefServiceCosCfgIdentifier_Type.__name__ = "OctetString"
_MefServiceCosCfgIdentifier_Object = MibTableColumn
mefServiceCosCfgIdentifier = _MefServiceCosCfgIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 5, 2, 1, 2),
    _MefServiceCosCfgIdentifier_Type()
)
mefServiceCosCfgIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceCosCfgIdentifier.setStatus("current")


class _MefServiceCosCfgType_Type(Integer32):
    """Custom type mefServiceCosCfgType based on Integer32"""
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
        *(("uni", 1),
          ("evc", 2),
          ("pcp", 3),
          ("dscp", 4),
          ("l2cp", 5))
    )


_MefServiceCosCfgType_Type.__name__ = "Integer32"
_MefServiceCosCfgType_Object = MibTableColumn
mefServiceCosCfgType = _MefServiceCosCfgType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 5, 2, 1, 3),
    _MefServiceCosCfgType_Type()
)
mefServiceCosCfgType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceCosCfgType.setStatus("current")


class _MefServiceCosCfgIdentifierList_Type(OctetString):
    """Custom type mefServiceCosCfgIdentifierList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_MefServiceCosCfgIdentifierList_Type.__name__ = "OctetString"
_MefServiceCosCfgIdentifierList_Object = MibTableColumn
mefServiceCosCfgIdentifierList = _MefServiceCosCfgIdentifierList_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 5, 2, 1, 4),
    _MefServiceCosCfgIdentifierList_Type()
)
mefServiceCosCfgIdentifierList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceCosCfgIdentifierList.setStatus("current")
_MefServiceCosCfgRowStatus_Type = RowStatus
_MefServiceCosCfgRowStatus_Object = MibTableColumn
mefServiceCosCfgRowStatus = _MefServiceCosCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 5, 2, 1, 5),
    _MefServiceCosCfgRowStatus_Type()
)
mefServiceCosCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceCosCfgRowStatus.setStatus("current")
_MefServiceNotificationCfg_ObjectIdentity = ObjectIdentity
mefServiceNotificationCfg = _MefServiceNotificationCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 6)
)
_MefServiceNotificationObj_ObjectIdentity = ObjectIdentity
mefServiceNotificationObj = _MefServiceNotificationObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 1, 7)
)
_MefServiceMibConformance_ObjectIdentity = ObjectIdentity
mefServiceMibConformance = _MefServiceMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 2)
)
_MefServiceUniMibCompliances_ObjectIdentity = ObjectIdentity
mefServiceUniMibCompliances = _MefServiceUniMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 2, 1)
)
_MefServiceUniMibGroups_ObjectIdentity = ObjectIdentity
mefServiceUniMibGroups = _MefServiceUniMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 2, 2)
)

# Managed Objects groups

mefServiceInterfaceUniMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 2, 2, 1)
)
mefServiceInterfaceUniMandatoryGroup.setObjects(
      *(("MEF-UNI-MIB", "mefServiceInterfaceCfgType"),
        ("MEF-UNI-MIB", "mefServiceInterfaceCfgIdentifier"),
        ("MEF-UNI-MIB", "mefServiceInterfaceCfgSpeed"),
        ("MEF-UNI-MIB", "mefServiceInterfaceCfgMode"),
        ("MEF-UNI-MIB", "mefServiceInterfaceCfgNegotiate"),
        ("MEF-UNI-MIB", "mefServiceInterfaceCfgFrameFormat"),
        ("MEF-UNI-MIB", "mefServiceInterfaceCfgMtuSize"),
        ("MEF-UNI-MIB", "mefServiceInterfaceCfgIngressBwpIndex"),
        ("MEF-UNI-MIB", "mefServiceInterfaceCfgEgressBwpIndex"),
        ("MEF-UNI-MIB", "mefServiceInterfaceStatusType"),
        ("MEF-UNI-MIB", "mefServiceInterfaceStatusPhysicalLayer"),
        ("MEF-UNI-MIB", "mefServiceInterfaceStatusSpeed"),
        ("MEF-UNI-MIB", "mefServiceInterfaceStatusMode"),
        ("MEF-UNI-MIB", "mefServiceInterfaceStatusMaxMtuSize"),
        ("MEF-UNI-MIB", "mefServiceInterfaceStatusMaxVc"),
        ("MEF-UNI-MIB", "mefServiceInterfaceStatusMaxEndPointPerVc"),
        ("MEF-UNI-MIB", "mefServiceL2cpCfgType"),
        ("MEF-UNI-MIB", "mefServiceL2cpCfgMatchScope"),
        ("MEF-UNI-MIB", "mefServiceL2cpCfgMacAddress"),
        ("MEF-UNI-MIB", "mefServiceL2cpCfgProtocol"),
        ("MEF-UNI-MIB", "mefServiceL2cpCfgSubType"),
        ("MEF-UNI-MIB", "mefServiceL2cpCfgEvcName"),
        ("MEF-UNI-MIB", "mefServiceL2cpCfgValid"),
        ("MEF-UNI-MIB", "mefServiceL2cpCfgRowStatus"),
        ("MEF-UNI-MIB", "mefServiceUniCfgIdentifier"),
        ("MEF-UNI-MIB", "mefServiceUniCfgBundlingMultiplex"),
        ("MEF-UNI-MIB", "mefServiceUniCfgCeVidUntagged"),
        ("MEF-UNI-MIB", "mefServiceEvcPerUniCfgServiceType"),
        ("MEF-UNI-MIB", "mefServiceEvcPerUniCfgServiceSpecific"),
        ("MEF-UNI-MIB", "mefServiceEvcPerUniCfgIdentifier"),
        ("MEF-UNI-MIB", "mefServiceEvcPerUniCfgCeVlanMap"),
        ("MEF-UNI-MIB", "mefServiceEvcPerUniCfgIngressBwpIndex"),
        ("MEF-UNI-MIB", "mefServiceEvcPerUniCfgIngressCosIndex"),
        ("MEF-UNI-MIB", "mefServiceEvcPerUniCfgEgressBwpIndex"),
        ("MEF-UNI-MIB", "mefServiceEvcPerUniCfgEgressCosIndex"),
        ("MEF-UNI-MIB", "mefServiceBwpNextIndex"),
        ("MEF-UNI-MIB", "mefServiceBwpCfgType"),
        ("MEF-UNI-MIB", "mefServiceBwpCfgIdentifier"),
        ("MEF-UNI-MIB", "mefServiceBwpCfgRateType"),
        ("MEF-UNI-MIB", "mefServiceBwpCfgCir"),
        ("MEF-UNI-MIB", "mefServiceBwpCfgCbs"),
        ("MEF-UNI-MIB", "mefServiceBwpCfgEir"),
        ("MEF-UNI-MIB", "mefServiceBwpCfgEbs"),
        ("MEF-UNI-MIB", "mefServiceBwpCfgCm"),
        ("MEF-UNI-MIB", "mefServiceBwpCfgCf"),
        ("MEF-UNI-MIB", "mefServiceBwpCfgRowStatus"),
        ("MEF-UNI-MIB", "mefServiceCosNextIndex"),
        ("MEF-UNI-MIB", "mefServiceCosCfgIdentifier"),
        ("MEF-UNI-MIB", "mefServiceCosCfgType"),
        ("MEF-UNI-MIB", "mefServiceCosCfgIdentifierList"),
        ("MEF-UNI-MIB", "mefServiceCosCfgRowStatus"))
)
if mibBuilder.loadTexts:
    mefServiceInterfaceUniMandatoryGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mefServiceUniMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 15007, 2, 2, 2, 1, 1)
)
mefServiceUniMibCompliance.setObjects(
    ("MEF-UNI-MIB", "mefServiceInterfaceUniMandatoryGroup")
)
if mibBuilder.loadTexts:
    mefServiceUniMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MEF-UNI-MIB",
    **{"mefUniMib": mefUniMib,
       "mefServiceNotifications": mefServiceNotifications,
       "mefServiceInterfaceObjects": mefServiceInterfaceObjects,
       "mefServiceInterface": mefServiceInterface,
       "mefServiceInterfaceCfgTable": mefServiceInterfaceCfgTable,
       "mefServiceInterfaceCfgEntry": mefServiceInterfaceCfgEntry,
       "mefServiceInterfaceCfgNumber": mefServiceInterfaceCfgNumber,
       "mefServiceInterfaceCfgType": mefServiceInterfaceCfgType,
       "mefServiceInterfaceCfgIdentifier": mefServiceInterfaceCfgIdentifier,
       "mefServiceInterfaceCfgSpeed": mefServiceInterfaceCfgSpeed,
       "mefServiceInterfaceCfgMode": mefServiceInterfaceCfgMode,
       "mefServiceInterfaceCfgNegotiate": mefServiceInterfaceCfgNegotiate,
       "mefServiceInterfaceCfgFrameFormat": mefServiceInterfaceCfgFrameFormat,
       "mefServiceInterfaceCfgMtuSize": mefServiceInterfaceCfgMtuSize,
       "mefServiceInterfaceCfgIngressBwpIndex": mefServiceInterfaceCfgIngressBwpIndex,
       "mefServiceInterfaceCfgEgressBwpIndex": mefServiceInterfaceCfgEgressBwpIndex,
       "mefServiceInterfaceStatusTable": mefServiceInterfaceStatusTable,
       "mefServiceInterfaceStatusEntry": mefServiceInterfaceStatusEntry,
       "mefServiceInterfaceStatusNumber": mefServiceInterfaceStatusNumber,
       "mefServiceInterfaceStatusType": mefServiceInterfaceStatusType,
       "mefServiceInterfaceStatusPhysicalLayer": mefServiceInterfaceStatusPhysicalLayer,
       "mefServiceInterfaceStatusSpeed": mefServiceInterfaceStatusSpeed,
       "mefServiceInterfaceStatusMode": mefServiceInterfaceStatusMode,
       "mefServiceInterfaceStatusMaxMtuSize": mefServiceInterfaceStatusMaxMtuSize,
       "mefServiceInterfaceStatusMaxVc": mefServiceInterfaceStatusMaxVc,
       "mefServiceInterfaceStatusMaxEndPointPerVc": mefServiceInterfaceStatusMaxEndPointPerVc,
       "mefServiceInterfaceL2cp": mefServiceInterfaceL2cp,
       "mefServiceL2cpCfgTable": mefServiceL2cpCfgTable,
       "mefServiceL2cpCfgEntry": mefServiceL2cpCfgEntry,
       "mefServiceL2cpCfgInterfaceNumber": mefServiceL2cpCfgInterfaceNumber,
       "mefServiceL2cpCfgIndex": mefServiceL2cpCfgIndex,
       "mefServiceL2cpCfgType": mefServiceL2cpCfgType,
       "mefServiceL2cpCfgMatchScope": mefServiceL2cpCfgMatchScope,
       "mefServiceL2cpCfgMacAddress": mefServiceL2cpCfgMacAddress,
       "mefServiceL2cpCfgProtocol": mefServiceL2cpCfgProtocol,
       "mefServiceL2cpCfgSubType": mefServiceL2cpCfgSubType,
       "mefServiceL2cpCfgEvcName": mefServiceL2cpCfgEvcName,
       "mefServiceL2cpCfgValid": mefServiceL2cpCfgValid,
       "mefServiceL2cpCfgRowStatus": mefServiceL2cpCfgRowStatus,
       "mefServiceUniAttributes": mefServiceUniAttributes,
       "mefServiceUniCfgTable": mefServiceUniCfgTable,
       "mefServiceUniCfgEntry": mefServiceUniCfgEntry,
       "mefServiceUniCfgNumber": mefServiceUniCfgNumber,
       "mefServiceUniCfgIdentifier": mefServiceUniCfgIdentifier,
       "mefServiceUniCfgBundlingMultiplex": mefServiceUniCfgBundlingMultiplex,
       "mefServiceUniCfgCeVidUntagged": mefServiceUniCfgCeVidUntagged,
       "mefServiceEvcPerUniCfgTable": mefServiceEvcPerUniCfgTable,
       "mefServiceEvcPerUniCfgEntry": mefServiceEvcPerUniCfgEntry,
       "mefServiceEvcPerUniCfgServiceType": mefServiceEvcPerUniCfgServiceType,
       "mefServiceEvcPerUniCfgServiceSpecific": mefServiceEvcPerUniCfgServiceSpecific,
       "mefServiceEvcPerUniCfgIdentifier": mefServiceEvcPerUniCfgIdentifier,
       "mefServiceEvcPerUniCfgCeVlanMap": mefServiceEvcPerUniCfgCeVlanMap,
       "mefServiceEvcPerUniCfgIngressBwpIndex": mefServiceEvcPerUniCfgIngressBwpIndex,
       "mefServiceEvcPerUniCfgIngressCosIndex": mefServiceEvcPerUniCfgIngressCosIndex,
       "mefServiceEvcPerUniCfgEgressBwpIndex": mefServiceEvcPerUniCfgEgressBwpIndex,
       "mefServiceEvcPerUniCfgEgressCosIndex": mefServiceEvcPerUniCfgEgressCosIndex,
       "mefServiceBwpAttributes": mefServiceBwpAttributes,
       "mefServiceBwpNextIndex": mefServiceBwpNextIndex,
       "mefServiceBwpCfgTable": mefServiceBwpCfgTable,
       "mefServiceBwpCfgEntry": mefServiceBwpCfgEntry,
       "mefServiceBwpCfgIndex": mefServiceBwpCfgIndex,
       "mefServiceBwpCfgIdentifier": mefServiceBwpCfgIdentifier,
       "mefServiceBwpCfgType": mefServiceBwpCfgType,
       "mefServiceBwpCfgRateType": mefServiceBwpCfgRateType,
       "mefServiceBwpCfgCir": mefServiceBwpCfgCir,
       "mefServiceBwpCfgCbs": mefServiceBwpCfgCbs,
       "mefServiceBwpCfgEir": mefServiceBwpCfgEir,
       "mefServiceBwpCfgEbs": mefServiceBwpCfgEbs,
       "mefServiceBwpCfgCm": mefServiceBwpCfgCm,
       "mefServiceBwpCfgCf": mefServiceBwpCfgCf,
       "mefServiceBwpCfgRowStatus": mefServiceBwpCfgRowStatus,
       "mefServiceCosAttributes": mefServiceCosAttributes,
       "mefServiceCosNextIndex": mefServiceCosNextIndex,
       "mefServiceCosCfgTable": mefServiceCosCfgTable,
       "mefServiceCosCfgEntry": mefServiceCosCfgEntry,
       "mefServiceCosCfgIndex": mefServiceCosCfgIndex,
       "mefServiceCosCfgIdentifier": mefServiceCosCfgIdentifier,
       "mefServiceCosCfgType": mefServiceCosCfgType,
       "mefServiceCosCfgIdentifierList": mefServiceCosCfgIdentifierList,
       "mefServiceCosCfgRowStatus": mefServiceCosCfgRowStatus,
       "mefServiceNotificationCfg": mefServiceNotificationCfg,
       "mefServiceNotificationObj": mefServiceNotificationObj,
       "mefServiceMibConformance": mefServiceMibConformance,
       "mefServiceUniMibCompliances": mefServiceUniMibCompliances,
       "mefServiceUniMibCompliance": mefServiceUniMibCompliance,
       "mefServiceUniMibGroups": mefServiceUniMibGroups,
       "mefServiceInterfaceUniMandatoryGroup": mefServiceInterfaceUniMandatoryGroup}
)
