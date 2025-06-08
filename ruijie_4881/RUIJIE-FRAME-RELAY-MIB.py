# SNMP MIB module (RUIJIE-FRAME-RELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-FRAME-RELAY-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:21 2025
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

(frCircuitDlci,
 frCircuitEntry,
 frCircuitIfIndex,
 frDlcmiEntry) = mibBuilder.importSymbols(
    "FRAME-RELAY-DTE-MIB",
    "frCircuitDlci",
    "frCircuitEntry",
    "frCircuitIfIndex",
    "frDlcmiEntry")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruijieFrameRelayMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50)
)
if mibBuilder.loadTexts:
    ruijieFrameRelayMIB.setRevisions(
        ("2000-10-13 00:00",
         "2000-05-22 00:00",
         "2000-05-16 00:00",
         "2009-05-18 00:00",
         "1999-08-21 00:00",
         "1996-08-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DlciNumber(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )



class RuijiefrMapProtocols(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              7,
              10,
              11,
              12,
              13,
              16,
              18,
              22,
              25,
              37,
              38,
              39,
              40,
              47,
              48,
              49,
              53,
              63,
              74,
              83,
              999)
        )
    )
    namedValues = NamedValues(
        *(("arp", 1),
          ("serialArp", 6),
          ("ip", 7),
          ("xns", 10),
          ("novell", 11),
          ("apollo", 12),
          ("vines", 13),
          ("appletalk", 16),
          ("ieeeSpanning", 18),
          ("decnet", 22),
          ("clns", 25),
          ("rsrb", 37),
          ("bridge", 38),
          ("stun", 39),
          ("frArp", 40),
          ("uncompressedTcp", 47),
          ("compressedTcp", 48),
          ("llc2", 49),
          ("frSwitch", 53),
          ("dlsw", 63),
          ("nhrp", 74),
          ("compressedRtp", 83),
          ("wildcard", 999))
    )



# MIB Managed Objects in the order of their OIDs

_RuijieFrMIBObjects_ObjectIdentity = ObjectIdentity
ruijieFrMIBObjects = _RuijieFrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1)
)
_RuijiefrLmiObjs_ObjectIdentity = ObjectIdentity
ruijiefrLmiObjs = _RuijiefrLmiObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 1)
)
_RuijiefrLmiTable_Object = MibTable
ruijiefrLmiTable = _RuijiefrLmiTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ruijiefrLmiTable.setStatus("current")
_RuijiefrLmiEntry_Object = MibTableRow
ruijiefrLmiEntry = _RuijiefrLmiEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ruijiefrLmiEntry.setStatus("current")


class _RuijiefrLmiLinkstatus_Type(Integer32):
    """Custom type ruijiefrLmiLinkstatus based on Integer32"""
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


_RuijiefrLmiLinkstatus_Type.__name__ = "Integer32"
_RuijiefrLmiLinkstatus_Object = MibTableColumn
ruijiefrLmiLinkstatus = _RuijiefrLmiLinkstatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 1, 1, 1, 1),
    _RuijiefrLmiLinkstatus_Type()
)
ruijiefrLmiLinkstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrLmiLinkstatus.setStatus("current")


class _RuijiefrLmiLinkType_Type(Integer32):
    """Custom type ruijiefrLmiLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dte", 1),
          ("dce", 2),
          ("nni", 3))
    )


_RuijiefrLmiLinkType_Type.__name__ = "Integer32"
_RuijiefrLmiLinkType_Object = MibTableColumn
ruijiefrLmiLinkType = _RuijiefrLmiLinkType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 1, 1, 1, 2),
    _RuijiefrLmiLinkType_Type()
)
ruijiefrLmiLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrLmiLinkType.setStatus("current")
_RuijiefrLmiEnquiryIns_Type = Counter32
_RuijiefrLmiEnquiryIns_Object = MibTableColumn
ruijiefrLmiEnquiryIns = _RuijiefrLmiEnquiryIns_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 1, 1, 1, 3),
    _RuijiefrLmiEnquiryIns_Type()
)
ruijiefrLmiEnquiryIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrLmiEnquiryIns.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrLmiEnquiryIns.setUnits("messages")
_RuijiefrLmiEnquiryOuts_Type = Counter32
_RuijiefrLmiEnquiryOuts_Object = MibTableColumn
ruijiefrLmiEnquiryOuts = _RuijiefrLmiEnquiryOuts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 1, 1, 1, 4),
    _RuijiefrLmiEnquiryOuts_Type()
)
ruijiefrLmiEnquiryOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrLmiEnquiryOuts.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrLmiEnquiryOuts.setUnits("messages")
_RuijiefrLmiStatusIns_Type = Counter32
_RuijiefrLmiStatusIns_Object = MibTableColumn
ruijiefrLmiStatusIns = _RuijiefrLmiStatusIns_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 1, 1, 1, 5),
    _RuijiefrLmiStatusIns_Type()
)
ruijiefrLmiStatusIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrLmiStatusIns.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrLmiStatusIns.setUnits("messages")
_RuijiefrLmiStatusOuts_Type = Counter32
_RuijiefrLmiStatusOuts_Object = MibTableColumn
ruijiefrLmiStatusOuts = _RuijiefrLmiStatusOuts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 1, 1, 1, 6),
    _RuijiefrLmiStatusOuts_Type()
)
ruijiefrLmiStatusOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrLmiStatusOuts.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrLmiStatusOuts.setUnits("messages")
_RuijiefrLmiUpdateStatusIns_Type = Counter32
_RuijiefrLmiUpdateStatusIns_Object = MibTableColumn
ruijiefrLmiUpdateStatusIns = _RuijiefrLmiUpdateStatusIns_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 1, 1, 1, 7),
    _RuijiefrLmiUpdateStatusIns_Type()
)
ruijiefrLmiUpdateStatusIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrLmiUpdateStatusIns.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrLmiUpdateStatusIns.setUnits("messages")
_RuijiefrLmiUpdateStatusOuts_Type = Counter32
_RuijiefrLmiUpdateStatusOuts_Object = MibTableColumn
ruijiefrLmiUpdateStatusOuts = _RuijiefrLmiUpdateStatusOuts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 1, 1, 1, 8),
    _RuijiefrLmiUpdateStatusOuts_Type()
)
ruijiefrLmiUpdateStatusOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrLmiUpdateStatusOuts.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrLmiUpdateStatusOuts.setUnits("messages")
_RuijiefrLmiStatusTimeouts_Type = Counter32
_RuijiefrLmiStatusTimeouts_Object = MibTableColumn
ruijiefrLmiStatusTimeouts = _RuijiefrLmiStatusTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 1, 1, 1, 9),
    _RuijiefrLmiStatusTimeouts_Type()
)
ruijiefrLmiStatusTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrLmiStatusTimeouts.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrLmiStatusTimeouts.setUnits("times")
_RuijiefrLmiStatusEnqTimeouts_Type = Counter32
_RuijiefrLmiStatusEnqTimeouts_Object = MibTableColumn
ruijiefrLmiStatusEnqTimeouts = _RuijiefrLmiStatusEnqTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 1, 1, 1, 10),
    _RuijiefrLmiStatusEnqTimeouts_Type()
)
ruijiefrLmiStatusEnqTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrLmiStatusEnqTimeouts.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrLmiStatusEnqTimeouts.setUnits("times")


class _RuijiefrLmiN392Dce_Type(Integer32):
    """Custom type ruijiefrLmiN392Dce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_RuijiefrLmiN392Dce_Type.__name__ = "Integer32"
_RuijiefrLmiN392Dce_Object = MibTableColumn
ruijiefrLmiN392Dce = _RuijiefrLmiN392Dce_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 1, 1, 1, 11),
    _RuijiefrLmiN392Dce_Type()
)
ruijiefrLmiN392Dce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrLmiN392Dce.setStatus("current")


class _RuijiefrLmiN393Dce_Type(Integer32):
    """Custom type ruijiefrLmiN393Dce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_RuijiefrLmiN393Dce_Type.__name__ = "Integer32"
_RuijiefrLmiN393Dce_Object = MibTableColumn
ruijiefrLmiN393Dce = _RuijiefrLmiN393Dce_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 1, 1, 1, 12),
    _RuijiefrLmiN393Dce_Type()
)
ruijiefrLmiN393Dce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrLmiN393Dce.setStatus("current")


class _RuijiefrLmiT392Dce_Type(Integer32):
    """Custom type ruijiefrLmiT392Dce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_RuijiefrLmiT392Dce_Type.__name__ = "Integer32"
_RuijiefrLmiT392Dce_Object = MibTableColumn
ruijiefrLmiT392Dce = _RuijiefrLmiT392Dce_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 1, 1, 1, 13),
    _RuijiefrLmiT392Dce_Type()
)
ruijiefrLmiT392Dce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrLmiT392Dce.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrLmiT392Dce.setUnits("seconds")
_RuijiefrCircuitObjs_ObjectIdentity = ObjectIdentity
ruijiefrCircuitObjs = _RuijiefrCircuitObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 2)
)
_RuijiefrCircuitTable_Object = MibTable
ruijiefrCircuitTable = _RuijiefrCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ruijiefrCircuitTable.setStatus("current")
_RuijiefrCircuitEntry_Object = MibTableRow
ruijiefrCircuitEntry = _RuijiefrCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ruijiefrCircuitEntry.setStatus("current")
_RuijiefrCircuitDEins_Type = Counter32
_RuijiefrCircuitDEins_Object = MibTableColumn
ruijiefrCircuitDEins = _RuijiefrCircuitDEins_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 2, 1, 1, 1),
    _RuijiefrCircuitDEins_Type()
)
ruijiefrCircuitDEins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrCircuitDEins.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrCircuitDEins.setUnits("packets")
_RuijiefrCircuitDEouts_Type = Counter32
_RuijiefrCircuitDEouts_Object = MibTableColumn
ruijiefrCircuitDEouts = _RuijiefrCircuitDEouts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 2, 1, 1, 2),
    _RuijiefrCircuitDEouts_Type()
)
ruijiefrCircuitDEouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrCircuitDEouts.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrCircuitDEouts.setUnits("packets")
_RuijiefrCircuitDropPktsOuts_Type = Counter32
_RuijiefrCircuitDropPktsOuts_Object = MibTableColumn
ruijiefrCircuitDropPktsOuts = _RuijiefrCircuitDropPktsOuts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 2, 1, 1, 3),
    _RuijiefrCircuitDropPktsOuts_Type()
)
ruijiefrCircuitDropPktsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrCircuitDropPktsOuts.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrCircuitDropPktsOuts.setUnits("packets")


