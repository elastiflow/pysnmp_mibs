# SNMP MIB module (RUIJIE-ACL-CONTEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-ACL-CONTEXT-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:06:22 2025
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

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "ConfigStatus",
    "IfIndex")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruijieAclVCMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66)
)
if mibBuilder.loadTexts:
    ruijieAclVCMIB.setRevisions(
        ("2009-12-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieAclVCMIBObjects_ObjectIdentity = ObjectIdentity
ruijieAclVCMIBObjects = _RuijieAclVCMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1)
)
_RuijieAclVCTable_Object = MibTable
ruijieAclVCTable = _RuijieAclVCTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieAclVCTable.setStatus("current")
_RuijieAclVCEntry_Object = MibTableRow
ruijieAclVCEntry = _RuijieAclVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 1, 1)
)
ruijieAclVCEntry.setIndexNames(
    (0, "RUIJIE-ACL-CONTEXT-MIB", "ruijieAclContextNameVC"),
    (0, "RUIJIE-ACL-CONTEXT-MIB", "ruijieAclNameVC"),
)
if mibBuilder.loadTexts:
    ruijieAclVCEntry.setStatus("current")


class _RuijieAclContextNameVC_Type(DisplayString):
    """Custom type ruijieAclContextNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_RuijieAclContextNameVC_Type.__name__ = "DisplayString"
_RuijieAclContextNameVC_Object = MibTableColumn
ruijieAclContextNameVC = _RuijieAclContextNameVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 1, 1, 1),
    _RuijieAclContextNameVC_Type()
)
ruijieAclContextNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAclContextNameVC.setStatus("current")


class _RuijieAclNameVC_Type(DisplayString):
    """Custom type ruijieAclNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieAclNameVC_Type.__name__ = "DisplayString"
_RuijieAclNameVC_Object = MibTableColumn
ruijieAclNameVC = _RuijieAclNameVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 1, 1, 2),
    _RuijieAclNameVC_Type()
)
ruijieAclNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAclNameVC.setStatus("current")


class _RuijieAclModeVC_Type(Integer32):
    """Custom type ruijieAclModeVC based on Integer32"""
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
        *(("acl-ip-standard", 1),
          ("acl-ip-extended", 2),
          ("acl-mac-extended", 3),
          ("acl-expert", 4),
          ("acl-ipv6-extended", 5))
    )


_RuijieAclModeVC_Type.__name__ = "Integer32"
_RuijieAclModeVC_Object = MibTableColumn
ruijieAclModeVC = _RuijieAclModeVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 1, 1, 3),
    _RuijieAclModeVC_Type()
)
ruijieAclModeVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAclModeVC.setStatus("current")
_RuijieAclEntryStatusVC_Type = ConfigStatus
_RuijieAclEntryStatusVC_Object = MibTableColumn
ruijieAclEntryStatusVC = _RuijieAclEntryStatusVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 1, 1, 4),
    _RuijieAclEntryStatusVC_Type()
)
ruijieAclEntryStatusVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAclEntryStatusVC.setStatus("current")
_RuijieAclIfVCTable_Object = MibTable
ruijieAclIfVCTable = _RuijieAclIfVCTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieAclIfVCTable.setStatus("current")
_RuijieAclIfVCEntry_Object = MibTableRow
ruijieAclIfVCEntry = _RuijieAclIfVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 2, 1)
)
ruijieAclIfVCEntry.setIndexNames(
    (0, "RUIJIE-ACL-CONTEXT-MIB", "ruijieAclIfContextNameVC"),
    (0, "RUIJIE-ACL-CONTEXT-MIB", "ruijieAclIfIndexVC"),
)
if mibBuilder.loadTexts:
    ruijieAclIfVCEntry.setStatus("current")


class _RuijieAclIfContextNameVC_Type(DisplayString):
    """Custom type ruijieAclIfContextNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_RuijieAclIfContextNameVC_Type.__name__ = "DisplayString"
_RuijieAclIfContextNameVC_Object = MibTableColumn
ruijieAclIfContextNameVC = _RuijieAclIfContextNameVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 2, 1, 1),
    _RuijieAclIfContextNameVC_Type()
)
ruijieAclIfContextNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAclIfContextNameVC.setStatus("current")
_RuijieAclIfIndexVC_Type = IfIndex
_RuijieAclIfIndexVC_Object = MibTableColumn
ruijieAclIfIndexVC = _RuijieAclIfIndexVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 2, 1, 2),
    _RuijieAclIfIndexVC_Type()
)
ruijieAclIfIndexVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAclIfIndexVC.setStatus("current")
_RuijieAclIfMaxEntryNumVC_Type = Integer32
_RuijieAclIfMaxEntryNumVC_Object = MibTableColumn
ruijieAclIfMaxEntryNumVC = _RuijieAclIfMaxEntryNumVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 2, 1, 3),
    _RuijieAclIfMaxEntryNumVC_Type()
)
ruijieAclIfMaxEntryNumVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAclIfMaxEntryNumVC.setStatus("current")
_RuijieAclIfCurruntEntryNumVC_Type = Integer32
_RuijieAclIfCurruntEntryNumVC_Object = MibTableColumn
ruijieAclIfCurruntEntryNumVC = _RuijieAclIfCurruntEntryNumVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 2, 1, 4),
    _RuijieAclIfCurruntEntryNumVC_Type()
)
ruijieAclIfCurruntEntryNumVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAclIfCurruntEntryNumVC.setStatus("current")


class _RuijieIfInAclNameVC_Type(DisplayString):
    """Custom type ruijieIfInAclNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieIfInAclNameVC_Type.__name__ = "DisplayString"
