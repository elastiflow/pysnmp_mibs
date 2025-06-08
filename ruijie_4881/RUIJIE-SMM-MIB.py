# SNMP MIB module (RUIJIE-SMM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-SMM-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:59:10 2025
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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ruijieSmmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 120)
)
if mibBuilder.loadTexts:
    ruijieSmmMIB.setRevisions(
        ("2012-12-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieSmmObjects_ObjectIdentity = ObjectIdentity
ruijieSmmObjects = _RuijieSmmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 120, 1)
)
_RuijieReportSimBillSwitch_Type = Unsigned32
_RuijieReportSimBillSwitch_Object = MibScalar
ruijieReportSimBillSwitch = _RuijieReportSimBillSwitch_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 120, 1, 1),
    _RuijieReportSimBillSwitch_Type()
)
ruijieReportSimBillSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieReportSimBillSwitch.setStatus("current")


class _RuijieQuerySimBillCmd_Type(OctetString):
    """Custom type ruijieQuerySimBillCmd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_RuijieQuerySimBillCmd_Type.__name__ = "OctetString"
_RuijieQuerySimBillCmd_Object = MibScalar
ruijieQuerySimBillCmd = _RuijieQuerySimBillCmd_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 120, 1, 2),
    _RuijieQuerySimBillCmd_Type()
)
ruijieQuerySimBillCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieQuerySimBillCmd.setStatus("current")
_RuijieSmsUseTable_Object = MibTable
ruijieSmsUseTable = _RuijieSmsUseTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 120, 1, 3)
)
if mibBuilder.loadTexts:
    ruijieSmsUseTable.setStatus("current")
_RuijieSmsUseEntry_Object = MibTableRow
ruijieSmsUseEntry = _RuijieSmsUseEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 120, 1, 3, 1)
)
ruijieSmsUseEntry.setIndexNames(
    (0, "RUIJIE-SMM-MIB", "ruijieSimImsi"),
)
if mibBuilder.loadTexts:
    ruijieSmsUseEntry.setStatus("current")


class _RuijieSimImsi_Type(DisplayString):
    """Custom type ruijieSimImsi based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RuijieSimImsi_Type.__name__ = "DisplayString"
_RuijieSimImsi_Object = MibTableColumn
ruijieSimImsi = _RuijieSimImsi_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 120, 1, 3, 1, 1),
    _RuijieSimImsi_Type()
)
ruijieSimImsi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSimImsi.setStatus("current")
_RuijieSmsUseCnt_Type = Unsigned32
_RuijieSmsUseCnt_Object = MibTableColumn
ruijieSmsUseCnt = _RuijieSmsUseCnt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 120, 1, 3, 1, 2),
    _RuijieSmsUseCnt_Type()
)
ruijieSmsUseCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSmsUseCnt.setStatus("current")
_RuijieSmmTrapObjects_ObjectIdentity = ObjectIdentity
ruijieSmmTrapObjects = _RuijieSmmTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 120, 2)
)
_RuijieSimBillTrapObjects_ObjectIdentity = ObjectIdentity
ruijieSimBillTrapObjects = _RuijieSimBillTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 120, 2, 1)
)


class _RuijieQuerySimBillContent_Type(OctetString):
    """Custom type ruijieQuerySimBillContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_RuijieQuerySimBillContent_Type.__name__ = "OctetString"
_RuijieQuerySimBillContent_Object = MibScalar
ruijieQuerySimBillContent = _RuijieQuerySimBillContent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 120, 2, 1, 1),
    _RuijieQuerySimBillContent_Type()
)
ruijieQuerySimBillContent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieQuerySimBillContent.setStatus("current")


class _RuijieReportSimBillContent_Type(OctetString):
    """Custom type ruijieReportSimBillContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_RuijieReportSimBillContent_Type.__name__ = "OctetString"
_RuijieReportSimBillContent_Object = MibScalar
ruijieReportSimBillContent = _RuijieReportSimBillContent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 120, 2, 1, 2),
    _RuijieReportSimBillContent_Type()
)
ruijieReportSimBillContent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieReportSimBillContent.setStatus("current")
_RuijieSmmTraps_ObjectIdentity = ObjectIdentity
ruijieSmmTraps = _RuijieSmmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 120, 3)
)
_RuijieSimBillNotifications_ObjectIdentity = ObjectIdentity
ruijieSimBillNotifications = _RuijieSimBillNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 120, 3, 1)
)

# Managed Objects groups


# Notification objects

ruijieQuerySimBill = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 120, 3, 1, 1)
)
ruijieQuerySimBill.setObjects(
    ("RUIJIE-SMM-MIB", "ruijieQuerySimBillContent")
)
if mibBuilder.loadTexts:
    ruijieQuerySimBill.setStatus(
        "current"
    )

ruijieReportSimBill = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 120, 3, 1, 2)
)
ruijieReportSimBill.setObjects(
    ("RUIJIE-SMM-MIB", "ruijieReportSimBillContent")
)
if mibBuilder.loadTexts:
    ruijieReportSimBill.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-SMM-MIB",
    **{"ruijieSmmMIB": ruijieSmmMIB,
       "ruijieSmmObjects": ruijieSmmObjects,
       "ruijieReportSimBillSwitch": ruijieReportSimBillSwitch,
       "ruijieQuerySimBillCmd": ruijieQuerySimBillCmd,
       "ruijieSmsUseTable": ruijieSmsUseTable,
       "ruijieSmsUseEntry": ruijieSmsUseEntry,
       "ruijieSimImsi": ruijieSimImsi,
       "ruijieSmsUseCnt": ruijieSmsUseCnt,
       "ruijieSmmTrapObjects": ruijieSmmTrapObjects,
       "ruijieSimBillTrapObjects": ruijieSimBillTrapObjects,
       "ruijieQuerySimBillContent": ruijieQuerySimBillContent,
       "ruijieReportSimBillContent": ruijieReportSimBillContent,
       "ruijieSmmTraps": ruijieSmmTraps,
       "ruijieSimBillNotifications": ruijieSimBillNotifications,
       "ruijieQuerySimBill": ruijieQuerySimBill,
       "ruijieReportSimBill": ruijieReportSimBill}
)