class _RuijiefrCircuitType_Type(Integer32):
    """Custom type ruijiefrCircuitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 1),
          ("svc", 2))
    )


_RuijiefrCircuitType_Type.__name__ = "Integer32"
_RuijiefrCircuitType_Object = MibTableColumn
ruijiefrCircuitType = _RuijiefrCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 2, 1, 1, 4),
    _RuijiefrCircuitType_Type()
)
ruijiefrCircuitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrCircuitType.setStatus("current")
_RuijiefrExtCircuitTable_Object = MibTable
ruijiefrExtCircuitTable = _RuijiefrExtCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ruijiefrExtCircuitTable.setStatus("current")
_RuijiefrExtCircuitEntry_Object = MibTableRow
ruijiefrExtCircuitEntry = _RuijiefrExtCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ruijiefrExtCircuitEntry.setStatus("current")
_RuijiefrExtCircuitIfName_Type = DisplayString
_RuijiefrExtCircuitIfName_Object = MibTableColumn
ruijiefrExtCircuitIfName = _RuijiefrExtCircuitIfName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 2, 2, 1, 1),
    _RuijiefrExtCircuitIfName_Type()
)
ruijiefrExtCircuitIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitIfName.setStatus("current")


class _RuijiefrExtCircuitIfType_Type(Integer32):
    """Custom type ruijiefrExtCircuitIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mainInterface", 1),
          ("pointToPoint", 2),
          ("multipoint", 3))
    )


_RuijiefrExtCircuitIfType_Type.__name__ = "Integer32"
_RuijiefrExtCircuitIfType_Object = MibTableColumn
ruijiefrExtCircuitIfType = _RuijiefrExtCircuitIfType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 2, 2, 1, 2),
    _RuijiefrExtCircuitIfType_Type()
)
ruijiefrExtCircuitIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitIfType.setStatus("current")
_RuijiefrExtCircuitSubifIndex_Type = InterfaceIndex
_RuijiefrExtCircuitSubifIndex_Object = MibTableColumn
ruijiefrExtCircuitSubifIndex = _RuijiefrExtCircuitSubifIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 2, 2, 1, 3),
    _RuijiefrExtCircuitSubifIndex_Type()
)
ruijiefrExtCircuitSubifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitSubifIndex.setStatus("current")


class _RuijiefrExtCircuitMapStatus_Type(Integer32):
    """Custom type ruijiefrExtCircuitMapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_RuijiefrExtCircuitMapStatus_Type.__name__ = "Integer32"
_RuijiefrExtCircuitMapStatus_Object = MibTableColumn
ruijiefrExtCircuitMapStatus = _RuijiefrExtCircuitMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 2, 2, 1, 4),
    _RuijiefrExtCircuitMapStatus_Type()
)
ruijiefrExtCircuitMapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitMapStatus.setStatus("current")


class _RuijiefrExtCircuitCreateType_Type(Integer32):
    """Custom type ruijiefrExtCircuitCreateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_RuijiefrExtCircuitCreateType_Type.__name__ = "Integer32"
_RuijiefrExtCircuitCreateType_Object = MibTableColumn
ruijiefrExtCircuitCreateType = _RuijiefrExtCircuitCreateType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 2, 2, 1, 5),
    _RuijiefrExtCircuitCreateType_Type()
)
ruijiefrExtCircuitCreateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitCreateType.setStatus("current")
_RuijiefrExtCircuitMulticast_Type = TruthValue
_RuijiefrExtCircuitMulticast_Object = MibTableColumn
ruijiefrExtCircuitMulticast = _RuijiefrExtCircuitMulticast_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 2, 2, 1, 6),
    _RuijiefrExtCircuitMulticast_Type()
)
ruijiefrExtCircuitMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitMulticast.setStatus("current")
_RuijiefrExtCircuitRoutedDlci_Type = DlciNumber
_RuijiefrExtCircuitRoutedDlci_Object = MibTableColumn
ruijiefrExtCircuitRoutedDlci = _RuijiefrExtCircuitRoutedDlci_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 2, 2, 1, 7),
    _RuijiefrExtCircuitRoutedDlci_Type()
)
ruijiefrExtCircuitRoutedDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitRoutedDlci.setStatus("current")
_RuijiefrExtCircuitRoutedIf_Type = InterfaceIndex
_RuijiefrExtCircuitRoutedIf_Object = MibTableColumn
ruijiefrExtCircuitRoutedIf = _RuijiefrExtCircuitRoutedIf_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 2, 2, 1, 8),
    _RuijiefrExtCircuitRoutedIf_Type()
)
ruijiefrExtCircuitRoutedIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitRoutedIf.setStatus("current")
_RuijiefrExtCircuitUncompressIns_Type = Counter32
_RuijiefrExtCircuitUncompressIns_Object = MibTableColumn
ruijiefrExtCircuitUncompressIns = _RuijiefrExtCircuitUncompressIns_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 2, 2, 1, 9),
    _RuijiefrExtCircuitUncompressIns_Type()
)
ruijiefrExtCircuitUncompressIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitUncompressIns.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitUncompressIns.setUnits("octets")
_RuijiefrExtCircuitUncompressOuts_Type = Counter32
_RuijiefrExtCircuitUncompressOuts_Object = MibTableColumn
ruijiefrExtCircuitUncompressOuts = _RuijiefrExtCircuitUncompressOuts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 2, 2, 1, 10),
    _RuijiefrExtCircuitUncompressOuts_Type()
)
ruijiefrExtCircuitUncompressOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitUncompressOuts.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitUncompressOuts.setUnits("octets")
_RuijiefrExtCircuitFECNOuts_Type = Counter32
_RuijiefrExtCircuitFECNOuts_Object = MibTableColumn
ruijiefrExtCircuitFECNOuts = _RuijiefrExtCircuitFECNOuts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 2, 2, 1, 11),
    _RuijiefrExtCircuitFECNOuts_Type()
)
ruijiefrExtCircuitFECNOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitFECNOuts.setStatus("current")
_RuijiefrExtCircuitBECNOuts_Type = Counter32
_RuijiefrExtCircuitBECNOuts_Object = MibTableColumn
ruijiefrExtCircuitBECNOuts = _RuijiefrExtCircuitBECNOuts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 2, 2, 1, 12),
    _RuijiefrExtCircuitBECNOuts_Type()
)
ruijiefrExtCircuitBECNOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitBECNOuts.setStatus("current")


class _RuijiefrExtCircuitMinThruputOut_Type(Integer32):
    """Custom type ruijiefrExtCircuitMinThruputOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9600, 1544000),
    )


_RuijiefrExtCircuitMinThruputOut_Type.__name__ = "Integer32"
_RuijiefrExtCircuitMinThruputOut_Object = MibTableColumn
ruijiefrExtCircuitMinThruputOut = _RuijiefrExtCircuitMinThruputOut_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 2, 2, 1, 13),
    _RuijiefrExtCircuitMinThruputOut_Type()
)
ruijiefrExtCircuitMinThruputOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitMinThruputOut.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitMinThruputOut.setUnits("bits per second")


class _RuijiefrExtCircuitMinThruputIn_Type(Integer32):
    """Custom type ruijiefrExtCircuitMinThruputIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9600, 1544000),
    )


_RuijiefrExtCircuitMinThruputIn_Type.__name__ = "Integer32"
_RuijiefrExtCircuitMinThruputIn_Object = MibTableColumn
ruijiefrExtCircuitMinThruputIn = _RuijiefrExtCircuitMinThruputIn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 2, 2, 1, 14),
    _RuijiefrExtCircuitMinThruputIn_Type()
)
ruijiefrExtCircuitMinThruputIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitMinThruputIn.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitMinThruputIn.setUnits("bits per second")
_RuijiefrExtCircuitBcastPktOuts_Type = Counter32
_RuijiefrExtCircuitBcastPktOuts_Object = MibTableColumn
ruijiefrExtCircuitBcastPktOuts = _RuijiefrExtCircuitBcastPktOuts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 2, 2, 1, 15),
    _RuijiefrExtCircuitBcastPktOuts_Type()
)
ruijiefrExtCircuitBcastPktOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitBcastPktOuts.setStatus("current")
_RuijiefrExtCircuitBcastByteOuts_Type = Counter32
_RuijiefrExtCircuitBcastByteOuts_Object = MibTableColumn
ruijiefrExtCircuitBcastByteOuts = _RuijiefrExtCircuitBcastByteOuts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 2, 2, 1, 16),
    _RuijiefrExtCircuitBcastByteOuts_Type()
)
ruijiefrExtCircuitBcastByteOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitBcastByteOuts.setStatus("current")


class _RuijiefrExtCircuitBandwidth_Type(Integer32):
    """Custom type ruijiefrExtCircuitBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_RuijiefrExtCircuitBandwidth_Type.__name__ = "Integer32"
_RuijiefrExtCircuitBandwidth_Object = MibTableColumn
ruijiefrExtCircuitBandwidth = _RuijiefrExtCircuitBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 2, 2, 1, 17),
    _RuijiefrExtCircuitBandwidth_Type()
)
ruijiefrExtCircuitBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitBandwidth.setUnits("bits per second")


class _RuijiefrExtCircuitShapeByteLimit_Type(Integer32):
    """Custom type ruijiefrExtCircuitShapeByteLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(125, 2147483647),
    )


_RuijiefrExtCircuitShapeByteLimit_Type.__name__ = "Integer32"
_RuijiefrExtCircuitShapeByteLimit_Object = MibTableColumn
ruijiefrExtCircuitShapeByteLimit = _RuijiefrExtCircuitShapeByteLimit_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 2, 2, 1, 18),
    _RuijiefrExtCircuitShapeByteLimit_Type()
)
ruijiefrExtCircuitShapeByteLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitShapeByteLimit.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitShapeByteLimit.setUnits("octets")


class _RuijiefrExtCircuitShapeInterval_Type(Integer32):
    """Custom type ruijiefrExtCircuitShapeInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 125),
    )


_RuijiefrExtCircuitShapeInterval_Type.__name__ = "Integer32"
_RuijiefrExtCircuitShapeInterval_Object = MibTableColumn
ruijiefrExtCircuitShapeInterval = _RuijiefrExtCircuitShapeInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 2, 2, 1, 19),
    _RuijiefrExtCircuitShapeInterval_Type()
)
ruijiefrExtCircuitShapeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitShapeInterval.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitShapeInterval.setUnits("milliseconds")


class _RuijiefrExtCircuitShapeByteIncrement_Type(Integer32):
    """Custom type ruijiefrExtCircuitShapeByteIncrement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(125, 2147483647),
    )