_RuijieIfInAclNameVC_Object = MibTableColumn
ruijieIfInAclNameVC = _RuijieIfInAclNameVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 2, 1, 5),
    _RuijieIfInAclNameVC_Type()
)
ruijieIfInAclNameVC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIfInAclNameVC.setStatus("current")


class _RuijieIfOutAclNameVC_Type(DisplayString):
    """Custom type ruijieIfOutAclNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieIfOutAclNameVC_Type.__name__ = "DisplayString"
_RuijieIfOutAclNameVC_Object = MibTableColumn
ruijieIfOutAclNameVC = _RuijieIfOutAclNameVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 2, 1, 6),
    _RuijieIfOutAclNameVC_Type()
)
ruijieIfOutAclNameVC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIfOutAclNameVC.setStatus("current")
_RuijieAceExtVCTable_Object = MibTable
ruijieAceExtVCTable = _RuijieAceExtVCTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3)
)
if mibBuilder.loadTexts:
    ruijieAceExtVCTable.setStatus("current")
_RuijieAceExtVCEntry_Object = MibTableRow
ruijieAceExtVCEntry = _RuijieAceExtVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1)
)
ruijieAceExtVCEntry.setIndexNames(
    (0, "RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtContextNameVC"),
    (0, "RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtAclNameVC"),
    (0, "RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtIndexVC"),
)
if mibBuilder.loadTexts:
    ruijieAceExtVCEntry.setStatus("current")


class _RuijieAceExtContextNameVC_Type(DisplayString):
    """Custom type ruijieAceExtContextNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_RuijieAceExtContextNameVC_Type.__name__ = "DisplayString"
_RuijieAceExtContextNameVC_Object = MibTableColumn
ruijieAceExtContextNameVC = _RuijieAceExtContextNameVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 1),
    _RuijieAceExtContextNameVC_Type()
)
ruijieAceExtContextNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAceExtContextNameVC.setStatus("current")


class _RuijieAceExtAclNameVC_Type(DisplayString):
    """Custom type ruijieAceExtAclNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieAceExtAclNameVC_Type.__name__ = "DisplayString"
_RuijieAceExtAclNameVC_Object = MibTableColumn
ruijieAceExtAclNameVC = _RuijieAceExtAclNameVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 2),
    _RuijieAceExtAclNameVC_Type()
)
ruijieAceExtAclNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAceExtAclNameVC.setStatus("current")


class _RuijieAceExtIndexVC_Type(Integer32):
    """Custom type ruijieAceExtIndexVC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RuijieAceExtIndexVC_Type.__name__ = "Integer32"
_RuijieAceExtIndexVC_Object = MibTableColumn
ruijieAceExtIndexVC = _RuijieAceExtIndexVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 3),
    _RuijieAceExtIndexVC_Type()
)
ruijieAceExtIndexVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAceExtIndexVC.setStatus("current")


class _RuijieAceExtIfAnyVIDVC_Type(TruthValue):
    """Custom type ruijieAceExtIfAnyVIDVC based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnyVIDVC_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnyVIDVC_Object = MibTableColumn
ruijieAceExtIfAnyVIDVC = _RuijieAceExtIfAnyVIDVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 4),
    _RuijieAceExtIfAnyVIDVC_Type()
)
ruijieAceExtIfAnyVIDVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnyVIDVC.setStatus("current")


class _RuijieAceExtVIDVC_Type(Unsigned32):
    """Custom type ruijieAceExtVIDVC based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_RuijieAceExtVIDVC_Type.__name__ = "Unsigned32"
_RuijieAceExtVIDVC_Object = MibTableColumn
ruijieAceExtVIDVC = _RuijieAceExtVIDVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 5),
    _RuijieAceExtVIDVC_Type()
)
ruijieAceExtVIDVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtVIDVC.setStatus("current")


class _RuijieAceExtIfAnySourceIpVC_Type(TruthValue):
    """Custom type ruijieAceExtIfAnySourceIpVC based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnySourceIpVC_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnySourceIpVC_Object = MibTableColumn
ruijieAceExtIfAnySourceIpVC = _RuijieAceExtIfAnySourceIpVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 6),
    _RuijieAceExtIfAnySourceIpVC_Type()
)
ruijieAceExtIfAnySourceIpVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnySourceIpVC.setStatus("current")
_RuijieAceExtSourceIpVC_Type = IpAddress
_RuijieAceExtSourceIpVC_Object = MibTableColumn
ruijieAceExtSourceIpVC = _RuijieAceExtSourceIpVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 7),
    _RuijieAceExtSourceIpVC_Type()
)
ruijieAceExtSourceIpVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtSourceIpVC.setStatus("current")


class _RuijieAceExtIfAnySourceWildCardVC_Type(TruthValue):
    """Custom type ruijieAceExtIfAnySourceWildCardVC based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnySourceWildCardVC_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnySourceWildCardVC_Object = MibTableColumn