_RuijiefrExtCircuitShapeByteIncrement_Type.__name__ = "Integer32"
_RuijiefrExtCircuitShapeByteIncrement_Object = MibTableColumn
ruijiefrExtCircuitShapeByteIncrement = _RuijiefrExtCircuitShapeByteIncrement_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 2, 2, 1, 20),
    _RuijiefrExtCircuitShapeByteIncrement_Type()
)
ruijiefrExtCircuitShapeByteIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitShapeByteIncrement.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitShapeByteIncrement.setUnits("octets")
_RuijiefrExtCircuitShapePkts_Type = Counter32
_RuijiefrExtCircuitShapePkts_Object = MibTableColumn
ruijiefrExtCircuitShapePkts = _RuijiefrExtCircuitShapePkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 2, 2, 1, 21),
    _RuijiefrExtCircuitShapePkts_Type()
)
ruijiefrExtCircuitShapePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitShapePkts.setStatus("current")
_RuijiefrExtCircuitShapeBytes_Type = Counter32
_RuijiefrExtCircuitShapeBytes_Object = MibTableColumn
ruijiefrExtCircuitShapeBytes = _RuijiefrExtCircuitShapeBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 2, 2, 1, 22),
    _RuijiefrExtCircuitShapeBytes_Type()
)
ruijiefrExtCircuitShapeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitShapeBytes.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitShapeBytes.setUnits("octets")
_RuijiefrExtCircuitShapePktsDelay_Type = Counter32
_RuijiefrExtCircuitShapePktsDelay_Object = MibTableColumn
ruijiefrExtCircuitShapePktsDelay = _RuijiefrExtCircuitShapePktsDelay_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 2, 2, 1, 23),
    _RuijiefrExtCircuitShapePktsDelay_Type()
)
ruijiefrExtCircuitShapePktsDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitShapePktsDelay.setStatus("current")
_RuijiefrExtCircuitShapeBytesDelay_Type = Counter32
_RuijiefrExtCircuitShapeBytesDelay_Object = MibTableColumn
ruijiefrExtCircuitShapeBytesDelay = _RuijiefrExtCircuitShapeBytesDelay_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 2, 2, 1, 24),
    _RuijiefrExtCircuitShapeBytesDelay_Type()
)
ruijiefrExtCircuitShapeBytesDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitShapeBytesDelay.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitShapeBytesDelay.setUnits("octets")
_RuijiefrExtCircuitShapeActive_Type = TruthValue
_RuijiefrExtCircuitShapeActive_Object = MibTableColumn
ruijiefrExtCircuitShapeActive = _RuijiefrExtCircuitShapeActive_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 2, 2, 1, 25),
    _RuijiefrExtCircuitShapeActive_Type()
)
ruijiefrExtCircuitShapeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitShapeActive.setStatus("current")


class _RuijiefrExtCircuitShapeAdapting_Type(Integer32):
    """Custom type ruijiefrExtCircuitShapeAdapting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("becn", 2),
          ("foreSight", 3))
    )


_RuijiefrExtCircuitShapeAdapting_Type.__name__ = "Integer32"
_RuijiefrExtCircuitShapeAdapting_Object = MibTableColumn
ruijiefrExtCircuitShapeAdapting = _RuijiefrExtCircuitShapeAdapting_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 2, 2, 1, 26),
    _RuijiefrExtCircuitShapeAdapting_Type()
)
ruijiefrExtCircuitShapeAdapting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitShapeAdapting.setStatus("current")


class _RuijiefrExtCircuitTxDataRate_Type(Integer32):
    """Custom type ruijiefrExtCircuitTxDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 45000000),
    )


_RuijiefrExtCircuitTxDataRate_Type.__name__ = "Integer32"
_RuijiefrExtCircuitTxDataRate_Object = MibTableColumn
ruijiefrExtCircuitTxDataRate = _RuijiefrExtCircuitTxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 2, 2, 1, 27),
    _RuijiefrExtCircuitTxDataRate_Type()
)
ruijiefrExtCircuitTxDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitTxDataRate.setStatus("current")


class _RuijiefrExtCircuitTxPktRate_Type(Integer32):
    """Custom type ruijiefrExtCircuitTxPktRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 45000000),
    )


_RuijiefrExtCircuitTxPktRate_Type.__name__ = "Integer32"
_RuijiefrExtCircuitTxPktRate_Object = MibTableColumn
ruijiefrExtCircuitTxPktRate = _RuijiefrExtCircuitTxPktRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 2, 2, 1, 28),
    _RuijiefrExtCircuitTxPktRate_Type()
)
ruijiefrExtCircuitTxPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitTxPktRate.setStatus("current")


class _RuijiefrExtCircuitRcvDataRate_Type(Integer32):
    """Custom type ruijiefrExtCircuitRcvDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 45000000),
    )


_RuijiefrExtCircuitRcvDataRate_Type.__name__ = "Integer32"
_RuijiefrExtCircuitRcvDataRate_Object = MibTableColumn
ruijiefrExtCircuitRcvDataRate = _RuijiefrExtCircuitRcvDataRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 2, 2, 1, 29),
    _RuijiefrExtCircuitRcvDataRate_Type()
)
ruijiefrExtCircuitRcvDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitRcvDataRate.setStatus("current")


class _RuijiefrExtCircuitRcvPktRate_Type(Integer32):
    """Custom type ruijiefrExtCircuitRcvPktRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 45000000),
    )


_RuijiefrExtCircuitRcvPktRate_Type.__name__ = "Integer32"
_RuijiefrExtCircuitRcvPktRate_Object = MibTableColumn
ruijiefrExtCircuitRcvPktRate = _RuijiefrExtCircuitRcvPktRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 2, 2, 1, 30),
    _RuijiefrExtCircuitRcvPktRate_Type()
)
ruijiefrExtCircuitRcvPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrExtCircuitRcvPktRate.setStatus("current")
_RuijiefrMapObjs_ObjectIdentity = ObjectIdentity
ruijiefrMapObjs = _RuijiefrMapObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 3)
)
_RuijiefrMapTable_Object = MibTable
ruijiefrMapTable = _RuijiefrMapTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ruijiefrMapTable.setStatus("current")
_RuijiefrMapEntry_Object = MibTableRow
ruijiefrMapEntry = _RuijiefrMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 3, 1, 1)
)
ruijiefrMapEntry.setIndexNames(
    (0, "FRAME-RELAY-DTE-MIB", "frCircuitIfIndex"),
    (0, "FRAME-RELAY-DTE-MIB", "frCircuitDlci"),
    (0, "RUIJIE-FRAME-RELAY-MIB", "ruijiefrMapIndex"),
)
if mibBuilder.loadTexts:
    ruijiefrMapEntry.setStatus("current")


class _RuijiefrMapIndex_Type(Integer32):
    """Custom type ruijiefrMapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_RuijiefrMapIndex_Type.__name__ = "Integer32"
_RuijiefrMapIndex_Object = MibTableColumn
ruijiefrMapIndex = _RuijiefrMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 3, 1, 1, 1),
    _RuijiefrMapIndex_Type()
)
ruijiefrMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrMapIndex.setStatus("current")
_RuijiefrMapProtocol_Type = RuijiefrMapProtocols
_RuijiefrMapProtocol_Object = MibTableColumn
ruijiefrMapProtocol = _RuijiefrMapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 3, 1, 1, 2),
    _RuijiefrMapProtocol_Type()
)
ruijiefrMapProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrMapProtocol.setStatus("current")


class _RuijiefrMapAddress_Type(OctetString):
    """Custom type ruijiefrMapAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RuijiefrMapAddress_Type.__name__ = "OctetString"
_RuijiefrMapAddress_Object = MibTableColumn
ruijiefrMapAddress = _RuijiefrMapAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 3, 1, 1, 3),
    _RuijiefrMapAddress_Type()
)
ruijiefrMapAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrMapAddress.setStatus("current")


class _RuijiefrMapType_Type(Integer32):
    """Custom type ruijiefrMapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2),
          ("svc", 3))
    )


_RuijiefrMapType_Type.__name__ = "Integer32"
_RuijiefrMapType_Object = MibTableColumn
ruijiefrMapType = _RuijiefrMapType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 3, 1, 1, 4),
    _RuijiefrMapType_Type()
)
ruijiefrMapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrMapType.setStatus("current")


class _RuijiefrMapEncaps_Type(Integer32):
    """Custom type ruijiefrMapEncaps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ietf", 1),
          ("cisco", 2))
    )


_RuijiefrMapEncaps_Type.__name__ = "Integer32"
_RuijiefrMapEncaps_Object = MibTableColumn
ruijiefrMapEncaps = _RuijiefrMapEncaps_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 3, 1, 1, 5),
    _RuijiefrMapEncaps_Type()
)
ruijiefrMapEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrMapEncaps.setStatus("current")
_RuijiefrMapBroadcast_Type = TruthValue
_RuijiefrMapBroadcast_Object = MibTableColumn
ruijiefrMapBroadcast = _RuijiefrMapBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 3, 1, 1, 6),
    _RuijiefrMapBroadcast_Type()
)
ruijiefrMapBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrMapBroadcast.setStatus("current")
_RuijiefrMapPayloadCompress_Type = TruthValue
_RuijiefrMapPayloadCompress_Object = MibTableColumn
ruijiefrMapPayloadCompress = _RuijiefrMapPayloadCompress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 3, 1, 1, 7),
    _RuijiefrMapPayloadCompress_Type()
)
ruijiefrMapPayloadCompress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrMapPayloadCompress.setStatus("deprecated")


class _RuijiefrMapTcpHdrCompress_Type(Integer32):
    """Custom type ruijiefrMapTcpHdrCompress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inapplicable", 1),
          ("passive", 2),
          ("active", 3))
    )


_RuijiefrMapTcpHdrCompress_Type.__name__ = "Integer32"
_RuijiefrMapTcpHdrCompress_Object = MibTableColumn
ruijiefrMapTcpHdrCompress = _RuijiefrMapTcpHdrCompress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 3, 1, 1, 8),
    _RuijiefrMapTcpHdrCompress_Type()
)
ruijiefrMapTcpHdrCompress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrMapTcpHdrCompress.setStatus("current")


class _RuijiefrMapRtpHdrCompress_Type(Integer32):
    """Custom type ruijiefrMapRtpHdrCompress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inapplicable", 1),
          ("passive", 2),
          ("active", 3))
    )


_RuijiefrMapRtpHdrCompress_Type.__name__ = "Integer32"
_RuijiefrMapRtpHdrCompress_Object = MibTableColumn
ruijiefrMapRtpHdrCompress = _RuijiefrMapRtpHdrCompress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 3, 1, 1, 9),
    _RuijiefrMapRtpHdrCompress_Type()
)
ruijiefrMapRtpHdrCompress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrMapRtpHdrCompress.setStatus("current")


class _RuijiefrMapPayloadCompressType_Type(Integer32):
    """Custom type ruijiefrMapPayloadCompressType based on Integer32"""
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
        *(("inapplicable", 1),
          ("cisco", 2),
          ("frf9Software", 3),
          ("frf9Hardware", 4))
    )


_RuijiefrMapPayloadCompressType_Type.__name__ = "Integer32"
_RuijiefrMapPayloadCompressType_Object = MibTableColumn
ruijiefrMapPayloadCompressType = _RuijiefrMapPayloadCompressType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 3, 1, 1, 10),
    _RuijiefrMapPayloadCompressType_Type()
)
ruijiefrMapPayloadCompressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrMapPayloadCompressType.setStatus("current")
_RuijiefrSvcObjs_ObjectIdentity = ObjectIdentity
ruijiefrSvcObjs = _RuijiefrSvcObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 4)
)
_RuijiefrSvcTable_Object = MibTable
ruijiefrSvcTable = _RuijiefrSvcTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ruijiefrSvcTable.setStatus("current")
_RuijiefrSvcEntry_Object = MibTableRow
ruijiefrSvcEntry = _RuijiefrSvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 4, 1, 1)
)
ruijiefrSvcEntry.setIndexNames(
    (0, "FRAME-RELAY-DTE-MIB", "frCircuitIfIndex"),
    (0, "FRAME-RELAY-DTE-MIB", "frCircuitDlci"),
)
if mibBuilder.loadTexts:
    ruijiefrSvcEntry.setStatus("current")


class _RuijiefrSvcAddrLocal_Type(OctetString):
    """Custom type ruijiefrSvcAddrLocal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RuijiefrSvcAddrLocal_Type.__name__ = "OctetString"