ruijieAceExtIfAnySourceWildCardVC = _RuijieAceExtIfAnySourceWildCardVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 8),
    _RuijieAceExtIfAnySourceWildCardVC_Type()
)
ruijieAceExtIfAnySourceWildCardVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnySourceWildCardVC.setStatus("current")
_RuijieAceExtSourceWildCardVC_Type = IpAddress
_RuijieAceExtSourceWildCardVC_Object = MibTableColumn
ruijieAceExtSourceWildCardVC = _RuijieAceExtSourceWildCardVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 9),
    _RuijieAceExtSourceWildCardVC_Type()
)
ruijieAceExtSourceWildCardVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtSourceWildCardVC.setStatus("current")


class _RuijieAceExtIfAnySourceMacAddrVC_Type(TruthValue):
    """Custom type ruijieAceExtIfAnySourceMacAddrVC based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnySourceMacAddrVC_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnySourceMacAddrVC_Object = MibTableColumn
ruijieAceExtIfAnySourceMacAddrVC = _RuijieAceExtIfAnySourceMacAddrVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 10),
    _RuijieAceExtIfAnySourceMacAddrVC_Type()
)
ruijieAceExtIfAnySourceMacAddrVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnySourceMacAddrVC.setStatus("current")
_RuijieAceExtSourceMacAddrVC_Type = MacAddress
_RuijieAceExtSourceMacAddrVC_Object = MibTableColumn
ruijieAceExtSourceMacAddrVC = _RuijieAceExtSourceMacAddrVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 11),
    _RuijieAceExtSourceMacAddrVC_Type()
)
ruijieAceExtSourceMacAddrVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtSourceMacAddrVC.setStatus("current")


class _RuijieAceExtIfAnyDestIpVC_Type(TruthValue):
    """Custom type ruijieAceExtIfAnyDestIpVC based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnyDestIpVC_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnyDestIpVC_Object = MibTableColumn
ruijieAceExtIfAnyDestIpVC = _RuijieAceExtIfAnyDestIpVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 12),
    _RuijieAceExtIfAnyDestIpVC_Type()
)
ruijieAceExtIfAnyDestIpVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnyDestIpVC.setStatus("current")
_RuijieAceExtDestIpVC_Type = IpAddress
_RuijieAceExtDestIpVC_Object = MibTableColumn
ruijieAceExtDestIpVC = _RuijieAceExtDestIpVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 13),
    _RuijieAceExtDestIpVC_Type()
)
ruijieAceExtDestIpVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtDestIpVC.setStatus("current")


class _RuijieAceExtIfAnyDestWildCardVC_Type(TruthValue):
    """Custom type ruijieAceExtIfAnyDestWildCardVC based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnyDestWildCardVC_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnyDestWildCardVC_Object = MibTableColumn
ruijieAceExtIfAnyDestWildCardVC = _RuijieAceExtIfAnyDestWildCardVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 14),
    _RuijieAceExtIfAnyDestWildCardVC_Type()
)
ruijieAceExtIfAnyDestWildCardVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnyDestWildCardVC.setStatus("current")
_RuijieAceExtDestIpWildCardVC_Type = IpAddress
_RuijieAceExtDestIpWildCardVC_Object = MibTableColumn
ruijieAceExtDestIpWildCardVC = _RuijieAceExtDestIpWildCardVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 15),
    _RuijieAceExtDestIpWildCardVC_Type()
)
ruijieAceExtDestIpWildCardVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtDestIpWildCardVC.setStatus("current")


class _RuijieAceExtIfAnyDestMacAddrVC_Type(TruthValue):
    """Custom type ruijieAceExtIfAnyDestMacAddrVC based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnyDestMacAddrVC_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnyDestMacAddrVC_Object = MibTableColumn
ruijieAceExtIfAnyDestMacAddrVC = _RuijieAceExtIfAnyDestMacAddrVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 16),
    _RuijieAceExtIfAnyDestMacAddrVC_Type()
)
ruijieAceExtIfAnyDestMacAddrVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnyDestMacAddrVC.setStatus("current")
_RuijieAceExtDestMacAddrVC_Type = MacAddress
_RuijieAceExtDestMacAddrVC_Object = MibTableColumn
ruijieAceExtDestMacAddrVC = _RuijieAceExtDestMacAddrVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 17),
    _RuijieAceExtDestMacAddrVC_Type()
)
ruijieAceExtDestMacAddrVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtDestMacAddrVC.setStatus("current")


class _RuijieAceExtIfAnyEtherLikeTypeVC_Type(TruthValue):
    """Custom type ruijieAceExtIfAnyEtherLikeTypeVC based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnyEtherLikeTypeVC_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnyEtherLikeTypeVC_Object = MibTableColumn
ruijieAceExtIfAnyEtherLikeTypeVC = _RuijieAceExtIfAnyEtherLikeTypeVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 18),
    _RuijieAceExtIfAnyEtherLikeTypeVC_Type()
)
ruijieAceExtIfAnyEtherLikeTypeVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnyEtherLikeTypeVC.setStatus("current")
_RuijieAceExtEtherLikeTypeVC_Type = Integer32
_RuijieAceExtEtherLikeTypeVC_Object = MibTableColumn
ruijieAceExtEtherLikeTypeVC = _RuijieAceExtEtherLikeTypeVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 19),
    _RuijieAceExtEtherLikeTypeVC_Type()
)
ruijieAceExtEtherLikeTypeVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtEtherLikeTypeVC.setStatus("current")


class _RuijieAceExtIfAnyIpProtocolFieldVC_Type(TruthValue):
    """Custom type ruijieAceExtIfAnyIpProtocolFieldVC based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnyIpProtocolFieldVC_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnyIpProtocolFieldVC_Object = MibTableColumn
ruijieAceExtIfAnyIpProtocolFieldVC = _RuijieAceExtIfAnyIpProtocolFieldVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 20),
    _RuijieAceExtIfAnyIpProtocolFieldVC_Type()
)
ruijieAceExtIfAnyIpProtocolFieldVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnyIpProtocolFieldVC.setStatus("current")
_RuijieAceExtIpProtocolFieldVC_Type = Integer32
_RuijieAceExtIpProtocolFieldVC_Object = MibTableColumn
ruijieAceExtIpProtocolFieldVC = _RuijieAceExtIpProtocolFieldVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 21),
    _RuijieAceExtIpProtocolFieldVC_Type()
)
ruijieAceExtIpProtocolFieldVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtIpProtocolFieldVC.setStatus("current")
_RuijieAceExtSourceProtocolPortVC_Type = Integer32
_RuijieAceExtSourceProtocolPortVC_Object = MibTableColumn
ruijieAceExtSourceProtocolPortVC = _RuijieAceExtSourceProtocolPortVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 22),
    _RuijieAceExtSourceProtocolPortVC_Type()
)
ruijieAceExtSourceProtocolPortVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtSourceProtocolPortVC.setStatus("current")
_RuijieAceExtDestProtocolPortVC_Type = Integer32
_RuijieAceExtDestProtocolPortVC_Object = MibTableColumn
ruijieAceExtDestProtocolPortVC = _RuijieAceExtDestProtocolPortVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 23),
    _RuijieAceExtDestProtocolPortVC_Type()
)
ruijieAceExtDestProtocolPortVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtDestProtocolPortVC.setStatus("current")


class _RuijieAceExtIfAnyProtocolTypeVC_Type(TruthValue):
    """Custom type ruijieAceExtIfAnyProtocolTypeVC based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnyProtocolTypeVC_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnyProtocolTypeVC_Object = MibTableColumn
ruijieAceExtIfAnyProtocolTypeVC = _RuijieAceExtIfAnyProtocolTypeVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 24),
    _RuijieAceExtIfAnyProtocolTypeVC_Type()
)
ruijieAceExtIfAnyProtocolTypeVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnyProtocolTypeVC.setStatus("current")
_RuijieAceExtProtocolTypeVC_Type = Integer32
_RuijieAceExtProtocolTypeVC_Object = MibTableColumn
ruijieAceExtProtocolTypeVC = _RuijieAceExtProtocolTypeVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 25),
    _RuijieAceExtProtocolTypeVC_Type()
)
ruijieAceExtProtocolTypeVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtProtocolTypeVC.setStatus("current")


class _RuijieAceExtFlowActionVC_Type(Integer32):
    """Custom type ruijieAceExtFlowActionVC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_RuijieAceExtFlowActionVC_Type.__name__ = "Integer32"
_RuijieAceExtFlowActionVC_Object = MibTableColumn
ruijieAceExtFlowActionVC = _RuijieAceExtFlowActionVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 26),
    _RuijieAceExtFlowActionVC_Type()
)
ruijieAceExtFlowActionVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtFlowActionVC.setStatus("current")
_RuijieAceExtEntryStautsVC_Type = RowStatus
_RuijieAceExtEntryStautsVC_Object = MibTableColumn
ruijieAceExtEntryStautsVC = _RuijieAceExtEntryStautsVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 27),
    _RuijieAceExtEntryStautsVC_Type()
)
ruijieAceExtEntryStautsVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtEntryStautsVC.setStatus("current")


class _RuijieAceExtTimeRangeNameVC_Type(DisplayString):
    """Custom type ruijieAceExtTimeRangeNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieAceExtTimeRangeNameVC_Type.__name__ = "DisplayString"
_RuijieAceExtTimeRangeNameVC_Object = MibTableColumn
ruijieAceExtTimeRangeNameVC = _RuijieAceExtTimeRangeNameVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 28),
    _RuijieAceExtTimeRangeNameVC_Type()
)
ruijieAceExtTimeRangeNameVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtTimeRangeNameVC.setStatus("current")


class _RuijieAceExtSourcePortOpVC_Type(Integer32):
    """Custom type ruijieAceExtSourcePortOpVC based on Integer32"""
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
        *(("noOperator", 1),
          ("lt", 2),
          ("gt", 3),
          ("eq", 4),
          ("neq", 5),
          ("range", 6))
    )


_RuijieAceExtSourcePortOpVC_Type.__name__ = "Integer32"
_RuijieAceExtSourcePortOpVC_Object = MibTableColumn
ruijieAceExtSourcePortOpVC = _RuijieAceExtSourcePortOpVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 29),
    _RuijieAceExtSourcePortOpVC_Type()
)
ruijieAceExtSourcePortOpVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtSourcePortOpVC.setStatus("current")
_RuijieAceExtSourceProtocolPortRangeVC_Type = Integer32
_RuijieAceExtSourceProtocolPortRangeVC_Object = MibTableColumn
ruijieAceExtSourceProtocolPortRangeVC = _RuijieAceExtSourceProtocolPortRangeVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 30),
    _RuijieAceExtSourceProtocolPortRangeVC_Type()
)
ruijieAceExtSourceProtocolPortRangeVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtSourceProtocolPortRangeVC.setStatus("current")


class _RuijieAceExtDestPortOpVC_Type(Integer32):
    """Custom type ruijieAceExtDestPortOpVC based on Integer32"""
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
        *(("noOperator", 1),
          ("lt", 2),
          ("gt", 3),
          ("eq", 4),
          ("neq", 5),
          ("range", 6))
    )


_RuijieAceExtDestPortOpVC_Type.__name__ = "Integer32"
_RuijieAceExtDestPortOpVC_Object = MibTableColumn
ruijieAceExtDestPortOpVC = _RuijieAceExtDestPortOpVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 31),
    _RuijieAceExtDestPortOpVC_Type()
)
ruijieAceExtDestPortOpVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtDestPortOpVC.setStatus("current")
_RuijieAceExtDestProtocolPortRangeVC_Type = Integer32
_RuijieAceExtDestProtocolPortRangeVC_Object = MibTableColumn
ruijieAceExtDestProtocolPortRangeVC = _RuijieAceExtDestProtocolPortRangeVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 32),
    _RuijieAceExtDestProtocolPortRangeVC_Type()
)
ruijieAceExtDestProtocolPortRangeVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtDestProtocolPortRangeVC.setStatus("current")


class _RuijieAceExtIfAnyCosVC_Type(TruthValue):
    """Custom type ruijieAceExtIfAnyCosVC based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnyCosVC_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnyCosVC_Object = MibTableColumn