_RuijiefrSvcAddrLocal_Object = MibTableColumn
ruijiefrSvcAddrLocal = _RuijiefrSvcAddrLocal_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 4, 1, 1, 1),
    _RuijiefrSvcAddrLocal_Type()
)
ruijiefrSvcAddrLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrSvcAddrLocal.setStatus("current")


class _RuijiefrSvcAddrRemote_Type(OctetString):
    """Custom type ruijiefrSvcAddrRemote based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RuijiefrSvcAddrRemote_Type.__name__ = "OctetString"
_RuijiefrSvcAddrRemote_Object = MibTableColumn
ruijiefrSvcAddrRemote = _RuijiefrSvcAddrRemote_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 4, 1, 1, 2),
    _RuijiefrSvcAddrRemote_Type()
)
ruijiefrSvcAddrRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrSvcAddrRemote.setStatus("current")


class _RuijiefrSvcThroughputIn_Type(Integer32):
    """Custom type ruijiefrSvcThroughputIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9600, 1544000),
    )


_RuijiefrSvcThroughputIn_Type.__name__ = "Integer32"
_RuijiefrSvcThroughputIn_Object = MibTableColumn
ruijiefrSvcThroughputIn = _RuijiefrSvcThroughputIn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 4, 1, 1, 3),
    _RuijiefrSvcThroughputIn_Type()
)
ruijiefrSvcThroughputIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrSvcThroughputIn.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrSvcThroughputIn.setUnits("bits per second")


class _RuijiefrSvcMinThruputOut_Type(Integer32):
    """Custom type ruijiefrSvcMinThruputOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9600, 1544000),
    )


_RuijiefrSvcMinThruputOut_Type.__name__ = "Integer32"
_RuijiefrSvcMinThruputOut_Object = MibTableColumn
ruijiefrSvcMinThruputOut = _RuijiefrSvcMinThruputOut_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 4, 1, 1, 4),
    _RuijiefrSvcMinThruputOut_Type()
)
ruijiefrSvcMinThruputOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrSvcMinThruputOut.setStatus("deprecated")
if mibBuilder.loadTexts:
    ruijiefrSvcMinThruputOut.setUnits("bits per second")


class _RuijiefrSvcMinThruputIn_Type(Integer32):
    """Custom type ruijiefrSvcMinThruputIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9600, 1544000),
    )


_RuijiefrSvcMinThruputIn_Type.__name__ = "Integer32"
_RuijiefrSvcMinThruputIn_Object = MibTableColumn
ruijiefrSvcMinThruputIn = _RuijiefrSvcMinThruputIn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 4, 1, 1, 5),
    _RuijiefrSvcMinThruputIn_Type()
)
ruijiefrSvcMinThruputIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrSvcMinThruputIn.setStatus("deprecated")
if mibBuilder.loadTexts:
    ruijiefrSvcMinThruputIn.setUnits("bits per second")


class _RuijiefrSvcCommitBurstIn_Type(Integer32):
    """Custom type ruijiefrSvcCommitBurstIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9600, 1544000),
    )


_RuijiefrSvcCommitBurstIn_Type.__name__ = "Integer32"
_RuijiefrSvcCommitBurstIn_Object = MibTableColumn
ruijiefrSvcCommitBurstIn = _RuijiefrSvcCommitBurstIn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 4, 1, 1, 6),
    _RuijiefrSvcCommitBurstIn_Type()
)
ruijiefrSvcCommitBurstIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrSvcCommitBurstIn.setStatus("current")


class _RuijiefrSvcExcessBurstIn_Type(Integer32):
    """Custom type ruijiefrSvcExcessBurstIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9600, 2440000),
    )


_RuijiefrSvcExcessBurstIn_Type.__name__ = "Integer32"
_RuijiefrSvcExcessBurstIn_Object = MibTableColumn
ruijiefrSvcExcessBurstIn = _RuijiefrSvcExcessBurstIn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 4, 1, 1, 7),
    _RuijiefrSvcExcessBurstIn_Type()
)
ruijiefrSvcExcessBurstIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrSvcExcessBurstIn.setStatus("current")
_RuijiefrSvcIdleTime_Type = Integer32
_RuijiefrSvcIdleTime_Object = MibTableColumn
ruijiefrSvcIdleTime = _RuijiefrSvcIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 4, 1, 1, 8),
    _RuijiefrSvcIdleTime_Type()
)
ruijiefrSvcIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrSvcIdleTime.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrSvcIdleTime.setUnits("seconds")
_RuijiefrElmiObjs_ObjectIdentity = ObjectIdentity
ruijiefrElmiObjs = _RuijiefrElmiObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 5)
)
_RuijiefrElmiIpAddr_Type = IpAddress
_RuijiefrElmiIpAddr_Object = MibScalar
ruijiefrElmiIpAddr = _RuijiefrElmiIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 5, 1),
    _RuijiefrElmiIpAddr_Type()
)
ruijiefrElmiIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrElmiIpAddr.setStatus("current")
_RuijiefrElmiTable_Object = MibTable
ruijiefrElmiTable = _RuijiefrElmiTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 5, 2)
)
if mibBuilder.loadTexts:
    ruijiefrElmiTable.setStatus("current")
_RuijiefrElmiEntry_Object = MibTableRow
ruijiefrElmiEntry = _RuijiefrElmiEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 5, 2, 1)
)
ruijiefrElmiEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ruijiefrElmiEntry.setStatus("current")


class _RuijiefrElmiLinkStatus_Type(Integer32):
    """Custom type ruijiefrElmiLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_RuijiefrElmiLinkStatus_Type.__name__ = "Integer32"
_RuijiefrElmiLinkStatus_Object = MibTableColumn
ruijiefrElmiLinkStatus = _RuijiefrElmiLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 5, 2, 1, 1),
    _RuijiefrElmiLinkStatus_Type()
)
ruijiefrElmiLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrElmiLinkStatus.setStatus("current")


class _RuijiefrElmiArStatus_Type(Integer32):
    """Custom type ruijiefrElmiArStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_RuijiefrElmiArStatus_Type.__name__ = "Integer32"
_RuijiefrElmiArStatus_Object = MibTableColumn
ruijiefrElmiArStatus = _RuijiefrElmiArStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 5, 2, 1, 2),
    _RuijiefrElmiArStatus_Type()
)
ruijiefrElmiArStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrElmiArStatus.setStatus("current")


class _RuijiefrElmiRemoteStatus_Type(Integer32):
    """Custom type ruijiefrElmiRemoteStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_RuijiefrElmiRemoteStatus_Type.__name__ = "Integer32"
_RuijiefrElmiRemoteStatus_Object = MibTableColumn
ruijiefrElmiRemoteStatus = _RuijiefrElmiRemoteStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 5, 2, 1, 3),
    _RuijiefrElmiRemoteStatus_Type()
)
ruijiefrElmiRemoteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrElmiRemoteStatus.setStatus("current")
_RuijiefrElmiNeighborTable_Object = MibTable
ruijiefrElmiNeighborTable = _RuijiefrElmiNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 5, 3)
)
if mibBuilder.loadTexts:
    ruijiefrElmiNeighborTable.setStatus("current")
_RuijiefrElmiNeighborEntry_Object = MibTableRow
ruijiefrElmiNeighborEntry = _RuijiefrElmiNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 5, 3, 1)
)
ruijiefrElmiNeighborEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ruijiefrElmiNeighborEntry.setStatus("current")


class _RuijiefrElmiNeighborArStatus_Type(Integer32):
    """Custom type ruijiefrElmiNeighborArStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notsupported", 1),
          ("enabled", 2),
          ("disabled", 3))
    )


_RuijiefrElmiNeighborArStatus_Type.__name__ = "Integer32"
_RuijiefrElmiNeighborArStatus_Object = MibTableColumn
ruijiefrElmiNeighborArStatus = _RuijiefrElmiNeighborArStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 5, 3, 1, 1),
    _RuijiefrElmiNeighborArStatus_Type()
)
ruijiefrElmiNeighborArStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrElmiNeighborArStatus.setStatus("current")
_RuijiefrElmiNeighborIpAddress_Type = IpAddress
_RuijiefrElmiNeighborIpAddress_Object = MibTableColumn
ruijiefrElmiNeighborIpAddress = _RuijiefrElmiNeighborIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 5, 3, 1, 2),
    _RuijiefrElmiNeighborIpAddress_Type()
)
ruijiefrElmiNeighborIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrElmiNeighborIpAddress.setStatus("current")
_RuijiefrElmiNeighborIfIndex_Type = InterfaceIndex
_RuijiefrElmiNeighborIfIndex_Object = MibTableColumn
ruijiefrElmiNeighborIfIndex = _RuijiefrElmiNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 5, 3, 1, 3),
    _RuijiefrElmiNeighborIfIndex_Type()
)
ruijiefrElmiNeighborIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrElmiNeighborIfIndex.setStatus("current")
_RuijiefrElmiNeighborVendorName_Type = DisplayString
_RuijiefrElmiNeighborVendorName_Object = MibTableColumn
ruijiefrElmiNeighborVendorName = _RuijiefrElmiNeighborVendorName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 5, 3, 1, 4),
    _RuijiefrElmiNeighborVendorName_Type()
)
ruijiefrElmiNeighborVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrElmiNeighborVendorName.setStatus("current")
_RuijiefrElmiNeighborPlatformName_Type = DisplayString
_RuijiefrElmiNeighborPlatformName_Object = MibTableColumn
ruijiefrElmiNeighborPlatformName = _RuijiefrElmiNeighborPlatformName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 5, 3, 1, 5),
    _RuijiefrElmiNeighborPlatformName_Type()
)
ruijiefrElmiNeighborPlatformName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrElmiNeighborPlatformName.setStatus("current")
_RuijiefrElmiNeighborDeviceName_Type = DisplayString
_RuijiefrElmiNeighborDeviceName_Object = MibTableColumn
ruijiefrElmiNeighborDeviceName = _RuijiefrElmiNeighborDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 5, 3, 1, 6),
    _RuijiefrElmiNeighborDeviceName_Type()
)
ruijiefrElmiNeighborDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrElmiNeighborDeviceName.setStatus("current")
_RuijiefrFragObjs_ObjectIdentity = ObjectIdentity
ruijiefrFragObjs = _RuijiefrFragObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 6)
)
_RuijiefrFragTable_Object = MibTable
ruijiefrFragTable = _RuijiefrFragTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 6, 1)
)
if mibBuilder.loadTexts:
    ruijiefrFragTable.setStatus("current")
_RuijiefrFragEntry_Object = MibTableRow
ruijiefrFragEntry = _RuijiefrFragEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 6, 1, 1)
)
ruijiefrFragEntry.setIndexNames(
    (0, "FRAME-RELAY-DTE-MIB", "frCircuitIfIndex"),
    (0, "FRAME-RELAY-DTE-MIB", "frCircuitDlci"),
)
if mibBuilder.loadTexts:
    ruijiefrFragEntry.setStatus("current")


class _RuijiefrFragSize_Type(Integer32):
    """Custom type ruijiefrFragSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1600),
    )


_RuijiefrFragSize_Type.__name__ = "Integer32"
_RuijiefrFragSize_Object = MibTableColumn
ruijiefrFragSize = _RuijiefrFragSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 6, 1, 1, 1),
    _RuijiefrFragSize_Type()
)
ruijiefrFragSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrFragSize.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrFragSize.setUnits("octets")
_RuijiefrFragType_Type = DisplayString
_RuijiefrFragType_Object = MibTableColumn
ruijiefrFragType = _RuijiefrFragType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 6, 1, 1, 2),
    _RuijiefrFragType_Type()
)
ruijiefrFragType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrFragType.setStatus("current")
_RuijiefrFragInPkts_Type = Counter32
_RuijiefrFragInPkts_Object = MibTableColumn
ruijiefrFragInPkts = _RuijiefrFragInPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 6, 1, 1, 3),
    _RuijiefrFragInPkts_Type()
)
ruijiefrFragInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrFragInPkts.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrFragInPkts.setUnits("packets")
_RuijiefrFragOutPkts_Type = Counter32
_RuijiefrFragOutPkts_Object = MibTableColumn
ruijiefrFragOutPkts = _RuijiefrFragOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 6, 1, 1, 4),
    _RuijiefrFragOutPkts_Type()
)
ruijiefrFragOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrFragOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrFragOutPkts.setUnits("packets")
_RuijiefrFragInOctets_Type = Counter32
_RuijiefrFragInOctets_Object = MibTableColumn
ruijiefrFragInOctets = _RuijiefrFragInOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 6, 1, 1, 5),
    _RuijiefrFragInOctets_Type()
)
ruijiefrFragInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrFragInOctets.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrFragInOctets.setUnits("octets")
_RuijiefrFragOutOctets_Type = Counter32
_RuijiefrFragOutOctets_Object = MibTableColumn
ruijiefrFragOutOctets = _RuijiefrFragOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 6, 1, 1, 6),
    _RuijiefrFragOutOctets_Type()
)
ruijiefrFragOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrFragOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrFragOutOctets.setUnits("octets")
_RuijiefrFragNotInPkts_Type = Counter32
_RuijiefrFragNotInPkts_Object = MibTableColumn
ruijiefrFragNotInPkts = _RuijiefrFragNotInPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 6, 1, 1, 7),
    _RuijiefrFragNotInPkts_Type()
)
ruijiefrFragNotInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrFragNotInPkts.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrFragNotInPkts.setUnits("packets")
_RuijiefrFragNotOutPkts_Type = Counter32
_RuijiefrFragNotOutPkts_Object = MibTableColumn
ruijiefrFragNotOutPkts = _RuijiefrFragNotOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 6, 1, 1, 8),
    _RuijiefrFragNotOutPkts_Type()
)
ruijiefrFragNotOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrFragNotOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrFragNotOutPkts.setUnits("packets")
_RuijiefrFragNotInOctets_Type = Counter32
_RuijiefrFragNotInOctets_Object = MibTableColumn
ruijiefrFragNotInOctets = _RuijiefrFragNotInOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 6, 1, 1, 9),
    _RuijiefrFragNotInOctets_Type()
)
ruijiefrFragNotInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrFragNotInOctets.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrFragNotInOctets.setUnits("octets")
_RuijiefrFragNotOutOctets_Type = Counter32
_RuijiefrFragNotOutOctets_Object = MibTableColumn
ruijiefrFragNotOutOctets = _RuijiefrFragNotOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 6, 1, 1, 10),
    _RuijiefrFragNotOutOctets_Type()
)
ruijiefrFragNotOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrFragNotOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrFragNotOutOctets.setUnits("octets")
_RuijiefrFragAssembledInPkts_Type = Counter32
_RuijiefrFragAssembledInPkts_Object = MibTableColumn
ruijiefrFragAssembledInPkts = _RuijiefrFragAssembledInPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 6, 1, 1, 11),
    _RuijiefrFragAssembledInPkts_Type()
)
ruijiefrFragAssembledInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrFragAssembledInPkts.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrFragAssembledInPkts.setUnits("packets")
_RuijiefrFragAssembledInOctets_Type = Counter32
_RuijiefrFragAssembledInOctets_Object = MibTableColumn
ruijiefrFragAssembledInOctets = _RuijiefrFragAssembledInOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 6, 1, 1, 12),
    _RuijiefrFragAssembledInOctets_Type()
)
ruijiefrFragAssembledInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrFragAssembledInOctets.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrFragAssembledInOctets.setUnits("octets")
_RuijiefrFragPreOutPkts_Type = Counter32
_RuijiefrFragPreOutPkts_Object = MibTableColumn
ruijiefrFragPreOutPkts = _RuijiefrFragPreOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 6, 1, 1, 13),
    _RuijiefrFragPreOutPkts_Type()
)
ruijiefrFragPreOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrFragPreOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrFragPreOutPkts.setUnits("packets")
_RuijiefrFragPreOutOctets_Type = Counter32
_RuijiefrFragPreOutOctets_Object = MibTableColumn
ruijiefrFragPreOutOctets = _RuijiefrFragPreOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 6, 1, 1, 14),
    _RuijiefrFragPreOutOctets_Type()
)
ruijiefrFragPreOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrFragPreOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrFragPreOutOctets.setUnits("octets")
_RuijiefrFragDroppedReAssembledInPkts_Type = Counter32
_RuijiefrFragDroppedReAssembledInPkts_Object = MibTableColumn
ruijiefrFragDroppedReAssembledInPkts = _RuijiefrFragDroppedReAssembledInPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 6, 1, 1, 15),
    _RuijiefrFragDroppedReAssembledInPkts_Type()
)
ruijiefrFragDroppedReAssembledInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrFragDroppedReAssembledInPkts.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrFragDroppedReAssembledInPkts.setUnits("packets")
_RuijiefrFragDroppedFragmentedOutPkts_Type = Counter32
_RuijiefrFragDroppedFragmentedOutPkts_Object = MibTableColumn
ruijiefrFragDroppedFragmentedOutPkts = _RuijiefrFragDroppedFragmentedOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 6, 1, 1, 16),
    _RuijiefrFragDroppedFragmentedOutPkts_Type()
)
ruijiefrFragDroppedFragmentedOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrFragDroppedFragmentedOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrFragDroppedFragmentedOutPkts.setUnits("packets")


class _RuijiefrFragTimeoutsIn_Type(Integer32):
    """Custom type ruijiefrFragTimeoutsIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_RuijiefrFragTimeoutsIn_Type.__name__ = "Integer32"
_RuijiefrFragTimeoutsIn_Object = MibTableColumn
ruijiefrFragTimeoutsIn = _RuijiefrFragTimeoutsIn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 6, 1, 1, 17),
    _RuijiefrFragTimeoutsIn_Type()
)
ruijiefrFragTimeoutsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrFragTimeoutsIn.setStatus("current")
_RuijiefrFragOutOfSeqFragPkts_Type = Counter32
_RuijiefrFragOutOfSeqFragPkts_Object = MibTableColumn
ruijiefrFragOutOfSeqFragPkts = _RuijiefrFragOutOfSeqFragPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 6, 1, 1, 18),
    _RuijiefrFragOutOfSeqFragPkts_Type()
)
ruijiefrFragOutOfSeqFragPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrFragOutOfSeqFragPkts.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrFragOutOfSeqFragPkts.setUnits("packets")
_RuijiefrFragUnexpectedBBitSetPkts_Type = Counter32
_RuijiefrFragUnexpectedBBitSetPkts_Object = MibTableColumn
ruijiefrFragUnexpectedBBitSetPkts = _RuijiefrFragUnexpectedBBitSetPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 6, 1, 1, 19),
    _RuijiefrFragUnexpectedBBitSetPkts_Type()
)
ruijiefrFragUnexpectedBBitSetPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrFragUnexpectedBBitSetPkts.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrFragUnexpectedBBitSetPkts.setUnits("packets")
_RuijiefrFragSeqMissedPkts_Type = Counter32
_RuijiefrFragSeqMissedPkts_Object = MibTableColumn
ruijiefrFragSeqMissedPkts = _RuijiefrFragSeqMissedPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 6, 1, 1, 20),
    _RuijiefrFragSeqMissedPkts_Type()
)
ruijiefrFragSeqMissedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrFragSeqMissedPkts.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrFragSeqMissedPkts.setUnits("packets")
_RuijiefrFragInterleavedOutPkts_Type = Counter32
_RuijiefrFragInterleavedOutPkts_Object = MibTableColumn
ruijiefrFragInterleavedOutPkts = _RuijiefrFragInterleavedOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 6, 1, 1, 21),
    _RuijiefrFragInterleavedOutPkts_Type()
)
ruijiefrFragInterleavedOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrFragInterleavedOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    ruijiefrFragInterleavedOutPkts.setUnits("packets")
_RuijiefrConnectionObjs_ObjectIdentity = ObjectIdentity
ruijiefrConnectionObjs = _RuijiefrConnectionObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 7)
)
_RuijiefrConnectionTable_Object = MibTable
ruijiefrConnectionTable = _RuijiefrConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 7, 1)
)
if mibBuilder.loadTexts:
    ruijiefrConnectionTable.setStatus("current")
_RuijiefrConnectionEntry_Object = MibTableRow
ruijiefrConnectionEntry = _RuijiefrConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 7, 1, 1)
)
ruijiefrConnectionEntry.setIndexNames(
    (0, "FRAME-RELAY-DTE-MIB", "frCircuitIfIndex"),
    (0, "FRAME-RELAY-DTE-MIB", "frCircuitDlci"),
)
if mibBuilder.loadTexts:
    ruijiefrConnectionEntry.setStatus("current")
_RuijiefrConnName_Type = DisplayString
_RuijiefrConnName_Object = MibTableColumn
ruijiefrConnName = _RuijiefrConnName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 7, 1, 1, 1),
    _RuijiefrConnName_Type()
)
ruijiefrConnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrConnName.setStatus("current")