ruijieAceExtIfAnyCosVC = _RuijieAceExtIfAnyCosVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 33),
    _RuijieAceExtIfAnyCosVC_Type()
)
ruijieAceExtIfAnyCosVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnyCosVC.setStatus("current")
_RuijieAceExtCosVC_Type = Integer32
_RuijieAceExtCosVC_Object = MibTableColumn
ruijieAceExtCosVC = _RuijieAceExtCosVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 34),
    _RuijieAceExtCosVC_Type()
)
ruijieAceExtCosVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtCosVC.setStatus("current")


class _RuijieAceExtIfAnyIpPrecVC_Type(TruthValue):
    """Custom type ruijieAceExtIfAnyIpPrecVC based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnyIpPrecVC_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnyIpPrecVC_Object = MibTableColumn
ruijieAceExtIfAnyIpPrecVC = _RuijieAceExtIfAnyIpPrecVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 35),
    _RuijieAceExtIfAnyIpPrecVC_Type()
)
ruijieAceExtIfAnyIpPrecVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnyIpPrecVC.setStatus("current")
_RuijieAceExtIpPrecVC_Type = Integer32
_RuijieAceExtIpPrecVC_Object = MibTableColumn
ruijieAceExtIpPrecVC = _RuijieAceExtIpPrecVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 36),
    _RuijieAceExtIpPrecVC_Type()
)
ruijieAceExtIpPrecVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtIpPrecVC.setStatus("current")


class _RuijieAceExtIfAnyDscpVC_Type(TruthValue):
    """Custom type ruijieAceExtIfAnyDscpVC based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnyDscpVC_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnyDscpVC_Object = MibTableColumn
ruijieAceExtIfAnyDscpVC = _RuijieAceExtIfAnyDscpVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 37),
    _RuijieAceExtIfAnyDscpVC_Type()
)
ruijieAceExtIfAnyDscpVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnyDscpVC.setStatus("current")
_RuijieAceExtDscpVC_Type = Integer32
_RuijieAceExtDscpVC_Object = MibTableColumn
ruijieAceExtDscpVC = _RuijieAceExtDscpVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 38),
    _RuijieAceExtDscpVC_Type()
)
ruijieAceExtDscpVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtDscpVC.setStatus("current")


class _RuijieAceExtIfAnyTcpFlagVC_Type(TruthValue):
    """Custom type ruijieAceExtIfAnyTcpFlagVC based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnyTcpFlagVC_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnyTcpFlagVC_Object = MibTableColumn
ruijieAceExtIfAnyTcpFlagVC = _RuijieAceExtIfAnyTcpFlagVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 39),
    _RuijieAceExtIfAnyTcpFlagVC_Type()
)
ruijieAceExtIfAnyTcpFlagVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnyTcpFlagVC.setStatus("current")
_RuijieAceExtTcpFlagVC_Type = Integer32
_RuijieAceExtTcpFlagVC_Object = MibTableColumn
ruijieAceExtTcpFlagVC = _RuijieAceExtTcpFlagVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 40),
    _RuijieAceExtTcpFlagVC_Type()
)
ruijieAceExtTcpFlagVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtTcpFlagVC.setStatus("current")


class _RuijieAceExtIfAnySourceMacAddrWildCardVC_Type(TruthValue):
    """Custom type ruijieAceExtIfAnySourceMacAddrWildCardVC based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnySourceMacAddrWildCardVC_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnySourceMacAddrWildCardVC_Object = MibTableColumn
ruijieAceExtIfAnySourceMacAddrWildCardVC = _RuijieAceExtIfAnySourceMacAddrWildCardVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 41),
    _RuijieAceExtIfAnySourceMacAddrWildCardVC_Type()
)
ruijieAceExtIfAnySourceMacAddrWildCardVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnySourceMacAddrWildCardVC.setStatus("current")
_RuijieAceExtSourceMacAddrWildCardVC_Type = MacAddress
_RuijieAceExtSourceMacAddrWildCardVC_Object = MibTableColumn
ruijieAceExtSourceMacAddrWildCardVC = _RuijieAceExtSourceMacAddrWildCardVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 42),
    _RuijieAceExtSourceMacAddrWildCardVC_Type()
)
ruijieAceExtSourceMacAddrWildCardVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtSourceMacAddrWildCardVC.setStatus("current")