class _RuijiefrConnID_Type(Integer32):
    """Custom type ruijiefrConnID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_RuijiefrConnID_Type.__name__ = "Integer32"
_RuijiefrConnID_Object = MibTableColumn
ruijiefrConnID = _RuijiefrConnID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 7, 1, 1, 2),
    _RuijiefrConnID_Type()
)
ruijiefrConnID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrConnID.setStatus("current")
_RuijiefrConnState_Type = DisplayString
_RuijiefrConnState_Object = MibTableColumn
ruijiefrConnState = _RuijiefrConnState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 7, 1, 1, 3),
    _RuijiefrConnState_Type()
)
ruijiefrConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrConnState.setStatus("current")
_RuijiefrConnSegment1Name_Type = DisplayString
_RuijiefrConnSegment1Name_Object = MibTableColumn
ruijiefrConnSegment1Name = _RuijiefrConnSegment1Name_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 7, 1, 1, 4),
    _RuijiefrConnSegment1Name_Type()
)
ruijiefrConnSegment1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrConnSegment1Name.setStatus("current")
_RuijiefrConnSegment1VCGroup_Type = DisplayString
_RuijiefrConnSegment1VCGroup_Object = MibTableColumn
ruijiefrConnSegment1VCGroup = _RuijiefrConnSegment1VCGroup_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 7, 1, 1, 5),
    _RuijiefrConnSegment1VCGroup_Type()
)
ruijiefrConnSegment1VCGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrConnSegment1VCGroup.setStatus("current")
_RuijiefrConnSegment1Dlci_Type = DlciNumber
_RuijiefrConnSegment1Dlci_Object = MibTableColumn
ruijiefrConnSegment1Dlci = _RuijiefrConnSegment1Dlci_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 7, 1, 1, 6),
    _RuijiefrConnSegment1Dlci_Type()
)
ruijiefrConnSegment1Dlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrConnSegment1Dlci.setStatus("current")
_RuijiefrConnSegment2Name_Type = DisplayString
_RuijiefrConnSegment2Name_Object = MibTableColumn
ruijiefrConnSegment2Name = _RuijiefrConnSegment2Name_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 7, 1, 1, 7),
    _RuijiefrConnSegment2Name_Type()
)
ruijiefrConnSegment2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrConnSegment2Name.setStatus("current")


class _RuijiefrConnSegment2Vpi_Type(Integer32):
    """Custom type ruijiefrConnSegment2Vpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_RuijiefrConnSegment2Vpi_Type.__name__ = "Integer32"
_RuijiefrConnSegment2Vpi_Object = MibTableColumn
ruijiefrConnSegment2Vpi = _RuijiefrConnSegment2Vpi_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 7, 1, 1, 8),
    _RuijiefrConnSegment2Vpi_Type()
)
ruijiefrConnSegment2Vpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrConnSegment2Vpi.setStatus("current")


class _RuijiefrConnSegment2Vci_Type(Integer32):
    """Custom type ruijiefrConnSegment2Vci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_RuijiefrConnSegment2Vci_Type.__name__ = "Integer32"
_RuijiefrConnSegment2Vci_Object = MibTableColumn
ruijiefrConnSegment2Vci = _RuijiefrConnSegment2Vci_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 7, 1, 1, 9),
    _RuijiefrConnSegment2Vci_Type()
)
ruijiefrConnSegment2Vci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrConnSegment2Vci.setStatus("current")


class _RuijiefrConnServiceTranslation_Type(Integer32):
    """Custom type ruijiefrConnServiceTranslation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("serviceTranslationEnabled", 1),
          ("serviceTranslationNotEnabled", 2))
    )


_RuijiefrConnServiceTranslation_Type.__name__ = "Integer32"
_RuijiefrConnServiceTranslation_Object = MibTableColumn
ruijiefrConnServiceTranslation = _RuijiefrConnServiceTranslation_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 7, 1, 1, 10),
    _RuijiefrConnServiceTranslation_Type()
)
ruijiefrConnServiceTranslation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrConnServiceTranslation.setStatus("current")
_RuijiefrConnFrSscsDlci_Type = DlciNumber
_RuijiefrConnFrSscsDlci_Object = MibTableColumn
ruijiefrConnFrSscsDlci = _RuijiefrConnFrSscsDlci_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 7, 1, 1, 11),
    _RuijiefrConnFrSscsDlci_Type()
)
ruijiefrConnFrSscsDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrConnFrSscsDlci.setStatus("current")