class _RuijieAceExtIfAnyDestMacAddrWildCardVC_Type(TruthValue):
    """Custom type ruijieAceExtIfAnyDestMacAddrWildCardVC based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnyDestMacAddrWildCardVC_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnyDestMacAddrWildCardVC_Object = MibTableColumn
ruijieAceExtIfAnyDestMacAddrWildCardVC = _RuijieAceExtIfAnyDestMacAddrWildCardVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 43),
    _RuijieAceExtIfAnyDestMacAddrWildCardVC_Type()
)
ruijieAceExtIfAnyDestMacAddrWildCardVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnyDestMacAddrWildCardVC.setStatus("current")
_RuijieAceExtDestMacAddrWildCardVC_Type = MacAddress
_RuijieAceExtDestMacAddrWildCardVC_Object = MibTableColumn
ruijieAceExtDestMacAddrWildCardVC = _RuijieAceExtDestMacAddrWildCardVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 44),
    _RuijieAceExtDestMacAddrWildCardVC_Type()
)
ruijieAceExtDestMacAddrWildCardVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtDestMacAddrWildCardVC.setStatus("current")


class _RuijieAceExtIfAnySourceIp6VC_Type(TruthValue):
    """Custom type ruijieAceExtIfAnySourceIp6VC based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnySourceIp6VC_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnySourceIp6VC_Object = MibTableColumn
ruijieAceExtIfAnySourceIp6VC = _RuijieAceExtIfAnySourceIp6VC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 45),
    _RuijieAceExtIfAnySourceIp6VC_Type()
)
ruijieAceExtIfAnySourceIp6VC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnySourceIp6VC.setStatus("current")


class _RuijieAceExtSourceIp6VC_Type(OctetString):
    """Custom type ruijieAceExtSourceIp6VC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_RuijieAceExtSourceIp6VC_Type.__name__ = "OctetString"
_RuijieAceExtSourceIp6VC_Object = MibTableColumn
ruijieAceExtSourceIp6VC = _RuijieAceExtSourceIp6VC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 46),
    _RuijieAceExtSourceIp6VC_Type()
)
ruijieAceExtSourceIp6VC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtSourceIp6VC.setStatus("current")


class _RuijieAceExtIfAnySourceIp6WildCardVC_Type(TruthValue):
    """Custom type ruijieAceExtIfAnySourceIp6WildCardVC based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnySourceIp6WildCardVC_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnySourceIp6WildCardVC_Object = MibTableColumn
ruijieAceExtIfAnySourceIp6WildCardVC = _RuijieAceExtIfAnySourceIp6WildCardVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 47),
    _RuijieAceExtIfAnySourceIp6WildCardVC_Type()
)
ruijieAceExtIfAnySourceIp6WildCardVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnySourceIp6WildCardVC.setStatus("current")


class _RuijieAceExtSourceIp6WildCardVC_Type(OctetString):
    """Custom type ruijieAceExtSourceIp6WildCardVC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_RuijieAceExtSourceIp6WildCardVC_Type.__name__ = "OctetString"
_RuijieAceExtSourceIp6WildCardVC_Object = MibTableColumn
ruijieAceExtSourceIp6WildCardVC = _RuijieAceExtSourceIp6WildCardVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 48),
    _RuijieAceExtSourceIp6WildCardVC_Type()
)
ruijieAceExtSourceIp6WildCardVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtSourceIp6WildCardVC.setStatus("current")


class _RuijieAceExtIfAnyDestIp6VC_Type(TruthValue):
    """Custom type ruijieAceExtIfAnyDestIp6VC based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnyDestIp6VC_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnyDestIp6VC_Object = MibTableColumn
ruijieAceExtIfAnyDestIp6VC = _RuijieAceExtIfAnyDestIp6VC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 49),
    _RuijieAceExtIfAnyDestIp6VC_Type()
)
ruijieAceExtIfAnyDestIp6VC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnyDestIp6VC.setStatus("current")


class _RuijieAceExtDestIp6VC_Type(OctetString):
    """Custom type ruijieAceExtDestIp6VC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_RuijieAceExtDestIp6VC_Type.__name__ = "OctetString"
_RuijieAceExtDestIp6VC_Object = MibTableColumn
ruijieAceExtDestIp6VC = _RuijieAceExtDestIp6VC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 50),
    _RuijieAceExtDestIp6VC_Type()
)
ruijieAceExtDestIp6VC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtDestIp6VC.setStatus("current")


class _RuijieAceExtIfAnyDestIp6WildCardVC_Type(TruthValue):
    """Custom type ruijieAceExtIfAnyDestIp6WildCardVC based on TruthValue"""
    defaultValue = 1


_RuijieAceExtIfAnyDestIp6WildCardVC_Type.__name__ = "TruthValue"
_RuijieAceExtIfAnyDestIp6WildCardVC_Object = MibTableColumn
ruijieAceExtIfAnyDestIp6WildCardVC = _RuijieAceExtIfAnyDestIp6WildCardVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 51),
    _RuijieAceExtIfAnyDestIp6WildCardVC_Type()
)
ruijieAceExtIfAnyDestIp6WildCardVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtIfAnyDestIp6WildCardVC.setStatus("current")


class _RuijieAceExtDestIp6WildCardVC_Type(OctetString):
    """Custom type ruijieAceExtDestIp6WildCardVC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_RuijieAceExtDestIp6WildCardVC_Type.__name__ = "OctetString"