class _RuijiefrConnEfciBit_Type(Integer32):
    """Custom type ruijiefrConnEfciBit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mapFecn", 1),
          ("notMapFecn", 2))
    )


_RuijiefrConnEfciBit_Type.__name__ = "Integer32"
_RuijiefrConnEfciBit_Object = MibTableColumn
ruijiefrConnEfciBit = _RuijiefrConnEfciBit_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 7, 1, 1, 12),
    _RuijiefrConnEfciBit_Type()
)
ruijiefrConnEfciBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrConnEfciBit.setStatus("current")


class _RuijiefrConnDeBit_Type(Integer32):
    """Custom type ruijiefrConnDeBit based on Integer32"""
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
        *(("noMapClp", 1),
          ("mapClp", 2),
          ("setDe0", 3),
          ("setDe1", 4))
    )


_RuijiefrConnDeBit_Type.__name__ = "Integer32"
_RuijiefrConnDeBit_Object = MibTableColumn
ruijiefrConnDeBit = _RuijiefrConnDeBit_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 7, 1, 1, 13),
    _RuijiefrConnDeBit_Type()
)
ruijiefrConnDeBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrConnDeBit.setStatus("current")


class _RuijiefrConnClpBit_Type(Integer32):
    """Custom type ruijiefrConnClpBit based on Integer32"""
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
        *(("setClpTo0AndCopyDeToFrsscsDe", 1),
          ("setClpTo1AndCopyDeToFrsscsDe", 2),
          ("copyDeToFrsscsDeAndClp", 3),
          ("copyDeToClp", 4),
          ("setClp1", 5),
          ("setClp0", 6))
    )


_RuijiefrConnClpBit_Type.__name__ = "Integer32"
_RuijiefrConnClpBit_Object = MibTableColumn
ruijiefrConnClpBit = _RuijiefrConnClpBit_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 1, 7, 1, 1, 14),
    _RuijiefrConnClpBit_Type()
)
ruijiefrConnClpBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiefrConnClpBit.setStatus("current")
_RuijieFrMIBConformance_ObjectIdentity = ObjectIdentity
ruijieFrMIBConformance = _RuijieFrMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 3)
)
_RuijieFrMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieFrMIBCompliances = _RuijieFrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 3, 1)
)
_RuijieFrMIBGroups_ObjectIdentity = ObjectIdentity
ruijieFrMIBGroups = _RuijieFrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 3, 2)
)
frDlcmiEntry.registerAugmentions(
    ("RUIJIE-FRAME-RELAY-MIB",
     "ruijiefrLmiEntry")
)
ruijiefrLmiEntry.setIndexNames(*frDlcmiEntry.getIndexNames())
frCircuitEntry.registerAugmentions(
    ("RUIJIE-FRAME-RELAY-MIB",
     "ruijiefrCircuitEntry")
)
ruijiefrCircuitEntry.setIndexNames(*frCircuitEntry.getIndexNames())
frCircuitEntry.registerAugmentions(
    ("RUIJIE-FRAME-RELAY-MIB",
     "ruijiefrExtCircuitEntry")
)
ruijiefrExtCircuitEntry.setIndexNames(*frCircuitEntry.getIndexNames())

# Managed Objects groups

ruijieFrMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 3, 2, 1)
)
ruijieFrMIBGroup.setObjects(
      *(("RUIJIE-FRAME-RELAY-MIB", "ruijiefrLmiLinkstatus"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrLmiLinkType"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrLmiEnquiryIns"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrLmiEnquiryOuts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrLmiStatusIns"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrLmiStatusOuts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrLmiUpdateStatusIns"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrLmiUpdateStatusOuts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrLmiStatusTimeouts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrLmiStatusEnqTimeouts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrLmiN392Dce"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrLmiN393Dce"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrLmiT392Dce"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrCircuitDEins"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrCircuitDEouts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrCircuitDropPktsOuts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrCircuitType"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitIfName"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitIfType"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitSubifIndex"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitMapStatus"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitCreateType"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitMulticast"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitRoutedDlci"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitRoutedIf"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrMapIndex"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrMapProtocol"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrMapAddress"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrMapType"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrMapEncaps"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrMapBroadcast"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrMapPayloadCompress"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrMapTcpHdrCompress"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrSvcAddrLocal"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrSvcAddrRemote"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrSvcThroughputIn"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrSvcMinThruputOut"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrSvcMinThruputIn"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrSvcCommitBurstIn"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrSvcExcessBurstIn"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrSvcIdleTime"))
)
if mibBuilder.loadTexts:
    ruijieFrMIBGroup.setStatus("deprecated")

ruijieFrMIBGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 3, 2, 2)
)
ruijieFrMIBGroupRev1.setObjects(
      *(("RUIJIE-FRAME-RELAY-MIB", "ruijiefrLmiLinkstatus"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrLmiLinkType"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrLmiEnquiryIns"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrLmiEnquiryOuts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrLmiStatusIns"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrLmiStatusOuts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrLmiUpdateStatusIns"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrLmiUpdateStatusOuts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrLmiStatusTimeouts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrLmiStatusEnqTimeouts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrLmiN392Dce"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrLmiN393Dce"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrLmiT392Dce"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrCircuitDEins"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrCircuitDEouts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrCircuitDropPktsOuts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrCircuitType"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitIfName"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitIfType"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitSubifIndex"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitMapStatus"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitCreateType"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitMulticast"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitRoutedDlci"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitRoutedIf"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitUncompressIns"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitUncompressOuts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrMapIndex"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrMapProtocol"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrMapAddress"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrMapType"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrMapEncaps"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrMapBroadcast"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrMapTcpHdrCompress"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrMapRtpHdrCompress"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrMapPayloadCompressType"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrSvcAddrLocal"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrSvcAddrRemote"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrSvcThroughputIn"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrSvcMinThruputOut"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrSvcMinThruputIn"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrSvcCommitBurstIn"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrSvcExcessBurstIn"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrSvcIdleTime"))
)
if mibBuilder.loadTexts:
    ruijieFrMIBGroupRev1.setStatus("deprecated")

ruijieFrLmiMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 3, 2, 3)
)
ruijieFrLmiMIBGroup.setObjects(
      *(("RUIJIE-FRAME-RELAY-MIB", "ruijiefrLmiLinkstatus"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrLmiLinkType"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrLmiEnquiryIns"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrLmiEnquiryOuts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrLmiStatusIns"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrLmiStatusOuts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrLmiUpdateStatusIns"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrLmiUpdateStatusOuts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrLmiStatusTimeouts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrLmiStatusEnqTimeouts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrLmiN392Dce"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrLmiN393Dce"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrLmiT392Dce"))
)
if mibBuilder.loadTexts:
    ruijieFrLmiMIBGroup.setStatus("current")

ruijieFrCircuitMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 3, 2, 4)
)
ruijieFrCircuitMIBGroup.setObjects(
      *(("RUIJIE-FRAME-RELAY-MIB", "ruijiefrCircuitDEins"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrCircuitDEouts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrCircuitDropPktsOuts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrCircuitType"))
)
if mibBuilder.loadTexts:
    ruijieFrCircuitMIBGroup.setStatus("current")

ruijieExtCircuitMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 3, 2, 5)
)
ruijieExtCircuitMIBGroup.setObjects(
      *(("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitIfName"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitIfType"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitSubifIndex"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitMapStatus"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitCreateType"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitMulticast"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitRoutedDlci"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitRoutedIf"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitUncompressIns"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitUncompressOuts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitFECNOuts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitBECNOuts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitMinThruputOut"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitMinThruputIn"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitBcastPktOuts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitBcastByteOuts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitBandwidth"))
)
if mibBuilder.loadTexts:
    ruijieExtCircuitMIBGroup.setStatus("deprecated")

ruijieFrTsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 3, 2, 6)
)
ruijieFrTsMIBGroup.setObjects(
      *(("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitShapeByteLimit"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitShapeInterval"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitShapeByteIncrement"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitShapePkts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitShapeBytes"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitShapePktsDelay"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitShapeBytesDelay"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitShapeActive"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitShapeAdapting"))
)
if mibBuilder.loadTexts:
    ruijieFrTsMIBGroup.setStatus("current")

ruijieFrMapMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 3, 2, 7)
)
ruijieFrMapMIBGroup.setObjects(
      *(("RUIJIE-FRAME-RELAY-MIB", "ruijiefrMapIndex"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrMapProtocol"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrMapAddress"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrMapType"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrMapEncaps"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrMapBroadcast"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrMapTcpHdrCompress"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrMapRtpHdrCompress"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrMapPayloadCompressType"))
)
if mibBuilder.loadTexts:
    ruijieFrMapMIBGroup.setStatus("current")

ruijieFrSvcMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 3, 2, 8)
)
ruijieFrSvcMIBGroup.setObjects(
      *(("RUIJIE-FRAME-RELAY-MIB", "ruijiefrSvcAddrLocal"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrSvcAddrRemote"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrSvcThroughputIn"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrSvcCommitBurstIn"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrSvcExcessBurstIn"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrSvcIdleTime"))
)
if mibBuilder.loadTexts:
    ruijieFrSvcMIBGroup.setStatus("current")

ruijieFrElmiMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 3, 2, 9)
)
ruijieFrElmiMIBGroup.setObjects(
      *(("RUIJIE-FRAME-RELAY-MIB", "ruijiefrElmiIpAddr"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrElmiArStatus"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrElmiRemoteStatus"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrElmiNeighborArStatus"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrElmiNeighborIpAddress"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrElmiNeighborIfIndex"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrElmiNeighborVendorName"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrElmiNeighborPlatformName"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrElmiNeighborDeviceName"))
)
if mibBuilder.loadTexts:
    ruijieFrElmiMIBGroup.setStatus("deprecated")

ruijieFrElmiMIBGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 3, 2, 10)
)
ruijieFrElmiMIBGroup1.setObjects(
      *(("RUIJIE-FRAME-RELAY-MIB", "ruijiefrElmiIpAddr"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrElmiArStatus"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrElmiRemoteStatus"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrElmiNeighborArStatus"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrElmiNeighborIpAddress"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrElmiNeighborIfIndex"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrElmiNeighborVendorName"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrElmiNeighborPlatformName"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrElmiNeighborDeviceName"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrElmiLinkStatus"))
)
if mibBuilder.loadTexts:
    ruijieFrElmiMIBGroup1.setStatus("current")

ruijieFrFragMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 3, 2, 11)
)
ruijieFrFragMIBGroup.setObjects(
      *(("RUIJIE-FRAME-RELAY-MIB", "ruijiefrFragSize"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrFragType"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrFragInPkts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrFragOutPkts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrFragInOctets"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrFragOutOctets"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrFragNotInPkts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrFragNotOutPkts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrFragNotInOctets"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrFragNotOutOctets"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrFragAssembledInPkts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrFragAssembledInOctets"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrFragPreOutPkts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrFragPreOutOctets"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrFragDroppedReAssembledInPkts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrFragDroppedFragmentedOutPkts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrFragTimeoutsIn"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrFragOutOfSeqFragPkts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrFragUnexpectedBBitSetPkts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrFragSeqMissedPkts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrFragInterleavedOutPkts"))
)
if mibBuilder.loadTexts:
    ruijieFrFragMIBGroup.setStatus("current")

ruijieFrConnMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 3, 2, 12)
)
ruijieFrConnMIBGroup.setObjects(
      *(("RUIJIE-FRAME-RELAY-MIB", "ruijiefrConnName"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrConnID"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrConnState"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrConnSegment1Name"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrConnSegment1VCGroup"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrConnSegment1Dlci"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrConnSegment2Name"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrConnSegment2Vpi"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrConnSegment2Vci"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrConnServiceTranslation"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrConnFrSscsDlci"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrConnEfciBit"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrConnDeBit"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrConnClpBit"))
)
if mibBuilder.loadTexts:
    ruijieFrConnMIBGroup.setStatus("current")

ruijieExtCircuitMIBGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 3, 2, 13)
)
ruijieExtCircuitMIBGroup1.setObjects(
      *(("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitIfName"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitIfType"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitSubifIndex"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitMapStatus"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitCreateType"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitMulticast"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitRoutedDlci"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitRoutedIf"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitUncompressIns"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitUncompressOuts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitFECNOuts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitBECNOuts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitMinThruputOut"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitMinThruputIn"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitBcastPktOuts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitBcastByteOuts"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitBandwidth"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitTxDataRate"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitTxPktRate"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitRcvDataRate"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijiefrExtCircuitRcvPktRate"))
)
if mibBuilder.loadTexts:
    ruijieExtCircuitMIBGroup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieFrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 3, 1, 1)
)
ruijieFrMIBCompliance.setObjects(
    ("RUIJIE-FRAME-RELAY-MIB", "ruijieFrMIBGroup")
)
if mibBuilder.loadTexts:
    ruijieFrMIBCompliance.setStatus(
        "obsolete"
    )

ruijieFrMIBCompliancesRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 3, 1, 2)
)
ruijieFrMIBCompliancesRev1.setObjects(
    ("RUIJIE-FRAME-RELAY-MIB", "ruijieFrMIBGroupRev1")
)
if mibBuilder.loadTexts:
    ruijieFrMIBCompliancesRev1.setStatus(
        "obsolete"
    )

ruijieFrMIBCompliancesRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 3, 1, 3)
)
ruijieFrMIBCompliancesRev2.setObjects(
      *(("RUIJIE-FRAME-RELAY-MIB", "ruijieFrLmiMIBGroup"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijieFrCircuitMIBGroup"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijieExtCircuitMIBGroup"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijieFrTsMIBGroup"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijieFrMapMIBGroup"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijieFrSvcMIBGroup"))
)
if mibBuilder.loadTexts:
    ruijieFrMIBCompliancesRev2.setStatus(
        "obsolete"
    )

ruijieFrMIBCompliancesRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 3, 1, 4)
)
ruijieFrMIBCompliancesRev3.setObjects(
      *(("RUIJIE-FRAME-RELAY-MIB", "ruijieFrLmiMIBGroup"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijieFrCircuitMIBGroup"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijieExtCircuitMIBGroup"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijieFrTsMIBGroup"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijieFrMapMIBGroup"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijieFrSvcMIBGroup"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijieFrElmiMIBGroup"))
)
if mibBuilder.loadTexts:
    ruijieFrMIBCompliancesRev3.setStatus(
        "deprecated"
    )

ruijieFrMIBCompliancesRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 50, 3, 1, 5)
)
ruijieFrMIBCompliancesRev4.setObjects(
      *(("RUIJIE-FRAME-RELAY-MIB", "ruijieFrLmiMIBGroup"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijieFrCircuitMIBGroup"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijieExtCircuitMIBGroup1"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijieFrTsMIBGroup"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijieFrMapMIBGroup"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijieFrSvcMIBGroup"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijieFrElmiMIBGroup1"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijieFrFragMIBGroup"),
        ("RUIJIE-FRAME-RELAY-MIB", "ruijieFrConnMIBGroup"))
)
if mibBuilder.loadTexts:
    ruijieFrMIBCompliancesRev4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-FRAME-RELAY-MIB",
    **{"DlciNumber": DlciNumber,
       "RuijiefrMapProtocols": RuijiefrMapProtocols,
       "ruijieFrameRelayMIB": ruijieFrameRelayMIB,
       "ruijieFrMIBObjects": ruijieFrMIBObjects,
       "ruijiefrLmiObjs": ruijiefrLmiObjs,
       "ruijiefrLmiTable": ruijiefrLmiTable,
       "ruijiefrLmiEntry": ruijiefrLmiEntry,
       "ruijiefrLmiLinkstatus": ruijiefrLmiLinkstatus,
       "ruijiefrLmiLinkType": ruijiefrLmiLinkType,
       "ruijiefrLmiEnquiryIns": ruijiefrLmiEnquiryIns,
       "ruijiefrLmiEnquiryOuts": ruijiefrLmiEnquiryOuts,
       "ruijiefrLmiStatusIns": ruijiefrLmiStatusIns,
       "ruijiefrLmiStatusOuts": ruijiefrLmiStatusOuts,
       "ruijiefrLmiUpdateStatusIns": ruijiefrLmiUpdateStatusIns,
       "ruijiefrLmiUpdateStatusOuts": ruijiefrLmiUpdateStatusOuts,
       "ruijiefrLmiStatusTimeouts": ruijiefrLmiStatusTimeouts,
       "ruijiefrLmiStatusEnqTimeouts": ruijiefrLmiStatusEnqTimeouts,
       "ruijiefrLmiN392Dce": ruijiefrLmiN392Dce,
       "ruijiefrLmiN393Dce": ruijiefrLmiN393Dce,
       "ruijiefrLmiT392Dce": ruijiefrLmiT392Dce,
       "ruijiefrCircuitObjs": ruijiefrCircuitObjs,
       "ruijiefrCircuitTable": ruijiefrCircuitTable,
       "ruijiefrCircuitEntry": ruijiefrCircuitEntry,
       "ruijiefrCircuitDEins": ruijiefrCircuitDEins,
       "ruijiefrCircuitDEouts": ruijiefrCircuitDEouts,
       "ruijiefrCircuitDropPktsOuts": ruijiefrCircuitDropPktsOuts,
       "ruijiefrCircuitType": ruijiefrCircuitType,
       "ruijiefrExtCircuitTable": ruijiefrExtCircuitTable,
       "ruijiefrExtCircuitEntry": ruijiefrExtCircuitEntry,
       "ruijiefrExtCircuitIfName": ruijiefrExtCircuitIfName,
       "ruijiefrExtCircuitIfType": ruijiefrExtCircuitIfType,
       "ruijiefrExtCircuitSubifIndex": ruijiefrExtCircuitSubifIndex,
       "ruijiefrExtCircuitMapStatus": ruijiefrExtCircuitMapStatus,
       "ruijiefrExtCircuitCreateType": ruijiefrExtCircuitCreateType,
       "ruijiefrExtCircuitMulticast": ruijiefrExtCircuitMulticast,
       "ruijiefrExtCircuitRoutedDlci": ruijiefrExtCircuitRoutedDlci,
       "ruijiefrExtCircuitRoutedIf": ruijiefrExtCircuitRoutedIf,
       "ruijiefrExtCircuitUncompressIns": ruijiefrExtCircuitUncompressIns,
       "ruijiefrExtCircuitUncompressOuts": ruijiefrExtCircuitUncompressOuts,
       "ruijiefrExtCircuitFECNOuts": ruijiefrExtCircuitFECNOuts,
       "ruijiefrExtCircuitBECNOuts": ruijiefrExtCircuitBECNOuts,
       "ruijiefrExtCircuitMinThruputOut": ruijiefrExtCircuitMinThruputOut,
       "ruijiefrExtCircuitMinThruputIn": ruijiefrExtCircuitMinThruputIn,
       "ruijiefrExtCircuitBcastPktOuts": ruijiefrExtCircuitBcastPktOuts,
       "ruijiefrExtCircuitBcastByteOuts": ruijiefrExtCircuitBcastByteOuts,
       "ruijiefrExtCircuitBandwidth": ruijiefrExtCircuitBandwidth,
       "ruijiefrExtCircuitShapeByteLimit": ruijiefrExtCircuitShapeByteLimit,
       "ruijiefrExtCircuitShapeInterval": ruijiefrExtCircuitShapeInterval,
       "ruijiefrExtCircuitShapeByteIncrement": ruijiefrExtCircuitShapeByteIncrement,
       "ruijiefrExtCircuitShapePkts": ruijiefrExtCircuitShapePkts,
       "ruijiefrExtCircuitShapeBytes": ruijiefrExtCircuitShapeBytes,
       "ruijiefrExtCircuitShapePktsDelay": ruijiefrExtCircuitShapePktsDelay,
       "ruijiefrExtCircuitShapeBytesDelay": ruijiefrExtCircuitShapeBytesDelay,
       "ruijiefrExtCircuitShapeActive": ruijiefrExtCircuitShapeActive,
       "ruijiefrExtCircuitShapeAdapting": ruijiefrExtCircuitShapeAdapting,
       "ruijiefrExtCircuitTxDataRate": ruijiefrExtCircuitTxDataRate,
       "ruijiefrExtCircuitTxPktRate": ruijiefrExtCircuitTxPktRate,
       "ruijiefrExtCircuitRcvDataRate": ruijiefrExtCircuitRcvDataRate,
       "ruijiefrExtCircuitRcvPktRate": ruijiefrExtCircuitRcvPktRate,
       "ruijiefrMapObjs": ruijiefrMapObjs,
       "ruijiefrMapTable": ruijiefrMapTable,
       "ruijiefrMapEntry": ruijiefrMapEntry,
       "ruijiefrMapIndex": ruijiefrMapIndex,
       "ruijiefrMapProtocol": ruijiefrMapProtocol,
       "ruijiefrMapAddress": ruijiefrMapAddress,
       "ruijiefrMapType": ruijiefrMapType,
       "ruijiefrMapEncaps": ruijiefrMapEncaps,
       "ruijiefrMapBroadcast": ruijiefrMapBroadcast,
       "ruijiefrMapPayloadCompress": ruijiefrMapPayloadCompress,
       "ruijiefrMapTcpHdrCompress": ruijiefrMapTcpHdrCompress,
       "ruijiefrMapRtpHdrCompress": ruijiefrMapRtpHdrCompress,
       "ruijiefrMapPayloadCompressType": ruijiefrMapPayloadCompressType,
       "ruijiefrSvcObjs": ruijiefrSvcObjs,
       "ruijiefrSvcTable": ruijiefrSvcTable,
       "ruijiefrSvcEntry": ruijiefrSvcEntry,
       "ruijiefrSvcAddrLocal": ruijiefrSvcAddrLocal,
       "ruijiefrSvcAddrRemote": ruijiefrSvcAddrRemote,
       "ruijiefrSvcThroughputIn": ruijiefrSvcThroughputIn,
       "ruijiefrSvcMinThruputOut": ruijiefrSvcMinThruputOut,
       "ruijiefrSvcMinThruputIn": ruijiefrSvcMinThruputIn,
       "ruijiefrSvcCommitBurstIn": ruijiefrSvcCommitBurstIn,
       "ruijiefrSvcExcessBurstIn": ruijiefrSvcExcessBurstIn,
       "ruijiefrSvcIdleTime": ruijiefrSvcIdleTime,
       "ruijiefrElmiObjs": ruijiefrElmiObjs,
       "ruijiefrElmiIpAddr": ruijiefrElmiIpAddr,
       "ruijiefrElmiTable": ruijiefrElmiTable,
       "ruijiefrElmiEntry": ruijiefrElmiEntry,
       "ruijiefrElmiLinkStatus": ruijiefrElmiLinkStatus,
       "ruijiefrElmiArStatus": ruijiefrElmiArStatus,
       "ruijiefrElmiRemoteStatus": ruijiefrElmiRemoteStatus,
       "ruijiefrElmiNeighborTable": ruijiefrElmiNeighborTable,
       "ruijiefrElmiNeighborEntry": ruijiefrElmiNeighborEntry,
       "ruijiefrElmiNeighborArStatus": ruijiefrElmiNeighborArStatus,
       "ruijiefrElmiNeighborIpAddress": ruijiefrElmiNeighborIpAddress,
       "ruijiefrElmiNeighborIfIndex": ruijiefrElmiNeighborIfIndex,
       "ruijiefrElmiNeighborVendorName": ruijiefrElmiNeighborVendorName,
       "ruijiefrElmiNeighborPlatformName": ruijiefrElmiNeighborPlatformName,
       "ruijiefrElmiNeighborDeviceName": ruijiefrElmiNeighborDeviceName,
       "ruijiefrFragObjs": ruijiefrFragObjs,
       "ruijiefrFragTable": ruijiefrFragTable,
       "ruijiefrFragEntry": ruijiefrFragEntry,
       "ruijiefrFragSize": ruijiefrFragSize,
       "ruijiefrFragType": ruijiefrFragType,
       "ruijiefrFragInPkts": ruijiefrFragInPkts,
       "ruijiefrFragOutPkts": ruijiefrFragOutPkts,
       "ruijiefrFragInOctets": ruijiefrFragInOctets,
       "ruijiefrFragOutOctets": ruijiefrFragOutOctets,
       "ruijiefrFragNotInPkts": ruijiefrFragNotInPkts,
       "ruijiefrFragNotOutPkts": ruijiefrFragNotOutPkts,
       "ruijiefrFragNotInOctets": ruijiefrFragNotInOctets,
       "ruijiefrFragNotOutOctets": ruijiefrFragNotOutOctets,
       "ruijiefrFragAssembledInPkts": ruijiefrFragAssembledInPkts,
       "ruijiefrFragAssembledInOctets": ruijiefrFragAssembledInOctets,
       "ruijiefrFragPreOutPkts": ruijiefrFragPreOutPkts,
       "ruijiefrFragPreOutOctets": ruijiefrFragPreOutOctets,
       "ruijiefrFragDroppedReAssembledInPkts": ruijiefrFragDroppedReAssembledInPkts,
       "ruijiefrFragDroppedFragmentedOutPkts": ruijiefrFragDroppedFragmentedOutPkts,
       "ruijiefrFragTimeoutsIn": ruijiefrFragTimeoutsIn,
       "ruijiefrFragOutOfSeqFragPkts": ruijiefrFragOutOfSeqFragPkts,
       "ruijiefrFragUnexpectedBBitSetPkts": ruijiefrFragUnexpectedBBitSetPkts,
       "ruijiefrFragSeqMissedPkts": ruijiefrFragSeqMissedPkts,
       "ruijiefrFragInterleavedOutPkts": ruijiefrFragInterleavedOutPkts,
       "ruijiefrConnectionObjs": ruijiefrConnectionObjs,
       "ruijiefrConnectionTable": ruijiefrConnectionTable,
       "ruijiefrConnectionEntry": ruijiefrConnectionEntry,
       "ruijiefrConnName": ruijiefrConnName,
       "ruijiefrConnID": ruijiefrConnID,
       "ruijiefrConnState": ruijiefrConnState,
       "ruijiefrConnSegment1Name": ruijiefrConnSegment1Name,
       "ruijiefrConnSegment1VCGroup": ruijiefrConnSegment1VCGroup,
       "ruijiefrConnSegment1Dlci": ruijiefrConnSegment1Dlci,
       "ruijiefrConnSegment2Name": ruijiefrConnSegment2Name,
       "ruijiefrConnSegment2Vpi": ruijiefrConnSegment2Vpi,
       "ruijiefrConnSegment2Vci": ruijiefrConnSegment2Vci,
       "ruijiefrConnServiceTranslation": ruijiefrConnServiceTranslation,
       "ruijiefrConnFrSscsDlci": ruijiefrConnFrSscsDlci,
       "ruijiefrConnEfciBit": ruijiefrConnEfciBit,
       "ruijiefrConnDeBit": ruijiefrConnDeBit,
       "ruijiefrConnClpBit": ruijiefrConnClpBit,
       "ruijieFrMIBConformance": ruijieFrMIBConformance,
       "ruijieFrMIBCompliances": ruijieFrMIBCompliances,
       "ruijieFrMIBCompliance": ruijieFrMIBCompliance,
       "ruijieFrMIBCompliancesRev1": ruijieFrMIBCompliancesRev1,
       "ruijieFrMIBCompliancesRev2": ruijieFrMIBCompliancesRev2,
       "ruijieFrMIBCompliancesRev3": ruijieFrMIBCompliancesRev3,
       "ruijieFrMIBCompliancesRev4": ruijieFrMIBCompliancesRev4,
       "ruijieFrMIBGroups": ruijieFrMIBGroups,
       "ruijieFrMIBGroup": ruijieFrMIBGroup,
       "ruijieFrMIBGroupRev1": ruijieFrMIBGroupRev1,
       "ruijieFrLmiMIBGroup": ruijieFrLmiMIBGroup,
       "ruijieFrCircuitMIBGroup": ruijieFrCircuitMIBGroup,
       "ruijieExtCircuitMIBGroup": ruijieExtCircuitMIBGroup,
       "ruijieFrTsMIBGroup": ruijieFrTsMIBGroup,
       "ruijieFrMapMIBGroup": ruijieFrMapMIBGroup,
       "ruijieFrSvcMIBGroup": ruijieFrSvcMIBGroup,
       "ruijieFrElmiMIBGroup": ruijieFrElmiMIBGroup,
       "ruijieFrElmiMIBGroup1": ruijieFrElmiMIBGroup1,
       "ruijieFrFragMIBGroup": ruijieFrFragMIBGroup,
       "ruijieFrConnMIBGroup": ruijieFrConnMIBGroup,
       "ruijieExtCircuitMIBGroup1": ruijieExtCircuitMIBGroup1}
)