_RuijieAceExtDestIp6WildCardVC_Object = MibTableColumn
ruijieAceExtDestIp6WildCardVC = _RuijieAceExtDestIp6WildCardVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 1, 3, 1, 52),
    _RuijieAceExtDestIp6WildCardVC_Type()
)
ruijieAceExtDestIp6WildCardVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAceExtDestIp6WildCardVC.setStatus("current")
_RuijieAclVCMIBConformance_ObjectIdentity = ObjectIdentity
ruijieAclVCMIBConformance = _RuijieAclVCMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 2)
)
_RuijieAclVCMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieAclVCMIBCompliances = _RuijieAclVCMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 2, 1)
)
_RuijieAclVCMIBGroups_ObjectIdentity = ObjectIdentity
ruijieAclVCMIBGroups = _RuijieAclVCMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 2, 2)
)

# Managed Objects groups

ruijieAclVCMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 2, 2, 1)
)
ruijieAclVCMIBGroup.setObjects(
      *(("RUIJIE-ACL-CONTEXT-MIB", "ruijieAclContextNameVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAclNameVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAclModeVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAclEntryStatusVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtContextNameVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtAclNameVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtIndexVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtIfAnyVIDVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtVIDVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtIfAnySourceIpVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtSourceIpVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtIfAnySourceWildCardVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtSourceWildCardVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtIfAnySourceMacAddrVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtSourceMacAddrVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtIfAnyDestIpVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtDestIpVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtIfAnyDestWildCardVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtDestIpWildCardVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtIfAnyDestMacAddrVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtDestMacAddrVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtIfAnyEtherLikeTypeVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtEtherLikeTypeVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtIfAnyIpProtocolFieldVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtIpProtocolFieldVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtSourceProtocolPortVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtDestProtocolPortVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtProtocolTypeVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtProtocolTypeVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtFlowActionVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtEntryStautsVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtTimeRangeNameVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtSourcePortOpVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtSourceProtocolPortRangeVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtDestPortOpVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtDestProtocolPortRangeVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtIfAnyCosVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtCosVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtIfAnyIpPrecVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtIpPrecVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtIfAnyDscpVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtDscpVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtIfAnyTcpFlagVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtTcpFlagVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtIfAnySourceMacAddrWildCardVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtSourceMacAddrWildCardVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtIfAnyDestMacAddrWildCardVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtDestMacAddrWildCardVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtIfAnySourceIp6VC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtSourceIp6VC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtIfAnySourceIp6WildCardVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtSourceIp6WildCardVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtIfAnyDestIp6VC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtDestIp6VC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtIfAnyDestIp6WildCardVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAceExtDestIp6WildCardVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAclIfContextNameVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAclIfIndexVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAclIfMaxEntryNumVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAclIfCurruntEntryNumVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieIfInAclNameVC"),
        ("RUIJIE-ACL-CONTEXT-MIB", "ruijieIfOutAclNameVC"))
)
if mibBuilder.loadTexts:
    ruijieAclVCMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieAclVCMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 66, 2, 1, 1)
)
ruijieAclVCMIBCompliance.setObjects(
    ("RUIJIE-ACL-CONTEXT-MIB", "ruijieAclVCMIBGroup")
)
if mibBuilder.loadTexts:
    ruijieAclVCMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-ACL-CONTEXT-MIB",
    **{"ruijieAclVCMIB": ruijieAclVCMIB,
       "ruijieAclVCMIBObjects": ruijieAclVCMIBObjects,
       "ruijieAclVCTable": ruijieAclVCTable,
       "ruijieAclVCEntry": ruijieAclVCEntry,
       "ruijieAclContextNameVC": ruijieAclContextNameVC,
       "ruijieAclNameVC": ruijieAclNameVC,
       "ruijieAclModeVC": ruijieAclModeVC,
       "ruijieAclEntryStatusVC": ruijieAclEntryStatusVC,
       "ruijieAclIfVCTable": ruijieAclIfVCTable,
       "ruijieAclIfVCEntry": ruijieAclIfVCEntry,
       "ruijieAclIfContextNameVC": ruijieAclIfContextNameVC,
       "ruijieAclIfIndexVC": ruijieAclIfIndexVC,
       "ruijieAclIfMaxEntryNumVC": ruijieAclIfMaxEntryNumVC,
       "ruijieAclIfCurruntEntryNumVC": ruijieAclIfCurruntEntryNumVC,
       "ruijieIfInAclNameVC": ruijieIfInAclNameVC,
       "ruijieIfOutAclNameVC": ruijieIfOutAclNameVC,
       "ruijieAceExtVCTable": ruijieAceExtVCTable,
       "ruijieAceExtVCEntry": ruijieAceExtVCEntry,
       "ruijieAceExtContextNameVC": ruijieAceExtContextNameVC,
       "ruijieAceExtAclNameVC": ruijieAceExtAclNameVC,
       "ruijieAceExtIndexVC": ruijieAceExtIndexVC,
       "ruijieAceExtIfAnyVIDVC": ruijieAceExtIfAnyVIDVC,
       "ruijieAceExtVIDVC": ruijieAceExtVIDVC,
       "ruijieAceExtIfAnySourceIpVC": ruijieAceExtIfAnySourceIpVC,
       "ruijieAceExtSourceIpVC": ruijieAceExtSourceIpVC,
       "ruijieAceExtIfAnySourceWildCardVC": ruijieAceExtIfAnySourceWildCardVC,
       "ruijieAceExtSourceWildCardVC": ruijieAceExtSourceWildCardVC,
       "ruijieAceExtIfAnySourceMacAddrVC": ruijieAceExtIfAnySourceMacAddrVC,
       "ruijieAceExtSourceMacAddrVC": ruijieAceExtSourceMacAddrVC,
       "ruijieAceExtIfAnyDestIpVC": ruijieAceExtIfAnyDestIpVC,
       "ruijieAceExtDestIpVC": ruijieAceExtDestIpVC,
       "ruijieAceExtIfAnyDestWildCardVC": ruijieAceExtIfAnyDestWildCardVC,
       "ruijieAceExtDestIpWildCardVC": ruijieAceExtDestIpWildCardVC,
       "ruijieAceExtIfAnyDestMacAddrVC": ruijieAceExtIfAnyDestMacAddrVC,
       "ruijieAceExtDestMacAddrVC": ruijieAceExtDestMacAddrVC,
       "ruijieAceExtIfAnyEtherLikeTypeVC": ruijieAceExtIfAnyEtherLikeTypeVC,
       "ruijieAceExtEtherLikeTypeVC": ruijieAceExtEtherLikeTypeVC,
       "ruijieAceExtIfAnyIpProtocolFieldVC": ruijieAceExtIfAnyIpProtocolFieldVC,
       "ruijieAceExtIpProtocolFieldVC": ruijieAceExtIpProtocolFieldVC,
       "ruijieAceExtSourceProtocolPortVC": ruijieAceExtSourceProtocolPortVC,
       "ruijieAceExtDestProtocolPortVC": ruijieAceExtDestProtocolPortVC,
       "ruijieAceExtIfAnyProtocolTypeVC": ruijieAceExtIfAnyProtocolTypeVC,
       "ruijieAceExtProtocolTypeVC": ruijieAceExtProtocolTypeVC,
       "ruijieAceExtFlowActionVC": ruijieAceExtFlowActionVC,
       "ruijieAceExtEntryStautsVC": ruijieAceExtEntryStautsVC,
       "ruijieAceExtTimeRangeNameVC": ruijieAceExtTimeRangeNameVC,
       "ruijieAceExtSourcePortOpVC": ruijieAceExtSourcePortOpVC,
       "ruijieAceExtSourceProtocolPortRangeVC": ruijieAceExtSourceProtocolPortRangeVC,
       "ruijieAceExtDestPortOpVC": ruijieAceExtDestPortOpVC,
       "ruijieAceExtDestProtocolPortRangeVC": ruijieAceExtDestProtocolPortRangeVC,
       "ruijieAceExtIfAnyCosVC": ruijieAceExtIfAnyCosVC,
       "ruijieAceExtCosVC": ruijieAceExtCosVC,
       "ruijieAceExtIfAnyIpPrecVC": ruijieAceExtIfAnyIpPrecVC,
       "ruijieAceExtIpPrecVC": ruijieAceExtIpPrecVC,
       "ruijieAceExtIfAnyDscpVC": ruijieAceExtIfAnyDscpVC,
       "ruijieAceExtDscpVC": ruijieAceExtDscpVC,
       "ruijieAceExtIfAnyTcpFlagVC": ruijieAceExtIfAnyTcpFlagVC,
       "ruijieAceExtTcpFlagVC": ruijieAceExtTcpFlagVC,
       "ruijieAceExtIfAnySourceMacAddrWildCardVC": ruijieAceExtIfAnySourceMacAddrWildCardVC,
       "ruijieAceExtSourceMacAddrWildCardVC": ruijieAceExtSourceMacAddrWildCardVC,
       "ruijieAceExtIfAnyDestMacAddrWildCardVC": ruijieAceExtIfAnyDestMacAddrWildCardVC,
       "ruijieAceExtDestMacAddrWildCardVC": ruijieAceExtDestMacAddrWildCardVC,
       "ruijieAceExtIfAnySourceIp6VC": ruijieAceExtIfAnySourceIp6VC,
       "ruijieAceExtSourceIp6VC": ruijieAceExtSourceIp6VC,
       "ruijieAceExtIfAnySourceIp6WildCardVC": ruijieAceExtIfAnySourceIp6WildCardVC,
       "ruijieAceExtSourceIp6WildCardVC": ruijieAceExtSourceIp6WildCardVC,
       "ruijieAceExtIfAnyDestIp6VC": ruijieAceExtIfAnyDestIp6VC,
       "ruijieAceExtDestIp6VC": ruijieAceExtDestIp6VC,
       "ruijieAceExtIfAnyDestIp6WildCardVC": ruijieAceExtIfAnyDestIp6WildCardVC,
       "ruijieAceExtDestIp6WildCardVC": ruijieAceExtDestIp6WildCardVC,
       "ruijieAclVCMIBConformance": ruijieAclVCMIBConformance,
       "ruijieAclVCMIBCompliances": ruijieAclVCMIBCompliances,
       "ruijieAclVCMIBCompliance": ruijieAclVCMIBCompliance,
       "ruijieAclVCMIBGroups": ruijieAclVCMIBGroups,
       "ruijieAclVCMIBGroup": ruijieAclVCMIBGroup}
)
